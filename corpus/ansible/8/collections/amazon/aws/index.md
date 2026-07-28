---
collection: ansible
version: "8"
title: "Amazon.Aws"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/index.html
fetched_at: 2026-07-28T01:01:47+00:00
---
# Amazon.Aws

Collection version 6.5.0

- [Description](index.md#description)
- [Communication](index.md#communication)
- [Changelog](index.md#changelog)
- [Scenario Guide](index.md#scenario-guide)
- [Module Development Guidelines](index.md#module-development-guidelines)
- [Dynamic Inventory Plugin Guide](index.md#dynamic-inventory-plugin-guide)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

A variety of Ansible content to help automate the management of AWS services.

**Author:**

- Ansible (<https://github.com/ansible>)

**Supported ansible-core versions:**

- 2.12.0 or newer

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)

## [Communication](index.md#id2)

- Matrix room `#aws:ansible.im`: [General usage and support questions](https://matrix.to/#/#aws:ansible.im).
- IRC channel `#ansible-aws` (Libera network):
  [General usage and support questions](https://web.libera.chat/?channel=#ansible-aws).

## [Changelog](index.md#id3)

- [amazon.aws Release Notes](docsite/CHANGELOG.md)

## [Scenario Guide](index.md#id4)

- [Amazon Web Services Guide](docsite/guide_aws.md)

## [Module Development Guidelines](index.md#id5)

- [Guidelines for Ansible Amazon AWS module development](docsite/dev_guidelines.md)

## [Dynamic Inventory Plugin Guide](index.md#id6)

- [Dynamic Inventory Plugin](docsite/aws_ec2_guide.md)
- [Authentication](docsite/aws_ec2_guide.md#authentication)
- [Minimal Example](docsite/aws_ec2_guide.md#minimal-example)
- [Allowed Options](docsite/aws_ec2_guide.md#allowed-options)
- [Complex Example](docsite/aws_ec2_guide.md#complex-example)
- [Using Dynamic Inventory Inside Playbook](docsite/aws_ec2_guide.md#using-dynamic-inventory-inside-playbook)

## [Plugin Index](index.md#id7)

These are the plugins in the amazon.aws collection:

### Modules

- [autoscaling_group module](autoscaling_group_module.md#ansible-collections-amazon-aws-autoscaling-group-module) – Create or delete AWS AutoScaling Groups (ASGs)
- [autoscaling_group_info module](autoscaling_group_info_module.md#ansible-collections-amazon-aws-autoscaling-group-info-module) – Gather information about EC2 Auto Scaling Groups (ASGs) in AWS
- [aws_az_info module](aws_az_info_module.md#ansible-collections-amazon-aws-aws-az-info-module) – Gather information about availability zones in AWS
- [aws_caller_info module](aws_caller_info_module.md#ansible-collections-amazon-aws-aws-caller-info-module) – Get information about the user and account being used to make AWS calls
- [backup_plan module](backup_plan_module.md#ansible-collections-amazon-aws-backup-plan-module) – Manage AWS Backup Plans
- [backup_plan_info module](backup_plan_info_module.md#ansible-collections-amazon-aws-backup-plan-info-module) – Describe AWS Backup Plans
- [backup_restore_job_info module](backup_restore_job_info_module.md#ansible-collections-amazon-aws-backup-restore-job-info-module) – List information about backup restore jobs
- [backup_selection module](backup_selection_module.md#ansible-collections-amazon-aws-backup-selection-module) – Create, delete and modify AWS Backup selection
- [backup_selection_info module](backup_selection_info_module.md#ansible-collections-amazon-aws-backup-selection-info-module) – Describe AWS Backup Selections
- [backup_tag module](backup_tag_module.md#ansible-collections-amazon-aws-backup-tag-module) – Manage tags on backup plan, backup vault, recovery point
- [backup_tag_info module](backup_tag_info_module.md#ansible-collections-amazon-aws-backup-tag-info-module) – List tags on AWS Backup resources
- [backup_vault module](backup_vault_module.md#ansible-collections-amazon-aws-backup-vault-module) – Manage AWS Backup Vaults
- [backup_vault_info module](backup_vault_info_module.md#ansible-collections-amazon-aws-backup-vault-info-module) – Describe AWS Backup Vaults
- [cloudformation module](cloudformation_module.md#ansible-collections-amazon-aws-cloudformation-module) – Create or delete an AWS CloudFormation stack
- [cloudformation_info module](cloudformation_info_module.md#ansible-collections-amazon-aws-cloudformation-info-module) – Obtain information about an AWS CloudFormation stack
- [cloudtrail module](cloudtrail_module.md#ansible-collections-amazon-aws-cloudtrail-module) – manage CloudTrail create, delete, update
- [cloudtrail_info module](cloudtrail_info_module.md#ansible-collections-amazon-aws-cloudtrail-info-module) – Gather information about trails in AWS Cloud Trail.
- [cloudwatch_metric_alarm module](cloudwatch_metric_alarm_module.md#ansible-collections-amazon-aws-cloudwatch-metric-alarm-module) – Create/update or delete AWS CloudWatch ‘metric alarms’
- [cloudwatch_metric_alarm_info module](cloudwatch_metric_alarm_info_module.md#ansible-collections-amazon-aws-cloudwatch-metric-alarm-info-module) – Gather information about the alarms for the specified metric
- [cloudwatchevent_rule module](cloudwatchevent_rule_module.md#ansible-collections-amazon-aws-cloudwatchevent-rule-module) – Manage CloudWatch Event rules and targets
- [cloudwatchlogs_log_group module](cloudwatchlogs_log_group_module.md#ansible-collections-amazon-aws-cloudwatchlogs-log-group-module) – create or delete log_group in CloudWatchLogs
- [cloudwatchlogs_log_group_info module](cloudwatchlogs_log_group_info_module.md#ansible-collections-amazon-aws-cloudwatchlogs-log-group-info-module) – Get information about log_group in CloudWatchLogs
- [cloudwatchlogs_log_group_metric_filter module](cloudwatchlogs_log_group_metric_filter_module.md#ansible-collections-amazon-aws-cloudwatchlogs-log-group-metric-filter-module) – Manage CloudWatch log group metric filter
- [ec2_ami module](ec2_ami_module.md#ansible-collections-amazon-aws-ec2-ami-module) – Create or destroy an image (AMI) in EC2
- [ec2_ami_info module](ec2_ami_info_module.md#ansible-collections-amazon-aws-ec2-ami-info-module) – Gather information about ec2 AMIs
- [ec2_eip module](ec2_eip_module.md#ansible-collections-amazon-aws-ec2-eip-module) – manages EC2 elastic IP (EIP) addresses.
- [ec2_eip_info module](ec2_eip_info_module.md#ansible-collections-amazon-aws-ec2-eip-info-module) – List EC2 EIP details
- [ec2_eni module](ec2_eni_module.md#ansible-collections-amazon-aws-ec2-eni-module) – Create and optionally attach an Elastic Network Interface (ENI) to an instance
- [ec2_eni_info module](ec2_eni_info_module.md#ansible-collections-amazon-aws-ec2-eni-info-module) – Gather information about EC2 ENI interfaces in AWS
- [ec2_instance module](ec2_instance_module.md#ansible-collections-amazon-aws-ec2-instance-module) – Create & manage EC2 instances
- [ec2_instance_info module](ec2_instance_info_module.md#ansible-collections-amazon-aws-ec2-instance-info-module) – Gather information about ec2 instances in AWS
- [ec2_key module](ec2_key_module.md#ansible-collections-amazon-aws-ec2-key-module) – Create or delete an EC2 key pair
- [ec2_key_info module](ec2_key_info_module.md#ansible-collections-amazon-aws-ec2-key-info-module) – Gather information about EC2 key pairs in AWS
- [ec2_metadata_facts module](ec2_metadata_facts_module.md#ansible-collections-amazon-aws-ec2-metadata-facts-module) – Gathers facts (instance metadata) about remote hosts within EC2
- [ec2_security_group module](ec2_security_group_module.md#ansible-collections-amazon-aws-ec2-security-group-module) – Maintain an EC2 security group
- [ec2_security_group_info module](ec2_security_group_info_module.md#ansible-collections-amazon-aws-ec2-security-group-info-module) – Gather information about EC2 security groups in AWS
- [ec2_snapshot module](ec2_snapshot_module.md#ansible-collections-amazon-aws-ec2-snapshot-module) – Creates a snapshot from an existing volume
- [ec2_snapshot_info module](ec2_snapshot_info_module.md#ansible-collections-amazon-aws-ec2-snapshot-info-module) – Gathers information about EC2 volume snapshots in AWS
- [ec2_spot_instance module](ec2_spot_instance_module.md#ansible-collections-amazon-aws-ec2-spot-instance-module) – Request, stop, reboot or cancel spot instance
- [ec2_spot_instance_info module](ec2_spot_instance_info_module.md#ansible-collections-amazon-aws-ec2-spot-instance-info-module) – Gather information about ec2 spot instance requests
- [ec2_tag module](ec2_tag_module.md#ansible-collections-amazon-aws-ec2-tag-module) – Create and remove tags on ec2 resources
- [ec2_tag_info module](ec2_tag_info_module.md#ansible-collections-amazon-aws-ec2-tag-info-module) – List tags on ec2 resources
- [ec2_vol module](ec2_vol_module.md#ansible-collections-amazon-aws-ec2-vol-module) – Create and attach a volume, return volume ID and device map
- [ec2_vol_info module](ec2_vol_info_module.md#ansible-collections-amazon-aws-ec2-vol-info-module) – Gather information about EC2 volumes in AWS
- [ec2_vpc_dhcp_option module](ec2_vpc_dhcp_option_module.md#ansible-collections-amazon-aws-ec2-vpc-dhcp-option-module) – Manages DHCP Options, and can ensure the DHCP options for the given VPC match what’s requested
- [ec2_vpc_dhcp_option_info module](ec2_vpc_dhcp_option_info_module.md#ansible-collections-amazon-aws-ec2-vpc-dhcp-option-info-module) – Gather information about DHCP options sets in AWS
- [ec2_vpc_endpoint module](ec2_vpc_endpoint_module.md#ansible-collections-amazon-aws-ec2-vpc-endpoint-module) – Create and delete AWS VPC endpoints
- [ec2_vpc_endpoint_info module](ec2_vpc_endpoint_info_module.md#ansible-collections-amazon-aws-ec2-vpc-endpoint-info-module) – Retrieves AWS VPC endpoints details using AWS methods
- [ec2_vpc_endpoint_service_info module](ec2_vpc_endpoint_service_info_module.md#ansible-collections-amazon-aws-ec2-vpc-endpoint-service-info-module) – Retrieves AWS VPC endpoint service details
- [ec2_vpc_igw module](ec2_vpc_igw_module.md#ansible-collections-amazon-aws-ec2-vpc-igw-module) – Manage an AWS VPC Internet gateway
- [ec2_vpc_igw_info module](ec2_vpc_igw_info_module.md#ansible-collections-amazon-aws-ec2-vpc-igw-info-module) – Gather information about internet gateways in AWS
- [ec2_vpc_nat_gateway module](ec2_vpc_nat_gateway_module.md#ansible-collections-amazon-aws-ec2-vpc-nat-gateway-module) – Manage AWS VPC NAT Gateways
- [ec2_vpc_nat_gateway_info module](ec2_vpc_nat_gateway_info_module.md#ansible-collections-amazon-aws-ec2-vpc-nat-gateway-info-module) – Retrieves AWS VPC Managed Nat Gateway details using AWS methods
- [ec2_vpc_net module](ec2_vpc_net_module.md#ansible-collections-amazon-aws-ec2-vpc-net-module) – Configure AWS Virtual Private Clouds
- [ec2_vpc_net_info module](ec2_vpc_net_info_module.md#ansible-collections-amazon-aws-ec2-vpc-net-info-module) – Gather information about ec2 VPCs in AWS
- [ec2_vpc_route_table module](ec2_vpc_route_table_module.md#ansible-collections-amazon-aws-ec2-vpc-route-table-module) – Manage route tables for AWS Virtual Private Clouds
- [ec2_vpc_route_table_info module](ec2_vpc_route_table_info_module.md#ansible-collections-amazon-aws-ec2-vpc-route-table-info-module) – Gather information about ec2 VPC route tables in AWS
- [ec2_vpc_subnet module](ec2_vpc_subnet_module.md#ansible-collections-amazon-aws-ec2-vpc-subnet-module) – Manage subnets in AWS virtual private clouds
- [ec2_vpc_subnet_info module](ec2_vpc_subnet_info_module.md#ansible-collections-amazon-aws-ec2-vpc-subnet-info-module) – Gather information about ec2 VPC subnets in AWS
- [elb_application_lb module](elb_application_lb_module.md#ansible-collections-amazon-aws-elb-application-lb-module) – Manage an Application Load Balancer
- [elb_application_lb_info module](elb_application_lb_info_module.md#ansible-collections-amazon-aws-elb-application-lb-info-module) – Gather information about Application Load Balancers in AWS
- [elb_classic_lb module](elb_classic_lb_module.md#ansible-collections-amazon-aws-elb-classic-lb-module) – Creates, updates or destroys an Amazon ELB
- [iam_instance_profile module](iam_instance_profile_module.md#ansible-collections-amazon-aws-iam-instance-profile-module) – manage IAM instance profiles
- [iam_instance_profile_info module](iam_instance_profile_info_module.md#ansible-collections-amazon-aws-iam-instance-profile-info-module) – gather information on IAM instance profiles
- [iam_policy module](iam_policy_module.md#ansible-collections-amazon-aws-iam-policy-module) – Manage inline IAM policies for users, groups, and roles
- [iam_policy_info module](iam_policy_info_module.md#ansible-collections-amazon-aws-iam-policy-info-module) – Retrieve inline IAM policies for users, groups, and roles
- [iam_user module](iam_user_module.md#ansible-collections-amazon-aws-iam-user-module) – Manage AWS IAM users
- [iam_user_info module](iam_user_info_module.md#ansible-collections-amazon-aws-iam-user-info-module) – Gather IAM user(s) facts in AWS
- [kms_key module](kms_key_module.md#ansible-collections-amazon-aws-kms-key-module) – Perform various KMS key management tasks
- [kms_key_info module](kms_key_info_module.md#ansible-collections-amazon-aws-kms-key-info-module) – Gather information about AWS KMS keys
- [lambda module](lambda_module.md#ansible-collections-amazon-aws-lambda-module) – Manage AWS Lambda functions
- [lambda_alias module](lambda_alias_module.md#ansible-collections-amazon-aws-lambda-alias-module) – Creates, updates or deletes AWS Lambda function aliases
- [lambda_event module](lambda_event_module.md#ansible-collections-amazon-aws-lambda-event-module) – Creates, updates or deletes AWS Lambda function event mappings
- [lambda_execute module](lambda_execute_module.md#ansible-collections-amazon-aws-lambda-execute-module) – Execute an AWS Lambda function
- [lambda_info module](lambda_info_module.md#ansible-collections-amazon-aws-lambda-info-module) – Gathers AWS Lambda function details
- [lambda_layer module](lambda_layer_module.md#ansible-collections-amazon-aws-lambda-layer-module) – Creates an AWS Lambda layer or deletes an AWS Lambda layer version
- [lambda_layer_info module](lambda_layer_info_module.md#ansible-collections-amazon-aws-lambda-layer-info-module) – List lambda layer or lambda layer versions
- [lambda_policy module](lambda_policy_module.md#ansible-collections-amazon-aws-lambda-policy-module) – Creates, updates or deletes AWS Lambda policy statements.
- [rds_cluster module](rds_cluster_module.md#ansible-collections-amazon-aws-rds-cluster-module) – rds_cluster module
- [rds_cluster_info module](rds_cluster_info_module.md#ansible-collections-amazon-aws-rds-cluster-info-module) – Obtain information about one or more RDS clusters
- [rds_cluster_snapshot module](rds_cluster_snapshot_module.md#ansible-collections-amazon-aws-rds-cluster-snapshot-module) – Manage Amazon RDS snapshots of DB clusters
- [rds_instance module](rds_instance_module.md#ansible-collections-amazon-aws-rds-instance-module) – Manage RDS instances
- [rds_instance_info module](rds_instance_info_module.md#ansible-collections-amazon-aws-rds-instance-info-module) – obtain information about one or more RDS instances
- [rds_instance_snapshot module](rds_instance_snapshot_module.md#ansible-collections-amazon-aws-rds-instance-snapshot-module) – Manage Amazon RDS instance snapshots
- [rds_option_group module](rds_option_group_module.md#ansible-collections-amazon-aws-rds-option-group-module) – Manages the creation, modification, deletion of RDS option groups
- [rds_option_group_info module](rds_option_group_info_module.md#ansible-collections-amazon-aws-rds-option-group-info-module) – rds_option_group_info module
- [rds_param_group module](rds_param_group_module.md#ansible-collections-amazon-aws-rds-param-group-module) – manage RDS parameter groups
- [rds_snapshot_info module](rds_snapshot_info_module.md#ansible-collections-amazon-aws-rds-snapshot-info-module) – obtain information about one or more RDS snapshots
- [rds_subnet_group module](rds_subnet_group_module.md#ansible-collections-amazon-aws-rds-subnet-group-module) – manage RDS database subnet groups
- [route53 module](route53_module.md#ansible-collections-amazon-aws-route53-module) – add or delete entries in Amazons Route 53 DNS service
- [route53_health_check module](route53_health_check_module.md#ansible-collections-amazon-aws-route53-health-check-module) – Manage health-checks in Amazons Route53 DNS service
- [route53_info module](route53_info_module.md#ansible-collections-amazon-aws-route53-info-module) – Retrieves route53 details using AWS methods
- [route53_zone module](route53_zone_module.md#ansible-collections-amazon-aws-route53-zone-module) – add or delete Route53 zones
- [s3_bucket module](s3_bucket_module.md#ansible-collections-amazon-aws-s3-bucket-module) – Manage S3 buckets in AWS, DigitalOcean, Ceph, Walrus, FakeS3 and StorageGRID
- [s3_object module](s3_object_module.md#ansible-collections-amazon-aws-s3-object-module) – Manage objects in S3
- [s3_object_info module](s3_object_info_module.md#ansible-collections-amazon-aws-s3-object-info-module) – Gather information about objects in S3

### Callback Plugins

- [aws_resource_actions callback](aws_resource_actions_callback.md#ansible-collections-amazon-aws-aws-resource-actions-callback) – summarizes all “resource:actions” completed

### Inventory Plugins

- [aws_ec2 inventory](aws_ec2_inventory.md#ansible-collections-amazon-aws-aws-ec2-inventory) – EC2 inventory source
- [aws_rds inventory](aws_rds_inventory.md#ansible-collections-amazon-aws-aws-rds-inventory) – RDS instance inventory source

### Lookup Plugins

- [aws_account_attribute lookup](aws_account_attribute_lookup.md#ansible-collections-amazon-aws-aws-account-attribute-lookup) – Look up AWS account attributes
- [aws_collection_constants lookup](aws_collection_constants_lookup.md#ansible-collections-amazon-aws-aws-collection-constants-lookup) – expose various collection related constants
- [aws_service_ip_ranges lookup](aws_service_ip_ranges_lookup.md#ansible-collections-amazon-aws-aws-service-ip-ranges-lookup) – Look up the IP ranges for services provided in AWS such as EC2 and S3.
- [secretsmanager_secret lookup](secretsmanager_secret_lookup.md#ansible-collections-amazon-aws-secretsmanager-secret-lookup) – Look up secrets stored in AWS Secrets Manager
- [ssm_parameter lookup](ssm_parameter_lookup.md#ansible-collections-amazon-aws-ssm-parameter-lookup) – gets the value for a SSM parameter or all parameters under a path

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
