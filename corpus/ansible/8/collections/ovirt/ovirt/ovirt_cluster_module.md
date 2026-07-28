---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirt_cluster module – Module to manage clusters in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirt_cluster_module.html
fetched_at: 2026-07-28T02:49:16+00:00
---
# ovirt.ovirt.ovirt_cluster module – Module to manage clusters in oVirt/RHV

> **Note:**
>
> This module is part of the [ovirt.ovirt collection](https://galaxy.ansible.com/ui/repo/published/ovirt/ovirt/) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ovirt.ovirt`.
> You need further requirements to be able to use this module,
> see [Requirements](ovirt_cluster_module.md#ansible-collections-ovirt-ovirt-ovirt-cluster-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_cluster`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_cluster_module.md#synopsis)
- [Requirements](ovirt_cluster_module.md#requirements)
- [Parameters](ovirt_cluster_module.md#parameters)
- [Notes](ovirt_cluster_module.md#notes)
- [Examples](ovirt_cluster_module.md#examples)
- [Return Values](ovirt_cluster_module.md#return-values)

## [Synopsis](ovirt_cluster_module.md#id1)

- Module to manage clusters in oVirt/RHV

## [Requirements](ovirt_cluster_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_cluster_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth**  dictionary / required | Dictionary with values needed to create HTTP/HTTPS connection to oVirt: |
| **ca_file**  string | A PEM file containing the trusted CA certificates.  The certificate presented by the server will be verified using these CA certificates.  If `ca_file` parameter is not set, system wide CA certificate store is used.  Default value is set by `OVIRT_CAFILE` environment variable. |
| **compress**  boolean | Flag indicating if compression is used for connection.  **Choices:**   - `false` - `true` ← (default) |
| **headers**  dictionary | Dictionary of HTTP headers to be added to each API call. |
| **hostname**  string | A string containing the hostname of the server, usually something like `*server.example.com*`.  Default value is set by `OVIRT_HOSTNAME` environment variable.  Either `url` or `hostname` is required. |
| **insecure**  boolean | A boolean flag that indicates if the server TLS certificate and host name should be checked.  **Choices:**   - `false` ← (default) - `true` |
| **kerberos**  boolean | A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.  **Choices:**   - `false` - `true` |
| **password**  string | The password of the user.  Default value is set by `OVIRT_PASSWORD` environment variable. |
| **timeout**  integer | Number of seconds to wait for response. |
| **token**  string | Token to be used instead of login with username/password.  Default value is set by `OVIRT_TOKEN` environment variable. |
| **url**  string | A string containing the API URL of the server, usually something like `*https://server.example.com/ovirt-engine/api*`.  Default value is set by `OVIRT_URL` environment variable.  Either `url` or `hostname` is required. |
| **username**  string | The name of the user, something like *admin@internal*.  Default value is set by `OVIRT_USERNAME` environment variable. |
| **ballooning**  aliases: balloon  boolean | If *True* enable memory balloon optimization. Memory balloon is used to re-distribute / reclaim the host memory based on VM needs in a dynamic way.  **Choices:**   - `false` - `true` |
| **comment**  string | Comment of the cluster. |
| **compatibility_version**  string | The compatibility version of the cluster. All hosts in this cluster must support at least this compatibility version. |
| **cpu_arch**  string | CPU architecture of cluster.  **Choices:**   - `"x86_64"` - `"ppc64"` - `"undefined"` |
| **cpu_type**  string | CPU codename. For example *Intel SandyBridge Family*. |
| **data_center**  string | Datacenter name where cluster reside. |
| **description**  string | Description of the cluster. |
| **external_network_providers**  list / elements=dictionary | List of references to the external network providers available in the cluster. If the automatic deployment of the external network provider is supported, the networks of the referenced network provider are available on every host in the cluster.  This is supported since oVirt version 4.2. |
| **id**  string | ID of the external network provider. Either `name` or `id` is required. |
| **name**  string | Name of the external network provider. Either `name` or `id` is required. |
| **fence_connectivity_threshold**  integer | The threshold used by `fence_skip_if_connectivity_broken`. |
| **fence_enabled**  boolean | If *True* enables fencing on the cluster.  Fencing is enabled by default.  **Choices:**   - `false` - `true` |
| **fence_skip_if_connectivity_broken**  boolean | If *True* fencing will be temporarily disabled if the percentage of hosts in the cluster that are experiencing connectivity issues is greater than or equal to the defined threshold.  The threshold can be specified by `fence_connectivity_threshold`.  **Choices:**   - `false` - `true` |
| **fence_skip_if_gluster_bricks_up**  boolean | A flag indicating if fencing should be skipped if Gluster bricks are up and running in the host being fenced.  This flag is optional, and the default value is `false`.  **Choices:**   - `false` - `true` |
| **fence_skip_if_gluster_quorum_not_met**  boolean | A flag indicating if fencing should be skipped if Gluster bricks are up and running and Gluster quorum will not be met without those bricks.  This flag is optional, and the default value is `false`.  **Choices:**   - `false` - `true` |
| **fence_skip_if_sd_active**  boolean | If *True* any hosts in the cluster that are Non Responsive and still connected to storage will not be fenced.  **Choices:**   - `false` - `true` |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_type**  string | The type of firewall to be used on hosts in this cluster.  Up to version 4.1, it was always *iptables*. Since version 4.2, you can choose between *iptables* and *firewalld*. For clusters with a compatibility version of 4.2 and higher, the default firewall type is *firewalld*.  **Choices:**   - `"firewalld"` - `"iptables"` |
| **gluster**  boolean | If *True*, hosts in this cluster will be used as Gluster Storage server nodes, and not for running virtual machines.  By default the cluster is created for virtual machine hosts.  **Choices:**   - `false` - `true` |
| **gluster_tuned_profile**  string | The name of the <https://fedorahosted.org/tuned> to set on all the hosts in the cluster. This is not mandatory and relevant only for clusters with Gluster service.  Could be for example *virtual-host*, *rhgs-sequential-io*, *rhgs-random-io* |
| **ha_reservation**  boolean | If *True* enables the oVirt/RHV to monitor cluster capacity for highly available virtual machines.  **Choices:**   - `false` - `true` |
| **host_reason**  boolean | If *True* enables an optional reason field when a host is placed into maintenance mode from the Manager, allowing the administrator to provide an explanation for the maintenance.  **Choices:**   - `false` - `true` |
| **id**  string | ID of the cluster to manage. |
| **ksm**  boolean | I *True* MoM enables to run Kernel Same-page Merging *KSM* when necessary and when it can yield a memory saving benefit that outweighs its CPU cost.  **Choices:**   - `false` - `true` |
| **ksm_numa**  boolean | If *True* enables KSM `ksm` for best performance inside NUMA nodes.  **Choices:**   - `false` - `true` |
| **mac_pool**  string | MAC pool to be used by this cluster.  `Note:`  This is supported since oVirt version 4.1. |
| **memory_policy**  aliases: performance_preset  string | *disabled* - Disables memory page sharing.  *server* - Sets the memory page sharing threshold to 150% of the system memory on each host.  *desktop* - Sets the memory page sharing threshold to 200% of the system memory on each host.  **Choices:**   - `"disabled"` - `"server"` - `"desktop"` |
| **migration_auto_converge**  string | If *True* auto-convergence is used during live migration of virtual machines.  Used only when `migration_policy` is set to *legacy*.  Following options are supported:  `true` - Override the global setting to *true*.  `false` - Override the global setting to *false*.  `inherit` - Use value which is set globally.  **Choices:**   - `"true"` - `"false"` - `"inherit"` |
| **migration_bandwidth**  string | The bandwidth settings define the maximum bandwidth of both outgoing and incoming migrations per host.  Following bandwidth options are supported:  `auto` - Bandwidth is copied from the *rate limit* [Mbps] setting in the data center host network QoS.  `hypervisor_default` - Bandwidth is controlled by local VDSM setting on sending host.  `custom` - Defined by user (in Mbps).  **Choices:**   - `"auto"` - `"hypervisor_default"` - `"custom"` |
| **migration_bandwidth_limit**  integer | Set the *custom* migration bandwidth limit.  This parameter is used only when `migration_bandwidth` is *custom*. |
| **migration_compressed**  string | If *True* compression is used during live migration of the virtual machine.  Used only when `migration_policy` is set to *legacy*.  Following options are supported:  `true` - Override the global setting to *true*.  `false` - Override the global setting to *false*.  `inherit` - Use value which is set globally.  **Choices:**   - `"true"` - `"false"` - `"inherit"` |
| **migration_encrypted**  string | If *True* encryption is used during live migration of the virtual machine.  Following options are supported:  `true` - Override the global setting to *true*.  `false` - Override the global setting to *false*.  `inherit` - Use value which is set globally.  **Choices:**   - `"true"` - `"false"` - `"inherit"` |
| **migration_policy**  string | A migration policy defines the conditions for live migrating virtual machines in the event of host failure.  Following policies are supported:  `legacy` - Legacy behavior of 3.6 version.  `minimal_downtime` - Virtual machines should not experience any significant downtime.  `suspend_workload` - Virtual machines may experience a more significant downtime.  `post_copy` - Virtual machines should not experience any significant downtime. If the VM migration is not converging for a long time, the migration will be switched to post-copy. Added in version *2.4*.  **Choices:**   - `"legacy"` - `"minimal_downtime"` - `"suspend_workload"` - `"post_copy"` |
| **name**  string / required | Name of the cluster to manage. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **network**  string | Management network of cluster to access cluster hosts. |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  **Default:** `3` |
| **resilience_policy**  string | The resilience policy defines how the virtual machines are prioritized in the migration.  Following values are supported:  `do_not_migrate` - Prevents virtual machines from being migrated.  `migrate` - Migrates all virtual machines in order of their defined priority.  `migrate_highly_available` - Migrates only highly available virtual machines to prevent overloading other hosts.  **Choices:**   - `"do_not_migrate"` - `"migrate"` - `"migrate_highly_available"` |
| **rng_sources**  list / elements=string | List that specify the random number generator devices that all hosts in the cluster will use.  Supported generators are: *hwrng* and *random*. |
| **scheduling_policy**  string | Name of the scheduling policy to be used for cluster. |
| **scheduling_policy_properties**  list / elements=dictionary | Custom scheduling policy properties of the cluster.  These optional properties override the properties of the scheduling policy specified by the `scheduling_policy` parameter. |
| **name**  string | Name of the scheduling policy property. |
| **value**  string | Value of scheduling policy property. |
| **serial_policy**  string | Specify a serial number policy for the virtual machines in the cluster.  Following options are supported:  `vm` - Sets the virtual machine’s UUID as its serial number.  `host` - Sets the host’s UUID as the virtual machine’s serial number.  `custom` - Allows you to specify a custom serial number in `serial_policy_value`.  **Choices:**   - `"vm"` - `"host"` - `"custom"` |
| **serial_policy_value**  string | Allows you to specify a custom serial number.  This parameter is used only when `serial_policy` is *custom*. |
| **spice_proxy**  string | The proxy by which the SPICE client will connect to virtual machines.  The address must be in the following format: *protocol://[host]:[port]* |
| **state**  string | Should the cluster be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **switch_type**  string | Type of switch to be used by all networks in given cluster. Either *legacy* which is using linux bridge or *ovs* using Open vSwitch.  **Choices:**   - `"legacy"` - `"ovs"` |
| **threads_as_cores**  boolean | If *True* the exposed host threads would be treated as cores which can be utilized by virtual machines.  **Choices:**   - `false` - `true` |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  **Default:** `180` |
| **trusted_service**  boolean | If *True* enables integration with an OpenAttestation server.  **Choices:**   - `false` - `true` |
| **virt**  boolean | If *True*, hosts in this cluster will be used to run virtual machines.  **Choices:**   - `false` - `true` |
| **vm_reason**  boolean | If *True* enables an optional reason field when a virtual machine is shut down from the Manager, allowing the administrator to provide an explanation for the maintenance.  **Choices:**   - `false` - `true` |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ovirt_cluster_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_cluster_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Create cluster
- ovirt.ovirt.ovirt_cluster:
    data_center: mydatacenter
    name: mycluster
    cpu_type: Intel SandyBridge Family
    description: mycluster
    compatibility_version: 4.0

# Create virt service cluster:
- ovirt.ovirt.ovirt_cluster:
    data_center: mydatacenter
    name: mycluster
    cpu_type: Intel Nehalem Family
    description: mycluster
    switch_type: legacy
    compatibility_version: 4.0
    ballooning: true
    gluster: false
    threads_as_cores: true
    ha_reservation: true
    trusted_service: false
    host_reason: false
    vm_reason: true
    ksm_numa: true
    memory_policy: server
    rng_sources:
      - hwrng
      - random

# Create cluster with default network provider
- ovirt.ovirt.ovirt_cluster:
    name: mycluster
    data_center: Default
    cpu_type: Intel SandyBridge Family
    external_network_providers:
      - name: ovirt-provider-ovn

# Remove cluster
- ovirt.ovirt.ovirt_cluster:
    state: absent
    name: mycluster

# Change cluster Name
- ovirt.ovirt.ovirt_cluster:
    id: 00000000-0000-0000-0000-000000000000
    name: "new_cluster_name"
```

## [Return Values](ovirt_cluster_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cluster**  dictionary | Dictionary of all the cluster attributes. Cluster attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/cluster>.  **Returned:** On success if cluster is found. |
| **id**  string | ID of the cluster which is managed  **Returned:** On success if cluster is found.  **Sample:** `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |

### Authors

- Ondra Machacek (@machacekondra)
- Martin Necas (@mnecas)

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
