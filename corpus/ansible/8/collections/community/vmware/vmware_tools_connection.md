---
collection: ansible
version: "8"
title: "community.vmware.vmware_tools connection – Execute tasks inside a VM via VMware Tools"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_tools_connection.html
fetched_at: 2026-07-28T02:01:33+00:00
---
# community.vmware.vmware_tools connection – Execute tasks inside a VM via VMware Tools

> **Note:**
>
> This connection plugin is part of the [community.vmware collection](https://galaxy.ansible.com/ui/repo/published/community/vmware/) (version 3.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
> You need further requirements to be able to use this connection plugin,
> see [Requirements](vmware_tools_connection.md#ansible-collections-community-vmware-vmware-tools-connection-requirements) for details.
>
> To use it in a playbook, specify: `community.vmware.vmware_tools`.

- [Synopsis](vmware_tools_connection.md#synopsis)
- [Requirements](vmware_tools_connection.md#requirements)
- [Parameters](vmware_tools_connection.md#parameters)

## [Synopsis](vmware_tools_connection.md#id1)

- Use VMware tools to run tasks in, or put/fetch files to guest operating systems running in VMware infrastructure.
- In case of Windows VMs, set `ansible_shell_type` to `powershell`.
- Does not work with ‘become’.

## [Requirements](vmware_tools_connection.md#id2)

The below requirements are needed on the local controller node that executes this connection.

- requests (Python library)

## [Parameters](vmware_tools_connection.md#id3)

| Parameter | Comments |
| --- | --- |
| **exec_command_sleep_interval**  float | Time in seconds to sleep between execution of command.  **Default:** `0.5`  **Configuration:**   - Variable: ansible_vmware_tools_exec_command_sleep_interval |
| **executable**  string | shell to use for execution inside container  **Default:** `"/bin/sh"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   executable = /bin/sh   ``` - Environment variable: [`ANSIBLE_EXECUTABLE`](../../../reference_appendices/config.md#envvar-ANSIBLE_EXECUTABLE) - Variable: ansible_executable - Variable: ansible_vmware_tools_executable |
| **file_chunk_size**  integer | File chunk size.  (Applicable when writing a file to disk, example: using the `fetch` module.)  **Default:** `128`  **Configuration:**   - Variable: ansible_vmware_tools_file_chunk_size |
| **validate_certs**  boolean | Verify SSL for the connection.  Note: This will validate certs for both `vmware_host` and the ESXi host running the VM.  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - Environment variable: [`VMWARE_VALIDATE_CERTS`](../../environment_variables.md#envvar-VMWARE_VALIDATE_CERTS) - Variable: ansible_vmware_validate_certs |
| **vm_password**  string / required | Password for the user in guest operating system.  **Configuration:**   - Variable: ansible_password - Variable: ansible_vmware_tools_password |
| **vm_path**  string | Mutually exclusive with vm_uuid  VM path absolute to the connection.  vCenter Example: `Datacenter/vm/Discovered virtual machine/testVM`.  ESXi Host Example: `ha-datacenter/vm/testVM`.  Must include VM name, appended to ‘folder’ as would be passed to [community.vmware.vmware_guest](vmware_guest_module.md#ansible-collections-community-vmware-vmware-guest-module).  Needs to include *vm* between the Datacenter and the rest of the VM path.  Datacenter default value for ESXi server is `ha-datacenter`.  Folder *vm* is not visible in the vSphere Web Client but necessary for VMware API to work.  **Configuration:**   - Variable: ansible_vmware_guest_path |
| **vm_user**  string / required | VM username.  `ansible_vmware_tools_user` is used for connecting to the VM.  `ansible_user` is used by Ansible on the VM.  **Configuration:**   - Variable: ansible_user - Variable: ansible_vmware_tools_user |
| **vm_uuid**  string | Mutually exclusive with vm_path  VM UUID to the connection.  UUID of the virtual machine from property config.uuid of vmware_vm_inventory plugin  **Configuration:**   - Variable: ansible_vmware_guest_uuid |
| **vmware_host**  string / required | FQDN or IP Address for the connection (vCenter or ESXi Host).  **Configuration:**   - Environment variable: [`VI_SERVER`](../../environment_variables.md#envvar-VI_SERVER) - Environment variable: [`VMWARE_HOST`](../../environment_variables.md#envvar-VMWARE_HOST) - Variable: ansible_host - Variable: ansible_vmware_host |
| **vmware_password**  string / required | Password for the connection.  **Configuration:**   - Environment variable: [`VI_PASSWORD`](../../environment_variables.md#envvar-VI_PASSWORD) - Environment variable: [`VMWARE_PASSWORD`](../../environment_variables.md#envvar-VMWARE_PASSWORD) - Variable: ansible_vmware_password |
| **vmware_port**  string | Port for the connection.  **Default:** `443`  **Configuration:**   - Environment variable: [`VI_PORTNUMBER`](../../environment_variables.md#envvar-VI_PORTNUMBER) - Environment variable: [`VMWARE_PORT`](../../environment_variables.md#envvar-VMWARE_PORT) - Variable: ansible_port - Variable: ansible_vmware_port |
| **vmware_user**  string / required | Username for the connection.  Requires the following permissions on the VM: - VirtualMachine.GuestOperations.Execute - VirtualMachine.GuestOperations.Modify - VirtualMachine.GuestOperations.Query  **Configuration:**   - Environment variable: [`VI_USERNAME`](../../environment_variables.md#envvar-VI_USERNAME) - Environment variable: [`VMWARE_USER`](../../environment_variables.md#envvar-VMWARE_USER) - Variable: ansible_vmware_user |

### Authors

- Deric Crago (@dericcrago)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
