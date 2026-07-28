---
collection: ansible
version: "8"
title: "no-unwanted-files"
source_url: https://docs.ansible.com/projects/ansible/8/dev_guide/testing/sanity/no-unwanted-files.html
fetched_at: 2026-07-28T01:03:41+00:00
---
# no-unwanted-files

Specific file types are allowed in certain directories:

- `lib` - All content must reside in the `lib/ansible` directory.
- `lib/ansible` - Only source code with one of the following extensions is allowed:

  - `*.cs` - C#
  - `*.ps1` - PowerShell
  - `*.psm1` - PowerShell
  - `*.py` - Python
