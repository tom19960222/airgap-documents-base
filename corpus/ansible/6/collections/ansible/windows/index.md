---
collection: ansible
version: "6"
title: "Ansible.Windows"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/
fetched_at: 2026-07-28T00:24:33+00:00
---
# Ansible.Windows

Collection version 1.12.0

- [Description](index.md#description)
- [Communication](index.md#communication)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Ansible collection for core Windows plugins.

**Authors:**

- Jordan Borean @jborean93
- Matt Davis @nitzmahone

**Supported ansible-core versions:**

- 2.11 or newer

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)

## [Communication](index.md#id2)

- Matrix room `#windows:ansible.im`: [General usage and support questions](https://matrix.to/#/#windows:ansible.im).
- IRC channel `#ansible-windows` (Libera network):
  [General usage and support questions](https://web.libera.chat/?channel=#ansible-windows).

## [Plugin Index](index.md#id3)

These are the plugins in the ansible.windows collection:

### Modules

- [win_acl module](win_acl_module.md#ansible-collections-ansible-windows-win-acl-module) – Set file/directory/registry permissions for a system user or group
- [win_acl_inheritance module](win_acl_inheritance_module.md#ansible-collections-ansible-windows-win-acl-inheritance-module) – Change ACL inheritance
- [win_certificate_store module](win_certificate_store_module.md#ansible-collections-ansible-windows-win-certificate-store-module) – Manages the certificate store
- [win_command module](win_command_module.md#ansible-collections-ansible-windows-win-command-module) – Executes a command on a remote Windows node
- [win_copy module](win_copy_module.md#ansible-collections-ansible-windows-win-copy-module) – Copies files to remote locations on windows hosts
- [win_dns_client module](win_dns_client_module.md#ansible-collections-ansible-windows-win-dns-client-module) – Configures DNS lookup on Windows hosts
- [win_domain module](win_domain_module.md#ansible-collections-ansible-windows-win-domain-module) – Ensures the existence of a Windows domain
- [win_domain_controller module](win_domain_controller_module.md#ansible-collections-ansible-windows-win-domain-controller-module) – Manage domain controller/member server state for a Windows host
- [win_domain_membership module](win_domain_membership_module.md#ansible-collections-ansible-windows-win-domain-membership-module) – Manage domain/workgroup membership for a Windows host
- [win_dsc module](win_dsc_module.md#ansible-collections-ansible-windows-win-dsc-module) – Invokes a PowerShell DSC configuration
- [win_environment module](win_environment_module.md#ansible-collections-ansible-windows-win-environment-module) – Modify environment variables on windows hosts
- [win_feature module](win_feature_module.md#ansible-collections-ansible-windows-win-feature-module) – Installs and uninstalls Windows Features on Windows Server
- [win_file module](win_file_module.md#ansible-collections-ansible-windows-win-file-module) – Creates, touches or removes files or directories
- [win_find module](win_find_module.md#ansible-collections-ansible-windows-win-find-module) – Return a list of files based on specific criteria
- [win_get_url module](win_get_url_module.md#ansible-collections-ansible-windows-win-get-url-module) – Downloads file from HTTP, HTTPS, or FTP to node
- [win_group module](win_group_module.md#ansible-collections-ansible-windows-win-group-module) – Add and remove local groups
- [win_group_membership module](win_group_membership_module.md#ansible-collections-ansible-windows-win-group-membership-module) – Manage Windows local group membership
- [win_hostname module](win_hostname_module.md#ansible-collections-ansible-windows-win-hostname-module) – Manages local Windows computer name
- [win_optional_feature module](win_optional_feature_module.md#ansible-collections-ansible-windows-win-optional-feature-module) – Manage optional Windows features
- [win_owner module](win_owner_module.md#ansible-collections-ansible-windows-win-owner-module) – Set owner
- [win_package module](win_package_module.md#ansible-collections-ansible-windows-win-package-module) – Installs/uninstalls an installable package
- [win_path module](win_path_module.md#ansible-collections-ansible-windows-win-path-module) – Manage Windows path environment variables
- [win_ping module](win_ping_module.md#ansible-collections-ansible-windows-win-ping-module) – A windows version of the classic ping module
- [win_powershell module](win_powershell_module.md#ansible-collections-ansible-windows-win-powershell-module) – Run PowerShell scripts
- [win_reboot module](win_reboot_module.md#ansible-collections-ansible-windows-win-reboot-module) – Reboot a windows machine
- [win_reg_stat module](win_reg_stat_module.md#ansible-collections-ansible-windows-win-reg-stat-module) – Get information about Windows registry keys
- [win_regedit module](win_regedit_module.md#ansible-collections-ansible-windows-win-regedit-module) – Add, change, or remove registry keys and values
- [win_service module](win_service_module.md#ansible-collections-ansible-windows-win-service-module) – Manage and query Windows services
- [win_service_info module](win_service_info_module.md#ansible-collections-ansible-windows-win-service-info-module) – Gather information about Windows services
- [win_share module](win_share_module.md#ansible-collections-ansible-windows-win-share-module) – Manage Windows shares
- [win_shell module](win_shell_module.md#ansible-collections-ansible-windows-win-shell-module) – Execute shell commands on target hosts
- [win_stat module](win_stat_module.md#ansible-collections-ansible-windows-win-stat-module) – Get information about Windows files
- [win_tempfile module](win_tempfile_module.md#ansible-collections-ansible-windows-win-tempfile-module) – Creates temporary files and directories
- [win_template module](win_template_module.md#ansible-collections-ansible-windows-win-template-module) – Template a file out to a remote server
- [win_updates module](win_updates_module.md#ansible-collections-ansible-windows-win-updates-module) – Download and install Windows updates
- [win_uri module](win_uri_module.md#ansible-collections-ansible-windows-win-uri-module) – Interacts with webservices
- [win_user module](win_user_module.md#ansible-collections-ansible-windows-win-user-module) – Manages local Windows user accounts
- [win_user_right module](win_user_right_module.md#ansible-collections-ansible-windows-win-user-right-module) – Manage Windows User Rights
- [win_wait_for module](win_wait_for_module.md#ansible-collections-ansible-windows-win-wait-for-module) – Waits for a condition before continuing
- [win_whoami module](win_whoami_module.md#ansible-collections-ansible-windows-win-whoami-module) – Get information about the current user and process

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
