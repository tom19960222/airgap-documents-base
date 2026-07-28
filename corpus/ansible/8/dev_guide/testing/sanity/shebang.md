---
collection: ansible
version: "8"
title: "shebang"
source_url: https://docs.ansible.com/projects/ansible/8/dev_guide/testing/sanity/shebang.html
fetched_at: 2026-07-28T01:03:49+00:00
---
# shebang

Most executable files should only use one of the following shebangs:

- `#!/bin/sh`
- `#!/bin/bash -eu`
- `#!/bin/bash -eux`
- `#!/usr/bin/make`
- `#!/usr/bin/env python`
- `#!/usr/bin/env bash`

This does not apply to Ansible modules, which should not be executable and must always use `#!/usr/bin/python`.

Some exceptions are permitted. Ask if you have questions.
