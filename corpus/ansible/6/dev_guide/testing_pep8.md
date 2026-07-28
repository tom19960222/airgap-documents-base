---
collection: ansible
version: "6"
title: "PEP 8"
source_url: https://docs.ansible.com/projects/ansible/6/dev_guide/testing_pep8.html
fetched_at: 2026-07-27T16:42:50+00:00
---
# [PEP 8](testing_pep8.md#id2)

Topics

- [PEP 8](testing_pep8.md#pep-8)

  - [Running Locally](testing_pep8.md#running-locally)

[PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines are enforced by [pycodestyle](https://pypi.org/project/pycodestyle/) on all python files in the repository by default.

## [Running Locally](testing_pep8.md#id3)

The [PEP 8](https://www.python.org/dev/peps/pep-0008/) check can be run locally with:

```YAML+Jinja
ansible-test sanity --test pep8 [file-or-directory-path-to-check] ...
```
