---
collection: ansible
version: "6"
title: "community.network.cnos_bgp module – Manage BGP resources and attributes on devices running CNOS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/cnos_bgp_module.html
fetched_at: 2026-07-27T17:18:04+00:00
---
# community.network.cnos_bgp module – Manage BGP resources and attributes on devices running CNOS

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.cnos_bgp`.

- [Synopsis](cnos_bgp_module.md#synopsis)
- [Parameters](cnos_bgp_module.md#parameters)
- [Notes](cnos_bgp_module.md#notes)
- [Examples](cnos_bgp_module.md#examples)
- [Return Values](cnos_bgp_module.md#return-values)

## [Synopsis](cnos_bgp_module.md#id1)

- This module allows you to work with Border Gateway Protocol (BGP) related configurations. The operators used are overloaded to ensure control over switch BGP configurations. This module is invoked using method with asNumber as one of its arguments. The first level of the BGP configuration allows to set up an AS number, with the following attributes going into various configuration operations under the context of BGP. After passing this level, there are eight BGP arguments that will perform further configurations. They are bgpArg1, bgpArg2, bgpArg3, bgpArg4, bgpArg5, bgpArg6, bgpArg7, and bgpArg8. For more details on how to use these arguments, see [Overloaded Variables]. This module uses SSH to manage network device configuration. The results of the operation will be placed in a directory named ‘results’ that must be created by the user in their local directory to where the playbook is run.

## [Parameters](cnos_bgp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **asNum**  string / required | AS number |
| **bgpArg1**  string / required | This is an overloaded bgp first argument. Usage of this argument can be found is the User Guide referenced above.  Choices:   - `"address-family"` - `"bestpath"` - `"bgp"` - `"cluster-id"` - `"confederation"` - `"enforce-first-as"` - `"fast-external-failover"` - `"graceful-restart"` - `"graceful-restart-helper"` - `"log-neighbor-changes"` - `"maxas-limit"` - `"neighbor"` - `"router-id"` - `"shutdown"` - `"synchronization"` - `"timers"` - `"vrf"` |
| **bgpArg2**  string | This is an overloaded bgp second argument. Usage of this argument can be found is the User Guide referenced above.  Choices:   - `"ipv4 or ipv6"` - `"always-compare-med"` - `"compare-confed-aspath"` - `"compare-routerid"` - `"dont-compare-originator-id"` - `"tie-break-on-age"` - `"as-path"` - `"med"` - `"identifier"` - `"peers"` |
| **bgpArg3**  string | This is an overloaded bgp third argument. Usage of this argument can be found is the User Guide referenced above.  Choices:   - `"aggregate-address"` - `"client-to-client"` - `"dampening"` - `"distance"` - `"maximum-paths"` - `"network"` - `"nexthop"` - `"redistribute"` - `"save"` - `"synchronization"` - `"ignore or multipath-relax"` - `"confed or missing-as-worst or non-deterministic or remove-recv-med or remove-send-med"` |
| **bgpArg4**  string | This is an overloaded bgp fourth argument. Usage of this argument can be found is the User Guide referenced above.  Choices:   - `"Aggregate prefix"` - `"Reachability Half-life time"` - `"route-map"` - `"Distance for routes ext"` - `"ebgp or ibgp"` - `"IP prefix <network>"` - `"IP prefix <network>/<length>"` - `"synchronization"` - `"Delay value"` - `"direct"` - `"ospf"` - `"static"` - `"memory"` |
| **bgpArg5**  string | This is an overloaded bgp fifth argument. Usage of this argument can be found is the User Guide referenced above.  Choices:   - `"as-set"` - `"summary-only"` - `"Value to start reusing a route"` - `"Distance for routes internal"` - `"Supported multipath numbers"` - `"backdoor"` - `"map"` - `"route-map"` |
| **bgpArg6**  string | This is an overloaded bgp sixth argument. Usage of this argument can be found is the User Guide referenced above.  Choices:   - `"summary-only"` - `"as-set"` - `"route-map name"` - `"Value to start suppressing a route"` - `"Distance local routes"` - `"Network mask"` - `"Pointer to route-map entries"` |
| **bgpArg7**  string | This is an overloaded bgp seventh argument. Use of this argument can be found is the User Guide referenced above.  Choices:   - `"Maximum duration to suppress a stable route(minutes)"` - `"backdoor"` - `"route-map"` - `"Name of the route map"` |
| **bgpArg8**  string | This is an overloaded bgp eight argument. Usage of this argument can be found is the User Guide referenced above.  Choices:   - `"Un-reachability Half-life time for the penalty(minutes)"` - `"backdoor"` |
| **deviceType**  string / required | This specifies the type of device where the method is executed. The choices NE1072T,NE1032,NE1032T,NE10032,NE2572 are added since Ansible 2.4. The choice NE0152T is added since 2.8  Choices:   - `"g8272_cnos"` - `"g8296_cnos"` - `"g8332_cnos"` - `"NE0152T"` - `"NE1072T"` - `"NE1032"` - `"NE1032T"` - `"NE10032"` - `"NE2572"` |
| **enablePassword**  string | Configures the password used to enter Global Configuration command mode on the switch. If the switch does not request this password, the parameter is ignored.While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used. |
| **host**  string / required | This is the variable used to search the hosts file at /etc/ansible/hosts and identify the IP address of the device on which the template is going to be applied. Usually the Ansible keyword {{ inventory_hostname }} is specified in the playbook as an abstraction of the group of network elements that need to be configured. |
| **outputfile**  string / required | This specifies the file path where the output of each command execution is saved. Each command that is specified in the merged template file and each response from the device are saved here. Usually the location is the results folder, but you can choose another location based on your write permission. |
| **password**  string / required | Configures the password used to authenticate the connection to the remote device. The value of the password parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used. |
| **username**  string / required | Configures the username used to authenticate the connection to the remote device. The value of the username parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used. |

## [Notes](cnos_bgp_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage Lenovo Network devices see <https://www.ansible.com/ansible-lenovo>.

## [Examples](cnos_bgp_module.md#id4)

```yaml+jinja
Tasks: The following are examples of using the module cnos_bgp. These are
 written in the main.yml file of the tasks directory.
---
- name: Test BGP  - neighbor
  community.network.cnos_bgp:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "neighbor"
      bgpArg2: "10.241.107.40"
      bgpArg3: 13
      bgpArg4: "address-family"
      bgpArg5: "ipv4"
      bgpArg6: "next-hop-self"

- name: Test BGP  - BFD
  community.network.cnos_bgp:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "neighbor"
      bgpArg2: "10.241.107.40"
      bgpArg3: 13
      bgpArg4: "bfd"

- name: Test BGP  - address-family - dampening
  community.network.cnos_bgp:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "address-family"
      bgpArg2: "ipv4"
      bgpArg3: "dampening"
      bgpArg4: 13
      bgpArg5: 233
      bgpArg6: 333
      bgpArg7: 15
      bgpArg8: 33

- name: Test BGP  - address-family - network
  community.network.cnos_bgp:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "address-family"
      bgpArg2: "ipv4"
      bgpArg3: "network"
      bgpArg4: "1.2.3.4/5"
      bgpArg5: "backdoor"

- name: Test BGP - bestpath - always-compare-med
  community.network.cnos_bgp:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "bestpath"
      bgpArg2: "always-compare-med"

- name: Test BGP - bestpath-compare-confed-aspat
  community.network.cnos_bgp:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "bestpath"
      bgpArg2: "compare-confed-aspath"

- name: Test BGP - bgp
  community.network.cnos_bgp:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "bgp"
      bgpArg2: 33

- name: Test BGP  - cluster-id
  community.network.cnos_bgp:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "cluster-id"
      bgpArg2: "1.2.3.4"

- name: Test BGP - confederation-identifier
  community.network.cnos_bgp:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "confederation"
      bgpArg2: "identifier"
      bgpArg3: 333

- name: Test BGP - enforce-first-as
  community.network.cnos_bgp:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "enforce-first-as"

- name: Test BGP - fast-external-failover
  community.network.cnos_bgp:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "fast-external-failover"

- name: Test BGP  - graceful-restart
  community.network.cnos_bgp:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "graceful-restart"
      bgpArg2: 333

- name: Test BGP - graceful-restart-helper
  community.network.cnos_bgp:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "graceful-restart-helper"

- name: Test BGP - maxas-limit
  community.network.cnos_bgp:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "maxas-limit"
      bgpArg2: 333

- name: Test BGP  - neighbor
  community.network.cnos_bgp:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "neighbor"
      bgpArg2: "10.241.107.40"
      bgpArg3: 13
      bgpArg4: "address-family"
      bgpArg5: "ipv4"
      bgpArg6: "next-hop-self"

- name: Test BGP - router-id
  community.network.cnos_bgp:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "router-id"
      bgpArg2: "1.2.3.4"

- name: Test BGP - synchronization
  community.network.cnos_bgp:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "synchronization"

- name: Test BGP - timers
  community.network.cnos_bgp:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "timers"
      bgpArg2: 333
      bgpArg3: 3333

- name: Test BGP - vrf
  community.network.cnos_bgp:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "vrf"
```

## [Return Values](cnos_bgp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success or failure message. Upon any failure, the method returns an error display string.  Returned: always |

### Authors

- Anil Kumar Muraleedharan (@amuraleedhar)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
