---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_instance_info module – Gather info for GCP Instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_instance_info_module.html
fetched_at: 2026-07-28T02:32:16+00:00
---
# google.cloud.gcp_compute_instance_info module – Gather info for GCP Instance

> **Note:**
>
> This module is part of the [google.cloud collection](https://galaxy.ansible.com/ui/repo/published/google/cloud/) (version 1.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install google.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](gcp_compute_instance_info_module.md#ansible-collections-google-cloud-gcp-compute-instance-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_instance_info`.

- [Synopsis](gcp_compute_instance_info_module.md#synopsis)
- [Requirements](gcp_compute_instance_info_module.md#requirements)
- [Parameters](gcp_compute_instance_info_module.md#parameters)
- [Notes](gcp_compute_instance_info_module.md#notes)
- [Examples](gcp_compute_instance_info_module.md#examples)
- [Return Values](gcp_compute_instance_info_module.md#return-values)

## [Synopsis](gcp_compute_instance_info_module.md#id1)

- Gather info for GCP Instance

## [Requirements](gcp_compute_instance_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_instance_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **filters**  list / elements=string | A list of filter value pairs. Available filters are listed here <https://cloud.google.com/compute/docs/reference/rest/v1/instances/list>  Each additional filter in the list will act be added as an AND condition (filter1 and filter2) . |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **zone**  string / required | A reference to the zone where the machine resides. |

## [Notes](gcp_compute_instance_info_module.md#id4)

> **Note:**
>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_instance_info_module.md#id5)

```yaml+jinja
- name: get info on an instance
  gcp_compute_instance_info:
    zone: us-central1-a
    filters:
    - name = test_object
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_compute_instance_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  **Returned:** always |
| **canIpForward**  boolean | Allows this instance to send and receive packets with non-matching destination or source IPs. This is required if you plan to use this instance to forward routes.  **Returned:** success |
| **confidentialInstanceConfig**  complex | Configuration for confidential computing (requires setting the machine type to any of the n2d-\* types and a boot disk of type pd-ssd).  **Returned:** success |
| **enableConfidentialCompute**  boolean | Enables confidential computing.  **Returned:** success |
| **cpuPlatform**  string | The CPU platform used by this instance.  **Returned:** success |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  **Returned:** success |
| **deletionProtection**  boolean | Whether the resource should be protected against deletion.  **Returned:** success |
| **disks**  complex | An array of disks that are associated with the instances that are created from this template.  **Returned:** success |
| **autoDelete**  boolean | Specifies whether the disk will be auto-deleted when the instance is deleted (but not when the disk is detached from the instance).  Tip: Disks should be set to autoDelete=true so that leftover disks are not left behind on machine deletion.  **Returned:** success |
| **boot**  boolean | Indicates that this is a boot disk. The virtual machine will use the first partition of the disk for its root filesystem.  **Returned:** success |
| **deviceName**  string | Specifies a unique device name of your choice that is reflected into the /dev/disk/by-id/google-\* tree of a Linux operating system running within the instance. This name can be used to reference the device for mounting, resizing, and so on, from within the instance.  **Returned:** success |
| **diskEncryptionKey**  complex | Encrypts or decrypts a disk using a customer-supplied encryption key.  **Returned:** success |
| **rawKey**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.  **Returned:** success |
| **rsaEncryptedKey**  string | Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit customer-supplied encryption key to either encrypt or decrypt this resource.  **Returned:** success |
| **sha256**  string | The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key that protects this resource.  **Returned:** success |
| **index**  integer | Assigns a zero-based index to this disk, where 0 is reserved for the boot disk. For example, if you have many disks attached to an instance, each disk would have a unique index number. If not specified, the server will choose an appropriate value.  **Returned:** success |
| **initializeParams**  complex | Specifies the parameters for a new disk that will be created alongside the new instance. Use initialization parameters to create boot disks or local SSDs attached to the new instance.  **Returned:** success |
| **diskName**  string | Specifies the disk name. If not specified, the default is to use the name of the instance.  **Returned:** success |
| **diskSizeGb**  integer | Specifies the size of the disk in base-2 GB.  **Returned:** success |
| **diskType**  string | Reference to a disk type.  Specifies the disk type to use to create the instance.  If not specified, the default is pd-standard.  **Returned:** success |
| **sourceImage**  string | The source image to create this disk. When creating a new instance, one of initializeParams.sourceImage or disks.source is required. To create a disk with one of the public operating system images, specify the image by its family name.  **Returned:** success |
| **sourceImageEncryptionKey**  complex | The customer-supplied encryption key of the source image. Required if the source image is protected by a customer-supplied encryption key.  Instance templates do not store customer-supplied encryption keys, so you cannot create disks for instances in a managed instance group if the source images are encrypted with your own keys.  **Returned:** success |
| **rawKey**  string | Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.  **Returned:** success |
| **sha256**  string | The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key that protects this resource.  **Returned:** success |
| **interface**  string | Specifies the disk interface to use for attaching this disk, which is either SCSI or NVME. The default is SCSI.  Persistent disks must always use SCSI and the request will fail if you attempt to attach a persistent disk in any other format than SCSI.  **Returned:** success |
| **mode**  string | The mode in which to attach this disk, either READ_WRITE or READ_ONLY. If not specified, the default is to attach the disk in READ_WRITE mode.  **Returned:** success |
| **source**  dictionary | Reference to a disk. When creating a new instance, one of initializeParams.sourceImage or disks.source is required.  If desired, you can also attach existing non-root persistent disks using this property. This field is only applicable for persistent disks.  **Returned:** success |
| **type**  string | Specifies the type of the disk, either SCRATCH or PERSISTENT. If not specified, the default is PERSISTENT.  **Returned:** success |
| **guestAccelerators**  complex | List of the type and count of accelerator cards attached to the instance .  **Returned:** success |
| **acceleratorCount**  integer | The number of the guest accelerator cards exposed to this instance.  **Returned:** success |
| **acceleratorType**  string | Full or partial URL of the accelerator type resource to expose to this instance.  **Returned:** success |
| **hostname**  string | The hostname of the instance to be created. The specified hostname must be RFC1035 compliant. If hostname is not specified, the default hostname is [INSTANCE_NAME].c.[PROJECT_ID].internal when using the global DNS, and [INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal when using zonal DNS.  **Returned:** success |
| **id**  integer | The unique identifier for the resource. This identifier is defined by the server.  **Returned:** success |
| **labelFingerprint**  string | The fingerprint used for optimistic locking of this resource. Used internally during updates.  **Returned:** success |
| **labels**  dictionary | Labels to apply to this instance. A list of key->value pairs.  **Returned:** success |
| **machineType**  string | A reference to a machine type which defines VM kind.  **Returned:** success |
| **metadata**  dictionary | The metadata key/value pairs to assign to instances that are created from this template. These pairs can consist of custom metadata or predefined keys.  **Returned:** success |
| **minCpuPlatform**  string | Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms .  **Returned:** success |
| **name**  string | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |
| **networkInterfaces**  complex | An array of configurations for this interface. This specifies how this interface is configured to interact with other network services, such as connecting to the internet. Only one network interface is supported per instance.  **Returned:** success |
| **accessConfigs**  complex | An array of configurations for this interface. Currently, only one access config, ONE_TO_ONE_NAT, is supported. If there are no accessConfigs specified, then this instance will have no external internet access.  **Returned:** success |
| **name**  string | The name of this access configuration. The default and recommended name is External NAT but you can use any arbitrary string you would like. For example, My external IP or Network Access.  **Returned:** success |
| **natIP**  dictionary | Reference to an address.  An external IP address associated with this instance.  Specify an unused static external IP address available to the project or leave this field undefined to use an IP from a shared ephemeral IP address pool. If you specify a static external IP address, it must live in the same region as the zone of the instance.  **Returned:** success |
| **networkTier**  string | This signifies the networking tier used for configuring this access configuration. If an AccessConfig is specified without a valid external IP address, an ephemeral IP will be created with this networkTier. If an AccessConfig with a valid external IP address is specified, it must match that of the networkTier associated with the Address resource owning that IP.  **Returned:** success |
| **publicPtrDomainName**  string | The DNS domain name for the public PTR record. You can set this field only if the setPublicPtr field is enabled.  **Returned:** success |
| **setPublicPtr**  boolean | Specifies whether a public DNS PTR record should be created to map the external IP address of the instance to a DNS domain name.  **Returned:** success |
| **type**  string | The type of configuration. The default and only option is ONE_TO_ONE_NAT.  **Returned:** success |
| **aliasIpRanges**  complex | An array of alias IP ranges for this network interface. Can only be specified for network interfaces on subnet-mode networks.  **Returned:** success |
| **ipCidrRange**  string | The IP CIDR range represented by this alias IP range.  This IP CIDR range must belong to the specified subnetwork and cannot contain IP addresses reserved by system or used by other network interfaces. This range may be a single IP address (e.g. 10.2.3.4), a netmask (e.g. /24) or a CIDR format string (e.g. 10.1.2.0/24).  **Returned:** success |
| **subnetworkRangeName**  string | Optional subnetwork secondary range name specifying the secondary range from which to allocate the IP CIDR range for this alias IP range. If left unspecified, the primary range of the subnetwork will be used.  **Returned:** success |
| **name**  string | The name of the network interface, generated by the server. For network devices, these are eth0, eth1, etc .  **Returned:** success |
| **network**  dictionary | Specifies the title of an existing network. Not setting the network title will select the default network interface, which could have SSH already configured .  **Returned:** success |
| **networkIP**  string | An IPv4 internal network address to assign to the instance for this network interface. If not specified by the user, an unused internal IP is assigned by the system.  **Returned:** success |
| **subnetwork**  dictionary | Reference to a VPC network.  If the network resource is in legacy mode, do not provide this property. If the network is in auto subnet mode, providing the subnetwork is optional. If the network is in custom subnet mode, then this field should be specified.  **Returned:** success |
| **scheduling**  complex | Sets the scheduling options for this instance.  **Returned:** success |
| **automaticRestart**  boolean | Specifies whether the instance should be automatically restarted if it is terminated by Compute Engine (not terminated by a user).  You can only set the automatic restart option for standard instances. Preemptible instances cannot be automatically restarted.  **Returned:** success |
| **onHostMaintenance**  string | Defines the maintenance behavior for this instance. For standard instances, the default behavior is MIGRATE. For preemptible instances, the default and only possible behavior is TERMINATE.  For more information, see Setting Instance Scheduling Options.  **Returned:** success |
| **preemptible**  boolean | Defines whether the instance is preemptible. This can only be set during instance creation, it cannot be set or changed after the instance has been created.  **Returned:** success |
| **serviceAccounts**  complex | A list of service accounts, with their specified scopes, authorized for this instance. Only one service account per VM instance is supported.  **Returned:** success |
| **email**  string | Email address of the service account.  **Returned:** success |
| **scopes**  list / elements=string | The list of scopes to be made available for this service account.  **Returned:** success |
| **shieldedInstanceConfig**  complex | Configuration for various parameters related to shielded instances.  **Returned:** success |
| **enableIntegrityMonitoring**  boolean | Defines whether the instance has integrity monitoring enabled.  **Returned:** success |
| **enableSecureBoot**  boolean | Defines whether the instance has Secure Boot enabled.  **Returned:** success |
| **enableVtpm**  boolean | Defines whether the instance has the vTPM enabled.  **Returned:** success |
| **status**  string | The status of the instance. One of the following values: PROVISIONING, STAGING, RUNNING, STOPPING, SUSPENDING, SUSPENDED, and TERMINATED.  As a user, use RUNNING to keep a machine “on” and TERMINATED to turn a machine off .  **Returned:** success |
| **statusMessage**  string | An optional, human-readable explanation of the status.  **Returned:** success |
| **tags**  complex | A list of tags to apply to this instance. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during instance creation. The tags can be later modified by the setTags method. Each tag within the list must comply with RFC1035.  **Returned:** success |
| **fingerprint**  string | Specifies a fingerprint for this request, which is essentially a hash of the metadata’s contents and used for optimistic locking.  The fingerprint is initially generated by Compute Engine and changes after every request to modify or update metadata. You must always provide an up-to-date fingerprint hash in order to update or change metadata.  **Returned:** success |
| **items**  list / elements=string | An array of tags. Each tag must be 1-63 characters long, and comply with RFC1035.  **Returned:** success |
| **zone**  string | A reference to the zone where the machine resides.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
