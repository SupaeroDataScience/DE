#!/usr/bin/env bash
# Open firewall ports required for student exercises on a GCP project.
#
# Ports:
#   8081 - Various web apps (Flask, FastAPI dev servers)
#   8501 - Streamlit default port
#
# Usage:
#   bash open_port.sh <project-id>
#   bash open_port.sh isae-sdd-481407    # 2025-2026 project

set -euo pipefail

PROJECT_ID="${1:?Usage: $0 <project-id>}"

echo "Opening firewall ports on project: ${PROJECT_ID}"

gcloud compute --project="${PROJECT_ID}" firewall-rules create open-8081 \
    --direction=INGRESS \
    --priority=1000 \
    --network=default \
    --action=ALLOW \
    --rules=tcp:8081 \
    --source-ranges=0.0.0.0/0

gcloud compute --project="${PROJECT_ID}" firewall-rules create open-8501 \
    --direction=INGRESS \
    --priority=1000 \
    --network=default \
    --action=ALLOW \
    --rules=tcp:8501 \
    --source-ranges=0.0.0.0/0

echo "Done. Ports 8081 and 8501 are now open."
