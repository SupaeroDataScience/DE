#!/usr/bin/env python3
"""
Sync email addresses from a Google Sheet to GCP project IAM as editors.

Prerequisites:
1. Authenticate with gcloud: gcloud auth login
2. The Google Sheet must be accessible (public or shared with you)

Usage:
    python sync_gcp_editors.py [--dry-run]

Options:
    --dry-run    Show what would be done without making changes
"""

import argparse
import csv
import io
import json
import re
import subprocess
import sys
import urllib.request
import urllib.error


# ── Replace these values each year ──────────────────────────────────────────
# 2025-2026 values (for reference):
#   SPREADSHEET_ID = "1T4SsMQtn4ZZvVio2q73eHi2tKvj00YXtWPK7LOF4LBg"
#   GCP_PROJECT    = "isae-sdd-481407"
# ────────────────────────────────────────────────────────────────────────────
SPREADSHEET_ID = "<YOUR_SPREADSHEET_ID>"
GCP_PROJECT = "<YOUR_GCP_PROJECT_ID>"
IAM_ROLE = "roles/editor"
EMAIL_COLUMN = 2  # 0-indexed, so column 3

EMAIL_REGEX = re.compile(r"[a-zA-Z0-9._%+-]+@gmail\.com", re.IGNORECASE)


def get_emails_from_sheet() -> set[str]:
    """Fetch all email addresses from the Google Sheet via CSV export."""
    print(f"Fetching emails from Google Sheet: {SPREADSHEET_ID}")

    # Export URL for first sheet (gid=0)
    export_url = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/export?format=csv&gid=0"

    try:
        with urllib.request.urlopen(export_url) as response:
            content = response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        if e.code == 403:
            raise PermissionError(
                "Cannot access the spreadsheet. Make sure it's shared publicly or with your account."
            )
        raise

    emails = set()
    reader = csv.reader(io.StringIO(content))
    for row in reader:
        if len(row) > EMAIL_COLUMN:
            cell = row[EMAIL_COLUMN]
            if cell:
                # Find Gmail addresses in column 3
                found = EMAIL_REGEX.findall(cell.strip())
                emails.update(email.lower() for email in found)

    print(f"  Found {len(emails)} unique Gmail address(es) in spreadsheet")
    return emails


def get_current_editors_and_owners(project: str) -> set[str]:
    """Get current editor and owner emails from GCP project IAM."""
    print(f"Fetching current IAM bindings for project: {project}")

    result = subprocess.run(
        ["gcloud", "projects", "get-iam-policy", project, "--format=json"],
        capture_output=True,
        text=True,
        check=True,
    )

    policy = json.loads(result.stdout)

    users = set()
    roles_to_check = {"roles/editor", "roles/owner"}
    for binding in policy.get("bindings", []):
        if binding.get("role") in roles_to_check:
            for member in binding.get("members", []):
                if member.startswith("user:"):
                    email = member.replace("user:", "").lower()
                    users.add(email)

    print(f"  Found {len(users)} current editor(s)/owner(s)")
    return users


def add_editor(project: str, email: str, dry_run: bool = False) -> bool:
    """Add an email as editor to the GCP project."""
    member = f"user:{email}"

    if dry_run:
        print(f"  [DRY-RUN] Would add: {email}")
        return True

    print(f"  Adding: {email}")
    try:
        subprocess.run(
            [
                "gcloud", "projects", "add-iam-policy-binding", project,
                f"--member={member}",
                f"--role={IAM_ROLE}",
                "--quiet",
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"    ERROR: Failed to add {email}: {e.stderr}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Sync Google Sheet emails to GCP project IAM as editors"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )
    args = parser.parse_args()

    if args.dry_run:
        print("=== DRY RUN MODE ===\n")

    # Get emails from sheet
    try:
        sheet_emails = get_emails_from_sheet()
    except Exception as e:
        print(f"ERROR: Failed to fetch emails from Google Sheet: {e}")
        print("\nMake sure you have authenticated:")
        print("  gcloud auth application-default login")
        sys.exit(1)

    if not sheet_emails:
        print("No emails found in spreadsheet. Exiting.")
        sys.exit(0)

    # Get current editors and owners
    try:
        current_users = get_current_editors_and_owners(GCP_PROJECT)
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Failed to get IAM policy: {e.stderr}")
        print("\nMake sure you have authenticated and have permissions:")
        print("  gcloud auth login")
        sys.exit(1)

    # Find emails to add (not already editor or owner)
    emails_to_add = sheet_emails - current_users

    print(f"\n=== Summary ===")
    print(f"Gmail addresses in spreadsheet: {len(sheet_emails)}")
    print(f"Current editors/owners: {len(current_users)}")
    print(f"Emails to add: {len(emails_to_add)}")

    if not emails_to_add:
        print("\nAll emails are already editors or owners. Nothing to do.")
        return

    print(f"\n=== Adding {len(emails_to_add)} email(s) as editors ===")

    success_count = 0
    for email in sorted(emails_to_add):
        if add_editor(GCP_PROJECT, email, dry_run=args.dry_run):
            success_count += 1

    print(f"\n=== Done ===")
    if args.dry_run:
        print(f"Would add {success_count} email(s)")
    else:
        print(f"Successfully added {success_count}/{len(emails_to_add)} email(s)")


if __name__ == "__main__":
    main()
