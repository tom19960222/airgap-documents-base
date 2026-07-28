---
collection: ansible
version: "8"
title: "Telekom_Mms.Icinga_Director"
source_url: https://docs.ansible.com/projects/ansible/8/collections/telekom_mms/icinga_director/index.html
fetched_at: 2026-07-28T01:03:00+00:00
---
# Telekom_Mms.Icinga_Director

Collection version 1.35.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

This collection contains Ansible modules to change objects in Icinga 2 using the director API.

**Authors:**

- Sebastian Gumprich <[sebastian.gumprich@telekom.de](mailto:sebastian.gumprich%40telekom.de)>
- Lars Krahl <[lars.krahl@telekom.de](mailto:lars.krahl%40telekom.de)>

**Supported ansible-core versions:**

- 2.9.10 or newer

- [Issue Tracker](https://github.com/telekom-mms/ansible-collection-icinga-director/issues)
- [Repository (Sources)](https://github.com/telekom-mms/ansible-collection-icinga-director)

## [Plugin Index](index.md#id2)

These are the plugins in the telekom_mms.icinga_director collection:

### Modules

- [icinga_command module](icinga_command_module.md#ansible-collections-telekom-mms-icinga-director-icinga-command-module) – Manage commands in Icinga2
- [icinga_command_info module](icinga_command_info_module.md#ansible-collections-telekom-mms-icinga-director-icinga-command-info-module) – Query commands in Icinga2
- [icinga_command_template module](icinga_command_template_module.md#ansible-collections-telekom-mms-icinga-director-icinga-command-template-module) – Manage command templates in Icinga2
- [icinga_command_template_info module](icinga_command_template_info_module.md#ansible-collections-telekom-mms-icinga-director-icinga-command-template-info-module) – Query command templates in Icinga2
- [icinga_deploy module](icinga_deploy_module.md#ansible-collections-telekom-mms-icinga-director-icinga-deploy-module) – Trigger deployment in Icinga2
- [icinga_deploy_info module](icinga_deploy_info_module.md#ansible-collections-telekom-mms-icinga-director-icinga-deploy-info-module) – Get deployment information through the director API
- [icinga_endpoint module](icinga_endpoint_module.md#ansible-collections-telekom-mms-icinga-director-icinga-endpoint-module) – Manage endpoints in Icinga2
- [icinga_endpoint_info module](icinga_endpoint_info_module.md#ansible-collections-telekom-mms-icinga-director-icinga-endpoint-info-module) – Query endpoints in Icinga2
- [icinga_host module](icinga_host_module.md#ansible-collections-telekom-mms-icinga-director-icinga-host-module) – Manage hosts in Icinga2
- [icinga_host_info module](icinga_host_info_module.md#ansible-collections-telekom-mms-icinga-director-icinga-host-info-module) – Query hosts in Icinga2
- [icinga_host_template module](icinga_host_template_module.md#ansible-collections-telekom-mms-icinga-director-icinga-host-template-module) – Manage host templates in Icinga2
- [icinga_host_template_info module](icinga_host_template_info_module.md#ansible-collections-telekom-mms-icinga-director-icinga-host-template-info-module) – Query host templates in Icinga2
- [icinga_hostgroup module](icinga_hostgroup_module.md#ansible-collections-telekom-mms-icinga-director-icinga-hostgroup-module) – Manage hostgroups in Icinga2
- [icinga_hostgroup_info module](icinga_hostgroup_info_module.md#ansible-collections-telekom-mms-icinga-director-icinga-hostgroup-info-module) – Query hostgroups in Icinga2
- [icinga_notification module](icinga_notification_module.md#ansible-collections-telekom-mms-icinga-director-icinga-notification-module) – Manage notifications in Icinga2
- [icinga_notification_info module](icinga_notification_info_module.md#ansible-collections-telekom-mms-icinga-director-icinga-notification-info-module) – Query notifications in Icinga2
- [icinga_notification_template module](icinga_notification_template_module.md#ansible-collections-telekom-mms-icinga-director-icinga-notification-template-module) – Manage notification templates in Icinga2
- [icinga_notification_template_info module](icinga_notification_template_info_module.md#ansible-collections-telekom-mms-icinga-director-icinga-notification-template-info-module) – Query notification templates in Icinga2
- [icinga_scheduled_downtime module](icinga_scheduled_downtime_module.md#ansible-collections-telekom-mms-icinga-director-icinga-scheduled-downtime-module) – Manage downtimes in Icinga2
- [icinga_service module](icinga_service_module.md#ansible-collections-telekom-mms-icinga-director-icinga-service-module) – Manage services in Icinga2
- [icinga_service_apply module](icinga_service_apply_module.md#ansible-collections-telekom-mms-icinga-director-icinga-service-apply-module) – Manage service apply rules in Icinga2
- [icinga_service_apply_info module](icinga_service_apply_info_module.md#ansible-collections-telekom-mms-icinga-director-icinga-service-apply-info-module) – Query service apply rules in Icinga2
- [icinga_service_info module](icinga_service_info_module.md#ansible-collections-telekom-mms-icinga-director-icinga-service-info-module) – Query services in Icinga2
- [icinga_service_template module](icinga_service_template_module.md#ansible-collections-telekom-mms-icinga-director-icinga-service-template-module) – Manage service templates in Icinga2
- [icinga_service_template_info module](icinga_service_template_info_module.md#ansible-collections-telekom-mms-icinga-director-icinga-service-template-info-module) – Query service templates in Icinga2
- [icinga_servicegroup module](icinga_servicegroup_module.md#ansible-collections-telekom-mms-icinga-director-icinga-servicegroup-module) – Manage servicegroups in Icinga2
- [icinga_servicegroup_info module](icinga_servicegroup_info_module.md#ansible-collections-telekom-mms-icinga-director-icinga-servicegroup-info-module) – Query servicegroups in Icinga2
- [icinga_serviceset module](icinga_serviceset_module.md#ansible-collections-telekom-mms-icinga-director-icinga-serviceset-module) – Manage servicesets in Icinga2
- [icinga_timeperiod module](icinga_timeperiod_module.md#ansible-collections-telekom-mms-icinga-director-icinga-timeperiod-module) – Manage timeperiods in Icinga2
- [icinga_timeperiod_info module](icinga_timeperiod_info_module.md#ansible-collections-telekom-mms-icinga-director-icinga-timeperiod-info-module) – Query timeperiods in Icinga2
- [icinga_timeperiod_template module](icinga_timeperiod_template_module.md#ansible-collections-telekom-mms-icinga-director-icinga-timeperiod-template-module) – Manage timeperiod templates in Icinga2
- [icinga_timeperiod_template_info module](icinga_timeperiod_template_info_module.md#ansible-collections-telekom-mms-icinga-director-icinga-timeperiod-template-info-module) – Query timeperiod templates in Icinga2
- [icinga_user module](icinga_user_module.md#ansible-collections-telekom-mms-icinga-director-icinga-user-module) – Manage users in Icinga2
- [icinga_user_group module](icinga_user_group_module.md#ansible-collections-telekom-mms-icinga-director-icinga-user-group-module) – Manage users groups in Icinga2
- [icinga_user_group_info module](icinga_user_group_info_module.md#ansible-collections-telekom-mms-icinga-director-icinga-user-group-info-module) – Query user groups in Icinga2
- [icinga_user_info module](icinga_user_info_module.md#ansible-collections-telekom-mms-icinga-director-icinga-user-info-module) – Query users in Icinga2
- [icinga_user_template module](icinga_user_template_module.md#ansible-collections-telekom-mms-icinga-director-icinga-user-template-module) – Manage user templates in Icinga2
- [icinga_user_template_info module](icinga_user_template_info_module.md#ansible-collections-telekom-mms-icinga-director-icinga-user-template-info-module) – Query user templates in Icinga2
- [icinga_zone module](icinga_zone_module.md#ansible-collections-telekom-mms-icinga-director-icinga-zone-module) – Manage zones in Icinga2
- [icinga_zone_info module](icinga_zone_info_module.md#ansible-collections-telekom-mms-icinga-director-icinga-zone-info-module) – Query zones in Icinga2

### Inventory Plugins

- [icinga_director_inventory inventory](icinga_director_inventory_inventory.md#ansible-collections-telekom-mms-icinga-director-icinga-director-inventory-inventory) – Returns Ansible inventory from Icinga

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
