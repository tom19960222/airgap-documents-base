---
collection: ansible
version: "6"
title: "community.zabbix.zabbix_template module – Create/update/delete/dump Zabbix template"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_template_module.html
fetched_at: 2026-07-27T17:24:21+00:00
---
# community.zabbix.zabbix_template module – Create/update/delete/dump Zabbix template

> **Note:**
>
> This module is part of the [community.zabbix collection](https://galaxy.ansible.com/community/zabbix) (version 1.9.0).
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
- [Notes](zabbix_template_module.md#notes)
- [Examples](zabbix_template_module.md#examples)
- [Return Values](zabbix_template_module.md#return-values)

## [Synopsis](zabbix_template_module.md#id1)

- This module allows you to create, modify, delete and dump Zabbix templates.
- Multiple templates can be created or modified at once if passing JSON or XML to module.

## [Requirements](zabbix_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](zabbix_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **clear_templates**  list / elements=string | List of template names to be unlinked and cleared from the template.  This option is ignored if template is being created for the first time. |
| **dump_format**  string | Format to use when dumping template with `state=dump`.  This option is deprecated and will eventually be removed in 2.14.  Choices:   - `"json"` ← (default) - `"xml"` |
| **link_templates**  list / elements=string | List of template names to be linked to the template.  Templates that are not specified and are linked to the existing template will be only unlinked and not cleared from the template. |
| **login_password**  string | Zabbix user password.  If not set the environment variable `ZABBIX_PASSWORD` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **login_user**  string | Zabbix user name.  If not set the environment variable `ZABBIX_USERNAME` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **macros**  list / elements=dictionary | List of user macros to create for the template.  Macros that are not specified and are present on the existing template will be replaced.  See examples on how to pass macros. |
| **macro**  string / required | Name of the macro.  Must be specified in {$NAME} format. |
| **value**  string / required | Value of the macro. |
| **omit_date**  boolean | Removes the date field for the exported/dumped template  Requires `state=dump`  Choices:   - `false` ← (default) - `true` |
| **server_url**  aliases: url  string | URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.  If not set the environment variable `ZABBIX_SERVER` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **state**  string | Required state of the template.  On `state=present` template will be created/imported or updated depending if it is already present.  On `state=dump` template content will get dumped into required format specified in *dump_format*.  On `state=absent` template will be deleted.  The `state=dump` is deprecated and will be removed in 2.14. The [community.zabbix.zabbix_template_info](zabbix_template_info_module.md#ansible-collections-community-zabbix-zabbix-template-info-module) module should be used instead.  Choices:   - `"present"` ← (default) - `"absent"` - `"dump"` |
| **tags**  list / elements=dictionary | List of tags to assign to the template.  Works only with >= Zabbix 4.2.  Providing *tags=[]* with *force=yes* will clean all of the tags from the template. |
| **tag**  string / required | Name of the template tag. |
| **value**  string | Value of the template tag.  Default: `""` |
| **template_groups**  list / elements=string | List of template groups to add template to when template is created.  Replaces the current template groups the template belongs to if the template is already present.  Required when creating a new template with `state=present` and *template_name* is used. Not required when updating an existing template. |
| **template_json**  json | JSON dump of templates to import.  Multiple templates can be imported this way.  Mutually exclusive with *template_name* and *template_xml*. |
| **template_name**  string | Name of Zabbix template.  Required when *template_json* or *template_xml* are not used.  Mutually exclusive with *template_json* and *template_xml*. |
| **template_xml**  string | XML dump of templates to import.  Multiple templates can be imported this way.  You are advised to pass XML structure matching the structure used by your version of Zabbix server.  Custom XML structure can be imported as long as it is valid, but may not yield consistent idempotent results on subsequent runs.  Mutually exclusive with *template_name* and *template_json*. |
| **timeout**  integer | The timeout of API request (seconds).  This option is deprecated with the move to httpapi connection and will be removed in the next release  Default: `10` |
| **validate_certs**  boolean | If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If not set the environment variable `ZABBIX_VALIDATE_CERTS` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release  Choices:   - `false` - `true` ← (default) |

## [Notes](zabbix_template_module.md#id4)

> **Note:**
>
> - there where breaking changes in the Zabbix API with version 5.4 onwards (especially UUIDs) which may require you to export the templates again (see version tag >= 5.4 in the resulting file/data).
> - If you use *login_password=zabbix*, the word “zabbix” is replaced by “\*\*\*\*\*\*\*\*” in all module output, because *login_password* uses `no_log`. See [this FAQ](https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-is-my-output-sometimes-replaced-with) for more information.

## [Examples](zabbix_template_module.md#id5)

```yaml+jinja
---
# Set following variables for Zabbix Server host in play or inventory
- name: Set connection specific variables
  set_fact:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 80
    ansible_httpapi_use_ssl: false
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: 'zabbixeu'  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu

# If you want to use Username and Password to be authenticated by Zabbix Server
- name: Set credentials to access Zabbix Server API
  set_fact:
    ansible_user: Admin
    ansible_httpapi_pass: zabbix

# If you want to use API token to be authenticated by Zabbix Server
# https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/general#api-tokens
- name: Set API token
  set_fact:
    ansible_zabbix_auth_key: 8ec0d52432c15c91fcafe9888500cf9a607f44091ab554dbee860f6b44fac895

- name: Create a new Zabbix template linked to groups, macros and templates
  community.zabbix.zabbix_template:
    template_name: ExampleHost
    template_groups:
      - Role
      - Role2
    link_templates:
      - Example template1
      - Example template2
    macros:
      - macro: '{$EXAMPLE_MACRO1}'
        value: 30000
      - macro: '{$EXAMPLE_MACRO2}'
        value: 3
      - macro: '{$EXAMPLE_MACRO3}'
        value: 'Example'
    state: present

- name: Unlink and clear templates from the existing Zabbix template
  community.zabbix.zabbix_template:
    template_name: ExampleHost
    clear_templates:
      - Example template3
      - Example template4
    state: present

- name: Import Zabbix templates from JSON
  community.zabbix.zabbix_template:
    template_json: "{{ lookup('file', 'zabbix_apache2.json') }}"
    state: present

- name: Import Zabbix templates from XML
  community.zabbix.zabbix_template:
    template_xml: "{{ lookup('file', 'zabbix_apache2.xml') }}"
    state: present

- name: Import Zabbix template from Ansible dict variable
  community.zabbix.zabbix_template:
    template_json:
      zabbix_export:
        version: '3.2'
        templates:
          - name: Template for Testing
            description: 'Testing template import'
            template: Test Template
            groups:
              - name: Templates
            applications:
              - name: Test Application
    state: present

- name: Configure macros on the existing Zabbix template
  community.zabbix.zabbix_template:
    template_name: Template
    macros:
      - macro: '{$TEST_MACRO}'
        value: 'Example'
    state: present

- name: Add tags to the existing Zabbix template
  community.zabbix.zabbix_template:
    template_name: Template
    tags:
      - tag: class
        value: application
    state: present

- name: Delete Zabbix template
  community.zabbix.zabbix_template:
    template_name: Template
    state: absent

- name: Dump Zabbix template as JSON
  community.zabbix.zabbix_template:
    template_name: Template
    omit_date: yes
    state: dump
  register: template_dump

- name: Dump Zabbix template as XML
  community.zabbix.zabbix_template:
    template_name: Template
    dump_format: xml
    omit_date: false
    state: dump
  register: template_dump
```

## [Return Values](zabbix_template_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **template_json**  string | The JSON dump of the template  Returned: when state is dump and omit_date is no  Sample: `"{'zabbix_export': {'date': '2017-11-29T16:37:24Z', 'groups': [{'name': 'Templates'}], 'templates': [{'applications': [], 'description': '', 'discovery_rules': [], 'groups': [{'name': 'Templates'}], 'httptests': [], 'items': [], 'macros': [], 'name': 'Test Template', 'screens': [], 'template': 'test', 'templates': []}], 'version': '3.2'}}"` |
| **template_xml**  string | dump of the template in XML representation  Returned: when state is dump, dump_format is xml and omit_date is yes  Sample: `"<?xml version=\"1.0\" ?>\n<zabbix_export>\n    <version>4.2</version>\n    <groups>\n        <group>\n            <name>Templates</name>\n        </group>\n    </groups>\n    <templates>\n        <template>\n            <template>test</template>\n            <name>Test Template</name>\n            <description/>\n            <groups>\n                <group>\n                    <name>Templates</name>\n                </group>\n            </groups>\n            <applications/>\n            <items/>\n            <discovery_rules/>\n            <httptests/>\n            <macros/>\n            <templates/>\n            <screens/>\n            <tags/>\n        </template>\n    </templates>\n</zabbix_export>"` |

### Authors

- sookido (@sookido)
- Logan Vig (@logan2211)
- Dusan Matejka (@D3DeFi)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
