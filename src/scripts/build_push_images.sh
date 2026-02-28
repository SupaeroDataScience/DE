#!/bin/bash
# build_push_images.sh — Build and push ALL Docker images for the Data Computation module
#
# Usage:
#   bash build_push_images.sh <registry>
#   bash build_push_images.sh europe-docker.pkg.dev/isae-sdd-481407/isae-sdd-de-2526-docker
#
# This builds from the companion codespace repo (../isae-cloud-computing-codespace/ by default).
# Override with CODESPACE_REPO env var if your layout differs.
#
# 2025-2026 reference:
#   REGISTRY = europe-docker.pkg.dev/isae-sdd-481407/isae-sdd-de-2526-docker

set -euo pipefail

REGISTRY="${1:?Usage: bash build_push_images.sh <registry-path>}"
CODESPACE_REPO="${CODESPACE_REPO:-$(cd "$(dirname "$0")/../../.." && pwd)/../isae-cloud-computing-codespace}"

if [ ! -d "$CODESPACE_REPO" ]; then
    echo "ERROR: Companion repo not found at: $CODESPACE_REPO"
    echo "Set CODESPACE_REPO env var to the correct path."
    exit 1
fi

echo "=============================================="
echo "Docker Image Build & Push"
echo "=============================================="
echo "Registry:       ${REGISTRY}"
echo "Codespace repo: ${CODESPACE_REPO}"
echo "=============================================="
echo ""

# Ensure Docker is authenticated for Artifact Registry
echo "==> Configuring Docker authentication..."
REGISTRY_HOST=$(echo "$REGISTRY" | cut -d'/' -f1)
gcloud auth configure-docker "$REGISTRY_HOST" --quiet

# Track results
BUILT=()
FAILED=()

build_and_push() {
    local name="$1"
    local context="$2"
    local tag="${REGISTRY}/${name}"

    echo ""
    echo "==> Building ${name}..."
    if docker build -t "$tag" "$context"; then
        echo "==> Pushing ${name}..."
        if docker push "$tag"; then
            BUILT+=("$name")
            return 0
        fi
    fi
    FAILED+=("$name")
    return 1
}

# 1. Activation function demo
build_and_push "demo-streamlit-activation-function:1.0" "${CODESPACE_REPO}/be-docker-deploy" || true

# 2. YOLO backend + frontend
build_and_push "yolo-v11-backend:1.0" "${CODESPACE_REPO}/be-ml-deployment/backend" || true
build_and_push "yolo-v11-frontend:1.0" "${CODESPACE_REPO}/be-ml-deployment/frontend" || true

# 3. Mascots (Build-Ship-Run workshop)
MASCOTS=(cat dog owl panda yoda)
for mascot in "${MASCOTS[@]}"; do
    build_and_push "webapp-gif:${mascot}-1.0" "${CODESPACE_REPO}/teacher/mascots/${mascot}" || true
done

# Summary
echo ""
echo "=============================================="
echo "Summary"
echo "=============================================="
echo "Built & pushed: ${#BUILT[@]}"
for img in "${BUILT[@]}"; do
    echo "  OK  ${img}"
done
if [ ${#FAILED[@]} -gt 0 ]; then
    echo "Failed: ${#FAILED[@]}"
    for img in "${FAILED[@]}"; do
        echo "  FAIL  ${img}"
    done
    echo ""
    echo "Fix failures and re-run. Successfully pushed images are idempotent."
    exit 1
fi
echo ""
echo "All images built and pushed successfully!"
