---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_report_chart module – Report chart widget configuration in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_report_chart_module.html
fetched_at: 2026-07-28T02:26:34+00:00
---
# fortinet.fortios.fortios_report_chart module – Report chart widget configuration in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_report_chart_module.md#ansible-collections-fortinet-fortios-fortios-report-chart-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_report_chart`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_report_chart_module.md#synopsis)
- [Requirements](fortios_report_chart_module.md#requirements)
- [Parameters](fortios_report_chart_module.md#parameters)
- [Notes](fortios_report_chart_module.md#notes)
- [Examples](fortios_report_chart_module.md#examples)
- [Return Values](fortios_report_chart_module.md#return-values)

## [Synopsis](fortios_report_chart_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify report feature and chart category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_report_chart_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_report_chart_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **report_chart**  dictionary | Report chart widget configuration. |
| **background**  string | Chart background. |
| **category**  string | Category.  **Choices:**   - `"misc"` - `"traffic"` - `"event"` - `"virus"` - `"webfilter"` - `"attack"` - `"spam"` - `"dlp"` - `"app-ctrl"` - `"vulnerability"` |
| **category_series**  dictionary | Category series of pie chart. |
| **databind**  string | Category series value expression. |
| **font_size**  integer | Font size of category-series title. |
| **color_palette**  string | Color palette (system will pick color automatically by default). |
| **column**  list / elements=dictionary | Table column definition. |
| **detail_unit**  string | Detail unit of column. |
| **detail_value**  string | Detail value of column. |
| **footer_unit**  string | Footer unit of column. |
| **footer_value**  string | Footer value of column. |
| **header_value**  string | Display name of table header. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **mapping**  list / elements=dictionary | Show detail in certain display value for certain condition. |
| **displayname**  string | Display name. |
| **id**  integer / required | id see <a href=’#notes’>Notes</a>. |
| **op**  string | Comparision operater.  **Choices:**   - `"none"` - `"greater"` - `"greater-equal"` - `"less"` - `"less-equal"` - `"equal"` - `"between"` |
| **value1**  string | Value 1. |
| **value2**  string | Value 2. |
| **value_type**  string | Value type.  **Choices:**   - `"integer"` - `"string"` |
| **comments**  string | Comment. |
| **dataset**  string | Bind dataset to chart. |
| **dimension**  string | Dimension.  **Choices:**   - `"2D"` - `"3D"` |
| **drill_down_charts**  list / elements=dictionary | Drill down charts. |
| **chart_name**  string | Drill down chart name. |
| **id**  integer / required | Drill down chart ID. see <a href=’#notes’>Notes</a>. |
| **status**  string | Enable/disable this drill down chart.  **Choices:**   - `"enable"` - `"disable"` |
| **favorite**  string | Favorite.  **Choices:**   - `"no"` - `"yes"` |
| **graph_type**  string | Graph type.  **Choices:**   - `"none"` - `"bar"` - `"pie"` - `"line"` - `"flow"` |
| **legend**  string | Enable/Disable Legend area.  **Choices:**   - `"enable"` - `"disable"` |
| **legend_font_size**  integer | Font size of legend area. |
| **name**  string / required | Chart Widget Name |
| **period**  string | Time period.  **Choices:**   - `"last24h"` - `"last7d"` |
| **policy**  integer | Used by monitor policy. |
| **style**  string | Style.  **Choices:**   - `"auto"` - `"manual"` |
| **title**  string | Chart title. |
| **title_font_size**  integer | Font size of chart title. |
| **type**  string | Chart type.  **Choices:**   - `"graph"` - `"table"` |
| **value_series**  dictionary | Value series of pie chart. |
| **databind**  string | Value series value expression. |
| **x_series**  dictionary | X-series of chart. |
| **caption**  string | X-series caption. |
| **caption_font_size**  integer | X-series caption font size. |
| **databind**  string | X-series value expression. |
| **font_size**  integer | X-series label font size. |
| **is_category**  string | X-series represent category or not.  **Choices:**   - `"yes"` - `"no"` |
| **label_angle**  string | X-series label angle.  **Choices:**   - `"45-degree"` - `"vertical"` - `"horizontal"` |
| **scale_direction**  string | Scale increase or decrease.  **Choices:**   - `"decrease"` - `"increase"` |
| **scale_format**  string | Date/time format.  **Choices:**   - `"YYYY-MM-DD-HH-MM"` - `"YYYY-MM-DD HH"` - `"YYYY-MM-DD"` - `"YYYY-MM"` - `"YYYY"` - `"HH-MM"` - `"MM-DD"` |
| **scale_step**  integer | Scale step. |
| **scale_unit**  string | Scale unit.  **Choices:**   - `"minute"` - `"hour"` - `"day"` - `"month"` - `"year"` |
| **unit**  string | X-series unit. |
| **y_series**  dictionary | Y-series of chart. |
| **caption**  string | Y-series caption. |
| **caption_font_size**  integer | Y-series caption font size. |
| **databind**  string | Y-series value expression. |
| **extra_databind**  string | Extra Y-series value. |
| **extra_y**  string | Allow another Y-series value  **Choices:**   - `"enable"` - `"disable"` |
| **extra_y_legend**  string | Extra Y-series legend type/name. |
| **font_size**  integer | Y-series label font size. |
| **group**  string | Y-series group option. |
| **label_angle**  string | Y-series label angle.  **Choices:**   - `"45-degree"` - `"vertical"` - `"horizontal"` |
| **unit**  string | Y-series unit. |
| **y_legend**  string | First Y-series legend type/name. |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_report_chart_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_report_chart_module.md#id5)

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
  - name: Report chart widget configuration.
    fortios_report_chart:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      report_chart:
        background: "<your_own_value>"
        category: "misc"
        category_series:
            databind: "<your_own_value>"
            font_size: "10"
        color_palette: "<your_own_value>"
        column:
         -
            detail_unit: "<your_own_value>"
            detail_value: "<your_own_value>"
            footer_unit: "<your_own_value>"
            footer_value: "<your_own_value>"
            header_value: "<your_own_value>"
            id:  "15"
            mapping:
             -
                displayname: "<your_own_value>"
                id:  "18"
                op: "none"
                value_type: "integer"
                value1: "<your_own_value>"
                value2: "<your_own_value>"
        comments: "<your_own_value>"
        dataset: "<your_own_value>"
        dimension: "2D"
        drill_down_charts:
         -
            chart_name: "<your_own_value>"
            id:  "28"
            status: "enable"
        favorite: "no"
        graph_type: "none"
        legend: "enable"
        legend_font_size: "2147483647"
        name: "default_name_34"
        period: "last24h"
        policy: "2147483647"
        style: "auto"
        title: "<your_own_value>"
        title_font_size: "2147483647"
        type: "graph"
        value_series:
            databind: "<your_own_value>"
        x_series:
            caption: "<your_own_value>"
            caption_font_size: "10"
            databind: "<your_own_value>"
            font_size: "10"
            is_category: "yes"
            label_angle: "45-degree"
            scale_direction: "decrease"
            scale_format: "YYYY-MM-DD-HH-MM"
            scale_step: "32767"
            scale_unit: "minute"
            unit: "<your_own_value>"
        y_series:
            caption: "<your_own_value>"
            caption_font_size: "10"
            databind: "<your_own_value>"
            extra_databind: "<your_own_value>"
            extra_y: "enable"
            extra_y_legend: "<your_own_value>"
            font_size: "10"
            group: "<your_own_value>"
            label_angle: "45-degree"
            unit: "<your_own_value>"
            y_legend: "<your_own_value>"
```

## [Return Values](fortios_report_chart_module.md#id6)

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
