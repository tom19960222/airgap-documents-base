---
collection: ansible
version: "8"
title: "community.general.ipbase_info module – Retrieve IP geolocation and other facts of a host’s IP address using the ipbase.com API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ipbase_info_module.html
fetched_at: 2026-07-28T01:46:48+00:00
---
# community.general.ipbase_info module – Retrieve IP geolocation and other facts of a host’s IP address using the ipbase.com API

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.ipbase_info`.

New in community.general 7.0.0

- [Synopsis](ipbase_info_module.md#synopsis)
- [Parameters](ipbase_info_module.md#parameters)
- [Attributes](ipbase_info_module.md#attributes)
- [Notes](ipbase_info_module.md#notes)
- [Examples](ipbase_info_module.md#examples)
- [Return Values](ipbase_info_module.md#return-values)

## [Synopsis](ipbase_info_module.md#id1)

- Retrieve IP geolocation and other facts of a host’s IP address using the ipbase.com API

## [Parameters](ipbase_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **apikey**  string | The API key for the request if you need more requests. |
| **hostname**  boolean | If the `hostname` parameter is set to `true`, the API response will contain the hostname of the IP.  **Choices:**   - `false` ← (default) - `true` |
| **ip**  string | The IP you want to get the info for. If not specified the API will detect the IP automatically. |
| **language**  string | An ISO Alpha 2 Language Code for localizing the IP data  **Default:** `"en"` |

## [Attributes](ipbase_info_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](ipbase_info_module.md#id4)

> **Note:**
>
> - Check <https://ipbase.com/> for more information.

## [Examples](ipbase_info_module.md#id5)

```yaml+jinja
- name: "Get IP geolocation information of the primary outgoing IP"
  community.general.ipbase_info:
  register: my_ip_info

- name: "Get IP geolocation information of a specific IP"
  community.general.ipbase_info:
    ip: "8.8.8.8"
  register: my_ip_info

- name: "Get IP geolocation information of a specific IP with all other possible parameters"
  community.general.ipbase_info:
    ip: "8.8.8.8"
    apikey: "xxxxxxxxxxxxxxxxxxxxxx"
    hostname: true
    language: "de"
  register: my_ip_info
```

## [Return Values](ipbase_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | JSON parsed response from ipbase.com. Please refer to <https://ipbase.com/docs/info> for the detailed structure of the response.  **Returned:** success  **Sample:** `{"connection": {"asn": 13335, "isp": "APNIC Research and Development", "organization": "Cloudflare, Inc.", "range": "1.1.1.1/32"}, "domains": {"count": 10943, "domains": ["eliwise.academy", "accountingprose.academy", "pistola.academy", "1and1-test-ntlds-fr.accountant", "omnergy.africa"]}, "hostname": "one.one.one.one", "ip": "1.1.1.1", "location": {"city": {"alpha2": null, "fips": "644000", "geonames_id": 5368753, "hasc_id": null, "name": "Los Angeles", "name_translated": "Los Angeles", "wikidata_id": "Q65"}, "continent": {"code": "NA", "name": "North America", "name_translated": "North America"}, "country": {"alpha2": "US", "alpha3": "USA", "calling_codes": ["+1"], "currencies": [{"code": "USD", "decimal_digits": 2, "name": "US Dollar", "name_plural": "US dollars", "rounding": 0, "symbol": "$", "symbol_native": "$"}], "emoji": "...", "fips": "US", "geonames_id": 6252001, "hasc_id": "US", "ioc": "USA", "is_in_european_union": false, "languages": [{"name": "English", "name_native": "English"}], "name": "United States", "name_translated": "United States", "timezones": ["America/New_York", "America/Detroit", "America/Kentucky/Louisville", "America/Kentucky/Monticello", "America/Indiana/Indianapolis", "America/Indiana/Vincennes", "America/Indiana/Winamac", "America/Indiana/Marengo", "America/Indiana/Petersburg", "America/Indiana/Vevay", "America/Chicago", "America/Indiana/Tell_City", "America/Indiana/Knox", "America/Menominee", "America/North_Dakota/Center", "America/North_Dakota/New_Salem", "America/North_Dakota/Beulah", "America/Denver", "America/Boise", "America/Phoenix", "America/Los_Angeles", "America/Anchorage", "America/Juneau", "America/Sitka", "America/Metlakatla", "America/Yakutat", "America/Nome", "America/Adak", "Pacific/Honolulu"], "wikidata_id": "Q30"}, "geonames_id": 5332870, "latitude": 34.053611755371094, "longitude": -118.24549865722656, "region": {"alpha2": "US-CA", "fips": "US06", "geonames_id": 5332921, "hasc_id": "US.CA", "name": "California", "name_translated": "California", "wikidata_id": "Q99"}, "zip": "90012"}, "range_type": {"description": "Public address", "type": "PUBLIC"}, "security": {"is_abuser": true, "is_anonymous": false, "is_bot": false, "is_datacenter": false, "is_icloud_relay": false, "is_known_attacker": true, "is_proxy": false, "is_spam": false, "is_tor": false, "is_vpn": false, "threat_score": 100}, "timezone": {"code": "PDT", "current_time": "2023-05-04T04:30:28-07:00", "gmt_offset": -25200, "id": "America/Los_Angeles", "is_daylight_saving": true}, "tlds": [".us"], "type": "v4"}` |

### Authors

- Dominik Kukacka (@dominikkukacka)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
