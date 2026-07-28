---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_template module – Create/update/delete Zabbix template"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_template_module.html
fetched_at: 2026-07-28T02:02:55+00:00
---
# community.zabbix.zabbix_template module – Create/update/delete Zabbix template

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
> see [Requirements](zabbix_template_module.md#ansible-collections-community-zabbix-zabbix-template-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_template`.

- [Synopsis](zabbix_template_module.md#synopsis)
- [Requirements](zabbix_template_module.md#requirements)
- [Parameters](zabbix_template_module.md#parameters)
- [Examples](zabbix_template_module.md#examples)

## [Synopsis](zabbix_template_module.md#id1)

- This module allows you to create, modify and delete Zabbix templates.
- Multiple templates can be created or modified at once if passing JSON or XML to module.

## [Requirements](zabbix_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **clear_templates**  list / elements=string | List of template names to be unlinked and cleared from the template.  This option is ignored if template is being created for the first time. |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **link_templates**  list / elements=string | List of template names to be linked to the template.  Templates that are not specified and are linked to the existing template will be only unlinked and not cleared from the template. |
| **macros**  list / elements=dictionary | List of user macros to create for the template.  Macros that are not specified and are present on the existing template will be replaced.  See examples on how to pass macros. |
| **macro**  string / required | Name of the macro.  Must be specified in {$NAME} format. |
| **value**  string / required | Value of the macro. |
| **state**  string | Required state of the template.  On `state=present` template will be created/imported or updated depending if it is already present.  On `state=absent` template will be deleted.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=dictionary | List of tags to assign to the template.  Providing *tags=[]* with *force=yes* will clean all of the tags from the template. |
| **tag**  string / required | Name of the template tag. |
| **value**  string | Value of the template tag.  **Default:** `""` |
| **template_groups**  list / elements=string | List of template groups to add template to when template is created.  Replaces the current template groups the template belongs to if the template is already present.  Required when creating a new template with `state=present` and *template_name* is used. Not required when updating an existing template. |
| **template_json**  json | JSON dump of templates to import.  Multiple templates can be imported this way.  Mutually exclusive with *template_name* and *template_xml*. |
| **template_name**  string | Name of Zabbix template.  Required when *template_json* or *template_xml* are not used.  Mutually exclusive with *template_json* and *template_xml*. |
| **template_xml**  string | XML dump of templates to import.  Multiple templates can be imported this way.  You are advised to pass XML structure matching the structure used by your version of Zabbix server.  Custom XML structure can be imported as long as it is valid, but may not yield consistent idempotent results on subsequent runs.  Mutually exclusive with *template_name* and *template_json*. |

## [Examples](zabbix_template_module.md#id4)

```yaml+jinja
---
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

- name: Create a new Zabbix template linked to groups, macros and templates
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_template:
    template_name: ExampleHost
    template_groups:
      - Role
      - Role2
    link_templates:
      - Example template1
      - Example template2
    macros:
      - macro: "{$EXAMPLE_MACRO1}"
        value: 30000
      - macro: "{$EXAMPLE_MACRO2}"
        value: 3
      - macro: "{$EXAMPLE_MACRO3}"
        value: "Example"
    state: present

- name: Unlink and clear templates from the existing Zabbix template
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_template:
    template_name: ExampleHost
    clear_templates:
      - Example template3
      - Example template4
    state: present

- name: Import Zabbix templates from JSON
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_template:
    template_json: "{{ lookup('file', 'zabbix_apache2.json') }}"
    state: present

- name: Import Zabbix templates from XML
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_template:
    template_xml: "{{ lookup('file', 'zabbix_apache2.xml') }}"
    state: present

- name: Import Zabbix template from Ansible dict variable
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_template:
    template_json:
      zabbix_export:
        version: "3.2"
        templates:
          - name: Template for Testing
            description: "Testing template import"
            template: Test Template
            groups:
              - name: Templates
    state: present

- name: Configure macros on the existing Zabbix template
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_template:
    template_name: Template
    macros:
      - macro: "{$TEST_MACRO}"
        value: "Example"
    state: present

- name: Add tags to the existing Zabbix template
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_template:
    template_name: Template
    tags:
      - tag: class
        value: application
    state: present

- name: Delete Zabbix template
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_template:
    template_name: Template
    state: absent
```

### Authors

- sookido (@sookido)
- Logan Vig (@logan2211)
- Dusan Matejka (@D3DeFi)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
