---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_template_info module – Gather information about Zabbix template"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_template_info_module.html
fetched_at: 2026-07-28T02:02:56+00:00
---
# community.zabbix.zabbix_template_info module – Gather information about Zabbix template

> **Note:**
>
> This module is part of the [community.zabbix collection](https://galaxy.ansible.com/ui/repo/published/community/zabbix/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.zabbix`.
> You need further requirements to be able to use this module,
> see [Requirements](zabbix_template_info_module.md#ansible-collections-community-zabbix-zabbix-template-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_template_info`.

- [Synopsis](zabbix_template_info_module.md#synopsis)
- [Requirements](zabbix_template_info_module.md#requirements)
- [Parameters](zabbix_template_info_module.md#parameters)
- [Examples](zabbix_template_info_module.md#examples)
- [Return Values](zabbix_template_info_module.md#return-values)

## [Synopsis](zabbix_template_info_module.md#id1)

- This module allows you to search for Zabbix template.

## [Requirements](zabbix_template_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_template_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **format**  string | Format to use when dumping template.  **Choices:**   - `"json"` ← (default) - `"xml"` - `"yaml"` - `"none"` |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **omit_date**  boolean | Removes the date field for the dumped template  **Choices:**   - `false` ← (default) - `true` |
| **template_name**  string / required | Name of the template in Zabbix. |

## [Examples](zabbix_template_info_module.md#id4)

```yaml+jinja
# If you want to use Username and Password to be authenticated by Zabbix Server
- name: Set credentials to access Zabbix Server API
  ansible.builtin.set_fact:
    ansible_user: Admin
    ansible_httpapi_pass: zabbix

# If you want to use API token to be authenticated by Zabbix Server
# https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/general#api-tokens
- name: Set API token
  ansible.builtin.set_fact:
    ansible_zabbix_auth_key: 8ec0d52432c15c91fcafe9888500cf9a607f44091ab554dbee860f6b44fac895

- name: Get Zabbix template as JSON
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_template_info:
    template_name: Template
    format: json
    omit_date: yes
  register: template_json

- name: Get Zabbix template as XML
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_template_info:
    template_name: Template
    format: xml
    omit_date: no
  register: template_json

- name: Get Zabbix template as YAML
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_template_info:
    template_name: Template
    format: yaml
    omit_date: no
  register: template_yaml

- name: Determine if Zabbix template exists
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_template_info:
    template_name: Template
    format: none
  register: template
```

## [Return Values](zabbix_template_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **template_id**  string | The ID of the template  **Returned:** always |
| **template_json**  string | The JSON of the template  **Returned:** when format is json and omit_date is true  **Sample:** `"{'changed': False, 'failed': False, 'template_id': '10529', 'template_json': {'zabbix_export': {'groups': [{'name': 'Templates', 'uuid': '7df96b18c230490a9a0a9e2307226338'}], 'templates': [{'groups': [{'name': 'Templates'}], 'name': 'ExampleTemplateForTempleteInfoModule', 'template': 'ExampleTemplateForTempleteInfoModule', 'uuid': '615e9b0662bb4399a2503a9aaa743517'}], 'version': '6.0'}}}"` |
| **template_xml**  string | The XML of the template  **Returned:** when format is xml and omit_date is false  **Sample:** `"<zabbix_export>\n    <version>6.0</version>\n    <groups>\n        <group>\n            <uuid>7df96b18c230490a9a0a9e2307226338</uuid>\n            <name>Templates</name>\n        </group>\n    </groups>\n    <templates>\n        <template>\n            <uuid>9a83162273f74032a1005fdb13943038</uuid>\n            <template>ExampleTemplateForTempleteInfoModule</template>\n            <name>ExampleTemplateForTempleteInfoModule</name>\n            <groups>\n                <group>\n                    <name>Templates</name>\n                </group>\n            </groups>\n        </template>\n    </templates>\n</zabbix_export>"` |
| **template_yaml**  string | The YAML of the template  **Returned:** when format is yaml and omit_date is false  **Sample:** `"zabbix_export:\n  version: \"6.0\"\n  groups:\n    -\n      uuid: 7df96b18c230490a9a0a9e2307226338\n      name: Templates\n      templates:\n        -\n          uuid: 67b075276bf047d3aeb8f7d5c2121c6a\n          template: ExampleTemplateForTempleteInfoModule\n          name: ExampleTemplateForTempleteInfoModule\n          groups:\n            -\n              name: Templatesn"` |

### Authors

- sky-joker (@sky-joker)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
