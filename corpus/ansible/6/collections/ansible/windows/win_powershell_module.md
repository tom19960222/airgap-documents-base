---
collection: ansible
version: "6"
title: "ansible.windows.win_powershell module – Run PowerShell scripts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_powershell_module.html
fetched_at: 2026-07-27T16:45:00+00:00
---
# ansible.windows.win_powershell module – Run PowerShell scripts

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ansible/windows) (version 1.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_powershell`.

New in ansible.windows 1.5.0

- [Synopsis](win_powershell_module.md#synopsis)
- [Parameters](win_powershell_module.md#parameters)
- [Notes](win_powershell_module.md#notes)
- [See Also](win_powershell_module.md#see-also)
- [Examples](win_powershell_module.md#examples)
- [Return Values](win_powershell_module.md#return-values)

## [Synopsis](win_powershell_module.md#id1)

- Runs a PowerShell script and outputs the data in a structured format.
- Use [ansible.windows.win_command](win_command_module.md#ansible-collections-ansible-windows-win-command-module) or [ansible.windows.win_shell](win_shell_module.md#ansible-collections-ansible-windows-win-shell-module) to run a tranditional PowerShell process with stdout, stderr, and rc results.

## [Parameters](win_powershell_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **arguments**  list / elements=string | A list of arguments to pass to *executable* when running a script in another PowerShell process.  These are not arguments to pass to *script*, use *parameters* for that purpose. |
| **chdir**  string | The PowerShell location to set when starting the script.  This can be a location in any of the PowerShell providers.  The default location is dependent on many factors, if relative paths are used then set this option. |
| **creates**  string | A path or path filter pattern; when the referenced path exists on the target host, the task will be skipped. |
| **depth**  integer | How deep the return values are serialized for `result`, `output`, and `information[x].message_data`.  This also controls the depth of the diff output set by `$Ansible.Diff`.  Setting this to a higher value can dramatically increase the amount of data that needs to be returned.  Default: `2` |
| **error_action**  string | The `$ErrorActionPreference` to set before executing *script*.  `silently_continue` will ignore any errors and exceptions raised.  `continue` is the default behaviour in PowerShell, errors are present in the *error* return value but only terminating exceptions will stop the script from continuing and set it as failed.  `stop` will treat errors like exceptions, will stop the script and set it as failed.  Choices:   - `"silently_continue"` - `"continue"` ← (default) - `"stop"` |
| **executable**  string | A custom PowerShell executable to run the script in.  When not defined the script will run in the current module PowerShell interpreter.  Both the remote PowerShell and the one specified by *executable* must be running on PowerShell v5.1 or newer.  Setting this value may change the values returned in the `output` return value depending on the underlying .NET type. |
| **parameters**  dictionary | Parameters to pass into the script as key value pairs.  The key corresponds to the parameter name and the value is the value for that parameter. |
| **removes**  string | A path or path filter pattern; when the referenced path **does not** exist on the target host, the task will be skipped. |
| **script**  string / required | The PowerShell script to run. |

## [Notes](win_powershell_module.md#id3)

> **Note:**
>
> - The module is set as failed when a terminating exception is throw, or `error_action=stop` and a normal error record is raised.
> - The output values are processed using a custom filter and while it mostly matches the `ConvertTo-Json` result the following value types are different.
> - `DateTime` will be an ISO 8601 string in UTC, `DateTimeOffset` will have the offset as specified by the value.
> - `Enum` will contain a dictionary with `Type`, `String`, `Value` being the type name, string representation and raw integer value respectively.
> - `Type` will contain a dictionary with `Name`, `FullName`, `AssemblyQualifiedName`, `BaseType` being the type name, the type name including the namespace, the full assembly name the type was defined in and the base type it derives from.
> - The script has access to the `$Ansible` variable where it can set `Result`, `Changed`, `Failed`, `Diff`, or access `Tmpdir`.
> - `$Ansible.Result` is a value that is returned back to the controller as is.
> - `$Ansible.Diff` was added in the `1.12.0` release of `ansible.windows` and is a dictionary that is set to the diff result that can be interepreted by Ansible.
> - `$Ansible.Changed` can be set to `true` or `false` to reflect whether the module made a change or not. By default this is set to `true`.
> - `$Ansible.Failed` can be set to `true` if the script wants to return the failure back to the controller.
> - `$Ansible.Tmpdir` is the path to a temporary directory to use as a scratch location that is cleaned up after the module has finished.
> - `$Ansible.Verbosity` reveals Ansible’s verbosity level for this play. Allows the script to set VerbosePreference/DebugPreference based on verbosity. Added in `1.9.0`.
> - Any host/console output like `Write-Host` or `[Console]::WriteLine` is not considered an output object, they are returned as a string in *host_out* and *host_err*.
> - The module will skip running the script when in check mode unless the script defines `[CmdletBinding(SupportsShouldProcess`]).

## [See Also](win_powershell_module.md#id4)

> **See also:**
>
> [ansible.windows.win_command](win_command_module.md#ansible-collections-ansible-windows-win-command-module)
> :   Executes a command on a remote Windows node.
>
> [ansible.windows.win_shell](win_shell_module.md#ansible-collections-ansible-windows-win-shell-module)
> :   Execute shell commands on target hosts.

## [Examples](win_powershell_module.md#id5)

```yaml+jinja
- name: Run basic PowerShell script
  ansible.windows.win_powershell:
    script: |
      echo "Hello World"

- name: Run PowerShell script with parameters
  ansible.windows.win_powershell:
    script: |
      [CmdletBinding()]
      param (
          [String]
          $Path,

          [Switch]
          $Force
      )

      New-Item -Path $Path -ItemType Directory -Force:$Force
    parameters:
      Path: C:\temp
      Force: true

- name: Run PowerShell script that modifies the module changed result
  ansible.windows.win_powershell:
    script: |
      if (Get-Service -Name test -ErrorAction SilentlyContinue) {
          Remove-Service -Name test
      }
      else {
          $Ansible.Changed = $false
      }

- name: Run PowerShell script in PowerShell 7
  ansible.windows.win_powershell:
    script: |
      $PSVersionTable.PSVersion.Major
    executable: pwsh.exe
    arguments:
    - -ExecutionPolicy
    - ByPass
  register: pwsh_output
  failed_when:
  - pwsh_output.output[0] != 7

- name: Run code in check mode
  ansible.windows.win_powershell:
    script: |
      [CmdletBinding(SupportsShouldProcess)]
      param ()

      # Use $Ansible to detect check mode
      if ($Ansible.CheckMode) {
          echo 'running in check mode'
      }
      else {
          echo 'running in normal mode'
      }

      # Use builtin ShouldProcess (-WhatIf)
      if ($PSCmdlet.ShouldProcess('target')) {
          echo 'also running in normal mode'
      }
      else {
          echo 'also running in check mode'
      }
  check_mode: yes

- name: Return a failure back to Ansible
  ansible.windows.win_powershell:
    script: |
      if (Test-Path C:\bad.file) {
          $Ansible.Failed = $true
      }

- name: Define when the script made a change or not
  ansible.windows.win_powershell:
    script: |
      if ((Get-Item WSMan:\localhost\Service\Auth\Basic).Value -eq 'true') {
          Set-Item WSMan:\localhost\Service\Auth\Basic -Value false
      }
      else {
          $Ansible.Changed = $true
      }

- name: Define when to enable Verbose/Debug output
  ansible.windows.win_powershell:
    script: |
      if ($Ansible.Verbosity -ge 3) {
          $VerbosePreference = "Continue"
      }
      if ($Ansible.Verbosity -eq 5) {
          $DebugPreference = "Continue"
      }
      Write-Output "Hello World!"
      Write-Verbose "Hello World!"
      Write-Debug "Hello World!"
```

## [Return Values](win_powershell_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **debug**  list / elements=string | A list of warning messages created by the script.  Debug messages only appear when `$DebugPreference = 'Continue'`.  Returned: always  Sample: `["debug record"]` |
| **error**  list / elements=dictionary | A list of error records created by the script.  Returned: always |
| **category_info**  dictionary | More information about the error record.  Returned: success |
| **activity**  string | Description of the operation which encountered the error.  Returned: always  Sample: `"Write-Error"` |
| **category**  string | The category name of the error record.  Returned: always  Sample: `"NotSpecified"` |
| **category_id**  integer | The integer representation of the category.  Returned: always  Sample: `0` |
| **reason**  string | Description of the error.  Returned: always  Sample: `"WriteErrorException"` |
| **target_name**  string | Description of the target object.  Can be an empty string if no target was specified.  Returned: always  Sample: `"C:\\Windows"` |
| **target_type**  string | Description of the type of the target object.  Can be an empty string if no target object was specified.  Returned: always  Sample: `"String"` |
| **error_details**  dictionary | Additional details about an ErrorRecord.  Can be null if there are not additional details.  Returned: success |
| **message**  string | Message for the error record.  Returned: always  Sample: `"Specific error message"` |
| **recommended_action**  string | Recommended action in the even that this error occurs.  This is empty unless the code which generates the error adds this explicitly.  Returned: always  Sample: `"Delete file"` |
| **exception**  dictionary | Details about the exception behind the error record.  Returned: success |
| **help_link**  string | A link to the help details for the exception.  May not be set as it’s dependent on whether the .NET exception class provides this info.  Returned: always  Sample: `"http://docs.ansible.com/"` |
| **hresult**  integer | The signed integer assigned to this exception.  May not be set as it’s dependent on whether the .NET exception class provides this info.  Returned: always  Sample: `-1` |
| **inner_exception**  dictionary | The inner exception details if there is one present.  The dict contains the same keys as a normal exception.  Returned: always |
| **message**  string | The exception message.  Returned: always  Sample: `"The method ran into an error"` |
| **source**  string | Name of the application or object that causes the error.  This may be an empty string as it’s dependent on the code that raises the exception.  Returned: always  Sample: `"C:\\Windows"` |
| **type**  string | The full .NET type of the Exception class.  Returned: always  Sample: `"System.Exception"` |
| **fully_qualified_error_id**  string | The unique identifier for the error condition  May be null if no id was specified when the record was created.  Returned: always  Sample: `"ParameterBindingFailed"` |
| **output**  string | The formatted error record message as typically seen in a PowerShell console.  Returned: always  Sample: `"Write-Error \"error\" : error\n    + CategoryInfo          : NotSpecified: (:) [Write-Error], WriteErrorException\n    + FullyQualifiedErrorId : Microsoft.PowerShell.Commands.WriteErrorException\n"` |
| **pipeline_iteration_info**  list / elements=integer | The status of the pipeline when this record was created.  The values are 0 index based.  Each element entry represents the command index in a pipeline statement.  The value of each element represents the pipeline input idx in that command.  For Example `'C:\Windows', 'C:\temp' | Get-ChildItem | Get-Item`, `[1, 2, 9]` represents an error occured with the 2nd output, 3rd, and 9th output of the 1st, 2nd, and 3rd command in that pipeline respectively.  Returned: always  Sample: `[0, 0]` |
| **script_stack_trace**  string | The script stack trace for the error record.  Returned: always  Sample: `"at <ScriptBlock>, <No file>: line 1"` |
| **target_object**  any | The object which the error occured.  May be null if no object was specified when the record was created.  Type type of this object depends on the error record itself.  If the value is a complex type, it will follow the `depth` limit specified.  Returned: always  Sample: `"C:\\Windows"` |
| **host_err**  string | The strings written to the host error output, typically the stderr.  This is not the same as objects sent to the error stream in PowerShell.  Returned: always  Sample: `"Error 1\nError 2"` |
| **host_out**  string | The strings written to the host output, typically the stdout.  This is not the same as objects sent to the output stream in PowerShell.  Returned: always  Sample: `"Line 1\nLine 2"` |
| **information**  list / elements=dictionary | A list of information records created by the script.  The information stream was only added in PowerShell v5, older versions will always have an empty list as a value.  Returned: always |
| **message_data**  complex | Message data associated with the record.  The value here can be of any type.  Returned: always  Sample: `"information record"` |
| **source**  string | The source of the record.  Returned: always  Sample: `"Write-Information"` |
| **tags**  list / elements=string | A list of tags associated with the record.  Returned: always  Sample: `["Host"]` |
| **time_generated**  string | The time the record was generated.  This is the time in UTC as an ISO 8601 formatted string.  Returned: always  Sample: `"2021-02-11T04:46:00.4694240Z"` |
| **output**  list / elements=string | A list containing all the objects outputted by the script.  The list elements can be anything as it is based on what was ran.  Returned: always  Sample: `["output 1", 2, ["inner list"], {"key": "value"}, "None"]` |
| **result**  complex | The values that were set by `$Ansible.Result` in the script.  Defaults to an empty dict but can be set to anything by the script.  Returned: always  Sample: `{"key": "value", "other key": 1}` |
| **verbose**  list / elements=string | A list of warning messages created by the script.  Verbose messages only appear when `$VerbosePreference = 'Continue'`.  Returned: always  Sample: `["verbose record"]` |
| **warning**  list / elements=string | A list of warning messages created by the script.  Warning messages only appear when `$WarningPreference = 'Continue'`.  Returned: always  Sample: `["warning record"]` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
