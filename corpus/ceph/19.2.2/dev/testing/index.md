---
collection: ceph
version: "19.2.2"
title: "Testing notes"
source_url: https://docs.ceph.com/en/squid/dev/testing/
fetched_at: 2026-07-27T16:41:33+00:00
---
# Testing notes

## build-integration-branch

### Setup

1. Create a github token at <https://github.com/settings/tokens>
   and put it in `~/.github_token`. Note that only the
   `public_repo` under the `repo` section needs to be checked.
2. Create a ceph repo label wip-yourname-testing if you don’t
   already have one at <https://github.com/ceph/ceph/labels>.
3. Create the `ci` remote:

   ```
   git remote add ci git@github.com:ceph/ceph-ci
   ```

### Using

1. Tag some subset of needs-qa commits with your label (usually wip-yourname-testing).
2. Create the integration branch:

   ```
   git checkout master
   git pull
   ../src/script/build-integration-branch wip-yourname-testing
   ```
3. Smoke test:

   ```
   ./run-make-check.sh
   ```
4. Push to ceph-ci:

   ```
   git push ci $(git rev-parse --abbrev-ref HEAD)
   ```

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
