---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_domain_permissions_profile module – Manages domain-permissions-profile objects on Checkpoint over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_domain_permissions_profile_module.html
fetched_at: 2026-07-28T01:16:08+00:00
---
# check_point.mgmt.cp_mgmt_domain_permissions_profile module – Manages domain-permissions-profile objects on Checkpoint over Web Services API

> **Note:**
>
> This module is part of the [check_point.mgmt collection](https://galaxy.ansible.com/ui/repo/published/check_point/mgmt/) (version 5.1.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install check_point.mgmt`.
>
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_domain_permissions_profile`.

New in check_point.mgmt 3.0.0

- [Synopsis](cp_mgmt_domain_permissions_profile_module.md#synopsis)
- [Parameters](cp_mgmt_domain_permissions_profile_module.md#parameters)
- [Examples](cp_mgmt_domain_permissions_profile_module.md#examples)
- [Return Values](cp_mgmt_domain_permissions_profile_module.md#return-values)

## [Synopsis](cp_mgmt_domain_permissions_profile_module.md#id1)

- Manages domain-permissions-profile objects on Checkpoint devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_domain_permissions_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_control**  dictionary | Access Control permissions.<br>Only a ‘Customized’ permission-type profile can edit these permissions. |
| **access_control_objects_and_settings**  string | Allow editing of the following objet types, VPN Community, Access Role, Custom application group,Custom application, Custom category, Limit, Application - Match Settings, Application Category - Match Settings,Override Categorization, Application and URL filtering blade - Advanced Settings, Content Awareness blade - Advanced Settings.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **app_control_and_url_filtering_update**  boolean | Install Application and URL Filtering updates.  **Choices:**   - `false` - `true` |
| **dlp_policy**  string | Configure DLP rules and Policies.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **geo_control_policy**  string | Work with Access Control rules that control traffic to and from specified countries.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **install_policy**  boolean | Install Access Control Policies.  **Choices:**   - `false` - `true` |
| **nat_policy**  string | Work with NAT in Access Control rules.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **policy_layers**  dictionary | Layer editing permissions.<br>Available only if show-policy is set to true. |
| **app_control_and_url_filtering**  boolean | Use Application and URL Filtering in Access Control rules.<br>Available only if edit-layers is set to “By Software Blades”.  **Choices:**   - `false` - `true` |
| **content_awareness**  boolean | Use specified data types in Access Control rules.<br>Available only if edit-layers is set to “By Software Blades”.  **Choices:**   - `false` - `true` |
| **edit_layers**  string | a “By Software Blades” - Edit Access Control layers that contain the blades enabled in the Permissions Profile.<br>”By Selected Profile In A Layer Editor” - Administrators can only edit the layer if the Access Control layer editor gives editing permission to their profiles.  **Choices:**   - `"By Software Blades"` - `"By Selected Profile In A Layer Editor"` |
| **firewall**  boolean | Work with Access Control and other Software Blades that do not have their own Policies.<br>Available only if edit-layers is set to “By Software Blades”.  **Choices:**   - `false` - `true` |
| **mobile_access**  boolean | Work with Mobile Access rules.<br>Available only if edit-layers is set to “By Software Blades”.  **Choices:**   - `false` - `true` |
| **qos_policy**  string | Work with QoS Policies and rules.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **show_policy**  boolean | Select to let administrators work with Access Control rules and NAT rules. If not selected, administrators cannot see these rules.  **Choices:**   - `false` - `true` |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **edit_common_objects**  boolean | Define and manage objects in the Check Point database, Network Objects, Services, Custom Application Site, VPN Community, Users, Servers, Resources, Time, UserCheck, and Limit.<br>Only a ‘Customized’ permission-type profile can edit this permission.  **Choices:**   - `false` - `true` |
| **endpoint**  dictionary | Endpoint permissions. Not supported for Multi-Domain Servers.<br>Only a ‘Customized’ permission-type profile can edit these permissions. |
| **allow_executing_push_operations**  boolean | The administrator can start operations that the Security Management Server pushes directly to client computers with no policy installation required.  **Choices:**   - `false` - `true` |
| **authorize_preboot_users**  boolean | The administrator can add and remove the users who are permitted to log on to Endpoint Security client computers with Full Disk Encryption.  **Choices:**   - `false` - `true` |
| **edit_endpoint_policies**  boolean | Available only if manage-policies-and-software-deployment is set to true.  **Choices:**   - `false` - `true` |
| **edit_software_deployment**  boolean | The administrator can define deployment rules, create packages for export, and configure advanced package settings.<br>Available only if manage-policies-and-software-deployment is set to true.  **Choices:**   - `false` - `true` |
| **manage_policies_and_software_deployment**  boolean | The administrator can work with policies, rules and actions.  **Choices:**   - `false` - `true` |
| **policies_installation**  boolean | The administrator can install policies on endpoint computers.  **Choices:**   - `false` - `true` |
| **recovery_media**  boolean | The administrator can create recovery media on endpoint computers and devices.  **Choices:**   - `false` - `true` |
| **remote_help**  boolean | The administrator can use the Remote Help feature to reset user passwords and give access to locked out users.  **Choices:**   - `false` - `true` |
| **reset_computer_data**  boolean | The administrator can reset a computer, which deletes all information about the computer from the Security Management Server.  **Choices:**   - `false` - `true` |
| **software_deployment_installation**  boolean | The administrator can deploy packages and install endpoint clients.  **Choices:**   - `false` - `true` |
| **events_and_reports**  dictionary | Events and Reports permissions.<br>Only a ‘Customized’ permission-type profile can edit these permissions. |
| **events**  string | Work with event queries on the Events tab. Create custom event queries.<br>Available only if smart-event is set to ‘Custom’.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **policy**  string | Configure SmartEvent Policy rules and install SmartEvent Policies.<br>Available only if smart-event is set to ‘Custom’.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **reports**  boolean | Create and run SmartEvent reports.<br>Available only if smart-event is set to ‘Custom’.  **Choices:**   - `false` - `true` |
| **smart_event**  string | a ‘Custom’ - Configure SmartEvent permissions.  **Choices:**   - `"custom"` - `"app control and url filtering reports only"` |
| **gateways**  dictionary | Gateways permissions. <br>Only a ‘Customized’ permission-type profile can edit these permissions. |
| **lsm_gw_db**  string | Access to objects defined in LSM gateway tables. These objects are managed in the SmartProvisioning GUI or LSMcli command-line.<br>Note, ‘Write’ permission on lsm-gw-db allows administrator to run a script on SmartLSM gateway in Expert mode.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **manage_provisioning_profiles**  string | Administrator can add, edit, delete, and assign provisioning profiles to gateways (both LSM and non-LSM).<br>Available for edit only if lsm-gw-db is set with ‘Write’ permission.<br>Note, ‘Read’ permission on lsm-gw-db enables ‘Read’ permission for manage-provisioning-profiles.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **manage_repository_scripts**  string | Add, change and remove scripts in the repository.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **open_shell**  boolean | Use the SmartConsole CLI to run commands.  **Choices:**   - `false` - `true` |
| **run_one_time_script**  boolean | Run user scripts from the command line.  **Choices:**   - `false` - `true` |
| **run_repository_script**  boolean | Run scripts from the repository.  **Choices:**   - `false` - `true` |
| **smart_update**  string | Install, update and delete Check Point licenses. This includes permissions to use SmartUpdate to manage licenses.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **system_backup**  boolean | Backup Security Gateways.  **Choices:**   - `false` - `true` |
| **system_restore**  boolean | Restore Security Gateways from saved backups.  **Choices:**   - `false` - `true` |
| **vsx_provisioning**  boolean | Create and configure Virtual Systems and other VSX virtual objects.  **Choices:**   - `false` - `true` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **management**  dictionary | Management permissions. |
| **approve_or_reject_sessions**  boolean | Approve / reject other sessions.  **Choices:**   - `false` - `true` |
| **cme_operations**  string | Permission to read / edit the Cloud Management Extension (CME) configuration.<br>Not supported for Multi-Domain Servers.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **high_availability_operations**  boolean | Configure and work with Domain High Availability.<br>Only a ‘Customized’ permission-type profile can edit this permission.  **Choices:**   - `false` - `true` |
| **manage_admins**  boolean | Controls the ability to manage Administrators, Permission Profiles, Trusted clients,API settings and Policy settings.<br>Only a “Read Write All” permission-type profile can edit this permission.<br>Not supported for Multi-Domain Servers.  **Choices:**   - `false` - `true` |
| **manage_integration_with_cloud_services**  boolean | Manage integration with Cloud Services.  **Choices:**   - `false` - `true` |
| **manage_sessions**  boolean | Lets you disconnect, discard, publish, or take over other administrator sessions.<br>Only a “Read Write All” permission-type profile can edit this permission.  **Choices:**   - `false` - `true` |
| **management_api_login**  boolean | Permission to log in to the Security Management Server and run API commands using thesetools, mgmt_cli (Linux and Windows binaries), Gaia CLI (clish) and Web Services (REST). Useful if you want to prevent administrators from running automatic scripts on the Management.<br>Note, This permission is not required to run commands from within the API terminal in SmartConsole.<br>Not supported for Multi-Domain Servers.  **Choices:**   - `false` - `true` |
| **publish_sessions**  boolean | Allow session publishing without an approval.  **Choices:**   - `false` - `true` |
| **monitoring_and_logging**  dictionary | Monitoring and Logging permissions.<br>’Customized’ permission-type profile can edit all these permissions. “Read Write All” permission-type can edit only dlp-logs-including-confidential-fields and manage-dlp-messages permissions. |
| **app_and_url_filtering_logs**  boolean | Work with Application and URL Filtering logs.  **Choices:**   - `false` - `true` |
| **dlp_logs_including_confidential_fields**  boolean | Show DLP logs including confidential fields.  **Choices:**   - `false` - `true` |
| **https_inspection_logs**  boolean | See logs generated by HTTPS Inspection.  **Choices:**   - `false` - `true` |
| **identities**  boolean | Show user and computer identity information in logs.  **Choices:**   - `false` - `true` |
| **manage_dlp_messages**  boolean | View/Release/Discard DLP messages.<br>Available only if dlp-logs-including-confidential-fields is set to true.  **Choices:**   - `false` - `true` |
| **management_logs**  string | See Multi-Domain Server audit logs.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **monitoring**  string | See monitoring views and reports.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **packet_capture_and_forensics**  boolean | See logs generated by the IPS and Forensics features.  **Choices:**   - `false` - `true` |
| **show_identities_by_default**  boolean | Show user and computer identity information in logs by default.  **Choices:**   - `false` - `true` |
| **show_packet_capture_by_default**  boolean | Enable packet capture by default.  **Choices:**   - `false` - `true` |
| **track_logs**  string | Use the log tracking features in SmartConsole.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **name**  string / required | Object name. |
| **others**  dictionary | Additional permissions.<br>Only a ‘Customized’ permission-type profile can edit these permissions. |
| **client_certificates**  boolean | Create and manage client certificates for Mobile Access.  **Choices:**   - `false` - `true` |
| **edit_cp_users_db**  boolean | Work with user accounts and groups.  **Choices:**   - `false` - `true` |
| **https_inspection**  string | Enable and configure HTTPS Inspection rules.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **ldap_users_db**  string | Work with the LDAP database and user accounts, groups and OUs.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **user_authority_access**  string | Work with Check Point User Authority authentication.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **user_device_mgmt_conf**  string | Gives access to the UDM (User & Device Management) web-based application that handles security challenges in a “bring your own device” (BYOD) workspace.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **permission_type**  string | The type of the Permissions Profile.  **Choices:**   - `"read write all"` - `"read only all"` - `"customized"` |
| **state**  string | State of the access rule (present or absent). Defaults to present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **threat_prevention**  dictionary | Threat Prevention permissions.<br>Only a ‘Customized’ permission-type profile can edit these permissions. |
| **edit_layers**  string | a ‘ALL’ - Gives permission to edit all layers.<br>”By Selected Profile In A Layer Editor” - Administrators can only edit the layer if the Threat Prevention layer editor gives editing permission to their profiles.<br>Available only if policy-layers is set to ‘Write’.  **Choices:**   - `"By Selected Profile In A Layer Editor"` - `"All"` |
| **edit_settings**  boolean | Work with general Threat Prevention settings.  **Choices:**   - `false` - `true` |
| **install_policy**  boolean | Install Policies.  **Choices:**   - `false` - `true` |
| **ips_update**  boolean | Update IPS protections.<br>Note, You do not have to log into the User Center to receive IPS updates.  **Choices:**   - `false` - `true` |
| **policy_exceptions**  string | Configure exceptions to Threat Prevention rules.<br>Note, To have policy-exceptions you must set the protections permission.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **policy_layers**  string | Configure Threat Prevention Policy rules.<br>Note, To have policy-layers permissions you must set policy-exceptionsand profiles permissions. To have ‘Write’ permissions for policy-layers, policy-exceptions must be set with ‘Write’ permission as well.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **profiles**  string | Configure Threat Prevention profiles.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **protections**  string | Work with malware protections.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_domain_permissions_profile_module.md#id3)

```yaml+jinja
- name: add-domain-permissions-profile
  cp_mgmt_domain_permissions_profile:
    name: customized profile
    state: present

- name: set-domain-permissions-profile
  cp_mgmt_domain_permissions_profile:
    access_control:
      policy_layers: By Selected Profile In A Layer Editor
    name: read profile
    permission_type: customized
    state: present

- name: delete-domain-permissions-profile
  cp_mgmt_domain_permissions_profile:
    name: profile
    state: absent
```

## [Return Values](cp_mgmt_domain_permissions_profile_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_domain_permissions_profile**  dictionary | The checkpoint object created or updated.  **Returned:** always, except when deleting the object. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
