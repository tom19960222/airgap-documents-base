---
collection: ansible
version: "8"
title: "ansible.utils.ipsubnet filter – This filter can be used to manipulate network subnets in several ways."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/ipsubnet_filter.html
fetched_at: 2026-07-28T01:09:50+00:00
---
# ansible.utils.ipsubnet filter – This filter can be used to manipulate network subnets in several ways.

> **Note:**
>
> This filter plugin is part of the [ansible.utils collection](https://galaxy.ansible.com/ui/repo/published/ansible/utils/) (version 2.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.utils`.
>
> To use it in a playbook, specify: `ansible.utils.ipsubnet`.

New in ansible.utils 2.5.0

- [Synopsis](ipsubnet_filter.md#synopsis)
- [Keyword parameters](ipsubnet_filter.md#keyword-parameters)
- [Examples](ipsubnet_filter.md#examples)
- [Return Value](ipsubnet_filter.md#return-value)

## [Synopsis](ipsubnet_filter.md#id1)

- This filter can be used to manipulate network subnets in several ways.

## [Keyword parameters](ipsubnet_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.ipsubnet(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **index**  integer | The second argument of the ipsubnet() filter is an index number; by specifying it you can get a new subnet  with the specified index. |
| **query**  string | You can provide query as 1st argument.  To check if a given string is a subnet, pass it through the filter without any arguments. If the given string is an IP address, it will be converted into a subnet. If you specify a subnet size as the first parameter of the ipsubnet() filter, and the subnet size is smaller than the current one, you will get the number of subnets a given subnet can be split into.  **Default:** `""` |
| **value**  string / required | subnets or individual address or any other values input for ipsubnet plugin |

## [Examples](ipsubnet_filter.md#id3)

```yaml+jinja
#### examples
# Ipsubnet filter plugin with different queries.
vars:
  address: 192.168.144.5
  subnet: 192.168.0.0/16
  ipv6_address: '2001:4860:4860::8888'
  ipv6_subnet: '2600:1f1c:1b3:8f00::/56'
tasks:
  - name: convert IP address to subnet
    debug:
      msg: '{{ address | ansible.utils.ipsubnet }}'
  - name: check if a given string is a subnet
    debug:
      msg: '{{ subnet | ansible.utils.ipsubnet }}'
  - name: Get the number of subnets a given subnet can be split into.
    debug:
      msg: '{{ subnet | ansible.utils.ipsubnet(20) }}'
  - name: Get a 1st subnet
    debug:
      msg: '{{ subnet | ansible.utils.ipsubnet(20, 0) }}'
  - name: Get a last subnet
    debug:
      msg: '{{ subnet | ansible.utils.ipsubnet(20, -1) }}'
  - name: Get first IPv6 subnet that has prefix length /120
    debug:
      msg: '{{ ipv6_subnet | ansible.utils.ipsubnet(120, 0) }}'
  - name: Get last subnet that has prefix length /120
    debug:
      msg: '{{ ipv6_subnet | ansible.utils.ipsubnet(120, -1) }}'
  - name: Get biggest subnet that contains that given IP address.
    debug:
      msg: '{{ address | ansible.utils.ipsubnet(20) }}'
  - name: Get 1st smaller subnet by specifying 0 as index number
    debug:
      msg: '{{ address | ansible.utils.ipsubnet(18, 0) }}'
  - name: Get last subnet
    debug:
      msg: '{{ address | ansible.utils.ipsubnet(18, -1) }}'
  - name: >-
      The rank of the IP in the subnet (the IP is the 36870nth /32 of the
      subnet)
    debug:
      msg: '{{ address | ansible.utils.ipsubnet(subnet) }}'
  - name: The rank in the /24 that contain the address
    debug:
      msg: '{{ address | ansible.utils.ipsubnet(''192.168.144.0/24'') }}'
  - name: An IP with the subnet in the first /30 in a /24
    debug:
      msg: '{{ ''192.168.144.1/30'' | ansible.utils.ipsubnet(''192.168.144.0/24'') }}'
  - name: The fifth subnet /30 in a /24
    debug:
      msg: '{{ ''192.168.144.16/30'' | ansible.utils.ipsubnet(''192.168.144.0/24'') }}'

# PLAY [Ipsubnet filter plugin with different queries.] ****************************************************************
# TASK [convert IP address to subnet] *************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_ipsubnet.yaml:10
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "192.168.144.5/32"
# }
#
# TASK [check if a given string is a subnet] ******************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_ipsubnet.yaml:15
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "192.168.0.0/16"
# }
#
# TASK [Get the number of subnets a given subnet can be split into.] ******************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_ipsubnet.yaml:20
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "16"
# }
#
# TASK [Get a 1st subnet] *************************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_ipsubnet.yaml:25
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "192.168.0.0/20"
# }
#
# TASK [Get a last subnet] ************************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_ipsubnet.yaml:30
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "192.168.240.0/20"
# }
#
# TASK [Get biggest subnet that contains that given IP address.] **********************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_ipsubnet.yaml:35
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "192.168.144.0/20"
# }
#
# TASK [Get 1st smaller subnet by specifying 0 as index number] ***********************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_ipsubnet.yaml:40
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "192.168.128.0/18"
# }
#
# TASK [Get last subnet] **************************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_ipsubnet.yaml:45
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "192.168.144.4/31"
# }
#
# TASK [The rank of the IP in the subnet (the IP is the 36870nth /32 of the subnet)] **************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_ipsubnet.yaml:50
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "36870"
# }
#
# TASK [The rank in the /24 that contain the address] *********************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_ipsubnet.yaml:55
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "6"
# }
#
# TASK [An IP with the subnet in the first /30 in a /24] ******************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_ipsubnet.yaml:60
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "1"
# }
#
# TASK [he fifth subnet /30 in a /24] *************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_ipsubnet.yaml:65
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "5"
# }
```

## [Return Value](ipsubnet_filter.md#id4)

| Key | Description |
| --- | --- |
| **data**  any | Returns values valid for a particular query.  **Returned:** success |

### Authors

- Ashwini Mhatre (@amhatre)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
