---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_report_layout module – Report layout configuration in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_report_layout_module.html
fetched_at: 2026-07-28T02:26:36+00:00
---
# fortinet.fortios.fortios_report_layout module – Report layout configuration in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortios/) (version 2.3.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_report_layout_module.md#ansible-collections-fortinet-fortios-fortios-report-layout-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_report_layout`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_report_layout_module.md#synopsis)
- [Requirements](fortios_report_layout_module.md#requirements)
- [Parameters](fortios_report_layout_module.md#parameters)
- [Notes](fortios_report_layout_module.md#notes)
- [Examples](fortios_report_layout_module.md#examples)
- [Return Values](fortios_report_layout_module.md#return-values)

## [Synopsis](fortios_report_layout_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify report feature and layout category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_report_layout_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_report_layout_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **report_layout**  dictionary | Report layout configuration. |
| **body_item**  list / elements=dictionary | Configure report body item. |
| **chart**  string | Report item chart name. |
| **chart_options**  list / elements=string | Report chart options.  **Choices:**   - `"include-no-data"` - `"hide-title"` - `"show-caption"` |
| **column**  integer | Report section column number. |
| **content**  string | Report item text content. |
| **description**  string | Description. |
| **drill_down_items**  string | Control how drill down charts are shown. |
| **drill_down_types**  string | Control whether keys from the parent being combined or not. |
| **hide**  string | Enable/disable hide item in report.  **Choices:**   - `"enable"` - `"disable"` |
| **id**  integer / required | Report item ID. see <a href=’#notes’>Notes</a>. |
| **img_src**  string | Report item image file name. |
| **list**  list / elements=dictionary | Configure report list item. |
| **content**  string | List entry content. |
| **id**  integer / required | List entry ID. see <a href=’#notes’>Notes</a>. |
| **list_component**  string | Report item list component.  **Choices:**   - `"bullet"` - `"numbered"` |
| **misc_component**  string | Report item miscellaneous component.  **Choices:**   - `"hline"` - `"page-break"` - `"column-break"` - `"section-start"` |
| **parameters**  list / elements=dictionary | Parameters. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **name**  string | Field name that match field of parameters defined in dataset. |
| **value**  string | Value to replace corresponding field of parameters defined in dataset. |
| **style**  string | Report item style. |
| **table_caption_style**  string | Table chart caption style. |
| **table_column_widths**  string | Report item table column widths. |
| **table_even_row_style**  string | Table chart even row style. |
| **table_head_style**  string | Table chart head style. |
| **table_odd_row_style**  string | Table chart odd row style. |
| **text_component**  string | Report item text component.  **Choices:**   - `"text"` - `"heading1"` - `"heading2"` - `"heading3"` |
| **title**  string | Report section title. |
| **top_n**  integer | Value of top. |
| **type**  string | Report item type.  **Choices:**   - `"text"` - `"image"` - `"chart"` - `"misc"` |
| **cutoff_option**  string | Cutoff-option is either run-time or custom.  **Choices:**   - `"run-time"` - `"custom"` |
| **cutoff_time**  string | Custom cutoff time to generate report (format = hh:mm). |
| **day**  string | Schedule days of week to generate report.  **Choices:**   - `"sunday"` - `"monday"` - `"tuesday"` - `"wednesday"` - `"thursday"` - `"friday"` - `"saturday"` |
| **description**  string | Description. |
| **email_recipients**  string | Email recipients for generated reports. |
| **email_send**  string | Enable/disable sending emails after reports are generated.  **Choices:**   - `"enable"` - `"disable"` |
| **format**  list / elements=string | Report format.  **Choices:**   - `"pdf"` |
| **max_pdf_report**  integer | Maximum number of PDF reports to keep at one time (oldest report is overwritten). |
| **name**  string / required | Report layout name. |
| **options**  list / elements=string | Report layout options.  **Choices:**   - `"include-table-of-content"` - `"auto-numbering-heading"` - `"view-chart-as-heading"` - `"show-html-navbar-before-heading"` - `"dummy-option"` |
| **page**  dictionary | Configure report page. |
| **column_break_before**  list / elements=string | Report page auto column break before heading.  **Choices:**   - `"heading1"` - `"heading2"` - `"heading3"` |
| **footer**  dictionary | Configure report page footer. |
| **footer_item**  list / elements=dictionary | Configure report footer item. |
| **content**  string | Report item text content. |
| **description**  string | Description. |
| **id**  integer / required | Report item ID. see <a href=’#notes’>Notes</a>. |
| **img_src**  string | Report item image file name. |
| **style**  string | Report item style. |
| **type**  string | Report item type.  **Choices:**   - `"text"` - `"image"` |
| **style**  string | Report footer style. |
| **header**  dictionary | Configure report page header. |
| **header_item**  list / elements=dictionary | Configure report header item. |
| **content**  string | Report item text content. |
| **description**  string | Description. |
| **id**  integer / required | Report item ID. see <a href=’#notes’>Notes</a>. |
| **img_src**  string | Report item image file name. |
| **style**  string | Report item style. |
| **type**  string | Report item type.  **Choices:**   - `"text"` - `"image"` |
| **style**  string | Report header style. |
| **options**  list / elements=string | Report page options.  **Choices:**   - `"header-on-first-page"` - `"footer-on-first-page"` |
| **page_break_before**  list / elements=string | Report page auto page break before heading.  **Choices:**   - `"heading1"` - `"heading2"` - `"heading3"` |
| **paper**  string | Report page paper.  **Choices:**   - `"a4"` - `"letter"` |
| **schedule_type**  string | Report schedule type.  **Choices:**   - `"demand"` - `"daily"` - `"weekly"` |
| **style_theme**  string | Report style theme. |
| **subtitle**  string | Report subtitle. |
| **time**  string | Schedule time to generate report (format = hh:mm). |
| **title**  string | Report title. |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_report_layout_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_report_layout_module.md#id5)

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
  - name: Report layout configuration.
    fortios_report_layout:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      report_layout:
        body_item:
         -
            chart: "<your_own_value>"
            chart_options: "include-no-data"
            column: "2147483647"
            content: "<your_own_value>"
            description: "<your_own_value>"
            drill_down_items: "<your_own_value>"
            drill_down_types: "<your_own_value>"
            hide: "enable"
            id:  "12"
            img_src: "<your_own_value>"
            list:
             -
                content: "<your_own_value>"
                id:  "16"
            list_component: "bullet"
            misc_component: "hline"
            parameters:
             -
                id:  "20"
                name: "default_name_21"
                value: "<your_own_value>"
            style: "<your_own_value>"
            table_caption_style: "<your_own_value>"
            table_column_widths: "<your_own_value>"
            table_even_row_style: "<your_own_value>"
            table_head_style: "<your_own_value>"
            table_odd_row_style: "<your_own_value>"
            text_component: "text"
            title: "<your_own_value>"
            top_n: "0"
            type: "text"
        cutoff_option: "run-time"
        cutoff_time: "<your_own_value>"
        day: "sunday"
        description: "<your_own_value>"
        email_recipients: "<your_own_value>"
        email_send: "enable"
        format: "pdf"
        max_pdf_report: "31"
        name: "default_name_41"
        options: "include-table-of-content"
        page:
            column_break_before: "heading1"
            footer:
                footer_item:
                 -
                    content: "<your_own_value>"
                    description: "<your_own_value>"
                    id:  "49"
                    img_src: "<your_own_value>"
                    style: "<your_own_value>"
                    type: "text"
                style: "<your_own_value>"
            header:
                header_item:
                 -
                    content: "<your_own_value>"
                    description: "<your_own_value>"
                    id:  "58"
                    img_src: "<your_own_value>"
                    style: "<your_own_value>"
                    type: "text"
                style: "<your_own_value>"
            options: "header-on-first-page"
            page_break_before: "heading1"
            paper: "a4"
        schedule_type: "demand"
        style_theme: "<your_own_value>"
        subtitle: "<your_own_value>"
        time: "<your_own_value>"
        title: "<your_own_value>"
```

## [Return Values](fortios_report_layout_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  **Returned:** always  **Sample:** `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  **Returned:** always  **Sample:** `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  **Returned:** always  **Sample:** `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  **Returned:** success  **Sample:** `"id"` |
| **name**  string | Name of the table used to fulfill the request  **Returned:** always  **Sample:** `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  **Returned:** always  **Sample:** `"webfilter"` |
| **revision**  string | Internal revision number  **Returned:** always  **Sample:** `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  **Returned:** always  **Sample:** `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  **Returned:** always  **Sample:** `"success"` |
| **vdom**  string | Virtual domain used  **Returned:** always  **Sample:** `"root"` |
| **version**  string | Version of the FortiGate  **Returned:** always  **Sample:** `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
- [Homepage](https://www.fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
