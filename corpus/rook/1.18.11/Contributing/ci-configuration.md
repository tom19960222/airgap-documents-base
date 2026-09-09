---
collection: rook
version: "1.18.11"
title: "CI Configuration"
source_url: https://github.com/rook/rook/blob/8059413c805f8ed3a0992af0113c002b0250805e/Documentation/Contributing/ci-configuration.md
fetched_at: 2026-05-27T11:20:14-06:00
---
This page contains information regarding the CI configuration used for the Rook project to test, build and release the project.

## Secrets

* Snyk (Security Scan):
    * `SNYK_TOKEN` - API Token for the [snyk security scanner](https://snyk.io/) (workflow file: `snyk.yaml`).
* Testing:
    * `IBM_INSTANCE_ID`: Used for KMS (Key Management System) IBM Key Protect access (see [`.github/workflows/encryption-pvc-kms-ibm-kp/action.yml`](https://github.com/rook/rook/blob/8059413c805f8ed3a0992af0113c002b0250805e/.github/workflows/encryption-pvc-kms-ibm-kp/action.yml)).
    * `IBM_SERVICE_API_KEY`: Used for KMS (Key Management System) IBM Key Protect access (see [`.github/workflows/encryption-pvc-kms-ibm-kp/action.yml`](https://github.com/rook/rook/blob/8059413c805f8ed3a0992af0113c002b0250805e/.github/workflows/encryption-pvc-kms-ibm-kp/action.yml)).
* Publishing:
    * `DOCKER_USERNAME` + `DOCKER_PASSWORD`: Username and password of registry.
    * `DOCKER_REGISTRY`: Target registry namespace (e.g., `rook`)
    * `AWS_USR` + `AWS_PSW`: AWS credentials with access to S3 for Helm chart publishing.
    * `GIT_API_TOKEN`: GitHub access token, used to push docs changes to the docs repositories `gh-pages` branch.
