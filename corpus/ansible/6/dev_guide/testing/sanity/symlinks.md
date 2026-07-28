---
collection: ansible
version: "6"
title: "symlinks"
source_url: https://docs.ansible.com/projects/ansible/6/dev_guide/testing/sanity/symlinks.html
fetched_at: 2026-07-27T16:42:36+00:00
---
# symlinks

Symbolic links are only permitted for files that exist to ensure proper tarball generation during a release.

If other types of symlinks are needed for tests they must be created as part of the test.
