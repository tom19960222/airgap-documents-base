---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_report_theme module – Report themes configuratio in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_report_theme_module.html
fetched_at: 2026-07-27T17:42:55+00:00
---
# fortinet.fortios.fortios_report_theme module – Report themes configuratio in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_report_theme_module.md#ansible-collections-fortinet-fortios-fortios-report-theme-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_report_theme`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_report_theme_module.md#synopsis)
- [Requirements](fortios_report_theme_module.md#requirements)
- [Parameters](fortios_report_theme_module.md#parameters)
- [Notes](fortios_report_theme_module.md#notes)
- [Examples](fortios_report_theme_module.md#examples)
- [Return Values](fortios_report_theme_module.md#return-values)

## [Synopsis](fortios_report_theme_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify report feature and theme category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_report_theme_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_report_theme_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **report_theme**  dictionary | Report themes configuration |
| **bullet_list_style**  string | Bullet list style. |
| **column_count**  string | Report page column count.  Choices:   - `"1"` - `"2"` - `"3"` |
| **default_html_style**  string | Default HTML report style. |
| **default_pdf_style**  string | Default PDF report style. |
| **graph_chart_style**  string | Graph chart style. |
| **heading1_style**  string | Report heading style. |
| **heading2_style**  string | Report heading style. |
| **heading3_style**  string | Report heading style. |
| **heading4_style**  string | Report heading style. |
| **hline_style**  string | Horizontal line style. |
| **image_style**  string | Image style. |
| **name**  string / required | Report theme name. |
| **normal_text_style**  string | Normal text style. |
| **numbered_list_style**  string | Numbered list style. |
| **page_footer_style**  string | Report page footer style. |
| **page_header_style**  string | Report page header style. |
| **page_orient**  string | Report page orientation.  Choices:   - `"portrait"` - `"landscape"` |
| **page_style**  string | Report page style. |
| **report_subtitle_style**  string | Report subtitle style. |
| **report_title_style**  string | Report title style. |
| **table_chart_caption_style**  string | Table chart caption style. |
| **table_chart_even_row_style**  string | Table chart even row style. |
| **table_chart_head_style**  string | Table chart head row style. |
| **table_chart_odd_row_style**  string | Table chart odd row style. |
| **table_chart_style**  string | Table chart style. |
| **toc_heading1_style**  string | Table of contents heading style. |
| **toc_heading2_style**  string | Table of contents heading style. |
| **toc_heading3_style**  string | Table of contents heading style. |
| **toc_heading4_style**  string | Table of contents heading style. |
| **toc_title_style**  string | Table of contents title style. |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_report_theme_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_report_theme_module.md#id5)

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
  - name: Report themes configuration
    fortios_report_theme:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      report_theme:
        bullet_list_style: "<your_own_value>"
        column_count: "1"
        default_html_style: "<your_own_value>"
        default_pdf_style: "<your_own_value>"
        graph_chart_style: "<your_own_value>"
        heading1_style: "<your_own_value>"
        heading2_style: "<your_own_value>"
        heading3_style: "<your_own_value>"
        heading4_style: "<your_own_value>"
        hline_style: "<your_own_value>"
        image_style: "<your_own_value>"
        name: "default_name_14"
        normal_text_style: "<your_own_value>"
        numbered_list_style: "<your_own_value>"
        page_footer_style: "<your_own_value>"
        page_header_style: "<your_own_value>"
        page_orient: "portrait"
        page_style: "<your_own_value>"
        report_subtitle_style: "<your_own_value>"
        report_title_style: "<your_own_value>"
        table_chart_caption_style: "<your_own_value>"
        table_chart_even_row_style: "<your_own_value>"
        table_chart_head_style: "<your_own_value>"
        table_chart_odd_row_style: "<your_own_value>"
        table_chart_style: "<your_own_value>"
        toc_heading1_style: "<your_own_value>"
        toc_heading2_style: "<your_own_value>"
        toc_heading3_style: "<your_own_value>"
        toc_heading4_style: "<your_own_value>"
        toc_title_style: "<your_own_value>"
```

## [Return Values](fortios_report_theme_module.md#id6)

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
