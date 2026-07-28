---
collection: ansible
version: "8"
title: "community.windows.win_pssession_configuration module – Manage PSSession Configurations"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_pssession_configuration_module.html
fetched_at: 2026-07-28T02:02:18+00:00
---
# community.windows.win_pssession_configuration module – Manage PSSession Configurations

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
> To use it in a playbook, specify: `community.windows.win_pssession_configuration`.

- [Synopsis](win_pssession_configuration_module.md#synopsis)
- [Parameters](win_pssession_configuration_module.md#parameters)
- [Notes](win_pssession_configuration_module.md#notes)
- [See Also](win_pssession_configuration_module.md#see-also)
- [Examples](win_pssession_configuration_module.md#examples)

## [Synopsis](win_pssession_configuration_module.md#id1)

- Register, unregister, and modify PSSession Configurations for PowerShell remoting.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](win_pssession_configuration_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_mode**  string | Controls whether the session configuration allows connection from the `local` machine only, both local and `remote`, or none (`disabled`).  **Choices:**   - `"disabled"` - `"local"` - `"remote"` |
| **alias_definitions**  dictionary | A dict that defines aliases for each session. |
| **assemblies_to_load**  list / elements=string | The assemblies that should be loaded into each session. |
| **async_poll**  integer | Sets a delay in seconds between each check of the asynchronous execution status.  Replicates the functionality of the `poll` keyword.  Has no effect in check mode.  *async_poll=0* is not supported.  **Default:** `1` |
| **async_timeout**  integer | Sets a timeout for how long in seconds to wait for asynchronous module execution and waiting for the connection to recover.  Replicates the functionality of the `async` keyword.  Has no effect in check mode.  **Default:** `300` |
| **author**  string | The author of the session configuration.  This value is metadata and does not affect the functionality of the session configuration.  If not set, a value may be generated automatically.  See also *lenient_config_fields*. |
| **company_name**  string | The company that authored the session configuration.  This value is metadata and does not affect the functionality of the session configuration.  If not set, a value may be generated automatically.  See also *lenient_config_fields*. |
| **copyright**  string | The copyright statement of the session configuration.  This value is metadata and does not affect the functionality of the session configuration.  If not set, a value may be generated automatically.  See also *lenient_config_fields*. |
| **description**  string | The description of the session configuration.  This value is metadata and does not affect the functionality of the session configuration.  See also *lenient_config_fields*. |
| **environment_variables**  dictionary | A dict that defines environment variables for each session. |
| **execution_policy**  string | The execution policy controlling script execution in the PowerShell session.  **Choices:**   - `"default"` - `"remote_signed"` - `"restricted"` - `"undefined"` - `"unrestricted"` |
| **formats_to_process**  list / elements=path | Paths to format definition files to process for each session. |
| **function_definitions**  dictionary | A dict that defines functions for each session. |
| **group_managed_service_account**  string | If the session will run as a group managed service account (gMSA) then this is the name.  Do not use *run_as_credential_username* and *run_as_credential_password* to specify a gMSA. |
| **guid**  any | The GUID (UUID) of the session configuration file.  This value is metadata, so it only matters if you use it externally.  If not set, a value will be generated automatically.  Acceptable GUID formats are flexible. Any string of 32 hexadecimal digits will be accepted, with all hyphens `-` and opening/closing `{}` ignored.  See also *lenient_config_fields*. |
| **language_mode**  string | Determines the language mode of the PowerShell session.  **Choices:**   - `"no_language"` - `"restricted_language"` - `"constrained_language"` - `"full_language"` |
| **lenient_config_fields**  list / elements=string | Some fields used in the session configuration do not affect its function, and are sometimes auto-generated when not specified.  To avoid unnecessarily changing the configuration on each run, the values of these options will only be enforced when they are explicitly specified.  **Default:** `["guid", "author", "company_name", "copyright", "description"]` |
| **maximum_received_data_size_per_command_mb**  any | Sets the maximum received data size per command in MB.  Must fit into a double precision floating point value. |
| **maximum_received_object_size_mb**  any | Sets the maximum object size in MB.  Must fit into a double precision floating point value. |
| **modules_to_import**  list / elements=any | A list of modules that should be imported into the session.  Any valid PowerShell module spec can be used here, so simple str names or dicts can be used.  If a dict is used, no snake_case conversion is done, so the original PowerShell names must be used. |
| **mount_user_drive**  boolean | If `yes` the session creates and mounts a user-specific PSDrive for use with file transfers.  **Choices:**   - `false` - `true` |
| **name**  string / required | The name of the session configuration to manage. |
| **powershell_version**  any | The minimum required PowerShell version for this session.  Must be a valid .Net System.Version string. |
| **processor_architecure**  string | The processor architecture of the session (32 bit vs. 64 bit).  **Choices:**   - `"amd64"` - `"x86"` |
| **required_groups**  dictionary | For JEA sessions, defines conditional access rules about which groups a connecting user must belong to.  For more information see <https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/jea/session-configurations#conditional-access-rules>. |
| **role_definitions**  dictionary | A dict defining the roles for JEA sessions.  For more information see <https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/jea/session-configurations#role-definitions>. |
| **run_as_credential_password**  string | The password for *run_as_credential_username*. |
| **run_as_credential_username**  string | Used to set a RunAs account for the session. All commands executed in the session will be run as this user.  To use a gMSA, see *group_managed_service_account*.  To use a virtual account, see *run_as_virtual_account* and *run_as_virtual_account_groups*.  Status will always be `changed` when a RunAs credential is set because the password cannot be retrieved for comparison. |
| **run_as_virtual_account**  boolean | If `yes` the session runs as a virtual account.  Do not use *run_as_credential_username* and *run_as_credential_password* to specify a virtual account.  **Choices:**   - `false` - `true` |
| **run_as_virtual_account_groups**  list / elements=string | If *run_as_virtual_account=yes* this is a list of groups to add the virtual account to. |
| **schema_version**  any | The schema version of the session configuration file.  If not set, a value will be generated automatically.  Must be a valid .Net System.Version string. |
| **scripts_to_process**  list / elements=string | A list of paths to script files ending in `.ps1` that should be applied to the session. |
| **security_descriptor_sddl**  string | An SDDL string that controls which users and groups can connect to the session.  If *role_definitions* is specified the security descriptor will be set based on that.  If this option is not specified the default security descriptor will be applied. |
| **session_type**  string | Controls what type of session this is.  **Choices:**   - `"default"` - `"empty"` - `"restricted_remote_server"` |
| **startup_script**  path | A script that gets run on session startup. |
| **state**  string | The desired state of the configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **thread_apartment_state**  string | The apartment state for the PowerShell session.  **Choices:**   - `"mta"` - `"sta"` |
| **thread_options**  string | Sets thread options for the session.  **Choices:**   - `"default"` - `"reuse_thread"` - `"use_current_thread"` - `"use_new_thread"` |
| **transcript_directory**  path | Automatic session transcripts will be written to this directory. |
| **types_to_process**  list / elements=path | Paths to type definition files to process for each session. |
| **use_shared_process**  boolean | If `yes` then the session shares a process for each session.  **Choices:**   - `false` - `true` |
| **user_drive_maximum_size**  any | The maximum size of the user drive in bytes.  Must fit into an Int64. |
| **variable_definitions**  list / elements=dictionary | A list of dicts where each elements defines a variable for each session. |
| **visible_aliases**  list / elements=string | The aliases that can be used in the session.  For more information see <https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/jea/role-capabilities>. |
| **visible_cmdlets**  list / elements=any | The cmdlets that can be used in the session.  The elements can be simple names or complex command specifications.  For more information see <https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/jea/role-capabilities>. |
| **visible_external_commands**  list / elements=string | The external commands and scripts that can be used in the session.  For more information see <https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/jea/role-capabilities>. |
| **visible_functions**  list / elements=any | The functions that can be used in the session.  The elements can be simple names or complex command specifications.  For more information see <https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/jea/role-capabilities>. |

## [Notes](win_pssession_configuration_module.md#id3)

> **Note:**
>
> - This module will restart the WinRM service on any change. This will terminate all WinRM connections including those by other Ansible runs.
> - Internally this module uses `async` when not in check mode to ensure things go smoothly when restarting the WinRM service.
> - The standard `async` and `poll` keywords cannot be used; instead use the *async_timeout* and *async_poll* options to control asynchronous execution.
> - Options that don’t list a default value here will use the defaults of `New-PSSessionConfigurationFile` and `Register-PSSessionConfiguration`.
> - If a value can be specified in both a session config file and directly in the session options, this module will prefer the setting be in the config file.

## [See Also](win_pssession_configuration_module.md#id4)

> **See also:**
>
> [C(New-PSSessionConfigurationFile) Reference](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-pssessionconfigurationfile)
> :   Details and defaults for options that end up in the session configuration file.
>
> [C(Register-PSSessionConfiguration) Reference](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/register-pssessionconfiguration)
> :   Details and defaults for options that are not specified in the session config file.
>
> [PowerShell Just Enough Administration (JEA)](https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/jea/overview)
> :   Refer to the JEA documentation for advanced usage of some options
>
> [About Session Configurations](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_session_configurations)
> :   General information about session configurations.
>
> [About Session Configuration Files](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_session_configuration_files)
> :   General information about session configuration files.

## [Examples](win_pssession_configuration_module.md#id5)

```yaml+jinja
- name: Register a session configuration that loads modules automatically
  community.windows.win_pssession_configuration:
    name: WebAdmin
    modules_to_import:
      - WebAdministration
      - IISAdministration
    description: This endpoint has IIS modules pre-loaded

- name: Set up an admin endpoint with a restricted execution policy
  community.windows.win_pssession_configuration:
    name: GloboCorp.Admin
    company_name: Globo Corp
    description: Admin Endpoint
    execution_policy: restricted

- name: Create a complex JEA endpoint
  community.windows.win_pssession_configuration:
    name: RBAC.Endpoint
    session_type: restricted_remote_server
    run_as_virtual_account: True
    transcript_directory: '\\server\share\Transcripts'
    language_mode: no_language
    execution_policy: restricted
    role_definitions:
      'CORP\IT Support':
        RoleCapabilities:
          - PasswordResetter
          - EmployeeOffboarder
      'CORP\Webhosts':
        RoleCapabilities: IISAdmin
    visible_functions:
      - tabexpansion2
      - help
    visible_cmdlets:
      - Get-Help
      - Name: Get-Service
        Parameters:
          - Name: DependentServices
          - Name: RequiredServices
          - Name: Name
            ValidateSet:
              - WinRM
              - W3SVC
              - WAS
    visible_aliases:
      - gsv
    state: present

- name: Remove a session configuration
  community.windows.win_pssession_configuration:
    name: UnusedEndpoint
    state: absent

- name: Set a sessions configuration with tweaked async values
  community.windows.win_pssession_configuration:
    name: MySession
    description: A sample session
    async_timeout: 500
    async_poll: 5
```

### Authors

- Brian Scholer (@briantist)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
