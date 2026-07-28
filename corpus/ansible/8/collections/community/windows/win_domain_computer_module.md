---
collection: ansible
version: "8"
title: "community.windows.win_domain_computer module – Manage computers in Active Directory"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_domain_computer_module.html
fetched_at: 2026-07-28T02:01:46+00:00
---
# community.windows.win_domain_computer module – Manage computers in Active Directory

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_domain_computer`.

- [Synopsis](win_domain_computer_module.md#synopsis)
- [Parameters](win_domain_computer_module.md#parameters)
- [Notes](win_domain_computer_module.md#notes)
- [See Also](win_domain_computer_module.md#see-also)
- [Examples](win_domain_computer_module.md#examples)
- [Return Values](win_domain_computer_module.md#return-values)

## [Synopsis](win_domain_computer_module.md#id1)

- Create, read, update and delete computers in Active Directory using a windows bridge computer to launch New-ADComputer, Get-ADComputer, Set-ADComputer, Remove-ADComputer and Move-ADObject powershell commands.

## [Parameters](win_domain_computer_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | Specifies a description of the object.  This parameter sets the value of the Description property for the object.  The LDAP display name (ldapDisplayName) for this property is description.  **Default:** `""` |
| **dns_hostname**  string | Specifies the fully qualified domain name (FQDN) of the computer.  This parameter sets the DNSHostName property for a computer object.  The LDAP display name for this property is dNSHostName.  Required when *state=present*. |
| **domain_password**  string | The password for *username*. |
| **domain_server**  string | Specifies the Active Directory Domain Services instance to connect to.  Can be in the form of an FQDN or NetBIOS name.  If not specified then the value is based on the domain of the computer running PowerShell. |
| **domain_username**  string | The username to use when interacting with AD.  If this is not set then the user Ansible used to log in with will be used instead when using CredSSP or Kerberos with credential delegation. |
| **enabled**  boolean | Specifies if an account is enabled.  An enabled account requires a password.  This parameter sets the Enabled property for an account object.  This parameter also sets the ADS_UF_ACCOUNTDISABLE flag of the Active Directory User Account Control (UAC) attribute.  **Choices:**   - `false` - `true` ← (default) |
| **managed_by**  string  *added in community.windows 1.3.0* | The value to be assigned to the LDAP `managedBy` attribute.  This value can be in the forms `Distinguished Name`, `objectGUID`, `objectSid` or `sAMAccountName`, see examples for more details. |
| **name**  string / required | Specifies the name of the object.  This parameter sets the Name property of the Active Directory object.  The LDAP display name (ldapDisplayName) of this property is name. |
| **odj_blob_path**  string | The path to the file where the BLOB will be saved. If omitted, a temporary file will be used.  If *offline_domain_join=output* the file will be deleted after its contents are returned.  The parent directory for the BLOB file must exist; intermediate directories will not be created. |
| **offline_domain_join**  string | Provisions a computer in the directory and provides a BLOB file that can be used on the target computer/image to join it to the domain while offline.  The `none` value doesn’t do any offline join operations.  `output` returns the BLOB in output. The BLOB should be treated as secret (it contains the machine password) so use `no_log` when using this option.  `path` preserves the offline domain join BLOB file on the target machine for later use. The path will be returned.  If the computer already exists, no BLOB will be created/returned, and the module will operate as it would have without offline domain join.  **Choices:**   - `"none"` ← (default) - `"output"` - `"path"` |
| **ou**  string | Specifies the X.500 path of the Organizational Unit (OU) or container where the new object is created. Required when *state=present*.  Special characters must be escaped, see [Distinguished Names](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ldap/distinguished-names) for details. |
| **sam_account_name**  string | Specifies the Security Account Manager (SAM) account name of the computer.  It maximum is 256 characters, 15 is advised for older operating systems compatibility.  The LDAP display name (ldapDisplayName) for this property is sAMAccountName.  If ommitted the value is the same as `name`.  Note that all computer SAMAccountNames need to end with a `$`.  If `$` is omitted, it will be added to the end. |
| **state**  string | Specified whether the computer should be `present` or `absent` in Active Directory.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](win_domain_computer_module.md#id3)

> **Note:**
>
> - For more information on Offline Domain Join see [the step-by-step guide](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd392267%2528v=ws.10%2529).
> - When using the ODJ BLOB to join a computer to the domain, it must be written out to a file.
> - The file must be UTF-16 encoded (in PowerShell this encoding is called `Unicode`), and it must end in a null character. See examples.
> - The `djoin.exe` part of the offline domain join process will not use *domain_server*, *domain_username*, or *domain_password*.
> - This must be run on a host that has the ActiveDirectory powershell module installed.

## [See Also](win_domain_computer_module.md#id4)

> **See also:**
>
> [ansible.windows.win_domain](../../ansible/windows/win_domain_module.md#ansible-collections-ansible-windows-win-domain-module)
> :   Ensures the existence of a Windows domain.
>
> [ansible.windows.win_domain_controller](../../ansible/windows/win_domain_controller_module.md#ansible-collections-ansible-windows-win-domain-controller-module)
> :   Manage domain controller/member server state for a Windows host.
>
> [community.windows.win_domain_group](win_domain_group_module.md#ansible-collections-community-windows-win-domain-group-module)
> :   Creates, modifies or removes domain groups.
>
> [ansible.windows.win_domain_membership](../../ansible/windows/win_domain_membership_module.md#ansible-collections-ansible-windows-win-domain-membership-module)
> :   Manage domain/workgroup membership for a Windows host.
>
> [community.windows.win_domain_user](win_domain_user_module.md#ansible-collections-community-windows-win-domain-user-module)
> :   Manages Windows Active Directory user accounts.

## [Examples](win_domain_computer_module.md#id5)

```yaml+jinja
- name: Add linux computer to Active Directory OU using a windows machine
  community.windows.win_domain_computer:
    name: one_linux_server
    sam_account_name: linux_server$
    dns_hostname: one_linux_server.my_org.local
    ou: "OU=servers,DC=my_org,DC=local"
    description: Example of linux server
    enabled: yes
    state: present
  delegate_to: my_windows_bridge.my_org.local

- name: Remove linux computer from Active Directory using a windows machine
  community.windows.win_domain_computer:
    name: one_linux_server
    state: absent
  delegate_to: my_windows_bridge.my_org.local

- name: Provision a computer for offline domain join
  community.windows.win_domain_computer:
    name: newhost
    dns_hostname: newhost.ansible.local
    ou: 'OU=A great\, big organizational unit name,DC=ansible,DC=local'
    state: present
    offline_domain_join: yes
    odj_return_blob: yes
  register: computer_status
  delegate_to: windc.ansible.local

- name: Join a workgroup computer to the domain
  vars:
    target_blob_file: 'C:\ODJ\blob.txt'
  ansible.windows.win_shell: |
    $blob = [Convert]::FromBase64String('{{ computer_status.odj_blob }}')
    [IO.File]::WriteAllBytes('{{ target_blob_file }}', $blob)
    & djoin.exe --% /RequestODJ /LoadFile '{{ target_blob_file }}' /LocalOS /WindowsPath "%SystemRoot%"

- name: Restart to complete domain join
  ansible.windows.win_restart:
```

## [Return Values](win_domain_computer_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **djoin**  dictionary | Information about the invocation of djoin.exe.  **Returned:** when offline_domain_join is True and the computer didn’t exist |
| **invocation**  string | The full command line used to call djoin.exe  **Returned:** always  **Sample:** `"djoin.exe /PROVISION /MACHINE compname /MACHINEOU OU=Hosts,DC=ansible,DC=local /DOMAIN ansible.local /SAVEFILE blobfile.txt"` |
| **rc**  integer | The return code from djoin.exe  **Returned:** when not check mode  **Sample:** `87` |
| **stderr**  string | The stderr from djoin.exe  **Returned:** when not check mode  **Sample:** `"Invalid input parameter combination."` |
| **stdout**  string | The stdout from djoin.exe  **Returned:** when not check mode  **Sample:** `"Computer provisioning completed successfully."` |
| **odj_blob**  string | The offline domain join BLOB. This is an empty string when in check mode or when offline_domain_join is ‘path’.  This field contains the base64 encoded raw bytes of the offline domain join BLOB file.  **Returned:** when offline_domain_join is not ‘none’ and the computer didn’t exist  **Sample:** `"<a long base64 string>"` |
| **odj_blob_file**  string | The path to the offline domain join BLOB file on the target host. If odj_blob_path was specified, this will match that path.  **Returned:** when offline_domain_join is ‘path’ and the computer didn’t exist  **Sample:** `"C:\\Users\\admin\\AppData\\Local\\Temp\\e4vxonty.rkb"` |

### Authors

- Daniel Sánchez Fábregas (@Daniel-Sanchez-Fabregas)
- Brian Scholer (@briantist)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
