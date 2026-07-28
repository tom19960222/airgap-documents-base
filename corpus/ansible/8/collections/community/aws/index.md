---
collection: ansible
version: "8"
title: "Community.Aws"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/index.html
fetched_at: 2026-07-28T01:02:06+00:00
---
# Community.Aws

Collection version 6.4.0

- [Description](index.md#description)
- [Communication](index.md#communication)
- [Changelog](index.md#changelog)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

A variety of Ansible content to help automate the management of AWS services.

**Author:**

- Ansible (<https://github.com/ansible>)

**Supported ansible-core versions:**

- 2.12.0 or newer

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)

## [Communication](index.md#id2)

- Matrix room `#aws:ansible.im`: [General usage and support questions](https://matrix.to/#/#aws:ansible.im).
- IRC channel `#ansible-aws` (Libera network):
  [General usage and support questions](https://web.libera.chat/?channel=#ansible-aws).

## [Changelog](index.md#id3)

- [community.aws Release Notes](docsite/CHANGELOG.md)

## [Plugin Index](index.md#id4)

These are the plugins in the community.aws collection:

### Modules

- [accessanalyzer_validate_policy_info module](accessanalyzer_validate_policy_info_module.md#ansible-collections-community-aws-accessanalyzer-validate-policy-info-module) – Performs validation of IAM policies
- [acm_certificate module](acm_certificate_module.md#ansible-collections-community-aws-acm-certificate-module) – Upload and delete certificates in the AWS Certificate Manager service
- [acm_certificate_info module](acm_certificate_info_module.md#ansible-collections-community-aws-acm-certificate-info-module) – Retrieve certificate information from AWS Certificate Manager service
- [api_gateway module](api_gateway_module.md#ansible-collections-community-aws-api-gateway-module) – Manage AWS API Gateway APIs
- [api_gateway_domain module](api_gateway_domain_module.md#ansible-collections-community-aws-api-gateway-domain-module) – Manage AWS API Gateway custom domains
- [api_gateway_info module](api_gateway_info_module.md#ansible-collections-community-aws-api-gateway-info-module) – Gather information about ec2 instances in AWS
- [application_autoscaling_policy module](application_autoscaling_policy_module.md#ansible-collections-community-aws-application-autoscaling-policy-module) – Manage Application Auto Scaling Scaling Policies
- [autoscaling_complete_lifecycle_action module](autoscaling_complete_lifecycle_action_module.md#ansible-collections-community-aws-autoscaling-complete-lifecycle-action-module) – Completes the lifecycle action of an instance
- [autoscaling_instance_refresh module](autoscaling_instance_refresh_module.md#ansible-collections-community-aws-autoscaling-instance-refresh-module) – Start or cancel an EC2 Auto Scaling Group (ASG) instance refresh in AWS
- [autoscaling_instance_refresh_info module](autoscaling_instance_refresh_info_module.md#ansible-collections-community-aws-autoscaling-instance-refresh-info-module) – Gather information about EC2 Auto Scaling Group (ASG) Instance Refreshes in AWS
- [autoscaling_launch_config module](autoscaling_launch_config_module.md#ansible-collections-community-aws-autoscaling-launch-config-module) – Create or delete AWS Autoscaling Launch Configurations
- [autoscaling_launch_config_find module](autoscaling_launch_config_find_module.md#ansible-collections-community-aws-autoscaling-launch-config-find-module) – Find AWS Autoscaling Launch Configurations
- [autoscaling_launch_config_info module](autoscaling_launch_config_info_module.md#ansible-collections-community-aws-autoscaling-launch-config-info-module) – Gather information about AWS Autoscaling Launch Configurations
- [autoscaling_lifecycle_hook module](autoscaling_lifecycle_hook_module.md#ansible-collections-community-aws-autoscaling-lifecycle-hook-module) – Create, delete or update AWS ASG Lifecycle Hooks
- [autoscaling_policy module](autoscaling_policy_module.md#ansible-collections-community-aws-autoscaling-policy-module) – Create or delete AWS scaling policies for Autoscaling groups
- [autoscaling_scheduled_action module](autoscaling_scheduled_action_module.md#ansible-collections-community-aws-autoscaling-scheduled-action-module) – Create, modify and delete ASG scheduled scaling actions
- [aws_region_info module](aws_region_info_module.md#ansible-collections-community-aws-aws-region-info-module) – Gather information about AWS regions
- [batch_compute_environment module](batch_compute_environment_module.md#ansible-collections-community-aws-batch-compute-environment-module) – Manage AWS Batch Compute Environments
- [batch_job_definition module](batch_job_definition_module.md#ansible-collections-community-aws-batch-job-definition-module) – Manage AWS Batch Job Definitions
- [batch_job_queue module](batch_job_queue_module.md#ansible-collections-community-aws-batch-job-queue-module) – Manage AWS Batch Job Queues
- [cloudformation_exports_info module](cloudformation_exports_info_module.md#ansible-collections-community-aws-cloudformation-exports-info-module) – Read a value from CloudFormation Exports
- [cloudformation_stack_set module](cloudformation_stack_set_module.md#ansible-collections-community-aws-cloudformation-stack-set-module) – Manage groups of CloudFormation stacks
- [cloudfront_distribution module](cloudfront_distribution_module.md#ansible-collections-community-aws-cloudfront-distribution-module) – Create, update and delete AWS CloudFront distributions
- [cloudfront_distribution_info module](cloudfront_distribution_info_module.md#ansible-collections-community-aws-cloudfront-distribution-info-module) – Obtain facts about an AWS CloudFront distribution
- [cloudfront_invalidation module](cloudfront_invalidation_module.md#ansible-collections-community-aws-cloudfront-invalidation-module) – create invalidations for AWS CloudFront distributions
- [cloudfront_origin_access_identity module](cloudfront_origin_access_identity_module.md#ansible-collections-community-aws-cloudfront-origin-access-identity-module) – Create, update and delete origin access identities for a CloudFront distribution
- [cloudfront_response_headers_policy module](cloudfront_response_headers_policy_module.md#ansible-collections-community-aws-cloudfront-response-headers-policy-module) – Create, update and delete response headers policies to be used in a Cloudfront distribution
- [codebuild_project module](codebuild_project_module.md#ansible-collections-community-aws-codebuild-project-module) – Create or delete an AWS CodeBuild project
- [codecommit_repository module](codecommit_repository_module.md#ansible-collections-community-aws-codecommit-repository-module) – Manage repositories in AWS CodeCommit
- [codepipeline module](codepipeline_module.md#ansible-collections-community-aws-codepipeline-module) – Create or delete AWS CodePipelines
- [config_aggregation_authorization module](config_aggregation_authorization_module.md#ansible-collections-community-aws-config-aggregation-authorization-module) – Manage cross-account AWS Config authorizations
- [config_aggregator module](config_aggregator_module.md#ansible-collections-community-aws-config-aggregator-module) – Manage AWS Config aggregations across multiple accounts
- [config_delivery_channel module](config_delivery_channel_module.md#ansible-collections-community-aws-config-delivery-channel-module) – Manage AWS Config delivery channels
- [config_recorder module](config_recorder_module.md#ansible-collections-community-aws-config-recorder-module) – Manage AWS Config Recorders
- [config_rule module](config_rule_module.md#ansible-collections-community-aws-config-rule-module) – Manage AWS Config rule resources
- [data_pipeline module](data_pipeline_module.md#ansible-collections-community-aws-data-pipeline-module) – Create and manage AWS Datapipelines
- [directconnect_confirm_connection module](directconnect_confirm_connection_module.md#ansible-collections-community-aws-directconnect-confirm-connection-module) – Confirms the creation of a hosted DirectConnect connection
- [directconnect_connection module](directconnect_connection_module.md#ansible-collections-community-aws-directconnect-connection-module) – Creates, deletes, modifies a DirectConnect connection
- [directconnect_gateway module](directconnect_gateway_module.md#ansible-collections-community-aws-directconnect-gateway-module) – Manage AWS Direct Connect gateway
- [directconnect_link_aggregation_group module](directconnect_link_aggregation_group_module.md#ansible-collections-community-aws-directconnect-link-aggregation-group-module) – Manage Direct Connect LAG bundles
- [directconnect_virtual_interface module](directconnect_virtual_interface_module.md#ansible-collections-community-aws-directconnect-virtual-interface-module) – Manage Direct Connect virtual interfaces
- [dms_endpoint module](dms_endpoint_module.md#ansible-collections-community-aws-dms-endpoint-module) – Creates or destroys a data migration services endpoint
- [dms_replication_subnet_group module](dms_replication_subnet_group_module.md#ansible-collections-community-aws-dms-replication-subnet-group-module) – creates or destroys a data migration services subnet group
- [dynamodb_table module](dynamodb_table_module.md#ansible-collections-community-aws-dynamodb-table-module) – Create, update or delete AWS Dynamo DB tables
- [dynamodb_ttl module](dynamodb_ttl_module.md#ansible-collections-community-aws-dynamodb-ttl-module) – Set TTL for a given DynamoDB table
- [ec2_ami_copy module](ec2_ami_copy_module.md#ansible-collections-community-aws-ec2-ami-copy-module) – copies AMI between AWS regions, return new image id
- [ec2_carrier_gateway module](ec2_carrier_gateway_module.md#ansible-collections-community-aws-ec2-carrier-gateway-module) – Manage an AWS VPC Carrier gateway
- [ec2_carrier_gateway_info module](ec2_carrier_gateway_info_module.md#ansible-collections-community-aws-ec2-carrier-gateway-info-module) – Gather information about carrier gateways in AWS
- [ec2_customer_gateway module](ec2_customer_gateway_module.md#ansible-collections-community-aws-ec2-customer-gateway-module) – Manage an AWS customer gateway
- [ec2_customer_gateway_info module](ec2_customer_gateway_info_module.md#ansible-collections-community-aws-ec2-customer-gateway-info-module) – Gather information about customer gateways in AWS
- [ec2_launch_template module](ec2_launch_template_module.md#ansible-collections-community-aws-ec2-launch-template-module) – Manage EC2 launch templates
- [ec2_placement_group module](ec2_placement_group_module.md#ansible-collections-community-aws-ec2-placement-group-module) – Create or delete an EC2 Placement Group
- [ec2_placement_group_info module](ec2_placement_group_info_module.md#ansible-collections-community-aws-ec2-placement-group-info-module) – List EC2 Placement Group(s) details
- [ec2_snapshot_copy module](ec2_snapshot_copy_module.md#ansible-collections-community-aws-ec2-snapshot-copy-module) – Copies an EC2 snapshot and returns the new Snapshot ID
- [ec2_transit_gateway module](ec2_transit_gateway_module.md#ansible-collections-community-aws-ec2-transit-gateway-module) – Create and delete AWS Transit Gateways
- [ec2_transit_gateway_info module](ec2_transit_gateway_info_module.md#ansible-collections-community-aws-ec2-transit-gateway-info-module) – Gather information about ec2 transit gateways in AWS
- [ec2_transit_gateway_vpc_attachment module](ec2_transit_gateway_vpc_attachment_module.md#ansible-collections-community-aws-ec2-transit-gateway-vpc-attachment-module) – Create and delete AWS Transit Gateway VPC attachments
- [ec2_transit_gateway_vpc_attachment_info module](ec2_transit_gateway_vpc_attachment_info_module.md#ansible-collections-community-aws-ec2-transit-gateway-vpc-attachment-info-module) – describes AWS Transit Gateway VPC attachments
- [ec2_vpc_egress_igw module](ec2_vpc_egress_igw_module.md#ansible-collections-community-aws-ec2-vpc-egress-igw-module) – Manage an AWS VPC Egress Only Internet gateway
- [ec2_vpc_nacl module](ec2_vpc_nacl_module.md#ansible-collections-community-aws-ec2-vpc-nacl-module) – create and delete Network ACLs
- [ec2_vpc_nacl_info module](ec2_vpc_nacl_info_module.md#ansible-collections-community-aws-ec2-vpc-nacl-info-module) – Gather information about Network ACLs in an AWS VPC
- [ec2_vpc_peer module](ec2_vpc_peer_module.md#ansible-collections-community-aws-ec2-vpc-peer-module) – create, delete, accept, and reject VPC peering connections between two VPCs.
- [ec2_vpc_peering_info module](ec2_vpc_peering_info_module.md#ansible-collections-community-aws-ec2-vpc-peering-info-module) – Retrieves AWS VPC Peering details using AWS methods.
- [ec2_vpc_vgw module](ec2_vpc_vgw_module.md#ansible-collections-community-aws-ec2-vpc-vgw-module) – Create and delete AWS VPN Virtual Gateways
- [ec2_vpc_vgw_info module](ec2_vpc_vgw_info_module.md#ansible-collections-community-aws-ec2-vpc-vgw-info-module) – Gather information about virtual gateways in AWS
- [ec2_vpc_vpn module](ec2_vpc_vpn_module.md#ansible-collections-community-aws-ec2-vpc-vpn-module) – Create, modify, and delete EC2 VPN connections
- [ec2_vpc_vpn_info module](ec2_vpc_vpn_info_module.md#ansible-collections-community-aws-ec2-vpc-vpn-info-module) – Gather information about VPN Connections in AWS.
- [ec2_win_password module](ec2_win_password_module.md#ansible-collections-community-aws-ec2-win-password-module) – Gets the default administrator password for EC2 Windows instances
- [ecs_attribute module](ecs_attribute_module.md#ansible-collections-community-aws-ecs-attribute-module) – manage ecs attributes
- [ecs_cluster module](ecs_cluster_module.md#ansible-collections-community-aws-ecs-cluster-module) – Create or terminate ECS clusters.
- [ecs_ecr module](ecs_ecr_module.md#ansible-collections-community-aws-ecs-ecr-module) – Manage Elastic Container Registry repositories
- [ecs_service module](ecs_service_module.md#ansible-collections-community-aws-ecs-service-module) – Create, terminate, start or stop a service in ECS
- [ecs_service_info module](ecs_service_info_module.md#ansible-collections-community-aws-ecs-service-info-module) – List or describe services in ECS
- [ecs_tag module](ecs_tag_module.md#ansible-collections-community-aws-ecs-tag-module) – create and remove tags on Amazon ECS resources
- [ecs_task module](ecs_task_module.md#ansible-collections-community-aws-ecs-task-module) – Run, start or stop a task in ECS
- [ecs_taskdefinition module](ecs_taskdefinition_module.md#ansible-collections-community-aws-ecs-taskdefinition-module) – register a task definition in ecs
- [ecs_taskdefinition_info module](ecs_taskdefinition_info_module.md#ansible-collections-community-aws-ecs-taskdefinition-info-module) – Describe a task definition in ECS
- [efs module](efs_module.md#ansible-collections-community-aws-efs-module) – create and maintain EFS file systems
- [efs_info module](efs_info_module.md#ansible-collections-community-aws-efs-info-module) – Get information about Amazon EFS file systems
- [efs_tag module](efs_tag_module.md#ansible-collections-community-aws-efs-tag-module) – create and remove tags on Amazon EFS resources
- [eks_cluster module](eks_cluster_module.md#ansible-collections-community-aws-eks-cluster-module) – Manage Elastic Kubernetes Service (EKS) Clusters
- [eks_fargate_profile module](eks_fargate_profile_module.md#ansible-collections-community-aws-eks-fargate-profile-module) – Manage EKS Fargate Profile
- [eks_nodegroup module](eks_nodegroup_module.md#ansible-collections-community-aws-eks-nodegroup-module) – Manage EKS Nodegroup module
- [elasticache module](elasticache_module.md#ansible-collections-community-aws-elasticache-module) – Manage cache clusters in Amazon ElastiCache
- [elasticache_info module](elasticache_info_module.md#ansible-collections-community-aws-elasticache-info-module) – Retrieve information for AWS ElastiCache clusters
- [elasticache_parameter_group module](elasticache_parameter_group_module.md#ansible-collections-community-aws-elasticache-parameter-group-module) – Manage cache parameter groups in Amazon ElastiCache.
- [elasticache_snapshot module](elasticache_snapshot_module.md#ansible-collections-community-aws-elasticache-snapshot-module) – Manage cache snapshots in Amazon ElastiCache
- [elasticache_subnet_group module](elasticache_subnet_group_module.md#ansible-collections-community-aws-elasticache-subnet-group-module) – manage ElastiCache subnet groups
- [elasticbeanstalk_app module](elasticbeanstalk_app_module.md#ansible-collections-community-aws-elasticbeanstalk-app-module) – Create, update, and delete an Elastic Beanstalk application
- [elb_classic_lb_info module](elb_classic_lb_info_module.md#ansible-collections-community-aws-elb-classic-lb-info-module) – Gather information about EC2 Elastic Load Balancers in AWS
- [elb_instance module](elb_instance_module.md#ansible-collections-community-aws-elb-instance-module) – De-registers or registers instances from EC2 ELBs
- [elb_network_lb module](elb_network_lb_module.md#ansible-collections-community-aws-elb-network-lb-module) – Manage a Network Load Balancer
- [elb_target module](elb_target_module.md#ansible-collections-community-aws-elb-target-module) – Manage a target in a target group
- [elb_target_group module](elb_target_group_module.md#ansible-collections-community-aws-elb-target-group-module) – Manage a target group for an Application or Network load balancer
- [elb_target_group_info module](elb_target_group_info_module.md#ansible-collections-community-aws-elb-target-group-info-module) – Gather information about ELB target groups in AWS
- [elb_target_info module](elb_target_info_module.md#ansible-collections-community-aws-elb-target-info-module) – Gathers which target groups a target is associated with.
- [glue_connection module](glue_connection_module.md#ansible-collections-community-aws-glue-connection-module) – Manage an AWS Glue connection
- [glue_crawler module](glue_crawler_module.md#ansible-collections-community-aws-glue-crawler-module) – Manage an AWS Glue crawler
- [glue_job module](glue_job_module.md#ansible-collections-community-aws-glue-job-module) – Manage an AWS Glue job
- [iam_access_key module](iam_access_key_module.md#ansible-collections-community-aws-iam-access-key-module) – Manage AWS IAM User access keys
- [iam_access_key_info module](iam_access_key_info_module.md#ansible-collections-community-aws-iam-access-key-info-module) – fetch information about AWS IAM User access keys
- [iam_group module](iam_group_module.md#ansible-collections-community-aws-iam-group-module) – Manage AWS IAM groups
- [iam_managed_policy module](iam_managed_policy_module.md#ansible-collections-community-aws-iam-managed-policy-module) – Manage User Managed IAM policies
- [iam_mfa_device_info module](iam_mfa_device_info_module.md#ansible-collections-community-aws-iam-mfa-device-info-module) – List the MFA (Multi-Factor Authentication) devices registered for a user
- [iam_password_policy module](iam_password_policy_module.md#ansible-collections-community-aws-iam-password-policy-module) – Update an IAM Password Policy
- [iam_role module](iam_role_module.md#ansible-collections-community-aws-iam-role-module) – Manage AWS IAM roles
- [iam_role_info module](iam_role_info_module.md#ansible-collections-community-aws-iam-role-info-module) – Gather information on IAM roles
- [iam_saml_federation module](iam_saml_federation_module.md#ansible-collections-community-aws-iam-saml-federation-module) – Maintain IAM SAML federation configuration.
- [iam_server_certificate module](iam_server_certificate_module.md#ansible-collections-community-aws-iam-server-certificate-module) – Manage IAM server certificates for use on ELBs and CloudFront
- [iam_server_certificate_info module](iam_server_certificate_info_module.md#ansible-collections-community-aws-iam-server-certificate-info-module) – Retrieve the information of a server certificate
- [inspector_target module](inspector_target_module.md#ansible-collections-community-aws-inspector-target-module) – Create, Update and Delete Amazon Inspector Assessment Targets
- [kinesis_stream module](kinesis_stream_module.md#ansible-collections-community-aws-kinesis-stream-module) – Manage a Kinesis Stream.
- [lightsail module](lightsail_module.md#ansible-collections-community-aws-lightsail-module) – Manage instances in AWS Lightsail
- [lightsail_snapshot module](lightsail_snapshot_module.md#ansible-collections-community-aws-lightsail-snapshot-module) – Creates snapshots of AWS Lightsail instances
- [lightsail_static_ip module](lightsail_static_ip_module.md#ansible-collections-community-aws-lightsail-static-ip-module) – Manage static IP addresses in AWS Lightsail
- [mq_broker module](mq_broker_module.md#ansible-collections-community-aws-mq-broker-module) – MQ broker management
- [mq_broker_config module](mq_broker_config_module.md#ansible-collections-community-aws-mq-broker-config-module) – Update Amazon MQ broker configuration
- [mq_broker_info module](mq_broker_info_module.md#ansible-collections-community-aws-mq-broker-info-module) – Retrieve MQ Broker details
- [mq_user module](mq_user_module.md#ansible-collections-community-aws-mq-user-module) – Manage users in existing Amazon MQ broker
- [mq_user_info module](mq_user_info_module.md#ansible-collections-community-aws-mq-user-info-module) – List users of an Amazon MQ broker
- [msk_cluster module](msk_cluster_module.md#ansible-collections-community-aws-msk-cluster-module) – Manage Amazon MSK clusters
- [msk_config module](msk_config_module.md#ansible-collections-community-aws-msk-config-module) – Manage Amazon MSK cluster configurations
- [networkfirewall module](networkfirewall_module.md#ansible-collections-community-aws-networkfirewall-module) – manage AWS Network Firewall firewalls
- [networkfirewall_info module](networkfirewall_info_module.md#ansible-collections-community-aws-networkfirewall-info-module) – describe AWS Network Firewall firewalls
- [networkfirewall_policy module](networkfirewall_policy_module.md#ansible-collections-community-aws-networkfirewall-policy-module) – manage AWS Network Firewall policies
- [networkfirewall_policy_info module](networkfirewall_policy_info_module.md#ansible-collections-community-aws-networkfirewall-policy-info-module) – describe AWS Network Firewall policies
- [networkfirewall_rule_group module](networkfirewall_rule_group_module.md#ansible-collections-community-aws-networkfirewall-rule-group-module) – create, delete and modify AWS Network Firewall rule groups
- [networkfirewall_rule_group_info module](networkfirewall_rule_group_info_module.md#ansible-collections-community-aws-networkfirewall-rule-group-info-module) – describe AWS Network Firewall rule groups
- [opensearch module](opensearch_module.md#ansible-collections-community-aws-opensearch-module) – Creates OpenSearch or ElasticSearch domain
- [opensearch_info module](opensearch_info_module.md#ansible-collections-community-aws-opensearch-info-module) – obtain information about one or more OpenSearch or ElasticSearch domain
- [redshift module](redshift_module.md#ansible-collections-community-aws-redshift-module) – create, delete, or modify an Amazon Redshift instance
- [redshift_cross_region_snapshots module](redshift_cross_region_snapshots_module.md#ansible-collections-community-aws-redshift-cross-region-snapshots-module) – Manage Redshift Cross Region Snapshots
- [redshift_info module](redshift_info_module.md#ansible-collections-community-aws-redshift-info-module) – Gather information about Redshift cluster(s)
- [redshift_subnet_group module](redshift_subnet_group_module.md#ansible-collections-community-aws-redshift-subnet-group-module) – manage Redshift cluster subnet groups
- [route53_wait module](route53_wait_module.md#ansible-collections-community-aws-route53-wait-module) – wait for changes in Amazons Route 53 DNS service to propagate
- [s3_bucket_info module](s3_bucket_info_module.md#ansible-collections-community-aws-s3-bucket-info-module) – Lists S3 buckets in AWS
- [s3_bucket_notification module](s3_bucket_notification_module.md#ansible-collections-community-aws-s3-bucket-notification-module) – Creates, updates or deletes S3 Bucket notifications targeting Lambda functions, SNS or SQS.
- [s3_cors module](s3_cors_module.md#ansible-collections-community-aws-s3-cors-module) – Manage CORS for S3 buckets in AWS
- [s3_lifecycle module](s3_lifecycle_module.md#ansible-collections-community-aws-s3-lifecycle-module) – Manage S3 bucket lifecycle rules in AWS
- [s3_logging module](s3_logging_module.md#ansible-collections-community-aws-s3-logging-module) – Manage logging facility of an s3 bucket in AWS
- [s3_metrics_configuration module](s3_metrics_configuration_module.md#ansible-collections-community-aws-s3-metrics-configuration-module) – Manage s3 bucket metrics configuration in AWS
- [s3_sync module](s3_sync_module.md#ansible-collections-community-aws-s3-sync-module) – Efficiently upload multiple files to S3
- [s3_website module](s3_website_module.md#ansible-collections-community-aws-s3-website-module) – Configure an s3 bucket as a website
- [secretsmanager_secret module](secretsmanager_secret_module.md#ansible-collections-community-aws-secretsmanager-secret-module) – Manage secrets stored in AWS Secrets Manager
- [ses_identity module](ses_identity_module.md#ansible-collections-community-aws-ses-identity-module) – Manages SES email and domain identity
- [ses_identity_policy module](ses_identity_policy_module.md#ansible-collections-community-aws-ses-identity-policy-module) – Manages SES sending authorization policies
- [ses_rule_set module](ses_rule_set_module.md#ansible-collections-community-aws-ses-rule-set-module) – Manages SES inbound receipt rule sets
- [sns module](sns_module.md#ansible-collections-community-aws-sns-module) – Send Amazon Simple Notification Service messages
- [sns_topic module](sns_topic_module.md#ansible-collections-community-aws-sns-topic-module) – Manages AWS SNS topics and subscriptions
- [sns_topic_info module](sns_topic_info_module.md#ansible-collections-community-aws-sns-topic-info-module) – sns_topic_info module
- [sqs_queue module](sqs_queue_module.md#ansible-collections-community-aws-sqs-queue-module) – Creates or deletes AWS SQS queues
- [ssm_inventory_info module](ssm_inventory_info_module.md#ansible-collections-community-aws-ssm-inventory-info-module) – Get SSM inventory information for EC2 instance
- [ssm_parameter module](ssm_parameter_module.md#ansible-collections-community-aws-ssm-parameter-module) – Manage key-value pairs in AWS Systems Manager Parameter Store
- [stepfunctions_state_machine module](stepfunctions_state_machine_module.md#ansible-collections-community-aws-stepfunctions-state-machine-module) – Manage AWS Step Functions state machines
- [stepfunctions_state_machine_execution module](stepfunctions_state_machine_execution_module.md#ansible-collections-community-aws-stepfunctions-state-machine-execution-module) – Start or stop execution of an AWS Step Functions state machine
- [storagegateway_info module](storagegateway_info_module.md#ansible-collections-community-aws-storagegateway-info-module) – Fetch AWS Storage Gateway information
- [sts_assume_role module](sts_assume_role_module.md#ansible-collections-community-aws-sts-assume-role-module) – Assume a role using AWS Security Token Service and obtain temporary credentials
- [sts_session_token module](sts_session_token_module.md#ansible-collections-community-aws-sts-session-token-module) – obtain a session token from the AWS Security Token Service
- [waf_condition module](waf_condition_module.md#ansible-collections-community-aws-waf-condition-module) – Create and delete WAF Conditions
- [waf_info module](waf_info_module.md#ansible-collections-community-aws-waf-info-module) – Retrieve information for WAF ACLs, Rules, Conditions and Filters
- [waf_rule module](waf_rule_module.md#ansible-collections-community-aws-waf-rule-module) – Create and delete WAF Rules
- [waf_web_acl module](waf_web_acl_module.md#ansible-collections-community-aws-waf-web-acl-module) – Create and delete WAF Web ACLs
- [wafv2_ip_set module](wafv2_ip_set_module.md#ansible-collections-community-aws-wafv2-ip-set-module) – wafv2_ip_set
- [wafv2_ip_set_info module](wafv2_ip_set_info_module.md#ansible-collections-community-aws-wafv2-ip-set-info-module) – Get information about wafv2 ip sets
- [wafv2_resources module](wafv2_resources_module.md#ansible-collections-community-aws-wafv2-resources-module) – wafv2_web_acl
- [wafv2_resources_info module](wafv2_resources_info_module.md#ansible-collections-community-aws-wafv2-resources-info-module) – wafv2_resources_info
- [wafv2_rule_group module](wafv2_rule_group_module.md#ansible-collections-community-aws-wafv2-rule-group-module) – wafv2_web_acl
- [wafv2_rule_group_info module](wafv2_rule_group_info_module.md#ansible-collections-community-aws-wafv2-rule-group-info-module) – wafv2_web_acl_info
- [wafv2_web_acl module](wafv2_web_acl_module.md#ansible-collections-community-aws-wafv2-web-acl-module) – Create and delete WAF Web ACLs
- [wafv2_web_acl_info module](wafv2_web_acl_info_module.md#ansible-collections-community-aws-wafv2-web-acl-info-module) – wafv2_web_acl

### Connection Plugins

- [aws_ssm connection](aws_ssm_connection.md#ansible-collections-community-aws-aws-ssm-connection) – connect to EC2 instances via AWS Systems Manager

### Inventory Plugins

- [aws_mq inventory](aws_mq_inventory.md#ansible-collections-community-aws-aws-mq-inventory) – MQ broker inventory source

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
