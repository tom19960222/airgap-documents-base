---
collection: ansible
version: "6"
title: "ansible.posix.firewalld module – Manage arbitrary ports/services with firewalld"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/posix/firewalld_module.html
fetched_at: 2026-07-27T16:44:42+00:00
---
# ansible.posix.firewalld module – Manage arbitrary ports/services with firewalld

> **Note:**
>
> This module is part of the [ansible.posix collection](https://galaxy.ansible.com/ansible/posix) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.posix`.
> You need further requirements to be able to use this module,
> see [Requirements](firewalld_module.md#ansible-collections-ansible-posix-firewalld-module-requirements) for details.
>
> To use it in a playbook, specify: `ansible.posix.firewalld`.

- [Synopsis](firewalld_module.md#synopsis)
- [Requirements](firewalld_module.md#requirements)
- [Parameters](firewalld_module.md#parameters)
- [Notes](firewalld_module.md#notes)
- [Examples](firewalld_module.md#examples)

## [Synopsis](firewalld_module.md#id1)

- This module allows for addition or deletion of services and ports (either TCP or UDP) in either running or permanent firewalld rules.

## [Requirements](firewalld_module.md#id2)

The below requirements are needed on the host that executes this module.

- firewalld >= 0.2.11
- python-firewall >= 0.2.11

## [Parameters](firewalld_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **icmp_block**  string | The ICMP block you would like to add/remove to/from a zone in firewalld. |
| **icmp_block_inversion**  string | Enable/Disable inversion of ICMP blocks for a zone in firewalld. |
| **immediate**  boolean | Should this configuration be applied immediately, if set as permanent.  Choices:   - `false` ← (default) - `true` |
| **interface**  string | The interface you would like to add/remove to/from a zone in firewalld. |
| **masquerade**  string | The masquerade setting you would like to enable/disable to/from zones within firewalld. |
| **offline**  boolean | Whether to run this module even when firewalld is offline.  Choices:   - `false` - `true` |
| **permanent**  boolean | Should this configuration be in the running firewalld configuration or persist across reboots.  As of Ansible 2.3, permanent operations can operate on firewalld configs when it is not running (requires firewalld >= 0.3.9).  Note that if this is `no`, immediate is assumed `yes`.  Choices:   - `false` - `true` |
| **port**  string | Name of a port or port range to add/remove to/from firewalld.  Must be in the form PORT/PROTOCOL or PORT-PORT/PROTOCOL for port ranges. |
| **port_forward**  list / elements=dictionary | Port and protocol to forward using firewalld. |
| **port**  string / required | Source port to forward from |
| **proto**  string / required | protocol to forward  Choices:   - `"udp"` - `"tcp"` |
| **toaddr**  string | Optional address to forward to |
| **toport**  string / required | destination port |
| **rich_rule**  string | Rich rule to add/remove to/from firewalld.  See [Syntax for firewalld rich language rules](https://firewalld.org/documentation/man-pages/firewalld.richlanguage.html). |
| **service**  string | Name of a service to add/remove to/from firewalld.  The service must be listed in output of firewall-cmd –get-services. |
| **source**  string | The source/network you would like to add/remove to/from firewalld. |
| **state**  string / required | Enable or disable a setting.  For ports: Should this port accept (enabled) or reject (disabled) connections.  The states `present` and `absent` can only be used in zone level operations (i.e. when no other parameters but zone and state are set).  Choices:   - `"absent"` - `"disabled"` - `"enabled"` - `"present"` |
| **target**  string  added in ansible.posix 1.2.0 | firewalld Zone target  If state is set to `absent`, this will reset the target to default  Choices:   - `"default"` - `"ACCEPT"` - `"DROP"` - `"%%REJECT%%"` |
| **timeout**  integer | The amount of time in seconds the rule should be in effect for when non-permanent.  Default: `0` |
| **zone**  string | The firewalld zone to add/remove to/from.  Note that the default zone can be configured per system but `public` is default from upstream.  Available choices can be extended based on per-system configs, listed here are “out of the box” defaults.  Possible values include `block`, `dmz`, `drop`, `external`, `home`, `internal`, `public`, `trusted`, `work`. |

## [Notes](firewalld_module.md#id4)

> **Note:**
>
> - Not tested on any Debian based system.
> - Requires the python2 bindings of firewalld, which may not be installed by default.
> - For distributions where the python2 firewalld bindings are unavailable (e.g Fedora 28 and later) you will have to set the ansible_python_interpreter for these hosts to the python3 interpreter path and install the python3 bindings.
> - Zone transactions (creating, deleting) can be performed by using only the zone and state parameters “present” or “absent”. Note that zone transactions must explicitly be permanent. This is a limitation in firewalld. This also means that you will have to reload firewalld after adding a zone that you wish to perform immediate actions on. The module will not take care of this for you implicitly because that would undo any previously performed immediate actions which were not permanent. Therefore, if you require immediate access to a newly created zone it is recommended you reload firewalld immediately after the zone creation returns with a changed state and before you perform any other immediate, non-permanent actions on that zone.
> - This module needs `python-firewall` or `python3-firewall` on managed nodes. It is usually provided as a subset with `firewalld` from the OS distributor for the OS default Python interpreter.

## [Examples](firewalld_module.md#id5)

```yaml+jinja
- name: permit traffic in default zone for https service
  ansible.posix.firewalld:
    service: https
    permanent: yes
    state: enabled

- name: do not permit traffic in default zone on port 8081/tcp
  ansible.posix.firewalld:
    port: 8081/tcp
    permanent: yes
    state: disabled

- ansible.posix.firewalld:
    port: 161-162/udp
    permanent: yes
    state: enabled

- ansible.posix.firewalld:
    zone: dmz
    service: http
    permanent: yes
    state: enabled

- ansible.posix.firewalld:
    rich_rule: rule service name="ftp" audit limit value="1/m" accept
    permanent: yes
    state: enabled

- ansible.posix.firewalld:
    source: 192.0.2.0/24
    zone: internal
    state: enabled

- ansible.posix.firewalld:
    zone: trusted
    interface: eth2
    permanent: yes
    state: enabled

- ansible.posix.firewalld:
    masquerade: yes
    state: enabled
    permanent: yes
    zone: dmz

- ansible.posix.firewalld:
    zone: custom
    state: present
    permanent: yes

- ansible.posix.firewalld:
    zone: drop
    state: enabled
    permanent: yes
    icmp_block_inversion: yes

- ansible.posix.firewalld:
    zone: drop
    state: enabled
    permanent: yes
    icmp_block: echo-request

- ansible.posix.firewalld:
    zone: internal
    state: present
    permanent: yes
    target: ACCEPT

- name: Redirect port 443 to 8443 with Rich Rule
  ansible.posix.firewalld:
    rich_rule: rule family=ipv4 forward-port port=443 protocol=tcp to-port=8443
    zone: public
    permanent: yes
    immediate: yes
    state: enabled
```

### Authors

- Adam Miller (@maxamillion)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.posix)
[Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
