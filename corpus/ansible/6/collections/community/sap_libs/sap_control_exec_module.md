---
collection: ansible
version: "6"
title: "community.sap_libs.sap_control_exec module – Ansible Module to execute SAPCONTROL"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/sap_libs/sap_control_exec_module.html
fetched_at: 2026-07-27T17:21:02+00:00
---
# community.sap_libs.sap_control_exec module – Ansible Module to execute SAPCONTROL

> **Note:**
>
> This module is part of the [community.sap_libs collection](https://galaxy.ansible.com/community/sap_libs) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.sap_libs`.
>
> To use it in a playbook, specify: `community.sap_libs.sap_control_exec`.

New in community.sap_libs 1.1.0

- [Synopsis](sap_control_exec_module.md#synopsis)
- [Parameters](sap_control_exec_module.md#parameters)
- [Notes](sap_control_exec_module.md#notes)
- [Examples](sap_control_exec_module.md#examples)
- [Return Values](sap_control_exec_module.md#return-values)

## [Synopsis](sap_control_exec_module.md#id1)

- Provides support for sapstartsrv formaly known as sapcontrol
- A complete information of all functions and the parameters can be found here <https://www.sap.com/documents/2016/09/0a40e60d-8b7c-0010-82c7-eda71af511fa.html>

## [Parameters](sap_control_exec_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | Forces the execution of the function `Stop`.  Choices:   - `false` ← (default) - `true` |
| **function**  string / required | The function to execute.  Choices:   - `"Start"` - `"Stop"` - `"RestartInstance"` - `"Shutdown"` - `"InstanceStart"` - `"GetProcessList"` - `"Bootstrap"` - `"InstanceStop"` - `"StopService"` - `"StartService"` - `"RestartService"` - `"ParameterValue"` - `"GetStartProfile"` - `"GetTraceFile"` - `"GetAlertTree"` - `"GetAlerts"` - `"GetEnvironment"` - `"GetVersionInfo"` - `"GetQueueStatistic"` - `"GetInstanceProperties"` - `"ListDeveloperTraces"` - `"ReadDeveloperTrace"` - `"ListLogFiles"` - `"ReadLogFile"` - `"AnalyseLogFiles"` - `"ConfigureLogFileList"` - `"GetLogFileList"` - `"CreateSnapshot"` - `"ReadSnapshot"` - `"ListSnapshots"` - `"DeleteSnapshots"` - `"GetAccessPointList"` - `"GetProcessParameter"` - `"SetProcessParameter"` - `"SetProcessParameter2"` - `"CheckParameter"` - `"OSExecute"` - `"SendSignal"` - `"GetCallstack"` - `"GetSystemInstanceList"` - `"StartSystem"` - `"StopSystem"` - `"RestartSystem"` - `"GetSystemUpdateList"` - `"UpdateSystem"` - `"UpdateSCSInstance"` - `"CheckUpdateSystem"` - `"AccessCheck"` - `"GetSecNetworkId"` - `"GetNetworkId"` - `"RequestLogonFile"` - `"UpdateSystemPKI"` - `"UpdateInstancePSE"` - `"StorePSE"` - `"DeletePSE"` - `"CheckPSE"` - `"CreatePSECredential"` - `"HACheckConfig"` - `"HACheckFailoverConfig"` - `"HAGetFailoverConfig"` - `"HAFailoverToNode"` - `"HASetMaintenanceMode"` - `"HACheckMaintenanceMode"` - `"ABAPReadSyslog"` - `"ABAPReadRawSyslog"` - `"ABAPGetWPTable"` - `"ABAPGetComponentList"` - `"ABAPCheckRFCDestinations"` - `"ABAPGetSystemWPTable"` - `"J2EEControlProcess"` - `"J2EEControlCluster"` - `"J2EEEnableDbgSession"` - `"J2EEDisableDbgSession"` - `"J2EEGetProcessList"` - `"J2EEGetProcessList2"` - `"J2EEGetThreadList"` - `"J2EEGetThreadList2"` - `"J2EEGetThreadCallStack"` - `"J2EEGetThreadTaskStack"` - `"J2EEGetSessionList"` - `"J2EEGetCacheStatistic"` - `"J2EEGetCacheStatistic2"` - `"J2EEGetApplicationAliasList"` - `"J2EEGetComponentList"` - `"J2EEControlComponents"` - `"J2EEGetWebSessionList"` - `"J2EEGetWebSessionList2"` - `"J2EEGetEJBSessionList"` - `"J2EEGetRemoteObjectList"` - `"J2EEGetVMGCHistory"` - `"J2EEGetVMGCHistory2"` - `"J2EEGetVMHeapInfo"` - `"J2EEGetClusterMsgList"` - `"J2EEGetSharedTableInfo"` - `"ICMGetThreadList"` - `"ICMGetConnectionList"` - `"ICMGetProxyConnectionList"` - `"ICMGetCacheEntries"` - `"WebDispGetServerList"` - `"WebDispGetGroupList"` - `"WebDispGetVirtHostList"` - `"WebDispGetUrlPrefixList"` - `"EnqGetStatistic"` - `"EnqGetLockTable"` - `"EnqRemoveUserLocks"` - `"StartWait"` - `"StopWait"` - `"WaitforStarted"` - `"WaitforStopped"` - `"RestartServiceWait"` - `"WaitforServiceStarted"` - `"CheckHostAgent"` |
| **hostname**  string | The hostname to connect to the sapstartsrv.  Could be an IP address, FQDN or hostname.  Default: `"localhost"` |
| **parameter**  string | The parameter to pass to the function. |
| **password**  string | The password to connect to the sapstartsrv. |
| **port**  integer | The port number of the sapstartsrv. |
| **sysnr**  string | The system number of the instance. |
| **username**  string | The username to connect to the sapstartsrv. |

## [Notes](sap_control_exec_module.md#id3)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](sap_control_exec_module.md#id4)

```yaml+jinja
- name: GetProcessList with sysnr
  community.sap_libs.sap_control_exec:
    hostname: 192.168.8.15
    sysnr: "01"
    function: GetProcessList

- name: GetProcessList with custom port
  community.sap_libs.sap_control_exec:
    hostname: 192.168.8.15
    function: GetProcessList
    port: 50113

- name: ParameterValue
  community.sap_libs.sap_control_exec:
    hostname: 192.168.8.15
    sysnr: "01"
    username: hdbadm
    password: test1234#
    function: ParameterValue
    parameter: ztta
```

## [Return Values](sap_control_exec_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success-message with functionname.  Returned: always  Sample: `"Succesful execution of: GetProcessList"` |
| **out**  list / elements=dictionary | The full output of the required function.  Returned: always  Sample: `[{"item": [{"description": "MessageServer", "dispstatus": "SAPControl-GREEN", "elapsedtime": "412:30:50", "name": "msg_server", "pid": 70643, "starttime": "2022 03 13 15:22:42", "textstatus": "Running"}, {"description": "EnqueueServer", "dispstatus": "SAPControl-GREEN", "elapsedtime": "412:30:50", "name": "enserver", "pid": 70644, "starttime": "2022 03 13 15:22:42", "textstatus": "Running"}, {"description": "Gateway", "dispstatus": "SAPControl-GREEN", "elapsedtime": "412:30:50", "name": "gwrd", "pid": 70645, "starttime": "2022 03 13 15:22:42", "textstatus": "Running"}]}]` |

### Authors

- Rainer Leber (@RainerLeber)
- Robert Kraemer (@rkpobe)

### Collection links

[Issue Tracker](https://github.com/sap-linuxlab/community.sap_libs)
[Repository (Sources)](https://github.com/sap-linuxlab/community.sap_libs)
