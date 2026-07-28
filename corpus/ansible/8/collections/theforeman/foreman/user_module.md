---
collection: ansible
version: "8"
title: "theforeman.foreman.user module – Manage Users"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/user_module.html
fetched_at: 2026-07-28T02:56:47+00:00
---
# theforeman.foreman.user module – Manage Users

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/ui/repo/published/theforeman/foreman/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](user_module.md#ansible-collections-theforeman-foreman-user-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.user`.

New in theforeman.foreman 1.0.0

- [Synopsis](user_module.md#synopsis)
- [Requirements](user_module.md#requirements)
- [Parameters](user_module.md#parameters)
- [Attributes](user_module.md#attributes)
- [Examples](user_module.md#examples)
- [Return Values](user_module.md#return-values)

## [Synopsis](user_module.md#id1)

- Create, update, and delete users

Aliases: foreman_user

## [Requirements](user_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin**  boolean | Whether or not the user is an administrator  **Choices:**   - `false` ← (default) - `true` |
| **auth_source**  string | Authentication source where the user exists |
| **default_location**  string | The location that the user uses by default |
| **default_organization**  string | The organizxation that the user uses by default |
| **description**  string | Description of the user |
| **firstname**  string | First name of the user |
| **lastname**  string | Last name of the user |
| **locale**  string | The language locale for the user  **Choices:**   - `"ca"` - `"de"` - `"en"` - `"en_GB"` - `"es"` - `"fr"` - `"gl"` - `"it"` - `"ja"` - `"ko"` - `"nl_NL"` - `"pl"` - `"pt_BR"` - `"ru"` - `"sv_SE"` - `"zh_CN"` - `"zh_TW"` |
| **locations**  list / elements=string | List of locations the entity should be assigned to |
| **login**  aliases: name  string / required | Name of the user |
| **mail**  string | Email address of the user  Required when creating a new user |
| **organizations**  list / elements=string | List of organizations the entity should be assigned to |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **roles**  list / elements=string | List of roles assigned to the user |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timezone**  string | Timezone for the user  If blank it will use the browser timezone.  **Choices:**   - `"International Date Line West"` - `"American Samoa"` - `"Midway Island"` - `"Hawaii"` - `"Alaska"` - `"Pacific Time (US & Canada)"` - `"Tijuana"` - `"Arizona"` - `"Chihuahua"` - `"Mazatlan"` - `"Mountain Time (US & Canada)"` - `"Central America"` - `"Central Time (US & Canada)"` - `"Guadalajara"` - `"Mexico City"` - `"Monterrey"` - `"Saskatchewan"` - `"Bogota"` - `"Eastern Time (US & Canada)"` - `"Indiana (East)"` - `"Lima"` - `"Quito"` - `"Atlantic Time (Canada)"` - `"Caracas"` - `"Georgetown"` - `"La Paz"` - `"Puerto Rico"` - `"Santiago"` - `"Newfoundland"` - `"Brasilia"` - `"Buenos Aires"` - `"Greenland"` - `"Montevideo"` - `"Mid-Atlantic"` - `"Azores"` - `"Cape Verde Is."` - `"Dublin"` - `"Edinburgh"` - `"Lisbon"` - `"London"` - `"Monrovia"` - `"UTC"` - `"Amsterdam"` - `"Belgrade"` - `"Berlin"` - `"Bern"` - `"Bratislava"` - `"Brussels"` - `"Budapest"` - `"Casablanca"` - `"Copenhagen"` - `"Ljubljana"` - `"Madrid"` - `"Paris"` - `"Prague"` - `"Rome"` - `"Sarajevo"` - `"Skopje"` - `"Stockholm"` - `"Vienna"` - `"Warsaw"` - `"West Central Africa"` - `"Zagreb"` - `"Zurich"` - `"Athens"` - `"Bucharest"` - `"Cairo"` - `"Harare"` - `"Helsinki"` - `"Jerusalem"` - `"Kaliningrad"` - `"Kyiv"` - `"Pretoria"` - `"Riga"` - `"Sofia"` - `"Tallinn"` - `"Vilnius"` - `"Baghdad"` - `"Istanbul"` - `"Kuwait"` - `"Minsk"` - `"Moscow"` - `"Nairobi"` - `"Riyadh"` - `"St. Petersburg"` - `"Tehran"` - `"Abu Dhabi"` - `"Baku"` - `"Muscat"` - `"Samara"` - `"Tbilisi"` - `"Volgograd"` - `"Yerevan"` - `"Kabul"` - `"Ekaterinburg"` - `"Islamabad"` - `"Karachi"` - `"Tashkent"` - `"Chennai"` - `"Kolkata"` - `"Mumbai"` - `"New Delhi"` - `"Sri Jayawardenepura"` - `"Kathmandu"` - `"Almaty"` - `"Astana"` - `"Dhaka"` - `"Urumqi"` - `"Rangoon"` - `"Bangkok"` - `"Hanoi"` - `"Jakarta"` - `"Krasnoyarsk"` - `"Novosibirsk"` - `"Beijing"` - `"Chongqing"` - `"Hong Kong"` - `"Irkutsk"` - `"Kuala Lumpur"` - `"Perth"` - `"Singapore"` - `"Taipei"` - `"Ulaanbaatar"` - `"Osaka"` - `"Sapporo"` - `"Seoul"` - `"Tokyo"` - `"Yakutsk"` - `"Adelaide"` - `"Darwin"` - `"Brisbane"` - `"Canberra"` - `"Guam"` - `"Hobart"` - `"Melbourne"` - `"Port Moresby"` - `"Sydney"` - `"Vladivostok"` - `"Magadan"` - `"New Caledonia"` - `"Solomon Is."` - `"Srednekolymsk"` - `"Auckland"` - `"Fiji"` - `"Kamchatka"` - `"Marshall Is."` - `"Wellington"` - `"Chatham Is."` - `"Nuku'alofa"` - `"Samoa"` - `"Tokelau Is."` |
| **user_password**  string | Password for the user.  When this parameter is set, the module will not be idempotent. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](user_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](user_module.md#id5)

```yaml+jinja
- name: Create a user
  theforeman.foreman.user:
    name: test
    firstname: Test
    lastname: Userson
    mail: test.userson@example.com
    description: Dr. Test Userson
    admin: false
    user_password: s3cret
    default_location: Test Location
    default_organization: Test Organization
    auth_source: Internal
    timezone: Stockholm
    locale: sv_SE
    roles:
      - Manager
    locations:
      - Test Location
    organizations:
      - Test Organization
    state: present

- name: Update a user
  theforeman.foreman.user:
    name: test
    firstname: Tester
    state: present

- name: Change password
  theforeman.foreman.user:
    name: test
    user_password: newp@ss
```

## [Return Values](user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **users**  list / elements=dictionary | List of users.  **Returned:** success |

### Authors

- Christoffer Reijer (@ephracis) Basalt AB

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
