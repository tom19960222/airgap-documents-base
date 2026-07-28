---
collection: ansible
version: "6"
title: "google.cloud.gcp_compute_instance module – Creates a GCP Instance"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_compute_instance_module.html
fetched_at: 2026-07-27T17:48:06+00:00
---
# google.cloud.gcp_compute_instance module – Creates a GCP Instance

> **Note:**
>
> This module is part of the [google.cloud collection](https://galaxy.ansible.com/google/cloud) (version 1.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install google.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](gcp_compute_instance_module.md#ansible-collections-google-cloud-gcp-compute-instance-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_instance`.

- [Synopsis](gcp_compute_instance_module.md#synopsis)
- [Requirements](gcp_compute_instance_module.md#requirements)
- [Parameters](gcp_compute_instance_module.md#parameters)
- [Examples](gcp_compute_instance_module.md#examples)
- [Return Values](gcp_compute_instance_module.md#return-values)

## [Synopsis](gcp_compute_instance_module.md#id1)

- An instance is a virtual machine (VM) hosted on Google’s infrastructure.

## [Requirements](gcp_compute_instance_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_instance_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **can_ip_forward**  aliases: ip_forward  boolean | Allows this instance to send and receive packets with non-matching destination or source IPs. This is required if you plan to use this instance to forward routes.  Choices:   - `false` - `true` |
| **deletion_protection**  boolean | Whether the resource should be protected against deletion.  Choices:   - `false` - `true` |
| **disks**  list / elements=dictionary | An array of disks that are associated with the instances that are created from this template. |
| **auto_delete**  boolean | Specifies whether the disk will be auto-deleted when the instance is deleted (but not when the disk is detached from the instance).  Tip: Disks should be set to autoDelete=true so that leftover disks are not left behind on machine deletion.  Choices:   - `false` - `true` |
| **boot**  boolean | Indicates that this is a boot disk. The virtual machine will use the first partition of the disk for its root filesystem.  Choices:   - `false` - `true` |
| **device_name**  string | Specifies a unique device name of your choice that is reflected into the /dev/disk/by-id/google-\* tree of a Linux operating system running within the instance. This name can be used to reference the device for mounting, resizing, and so on, from within the instance. |
| **disk_encryption_key**  dictionary | Encrypts or decrypts a disk using a customer-supplied encryption key. |
| **raw_key**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource. |
| **rsa_encrypted_key**  string | Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit customer-supplied encryption key to either encrypt or decrypt this resource. |
| **index**  integer | Assigns a zero-based index to this disk, where 0 is reserved for the boot disk. For example, if you have many disks attached to an instance, each disk would have a unique index number. If not specified, the server will choose an appropriate value. |
| **initialize_params**  dictionary | Specifies the parameters for a new disk that will be created alongside the new instance. Use initialization parameters to create boot disks or local SSDs attached to the new instance. |
| **disk_name**  string | Specifies the disk name. If not specified, the default is to use the name of the instance. |
| **disk_size_gb**  integer | Specifies the size of the disk in base-2 GB. |
| **disk_type**  string | Reference to a disk type.  Specifies the disk type to use to create the instance.  If not specified, the default is pd-standard. |
| **source_image**  aliases: image, image_family  string | The source image to create this disk. When creating a new instance, one of initializeParams.sourceImage or disks.source is required. To create a disk with one of the public operating system images, specify the image by its family name. |
| **source_image_encryption_key**  dictionary | The customer-supplied encryption key of the source image. Required if the source image is protected by a customer-supplied encryption key.  Instance templates do not store customer-supplied encryption keys, so you cannot create disks for instances in a managed instance group if the source images are encrypted with your own keys. |
| **raw_key**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource. |
| **interface**  string | Specifies the disk interface to use for attaching this disk, which is either SCSI or NVME. The default is SCSI.  Persistent disks must always use SCSI and the request will fail if you attempt to attach a persistent disk in any other format than SCSI.  Some valid choices include: “SCSI”, “NVME” |
| **mode**  string | The mode in which to attach this disk, either READ_WRITE or READ_ONLY. If not specified, the default is to attach the disk in READ_WRITE mode.  Some valid choices include: “READ_WRITE”, “READ_ONLY” |
| **source**  dictionary | Reference to a disk. When creating a new instance, one of initializeParams.sourceImage or disks.source is required.  If desired, you can also attach existing non-root persistent disks using this property. This field is only applicable for persistent disks.  This field represents a link to a Disk resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_disk task and then set this source field to “{{ name-of-resource }}” |
| **type**  string | Specifies the type of the disk, either SCRATCH or PERSISTENT. If not specified, the default is PERSISTENT.  Some valid choices include: “SCRATCH”, “PERSISTENT” |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **guest_accelerators**  list / elements=dictionary | List of the type and count of accelerator cards attached to the instance . |
| **accelerator_count**  integer | The number of the guest accelerator cards exposed to this instance. |
| **accelerator_type**  string | Full or partial URL of the accelerator type resource to expose to this instance. |
| **hostname**  string | The hostname of the instance to be created. The specified hostname must be RFC1035 compliant. If hostname is not specified, the default hostname is [INSTANCE_NAME].c.[PROJECT_ID].internal when using the global DNS, and [INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal when using zonal DNS. |
| **labels**  dictionary | Labels to apply to this instance. A list of key->value pairs. |
| **machine_type**  string | A reference to a machine type which defines VM kind. |
| **metadata**  dictionary | The metadata key/value pairs to assign to instances that are created from this template. These pairs can consist of custom metadata or predefined keys. |
| **min_cpu_platform**  string | Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms . |
| **name**  string | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **network_interfaces**  list / elements=dictionary | An array of configurations for this interface. This specifies how this interface is configured to interact with other network services, such as connecting to the internet. Only one network interface is supported per instance. |
| **access_configs**  list / elements=dictionary | An array of configurations for this interface. Currently, only one access config, ONE_TO_ONE_NAT, is supported. If there are no accessConfigs specified, then this instance will have no external internet access. |
| **name**  string / required | The name of this access configuration. The default and recommended name is External NAT but you can use any arbitrary string you would like. For example, My external IP or Network Access. |
| **nat_ip**  dictionary | Reference to an address.  An external IP address associated with this instance.  Specify an unused static external IP address available to the project or leave this field undefined to use an IP from a shared ephemeral IP address pool. If you specify a static external IP address, it must live in the same region as the zone of the instance.  This field represents a link to a Address resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘address’ and value of your resource’s address Alternatively, you can add `register: name-of-resource` to a gcp_compute_address task and then set this nat_ip field to “{{ name-of-resource }}” |
| **network_tier**  string | This signifies the networking tier used for configuring this access configuration. If an AccessConfig is specified without a valid external IP address, an ephemeral IP will be created with this networkTier. If an AccessConfig with a valid external IP address is specified, it must match that of the networkTier associated with the Address resource owning that IP.  Some valid choices include: “PREMIUM”, “STANDARD” |
| **public_ptr_domain_name**  string | The DNS domain name for the public PTR record. You can set this field only if the setPublicPtr field is enabled. |
| **set_public_ptr**  boolean | Specifies whether a public DNS PTR record should be created to map the external IP address of the instance to a DNS domain name.  Choices:   - `false` - `true` |
| **type**  string / required | The type of configuration. The default and only option is ONE_TO_ONE_NAT.  Some valid choices include: “ONE_TO_ONE_NAT” |
| **alias_ip_ranges**  list / elements=dictionary | An array of alias IP ranges for this network interface. Can only be specified for network interfaces on subnet-mode networks. |
| **ip_cidr_range**  string | The IP CIDR range represented by this alias IP range.  This IP CIDR range must belong to the specified subnetwork and cannot contain IP addresses reserved by system or used by other network interfaces. This range may be a single IP address (e.g. 10.2.3.4), a netmask (e.g. /24) or a CIDR format string (e.g. 10.1.2.0/24). |
| **subnetwork_range_name**  string | Optional subnetwork secondary range name specifying the secondary range from which to allocate the IP CIDR range for this alias IP range. If left unspecified, the primary range of the subnetwork will be used. |
| **network**  dictionary | Specifies the title of an existing network. Not setting the network title will select the default network interface, which could have SSH already configured .  This field represents a link to a Network resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_network task and then set this network field to “{{ name-of-resource }}” |
| **network_ip**  string | An IPv4 internal network address to assign to the instance for this network interface. If not specified by the user, an unused internal IP is assigned by the system. |
| **subnetwork**  dictionary | Reference to a VPC network.  If the network resource is in legacy mode, do not provide this property. If the network is in auto subnet mode, providing the subnetwork is optional. If the network is in custom subnet mode, then this field should be specified.  This field represents a link to a Subnetwork resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_subnetwork task and then set this subnetwork field to “{{ name-of-resource }}” |
| **project**  string | The Google Cloud Platform project to use. |
| **scheduling**  dictionary | Sets the scheduling options for this instance. |
| **automatic_restart**  boolean | Specifies whether the instance should be automatically restarted if it is terminated by Compute Engine (not terminated by a user).  You can only set the automatic restart option for standard instances. Preemptible instances cannot be automatically restarted.  Choices:   - `false` - `true` |
| **on_host_maintenance**  string | Defines the maintenance behavior for this instance. For standard instances, the default behavior is MIGRATE. For preemptible instances, the default and only possible behavior is TERMINATE.  For more information, see Setting Instance Scheduling Options. |
| **preemptible**  boolean | Defines whether the instance is preemptible. This can only be set during instance creation, it cannot be set or changed after the instance has been created.  Choices:   - `false` - `true` |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **service_accounts**  list / elements=dictionary | A list of service accounts, with their specified scopes, authorized for this instance. Only one service account per VM instance is supported. |
| **email**  string | Email address of the service account. |
| **scopes**  list / elements=string | The list of scopes to be made available for this service account. |
| **shielded_instance_config**  dictionary | Configuration for various parameters related to shielded instances. |
| **enable_integrity_monitoring**  boolean | Defines whether the instance has integrity monitoring enabled.  Choices:   - `false` - `true` |
| **enable_secure_boot**  boolean | Defines whether the instance has Secure Boot enabled.  Choices:   - `false` - `true` |
| **enable_vtpm**  boolean | Defines whether the instance has the vTPM enabled.  Choices:   - `false` - `true` |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |
| **status**  string | The status of the instance. One of the following values: PROVISIONING, STAGING, RUNNING, STOPPING, SUSPENDING, SUSPENDED, and TERMINATED.  As a user, use RUNNING to keep a machine “on” and TERMINATED to turn a machine off .  Some valid choices include: “PROVISIONING”, “STAGING”, “RUNNING”, “STOPPING”, “SUSPENDING”, “SUSPENDED”, “TERMINATED” |
| **tags**  dictionary | A list of tags to apply to this instance. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during instance creation. The tags can be later modified by the setTags method. Each tag within the list must comply with RFC1035. |
| **fingerprint**  string | Specifies a fingerprint for this request, which is essentially a hash of the metadata’s contents and used for optimistic locking.  The fingerprint is initially generated by Compute Engine and changes after every request to modify or update metadata. You must always provide an up-to-date fingerprint hash in order to update or change metadata. |
| **items**  list / elements=string | An array of tags. Each tag must be 1-63 characters long, and comply with RFC1035. |
| **zone**  string / required | A reference to the zone where the machine resides. |

## [Examples](gcp_compute_instance_module.md#id4)

```yaml+jinja
- name: create a disk
  google.cloud.gcp_compute_disk:
    name: disk-instance
    size_gb: 50
    source_image: projects/ubuntu-os-cloud/global/images/family/ubuntu-1604-lts
    zone: us-central1-a
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: disk

- name: create a network
  google.cloud.gcp_compute_network:
    name: network-instance
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: network

- name: create a address
  google.cloud.gcp_compute_address:
    name: address-instance
    region: us-central1
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: address

- name: create a instance
  google.cloud.gcp_compute_instance:
    name: test_object
    machine_type: n1-standard-1
    disks:
    - auto_delete: 'true'
      boot: 'true'
      source: "{{ disk }}"
    - auto_delete: 'true'
      interface: NVME
      type: SCRATCH
      initialize_params:
        disk_type: local-ssd
    metadata:
      startup-script-url: gs:://graphite-playground/bootstrap.sh
      cost-center: '12345'
    labels:
      environment: production
    network_interfaces:
    - network: "{{ network }}"
      access_configs:
      - name: External NAT
        nat_ip: "{{ address }}"
        type: ONE_TO_ONE_NAT
    zone: us-central1-a
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_instance_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **canIpForward**  boolean | Allows this instance to send and receive packets with non-matching destination or source IPs. This is required if you plan to use this instance to forward routes.  Returned: success |
| **cpuPlatform**  string | The CPU platform used by this instance.  Returned: success |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  Returned: success |
| **deletionProtection**  boolean | Whether the resource should be protected against deletion.  Returned: success |
| **disks**  complex | An array of disks that are associated with the instances that are created from this template.  Returned: success |
| **autoDelete**  boolean | Specifies whether the disk will be auto-deleted when the instance is deleted (but not when the disk is detached from the instance).  Tip: Disks should be set to autoDelete=true so that leftover disks are not left behind on machine deletion.  Returned: success |
| **boot**  boolean | Indicates that this is a boot disk. The virtual machine will use the first partition of the disk for its root filesystem.  Returned: success |
| **deviceName**  string | Specifies a unique device name of your choice that is reflected into the /dev/disk/by-id/google-\* tree of a Linux operating system running within the instance. This name can be used to reference the device for mounting, resizing, and so on, from within the instance.  Returned: success |
| **diskEncryptionKey**  complex | Encrypts or decrypts a disk using a customer-supplied encryption key.  Returned: success |
| **rawKey**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.  Returned: success |
| **rsaEncryptedKey**  string | Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit customer-supplied encryption key to either encrypt or decrypt this resource.  Returned: success |
| **sha256**  string | The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key that protects this resource.  Returned: success |
| **index**  integer | Assigns a zero-based index to this disk, where 0 is reserved for the boot disk. For example, if you have many disks attached to an instance, each disk would have a unique index number. If not specified, the server will choose an appropriate value.  Returned: success |
| **initializeParams**  complex | Specifies the parameters for a new disk that will be created alongside the new instance. Use initialization parameters to create boot disks or local SSDs attached to the new instance.  Returned: success |
| **diskName**  string | Specifies the disk name. If not specified, the default is to use the name of the instance.  Returned: success |
| **diskSizeGb**  integer | Specifies the size of the disk in base-2 GB.  Returned: success |
| **diskType**  string | Reference to a disk type.  Specifies the disk type to use to create the instance.  If not specified, the default is pd-standard.  Returned: success |
| **sourceImage**  string | The source image to create this disk. When creating a new instance, one of initializeParams.sourceImage or disks.source is required. To create a disk with one of the public operating system images, specify the image by its family name.  Returned: success |
| **sourceImageEncryptionKey**  complex | The customer-supplied encryption key of the source image. Required if the source image is protected by a customer-supplied encryption key.  Instance templates do not store customer-supplied encryption keys, so you cannot create disks for instances in a managed instance group if the source images are encrypted with your own keys.  Returned: success |
| **rawKey**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.  Returned: success |
| **sha256**  string | The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key that protects this resource.  Returned: success |
| **interface**  string | Specifies the disk interface to use for attaching this disk, which is either SCSI or NVME. The default is SCSI.  Persistent disks must always use SCSI and the request will fail if you attempt to attach a persistent disk in any other format than SCSI.  Returned: success |
| **mode**  string | The mode in which to attach this disk, either READ_WRITE or READ_ONLY. If not specified, the default is to attach the disk in READ_WRITE mode.  Returned: success |
| **source**  dictionary | Reference to a disk. When creating a new instance, one of initializeParams.sourceImage or disks.source is required.  If desired, you can also attach existing non-root persistent disks using this property. This field is only applicable for persistent disks.  Returned: success |
| **type**  string | Specifies the type of the disk, either SCRATCH or PERSISTENT. If not specified, the default is PERSISTENT.  Returned: success |
| **guestAccelerators**  complex | List of the type and count of accelerator cards attached to the instance .  Returned: success |
| **acceleratorCount**  integer | The number of the guest accelerator cards exposed to this instance.  Returned: success |
| **acceleratorType**  string | Full or partial URL of the accelerator type resource to expose to this instance.  Returned: success |
| **hostname**  string | The hostname of the instance to be created. The specified hostname must be RFC1035 compliant. If hostname is not specified, the default hostname is [INSTANCE_NAME].c.[PROJECT_ID].internal when using the global DNS, and [INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal when using zonal DNS.  Returned: success |
| **id**  integer | The unique identifier for the resource. This identifier is defined by the server.  Returned: success |
| **labelFingerprint**  string | The fingerprint used for optimistic locking of this resource. Used internally during updates.  Returned: success |
| **labels**  dictionary | Labels to apply to this instance. A list of key->value pairs.  Returned: success |
| **machineType**  string | A reference to a machine type which defines VM kind.  Returned: success |
| **metadata**  dictionary | The metadata key/value pairs to assign to instances that are created from this template. These pairs can consist of custom metadata or predefined keys.  Returned: success |
| **minCpuPlatform**  string | Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms .  Returned: success |
| **name**  string | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  Returned: success |
| **networkInterfaces**  complex | An array of configurations for this interface. This specifies how this interface is configured to interact with other network services, such as connecting to the internet. Only one network interface is supported per instance.  Returned: success |
| **accessConfigs**  complex | An array of configurations for this interface. Currently, only one access config, ONE_TO_ONE_NAT, is supported. If there are no accessConfigs specified, then this instance will have no external internet access.  Returned: success |
| **name**  string | The name of this access configuration. The default and recommended name is External NAT but you can use any arbitrary string you would like. For example, My external IP or Network Access.  Returned: success |
| **natIP**  dictionary | Reference to an address.  An external IP address associated with this instance.  Specify an unused static external IP address available to the project or leave this field undefined to use an IP from a shared ephemeral IP address pool. If you specify a static external IP address, it must live in the same region as the zone of the instance.  Returned: success |
| **networkTier**  string | This signifies the networking tier used for configuring this access configuration. If an AccessConfig is specified without a valid external IP address, an ephemeral IP will be created with this networkTier. If an AccessConfig with a valid external IP address is specified, it must match that of the networkTier associated with the Address resource owning that IP.  Returned: success |
| **publicPtrDomainName**  string | The DNS domain name for the public PTR record. You can set this field only if the setPublicPtr field is enabled.  Returned: success |
| **setPublicPtr**  boolean | Specifies whether a public DNS PTR record should be created to map the external IP address of the instance to a DNS domain name.  Returned: success |
| **type**  string | The type of configuration. The default and only option is ONE_TO_ONE_NAT.  Returned: success |
| **aliasIpRanges**  complex | An array of alias IP ranges for this network interface. Can only be specified for network interfaces on subnet-mode networks.  Returned: success |
| **ipCidrRange**  string | The IP CIDR range represented by this alias IP range.  This IP CIDR range must belong to the specified subnetwork and cannot contain IP addresses reserved by system or used by other network interfaces. This range may be a single IP address (e.g. 10.2.3.4), a netmask (e.g. /24) or a CIDR format string (e.g. 10.1.2.0/24).  Returned: success |
| **subnetworkRangeName**  string | Optional subnetwork secondary range name specifying the secondary range from which to allocate the IP CIDR range for this alias IP range. If left unspecified, the primary range of the subnetwork will be used.  Returned: success |
| **name**  string | The name of the network interface, generated by the server. For network devices, these are eth0, eth1, etc .  Returned: success |
| **network**  dictionary | Specifies the title of an existing network. Not setting the network title will select the default network interface, which could have SSH already configured .  Returned: success |
| **networkIP**  string | An IPv4 internal network address to assign to the instance for this network interface. If not specified by the user, an unused internal IP is assigned by the system.  Returned: success |
| **subnetwork**  dictionary | Reference to a VPC network.  If the network resource is in legacy mode, do not provide this property. If the network is in auto subnet mode, providing the subnetwork is optional. If the network is in custom subnet mode, then this field should be specified.  Returned: success |
| **scheduling**  complex | Sets the scheduling options for this instance.  Returned: success |
| **automaticRestart**  boolean | Specifies whether the instance should be automatically restarted if it is terminated by Compute Engine (not terminated by a user).  You can only set the automatic restart option for standard instances. Preemptible instances cannot be automatically restarted.  Returned: success |
| **onHostMaintenance**  string | Defines the maintenance behavior for this instance. For standard instances, the default behavior is MIGRATE. For preemptible instances, the default and only possible behavior is TERMINATE.  For more information, see Setting Instance Scheduling Options.  Returned: success |
| **preemptible**  boolean | Defines whether the instance is preemptible. This can only be set during instance creation, it cannot be set or changed after the instance has been created.  Returned: success |
| **serviceAccounts**  complex | A list of service accounts, with their specified scopes, authorized for this instance. Only one service account per VM instance is supported.  Returned: success |
| **email**  string | Email address of the service account.  Returned: success |
| **scopes**  list / elements=string | The list of scopes to be made available for this service account.  Returned: success |
| **shieldedInstanceConfig**  complex | Configuration for various parameters related to shielded instances.  Returned: success |
| **enableIntegrityMonitoring**  boolean | Defines whether the instance has integrity monitoring enabled.  Returned: success |
| **enableSecureBoot**  boolean | Defines whether the instance has Secure Boot enabled.  Returned: success |
| **enableVtpm**  boolean | Defines whether the instance has the vTPM enabled.  Returned: success |
| **status**  string | The status of the instance. One of the following values: PROVISIONING, STAGING, RUNNING, STOPPING, SUSPENDING, SUSPENDED, and TERMINATED.  As a user, use RUNNING to keep a machine “on” and TERMINATED to turn a machine off .  Returned: success |
| **statusMessage**  string | An optional, human-readable explanation of the status.  Returned: success |
| **tags**  complex | A list of tags to apply to this instance. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during instance creation. The tags can be later modified by the setTags method. Each tag within the list must comply with RFC1035.  Returned: success |
| **fingerprint**  string | Specifies a fingerprint for this request, which is essentially a hash of the metadata’s contents and used for optimistic locking.  The fingerprint is initially generated by Compute Engine and changes after every request to modify or update metadata. You must always provide an up-to-date fingerprint hash in order to update or change metadata.  Returned: success |
| **items**  list / elements=string | An array of tags. Each tag must be 1-63 characters long, and comply with RFC1035.  Returned: success |
| **zone**  string | A reference to the zone where the machine resides.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
