---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_virtualmachinescaleset module – Manage Azure virtual machine scale sets"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_virtualmachinescaleset_module.html
fetched_at: 2026-07-28T01:15:12+00:00
---
# azure.azcollection.azure_rm_virtualmachinescaleset module – Manage Azure virtual machine scale sets

> **Note:**
>
> This module is part of the [azure.azcollection collection](https://galaxy.ansible.com/ui/repo/published/azure/azcollection/) (version 1.19.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install azure.azcollection`.
> You need further requirements to be able to use this module,
> see [Requirements](azure_rm_virtualmachinescaleset_module.md#ansible-collections-azure-azcollection-azure-rm-virtualmachinescaleset-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_virtualmachinescaleset`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_virtualmachinescaleset_module.md#synopsis)
- [Requirements](azure_rm_virtualmachinescaleset_module.md#requirements)
- [Parameters](azure_rm_virtualmachinescaleset_module.md#parameters)
- [Notes](azure_rm_virtualmachinescaleset_module.md#notes)
- [See Also](azure_rm_virtualmachinescaleset_module.md#see-also)
- [Examples](azure_rm_virtualmachinescaleset_module.md#examples)
- [Return Values](azure_rm_virtualmachinescaleset_module.md#return-values)

## [Synopsis](azure_rm_virtualmachinescaleset_module.md#id1)

- Create and update a virtual machine scale set.
- Note that this module was called azure.azcollection.azure_rm_virtualmachine_scaleset before Ansible 2.8. The usage did not change.

## [Requirements](azure_rm_virtualmachinescaleset_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_virtualmachinescaleset_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **admin_password**  string | Password for the admin username.  Not required if the os_type is Linux and SSH password authentication is disabled by setting *ssh_password_enabled=false*. |
| **admin_username**  string | Admin username used to access the host after it is created. Required when creating a VM. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **application_gateway**  string | Application gateway name. |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **capacity**  integer | Capacity of VMSS.  **Default:** `1` |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **custom_data**  string | Data which is made available to the virtual machine and used by e.g., `cloud-init`.  Many images in the marketplace are not cloud-init ready. Thus, data sent to *custom_data* would be ignored.  If the image you are attempting to use is not listed in <https://docs.microsoft.com/en-us/azure/virtual-machines/linux/using-cloud-init#cloud-init-overview>, follow these steps <https://docs.microsoft.com/en-us/azure/virtual-machines/linux/cloudinit-prepare-custom-image>. |
| **data_disks**  list / elements=dictionary | Describes list of data disks. |
| **caching**  string | Type of data disk caching.  **Choices:**   - `"ReadOnly"` ← (default) - `"ReadWrite"` |
| **disk_size_gb**  integer | The initial disk size in GB for blank data disks. |
| **lun**  string | The logical unit number for data disk.  **Default:** `"0"` |
| **managed_disk_type**  string | Managed data disk type.  **Choices:**   - `"Standard_LRS"` - `"Premium_LRS"` - `"StandardSSD_LRS"` - `"UltraSSD_LRS"` - `"Premium_ZRS"` - `"StandardSSD_ZRS"` |
| **enable_accelerated_networking**  boolean | Indicates whether user wants to allow accelerated networking for virtual machines in scaleset being created.  **Choices:**   - `false` - `true` |
| **ephemeral_os_disk**  boolean | Parameters of ephemeral disk settings that can be specified for operating system disk.  Ephemeral OS disk is only supported for VMS Instances using Managed Disk.  **Choices:**   - `false` - `true` |
| **eviction_policy**  string | Specifies the eviction policy for the Azure Spot virtual machine.  Requires priority to be set to Spot.  **Choices:**   - `"Deallocate"` - `"Delete"` |
| **image**  any | Specifies the image used to build the VM.  If a string, the image is sourced from a custom image based on the name.  If a dict with the keys *publisher*, *offer*, *sku*, and *version*, the image is sourced from a Marketplace image. Note that set *version=latest* to get the most recent version of a given image.  If a dict with the keys *name* and *resource_group*, the image is sourced from a custom image based on the *name* and *resource_group* set. Note that the key *resource_group* is optional and if omitted, all images in the subscription will be searched for by *name*.  Custom image support was added in Ansible 2.5.  Required when creating. |
| **load_balancer**  string | Load balancer name. |
| **location**  string | Valid Azure location. Defaults to location of the resource group. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **managed_disk_type**  string | Managed disk type.  **Choices:**   - `"Standard_LRS"` - `"Premium_LRS"` - `"StandardSSD_LRS"` - `"UltraSSD_LRS"` - `"Premium_ZRS"` - `"StandardSSD_ZRS"` |
| **max_price**  float | Specifies the maximum price you are willing to pay for a Azure Spot VM/VMSS.  This price is in US Dollars.  `-1` indicates default price to be up-to on-demand.  Requires priority to be set to Spot.  **Default:** `-1.0` |
| **name**  string / required | Name of the virtual machine. |
| **orchestration_mode**  string | Specifies the orchestration mode for the virtual machine scale set.  When *orchestration_mode=Flexible*, *public_ip_per_vm=True* must be set.  When *orchestration_mode=Flexible*, *platform_fault_domain_count* must be set.  When *orchestration_mode=Flexible*, *single_placement_group=False* must be set.  When *orchestration_mode=Flexible*, it cannot be configured *overprovision*.  When *orchestration_mode=Flexible*, it cannot be configured *upgrade_policy* and configured when *orchestration_mode=Uniform*.  **Choices:**   - `"Flexible"` - `"Uniform"` |
| **os_disk_caching**  aliases: disk_caching  string | Type of OS disk caching.  **Choices:**   - `"ReadOnly"` ← (default) - `"ReadWrite"` |
| **os_disk_size_gb**  integer | Specifies the size of the operating system disk in gigabytes.  This can be used to overwrite the size of the disk in a virtual machine image. |
| **os_type**  string | Base type of operating system.  **Choices:**   - `"Windows"` - `"Linux"` ← (default) |
| **overprovision**  boolean | Specifies whether the Virtual Machine Scale Set should be overprovisioned.  **Choices:**   - `false` - `true` |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **plan**  dictionary | Third-party billing plan for the VM. |
| **name**  string / required | Billing plan name. |
| **product**  string / required | Product name. |
| **promotion_code**  string | Optional promotion code. |
| **publisher**  string / required | Publisher offering the plan. |
| **platform_fault_domain_count**  integer | Fault Domain count for each placement group.  **Default:** `1` |
| **priority**  string | Priority of the VMSS.  `None` is the equivalent of Regular VM.  **Choices:**   - `"None"` - `"Spot"` |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **public_ip_per_vm**  boolean | Assign a public IP to each virtual machine of the scale set  **Choices:**   - `false` ← (default) - `true` |
| **remove_on_absent**  list / elements=string | When removing a VM using *state=absent*, also remove associated resources.  It can be `all` or a list with any of the following [‘network_interfaces’, ‘virtual_storage’, ‘public_ips’].  Any other input will be ignored.  **Default:** `["all"]` |
| **resource_group**  string / required | Name of the resource group containing the virtual machine scale set. |
| **scale_in_policy**  string | define the order in which vmss instances are scaled-in  **Choices:**   - `"Default"` - `"NewestVM"` - `"OldestVM"` |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **security_group**  aliases: security_group_name  any | Existing security group with which to associate the subnet.  It can be the security group name which is in the same resource group.  It can be the resource ID.  It can be a dict which contains *name* and *resource_group* of the security group. |
| **security_profile**  dictionary | Specifies the Security related profile settings for the virtual machine sclaset. |
| **encryption_at_host**  boolean | This property can be used by user in the request to enable or disable the Host Encryption for the virtual machine sclaset.  This will enable the encryption for all the disks including Resource/Temp disk at host itself.  **Choices:**   - `false` - `true` |
| **security_type**  string | Specifies the SecurityType of the virtual machine sclaset.  It is set as TrustedLaunch to enable UefiSettings.  **Choices:**   - `"TrustedLaunch"` |
| **uefi_settings**  dictionary | Specifies the security settings like secure boot and vTPM used while creating the virtual machine scalset. |
| **secure_boot_enabled**  boolean | Specifies whether secure boot should be enabled on the virtual machine sclaset.  **Choices:**   - `false` - `true` |
| **v_tpm_enabled**  boolean | Specifies whether vTPM should be enabled on the virtual machine scalset.  **Choices:**   - `false` - `true` |
| **short_hostname**  string | Short host name. |
| **single_placement_group**  boolean | When true this limits the scale set to a single placement group, of max size 100 virtual machines.  **Choices:**   - `false` ← (default) - `true` |
| **ssh_password_enabled**  boolean | When the os_type is Linux, setting *ssh_password_enabled=false* will disable SSH password authentication and require use of SSH keys.  **Choices:**   - `false` - `true` ← (default) |
| **ssh_public_keys**  list / elements=dictionary | For *os_type=Linux* provide a list of SSH keys.  Each item in the list should be a dictionary where the dictionary contains two keys, `path` and `key_data`.  Set the `path` to the default location of the authorized_keys files.  On an Enterprise Linux host, for example, the *path=/home/<admin username>/.ssh/authorized_keys*. Set `key_data` to the actual value of the public key. |
| **state**  string | Assert the state of the virtual machine scale set.  State `present` will check that the machine exists with the requested configuration. If the configuration of the existing machine does not match, the machine will be updated.  State `absent` will remove the virtual machine scale set.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subnet_name**  aliases: subnet  string | Subnet name. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **terminate_event_timeout_minutes**  integer | timeout time for termination notification event  in range between 5 and 15 |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **tier**  string | SKU Tier.  **Choices:**   - `"Basic"` - `"Standard"` |
| **upgrade_policy**  string | Upgrade policy.  Required when creating the Azure virtual machine scale sets.  **Choices:**   - `"Manual"` - `"Automatic"` |
| **virtual_network_name**  aliases: virtual_network  string | Virtual Network name. |
| **virtual_network_resource_group**  string | When creating a virtual machine, if a specific virtual network from another resource group should be used.  Use this parameter to specify the resource group to use. |
| **vm_size**  string | A valid Azure VM size value. For example, `Standard_D4`.  The list of choices varies depending on the subscription and location. Check your subscription for available choices. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |
| **zones**  list / elements=string | A list of Availability Zones for your virtual machine scale set. |

## [Notes](azure_rm_virtualmachinescaleset_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_virtualmachinescaleset_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_virtualmachinescaleset_module.md#id6)

```yaml+jinja
- name: Create VMSS
  azure_rm_virtualmachinescaleset:
    resource_group: myResourceGroup
    name: testvmss
    vm_size: Standard_DS1_v2
    capacity: 2
    virtual_network_name: testvnet
    upgrade_policy: Manual
    subnet_name: testsubnet
    terminate_event_timeout_minutes: 10
    scale_in_policy: NewestVM
    admin_username: "{{ username }}"
    ssh_password_enabled: false
    ssh_public_keys:
      - path: /home/adminUser/.ssh/authorized_keys
        key_data: < insert your ssh public key here... >
    managed_disk_type: Standard_LRS
    image:
      offer: 0001-com-ubuntu-server-focal
      publisher: canonical
      sku: 20_04-lts-gen2
      version: latest
    data_disks:
      - lun: 0
        disk_size_gb: 64
        caching: ReadWrite
        managed_disk_type: Standard_LRS

- name: Create VMSS with an image that requires plan information
  azure_rm_virtualmachinescaleset:
    resource_group: myResourceGroup
    name: testvmss
    vm_size: Standard_DS1_v2
    capacity: 3
    virtual_network_name: testvnet
    upgrade_policy: Manual
    subnet_name: testsubnet
    admin_username: "{{ username }}"
    ssh_password_enabled: false
    ssh_public_keys:
      - path: /home/adminUser/.ssh/authorized_keys
        key_data: < insert your ssh public key here... >
    managed_disk_type: Standard_LRS
    image:
      offer: cis-ubuntu-linux-1804-l1
      publisher: center-for-internet-security-inc
      sku: Stable
      version: latest
    plan:
      name: cis-ubuntu-linux-1804-l1
      product: cis-ubuntu-linux-1804-l1
      publisher: center-for-internet-security-inc
    data_disks:
      - lun: 0
        disk_size_gb: 64
        caching: ReadWrite
        managed_disk_type: Standard_LRS

- name: Create a VMSS with a custom image
  azure_rm_virtualmachinescaleset:
    resource_group: myResourceGroup
    name: testvmss
    vm_size: Standard_DS1_v2
    capacity: 2
    virtual_network_name: testvnet
    upgrade_policy: Manual
    subnet_name: testsubnet
    admin_username: "{{ username }}"
    admin_password: "{{ password }}"
    managed_disk_type: Standard_LRS
    image: customimage001

- name: Create a VMSS with over 100 instances
  azure_rm_virtualmachinescaleset:
    resource_group: myResourceGroup
    name: testvmss
    vm_size: Standard_DS1_v2
    capacity: 120
    single_placement_group: false
    virtual_network_name: testvnet
    upgrade_policy: Manual
    subnet_name: testsubnet
    admin_username: "{{ username }}"
    admin_password: "{{ password }}"
    managed_disk_type: Standard_LRS
    image: customimage001

- name: Create a VMSS with a custom image from a particular resource group
  azure_rm_virtualmachinescaleset:
    resource_group: myResourceGroup
    name: testvmss
    vm_size: Standard_DS1_v2
    capacity: 2
    virtual_network_name: testvnet
    upgrade_policy: Manual
    subnet_name: testsubnet
    admin_username: "{{ username }}"
    admin_password: "{{ password }}"
    managed_disk_type: Standard_LRS
    image:
      name: customimage001
      resource_group: myResourceGroup

- name: Create a VMSS with Spot Instance
  azure_rm_virtualmachinescaleset:
    resource_group: myResourceGroup
    name: testvmss
    vm_size: Standard_DS1_v2
    capacity: 5
    priority: Spot
    eviction_policy: Deallocate
    virtual_network_name: testvnet
    upgrade_policy: Manual
    subnet_name: testsubnet
    admin_username: "{{ username }}"
    admin_password: "{{ password }}"
    managed_disk_type: Standard_LRS
    image: customimage001

- name: Create VMSS with security group
  azure_rm_virtualmachinescaleset:
    resource_group: "{{ resource_group }}"
    name: testVMSS{{ rpfx }}
    vm_size: Standard_D4s_v3
    admin_username: testuser
    single_placement_group: false
    platform_fault_domain_count: 1
    public_ip_per_vm: true
    ssh_password_enabled: false
    ssh_public_keys:
      - path: /home/testuser/.ssh/authorized_keys
        key_data: "ssh-rsa ****"
    virtual_network_name: VMSStestVnet
    subnet_name: VMSStestSubnet
    managed_disk_type: Standard_LRS
    orchestration_mode: Flexible
    os_disk_caching: ReadWrite
    security_profile:
      uefi_settings:
        secure_boot_enabled: true
        v_tpm_enabled: false
      encryption_at_host: false
      security_type: TrustedLaunch
    image:
      offer: 0001-com-ubuntu-server-jammy
      publisher: Canonical
      sku: 22_04-lts-gen2
      version: latest
    data_disks:
      - lun: 0
        disk_size_gb: 64
        caching: ReadWrite
        managed_disk_type: Standard_LRS
```

## [Return Values](azure_rm_virtualmachinescaleset_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **azure_vmss**  dictionary | Facts about the current state of the object.  Note that facts are not part of the registered output but available directly.  **Returned:** always  **Sample:** `{"properties": {"orchestrationMode": "Flexible", "overprovision": true, "platformFaultDomainCount": 1, "scaleInPolicy": {"rules": ["NewestVM"]}, "singlePlacementGroup": true, "upgradePolicy": {"mode": "Manual"}, "virtualMachineProfile": {"networkProfile": {"networkInterfaceConfigurations": [{"name": "testvmss", "properties": {"dnsSettings": {"dnsServers": []}, "enableAcceleratedNetworking": false, "ipConfigurations": [{"name": "default", "properties": {"privateIPAddressVersion": "IPv4", "subnet": {"id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/virtualNetworks/testvnet/subnets/testsubnet"}}}], "primary": true}}]}, "osProfile": {"adminUsername": "testuser", "computerNamePrefix": "testvmss", "linuxConfiguration": {"disablePasswordAuthentication": true, "ssh": {"publicKeys": [{"keyData": "", "path": "/home/testuser/.ssh/authorized_keys"}]}}, "secrets": []}, "scheduledEventsProfile": {"terminateNotificationProfile": {"enable": true, "notBeforeTimeout": "PT10M"}}, "storageProfile": {"dataDisks": [{"caching": "ReadWrite", "createOption": "empty", "diskSizeGB": 64, "lun": 0, "managedDisk": {"storageAccountType": "Standard_LRS"}}], "imageReference": {"offer": "0001-com-ubuntu-server-focal", "publisher": "canonical", "sku": "20_04-lts-gen2", "version": "20.04.202111210"}, "osDisk": {"caching": "ReadWrite", "createOption": "fromImage", "managedDisk": {"storageAccountType": "Standard_LRS"}}, "securityProfile": {"encryptionAtHost": false, "securityType": "TrustedLaunch", "uefiSettings": {"secureBootEnabled": true, "vTpmEnabled": false}}}}}, "sku": {"capacity": 2, "name": "Standard_DS1_v2", "tier": "Standard"}, "tags": null, "type": "Microsoft.Compute/virtualMachineScaleSets"}` |

### Authors

- Sertac Ozercan (@sozercan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
