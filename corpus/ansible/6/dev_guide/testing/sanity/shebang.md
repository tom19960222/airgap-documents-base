---
collection: ansible
version: "6"
title: "shebang"
source_url: https://docs.ansible.com/projects/ansible/6/dev_guide/testing/sanity/shebang.html
fetched_at: 2026-07-27T16:42:36+00:00
---
# shebang

Most executable files should only use one of the following shebangs:

- `#!/bin/sh`
- `#!/bin/bash`
- `#!/usr/bin/make`
- `#!/usr/bin/env python`
- `#!/usr/bin/env bash`

NOTE: For `#!/bin/bash`, any of the options `eux` may also be used, such as `#!/bin/bash -eux`.

This does not apply to Ansible modules, which should not be executable and must always use `#!/usr/bin/python`.

Some exceptions are permitted. Ask if you have questions.
