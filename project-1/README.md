## Project 1 - The Global Launch

![Azure](https://img.shields.io/badge/Azure-Blob%20Storage-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Static Site](https://img.shields.io/badge/Hosting-Static%20Website-00ff88?style=for-the-badge)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Status](https://img.shields.io/badge/Status-Live-00ff88?style=for-the-badge)

---

### Project Overview

**Mission:** Host a static portfolio website on cloud object storage — without provisioning a single server.

**Live URL:** https://lulupfolio.z1.web.core.windows.net

---

### Objectives

- [x] Create a public cloud storage bucket (Azure Blob Storage)
- [x] Upload HTML/CSS portfolio website
- [x] Enable Static Website Hosting
- [x] Configure public access policies
- [x] Set up CI/CD pipeline with GitHub Actions
- [x] Attempt CDN configuration (restricted by Azure Student plan)

---

### Architecture

```
User (Browser)
      │
      │ HTTPS Request
      ▼
 Azure Global Network
      │
      ▼
 Azure Blob Storage ($web container)
 ┌─────────────────────────────┐
 │  index.html                 │
 │  404.html                   │
 └─────────────────────────────┘
      │
      ▼
 Static Website Served ✅
 No EC2 · No VM · No OS Management
```

---

### Cloud Services Used

| Service                | Purpose                                       |
| ---------------------- | --------------------------------------------- |
| Azure Blob Storage     | Object storage for website files              |
| Static Website Hosting | Serves HTML/CSS directly from the bucket      |
| $web Container         | Special Azure container for static site files |
| GitHub Actions         | CI/CD — auto-deploys on every push to main    |

---

### Deployment Steps

#### 1. Create Azure Storage Account

- Platform: Microsoft Azure (Azure for Students)
- Resource Group: `decodelabs-project1`
- Storage Account: `lulupfolio`
- Region: **South Africa North** (closest to Nigeria)
- Performance: Standard | Redundancy: LRS

#### 2. Enable Static Website Hosting

- Navigate to: Storage Account → Data Management → Static website
- Set Index document: `index.html`
- Set Error document: `404.html`
- Azure automatically creates the `$web` container

#### 3. Upload Website Files

Files uploaded to the `$web` container:

- `index.html` — Main portfolio page
- `404.html` — Custom error page

#### 4. Configure CI/CD with GitHub Actions

Every push to the `main` branch automatically deploys to Azure:

```yaml
name: Deploy to Azure Blob Storage

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Upload to Azure Blob Storage
        uses: azure/CLI@v1
        with:
          inlineScript: |
            az storage blob upload-batch \
              --account-name lulupfolio \
              --source . \
              --destination '$web' \
              --overwrite \
              --connection-string "${{ secrets.AZURE_STORAGE_CONNECTION_STRING }}"
```

> The connection string is stored as a **GitHub Secret** — never exposed in code.

---

### Security Practices Applied

- No root account keys used or exposed
- Azure connection string stored as encrypted GitHub Secret
- Public access scoped only to the `$web` static website container
- Principle of Least Privilege followed throughout

---

### Challenges & Learnings

| Challenge                               | What I Learned                                                                                    |
| --------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Region policy violation on first deploy | Azure Student subscriptions restrict certain regions — solved by selecting **South Africa North** |
| Microsoft.Cdn not registered            | Azure resource providers must be manually registered for student subscriptions                    |
| Azure Front Door blocked for students   | Premium CDN services require paid plans — documented limitation, not a failure                    |

---

### Key Concepts Demonstrated

- **Object Storage vs Traditional Servers** — Storage buckets serve files directly over HTTP with no OS or compute layer
- **Serverless Hosting** — Zero server provisioning, infinite scalability, pay-per-use pricing
- **11 Nines Durability** — Azure Blob replicates data across multiple availability zones
- **CI/CD Pipeline** — GitHub Actions automates deployment on every code push
- **Least Privilege Security** — Secrets managed via GitHub, no hardcoded credentials

---

### Project Structure

```
decodelabs-project1/
├── index.html          # Main portfolio page
├── 404.html            # Custom error page
├── .github/
│   └── workflows/
│       └── deploy.yml  # GitHub Actions CI/CD pipeline
└── README.md           # This file
```

---

### Author

**Oluchukwu Anakor**
Cloud Computing Intern — DecodeLabs Batch 2026
