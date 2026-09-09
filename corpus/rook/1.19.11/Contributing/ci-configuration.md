---
collection: rook
version: "1.19.11"
title: "CI Configuration"
source_url: https://github.com/rook/rook/blob/e6818be5fcdcc4e3752f1cb03a7c0fbcc12dbdf1/Documentation/Contributing/ci-configuration.md
fetched_at: 2026-09-02T10:46:10-06:00
---
This page contains information regarding the CI configuration used for the Rook project to test, build and release the project.

## Secrets

* Snyk (Security Scan):
    * `SNYK_TOKEN` - API Token for the [snyk security scanner](https://snyk.io/) (workflow file: `snyk.yaml`).
* Testing:
    * `IBM_INSTANCE_ID`: Used for KMS (Key Management System) IBM Key Protect access (see [`.github/workflows/encryption-pvc-kms-ibm-kp/action.yml`](https://github.com/rook/rook/blob/e6818be5fcdcc4e3752f1cb03a7c0fbcc12dbdf1/.github/workflows/encryption-pvc-kms-ibm-kp/action.yml)).
    * `IBM_SERVICE_API_KEY`: Used for KMS (Key Management System) IBM Key Protect access (see [`.github/workflows/encryption-pvc-kms-ibm-kp/action.yml`](https://github.com/rook/rook/blob/e6818be5fcdcc4e3752f1cb03a7c0fbcc12dbdf1/.github/workflows/encryption-pvc-kms-ibm-kp/action.yml)).
* Publishing:
    * `DOCKER_USERNAME` + `DOCKER_PASSWORD`: Username and password of registry.
    * `DOCKER_REGISTRY`: Target registry namespace (e.g., `rook`)
    * `AWS_USR` + `AWS_PSW`: AWS credentials with access to S3 for Helm chart publishing.
    * `GIT_API_TOKEN`: GitHub access token, used to push docs changes to the docs repositories `gh-pages` branch.
