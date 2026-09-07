---
collection: ceph
version: "20.2.4"
title: "Testing notes"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/dev/testing.rst
fetched_at: 2026-08-18T01:32:45Z
---
# Testing notes

## build-integration-branch

### Setup

1. Create a github token at <https://github.com/settings/tokens>
   and put it in `~/.github_token`.  Note that only the
   `public_repo` under the `repo` section needs to be checked.

1. Create a ceph repo label `wip-yourname-testing` if you don't
   already have one at <https://github.com/ceph/ceph/labels>.

1. Create the `ci` remote:

```
git remote add ci git@github.com:ceph/ceph-ci
```

### Using

1. Tag some subset of `needs-qa` commits with your label (usually `wip-yourname-testing`).

1. Create the integration branch:

```
git checkout master
git pull
../src/script/build-integration-branch wip-yourname-testing
```

1. Smoke test:

```
./run-make-check.sh
```

1. Push to ceph-ci:

```
git push ci $(git rev-parse --abbrev-ref HEAD)
```
