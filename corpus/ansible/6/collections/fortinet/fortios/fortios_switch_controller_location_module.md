---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_switch_controller_location module – Configure FortiSwitch location services in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_switch_controller_location_module.html
fetched_at: 2026-07-27T17:43:31+00:00
---
# fortinet.fortios.fortios_switch_controller_location module – Configure FortiSwitch location services in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_switch_controller_location_module.md#ansible-collections-fortinet-fortios-fortios-switch-controller-location-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_switch_controller_location`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_switch_controller_location_module.md#synopsis)
- [Requirements](fortios_switch_controller_location_module.md#requirements)
- [Parameters](fortios_switch_controller_location_module.md#parameters)
- [Notes](fortios_switch_controller_location_module.md#notes)
- [Examples](fortios_switch_controller_location_module.md#examples)
- [Return Values](fortios_switch_controller_location_module.md#return-values)

## [Synopsis](fortios_switch_controller_location_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify switch_controller feature and location category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_switch_controller_location_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_switch_controller_location_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **switch_controller_location**  dictionary | Configure FortiSwitch location services. |
| **address_civic**  dictionary | Configure location civic address. |
| **additional**  string | Location additional details. |
| **additional_code**  string | Location additional code details. |
| **block**  string | Location block details. |
| **branch_road**  string | Location branch road details. |
| **building**  string | Location building details. |
| **city**  string | Location city details. |
| **city_division**  string | Location city division details. |
| **country**  string | The two-letter ISO 3166 country code in capital ASCII letters eg. US, CA, DK, DE. |
| **country_subdivision**  string | National subdivisions (state, canton, region, province, or prefecture). |
| **county**  string | County, parish, gun (JP), or district (IN). |
| **direction**  string | Leading street direction. |
| **floor**  string | Floor. |
| **landmark**  string | Landmark or vanity address. |
| **language**  string | Language. |
| **name**  string | Name (residence and office occupant). |
| **number**  string | House number. |
| **number_suffix**  string | House number suffix. |
| **parent_key**  string | Parent key name. |
| **place_type**  string | Place type. |
| **post_office_box**  string | Post office box. |
| **postal_community**  string | Postal community name. |
| **primary_road**  string | Primary road name. |
| **road_section**  string | Road section. |
| **room**  string | Room number. |
| **script**  string | Script used to present the address information. |
| **seat**  string | Seat number. |
| **street**  string | Street. |
| **street_name_post_mod**  string | Street name post modifier. |
| **street_name_pre_mod**  string | Street name pre modifier. |
| **street_suffix**  string | Street suffix. |
| **sub_branch_road**  string | Sub branch road name. |
| **trailing_str_suffix**  string | Trailing street suffix. |
| **unit**  string | Unit (apartment, suite). |
| **zip**  string | Postal/zip code. |
| **coordinates**  dictionary | Configure location GPS coordinates. |
| **altitude**  string | Plus or minus floating point number. For example, 117.47. |
| **altitude_unit**  string | Configure the unit for which the altitude is to (m = meters, f = floors of a building).  Choices:   - `"m"` - `"f"` |
| **datum**  string | WGS84, NAD83, NAD83/MLLW.  Choices:   - `"WGS84"` - `"NAD83"` - `"NAD83/MLLW"` |
| **latitude**  string | Floating point starting with +/- or ending with (N or S). For example, +/-16.67 or 16.67N. |
| **longitude**  string | Floating point starting with +/- or ending with (N or S). For example, +/-26.789 or 26.789E. |
| **parent_key**  string | Parent key name. |
| **elin_number**  dictionary | Configure location ELIN number. |
| **elin_num**  string | Configure ELIN callback number. |
| **parent_key**  string | Parent key name. |
| **name**  string / required | Unique location item name. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_switch_controller_location_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_switch_controller_location_module.md#id5)

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
  - name: Configure FortiSwitch location services.
    fortios_switch_controller_location:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      switch_controller_location:
        address_civic:
            additional: "<your_own_value>"
            additional_code: "<your_own_value>"
            block: "<your_own_value>"
            branch_road: "<your_own_value>"
            building: "<your_own_value>"
            city: "<your_own_value>"
            city_division: "<your_own_value>"
            country: "<your_own_value>"
            country_subdivision: "<your_own_value>"
            county: "<your_own_value>"
            direction: "<your_own_value>"
            floor: "<your_own_value>"
            landmark: "<your_own_value>"
            language: "<your_own_value>"
            name: "default_name_18"
            number: "<your_own_value>"
            number_suffix: "<your_own_value>"
            parent_key: "<your_own_value>"
            place_type: "<your_own_value>"
            post_office_box: "<your_own_value>"
            postal_community: "<your_own_value>"
            primary_road: "<your_own_value>"
            road_section: "<your_own_value>"
            room: "<your_own_value>"
            script: "<your_own_value>"
            seat: "<your_own_value>"
            street: "<your_own_value>"
            street_name_post_mod: "<your_own_value>"
            street_name_pre_mod: "<your_own_value>"
            street_suffix: "<your_own_value>"
            sub_branch_road: "<your_own_value>"
            trailing_str_suffix: "<your_own_value>"
            unit: "<your_own_value>"
            zip: "<your_own_value>"
        coordinates:
            altitude: "<your_own_value>"
            altitude_unit: "m"
            datum: "WGS84"
            latitude: "<your_own_value>"
            longitude: "<your_own_value>"
            parent_key: "<your_own_value>"
        elin_number:
            elin_num: "<your_own_value>"
            parent_key: "<your_own_value>"
        name: "default_name_48"
```

## [Return Values](fortios_switch_controller_location_module.md#id6)

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
