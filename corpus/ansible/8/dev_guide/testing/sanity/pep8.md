---
collection: ansible
version: "8"
title: "pep8"
source_url: https://docs.ansible.com/projects/ansible/8/dev_guide/testing/sanity/pep8.html
fetched_at: 2026-07-28T01:03:43+00:00
---
# pep8

Python static analysis for PEP 8 style guideline compliance.

[PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines are enforced by [pycodestyle](https://pypi.org/project/pycodestyle/) on all python files in the repository by default.

## Running locally

The [PEP 8](https://www.python.org/dev/peps/pep-0008/) check can be run locally as follows:

```shell
ansible-test sanity --test pep8 [file-or-directory-path-to-check] ...
```
