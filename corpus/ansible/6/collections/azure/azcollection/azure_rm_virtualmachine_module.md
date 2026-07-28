---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_virtualmachine module – Manage Azure virtual machines"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_virtualmachine_module.html
fetched_at: 2026-07-27T16:47:16+00:00
---
# azure.azcollection.azure_rm_virtualmachine module – Manage Azure virtual machines

> **Note:**
>
> This module is part of the [azure.azcollection collection](https://galaxy.ansible.com/azure/azcollection) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install azure.azcollection`.
> You need further requirements to be able to use this module,
> see [Requirements](azure_rm_virtualmachine_module.md#ansible-collections-azure-azcollection-azure-rm-virtualmachine-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_virtualmachine`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_virtualmachine_module.md#synopsis)
- [Requirements](azure_rm_virtualmachine_module.md#requirements)
- [Parameters](azure_rm_virtualmachine_module.md#parameters)
- [Notes](azure_rm_virtualmachine_module.md#notes)
- [See Also](azure_rm_virtualmachine_module.md#see-also)
- [Examples](azure_rm_virtualmachine_module.md#examples)
- [Return Values](azure_rm_virtualmachine_module.md#return-values)

## [Synopsis](azure_rm_virtualmachine_module.md#id1)

- Manage and configure virtual machines (VMs) and associated resources on Azure.
- Requires a resource group containing at least one virtual network with at least one subnet.
- Supports images from the Azure Marketplace, which can be discovered with [azure.azcollection.azure_rm_virtualmachineimage_info](azure_rm_virtualmachineimage_info_module.md#ansible-collections-azure-azcollection-azure-rm-virtualmachineimage-info-module).
- Supports custom images since Ansible 2.5.
- To use *custom_data* on a Linux image, the image must have cloud-init enabled. If cloud-init is not enabled, *custom_data* is ignored.

## [Requirements](azure_rm_virtualmachine_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_virtualmachine_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **accept_terms**  boolean | Accept terms for Marketplace images that require it.  Only Azure service admin/account admin users can purchase images from the Marketplace.  Only valid when a *plan* is specified.  Choices:   - `false` ← (default) - `true` |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  added in azure.azcollection 0.0.1 | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **admin_password**  string | Password for the admin username.  Not required if the *os_type=Linux* and SSH password authentication is disabled by setting *ssh_password_enabled=false*. |
| **admin_username**  string | Admin username used to access the VM after it is created.  Required when creating a VM. |
| **allocated**  boolean | Whether the VM is allocated or deallocated, only useful with *state=present*.  Choices:   - `false` - `true` ← (default) |
| **api_profile**  string  added in azure.azcollection 0.0.1 | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  Default: `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  Choices:   - `false` - `true` ← (default) |
| **auth_source**  string  added in azure.azcollection 0.0.1 | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  Choices:   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **availability_set**  string | Name or ID of an existing availability set to add the VM to. The *availability_set* should be in the same resource group as VM. |
| **boot_diagnostics**  string | Manage boot diagnostics settings for a VM.  Boot diagnostics includes a serial console and remote console screenshots. |
| **enabled**  boolean / required | Flag indicating if boot diagnostics are enabled.  Choices:   - `false` - `true` |
| **resource_group**  string | Resource group where the storage account is located. |
| **storage_account**  string | The name of an existing storage account to use for boot diagnostics.  If not specified, uses *storage_account_name* defined one level up.  If storage account is not specified anywhere, and `enabled` is `true`, a default storage account is created for boot diagnostics data. |
| **cert_validation_mode**  string  added in azure.azcollection 0.0.1 | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  Choices:   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  added in azure.azcollection 0.0.1 | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  Default: `"AzureCloud"` |
| **custom_data**  string | Data made available to the VM and used by `cloud-init`.  Only used on Linux images with `cloud-init` enabled.  Consult <https://docs.microsoft.com/en-us/azure/virtual-machines/linux/using-cloud-init#cloud-init-overview> for cloud-init ready images.  To enable cloud-init on a Linux image, follow <https://docs.microsoft.com/en-us/azure/virtual-machines/linux/cloudinit-prepare-custom-image>. |
| **data_disks**  string | Describes list of data disks.  Use azure.azcollection.azure_rm_mangeddisk to manage the specific disk. |
| **caching**  string | Type of data disk caching.  Choices:   - `"ReadOnly"` ← (default) - `"ReadWrite"` |
| **disk_size_gb**  string | The initial disk size in GB for blank data disks.  This value cannot be larger than `1023` GB.  Size can be changed only when the virtual machine is deallocated.  Not sure when *managed_disk_id* defined. |
| **lun**  string / required | The logical unit number for data disk.  This value is used to identify data disks within the VM and therefore must be unique for each data disk attached to a VM. |
| **managed_disk_type**  string | Managed data disk type.  Only used when OS disk created with managed disk.  Choices:   - `"Standard_LRS"` - `"StandardSSD_LRS"` - `"StandardSSD_ZRS"` - `"Premium_LRS"` - `"Premium_ZRS"` |
| **storage_account_name**  string | Name of an existing storage account that supports creation of VHD blobs.  If not specified for a new VM, a new storage account started with *name* will be created using storage type `Standard_LRS`.  Only used when OS disk created with virtual hard disk (VHD).  Used when *managed_disk_type* not defined.  Cannot be updated unless *lun* updated. |
| **storage_blob_name**  string | Name of the storage blob used to hold the OS disk image of the VM.  Must end with ‘.vhd’.  Default to the *name* + timestamp + *lun* + ‘.vhd’.  Only used when OS disk created with virtual hard disk (VHD).  Used when *managed_disk_type* not defined.  Cannot be updated unless *lun* updated. |
| **storage_container_name**  string | Name of the container to use within the storage account to store VHD blobs.  If no name is specified a default container named ‘vhds’ will created.  Only used when OS disk created with virtual hard disk (VHD).  Used when *managed_disk_type* not defined.  Cannot be updated unless *lun* updated.  Default: `"vhds"` |
| **ephemeral_os_disk**  boolean | Parameters of ephemeral disk settings that can be specified for operating system disk.  Ephemeral OS disk is only supported for VMS Instances using Managed Disk.  Choices:   - `false` - `true` |
| **eviction_policy**  string | Specifies the eviction policy for the Azure Spot virtual machine.  Requires priority to be set to Spot.  Choices:   - `"Deallocate"` - `"Delete"` |
| **generalized**  boolean | Whether the VM is generalized or not.  Set to `true` with *state=present* to generalize the VM.  Generalizing a VM is irreversible.  Choices:   - `false` ← (default) - `true` |
| **image**  string / required | The image used to build the VM.  For custom images, the name of the image. To narrow the search to a specific resource group, a dict with the keys *name* and *resource_group*.  For Marketplace images, a dict with the keys *publisher*, *offer*, *sku*, and *version*.  Set *version=latest* to get the most recent version of a given image. |
| **license_type**  string | On-premise license for the image or disk.  Only used for images that contain the Windows Server operating system.  To remove all license type settings, set to the string `None`.  Choices:   - `"Windows_Server"` - `"Windows_Client"` - `"RHEL_BYOS"` - `"SLES_BYOS"` |
| **linux_config**  string | Specifies the Linux operating system settings on the virtual machine. |
| **disable_password_authentication**  boolean | Specifies whether password authentication should be disabled.  Choices:   - `false` - `true` |
| **location**  string | Valid Azure location for the VM. Defaults to location of the resource group. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **managed_disk_type**  string | Managed OS disk type.  Create OS disk with managed disk if defined.  If not defined, the OS disk will be created with virtual hard disk (VHD).  Choices:   - `"Standard_LRS"` - `"StandardSSD_LRS"` - `"StandardSSD_ZRS"` - `"Premium_LRS"` - `"Premium_ZRS"` |
| **max_price**  string | Specifies the maximum price you are willing to pay for a Azure Spot VM/VMSS.  This price is in US Dollars.  `-1` indicates default price to be up-to on-demand.  Requires priority to be set to Spot.  Default: `-1` |
| **name**  string / required | Name of the VM. |
| **network_interface_names**  aliases: network_interfaces  list / elements=string | Network interface names to add to the VM.  Can be a string of name or resource ID of the network interface.  Can be a dict containing *resource_group* and *name* of the network interface.  If a network interface name is not provided when the VM is created, a default network interface will be created.  To create a new network interface, at least one Virtual Network with one Subnet must exist. |
| **open_ports**  string | List of ports to open in the security group for the VM, when a security group and network interface are created with a VM.  For Linux hosts, defaults to allowing inbound TCP connections to port 22.  For Windows hosts, defaults to opening ports 3389 and 5986. |
| **os_disk_caching**  aliases: disk_caching  string | Type of OS disk caching.  Choices:   - `"ReadOnly"` - `"ReadWrite"` |
| **os_disk_name**  string | OS disk name. |
| **os_disk_size_gb**  string | Type of OS disk size in GB. |
| **os_type**  string | Base type of operating system.  Choices:   - `"Windows"` - `"Linux"` ← (default) |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **plan**  dictionary | Third-party billing plan for the VM. |
| **name**  string / required | Billing plan name. |
| **product**  string / required | Product name. |
| **promotion_code**  string | Optional promotion code. |
| **publisher**  string / required | Publisher offering the plan. |
| **priority**  string | Priority of the VM.  `None` is the equivalent of Regular VM.  Choices:   - `"None"` - `"Spot"` |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **proximity_placement_group**  dictionary | The name or ID of the proximity placement group the VM should be associated with. |
| **id**  string | The ID of the proximity placement group the VM should be associated with. |
| **name**  string | The Name of the proximity placement group the VM should be associated with. |
| **resource_group**  string | The resource group of the proximity placement group the VM should be associated with. |
| **public_ip_allocation_method**  aliases: public_ip_allocation  string | Allocation method for the public IP of the VM.  Used only if a network interface is not specified.  When set to `Dynamic`, the public IP address may change any time the VM is rebooted or power cycled.  The `Disabled` choice was added in Ansible 2.6.  Choices:   - `"Dynamic"` - `"Static"` ← (default) - `"Disabled"` |
| **remove_on_absent**  list / elements=string | Associated resources to remove when removing a VM using *state=absent*.  To remove all resources related to the VM being removed, including auto-created resources, set to `all`.  To remove only resources that were automatically created while provisioning the VM being removed, set to `all_autocreated`.  To remove only specific resources, set to `network_interfaces`, `virtual_storage` or `public_ips`.  Any other input will be ignored.  Default: `["all"]` |
| **resource_group**  string / required | Name of the resource group containing the VM. |
| **restarted**  boolean | Set to `true` with *state=present* to restart a running VM.  Choices:   - `false` ← (default) - `true` |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **short_hostname**  string | Name assigned internally to the host. On a Linux VM this is the name returned by the `hostname` command.  When creating a VM, short_hostname defaults to *name*. |
| **ssh_password_enabled**  boolean | Whether to enable or disable SSH passwords.  When *os_type=Linux*, set to `false` to disable SSH password authentication and require use of SSH keys.  Choices:   - `false` - `true` ← (default) |
| **ssh_public_keys**  string | For *os_type=Linux* provide a list of SSH keys.  Accepts a list of dicts where each dictionary contains two keys, *path* and *key_data*.  Set *path* to the default location of the authorized_keys files. For example, *path=/home/<admin username>/.ssh/authorized_keys*.  Set *key_data* to the actual value of the public key. |
| **started**  boolean | Whether the VM is started or stopped.  Set to (true) with *state=present* to start the VM.  Set to `false` to stop the VM.  Choices:   - `false` - `true` |
| **state**  string | State of the VM.  Set to `present` to create a VM with the configuration specified by other options, or to update the configuration of an existing VM.  Set to `absent` to remove a VM.  Does not affect power state. Use *started*/*allocated*/*restarted* parameters to change the power state of a VM.  Choices:   - `"absent"` - `"present"` ← (default) |
| **storage_account_name**  aliases: storage_account  string | Name of a storage account that supports creation of VHD blobs.  If not specified for a new VM, a new storage account named <vm name>01 will be created using storage type `Standard_LRS`. |
| **storage_blob_name**  aliases: storage_blob  string | Name of the storage blob used to hold the OS disk image of the VM.  Must end with ‘.vhd’.  If not specified, defaults to the VM name + ‘.vhd’. |
| **storage_container_name**  aliases: storage_container  string | Name of the container to use within the storage account to store VHD blobs.  If not specified, a default container will be created.  Default: `"vhds"` |
| **subnet_name**  aliases: subnet  string | Subnet for the VM.  Defaults to the first subnet found in the virtual network or the subnet of the *network_interface_name*, if provided.  If the subnet is in another resource group, specify the resource group with *virtual_network_resource_group*. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **virtual_network_name**  aliases: virtual_network  string | The virtual network to use when creating a VM.  If not specified, a new network interface will be created and assigned to the first virtual network found in the resource group.  Use with *virtual_network_resource_group* to place the virtual network in another resource group. |
| **virtual_network_resource_group**  string | The resource group to use when creating a VM with another resource group’s virtual network. |
| **vm_identity**  string | Identity for the VM.  Choices:   - `"SystemAssigned"` |
| **vm_size**  string | A valid Azure VM size value. For example, `Standard_D4`.  Choices vary depending on the subscription and location. Check your subscription for available choices.  Required when creating a VM. |
| **windows_config**  string | Specifies Windows operating system settings on the virtual machine. |
| **enable_automatic_updates**  boolean / required | Indicates whether Automatic Updates is enabled for the Windows virtual machine.  Choices:   - `false` - `true` |
| **provision_vm_agent**  boolean / required | Indicates whether virtual machine agent should be provisioned on the virtual machine.  Choices:   - `false` - `true` |
| **winrm**  string | List of Windows Remote Management configurations of the VM. |
| **certificate_store**  string | The certificate store on the VM to which the certificate should be added.  The specified certificate store is implicitly in the LocalMachine account. |
| **certificate_url**  string | The URL of a certificate that has been uploaded to Key Vault as a secret. |
| **protocol**  string / required | The protocol of the winrm listener.  Choices:   - `"http"` - `"https"` |
| **source_vault**  string | The relative URL of the Key Vault containing the certificate. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |
| **zones**  list / elements=string | A list of Availability Zones for your VM. |

## [Notes](azure_rm_virtualmachine_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_virtualmachine_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_virtualmachine_module.md#id6)

```yaml+jinja
- name: Create VM with defaults
  azure_rm_virtualmachine:
    resource_group: myResourceGroup
    name: testvm10
    admin_username: "{{ username }}"
    admin_password: "{{ password }}"
    image:
      offer: CentOS
      publisher: OpenLogic
      sku: '7.1'
      version: latest

- name: Create an availability set for managed disk vm
  azure_rm_availabilityset:
    name: avs-managed-disk
    resource_group: myResourceGroup
    platform_update_domain_count: 5
    platform_fault_domain_count: 2
    sku: Aligned

- name: Create a VM with managed disk
  azure_rm_virtualmachine:
    resource_group: myResourceGroup
    name: vm-managed-disk
    admin_username: "{{ username }}"
    availability_set: avs-managed-disk
    managed_disk_type: Standard_LRS
    image:
      offer: 0001-com-ubuntu-server-focal
      publisher: canonical
      sku: 20_04-lts-gen2
      version: latest
    vm_size: Standard_D4

- name: Create a VM with existing storage account and NIC
  azure_rm_virtualmachine:
    resource_group: myResourceGroup
    name: testvm002
    vm_size: Standard_D4
    storage_account: testaccount001
    admin_username: "{{ username }}"
    ssh_public_keys:
      - path: /home/adminUser/.ssh/authorized_keys
        key_data: < insert your ssh public key here... >
    network_interfaces: testvm001
    image:
      offer: CentOS
      publisher: OpenLogic
      sku: '7.1'
      version: latest

- name: Create a VM with OS and multiple data managed disks
  azure_rm_virtualmachine:
    resource_group: myResourceGroup
    name: testvm001
    vm_size: Standard_D4
    managed_disk_type: Standard_LRS
    admin_username: "{{ username }}"
    ssh_public_keys:
      - path: /home/adminUser/.ssh/authorized_keys
        key_data: < insert your ssh public key here... >
    image:
      offer: 0001-com-ubuntu-server-focal
      publisher: canonical
      sku: 20_04-lts-gen2
      version: latest
    data_disks:
      - lun: 0
        managed_disk_id: "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDisk"
      - lun: 1
        disk_size_gb: 128
        managed_disk_type: Premium_LRS

- name: Create a VM with OS and multiple data storage accounts
  azure_rm_virtualmachine:
    resource_group: myResourceGroup
    name: testvm001
    vm_size: Standard_DS1_v2
    admin_username: "{{ username }}"
    ssh_password_enabled: false
    ssh_public_keys:
      - path: /home/adminUser/.ssh/authorized_keys
        key_data: < insert your ssh public key here... >
    network_interfaces: testvm001
    storage_container: osdisk
    storage_blob: osdisk.vhd
    boot_diagnostics:
      enabled: yes
    image:
      offer: 0001-com-ubuntu-server-focal
      publisher: canonical
      sku: 20_04-lts-gen2
      version: latest
    data_disks:
      - lun: 0
        disk_size_gb: 64
        storage_container_name: datadisk1
        storage_blob_name: datadisk1.vhd
      - lun: 1
        disk_size_gb: 128
        storage_container_name: datadisk2
        storage_blob_name: datadisk2.vhd

- name: Create a VM with a custom image
  azure_rm_virtualmachine:
    resource_group: myResourceGroup
    name: testvm001
    vm_size: Standard_DS1_v2
    admin_username: "{{ username }}"
    admin_password: "{{ password }}"
    image: customimage001

- name: Create a VM with a custom image from a particular resource group
  azure_rm_virtualmachine:
    resource_group: myResourceGroup
    name: testvm001
    vm_size: Standard_DS1_v2
    admin_username: "{{ username }}"
    admin_password: "{{ password }}"
    image:
      name: customimage001
      resource_group: myResourceGroup

- name: Create a VM with an image id
  azure_rm_virtualmachine:
    resource_group: myResourceGroup
    name: testvm001
    vm_size: Standard_DS1_v2
    admin_username: "{{ username }}"
    admin_password: "{{ password }}"
    image:
      id: '{{image_id}}'

- name: Create a VM with spcified OS disk size
  azure_rm_virtualmachine:
    resource_group: myResourceGroup
    name: big-os-disk
    admin_username: "{{ username }}"
    admin_password: "{{ password }}"
    os_disk_size_gb: 512
    image:
      offer: CentOS
      publisher: OpenLogic
      sku: '7.1'
      version: latest

- name: Create a VM with OS and Plan, accepting the terms
  azure_rm_virtualmachine:
    resource_group: myResourceGroup
    name: f5-nva
    admin_username: "{{ username }}"
    admin_password: "{{ password }}"
    image:
      publisher: f5-networks
      offer: f5-big-ip-best
      sku: f5-bigip-virtual-edition-200m-best-hourly
      version: latest
    plan:
      name: f5-bigip-virtual-edition-200m-best-hourly
      product: f5-big-ip-best
      publisher: f5-networks

- name: Create a VM with Spot Instance
  azure_rm_virtualmachine:
    resource_group: myResourceGroup
    name: testvm10
    vm_size: Standard_D4
    priority: Spot
    eviction_policy: Deallocate
    admin_username: "{{ username }}"
    admin_password: "{{ password }}"
    image:
      offer: CentOS
      publisher: OpenLogic
      sku: '7.1'
      version: latest

- name: Power Off
  azure_rm_virtualmachine:
    resource_group: myResourceGroup
    name: testvm002
    started: no

- name: Deallocate
  azure_rm_virtualmachine:
    resource_group: myResourceGroup
    name: testvm002
    allocated: no

- name: Power On
  azure_rm_virtualmachine:
    resource_group: myResourceGroup
    name: testvm002

- name: Restart
  azure_rm_virtualmachine:
    resource_group: myResourceGroup
    name: testvm002
    restarted: yes

- name: Create a VM with an Availability Zone
  azure_rm_virtualmachine:
    resource_group: myResourceGroup
    name: testvm001
    vm_size: Standard_DS1_v2
    admin_username: "{{ username }}"
    admin_password: "{{ password }}"
    image: customimage001
    zones: [1]

- name: Remove a VM and all resources that were autocreated
  azure_rm_virtualmachine:
    resource_group: myResourceGroup
    name: testvm002
    remove_on_absent: all_autocreated
    state: absent
```

## [Return Values](azure_rm_virtualmachine_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **azure_vm**  dictionary | Facts about the current state of the object. Note that facts are not part of the registered output but available directly.  Returned: always  Sample: `{"properties": {"availabilitySet": {"id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Compute/availabilitySets/MYAVAILABILITYSET"}, "hardwareProfile": {"vmSize": "Standard_D1"}, "instanceView": {"disks": [{"name": "testvm10.vhd", "statuses": [{"code": "ProvisioningState/succeeded", "displayStatus": "Provisioning succeeded", "level": "Info", "time": "2016-03-30T07:11:16.187272Z"}]}], "statuses": [{"code": "ProvisioningState/succeeded", "displayStatus": "Provisioning succeeded", "level": "Info", "time": "2016-03-30T20:33:38.946916Z"}, {"code": "PowerState/running", "displayStatus": "VM running", "level": "Info"}], "vmAgent": {"extensionHandlers": [], "statuses": [{"code": "ProvisioningState/succeeded", "displayStatus": "Ready", "level": "Info", "message": "GuestAgent is running and accepting new configurations.", "time": "2016-03-30T20:31:16.000Z"}], "vmAgentVersion": "WALinuxAgent-2.0.16"}}, "networkProfile": {"networkInterfaces": [{"id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/networkInterfaces/testvm10_NIC01", "name": "testvm10_NIC01", "properties": {"dnsSettings": {"appliedDnsServers": [], "dnsServers": []}, "enableIPForwarding": false, "ipConfigurations": [{"etag": "W/\"041c8c2a-d5dd-4cd7-8465-9125cfbe2cf8\"", "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/networkInterfaces/testvm10_NIC01/ipConfigurations/default", "name": "default", "properties": {"privateIPAddress": "10.10.0.5", "privateIPAllocationMethod": "Dynamic", "provisioningState": "Succeeded", "publicIPAddress": {"id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/publicIPAddresses/testvm10_PIP01", "name": "testvm10_PIP01", "properties": {"idleTimeoutInMinutes": 4, "ipAddress": "13.92.246.197", "ipConfiguration": {"id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/networkInterfaces/testvm10_NIC01/ipConfigurations/default"}, "provisioningState": "Succeeded", "publicIPAllocationMethod": "Static", "resourceGuid": "3447d987-ca0d-4eca-818b-5dddc0625b42"}}}}], "macAddress": "00-0D-3A-12-AA-14", "primary": true, "provisioningState": "Succeeded", "resourceGuid": "10979e12-ccf9-42ee-9f6d-ff2cc63b3844", "virtualMachine": {"id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Compute/virtualMachines/testvm10"}}}]}, "osProfile": {"adminUsername": "chouseknecht", "computerName": "test10", "linuxConfiguration": {"disablePasswordAuthentication": false}, "secrets": []}, "provisioningState": "Succeeded", "proximityPlacementGroup": {"id": "/subscriptions/xxx/resourceGroups/xxx/providers/Microsoft.Compute/proximityPlacementGroups/testid13"}, "storageProfile": {"dataDisks": [{"caching": "ReadWrite", "createOption": "empty", "diskSizeGB": 64, "lun": 0, "name": "datadisk1.vhd", "vhd": {"uri": "https://testvm10sa1.blob.core.windows.net/datadisk/datadisk1.vhd"}}], "imageReference": {"offer": "CentOS", "publisher": "OpenLogic", "sku": "7.1", "version": "7.1.20160308"}, "osDisk": {"caching": "ReadOnly", "createOption": "fromImage", "name": "testvm10.vhd", "osType": "Linux", "vhd": {"uri": "https://testvm10sa1.blob.core.windows.net/vhds/testvm10.vhd"}}}}, "type": "Microsoft.Compute/virtualMachines"}` |
| **deleted_network_interfaces**  list / elements=string | List of deleted NICs.  Returned: on delete  Sample: `["testvm1001"]` |
| **deleted_public_ips**  list / elements=string | List of deleted public IP address names.  Returned: on delete  Sample: `["testvm1001"]` |
| **deleted_vhd_uris**  list / elements=string | List of deleted Virtual Hard Disk URIs.  Returned: on delete  Sample: `["https://testvm104519.blob.core.windows.net/vhds/testvm10.vhd"]` |
| **powerstate**  string | Indicates if the state is `running`, `stopped`, `deallocated`, `generalized`.  Returned: always  Sample: `"running"` |

### Authors

- Chris Houseknecht (@chouseknecht)
- Matt Davis (@nitzmahone)
- Christopher Perrin (@cperrin88)
- James E. King III (@jeking3)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
