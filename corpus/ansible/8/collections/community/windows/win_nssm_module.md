---
collection: ansible
version: "8"
title: "community.windows.win_nssm module – Install a service using NSSM"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_nssm_module.html
fetched_at: 2026-07-28T02:02:08+00:00
---
# community.windows.win_nssm module – Install a service using NSSM

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
> see [Requirements](win_nssm_module.md#ansible-collections-community-windows-win-nssm-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_nssm`.

- [Synopsis](win_nssm_module.md#synopsis)
- [Requirements](win_nssm_module.md#requirements)
- [Parameters](win_nssm_module.md#parameters)
- [Notes](win_nssm_module.md#notes)
- [See Also](win_nssm_module.md#see-also)
- [Examples](win_nssm_module.md#examples)

## [Synopsis](win_nssm_module.md#id1)

- Install a Windows service using the NSSM wrapper.
- NSSM is a service helper which doesn’t suck. See <https://nssm.cc/> for more information.

## [Requirements](win_nssm_module.md#id2)

The below requirements are needed on the host that executes this module.

- nssm >= 2.24.0 # (install via [chocolatey.chocolatey.win_chocolatey](../../chocolatey/chocolatey/win_chocolatey_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-module)) `win_chocolatey: name=nssm`

## [Parameters](win_nssm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **app_environment**  dictionary  *added in community.windows 1.2.0* | Key/Value pairs which will be added to the environment of the service application. |
| **app_parameters**  string | A string representing a dictionary of parameters to be passed to the application when it starts.  DEPRECATED since v2.8, please use *arguments* instead.  This is mutually exclusive with *arguments*. |
| **app_rotate_bytes**  integer | NSSM will not rotate any file which is smaller than the configured number of bytes.  **Default:** `104858` |
| **app_rotate_online**  integer | If set to 1, nssm can rotate files which grow to the configured file size limit while the service is running.  **Choices:**   - `0` ← (default) - `1` |
| **app_stop_method_console**  integer | Time to wait after sending Control-C. |
| **app_stop_method_skip**  integer | To disable service shutdown methods, set to the sum of one or more of the numbers  1 - Don’t send Control-C to the console.  2 - Don’t send WM_CLOSE to windows.  4 - Don’t send WM_QUIT to threads.  8 - Don’t call TerminateProcess().  **Choices:**   - `1` - `2` - `3` - `4` - `5` - `6` - `7` - `8` - `9` - `10` - `11` - `12` - `13` - `14` - `15` |
| **application**  path | The application binary to run as a service  Required when *state* is `present`, `started`, `stopped`, or `restarted`. |
| **arguments**  aliases: app_parameters_free_form  string | Parameters to be passed to the application when it starts.  This can be either a simple string or a list.  This is mutually exclusive with *app_parameters*. |
| **dependencies**  list / elements=string | Service dependencies that has to be started to trigger startup, separated by comma. |
| **description**  string | The description to set for the service. |
| **display_name**  string | The display name to set for the service. |
| **executable**  path | The location of the NSSM utility (in case it is not located in your PATH).  **Default:** `"nssm.exe"` |
| **name**  string / required | Name of the service to operate on. |
| **password**  string | Password to be used for service startup.  This is not required for the well known service accounts and group managed service accounts. |
| **start_mode**  string | If `auto` is selected, the service will start at bootup.  `delayed` causes a delayed but automatic start after boot.  `manual` means that the service will start only when another service needs it.  `disabled` means that the service will stay off, regardless if it is needed or not.  **Choices:**   - `"auto"` ← (default) - `"delayed"` - `"disabled"` - `"manual"` |
| **state**  string | State of the service on the system.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"started"` - `"stopped"` - `"restarted"` |
| **stderr_file**  path | Path to receive error output. |
| **stdout_file**  path | Path to receive output. |
| **username**  aliases: user  string | User to be used for service startup.  Group managed service accounts must end with `$`.  Before `1.8.0`, this parameter was just `user`. |
| **working_directory**  aliases: app_directory, chdir  path | The working directory to run the service executable from (defaults to the directory containing the application binary) |

## [Notes](win_nssm_module.md#id4)

> **Note:**
>
> - The service will NOT be started after its creation when `state=present`.
> - Once the service is created, you can use the [ansible.windows.win_service](../../ansible/windows/win_service_module.md#ansible-collections-ansible-windows-win-service-module) module to start it or configure some additionals properties, such as its startup type, dependencies, service account, and so on.

## [See Also](win_nssm_module.md#id5)

> **See also:**
>
> [ansible.windows.win_service](../../ansible/windows/win_service_module.md#ansible-collections-ansible-windows-win-service-module)
> :   Manage and query Windows services.

## [Examples](win_nssm_module.md#id6)

```yaml+jinja
- name: Install the foo service
  community.windows.win_nssm:
    name: foo
    application: C:\windows\foo.exe

# This will yield the following command: C:\windows\foo.exe bar "true"
- name: Install the Consul service with a list of parameters
  community.windows.win_nssm:
    name: Consul
    application: C:\consul\consul.exe
    arguments:
      - agent
      - -config-dir=C:\consul\config

# This is strictly equivalent to the previous example
- name: Install the Consul service with an arbitrary string of parameters
  community.windows.win_nssm:
    name: Consul
    application: C:\consul\consul.exe
    arguments: agent -config-dir=C:\consul\config

# Install the foo service, and then configure and start it with win_service
- name: Install the foo service, redirecting stdout and stderr to the same file
  community.windows.win_nssm:
    name: foo
    application: C:\windows\foo.exe
    stdout_file: C:\windows\foo.log
    stderr_file: C:\windows\foo.log

- name: Configure and start the foo service using win_service
  ansible.windows.win_service:
    name: foo
    dependencies: [ adf, tcpip ]
    username: foouser
    password: secret
    start_mode: manual
    state: started

- name: Install a script based service and define custom environment variables
  community.windows.win_nssm:
    name: <ServiceName>
    application: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
    arguments:
      - <path-to-script>
      - <script arg>
    app_environment:
      AUTH_TOKEN: <token value>
      SERVER_URL: https://example.com
      PATH: "<path-prepends>;{{ ansible_env.PATH }};<path-appends>"

- name: Remove the foo service
  community.windows.win_nssm:
    name: foo
    state: absent
```

### Authors

- Adam Keech (@smadam813)
- George Frank (@georgefrank)
- Hans-Joachim Kliemeck (@h0nIg)
- Michael Wild (@themiwi)
- Kevin Subileau (@ksubileau)
- Shachaf Goldstein (@Shachaf92)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
