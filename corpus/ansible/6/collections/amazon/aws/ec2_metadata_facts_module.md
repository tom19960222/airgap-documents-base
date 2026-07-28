---
collection: ansible
version: "6"
title: "amazon.aws.ec2_metadata_facts module – gathers facts (instance metadata) about remote hosts within EC2"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/ec2_metadata_facts_module.html
fetched_at: 2026-07-27T16:43:45+00:00
---
# amazon.aws.ec2_metadata_facts module – gathers facts (instance metadata) about remote hosts within EC2

> **Note:**
>
> This module is part of the [amazon.aws collection](https://galaxy.ansible.com/amazon/aws) (version 3.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install amazon.aws`.
>
> To use it in a playbook, specify: `amazon.aws.ec2_metadata_facts`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_metadata_facts_module.md#synopsis)
- [Notes](ec2_metadata_facts_module.md#notes)
- [Examples](ec2_metadata_facts_module.md#examples)
- [Returned Facts](ec2_metadata_facts_module.md#returned-facts)

## [Synopsis](ec2_metadata_facts_module.md#id4)

- This module fetches data from the instance metadata endpoint in EC2 as per <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html>.
- The module must be called from within the EC2 instance itself.
- The module is configured to utilize the session oriented Instance Metadata Service v2 (IMDSv2) <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html>.
- If the HttpEndpoint parameter <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceMetadataOptions.html#API_ModifyInstanceMetadataOptions_RequestParameters> is set to disabled for the EC2 instance, the module will return an error while retrieving a session token.

## [Notes](ec2_metadata_facts_module.md#id5)

> **Note:**
>
> - Parameters to filter on ec2_metadata_facts may be added later.

## [Examples](ec2_metadata_facts_module.md#id6)

```yaml+jinja
# Gather EC2 metadata facts
- amazon.aws.ec2_metadata_facts:

- debug:
    msg: "This instance is a t1.micro"
  when: ansible_ec2_instance_type == "t1.micro"
```

## [Returned Facts](ec2_metadata_facts_module.md#id7)

Facts returned by this module are added/updated in the `hostvars` host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.

| Key | Description |
| --- | --- |
| **ansible_ec2_ami_id**  string | The AMI ID used to launch the instance.  Returned: success  Sample: `"ami-XXXXXXXX"` |
| **ansible_ec2_ami_launch_index**  string | If you started more than one instance at the same time, this value indicates the order in which the instance was launched.  The value of the first instance launched is 0.  Returned: success  Sample: `"0"` |
| **ansible_ec2_ami_manifest_path**  string | The path to the AMI manifest file in Amazon S3.  If you used an Amazon EBS-backed AMI to launch the instance, the returned result is unknown.  Returned: success  Sample: `"(unknown)"` |
| **ansible_ec2_ancestor_ami_ids**  string | The AMI IDs of any instances that were rebundled to create this AMI.  This value will only exist if the AMI manifest file contained an ancestor-amis key.  Returned: success  Sample: `"(unknown)"` |
| **ansible_ec2_block_device_mapping_ami**  string | The virtual device that contains the root/boot file system.  Returned: success  Sample: `"/dev/sda1"` |
| **ansible_ec2_block_device_mapping_ebsN**  string | The virtual devices associated with Amazon EBS volumes, if any are present.  Amazon EBS volumes are only available in metadata if they were present at launch time or when the instance was last started.  The N indicates the index of the Amazon EBS volume (such as ebs1 or ebs2).  Returned: success  Sample: `"/dev/xvdb"` |
| **ansible_ec2_block_device_mapping_ephemeralN**  string | The virtual devices associated with ephemeral devices, if any are present. The N indicates the index of the ephemeral volume.  Returned: success  Sample: `"/dev/xvdc"` |
| **ansible_ec2_block_device_mapping_root**  string | The virtual devices or partitions associated with the root devices, or partitions on the virtual device, where the root (/ or C) file system is associated with the given instance.  Returned: success  Sample: `"/dev/sda1"` |
| **ansible_ec2_block_device_mapping_swap**  string | The virtual devices associated with swap. Not always present.  Returned: success  Sample: `"/dev/sda2"` |
| **ansible_ec2_fws_instance_monitoring**  string | Value showing whether the customer has enabled detailed one-minute monitoring in CloudWatch.  Returned: success  Sample: `"enabled"` |
| **ansible_ec2_hostname**  string | The private IPv4 DNS hostname of the instance.  In cases where multiple network interfaces are present, this refers to the eth0 device (the device for which the device number is 0).  Returned: success  Sample: `"ip-10-0-0-1.ec2.internal"` |
| **ansible_ec2_iam_info**  complex | If there is an IAM role associated with the instance, contains information about the last time the instance profile was updated, including the instance’s LastUpdated date, InstanceProfileArn, and InstanceProfileId. Otherwise, not present.  Returned: success  Sample: `""` |
| **InstanceProfileArn**  string | The ARN of the InstanceProfile associated with the Instance.  Returned: success |
| **InstanceProfileId**  string | The Id of the InstanceProfile associated with the Instance.  Returned: success |
| **LastUpdated**  string | The last time which InstanceProfile is associated with the Instance changed.  Returned: success |
| **ansible_ec2_iam_info_instanceprofilearn**  string | The IAM instance profile ARN.  Returned: success  Sample: `"arn:aws:iam::<account id>:instance-profile/role_name"` |
| **ansible_ec2_iam_info_instanceprofileid**  string | IAM instance profile ID.  Returned: success  Sample: `""` |
| **ansible_ec2_iam_info_lastupdated**  string | IAM info last updated time.  Returned: success  Sample: `"2017-05-12T02:42:27Z"` |
| **ansible_ec2_iam_instance_profile_role**  string | IAM instance role.  Returned: success  Sample: `"role_name"` |
| **ansible_ec2_iam_security_credentials_role_name**  string | If there is an IAM role associated with the instance, role-name is the name of the role, and role-name contains the temporary security credentials associated with the role. Otherwise, not present.  Returned: success  Sample: `""` |
| **ansible_ec2_iam_security_credentials_role_name_accesskeyid**  string | IAM role access key ID.  Returned: success  Sample: `""` |
| **ansible_ec2_iam_security_credentials_role_name_code**  string | IAM code.  Returned: success  Sample: `"Success"` |
| **ansible_ec2_iam_security_credentials_role_name_expiration**  string | IAM role credentials expiration time.  Returned: success  Sample: `"2017-05-12T09:11:41Z"` |
| **ansible_ec2_iam_security_credentials_role_name_lastupdated**  string | IAM role last updated time.  Returned: success  Sample: `"2017-05-12T02:40:44Z"` |
| **ansible_ec2_iam_security_credentials_role_name_secretaccesskey**  string | IAM role secret access key.  Returned: success  Sample: `""` |
| **ansible_ec2_iam_security_credentials_role_name_token**  string | IAM role token.  Returned: success  Sample: `""` |
| **ansible_ec2_iam_security_credentials_role_name_type**  string | IAM role type.  Returned: success  Sample: `"AWS-HMAC"` |
| **ansible_ec2_instance_action**  string | Notifies the instance that it should reboot in preparation for bundling.  Returned: success  Sample: `"none"` |
| **ansible_ec2_instance_id**  string | The ID of this instance.  Returned: success  Sample: `"i-XXXXXXXXXXXXXXXXX"` |
| **ansible_ec2_instance_identity_document**  string | JSON containing instance attributes, such as instance-id, private IP address, etc.  Returned: success  Sample: `""` |
| **ansible_ec2_instance_identity_document_accountid**  string | Returned: success  Sample: `"012345678901"` |
| **ansible_ec2_instance_identity_document_architecture**  string | Instance system architecture.  Returned: success  Sample: `"x86_64"` |
| **ansible_ec2_instance_identity_document_availabilityzone**  string | The Availability Zone in which the instance launched.  Returned: success  Sample: `"us-east-1a"` |
| **ansible_ec2_instance_identity_document_billingproducts**  string | Billing products for this instance.  Returned: success  Sample: `""` |
| **ansible_ec2_instance_identity_document_devpayproductcodes**  string | Product codes for the launched AMI.  Returned: success  Sample: `""` |
| **ansible_ec2_instance_identity_document_imageid**  string | The AMI ID used to launch the instance.  Returned: success  Sample: `"ami-01234567"` |
| **ansible_ec2_instance_identity_document_instanceid**  string | The ID of this instance.  Returned: success  Sample: `"i-0123456789abcdef0"` |
| **ansible_ec2_instance_identity_document_instancetype**  string | The type of instance.  Returned: success  Sample: `"m4.large"` |
| **ansible_ec2_instance_identity_document_kernelid**  string | The ID of the kernel launched with this instance, if applicable.  Returned: success  Sample: `""` |
| **ansible_ec2_instance_identity_document_pendingtime**  string | The instance pending time.  Returned: success  Sample: `"2017-05-11T20:51:20Z"` |
| **ansible_ec2_instance_identity_document_privateip**  string | The private IPv4 address of the instance.  In cases where multiple network interfaces are present, this refers to the eth0 device (the device for which the device number is 0).  Returned: success  Sample: `"10.0.0.1"` |
| **ansible_ec2_instance_identity_document_ramdiskid**  string | The ID of the RAM disk specified at launch time, if applicable.  Returned: success  Sample: `""` |
| **ansible_ec2_instance_identity_document_region**  string | The Region in which the instance launched.  Returned: success  Sample: `"us-east-1"` |
| **ansible_ec2_instance_identity_document_version**  string | Identity document version.  Returned: success  Sample: `"2010-08-31"` |
| **ansible_ec2_instance_identity_pkcs7**  string | Used to verify the document’s authenticity and content against the signature.  Returned: success  Sample: `""` |
| **ansible_ec2_instance_identity_rsa2048**  string | Used to verify the document’s authenticity and content against the signature.  Returned: success  Sample: `""` |
| **ansible_ec2_instance_identity_signature**  string | Data that can be used by other parties to verify its origin and authenticity.  Returned: success  Sample: `""` |
| **ansible_ec2_instance_life_cycle**  string | The purchasing option of the instance.  Returned: success  Sample: `"on-demand"` |
| **ansible_ec2_instance_type**  string | The type of the instance.  Returned: success  Sample: `"m4.large"` |
| **ansible_ec2_local_hostname**  string | The private IPv4 DNS hostname of the instance.  In cases where multiple network interfaces are present, this refers to the eth0 device (the device for which the device number is 0).  Returned: success  Sample: `"ip-10-0-0-1.ec2.internal"` |
| **ansible_ec2_local_ipv4**  string | The private IPv4 address of the instance.  In cases where multiple network interfaces are present, this refers to the eth0 device (the device for which the device number is 0).  Returned: success  Sample: `"10.0.0.1"` |
| **ansible_ec2_mac**  string | The instance’s media access control (MAC) address.  In cases where multiple network interfaces are present, this refers to the eth0 device (the device for which the device number is 0).  Returned: success  Sample: `"00:11:22:33:44:55"` |
| **ansible_ec2_metrics_vhostmd**  string | Metrics; no longer available.  Returned: success  Sample: `""` |
| **ansible_ec2_network_interfaces_macs_mac_address_device_number**  string | The unique device number associated with that interface. The device number corresponds to the device name; for example, a device-number of 2 is for the eth2 device.  This category corresponds to the DeviceIndex and device-index fields that are used by the Amazon EC2 API and the EC2 commands for the AWS CLI.  Returned: success  Sample: `"0"` |
| **ansible_ec2_network_interfaces_macs_mac_address_interface_id**  string | The elastic network interface ID.  Returned: success  Sample: `"eni-12345678"` |
| **ansible_ec2_network_interfaces_macs_mac_address_ipv4_associations_ip_address**  string | The private IPv4 addresses that are associated with each public-ip address and assigned to that interface.  Returned: success  Sample: `""` |
| **ansible_ec2_network_interfaces_macs_mac_address_ipv6s**  string | The IPv6 addresses associated with the interface. Returned only for instances launched into a VPC.  Returned: success  Sample: `""` |
| **ansible_ec2_network_interfaces_macs_mac_address_local_hostname**  string | The interface’s local hostname.  Returned: success  Sample: `""` |
| **ansible_ec2_network_interfaces_macs_mac_address_local_ipv4s**  string | The private IPv4 addresses associated with the interface.  Returned: success  Sample: `""` |
| **ansible_ec2_network_interfaces_macs_mac_address_mac**  string | The instance’s MAC address.  Returned: success  Sample: `"00:11:22:33:44:55"` |
| **ansible_ec2_network_interfaces_macs_mac_address_owner_id**  string | The ID of the owner of the network interface.  In multiple-interface environments, an interface can be attached by a third party, such as Elastic Load Balancing.  Traffic on an interface is always billed to the interface owner.  Returned: success  Sample: `"01234567890"` |
| **ansible_ec2_network_interfaces_macs_mac_address_public_hostname**  string | The interface’s public DNS (IPv4). If the instance is in a VPC, this category is only returned if the enableDnsHostnames attribute is set to true.  Returned: success  Sample: `"ec2-1-2-3-4.compute-1.amazonaws.com"` |
| **ansible_ec2_network_interfaces_macs_mac_address_public_ipv4s**  string | The Elastic IP addresses associated with the interface. There may be multiple IPv4 addresses on an instance.  Returned: success  Sample: `"1.2.3.4"` |
| **ansible_ec2_network_interfaces_macs_mac_address_security_group_ids**  string | The IDs of the security groups to which the network interface belongs. Returned only for instances launched into a VPC.  Returned: success  Sample: `"sg-01234567,sg-01234568"` |
| **ansible_ec2_network_interfaces_macs_mac_address_security_groups**  string | Security groups to which the network interface belongs. Returned only for instances launched into a VPC.  Returned: success  Sample: `"secgroup1,secgroup2"` |
| **ansible_ec2_network_interfaces_macs_mac_address_subnet_id**  string | The ID of the subnet in which the interface resides. Returned only for instances launched into a VPC.  Returned: success  Sample: `"subnet-01234567"` |
| **ansible_ec2_network_interfaces_macs_mac_address_subnet_ipv4_cidr_block**  string | The IPv4 CIDR block of the subnet in which the interface resides. Returned only for instances launched into a VPC.  Returned: success  Sample: `"10.0.1.0/24"` |
| **ansible_ec2_network_interfaces_macs_mac_address_subnet_ipv6_cidr_blocks**  string | The IPv6 CIDR block of the subnet in which the interface resides. Returned only for instances launched into a VPC.  Returned: success  Sample: `""` |
| **ansible_ec2_network_interfaces_macs_mac_address_vpc_id**  string | The ID of the VPC in which the interface resides. Returned only for instances launched into a VPC.  Returned: success  Sample: `"vpc-0123456"` |
| **ansible_ec2_network_interfaces_macs_mac_address_vpc_ipv4_cidr_block**  string | The IPv4 CIDR block of the VPC in which the interface resides. Returned only for instances launched into a VPC.  Returned: success  Sample: `"10.0.0.0/16"` |
| **ansible_ec2_network_interfaces_macs_mac_address_vpc_ipv4_cidr_blocks**  string | The IPv4 CIDR block of the VPC in which the interface resides. Returned only for instances launched into a VPC.  Returned: success  Sample: `"10.0.0.0/16"` |
| **ansible_ec2_network_interfaces_macs_mac_address_vpc_ipv6_cidr_blocks**  string | The IPv6 CIDR block of the VPC in which the interface resides. Returned only for instances launched into a VPC.  Returned: success  Sample: `""` |
| **ansible_ec2_placement_availability_zone**  string | The Availability Zone in which the instance launched.  Returned: success  Sample: `"us-east-1a"` |
| **ansible_ec2_placement_region**  string | The Region in which the instance launched.  Returned: success  Sample: `"us-east-1"` |
| **ansible_ec2_product_codes**  string | Product codes associated with the instance, if any.  Returned: success  Sample: `"aw0evgkw8e5c1q413zgy5pjce"` |
| **ansible_ec2_profile**  string | EC2 instance hardware profile.  Returned: success  Sample: `"default-hvm"` |
| **ansible_ec2_public_hostname**  string | The instance’s public DNS. If the instance is in a VPC, this category is only returned if the enableDnsHostnames attribute is set to true.  Returned: success  Sample: `"ec2-1-2-3-4.compute-1.amazonaws.com"` |
| **ansible_ec2_public_ipv4**  string | The public IPv4 address. If an Elastic IP address is associated with the instance, the value returned is the Elastic IP address.  Returned: success  Sample: `"1.2.3.4"` |
| **ansible_ec2_public_key**  string | Public key. Only available if supplied at instance launch time.  Returned: success  Sample: `""` |
| **ansible_ec2_ramdisk_id**  string | The ID of the RAM disk specified at launch time, if applicable.  Returned: success  Sample: `""` |
| **ansible_ec2_reservation_id**  string | The ID of the reservation.  Returned: success  Sample: `"r-0123456789abcdef0"` |
| **ansible_ec2_security_groups**  string | The names of the security groups applied to the instance. After launch, you can only change the security groups of instances running in a VPC.  Such changes are reflected here and in network/interfaces/macs/mac/security-groups.  Returned: success  Sample: `"securitygroup1,securitygroup2"` |
| **ansible_ec2_services_domain**  string | The domain for AWS resources for the region; for example, amazonaws.com for us-east-1.  Returned: success  Sample: `"amazonaws.com"` |
| **ansible_ec2_services_partition**  string | The partition that the resource is in. For standard AWS regions, the partition is aws.  If you have resources in other partitions, the partition is aws-partitionname.  For example, the partition for resources in the China (Beijing) region is aws-cn.  Returned: success  Sample: `"aws"` |
| **ansible_ec2_spot_termination_time**  string | The approximate time, in UTC, that the operating system for your Spot instance will receive the shutdown signal.  This item is present and contains a time value only if the Spot instance has been marked for termination by Amazon EC2.  The termination-time item is not set to a time if you terminated the Spot instance yourself.  Returned: success  Sample: `"2015-01-05T18:02:00Z"` |
| **ansible_ec2_user_data**  string | The instance user data.  Returned: success  Sample: `"#!/bin/bash"` |

### Authors

- Silviu Dicu (@silviud)
- Vinay Dandekar (@roadmapper)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
