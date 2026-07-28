---
collection: ansible
version: "6"
title: "vmware.vmware_rest.appliance_vmon_service_info module – Returns the state of a service."
source_url: https://docs.ansible.com/projects/ansible/6/collections/vmware/vmware_rest/appliance_vmon_service_info_module.html
fetched_at: 2026-07-28T00:22:00+00:00
---
# vmware.vmware_rest.appliance_vmon_service_info module – Returns the state of a service.

> **Note:**
>
> This module is part of the [vmware.vmware_rest collection](https://galaxy.ansible.com/vmware/vmware_rest) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vmware.vmware_rest`.
> You need further requirements to be able to use this module,
> see [Requirements](appliance_vmon_service_info_module.md#ansible-collections-vmware-vmware-rest-appliance-vmon-service-info-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.appliance_vmon_service_info`.

New in vmware.vmware_rest 2.0.0

- [Synopsis](appliance_vmon_service_info_module.md#synopsis)
- [Requirements](appliance_vmon_service_info_module.md#requirements)
- [Parameters](appliance_vmon_service_info_module.md#parameters)
- [Notes](appliance_vmon_service_info_module.md#notes)
- [Examples](appliance_vmon_service_info_module.md#examples)
- [Return Values](appliance_vmon_service_info_module.md#return-values)

## [Synopsis](appliance_vmon_service_info_module.md#id1)

- Returns the state of a service.

## [Requirements](appliance_vmon_service_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](appliance_vmon_service_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **service**  string | identifier of the service whose state is being queried.  The parameter must be the id of a resource returned by [vmware.vmware_rest.appliance_vmon_service](appliance_vmon_service_module.md#ansible-collections-vmware-vmware-rest-appliance-vmon-service-module). Required with *state=[‘get’]* |
| **session_timeout**  float  added in vmware.vmware_rest 2.1.0 | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Notes](appliance_vmon_service_info_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](appliance_vmon_service_info_module.md#id5)

```yaml+jinja
- name: Get information about a VMON service
  vmware.vmware_rest.appliance_vmon_service_info:
    service: vpxd
  register: result
```

## [Return Values](appliance_vmon_service_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **value**  list / elements=string | Get information about a VMON service  Returned: On success  Sample: `[{"key": "analytics", "value": {"description_key": "cis.analytics.ServiceDescription", "health": "HEALTHY", "health_messages": [], "name_key": "cis.analytics.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "applmgmt", "value": {"description_key": "cis.applmgmt.ServiceDescription", "health": "HEALTHY", "health_messages": [], "name_key": "cis.applmgmt.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "certificateauthority", "value": {"description_key": "cis.certificateauthority.ServiceDescription", "health": "HEALTHY", "health_messages": [{"args": ["GREEN"], "default_message": "Health is GREEN", "id": "certificateathority.health.statuscode"}], "name_key": "cis.certificateauthority.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "certificatemanagement", "value": {"description_key": "cis.certificatemanagement.ServiceDescription", "health": "HEALTHY", "health_messages": [{"args": ["GREEN"], "default_message": "Health is GREEN", "id": "certificatemanagement.health.statuscode"}], "name_key": "cis.certificatemanagement.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "cis-license", "value": {"description_key": "cis.cis-license.ServiceDescription", "health": "HEALTHY", "health_messages": [{"args": [], "default_message": "The License Service is operational.", "id": "cis.license.health.ok"}], "name_key": "cis.cis-license.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "content-library", "value": {"description_key": "cis.content-library.ServiceDescription", "health": "HEALTHY", "health_messages": [{"args": [], "default_message": "Database server connection is GREEN.", "id": "com.vmware.vdcs.vsphere-cs-lib.db_health_green"}], "name_key": "cis.content-library.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "eam", "value": {"description_key": "cis.eam.ServiceDescription", "health": "HEALTHY", "health_messages": [{"args": [], "default_message": "", "id": "cis.eam.statusOK"}], "name_key": "cis.eam.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "envoy", "value": {"description_key": "cis.envoy.ServiceDescription", "health": "HEALTHY", "health_messages": [], "name_key": "cis.envoy.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "hvc", "value": {"description_key": "cis.hvc.ServiceDescription", "health": "HEALTHY", "health_messages": [{"args": ["GREEN"], "default_message": "Health is GREEN", "id": "hvc.health.statuscode"}], "name_key": "cis.hvc.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "imagebuilder", "value": {"description_key": "cis.imagebuilder.ServiceDescription", "name_key": "cis.imagebuilder.ServiceName", "startup_type": "MANUAL", "state": "STOPPED"}}, {"key": "infraprofile", "value": {"description_key": "cis.infraprofile.ServiceDescription", "health": "HEALTHY", "health_messages": [{"args": ["GREEN"], "default_message": "Health is GREEN", "id": "infraprofile.health.statuscode"}], "name_key": "cis.infraprofile.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "lookupsvc", "value": {"description_key": "cis.lookupsvc.ServiceDescription", "health": "HEALTHY", "health_messages": [], "name_key": "cis.lookupsvc.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "netdumper", "value": {"description_key": "cis.netdumper.ServiceDescription", "name_key": "cis.netdumper.ServiceName", "startup_type": "MANUAL", "state": "STOPPED"}}, {"key": "observability-vapi", "value": {"description_key": "cis.observability-vapi.ServiceDescription", "health": "HEALTHY", "health_messages": [{"args": ["GREEN"], "default_message": "Health is GREEN", "id": "observability.health.statuscode"}], "name_key": "cis.observability-vapi.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "perfcharts", "value": {"description_key": "cis.perfcharts.ServiceDescription", "health": "HEALTHY", "health_messages": [{"args": [], "default_message": "health.statsReoptInitalizer.green", "id": "health.statsReoptInitalizer.green"}], "name_key": "cis.perfcharts.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "pschealth", "value": {"description_key": "cis.pschealth.ServiceDescription", "health": "HEALTHY", "health_messages": [], "name_key": "cis.pschealth.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "rbd", "value": {"description_key": "cis.rbd.ServiceDescription", "name_key": "cis.rbd.ServiceName", "startup_type": "MANUAL", "state": "STOPPED"}}, {"key": "rhttpproxy", "value": {"description_key": "cis.rhttpproxy.ServiceDescription", "health": "HEALTHY", "health_messages": [], "name_key": "cis.rhttpproxy.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "sca", "value": {"description_key": "cis.sca.ServiceDescription", "health": "HEALTHY", "health_messages": [], "name_key": "cis.sca.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "sps", "value": {"description_key": "cis.sps.ServiceDescription", "health": "HEALTHY", "health_messages": [], "name_key": "cis.sps.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "statsmonitor", "value": {"description_key": "cis.statsmonitor.ServiceDescription", "health": "HEALTHY", "health_messages": [{"args": [], "default_message": "Appliance monitoring service is healthy.", "id": "com.vmware.applmgmt.mon.health.healthy"}], "name_key": "cis.statsmonitor.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "sts", "value": {"description_key": "cis.sts.ServiceDescription", "health": "HEALTHY", "health_messages": [], "name_key": "cis.sts.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "topologysvc", "value": {"description_key": "cis.topologysvc.ServiceDescription", "health": "HEALTHY", "health_messages": [{"args": ["GREEN"], "default_message": "Health is GREEN", "id": "topologysvc.health.statuscode"}], "name_key": "cis.topologysvc.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "trustmanagement", "value": {"description_key": "cis.trustmanagement.ServiceDescription", "health": "HEALTHY", "health_messages": [{"args": ["GREEN"], "default_message": "Health is GREEN", "id": "trustmanagement.health.statuscode"}], "name_key": "cis.trustmanagement.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "updatemgr", "value": {"description_key": "cis.updatemgr.ServiceDescription", "health": "HEALTHY", "health_messages": [], "name_key": "cis.updatemgr.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "vapi-endpoint", "value": {"description_key": "cis.vapi-endpoint.ServiceDescription", "health": "HEALTHY", "health_messages": [{"args": ["2022-06-23T22:40:32UTC", "2022-06-23T22:40:32UTC"], "default_message": "Configuration health status is created between 2022-06-23T22:40:32UTC and 2022-06-23T22:40:32UTC.", "id": "com.vmware.vapi.endpoint.healthStatusProducedTimes"}], "name_key": "cis.vapi-endpoint.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "vcha", "value": {"description_key": "cis.vcha.ServiceDescription", "name_key": "cis.vcha.ServiceName", "startup_type": "DISABLED", "state": "STOPPED"}}, {"key": "vlcm", "value": {"description_key": "cis.vlcm.ServiceDescription", "health": "HEALTHY", "health_messages": [], "name_key": "cis.vlcm.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "vmcam", "value": {"description_key": "cis.vmcam.ServiceDescription", "name_key": "cis.vmcam.ServiceName", "startup_type": "MANUAL", "state": "STOPPED"}}, {"key": "vmonapi", "value": {"description_key": "cis.vmonapi.ServiceDescription", "health": "HEALTHY", "health_messages": [], "name_key": "cis.vmonapi.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "vmware-postgres-archiver", "value": {"description_key": "cis.vmware-postgres-archiver.ServiceDescription", "health": "HEALTHY", "health_messages": [{"args": [], "default_message": "VMware Archiver service is healthy.", "id": "cis.vmware-postgres-archiver.health.healthy"}], "name_key": "cis.vmware-postgres-archiver.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "vmware-vpostgres", "value": {"description_key": "cis.vmware-vpostgres.ServiceDescription", "health": "HEALTHY", "health_messages": [{"args": [], "default_message": "Service vmware-vpostgres is healthy.", "id": "cis.vmware-vpostgres.health.healthy"}], "name_key": "cis.vmware-vpostgres.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "vpxd", "value": {"description_key": "cis.vpxd.ServiceDescription", "health": "HEALTHY", "health_messages": [{"args": ["vCenter Server", "GREEN"], "default_message": "{0} health is {1}", "id": "vc.health.statuscode"}, {"args": ["VirtualCenter Database", "GREEN"], "default_message": "{0} health is {1}", "id": "vc.health.statuscode"}], "name_key": "cis.vpxd.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "vpxd-svcs", "value": {"description_key": "cis.vpxd-svcs.ServiceDescription", "health": "HEALTHY", "health_messages": [{"args": [], "default_message": "Tagging service is in a healthy state", "id": "cis.tagging.health.status"}], "name_key": "cis.vpxd-svcs.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "vsan-health", "value": {"description_key": "cis.vsan-health.ServiceDescription", "health": "HEALTHY", "health_messages": [], "name_key": "cis.vsan-health.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "vsm", "value": {"description_key": "cis.vsm.ServiceDescription", "health": "HEALTHY", "health_messages": [], "name_key": "cis.vsm.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "vsphere-ui", "value": {"description_key": "cis.vsphere-ui.ServiceDescription", "health": "HEALTHY", "health_messages": [], "name_key": "cis.vsphere-ui.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "vstats", "value": {"description_key": "cis.vstats.ServiceDescription", "health": "HEALTHY", "health_messages": [], "name_key": "cis.vstats.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "vtsdb", "value": {"description_key": "cis.vtsdb.ServiceDescription", "health": "HEALTHY", "health_messages": [{"args": [], "default_message": "Service vtsdb is healthy.", "id": "cis.vtsdb.health.healthy"}], "name_key": "cis.vtsdb.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}, {"key": "wcp", "value": {"description_key": "cis.wcp.ServiceDescription", "health": "HEALTHY", "health_messages": [], "name_key": "cis.wcp.ServiceName", "startup_type": "AUTOMATIC", "state": "STARTED"}}]` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
[Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
