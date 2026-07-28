---
collection: ansible
version: "6"
title: "Amazon.Aws"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/
fetched_at: 2026-07-28T00:24:32+00:00
---
# Amazon.Aws

Collection version 3.5.0

- [Description](index.md#description)
- [Communication](index.md#communication)
- [Scenario Guide](index.md#scenario-guide)
- [Module Development Guidelines](index.md#module-development-guidelines)
- [Dynamic Inventory Plugin Guide](index.md#dynamic-inventory-plugin-guide)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

**Author:**

- Ansible (<https://github.com/ansible>)

**Supported ansible-core versions:**

- 2.9.10 or newer

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)

## [Communication](index.md#id2)

- Matrix room `#aws:ansible.im`: [General usage and support questions](https://matrix.to/#/#aws:ansible.im).
- IRC channel `#ansible-aws` (Libera network):
  [General usage and support questions](https://web.libera.chat/?channel=#ansible-aws).

## [Scenario Guide](index.md#id3)

- [Amazon Web Services Guide](docsite/guide_aws.md)

## [Module Development Guidelines](index.md#id4)

- [Guidelines for Ansible Amazon AWS module development](docsite/dev_guidelines.md)

## [Dynamic Inventory Plugin Guide](index.md#id5)

- [Dynamic Inventory Plugin](docsite/aws_ec2_guide.md)
- [Authentication](docsite/aws_ec2_guide.md#authentication)
- [Minimal Example](docsite/aws_ec2_guide.md#minimal-example)
- [Allowed Options](docsite/aws_ec2_guide.md#allowed-options)
- [Complex Example](docsite/aws_ec2_guide.md#complex-example)
- [Using Dynamic Inventory Inside Playbook](docsite/aws_ec2_guide.md#using-dynamic-inventory-inside-playbook)

## [Plugin Index](index.md#id6)

These are the plugins in the amazon.aws collection:

### Modules

- [aws_az_info module](aws_az_info_module.md#ansible-collections-amazon-aws-aws-az-info-module) – Gather information about availability zones in AWS.
- [aws_caller_info module](aws_caller_info_module.md#ansible-collections-amazon-aws-aws-caller-info-module) – Get information about the user and account being used to make AWS calls.
- [aws_s3 module](aws_s3_module.md#ansible-collections-amazon-aws-aws-s3-module) – manage objects in S3.
- [cloudformation module](cloudformation_module.md#ansible-collections-amazon-aws-cloudformation-module) – Create or delete an AWS CloudFormation stack
- [cloudformation_info module](cloudformation_info_module.md#ansible-collections-amazon-aws-cloudformation-info-module) – Obtain information about an AWS CloudFormation stack
- [ec2 module](ec2_module.md#ansible-collections-amazon-aws-ec2-module) – create, terminate, start or stop an instance in ec2
- [ec2_ami module](ec2_ami_module.md#ansible-collections-amazon-aws-ec2-ami-module) – Create or destroy an image (AMI) in ec2
- [ec2_ami_info module](ec2_ami_info_module.md#ansible-collections-amazon-aws-ec2-ami-info-module) – Gather information about ec2 AMIs
- [ec2_eni module](ec2_eni_module.md#ansible-collections-amazon-aws-ec2-eni-module) – Create and optionally attach an Elastic Network Interface (ENI) to an instance
- [ec2_eni_info module](ec2_eni_info_module.md#ansible-collections-amazon-aws-ec2-eni-info-module) – Gather information about ec2 ENI interfaces in AWS
- [ec2_group module](ec2_group_module.md#ansible-collections-amazon-aws-ec2-group-module) – maintain an ec2 VPC security group.
- [ec2_group_info module](ec2_group_info_module.md#ansible-collections-amazon-aws-ec2-group-info-module) – Gather information about ec2 security groups in AWS.
- [ec2_instance module](ec2_instance_module.md#ansible-collections-amazon-aws-ec2-instance-module) – Create & manage EC2 instances
- [ec2_instance_info module](ec2_instance_info_module.md#ansible-collections-amazon-aws-ec2-instance-info-module) – Gather information about ec2 instances in AWS
- [ec2_key module](ec2_key_module.md#ansible-collections-amazon-aws-ec2-key-module) – create or delete an ec2 key pair
- [ec2_metadata_facts module](ec2_metadata_facts_module.md#ansible-collections-amazon-aws-ec2-metadata-facts-module) – gathers facts (instance metadata) about remote hosts within EC2
- [ec2_snapshot module](ec2_snapshot_module.md#ansible-collections-amazon-aws-ec2-snapshot-module) – Creates a snapshot from an existing volume
- [ec2_snapshot_info module](ec2_snapshot_info_module.md#ansible-collections-amazon-aws-ec2-snapshot-info-module) – Gathers information about EC2 volume snapshots in AWS
- [ec2_spot_instance module](ec2_spot_instance_module.md#ansible-collections-amazon-aws-ec2-spot-instance-module) – request, stop, reboot or cancel spot instance
- [ec2_spot_instance_info module](ec2_spot_instance_info_module.md#ansible-collections-amazon-aws-ec2-spot-instance-info-module) – Gather information about ec2 spot instance requests
- [ec2_tag module](ec2_tag_module.md#ansible-collections-amazon-aws-ec2-tag-module) – create and remove tags on ec2 resources
- [ec2_tag_info module](ec2_tag_info_module.md#ansible-collections-amazon-aws-ec2-tag-info-module) – list tags on ec2 resources
- [ec2_vol module](ec2_vol_module.md#ansible-collections-amazon-aws-ec2-vol-module) – Create and attach a volume, return volume id and device map
- [ec2_vol_info module](ec2_vol_info_module.md#ansible-collections-amazon-aws-ec2-vol-info-module) – Gather information about ec2 volumes in AWS
- [ec2_vpc_dhcp_option module](ec2_vpc_dhcp_option_module.md#ansible-collections-amazon-aws-ec2-vpc-dhcp-option-module) – Manages DHCP Options, and can ensure the DHCP options for the given VPC match what’s requested
- [ec2_vpc_dhcp_option_info module](ec2_vpc_dhcp_option_info_module.md#ansible-collections-amazon-aws-ec2-vpc-dhcp-option-info-module) – Gather information about dhcp options sets in AWS
- [ec2_vpc_endpoint module](ec2_vpc_endpoint_module.md#ansible-collections-amazon-aws-ec2-vpc-endpoint-module) – Create and delete AWS VPC Endpoints.
- [ec2_vpc_endpoint_info module](ec2_vpc_endpoint_info_module.md#ansible-collections-amazon-aws-ec2-vpc-endpoint-info-module) – Retrieves AWS VPC endpoints details using AWS methods.
- [ec2_vpc_endpoint_service_info module](ec2_vpc_endpoint_service_info_module.md#ansible-collections-amazon-aws-ec2-vpc-endpoint-service-info-module) – retrieves AWS VPC endpoint service details
- [ec2_vpc_igw module](ec2_vpc_igw_module.md#ansible-collections-amazon-aws-ec2-vpc-igw-module) – Manage an AWS VPC Internet gateway
- [ec2_vpc_igw_info module](ec2_vpc_igw_info_module.md#ansible-collections-amazon-aws-ec2-vpc-igw-info-module) – Gather information about internet gateways in AWS
- [ec2_vpc_nat_gateway module](ec2_vpc_nat_gateway_module.md#ansible-collections-amazon-aws-ec2-vpc-nat-gateway-module) – Manage AWS VPC NAT Gateways.
- [ec2_vpc_nat_gateway_info module](ec2_vpc_nat_gateway_info_module.md#ansible-collections-amazon-aws-ec2-vpc-nat-gateway-info-module) – Retrieves AWS VPC Managed Nat Gateway details using AWS methods.
- [ec2_vpc_net module](ec2_vpc_net_module.md#ansible-collections-amazon-aws-ec2-vpc-net-module) – Configure AWS virtual private clouds
- [ec2_vpc_net_info module](ec2_vpc_net_info_module.md#ansible-collections-amazon-aws-ec2-vpc-net-info-module) – Gather information about ec2 VPCs in AWS
- [ec2_vpc_route_table module](ec2_vpc_route_table_module.md#ansible-collections-amazon-aws-ec2-vpc-route-table-module) – Manage route tables for AWS virtual private clouds
- [ec2_vpc_route_table_info module](ec2_vpc_route_table_info_module.md#ansible-collections-amazon-aws-ec2-vpc-route-table-info-module) – Gather information about ec2 VPC route tables in AWS
- [ec2_vpc_subnet module](ec2_vpc_subnet_module.md#ansible-collections-amazon-aws-ec2-vpc-subnet-module) – Manage subnets in AWS virtual private clouds
- [ec2_vpc_subnet_info module](ec2_vpc_subnet_info_module.md#ansible-collections-amazon-aws-ec2-vpc-subnet-info-module) – Gather information about ec2 VPC subnets in AWS
- [elb_classic_lb module](elb_classic_lb_module.md#ansible-collections-amazon-aws-elb-classic-lb-module) – creates, updates or destroys an Amazon ELB.
- [s3_bucket module](s3_bucket_module.md#ansible-collections-amazon-aws-s3-bucket-module) – Manage S3 buckets in AWS, DigitalOcean, Ceph, Walrus, FakeS3 and StorageGRID

### Callback Plugins

- [aws_resource_actions callback](aws_resource_actions_callback.md#ansible-collections-amazon-aws-aws-resource-actions-callback) – summarizes all “resource:actions” completed

### Inventory Plugins

- [aws_ec2 inventory](aws_ec2_inventory.md#ansible-collections-amazon-aws-aws-ec2-inventory) – EC2 inventory source
- [aws_rds inventory](aws_rds_inventory.md#ansible-collections-amazon-aws-aws-rds-inventory) – rds instance source

### Lookup Plugins

- [aws_account_attribute lookup](aws_account_attribute_lookup.md#ansible-collections-amazon-aws-aws-account-attribute-lookup) – Look up AWS account attributes.
- [aws_secret lookup](aws_secret_lookup.md#ansible-collections-amazon-aws-aws-secret-lookup) – Look up secrets stored in AWS Secrets Manager.
- [aws_service_ip_ranges lookup](aws_service_ip_ranges_lookup.md#ansible-collections-amazon-aws-aws-service-ip-ranges-lookup) – Look up the IP ranges for services provided in AWS such as EC2 and S3.
- [aws_ssm lookup](aws_ssm_lookup.md#ansible-collections-amazon-aws-aws-ssm-lookup) – Get the value for a SSM parameter or all parameters under a path.

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
