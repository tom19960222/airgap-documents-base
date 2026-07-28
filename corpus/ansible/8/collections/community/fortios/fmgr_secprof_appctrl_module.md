---
collection: ansible
version: "8"
title: "community.fortios.fmgr_secprof_appctrl module – Manage application control security profiles"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/fortios/fmgr_secprof_appctrl_module.html
fetched_at: 2026-07-28T01:44:18+00:00
---
# community.fortios.fmgr_secprof_appctrl module – Manage application control security profiles

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/ui/repo/published/community/fortios/) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_secprof_appctrl`.

- [Synopsis](fmgr_secprof_appctrl_module.md#synopsis)
- [Parameters](fmgr_secprof_appctrl_module.md#parameters)
- [Notes](fmgr_secprof_appctrl_module.md#notes)
- [Examples](fmgr_secprof_appctrl_module.md#examples)
- [Return Values](fmgr_secprof_appctrl_module.md#return-values)

## [Synopsis](fmgr_secprof_appctrl_module.md#id1)

- Manage application control security profiles within FortiManager

## [Parameters](fmgr_secprof_appctrl_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string | The ADOM the configuration should belong to.  **Default:** `"root"` |
| **app_replacemsg**  string | Enable/disable replacement messages for blocked applications.  choice | disable | Disable replacement messages for blocked applications.  choice | enable | Enable replacement messages for blocked applications.  **Choices:**   - `"disable"` - `"enable"` |
| **comment**  string | comments |
| **deep_app_inspection**  string | Enable/disable deep application inspection.  choice | disable | Disable deep application inspection.  choice | enable | Enable deep application inspection.  **Choices:**   - `"disable"` - `"enable"` |
| **entries**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED. This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, OMIT THE USE OF THIS PARAMETER  AND USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **entries_action**  string | Pass or block traffic, or reset connection for traffic from this application.  choice | pass | Pass or allow matching traffic.  choice | block | Block or drop matching traffic.  choice | reset | Reset sessions for matching traffic.  **Choices:**   - `"pass"` - `"block"` - `"reset"` |
| **entries_application**  string | ID of allowed applications. |
| **entries_behavior**  string | Application behavior filter. |
| **entries_category**  string | Category ID list. |
| **entries_log**  string | Enable/disable logging for this application list.  choice | disable | Disable logging.  choice | enable | Enable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **entries_log_packet**  string | Enable/disable packet logging.  choice | disable | Disable packet logging.  choice | enable | Enable packet logging.  **Choices:**   - `"disable"` - `"enable"` |
| **entries_parameters_value**  string | Parameter value. |
| **entries_per_ip_shaper**  string | Per-IP traffic shaper. |
| **entries_popularity**  string | Application popularity filter (1 - 5, from least to most popular).  FLAG Based Options. Specify multiple in list form.  flag | 1 | Popularity level 1.  flag | 2 | Popularity level 2.  flag | 3 | Popularity level 3.  flag | 4 | Popularity level 4.  flag | 5 | Popularity level 5.  **Choices:**   - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` |
| **entries_protocols**  string | Application protocol filter. |
| **entries_quarantine**  string | Quarantine method.  choice | none | Quarantine is disabled.  choice | attacker | Block all traffic sent from attacker’s IP address.  The attacker’s IP address is also added to the banned user list. The target’s address is not affected.  **Choices:**   - `"none"` - `"attacker"` |
| **entries_quarantine_expiry**  string | Duration of quarantine. (Format  Requires quarantine set to attacker. |
| **entries_quarantine_log**  string | Enable/disable quarantine logging.  choice | disable | Disable quarantine logging.  choice | enable | Enable quarantine logging.  **Choices:**   - `"disable"` - `"enable"` |
| **entries_rate_count**  string | Count of the rate. |
| **entries_rate_duration**  string | Duration (sec) of the rate. |
| **entries_rate_mode**  string | Rate limit mode.  choice | periodical | Allow configured number of packets every rate-duration.  choice | continuous | Block packets once the rate is reached.  **Choices:**   - `"periodical"` - `"continuous"` |
| **entries_rate_track**  string | Track the packet protocol field.  choice | none |  choice | src-ip | Source IP.  choice | dest-ip | Destination IP.  choice | dhcp-client-mac | DHCP client.  choice | dns-domain | DNS domain.  **Choices:**   - `"none"` - `"src-ip"` - `"dest-ip"` - `"dhcp-client-mac"` - `"dns-domain"` |
| **entries_risk**  string | Risk, or impact, of allowing traffic from this application to occur 1 - 5;  (Low, Elevated, Medium, High, and Critical). |
| **entries_session_ttl**  string | Session TTL (0 = default). |
| **entries_shaper**  string | Traffic shaper. |
| **entries_shaper_reverse**  string | Reverse traffic shaper. |
| **entries_sub_category**  string | Application Sub-category ID list. |
| **entries_technology**  string | Application technology filter. |
| **entries_vendor**  string | Application vendor filter. |
| **extended_log**  string | Enable/disable extended logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **mode**  string | Sets one of three modes for managing the object.  Allows use of soft-adds instead of overwriting existing values  **Choices:**   - `"add"` ← (default) - `"set"` - `"delete"` - `"update"` |
| **name**  string | List name. |
| **options**  string | NO DESCRIPTION PARSED ENTER MANUALLY  FLAG Based Options. Specify multiple in list form.  flag | allow-dns | Allow DNS.  flag | allow-icmp | Allow ICMP.  flag | allow-http | Allow generic HTTP web browsing.  flag | allow-ssl | Allow generic SSL communication.  flag | allow-quic | Allow QUIC.  **Choices:**   - `"allow-dns"` - `"allow-icmp"` - `"allow-http"` - `"allow-ssl"` - `"allow-quic"` |
| **other_application_action**  string | Action for other applications.  choice | pass | Allow sessions matching an application in this application list.  choice | block | Block sessions matching an application in this application list.  **Choices:**   - `"pass"` - `"block"` |
| **other_application_log**  string | Enable/disable logging for other applications.  choice | disable | Disable logging for other applications.  choice | enable | Enable logging for other applications.  **Choices:**   - `"disable"` - `"enable"` |
| **p2p_black_list**  string | NO DESCRIPTION PARSED ENTER MANUALLY  FLAG Based Options. Specify multiple in list form.  flag | skype | Skype.  flag | edonkey | Edonkey.  flag | bittorrent | Bit torrent.  **Choices:**   - `"skype"` - `"edonkey"` - `"bittorrent"` |
| **replacemsg_group**  string | Replacement message group. |
| **unknown_application_action**  string | Pass or block traffic from unknown applications.  choice | pass | Pass or allow unknown applications.  choice | block | Drop or block unknown applications.  **Choices:**   - `"pass"` - `"block"` |
| **unknown_application_log**  string | Enable/disable logging for unknown applications.  choice | disable | Disable logging for unknown applications.  choice | enable | Enable logging for unknown applications.  **Choices:**   - `"disable"` - `"enable"` |

## [Notes](fmgr_secprof_appctrl_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_secprof_appctrl_module.md#id4)

```yaml+jinja
- name: DELETE Profile
  community.fortios.fmgr_secprof_appctrl:
    name: "Ansible_Application_Control_Profile"
    comment: "Created by Ansible Module TEST"
    mode: "delete"

- name: CREATE Profile
  community.fortios.fmgr_secprof_appctrl:
    name: "Ansible_Application_Control_Profile"
    comment: "Created by Ansible Module TEST"
    mode: "set"
    entries: [{
              action: "block",
              log: "enable",
              log-packet: "enable",
              protocols: ["1"],
              quarantine: "attacker",
              quarantine-log: "enable",
              },
              {action: "pass",
              category: ["2","3","4"]},
            ]
```

## [Return Values](fmgr_secprof_appctrl_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  **Returned:** always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.fortios)
