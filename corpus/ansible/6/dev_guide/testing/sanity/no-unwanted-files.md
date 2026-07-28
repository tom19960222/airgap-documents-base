---
collection: ansible
version: "6"
title: "no-unwanted-files"
source_url: https://docs.ansible.com/projects/ansible/6/dev_guide/testing/sanity/no-unwanted-files.html
fetched_at: 2026-07-27T16:42:31+00:00
---
# no-unwanted-files

Specific file types are allowed in certain directories:

- `lib` - All content must reside in the `lib/ansible` directory.
- `lib/ansible` - Only source code with one of the following extensions is allowed:

  - `*.cs` - C#
  - `*.ps1` - PowerShell
  - `*.psm1` - PowerShell
  - `*.py` - Python
