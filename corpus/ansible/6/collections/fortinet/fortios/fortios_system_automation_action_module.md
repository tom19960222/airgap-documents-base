---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_system_automation_action module – Action for automation stitches in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_system_automation_action_module.html
fetched_at: 2026-07-27T17:44:11+00:00
---
# fortinet.fortios.fortios_system_automation_action module – Action for automation stitches in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_system_automation_action_module.md#ansible-collections-fortinet-fortios-fortios-system-automation-action-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_automation_action`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_automation_action_module.md#synopsis)
- [Requirements](fortios_system_automation_action_module.md#requirements)
- [Parameters](fortios_system_automation_action_module.md#parameters)
- [Notes](fortios_system_automation_action_module.md#notes)
- [Examples](fortios_system_automation_action_module.md#examples)
- [Return Values](fortios_system_automation_action_module.md#return-values)

## [Synopsis](fortios_system_automation_action_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and automation_action category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_automation_action_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_system_automation_action_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **system_automation_action**  dictionary | Action for automation stitches. |
| **accprofile**  string | Access profile for CLI script action to access FortiGate features. Source system.accprofile.name. |
| **action_type**  string | Action type.  Choices:   - `"email"` - `"fortiexplorer-notification"` - `"alert"` - `"disable-ssid"` - `"system-actions"` - `"quarantine"` - `"quarantine-forticlient"` - `"quarantine-nsx"` - `"quarantine-fortinac"` - `"ban-ip"` - `"aws-lambda"` - `"azure-function"` - `"google-cloud-function"` - `"alicloud-function"` - `"webhook"` - `"cli-script"` - `"slack-notification"` - `"microsoft-teams-notification"` - `"ios-notification"` |
| **alicloud_access_key_id**  string | AliCloud AccessKey ID. |
| **alicloud_access_key_secret**  string | AliCloud AccessKey secret. |
| **alicloud_account_id**  string | AliCloud account ID. |
| **alicloud_function**  string | AliCloud function name. |
| **alicloud_function_authorization**  string | AliCloud function authorization type.  Choices:   - `"anonymous"` - `"function"` |
| **alicloud_function_domain**  string | AliCloud function domain. |
| **alicloud_region**  string | AliCloud region. |
| **alicloud_service**  string | AliCloud service name. |
| **alicloud_version**  string | AliCloud version. |
| **aws_api_id**  string | AWS API Gateway ID. |
| **aws_api_key**  string | AWS API Gateway API key. |
| **aws_api_path**  string | AWS API Gateway path. |
| **aws_api_stage**  string | AWS API Gateway deployment stage name. |
| **aws_domain**  string | AWS domain. |
| **aws_region**  string | AWS region. |
| **azure_api_key**  string | Azure function API key. |
| **azure_app**  string | Azure function application name. |
| **azure_domain**  string | Azure function domain. |
| **azure_function**  string | Azure function name. |
| **azure_function_authorization**  string | Azure function authorization level.  Choices:   - `"anonymous"` - `"function"` - `"admin"` |
| **delay**  integer | Delay before execution (in seconds). |
| **description**  string | Description. |
| **email_body**  string | Email body. |
| **email_from**  string | Email sender name. |
| **email_subject**  string | Email subject. |
| **email_to**  list / elements=dictionary | Email addresses. |
| **name**  string | Email address. |
| **execute_security_fabric**  string | Enable/disable execution of CLI script on all or only one FortiGate unit in the Security Fabric.  Choices:   - `"enable"` - `"disable"` |
| **fos_message**  string | Message content. |
| **gcp_function**  string | Google Cloud function name. |
| **gcp_function_domain**  string | Google Cloud function domain. |
| **gcp_function_region**  string | Google Cloud function region. |
| **gcp_project**  string | Google Cloud Platform project name. |
| **headers**  list / elements=dictionary | Request headers. |
| **header**  string | Request header. |
| **http_body**  string | Request body (if necessary). Should be serialized json string. |
| **http_headers**  list / elements=dictionary | Request headers. |
| **id**  integer | Entry ID. |
| **key**  string | Request header key. |
| **value**  string | Request header value. |
| **message_type**  string | Message type.  Choices:   - `"text"` - `"json"` |
| **method**  string | Request method (POST, PUT, GET, PATCH or DELETE).  Choices:   - `"post"` - `"put"` - `"get"` - `"patch"` - `"delete"` |
| **minimum_interval**  integer | Limit execution to no more than once in this interval (in seconds). |
| **name**  string / required | Name. |
| **output_size**  integer | Number of megabytes to limit script output to (1 - 1024). |
| **port**  integer | Protocol port. |
| **protocol**  string | Request protocol.  Choices:   - `"http"` - `"https"` |
| **replacement_message**  string | Enable/disable replacement message.  Choices:   - `"enable"` - `"disable"` |
| **replacemsg_group**  string | Replacement message group. Source system.replacemsg-group.name. |
| **required**  string | Required in action chain.  Choices:   - `"enable"` - `"disable"` |
| **script**  string | CLI script. |
| **sdn_connector**  list / elements=dictionary | NSX SDN connector names. |
| **name**  string | SDN connector name. Source system.sdn-connector.name. |
| **security_tag**  string | NSX security tag. |
| **system_action**  string | System action type.  Choices:   - `"reboot"` - `"shutdown"` - `"backup-config"` |
| **timeout**  integer | Maximum running time for this script in seconds (0 = no timeout). |
| **tls_certificate**  string | Custom TLS certificate for API request. Source certificate.local.name. |
| **uri**  string | Request API URI. |
| **verify_host_cert**  string | Enable/disable verification of the remote host certificate.  Choices:   - `"enable"` - `"disable"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_system_automation_action_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_automation_action_module.md#id5)

```yaml+jinja
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Action for automation stitches.
    fortios_system_automation_action:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_automation_action:
        accprofile: "<your_own_value> (source system.accprofile.name)"
        action_type: "email"
        alicloud_access_key_id: "<your_own_value>"
        alicloud_access_key_secret: "<your_own_value>"
        alicloud_account_id: "<your_own_value>"
        alicloud_function: "<your_own_value>"
        alicloud_function_authorization: "anonymous"
        alicloud_function_domain: "<your_own_value>"
        alicloud_region: "<your_own_value>"
        alicloud_service: "<your_own_value>"
        alicloud_version: "<your_own_value>"
        aws_api_id: "<your_own_value>"
        aws_api_key: "<your_own_value>"
        aws_api_path: "<your_own_value>"
        aws_api_stage: "<your_own_value>"
        aws_domain: "<your_own_value>"
        aws_region: "<your_own_value>"
        azure_api_key: "<your_own_value>"
        azure_app: "<your_own_value>"
        azure_domain: "<your_own_value>"
        azure_function: "<your_own_value>"
        azure_function_authorization: "anonymous"
        delay: "0"
        description: "<your_own_value>"
        email_body: "<your_own_value>"
        email_from: "<your_own_value>"
        email_subject: "<your_own_value>"
        email_to:
         -
            name: "default_name_31"
        execute_security_fabric: "enable"
        fos_message: "<your_own_value>"
        gcp_function: "<your_own_value>"
        gcp_function_domain: "<your_own_value>"
        gcp_function_region: "<your_own_value>"
        gcp_project: "<your_own_value>"
        headers:
         -
            header: "<your_own_value>"
        http_body: "<your_own_value>"
        http_headers:
         -
            id:  "42"
            key: "<your_own_value>"
            value: "<your_own_value>"
        message_type: "text"
        method: "post"
        minimum_interval: "0"
        name: "default_name_48"
        output_size: "10"
        port: "0"
        protocol: "http"
        replacement_message: "enable"
        replacemsg_group: "<your_own_value> (source system.replacemsg-group.name)"
        required: "enable"
        script: "<your_own_value>"
        sdn_connector:
         -
            name: "default_name_57 (source system.sdn-connector.name)"
        security_tag: "<your_own_value>"
        system_action: "reboot"
        timeout: "0"
        tls_certificate: "<your_own_value> (source certificate.local.name)"
        uri: "<your_own_value>"
        verify_host_cert: "enable"
```

## [Return Values](fortios_system_automation_action_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
