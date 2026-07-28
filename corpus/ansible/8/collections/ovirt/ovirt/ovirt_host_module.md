---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirt_host module – Module to manage hosts in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirt_host_module.html
fetched_at: 2026-07-28T02:49:31+00:00
---
# ovirt.ovirt.ovirt_host module – Module to manage hosts in oVirt/RHV

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
> see [Requirements](ovirt_host_module.md#ansible-collections-ovirt-ovirt-ovirt-host-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_host`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_host_module.md#synopsis)
- [Requirements](ovirt_host_module.md#requirements)
- [Parameters](ovirt_host_module.md#parameters)
- [Notes](ovirt_host_module.md#notes)
- [Examples](ovirt_host_module.md#examples)
- [Return Values](ovirt_host_module.md#return-values)

## [Synopsis](ovirt_host_module.md#id1)

- Module to manage hosts in oVirt/RHV

## [Requirements](ovirt_host_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_host_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **activate**  boolean | If `state` is *present* activate the host.  This parameter is good to disable, when you don’t want to change the state of host when using *present* `state`.  **Choices:**   - `false` - `true` ← (default) |
| **address**  string | Host address. It can be either FQDN (preferred) or IP address. |
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
| **check_upgrade**  boolean | If *true* and `state` is *upgraded* run check for upgrade action before executing upgrade action.  **Choices:**   - `false` - `true` ← (default) |
| **cluster**  string | Name of the cluster, where host should be created. |
| **comment**  string | Description of the host. |
| **enroll_certificate**  boolean | Enrolls the certificate of the host. Useful in case you get a warning that it is about to expire or has already expired.  The host must be in maintenance status before enrolling the certificates.  **Choices:**   - `false` ← (default) - `true` |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  **Choices:**   - `false` ← (default) - `true` |
| **force**  boolean | Indicates that the host should be removed even if it is non-responsive, or if it is part of a Gluster Storage cluster and has volume bricks on it.  WARNING: It doesn’t forcibly remove the host if another host related operation is being executed on the host at the same time.  **Choices:**   - `false` ← (default) - `true` |
| **hosted_engine**  string | If *deploy* it means this host should deploy also hosted engine components.  If *undeploy* it means this host should un-deploy hosted engine components and this host will not function as part of the High Availability cluster.  **Choices:**   - `"deploy"` - `"undeploy"` |
| **id**  string | ID of the host to manage. |
| **iscsi**  dictionary | If `state` is *iscsidiscover* it means that the iscsi attribute is being used to discover targets  If `state` is *iscsilogin* it means that the iscsi attribute is being used to login to the specified targets passed as part of the iscsi attribute |
| **address**  string | Address of the iSCSI storage server. |
| **password**  string | A CHAP password for logging into a target. |
| **port**  string | The port being used to connect with iscsi. |
| **portal**  string | The portal being used to connect with iscsi. |
| **target**  string | The target IQN for the storage device. |
| **username**  string | A CHAP user name for logging into a target. |
| **kdump_integration**  string | Specify if host will have enabled Kdump integration.  **Choices:**   - `"enabled"` - `"disabled"` |
| **kernel_params**  list / elements=string | List of kernel boot parameters.  Following are most common kernel parameters used for host:  Hostdev Passthrough & SR-IOV: intel_iommu=on  Nested Virtualization: kvm-intel.nested=1  Unsafe Interrupts: vfio_iommu_type1.allow_unsafe_interrupts=1  PCI Reallocation: pci=realloc  `Note:`  Modifying kernel boot parameters settings can lead to a host boot failure. Please consult the product documentation before doing any changes.  Kernel boot parameters changes require host deploy and restart. The host needs to be *reinstalled* successfully and then to be *rebooted* for kernel boot parameters to be applied. |
| **name**  string / required | Name of the host to manage. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **override_display**  string | Override the display address of all VMs on this host with specified address. |
| **override_iptables**  boolean | If True host iptables will be overridden by host deploy script.  Note that `override_iptables` is *false* by default in oVirt/RHV.  **Choices:**   - `false` - `true` |
| **password**  string | Password of the root. It’s required in case `public_key` is set to *False*. |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  **Default:** `3` |
| **power_management_enabled**  boolean | Enable or disable power management of the host.  For more comprehensive setup of PM use `ovirt_host_pm` module.  **Choices:**   - `false` - `true` |
| **public_key**  aliases: ssh_public_key  boolean | *True* if the public key should be used to authenticate to host.  It’s required in case `password` is not set.  **Choices:**   - `false` ← (default) - `true` |
| **reboot_after_installation**  boolean | If *true* reboot host after successful installation.  Default value on engine is *true*.  **Choices:**   - `false` - `true` |
| **reboot_after_upgrade**  boolean | If *true* and `state` is *upgraded* reboot host after successful upgrade.  **Choices:**   - `false` - `true` ← (default) |
| **spm_priority**  integer | SPM priority of the host. Integer value from 1 to 10, where higher number means higher priority. |
| **ssh_port**  integer | The host SSH port. |
| **state**  string | State which should a host to be in after successful completion.  *iscsilogin* and *iscsidiscover* are supported since version 2.4.  *refreshed* is supported since 3.1.0  **Choices:**   - `"present"` ← (default) - `"absent"` - `"maintenance"` - `"upgraded"` - `"started"` - `"restarted"` - `"stopped"` - `"reinstalled"` - `"iscsidiscover"` - `"iscsilogin"` - `"refreshed"` |
| **timeout**  integer | The amount of time in seconds the module should wait for the host to get into desired state.  **Default:** `600` |
| **vgpu_placement**  string | If *consolidated*, each vGPU is placed on the first physical card with available space. This is the default placement, utilizing all available space on the physical cards.  If *separated*, each vGPU is placed on a separate physical card, if possible. This can be useful for improving vGPU performance.  **Choices:**   - `"consolidated"` - `"separated"` |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ovirt_host_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_host_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Add host with username/password supporting SR-IOV.
# Note that override_iptables is false by default in oVirt/RHV:
- ovirt.ovirt.ovirt_host:
    cluster: Default
    name: myhost
    address: 10.34.61.145
    password: secret
    override_iptables: true
    kernel_params:
      - intel_iommu=on

# Add host using public key
- ovirt.ovirt.ovirt_host:
    public_key: true
    cluster: Default
    name: myhost2
    address: 10.34.61.145
    override_iptables: true

# Deploy hosted engine host
- ovirt.ovirt.ovirt_host:
    cluster: Default
    name: myhost2
    password: secret
    address: 10.34.61.145
    override_iptables: true
    hosted_engine: deploy

# Maintenance
- ovirt.ovirt.ovirt_host:
    state: maintenance
    name: myhost

# Restart host using power management:
- ovirt.ovirt.ovirt_host:
    state: restarted
    name: myhost

# Upgrade host
- ovirt.ovirt.ovirt_host:
    state: upgraded
    name: myhost

# discover iscsi targets
- ovirt.ovirt.ovirt_host:
    state: iscsidiscover
    name: myhost
    iscsi:
      username: iscsi_user
      password: secret
      address: 10.34.61.145
      port: 3260

# login to iscsi targets
- ovirt.ovirt.ovirt_host:
    state: iscsilogin
    name: myhost
    iscsi:
      username: iscsi_user
      password: secret
      address: 10.34.61.145
      target: "iqn.2015-07.com.mlipchuk2.redhat:444"
      port: 3260

# Reinstall host using public key
- ovirt.ovirt.ovirt_host:
    state: reinstalled
    name: myhost
    public_key: true

# Remove host
- ovirt.ovirt.ovirt_host:
    state: absent
    name: myhost
    force: True

# Retry removing host when failed (https://bugzilla.redhat.com/show_bug.cgi?id=1719271)
- ovirt.ovirt.ovirt_host:
    state: absent
    name: myhost
  register: result
  until: not result.failed
  retries: 6
  delay: 20

# Change host Name
- ovirt.ovirt.ovirt_host:
    id: 00000000-0000-0000-0000-000000000000
    name: "new host name"

- name: Enroll host certificates
  ovirt.ovirt.ovirt_host:
    state: maintenance
    name: myhost
    enroll_certificate: True
```

## [Return Values](ovirt_host_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **host**  dictionary | Dictionary of all the host attributes. Host attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/host>.  **Returned:** On success if host is found. |
| **id**  string | ID of the host which is managed  **Returned:** On success if host is found.  **Sample:** `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |
| **iscsi_targets**  list / elements=string | List of host iscsi targets  **Returned:** On success if host is found and state is iscsidiscover. |

### Authors

- Ondra Machacek (@machacekondra)
- Martin Necas (@mnecas)

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
