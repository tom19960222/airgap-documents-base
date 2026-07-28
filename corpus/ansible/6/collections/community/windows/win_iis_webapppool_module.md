---
collection: ansible
version: "6"
title: "community.windows.win_iis_webapppool module – Configure IIS Web Application Pools"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_iis_webapppool_module.html
fetched_at: 2026-07-27T17:23:31+00:00
---
# community.windows.win_iis_webapppool module – Configure IIS Web Application Pools

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_iis_webapppool`.

- [Synopsis](win_iis_webapppool_module.md#synopsis)
- [Parameters](win_iis_webapppool_module.md#parameters)
- [See Also](win_iis_webapppool_module.md#see-also)
- [Examples](win_iis_webapppool_module.md#examples)
- [Return Values](win_iis_webapppool_module.md#return-values)

## [Synopsis](win_iis_webapppool_module.md#id1)

- Creates, removes and configures an IIS Web Application Pool.

## [Parameters](win_iis_webapppool_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attributes**  string | This field is a free form dictionary value for the application pool attributes.  These attributes are based on the naming standard at <https://www.iis.net/configreference/system.applicationhost/applicationpools/add#005>, see the examples section for more details on how to set this.  You can also set the attributes of child elements like cpu and processModel, see the examples to see how it is done.  While you can use the numeric values for enums it is recommended to use the enum name itself, e.g. use SpecificUser instead of 3 for processModel.identityType.  managedPipelineMode may be either “Integrated” or “Classic”.  startMode may be either “OnDemand” or “AlwaysRunning”.  Use `state` module parameter to modify the state of the app pool.  When trying to set ‘processModel.password’ and you receive a ‘Value does fall within the expected range’ error, you have a corrupted keystore. Please follow <http://structuredsight.com/2014/10/26/im-out-of-range-youre-out-of-range/> to help fix your host. |
| **name**  string / required | Name of the application pool. |
| **state**  string | The state of the application pool.  If `absent` will ensure the app pool is removed.  If `present` will ensure the app pool is configured and exists.  If `restarted` will ensure the app pool exists and will restart, this is never idempotent.  If `started` will ensure the app pool exists and is started.  If `stopped` will ensure the app pool exists and is stopped.  Choices:   - `"absent"` - `"present"` ← (default) - `"restarted"` - `"started"` - `"stopped"` |

## [See Also](win_iis_webapppool_module.md#id3)

> **See also:**
>
> [community.windows.win_iis_virtualdirectory](win_iis_virtualdirectory_module.md#ansible-collections-community-windows-win-iis-virtualdirectory-module)
> :   Configures a virtual directory in IIS.
>
> [community.windows.win_iis_webapplication](win_iis_webapplication_module.md#ansible-collections-community-windows-win-iis-webapplication-module)
> :   Configures IIS web applications.
>
> [community.windows.win_iis_webbinding](win_iis_webbinding_module.md#ansible-collections-community-windows-win-iis-webbinding-module)
> :   Configures a IIS Web site binding.
>
> [community.windows.win_iis_website](win_iis_website_module.md#ansible-collections-community-windows-win-iis-website-module)
> :   Configures a IIS Web site.

## [Examples](win_iis_webapppool_module.md#id4)

```yaml+jinja
- name: Return information about an existing application pool
  community.windows.win_iis_webapppool:
    name: DefaultAppPool
    state: present

- name: Create a new application pool in 'Started' state
  community.windows.win_iis_webapppool:
    name: AppPool
    state: started

- name: Stop an application pool
  community.windows.win_iis_webapppool:
    name: AppPool
    state: stopped

- name: Restart an application pool (non-idempotent)
  community.windows.win_iis_webapppool:
    name: AppPool
    state: restarted

- name: Change application pool attributes using new dict style
  community.windows.win_iis_webapppool:
    name: AppPool
    attributes:
      managedRuntimeVersion: v4.0
      autoStart: no

- name: Creates an application pool, sets attributes and starts it
  community.windows.win_iis_webapppool:
    name: AnotherAppPool
    state: started
    attributes:
      managedRuntimeVersion: v4.0
      autoStart: no

# In the below example we are setting attributes in child element processModel
# https://www.iis.net/configreference/system.applicationhost/applicationpools/add/processmodel
- name: Manage child element and set identity of application pool
  community.windows.win_iis_webapppool:
    name: IdentitiyAppPool
    state: started
    attributes:
      managedPipelineMode: Classic
      processModel.identityType: SpecificUser
      processModel.userName: '{{ansible_user}}'
      processModel.password: '{{ansible_password}}'
      processModel.loadUserProfile: true

- name: Manage a timespan attribute
  community.windows.win_iis_webapppool:
    name: TimespanAppPool
    state: started
    attributes:
      # Timespan with full string "day:hour:minute:second.millisecond"
      recycling.periodicRestart.time: "00:00:05:00.000000"
      recycling.periodicRestart.schedule: ["00:10:00", "05:30:00"]
      # Shortened timespan "hour:minute:second"
      processModel.pingResponseTime: "00:03:00"
```

## [Return Values](win_iis_webapppool_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **attributes**  dictionary | Application Pool attributes that were set and processed by this module invocation.  Returned: success  Sample: `{"enable32BitAppOnWin64": "true", "managedPipelineMode": "Classic", "managedRuntimeVersion": "v4.0"}` |
| **info**  complex | Information on current state of the Application Pool. See <https://www.iis.net/configreference/system.applicationhost/applicationpools/add#005> for the full list of return attributes based on your IIS version.  Returned: success |
| **attributes**  dictionary | Key value pairs showing the current Application Pool attributes.  Returned: success  Sample: `{"CLRConfigFile": "", "applicationPoolSid": "S-1-5-82-1352790163-598702362-1775843902-1923651883-1762956711", "autoStart": true, "enable32BitAppOnWin64": true, "enableConfigurationOverride": true, "managedPipelineMode": "Classic", "managedRuntimeLoader": "webengine4.dll", "managedRuntimeVersion": "v4.0", "name": "DefaultAppPool", "passAnonymousToken": true, "queueLength": 1000, "startMode": "OnDemand", "state": "Started"}` |
| **cpu**  dictionary | Key value pairs showing the current Application Pool cpu attributes.  Returned: success  Sample: `{"action": "NoAction", "limit": 0, "resetInterval": {"Days": 0, "Hours": 0}}` |
| **failure**  dictionary | Key value pairs showing the current Application Pool failure attributes.  Returned: success  Sample: `{"autoShutdownExe": "", "orphanActionExe": "", "rapidFailProtextionInterval": {"Days": 0, "Hours": 0}}` |
| **name**  string | Name of Application Pool that was processed by this module invocation.  Returned: success  Sample: `"DefaultAppPool"` |
| **processModel**  dictionary | Key value pairs showing the current Application Pool processModel attributes.  Returned: success  Sample: `{"identityType": "ApplicationPoolIdentity", "logonType": "LogonBatch", "pingInterval": {"Days": 0, "Hours": 0}}` |
| **recycling**  dictionary | Key value pairs showing the current Application Pool recycling attributes.  Returned: success  Sample: `{"disallowOverlappingRotation": false, "disallowRotationOnConfigChange": false, "logEventOnRecycle": "Time,Requests,Schedule,Memory,IsapiUnhealthy,OnDemand,ConfigChange,PrivateMemory"}` |
| **state**  string | Current runtime state of the pool as the module completed.  Returned: success  Sample: `"Started"` |

### Authors

- Henrik Wallström (@henrikwallstrom)
- Jordan Borean (@jborean93)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
