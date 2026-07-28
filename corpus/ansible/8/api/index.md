---
collection: ansible
version: "8"
title: "Ansible API Documentation"
source_url: https://docs.ansible.com/projects/ansible/8/api/index.html
fetched_at: 2026-07-28T01:04:10+00:00
---
# Ansible API Documentation

The Ansible API is under construction. These stub references for attributes, classes, functions, methods, and modules will be documented in future.
The [module utilities](../reference_appendices/module_utils.md#ansible-module-utils) included in `ansible.module_utils.basic` and `AnsibleModule` are documented under Reference & Appendices.

- [Attributes](index.md#attributes)
- [Classes](index.md#classes)
- [Functions](index.md#functions)
- [Methods](index.md#methods)
- [Modules](index.md#module-ansible.module_utils)

## [Attributes](index.md#id1)

AnsibleModule.params

The parameters accepted by the module.

ansible.module_utils.basic.ANSIBLE_VERSION

ansible.module_utils.basic.SELINUX_SPECIAL_FS

Deprecated in favor of ansibleModule._selinux_special_fs.

AnsibleModule.ansible_version

AnsibleModule._debug

AnsibleModule._diff

AnsibleModule.no_log

AnsibleModule._selinux_special_fs

(formerly ansible.module_utils.basic.SELINUX_SPECIAL_FS)

AnsibleModule._syslog_facility

self.playbook

self.play

self.task

sys.path

## [Classes](index.md#id2)

``ansible.module_utils.basic.AnsibleModule``

The basic utilities for AnsibleModule.

*class* AnsibleModule

The main class for an Ansible module.

## [Functions](index.md#id3)

ansible.module_utils.basic._load_params()

Load parameters.

## [Methods](index.md#id4)

AnsibleModule.log()

Logs the output of Ansible.

AnsibleModule.debug()

Debugs Ansible.

Ansible.get_bin_path()

Retrieves the path for executables.

AnsibleModule.run_command()

Runs a command within an Ansible module.

module.fail_json()

Exits and returns a failure.

module.exit_json()

Exits and returns output.

## [Modules](index.md#id5)
