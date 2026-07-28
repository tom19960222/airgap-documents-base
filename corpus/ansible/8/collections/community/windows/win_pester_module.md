---
collection: ansible
version: "8"
title: "community.windows.win_pester module – Run Pester tests on Windows hosts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_pester_module.html
fetched_at: 2026-07-28T02:02:10+00:00
---
# community.windows.win_pester module – Run Pester tests on Windows hosts

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
> You need further requirements to be able to use this module,
> see [Requirements](win_pester_module.md#ansible-collections-community-windows-win-pester-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_pester`.

- [Synopsis](win_pester_module.md#synopsis)
- [Requirements](win_pester_module.md#requirements)
- [Parameters](win_pester_module.md#parameters)
- [Examples](win_pester_module.md#examples)
- [Return Values](win_pester_module.md#return-values)

## [Synopsis](win_pester_module.md#id1)

- Run Pester tests on Windows hosts.
- Test files have to be available on the remote host.

## [Requirements](win_pester_module.md#id2)

The below requirements are needed on the host that executes this module.

- Pester

## [Parameters](win_pester_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **output_file**  string | Generates an output test report. |
| **output_format**  string | Format of the test report to be generated.  This parameter is to be used with output_file option.  **Default:** `"NunitXML"` |
| **path**  string / required | Path to a pester test file or a folder where tests can be found.  If the path is a folder, the module will consider all ps1 files as Pester tests. |
| **tags**  list / elements=string | Runs only tests in Describe blocks with specified Tags values.  Accepts multiple comma separated tags. |
| **test_parameters**  dictionary | Allows to specify parameters to the test script. |
| **version**  aliases: minimum_version  string | Minimum version of the pester module that has to be available on the remote host. |

## [Examples](win_pester_module.md#id4)

```yaml+jinja
- name: Get facts
  ansible.windows.setup:

- name: Add Pester module
  action:
    module_name: "{{ 'community.windows.win_psmodule' if ansible_powershell_version >= 5 else 'chocolatey.chocolatey.win_chocolatey' }}"
    name: Pester
    state: present

- name: Run the pester test provided in the path parameter.
  community.windows.win_pester:
    path: C:\Pester

- name: Run the pester tests only for the tags specified.
  community.windows.win_pester:
    path: C:\Pester\TestScript.tests
    tags: CI,UnitTests

# Run pesters tests files that are present in the specified folder
# ensure that the pester module version available is greater or equal to the version parameter.
- name: Run the pester test present in a folder and check the Pester module version.
  community.windows.win_pester:
    path: C:\Pester\test01.test.ps1
    version: 4.1.0

- name: Run the pester test present in a folder with given script parameters.
  community.windows.win_pester:
    path: C:\Pester\test04.test.ps1
    test_parameters:
      Process: lsass
      Service: bits

- name: Run the pester test present in a folder and generate NunitXML test result..
  community.windows.win_pester:
    path: C:\Pester\test04.test.ps1
    output_file: c:\Pester\resullt\testresult.xml
```

## [Return Values](win_pester_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  list / elements=string | Results of the Pester tests.  **Returned:** success  **Sample:** `["False"]` |
| **pester_version**  string | Version of the pester module found on the remote host.  **Returned:** always  **Sample:** `"4.3.1"` |

### Authors

- Erwan Quelin (@equelin)
- Prasoon Karunan V (@prasoonkarunan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
