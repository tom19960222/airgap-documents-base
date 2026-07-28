---
collection: ansible
version: "8"
title: "cisco.nxos.storage.nxos_zone_zoneset module – Configuration of zone/zoneset for Cisco NXOS MDS Switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/storage.nxos_zone_zoneset_module.html
fetched_at: 2026-07-28T01:39:28+00:00
---
# cisco.nxos.storage.nxos_zone_zoneset module – Configuration of zone/zoneset for Cisco NXOS MDS Switches.

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.storage.nxos_zone_zoneset`.

New in cisco.nxos 1.0.0

- [Synopsis](storage.nxos_zone_zoneset_module.md#synopsis)
- [Parameters](storage.nxos_zone_zoneset_module.md#parameters)
- [Notes](storage.nxos_zone_zoneset_module.md#notes)
- [Examples](storage.nxos_zone_zoneset_module.md#examples)
- [Return Values](storage.nxos_zone_zoneset_module.md#return-values)

## [Synopsis](storage.nxos_zone_zoneset_module.md#id1)

- Configuration of zone/zoneset for Cisco MDS NXOS.

Aliases: nxos_zone_zoneset

## [Parameters](storage.nxos_zone_zoneset_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **zone_zoneset_details**  list / elements=dictionary | List of zone/zoneset details to be added or removed |
| **default_zone**  string | default zone behaviour for the vsan  **Choices:**   - `"permit"` - `"deny"` |
| **mode**  string | mode of the zone for the vsan  **Choices:**   - `"enhanced"` - `"basic"` |
| **smart_zoning**  boolean | Removes the vsan if True  **Choices:**   - `false` - `true` |
| **vsan**  integer / required | vsan id |
| **zone**  list / elements=dictionary | List of zone options for that vsan |
| **members**  list / elements=dictionary | Members of the zone that needs to be removed or added |
| **devtype**  string | devtype of the zone member used along with Smart zoning config  **Choices:**   - `"initiator"` - `"target"` - `"both"` |
| **pwwn**  aliases: device_alias  string / required | pwwn member of the zone, use alias ‘device_alias’ as option for device_alias member |
| **remove**  boolean | Removes member from the zone if True  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | name of the zone |
| **remove**  boolean | Deletes the zone if True  **Choices:**   - `false` ← (default) - `true` |
| **zoneset**  list / elements=dictionary | List of zoneset options for the vsan |
| **action**  string | activates/de-activates the zoneset  **Choices:**   - `"activate"` - `"deactivate"` |
| **members**  list / elements=dictionary | Members of the zoneset that needs to be removed or added |
| **name**  string / required | name of the zone that needs to be added to the zoneset or removed from the zoneset |
| **remove**  boolean | Removes zone member from the zoneset  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | name of the zoneset |
| **remove**  boolean | Removes zoneset if True  **Choices:**   - `false` ← (default) - `true` |

## [Notes](storage.nxos_zone_zoneset_module.md#id3)

> **Note:**
>
> - Tested against Cisco MDS NX-OS 8.4(1)

## [Examples](storage.nxos_zone_zoneset_module.md#id4)

```yaml+jinja
- name: Test that zone/zoneset module works
  cisco.nxos.nxos_zone_zoneset:
    zone_zoneset_details:
    - mode: enhanced
      vsan: 22
      zone:
      - members:
        - pwwn: 11:11:11:11:11:11:11:11
        - device_alias: test123
        - pwwn: 61:61:62:62:12:12:12:12
          remove: true
        name: zoneA
      - members:
        - pwwn: 10:11:11:11:11:11:11:11
        - pwwn: 62:62:62:62:21:21:21:21
        name: zoneB
      - name: zoneC
        remove: true
      zoneset:
      - action: activate
        members:
        - name: zoneA
        - name: zoneB
        - name: zoneC
          remove: true
        name: zsetname1
      - action: deactivate
        name: zsetTestExtra
        remove: true
    - mode: basic
      smart_zoning: true
      vsan: 21
      zone:
      - members:
        - devtype: both
          pwwn: 11:11:11:11:11:11:11:11
        - pwwn: 62:62:62:62:12:12:12:12
        - devtype: both
          pwwn: 92:62:62:62:12:12:1a:1a
          remove: true
        name: zone21A
      - members:
        - pwwn: 10:11:11:11:11:11:11:11
        - pwwn: 62:62:62:62:21:21:21:21
        name: zone21B
      zoneset:
      - action: activate
        members:
        - name: zone21A
        - name: zone21B
        name: zsetname212
```

## [Return Values](storage.nxos_zone_zoneset_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["terminal dont-ask", "zone name zoneA vsan 923", "member pwwn 11:11:11:11:11:11:11:11", "no member device-alias test123", "zone commit vsan 923", "no terminal dont-ask"]` |
| **messages**  list / elements=string | debug messages  **Returned:** always  **Sample:** `["zone mode is already enhanced ,no change in zone mode configuration for vsan 922", "zone member '11:11:11:11:11:11:11:11' is already present in zone 'zoneA' in vsan 922 hence nothing to add", "zone member 'test123' is already present in zone 'zoneA' in vsan 922 hence nothing to add", "zone member '61:61:62:62:12:12:12:12' is not present in zone 'zoneA' in vsan 922 hence nothing to remove", "zone member '10:11:11:11:11:11:11:11' is already present in zone 'zoneB' in vsan 922 hence nothing to add", "zone member '62:62:62:62:21:21:21:21' is already present in zone 'zoneB' in vsan 922 hence nothing to add", "zone 'zoneC' is not present in vsan 922 , so nothing to remove"]` |

### Authors

- Suhas Bharadwaj (@srbharadwaj)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
