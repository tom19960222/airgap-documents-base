---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_interface module – NetApp ONTAP LIF configuration"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_interface_module.html
fetched_at: 2026-07-28T00:12:30+00:00
---
# netapp.ontap.na_ontap_interface module – NetApp ONTAP LIF configuration

> **Note:**
>
> This module is part of the [netapp.ontap collection](https://galaxy.ansible.com/netapp/ontap) (version 21.24.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
> You need further requirements to be able to use this module,
> see [Requirements](na_ontap_interface_module.md#ansible-collections-netapp-ontap-na-ontap-interface-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_interface`.

New in netapp.ontap 2.6.0

- [Synopsis](na_ontap_interface_module.md#synopsis)
- [Requirements](na_ontap_interface_module.md#requirements)
- [Parameters](na_ontap_interface_module.md#parameters)
- [Notes](na_ontap_interface_module.md#notes)
- [Examples](na_ontap_interface_module.md#examples)

## [Synopsis](na_ontap_interface_module.md#id1)

- Creating / deleting and modifying the LIF.

## [Requirements](na_ontap_interface_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address**  string | Specifies the LIF’s IP address.  ZAPI - Required when `state=present` and is_ipv4_link_local if false and subnet_name is not set.  REST - Required when `state=present` and `interface_type` is IP. |
| **admin_status**  string | Specifies the administrative status of the LIF.  Choices:   - `"up"` - `"down"` |
| **broadcast_domain**  string  added in netapp.ontap 21.21.0 | broadcast_domain name can be used to specify the location on an IP interface with REST, as an alternative to node or port.  only used when creating an IP interface to select a node, ignored if the interface already exists.  if the broadcast domain is not found, make sure to check the ipspace value.  home_port and broadcast_domain are mutually exclusive. home_node may or may not be present.  not supported for FC interface.  ignored with ZAPI. |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **current_node**  string | Specifies the LIF’s current node.  By default, this is home_node |
| **current_port**  string | Specifies the LIF’s current port. |
| **data_protocol**  string | The data protocol for which the FC interface is configured.  Ignored with ZAPI or for IP interfaces.  Required to create a FC type interface.  Choices:   - `"fcp"` - `"fc_nvme"` |
| **dns_domain_name**  string  added in netapp.ontap 2.9.0 | Specifies the unique, fully qualified domain name of the DNS zone of this LIF.  Supported from ONTAP 9.9.0 or later in REST.  Not supported for FC interfaces. |
| **failover_group**  string  added in netapp.ontap 20.1.0 | Specifies the failover group for the LIF.  Not supported with REST. |
| **failover_policy**  string | Specifies the failover policy for the LIF.  When using REST, this values are mapped to ‘home_port_only’, ‘default’, ‘home_node_only’, ‘sfo_partners_only’, ‘broadcast_domain_only’.  Choices:   - `"disabled"` - `"system-defined"` - `"local-only"` - `"sfo-partner-only"` - `"broadcast-domain-wide"` |
| **failover_scope**  string  added in netapp.ontap 21.13.0 | Specifies the failover scope for the LIF.  REST only, and only for IP interfaces. Not supported for FC interfaces.  Choices:   - `"home_port_only"` - `"default"` - `"home_node_only"` - `"sfo_partners_only"` - `"broadcast_domain_only"` |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **firewall_policy**  string | Specifies the firewall policy for the LIF.  This option is deprecated in REST.  With REST, the module tries to derive a service_policy and may error out. |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **force_subnet_association**  boolean  added in netapp.ontap 2.9.0 | Set this to true to acquire the address from the named subnet and assign the subnet to the LIF.  not supported with REST.  Choices:   - `false` - `true` |
| **from_name**  string  added in netapp.ontap 21.11.0 | name of the interface to be renamed |
| **home_node**  string | Specifies the LIF’s home node.  By default, the first node from the cluster is considered as home node. |
| **home_port**  string | Specifies the LIF’s home port.  Requires ONTAP 9.8 or later with FC interfaces when using REST.  With REST, at least one of home_port, home_node, or broadcast_domain is required to create IP interfaces.  With REST, either home_port or current_port is required to create FC interfaces.  With ZAPI, home_port is required to create IP and FC interfaces.  home_port and broadcast_domain are mutually exclusive (REST and IP interfaces). |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **ignore_zapi_options**  list / elements=string  added in netapp.ontap 21.13.0 | ignore unsupported options that should not be relevant.  ignored with ZAPI.  Choices:   - `"failover_group"` - `"force_subnet_association"` ← (default) - `"listen_for_dns_query"`   Default: `["force_subnet_association"]` |
| **interface_name**  string / required | Specifies the logical interface (LIF) name. |
| **interface_type**  string  added in netapp.ontap 21.13.0 | type of the interface.  IP is assumed if address or netmask are present.  IP interfaces includes cluster, intercluster, management, and NFS, CIFS, iSCSI interfaces.  FC interfaces includes FCP and NVME-FC interfaces.  ignored with ZAPI.  required with REST, but maybe derived from deprecated options like `role`, `protocols`, and `firewall_policy`.  Choices:   - `"fc"` - `"ip"` |
| **ipspace**  string  added in netapp.ontap 21.13.0 | IPspace name is required with REST for cluster-scoped interfaces. It is optional with SVM scope.  ignored with ZAPI. |
| **is_auto_revert**  boolean | If true, data LIF will revert to its home node under certain circumstances such as startup,  and load balancing migration capability is disabled automatically  Choices:   - `false` - `true` |
| **is_dns_update_enabled**  boolean  added in netapp.ontap 2.9.0 | Specifies if DNS update is enabled for this LIF. Dynamic updates will be sent for this LIF if updates are enabled at Vserver level.  Supported from ONTAP 9.9.1 or later in REST.  Not supported for FC interfaces.  Choices:   - `false` - `true` |
| **is_ipv4_link_local**  boolean  added in netapp.ontap 20.1.0 | Specifies the LIF’s are to acquire a ipv4 link local address.  Use case for this is when creating Cluster LIFs to allow for auto assignment of ipv4 link local address.  Not supported in REST  Choices:   - `false` - `true` |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **listen_for_dns_query**  boolean  added in netapp.ontap 2.9.0 | If True, this IP address will listen for DNS queries for the dnszone specified.  Not supported with REST.  Choices:   - `false` - `true` |
| **netmask**  string | Specifies the LIF’s netmask.  ZAPI - Required when `state=present` and is_ipv4_link_local if false and subnet_name is not set.  REST - Required when `state=present` and `interface_type` is IP. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **protocols**  list / elements=string | Specifies the list of data protocols configured on the LIF. By default, the values in this element are nfs, cifs and fcache.  Other supported protocols are iscsi and fcp. A LIF can be configured to not support any data protocols by specifying ‘none’.  Protocol values of none, iscsi, fc-nvme or fcp can’t be combined with any other data protocol(s).  address, netmask and firewall_policy parameters are not supported for ‘fc-nvme’ option.  This option is ignored with REST, though it can be used to derive `interface_type` or `data_protocol`. |
| **role**  string | Specifies the role of the LIF.  When setting role as “intercluster” or “cluster”, setting protocol is not supported.  When creating a “cluster” role, the node name will appear as the prefix in the name of LIF.  For example, if the specified name is clif and node name is node1, the LIF name appears in the ONTAP as node1_clif.  Possible values are ‘undef’, ‘cluster’, ‘data’, ‘node-mgmt’, ‘intercluster’, ‘cluster-mgmt’.  Required when `state=present` unless service_policy is present and ONTAP version is 9.8 or better.  This option is deprecated in REST.  With REST, the module tries to derive a service_policy and may error out. |
| **service_policy**  string  added in netapp.ontap 20.4.0 | Starting with ONTAP 9.5, you can configure LIF service policies to identify a single service or a list of services that will use a LIF.  In ONTAP 9.5, you can assign service policies only for LIFs in the admin SVM.  In ONTAP 9.6, you can additionally assign service policies for LIFs in the data SVMs.  When you specify a service policy for a LIF, you need not specify the data protocol and role for the LIF.  NOTE that role is still required because of a ZAPI issue. This limitation is removed in ONTAP 9.8.  Creating LIFs by specifying the role and data protocols is also supported. |
| **state**  string | Whether the specified interface should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **subnet_name**  string  added in netapp.ontap 2.8.0 | Subnet where the interface address is allocated from.  If the option is not used, the IP address will need to be provided by the administrator during configuration.  Not supported in REST. |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **vserver**  string | The name of the vserver to use.  Required with ZAPI.  Required with REST for FC interfaces (data vservers).  Required with REST for SVM-scoped IP interfaces (data vservers).  Invalid with REST for cluster-scoped IP interfaces.  To help with transition from ZAPI to REST, vserver is ignored when the role is set to ‘cluster’, ‘node-mgmt’, ‘intercluster’, ‘cluster-mgmt’.  Remove this option to suppress the warning. |

## [Notes](na_ontap_interface_module.md#id4)

> **Note:**
>
> - REST support requires ONTAP 9.7 or later.
> - Support check_mode.
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_interface_module.md#id5)

```yaml+jinja
- name: Create interface - ZAPI
  netapp.ontap.na_ontap_interface:
    state: present
    interface_name: data2
    home_port: e0d
    home_node: laurentn-vsim1
    role: data
    protocols:
      - nfs
      - cifs
    admin_status: up
    failover_policy: local-only
    firewall_policy: mgmt
    is_auto_revert: true
    address: 10.10.10.10
    netmask: 255.255.255.0
    force_subnet_association: false
    dns_domain_name: test.com
    listen_for_dns_query: true
    is_dns_update_enabled: true
    vserver: svm1
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Create data interface - REST - NAS
  netapp.ontap.na_ontap_interface:
    state: present
    interface_name: data2
    home_port: e0d
    home_node: laurentn-vsim1
    admin_status: up
    failover_scope: home_node_only
    service_policy: default-data-files
    is_auto_revert: true
    interface_type: ip
    address: 10.10.10.10
    netmask: 255.255.255.0
    vserver: svm1
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Create cluster interface - ZAPI
  netapp.ontap.na_ontap_interface:
    state: present
    interface_name: cluster_lif
    home_port: e0a
    home_node: cluster1-01
    role: cluster
    admin_status: up
    is_auto_revert: true
    is_ipv4_link_local: true
    vserver: Cluster
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Create cluster interface - REST
  netapp.ontap.na_ontap_interface:
    state: present
    interface_name: cluster_lif
    home_port: e0a
    home_node: cluster1-01
    service_policy: default-cluster
    admin_status: up
    is_auto_revert: true
    vserver: Cluster
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Rename interface
  netapp.ontap.na_ontap_interface:
    state: present
    from_name: ansibleSVM_lif
    interface_name: ansibleSVM_lif01
    vserver: ansibleSVM
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Migrate an interface
  netapp.ontap.na_ontap_interface:
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    vserver: ansible
    https: true
    validate_certs: false
    state: present
    interface_name: carchi_interface3
    home_port: e0d
    home_node: ansdev-stor-1
    current_node: ansdev-stor-2
    role: data
    failover_policy: local-only
    firewall_policy: mgmt
    is_auto_revert: true
    address: 10.10.10.12
    netmask: 255.255.255.0
    force_subnet_association: false
    admin_status: up

- name: Delete interface
  netapp.ontap.na_ontap_interface:
    state: absent
    interface_name: data2
    vserver: svm1
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
