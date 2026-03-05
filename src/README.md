# Data Computation Module — Teacher Handover

Last updated: 2025-2026 edition (January 2026).

This document is a self-contained handover for the **Data Computation** module of the ISAE-Supaero Data Engineering Master's course. It covers infrastructure setup, session-by-session checklists, year-to-year update instructions, and known issues.

Course website: <https://supaerodatascience.github.io/DE/>

---

## 1. Quick Start (TL;DR)

Before the first session, at minimum:

1. **GCP project** — Have a shared GCP project with billing enabled (2025-2026: `isae-sdd-481407`).
2. **Student access** — Create a Google Form/Sheet to collect student Gmail addresses; run `sync_gcp_editors.py` to grant Editor access.
3. **Codespace repo** — Verify <https://github.com/fchouteau/isae-cloud-computing-codespace> is public and the devcontainer builds.
4. **GCS bucket** — Create the shared bucket (2025-2026: `gs://isae-sdd-de-2526`).
5. **Artifact Registry** — Create a Docker Artifact Registry repo (2025-2026: `isae-sdd-de-2526-docker` in `europe`).
6. **Docker images** — Build and push the pre-built images (YOLO backend/frontend, activation-function demo, BE mascots).
7. **Firewall rules** — Run `open_port.sh <project-id>` to open ports 8081 and 8501.
8. **Slides & site** — Run `make all` from `src/` and verify the site builds.
9. **Year-specific values** — Grep for last year's project ID and update (see Section 4).
10. **Slack channel** — Set up a Slack channel for student communication.

---

## 2. Infrastructure Setup

### 2A. GCP Shared Project

#### Pre-class setup

Do this **at least 1-2 weeks before class** — quota increases and org policy changes can take time.

##### Step 1: Project & Billing

1. **Create or reuse a GCP project.** Naming convention: `isae-sdd-YYMMDD` or similar. 2025-2026 used `isae-sdd-481407`.
2. **Enable billing** with a billing account (ISAE provides educational credits or use a coupon).
3. **Set a budget alert** to avoid surprise charges:
   ```bash
   # Via console: Billing → Budgets & alerts → Create budget
   # Set alerts at 50%, 80%, 100% of expected spend
   ```

##### Step 2: Enable APIs

All APIs used during the course:

```bash
gcloud services enable \
    compute.googleapis.com \
    storage.googleapis.com \
    artifactregistry.googleapis.com \
    run.googleapis.com \
    cloudbuild.googleapis.com \
    iam.googleapis.com
```

Verify they're enabled:

```bash
gcloud services list --enabled --filter="NAME:(compute OR storage OR artifactregistry OR run OR cloudbuild OR iam)"
```

##### Step 3: Check and increase quotas

Default quotas are too low for 60 students creating VMs simultaneously. Go to [IAM & Admin → Quotas](https://console.cloud.google.com/iam-admin/quotas) and check:

| Quota | Default | Needed (60 students) | Notes |
|-------|---------|---------------------|-------|
| **CPUs per region** (Compute Engine) | 8-24 | ≥ 130 | 60 students × 2 vCPUs + buffer |
| **VM instances per region** | 8-10 | ≥ 70 | One VM per student + buffer |
| **In-use external IP addresses per region** | 8 | ≥ 70 | Each VM gets an external IP |
| **Persistent Disk Standard (GB) per region** | 2048 | ≥ 4000 | 60 × 50GB boot disks |
| **Cloud Run services per region** | 100 | OK as-is | 60 students is within default |
| **Firewall rules per project** | 100 | OK as-is | We only create 2-3 |

Request increases for the region(s) you use. 2025-2026 used `europe-west9`. If that region has limited availability, `europe-west1` or `europe-west4` are good alternatives.

**Quota increases take minutes to hours.** For large increases (>10× default), Google may take a few days and may ask for justification — mention educational use.

##### Step 4: Check organization policies

If the project lives under a GCP Organization (e.g., ISAE's org), org-level policies may block student actions. Check and request exceptions if needed:

| Policy | Risk | How to check |
|--------|------|-------------|
| `constraints/compute.vmExternalIpAccess` | May block students from creating VMs with external IPs | `gcloud resource-manager org-policies describe compute.vmExternalIpAccess --project=<project>` |
| `constraints/iam.allowedPolicyMemberDomains` | May block adding `@gmail.com` accounts as project members | Check if only `@isae-supaero.fr` is allowed |
| `constraints/run.allowedIngress` | May block `--allow-unauthenticated` on Cloud Run | `gcloud resource-manager org-policies describe run.allowedIngress --project=<project>` |
| `constraints/compute.restrictLoadBalancerCreationForTypes` | Rarely an issue, but check if load balancers are restricted | Usually fine for the exercises |

If the project is **not** under an organization (standalone project), these don't apply.

##### Step 5: Verify networking

1. **Default VPC network must exist.** New projects have one, but if someone deleted it:
   ```bash
   gcloud compute networks list
   # Should show "default" network. If missing:
   gcloud compute networks create default --subnet-mode=auto
   ```
2. **Open firewall ports** for student exercises:
   ```bash
   bash scripts/open_port.sh <project-id>
   ```
   This creates rules for ports 8081 (Flask/FastAPI) and 8501 (Streamlit).
3. **Verify firewall rule for Container-Optimized OS deployments:**
   ```bash
   # The open_port.sh script creates general rules.
   # For the deployment workshop, VMs use --tags=http-server-8501
   # which matches the firewall rule targeting that tag.
   gcloud compute firewall-rules list --filter="allowed[].ports:8501"
   ```

##### Step 6: Create shared storage

1. **GCS bucket** (used in the GCP ML Workflow workshop):
   ```bash
   gcloud storage buckets create gs://isae-sdd-de-YYMM --location=europe-west9 --uniform-bucket-level-access
   # 2025-2026: gs://isae-sdd-de-2526
   ```
2. **Artifact Registry Docker repo** (see Section 2C for details):
   ```bash
   gcloud artifacts repositories create isae-sdd-de-YYMM-docker \
       --repository-format=docker --location=europe
   ```

##### Step 7: IAM — Grant student access

1. **Collect student Gmail addresses** via a Google Form linked to a Google Sheet.
   - The sheet must be publicly readable (or shared with your account).
   - Gmail column must be column 3 (0-indexed: 2). Adjust `EMAIL_COLUMN` in `sync_gcp_editors.py` if needed.
2. **Choose a permission strategy:**

   **Option A: Editor role (simple, used in 2025-2026)**

   Quick and easy — one role covers everything. Downside: students can also modify IAM, delete the Artifact Registry, change billing, etc.
   ```bash
   # sync_gcp_editors.py uses this by default (IAM_ROLE = "roles/editor")
   python scripts/sync_gcp_editors.py --dry-run
   python scripts/sync_gcp_editors.py
   ```

   **Option B: Least-privilege custom roles (recommended if you have time)**

   Grant only what students actually need for the exercises:

   | Role | Why | Used in |
   |------|-----|---------|
   | `roles/compute.instanceAdmin.v1` | Create, SSH into, and delete VMs | GCP hands-on, ML workflow, deployment |
   | `roles/storage.objectAdmin` | Read/write objects in GCS buckets | ML workflow (upload/download results) |
   | `roles/artifactregistry.writer` | Push and pull Docker images | Docker workshop, ML deployment |
   | `roles/run.developer` | Deploy and manage Cloud Run services | ML deployment |
   | `roles/iam.serviceAccountUser` | Use the default compute service account when creating VMs/Cloud Run | All compute tasks |
   | `roles/serviceusage.serviceUsageConsumer` | Use enabled APIs | All tasks |

   Grant all at once:
   ```bash
   ROLES=(
     roles/compute.instanceAdmin.v1
     roles/storage.objectAdmin
     roles/artifactregistry.writer
     roles/run.developer
     roles/iam.serviceAccountUser
     roles/serviceusage.serviceUsageConsumer
   )
   for email in $(python scripts/sync_gcp_editors.py --dry-run 2>/dev/null | grep "Would add" | awk '{print $NF}'); do
     for role in "${ROLES[@]}"; do
       gcloud projects add-iam-policy-binding <project-id> \
         --member="user:${email}" --role="${role}" --quiet
     done
   done
   ```

   To use Option B with `sync_gcp_editors.py`, change `IAM_ROLE` to each role and run it multiple times, or modify the script to loop over roles.

   **What neither option gives:** `--allow-unauthenticated` on Cloud Run requires `roles/run.admin` or manual intervention — see Section 7. Keep this as a teacher-only action.

##### Step 8: Smoke-test everything

Before class, run through the student workflow yourself:

- [ ] Create a Codespace from the repo and run `install.sh`
- [ ] `gcloud init` inside Codespace, verify project access
- [ ] Create a VM: `gcloud compute instances create test-vm --zone=europe-west9-a --machine-type=e2-small`
- [ ] SSH into it: `gcloud compute ssh test-vm --zone=europe-west9-a`
- [ ] Upload to GCS: `echo test | gcloud storage cp - gs://isae-sdd-de-YYMM/test.txt`
- [ ] Pull a Docker image: `docker pull europe-docker.pkg.dev/<project>/<repo>/demo-streamlit-activation-function:1.0`
- [ ] Deploy to Cloud Run: `gcloud run deploy test --image=... --region=europe-west9 --allow-unauthenticated`
- [ ] Clean up all test resources

If any step fails, fix it before class. Students hitting infra issues wastes precious class time.

#### During the course

- **Monitor billing** daily during class weeks via [Billing → Reports](https://console.cloud.google.com/billing/).
- **Monitor active VMs:** `gcloud compute instances list` — remind students to delete after each session.
- If a student can't access the project, re-run `sync_gcp_editors.py` or manually add them:
  ```bash
  gcloud projects add-iam-policy-binding <project> --member="user:student@gmail.com" --role="roles/editor"
  ```
- For Cloud Run `--allow-unauthenticated` issues, manually grant public access (see Section 7).
- **If quota is exhausted mid-class:** Have students pair up, or use a secondary region as fallback.

#### Post-class cleanup

1. **Delete all student VMs:**
   ```bash
   gcloud compute instances list --project=<project>
   # Bulk delete (careful — lists ALL VMs):
   gcloud compute instances list --format="value(name,zone)" | while read name zone; do
     gcloud compute instances delete "$name" --zone="$zone" --quiet
   done
   ```
2. **Delete Cloud Run services:**
   ```bash
   gcloud run services list --region=europe-west9 --format="value(name)" | while read name; do
     gcloud run services delete "$name" --region=europe-west9 --quiet
   done
   ```
3. **Empty and optionally delete the GCS bucket.**
4. **Clean up Artifact Registry** (optional — images don't cost much for storage):
   ```bash
   gcloud artifacts docker images list europe-docker.pkg.dev/<project>/<repo>
   ```
5. **Remove student IAM bindings** (or delete the project entirely if you're done).
6. **Verify no recurring charges** a week later via the billing dashboard.

### 2B. GitHub Codespace Repository

**Repository:** <https://github.com/fchouteau/isae-cloud-computing-codespace>

#### Ownership model

The codespace repo is a **separate git repository** from the course website repo (`isae-data-engineering`). The teacher must have **push access** to update it each year.

**Local layout:** When developing, the two repos live side-by-side:

```
your-workspace/
├── isae-data-engineering/              # This repo (course website + teacher handover)
│   └── src/scripts/                    # Teacher scripts
└── isae-cloud-computing-codespace/     # Companion repo (student exercises)
    ├── teacher/                        # Teacher build infra (mascots, image scripts)
    └── be-*/tp-*/                      # Student exercise folders
```

Scripts in `src/scripts/` reference the companion repo as `../isae-cloud-computing-codespace/` (relative to the main repo root).

**To transfer to a new teacher:**

1. Add the new teacher as a collaborator (or transfer repo ownership) on GitHub.
2. The new teacher forks or clones the repo.
3. Update all references to `fchouteau/isae-cloud-computing-codespace` in course docs (see Section 4).
4. The new teacher updates the codespace repo URL in `src/docs/1_2c_handson_codespace.md`.

This repo is the students' development environment. It contains:

| Folder | Purpose |
|--------|---------|
| `tp-codespace-train-local/` | Session 1: Codespace + ML training exercise |
| `tp-docker-cli-app/` | Session 2: Docker CLI app (volume mounts) |
| `be-docker-build-ship-run/` | Day 2 morning: Team Docker workshop (Build-Ship-Run) |
| `be-docker-deploy/` | Day 2 morning: Container deployment to GCE |
| `be-cloud-computing/` | Day 2 morning: GCP ML workflow (GCE + GCS) |
| `be-ml-deployment/` | Day 2 afternoon: ML deployment (YOLO, Cloud Run) |
| `.devcontainer/` | Codespace configuration |
| `install.sh` | Post-start hook (installs gcloud CLI, etc.) |

**Key risks:**

- If the repo is private, students cannot create Codespaces. Keep it **public**.
- The `install.sh` script runs on every Codespace start. If it breaks (e.g., gcloud installer URL changes), students are stuck. Test it before class.
- GitHub gives 60 free CPU-hours/month per student. Remind students to **stop their Codespace** when done.
- The devcontainer requests 4 CPUs (`hostRequirements.cpus: 4`).

### 2C. Docker Images / Artifact Registry

Create an Artifact Registry Docker repository:

```bash
gcloud artifacts repositories create isae-sdd-de-2526-docker \
    --repository-format=docker \
    --location=europe \
    --description="ISAE SDD Data Engineering Docker images"
```

Images to build and push (from the codespace repo):

| Image | Source folder | Used in |
|-------|--------------|---------|
| `demo-streamlit-activation-function:1.0` | `be-docker-deploy/` | Docker deployment workshop |
| `yolo-v11-backend:1.0` | `be-ml-deployment/backend/` | ML deployment workshop |
| `yolo-v11-frontend:1.0` | `be-ml-deployment/frontend/` | ML deployment workshop |
| `{group}-{mascot}:1.0` (5 mascots) | `be-docker-build-ship-run/{mascot}/` | Build-Ship-Run workshop (students build these, but have pre-built backups) |

Build and push pattern:

```bash
REGISTRY="europe-docker.pkg.dev/isae-sdd-481407/isae-sdd-de-2526-docker"

# Example: activation function demo
cd be-docker-deploy
docker build -t ${REGISTRY}/demo-streamlit-activation-function:1.0 .
docker push ${REGISTRY}/demo-streamlit-activation-function:1.0

# Example: YOLO backend
cd be-ml-deployment/backend
docker build -t ${REGISTRY}/yolo-v11-backend:1.0 .
docker push ${REGISTRY}/yolo-v11-backend:1.0
```

Authenticate Docker first: `gcloud auth configure-docker europe-docker.pkg.dev`

### 2D. Course Content & Links

Files containing year-specific values (project IDs, bucket names, registry paths):

| File | Values to check |
|------|-----------------|
| `src/docs/1_2b_handson_setup.md` | Project setup instructions, form link |
| `src/docs/1_4a_gcp_workflow.md` | GCS bucket name (`gs://isae-sdd-de-2526`), zone |
| `src/docs/1_4b_docker_workflow.md` | Artifact Registry path (`europe-docker.pkg.dev/isae-sdd-481407/isae-sdd-de-2526-docker`) |
| `src/docs/1_4c_deployment_workflow.md` | Same Artifact Registry path, project ID in `gcloud` commands |
| `src/docs/1_5b_deployment_be.md` | Artifact Registry path, project ID in `gcloud run deploy` |
| `src/docs/1_2c_handson_codespace.md` | Codespace repo URL (`fchouteau/isae-cloud-computing-codespace`) |
| Codespace: `be-ml-deployment/docker-compose.yml` | Artifact Registry image paths |

External links to verify each year:

- [ ] <https://supaerodatascience.github.io/DE/> (course website)
- [ ] <https://github.com/fchouteau/isae-cloud-computing-codespace> (codespace repo)
- [ ] Docker Hub images used in hands-on: `dockersamples/static-site`, `alpine:3.18`
- [ ] GCS public assets: `gs://fchouteau-isae-cloud/` (mascot gifs, BE resources)
- [ ] Streamlit video URL in `1_2c_handson_codespace.md`

### 2E. Building & Deploying the Course Website

The course website is at <https://supaerodatascience.github.io/DE/>. It's built from `src/` in this repo and deployed to the `gh-pages` branch.

#### Prerequisites

Install these tools (once):

```bash
pip install mkdocs mkdocs-material    # Site generator + theme
npm install -g reveal-md              # Slide generator (Reveal.js)
```

#### Local preview

From the `src/` directory:

```bash
make serve-site     # Build slides into docs/slides/, then serve MkDocs with live reload
                    # → http://localhost:8000

make serve-slides   # Serve reveal.js slides only (hot reload, no MkDocs)
                    # → http://localhost:1948
```

`make serve-site` does two things in sequence: first builds slides with `reveal-md` into `docs/slides/`, then starts `mkdocs serve`. The slides are embedded in the MkDocs site via iframes.

#### Production build

```bash
make all            # Build both slides and site into site/ directory (for CI or manual upload)
```

#### Deploying to GitHub Pages

```bash
make deploy REMOTE=supaero   # Build and deploy to gh-pages in one step
```

**What `make deploy` does:**

1. Runs `mkdocs build` → builds the site into `site/`
2. Runs `reveal-md` → builds slides directly into `site/slides/`
3. Runs `ghp-import` → commits the entire `site/` directory to `gh-pages` and pushes

No branch checkouts are performed — your working tree is never touched. This uses `ghp-import` (the same tool `mkdocs gh-deploy` uses internally) to force-push to `gh-pages` without checking it out.

**Important variables** (in `src/Makefile`):

| Variable | Default | Purpose |
|----------|---------|---------|
| `REMOTE` | `origin` | Git remote to push to |

Override if needed: `make deploy REMOTE=supaero`

---

## 3. Session Checklists

### Session 1: Cloud Computing & Codespaces (3h)

**Schedule:**

| Time | Activity | Materials |
|------|----------|-----------|
| 0:00-0:45 | Lecture: Intro + Cloud Computing | Slides `1_1_data_computation`, `1_2a_cloud_computing`, `1_2b_cloud_handson` |
| 0:45-1:00 | Setup: GCP accounts + Gmail collection | `1_2b_handson_setup.md` |
| 1:00-2:00 | Hands-on: Codespace exploration | `1_2c_handson_codespace.md` |
| 2:00-3:00 | Hands-on: GCP (gcloud, VMs, GCS) | `1_2d_handson_gcp.md` |

**Pre-session checklist:**

- [ ] GCP project created and billing enabled
- [ ] Google Form/Sheet for Gmail collection ready
- [ ] `sync_gcp_editors.py` tested with `--dry-run`
- [ ] Codespace repo accessible and devcontainer builds
- [ ] Slides built: `cd src && make serve-slides` to verify
- [ ] Slack channel set up for student questions

**During-session notes:**

- Students need to create Codespace FIRST, then configure gcloud inside it.
- The `gcloud init` step inside Codespace requires browser auth — students open the URL, authenticate, paste the code back.
- Students joining a shared project (Option A) only need their Gmail added. Option B (individual projects) requires credit coupons.
- Remind students to stop Codespace at end of session.

**Key gotchas:**

- ISAE wifi (`isae-edu`) blocks many ports. **eduroam** or **4G** is required for VM SSH and port forwarding.
- Some students may not have a Gmail address — they need to create one.
- If `install.sh` fails on Codespace start, have students run it manually: `chmod +x install.sh && ./install.sh`

### Session 2: Docker (3h)

**Schedule:**

| Time | Activity | Materials |
|------|----------|-----------|
| 0:00-0:45 | Lecture: Containers & Docker | Slides `1_3a_containers`, `1_3b_docker_cheatsheet` |
| 0:45-2:15 | Hands-on: Docker basics, Dockerfiles, Flask app, CLI app | `1_3b_handson_docker.md` |
| 2:15-3:00 | Hands-on: Container Registry (Artifact Registry push) | `1_3b_handson_docker.md` §4 |

**Pre-session checklist:**

- [ ] Artifact Registry Docker repo created
- [ ] Students have Codespace from Session 1 (or can create new one)
- [ ] Verify `alpine:3.18` is pullable (Docker Hub uptime)

**During-session notes:**

- Students build a Flask cat-gif app and a Typer CLI app.
- The CLI app exercise uses volume mounts — students often confuse host paths vs container paths.
- Pushing to Artifact Registry requires `gcloud auth configure-docker europe-docker.pkg.dev`.

**Key gotchas:**

- **Alpine 3.18 is pinned** in the Dockerfile example. Alpine 3.20+ changed how pip works (PEP 668 externally-managed environments). If you update to a newer Alpine, students will get `error: externally-managed-environment`. Stick with `alpine:3.18` or add `--break-system-packages` flag.
- Students may run out of Codespace disk if they pull many images. `docker system prune` helps.

### Day 2 Morning: GCP ML Workflow + Docker Workshops (3h)

**Schedule:**

| Time | Activity | Materials |
|------|----------|-----------|
| 0:00-0:15 | Lecture: Putting it all together | Slides `1_4_be` |
| 0:15-1:15 | Workshop: GCP ML Workflow (GCE + GCS) | `1_4a_gcp_workflow.md` |
| 1:15-2:15 | Workshop: Docker Build-Ship-Run (teams) | `1_4b_docker_workflow.md` |
| 2:15-3:00 | Workshop: Docker Deployment to GCE | `1_4c_deployment_workflow.md` |

**Pre-session checklist:**

- [ ] GCS bucket `gs://isae-sdd-de-2526` created and accessible by students
- [ ] Mascot resources uploaded to `gs://fchouteau-isae-cloud/be/` (cat, dog, owl, panda, yoda)
- [ ] Pre-built Docker images pushed to Artifact Registry (activation-function demo, mascots as backup)
- [ ] Firewall rule for port 8501 exists (`open_port.sh` run)
- [ ] **Critical:** Tell students to create a FRESH Codespace (the exercises expect clean state)

**During-session notes:**

- GCP ML Workflow: Students create VMs, run PyTorch training, upload to GCS, delete VMs. **Hammer the "delete your VM" message.**
- Build-Ship-Run: Teams of 2-5. Each member picks a mascot, builds, pushes, then pulls a teammate's image. The fun is seeing each other's mascots.
- Deployment: Students deploy the activation-function Streamlit app to a GCE VM with Container-Optimized OS.

**Key gotchas:**

- VMs in `europe-west9-a` — startup script takes ~2 minutes. Students get impatient and SSH too early, then `python` isn't found (venv not ready).
- The Build-Ship-Run exercise needs coordination — wait for everyone to push before starting the "RUN" phase.
- `gcloud compute ssh` may prompt for OS Login setup on first use.

### Day 2 Afternoon: ML Deployment (3h)

**Schedule:**

| Time | Activity | Materials |
|------|----------|-----------|
| 0:00-0:30 | Lecture: Deployment & APIs | Slides `1_5_deployment` |
| 0:30-1:30 | Hands-on: Backend + Frontend locally | `1_5b_deployment_be.md` §3-4 |
| 1:30-2:00 | Hands-on: docker-compose | `1_5b_deployment_be.md` §5 |
| 2:00-2:45 | Hands-on: Cloud Run deployment | `1_5b_deployment_be.md` §6 |
| 2:45-3:00 | Conclusion + cleanup | Slides `1_6_conclusion` |

**Pre-session checklist:**

- [ ] YOLO backend and frontend images pushed to Artifact Registry
- [ ] Test Cloud Run deployment yourself first to verify it works with current quotas/permissions
- [ ] Prepare to manually grant `allUsers` → `roles/run.invoker` for students who hit the auth error

**During-session notes:**

- Students run backend (port 8000) and frontend (port 8501) as separate containers.
- The `--network="host"` flag is needed for local frontend→backend communication, but NOT for Cloud Run.
- docker-compose uses hostnames (`http://yolo:8000`) not `localhost`. Students forget this.
- Cloud Run deployment takes 2-3 minutes. The `--memory=4Gi` flag is required for YOLO.

**Key gotchas:**

- **Cloud Run `--allow-unauthenticated`** requires the `roles/run.admin` permission (or `roles/iam.serviceAccountUser`). The Editor role is NOT sufficient. You will need to either:
  - Grant students `roles/run.admin` (risky), or
  - Manually make each student's service public via the console or CLI.
  - See the instructions in `1_5b_deployment_be.md` §6 for the exact `gcloud run services add-iam-policy-binding` command.
- Students MUST clean up Cloud Run services at the end. Cloud Run bills per request + idle instances.

---

## 4. What to Update for Next Year

### Scenario A: Reuse the same GCP project

If you keep `isae-sdd-481407`:

1. Create a new GCS bucket with the new year suffix.
2. Create a new Artifact Registry repo with the new year suffix.
3. Rebuild and push Docker images to the new registry.
4. Update all course content with new bucket/registry names (see table below).
5. Re-run `sync_gcp_editors.py` with the new spreadsheet.

### Scenario B: Create a new GCP project

1. Create a new project, enable APIs (see Section 2A).
2. Open firewall ports: `bash scripts/open_port.sh <new-project-id>`
3. Update all references to the old project ID.

### Finding values to replace

```bash
# From the repo root, find all references to 2025-2026 values in course content:
grep -rn "isae-sdd-481407\|isae-sdd-de-2526\|sdd2526\|fchouteau/isae-cloud-computing-codespace" src/docs/ src/reveal/

# Also search the companion repo for year-specific values:
grep -rn "isae-sdd-481407\|isae-sdd-de-2526\|sdd2526\|fchouteau" ../isae-cloud-computing-codespace/
```

**Companion repo files with year-specific values:**

| File | Values |
|------|--------|
| `be-ml-deployment/docker-compose.yml` | Full Artifact Registry path (project ID + repo name) |
| `be-ml-deployment/backend/Makefile` | Full Artifact Registry path |
| `be-ml-deployment/frontend/Makefile` | Full Artifact Registry path |
| `be-cloud-computing/train_remote.sh` | GCS bucket (`GCS_BUCKET` variable at top of file) |
| `teacher/mascots/build_all.sh` | Registry path (`REGISTRY` variable) |
| `teacher/mascots/push_all.sh` | Registry path (`REGISTRY` variable) |

### Value replacement table

| Old value (2025-2026) | What it is | Replace with |
|----------------------|------------|--------------|
| `isae-sdd-481407` | GCP project ID | New project ID |
| `isae-sdd-de-2526` | GCS bucket suffix | New year suffix (e.g., `isae-sdd-de-2627`) |
| `isae-sdd-de-2526-docker` | Artifact Registry repo name | New year suffix |
| `gs://isae-sdd-de-2526` | GCS bucket URL | New bucket URL |
| `europe-docker.pkg.dev/isae-sdd-481407/isae-sdd-de-2526-docker` | Full Artifact Registry path | Updated project + repo |
| `fchouteau/isae-cloud-computing-codespace` | Codespace repo | Your GitHub username + repo |
| `gs://fchouteau-isae-cloud/` | Public GCS bucket with static assets | Your own bucket (or keep if you have access) |
| `europe-west9` / `europe-west9-a` | GCP region/zone | Keep or change based on quota availability |

Also update `scripts/sync_gcp_editors.py` with new `SPREADSHEET_ID` and `GCP_PROJECT` values.

---

## 5. End-of-Year Handover

### Access transfer

- [ ] Add the next teacher as Owner on the GCP project (or transfer project ownership).
- [ ] Transfer ownership of the Codespace repo (or add as admin). See Section 2B for details.
- [ ] Transfer ownership of the course website repo (`isae-data-engineering`) or add as admin.
- [ ] Share access to the Google Sheet with student emails.
- [ ] Share the `gs://fchouteau-isae-cloud/` bucket (static assets for BE exercises).

### Data cleanup

- [ ] Delete all student VMs and Cloud Run services.
- [ ] Delete or empty the year's GCS bucket.
- [ ] Optionally delete Artifact Registry images (or keep for reference).
- [ ] Verify no recurring GCP charges.

### Briefing notes for successor

Key things to communicate:

- The module is 2 days (4 sessions of 3h each).
- All student work happens in GitHub Codespaces — no local setup required.
- The shared GCP project model (since 2024-2025) is simpler than per-student projects but requires you to manage IAM.
- Students need Gmail addresses for GCP access. Collect these in advance if possible.
- Wi-fi at ISAE is unreliable for cloud work. Always have a fallback plan (eduroam, 4G).
- The `alpine:3.18` pin in the Docker hands-on is intentional — don't upgrade without testing.

---

## 6. Helper Scripts Reference

Scripts are in `src/scripts/`.

| Script | Purpose | Usage |
|--------|---------|-------|
| `sync_gcp_editors.py` | Reads Gmail addresses from a Google Sheet and grants them Editor access on the GCP project. | `python sync_gcp_editors.py [--dry-run]` — Update `SPREADSHEET_ID` and `GCP_PROJECT` constants first. |
| `open_port.sh` | Creates GCP firewall rules to open ports 8081 and 8501 on the shared project. | `bash open_port.sh <project-id>` |
| `build_push_images.sh` | Builds and pushes ALL Docker images (mascots, YOLO, activation-function) to Artifact Registry in one shot. | `bash build_push_images.sh <registry-path>` — e.g., `bash build_push_images.sh europe-docker.pkg.dev/isae-sdd-481407/isae-sdd-de-2526-docker` |
| `deploy_vms.py` | **DEPRECATED.** Bulk-creates GCE VMs (used in 2023-2024 per-student model). Kept for reference. | Update config constants if ever needed. |

---

## 7. Troubleshooting & Known Issues

### Alpine 3.18 pin

The Docker hands-on uses `FROM alpine:3.18`. Alpine 3.19+ enforces PEP 668 (externally-managed environments), which causes `pip install` to fail with `error: externally-managed-environment`. Either:

- Keep `alpine:3.18` (recommended for simplicity), or
- Add `--break-system-packages` to pip commands, or
- Use a Python base image instead of Alpine.

### Wi-fi issues at ISAE

`isae-edu` blocks many outbound ports (SSH, non-standard HTTP ports). Solutions:

- Use **eduroam** (works with ISAE credentials).
- Use **4G hotspot** as fallback.
- For port-forwarded apps on Codespace, use the GitHub-provided URL (HTTPS on port 443) instead of direct port access.

### Cloud Run authentication

The `--allow-unauthenticated` flag on `gcloud run deploy` requires permissions beyond the Editor role. When a student gets a permission error:

```bash
# Run as project owner:
gcloud run services add-iam-policy-binding <service-name> \
    --region=europe-west9 \
    --member="allUsers" \
    --role="roles/run.invoker"
```

Or do it via the Cloud Run console: Service → Security → Authentication → "Allow unauthenticated invocations."

### GCE startup script not ready

Students SSH into a VM before the startup script finishes (~2 minutes). They get "python: command not found" because the venv isn't set up yet. Solutions:

- Tell students to wait 2 minutes after VM creation.
- Check script status: `gcloud compute ssh <vm> --zone=europe-west9-a --command="tail /var/log/syslog | grep startup-script"`

### Docker Hub rate limits

Docker Hub limits anonymous pulls to 100/6h per IP. In a classroom of 40+ students sharing the same IP, you can hit this. Solutions:

- Pre-pull common images in the Codespace devcontainer setup.
- Use `gcloud builds submit` to build on Cloud Build instead of locally.
- Have students authenticate to Docker Hub (free account) with `docker login`.

### Codespace disk space

Codespace default disk is 32GB. Pulling multiple Docker images can fill it. Run `docker system prune` to reclaim space.

### gcloud SSH OS Login

First `gcloud compute ssh` may trigger OS Login setup, asking students to configure POSIX account info. This is normal — they just need to follow the prompts.

### docker-compose hostname vs localhost

In docker-compose, services communicate via hostnames defined in `docker-compose.yml` (e.g., `http://yolo:8000`), NOT `http://localhost:8000`. Students consistently forget this.

### Mascot Dockerfiles — verify annually

The mascot Flask apps (`teacher/mascots/` in the companion repo) use `FROM python:3.12-alpine`. Like the `alpine:3.18` pin in the Docker hands-on, this can break if Alpine's pip behavior changes. Each year:

1. Try building one mascot image: `cd teacher/mascots/cat && docker build -t test .`
2. If it fails with `externally-managed-environment`, either pin the Alpine version or add `--break-system-packages` to the pip command in the Dockerfile.

---

## 8. Build Tool Versions

A dedicated environment is recommended to avoid polluting your system. For example, with conda:

```bash
conda create -n isae-de python=3.12 nodejs=22 -y
conda activate isae-de
pip install mkdocs mkdocs-material mkdocs-material-extensions
npm install -g reveal-md
```

Pinned versions used for the 2025-2026 edition:

mkdocs                      1.6.1 (maintenance)
mkdocs-material             9.7.1 (maintenance)
mkdocs-material-extensions  1.3.1 (maintenance)

node                        v22.21.1
reveal-md                   6.1.4 (maintenance)
