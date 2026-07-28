---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_map module – Create/update/delete Zabbix maps"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_map_module.html
fetched_at: 2026-07-28T02:02:49+00:00
---
# community.zabbix.zabbix_map module – Create/update/delete Zabbix maps

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
> see [Requirements](zabbix_map_module.md#ansible-collections-community-zabbix-zabbix-map-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_map`.

- [Synopsis](zabbix_map_module.md#synopsis)
- [Requirements](zabbix_map_module.md#requirements)
- [Parameters](zabbix_map_module.md#parameters)
- [Examples](zabbix_map_module.md#examples)

## [Synopsis](zabbix_map_module.md#id1)

- This module allows you to create, modify and delete Zabbix map entries, using Graphviz binaries and text description written in DOT language. Nodes of the graph will become map elements and edges will become links between map elements. See <https://en.wikipedia.org/wiki/DOT_(graph_description_language>) and <https://www.graphviz.org/> for details. Inspired by <http://blog.zabbix.com/maps-for-the-lazy/>.
- The following extra node attributes are supported: `zbx_host` contains name of the host in Zabbix. Use this if desired type of map element is `host`. `zbx_group` contains name of the host group in Zabbix. Use this if desired type of map element is `host group`. `zbx_sysmap` contains name of the map in Zabbix. Use this if desired type of map element is `map`. `zbx_label` contains label of map element. `zbx_image` contains name of the image used to display the element in default state. `zbx_image_disabled` contains name of the image used to display disabled map element. `zbx_image_maintenance` contains name of the image used to display map element in maintenance. `zbx_image_problem` contains name of the image used to display map element with problems. `zbx_url` contains map element URL in `name:url` format. More than one URL could be specified by adding a postfix (e.g., `zbx_url1`, `zbx_url2`).
- The following extra link attributes are supported: `zbx_draw_style` contains link line draw style. Possible values: `line`, `bold`, `dotted`, `dashed`. `zbx_trigger` contains name of the trigger used as a link indicator in `host_name:trigger_name` format. More than one trigger could be specified by adding a postfix (e.g., `zbx_trigger1`, `zbx_trigger2`). `zbx_trigger_color` contains indicator color specified either as CSS3 name or as a hexadecimal code starting with `#`. `zbx_trigger_draw_style` contains indicator draw style. Possible values are the same as for `zbx_draw_style`.

## [Requirements](zabbix_map_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9
- pydotplus
- webcolors
- Pillow
- Graphviz

## [Parameters](zabbix_map_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **data**  aliases: dot_data  string | Graph written in DOT language. |
| **default_image**  aliases: image  string | Name of the Zabbix image used to display the element if this element doesn’t have the `zbx_image` attribute defined. |
| **expand_problem**  boolean | Whether the problem trigger will be displayed for elements with a single problem.  **Choices:**   - `false` - `true` ← (default) |
| **height**  integer | Height of the map.  **Default:** `600` |
| **highlight**  boolean | Whether icon highlighting is enabled.  **Choices:**   - `false` - `true` ← (default) |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **label_type**  string | Map element label type.  **Choices:**   - `"label"` - `"ip"` - `"name"` ← (default) - `"status"` - `"nothing"` - `"custom"` |
| **margin**  integer | Size of white space between map’s borders and its elements.  **Default:** `40` |
| **name**  aliases: map_name  string / required | Name of the map. |
| **state**  string | State of the map.  On `present`, it will create if map does not exist or update the map if the associated data is different.  On `absent` will remove the map if it exists.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **width**  integer | Width of the map.  **Default:** `800` |

## [Examples](zabbix_map_module.md#id4)

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

###
### Example inventory:
# [web]
# web[01:03].example.com ansible_host=127.0.0.1
# [db]
# db.example.com ansible_host=127.0.0.1
# [backup]
# backup.example.com ansible_host=127.0.0.1
###
### Each inventory host is present in Zabbix with a matching name.
###
### Contents of "map.j2":
# digraph G {
#     graph [layout=dot splines=false overlap=scale]
#     INTERNET [zbx_url="Google:https://google.com" zbx_image="Cloud_(96)"]
# {% for web_host in groups.web %}
#     {% set web_loop = loop %}
#     web{{ '%03d' % web_loop.index }} [zbx_host="{{ web_host }}"]
#     INTERNET -> web{{ '%03d' % web_loop.index }} [zbx_trigger="{{ web_host }}:Zabbix agent on {HOST.NAME} is unreachable for 5 minutes"]
#     {% for db_host in groups.db %}
#       {% set db_loop = loop %}
#     web{{ '%03d' % web_loop.index }} -> db{{ '%03d' % db_loop.index }}
#     {% endfor %}
# {% endfor %}
#     { rank=same
# {% for db_host in groups.db %}
#     {% set db_loop = loop %}
#     db{{ '%03d' % db_loop.index }} [zbx_host="{{ db_host }}"]
#     {% for backup_host in groups.backup %}
#         {% set backup_loop = loop %}
#         db{{ '%03d' % db_loop.index }} -> backup{{ '%03d' % backup_loop.index }} [color="blue"]
#     {% endfor %}
# {% endfor %}
# {% for backup_host in groups.backup %}
#     {% set backup_loop = loop %}
#         backup{{ '%03d' % backup_loop.index }} [zbx_host="{{ backup_host }}"]
# {% endfor %}
#     }
# }
###
### Create Zabbix map "Demo Map" made of template "map.j2"
- name: Create Zabbix map
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_map:
    name: Demo map
    state: present
    data: "{{ lookup('template', 'map.j2') }}"
    default_image: Server_(64)
    expand_problem: no
    highlight: no
    label_type: label
  delegate_to: localhost
  run_once: yes
```

### Authors

- Antony Alekseyev (@Akint)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
