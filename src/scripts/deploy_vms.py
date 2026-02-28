#!/usr/bin/env python3
"""
DEPRECATED — Kept for reference only.

This script was used in 2023-2024 when each student had an individual GCP VM.
Since 2024-2025 the course uses a shared GCP project where students create their
own resources, so pre-deploying VMs is no longer necessary.

A future teacher might still find this useful if reverting to the per-student VM
model or for bulk-creating VMs for a workshop.

Usage (if ever needed):
    python deploy_vms.py
"""

import subprocess
import shlex

# ── Configuration ──────────────────────────────────────────────────────────
# Replace these values for your year's project.
# 2023-2024 values (for reference):
#   GCP_PROJECT       = "sdd2324"
#   SERVICE_ACCOUNT   = "384413213440-compute@developer.gserviceaccount.com"
# ──────────────────────────────────────────────────────────────────────────

GCP_PROJECT = "<YOUR_GCP_PROJECT_ID>"
SERVICE_ACCOUNT = "<YOUR_SERVICE_ACCOUNT>"
ZONES = ["europe-west1-b", "europe-west4-a"]
MACHINE_TYPE = "n1-standard-1"
VM_IMAGE = "projects/ubuntu-os-cloud/global/images/ubuntu-2204-jammy-v20231030"
NUM_VMS = 64
VMS_PER_ZONE = NUM_VMS // len(ZONES)

base_cmd = """
gcloud compute instances create dev-instance-{index:02d} \
    --project={project} \
    --zone={zone} \
    --machine-type={machine_type} \
    --service-account={service_account} \
    --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append \
    --create-disk=auto-delete=yes,boot=yes,device-name=dev-instance-{index},image={image},mode=rw,size=10,type=projects/{project}/zones/{zone}/diskTypes/pd-standard \
    --reservation-affinity=any
"""

for index in range(NUM_VMS):
    zone = ZONES[0] if index < VMS_PER_ZONE else ZONES[1]

    gce_cmd = base_cmd.format(
        index=index,
        project=GCP_PROJECT,
        zone=zone,
        machine_type=MACHINE_TYPE,
        service_account=SERVICE_ACCOUNT,
        image=VM_IMAGE,
    )
    gce_cmd = shlex.split(gce_cmd)
    print(f"Creating VM {index:02d} in {zone}...")
    subprocess.check_call(gce_cmd)
