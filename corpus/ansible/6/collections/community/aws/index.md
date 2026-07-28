---
collection: ansible
version: "6"
title: "Community.Aws"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/
fetched_at: 2026-07-28T00:24:41+00:00
---
# Community.Aws

Collection version 3.6.0

- [Description](index.md#description)
- [Communication](index.md#communication)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

**Author:**

- Ansible (<https://github.com/ansible>)

**Supported ansible-core versions:**

- 2.9.10 or newer

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)

## [Communication](index.md#id2)

- Matrix room `#aws:ansible.im`: [General usage and support questions](https://matrix.to/#/#aws:ansible.im).
- IRC channel `#ansible-aws` (Libera network):
  [General usage and support questions](https://web.libera.chat/?channel=#ansible-aws).

## [Plugin Index](index.md#id3)

These are the plugins in the community.aws collection:

### Modules

- [aws_acm module](aws_acm_module.md#ansible-collections-community-aws-aws-acm-module) – Upload and delete certificates in the AWS Certificate Manager service
- [aws_acm_info module](aws_acm_info_module.md#ansible-collections-community-aws-aws-acm-info-module) – Retrieve certificate information from AWS Certificate Manager service
- [aws_api_gateway module](aws_api_gateway_module.md#ansible-collections-community-aws-aws-api-gateway-module) – Manage AWS API Gateway APIs
- [aws_api_gateway_domain module](aws_api_gateway_domain_module.md#ansible-collections-community-aws-aws-api-gateway-domain-module) – Manage AWS API Gateway custom domains
- [aws_application_scaling_policy module](aws_application_scaling_policy_module.md#ansible-collections-community-aws-aws-application-scaling-policy-module) – Manage Application Auto Scaling Scaling Policies
- [aws_batch_compute_environment module](aws_batch_compute_environment_module.md#ansible-collections-community-aws-aws-batch-compute-environment-module) – Manage AWS Batch Compute Environments
- [aws_batch_job_definition module](aws_batch_job_definition_module.md#ansible-collections-community-aws-aws-batch-job-definition-module) – Manage AWS Batch Job Definitions
- [aws_batch_job_queue module](aws_batch_job_queue_module.md#ansible-collections-community-aws-aws-batch-job-queue-module) – Manage AWS Batch Job Queues
- [aws_codebuild module](aws_codebuild_module.md#ansible-collections-community-aws-aws-codebuild-module) – Create or delete an AWS CodeBuild project
- [aws_codecommit module](aws_codecommit_module.md#ansible-collections-community-aws-aws-codecommit-module) – Manage repositories in AWS CodeCommit
- [aws_codepipeline module](aws_codepipeline_module.md#ansible-collections-community-aws-aws-codepipeline-module) – Create or delete AWS CodePipelines
- [aws_config_aggregation_authorization module](aws_config_aggregation_authorization_module.md#ansible-collections-community-aws-aws-config-aggregation-authorization-module) – Manage cross-account AWS Config authorizations
- [aws_config_aggregator module](aws_config_aggregator_module.md#ansible-collections-community-aws-aws-config-aggregator-module) – Manage AWS Config aggregations across multiple accounts
- [aws_config_delivery_channel module](aws_config_delivery_channel_module.md#ansible-collections-community-aws-aws-config-delivery-channel-module) – Manage AWS Config delivery channels
- [aws_config_recorder module](aws_config_recorder_module.md#ansible-collections-community-aws-aws-config-recorder-module) – Manage AWS Config Recorders
- [aws_config_rule module](aws_config_rule_module.md#ansible-collections-community-aws-aws-config-rule-module) – Manage AWS Config resources
- [aws_direct_connect_confirm_connection module](aws_direct_connect_confirm_connection_module.md#ansible-collections-community-aws-aws-direct-connect-confirm-connection-module) – Confirms the creation of a hosted DirectConnect connection.
- [aws_direct_connect_connection module](aws_direct_connect_connection_module.md#ansible-collections-community-aws-aws-direct-connect-connection-module) – Creates, deletes, modifies a DirectConnect connection
- [aws_direct_connect_gateway module](aws_direct_connect_gateway_module.md#ansible-collections-community-aws-aws-direct-connect-gateway-module) – Manage AWS Direct Connect gateway
- [aws_direct_connect_link_aggregation_group module](aws_direct_connect_link_aggregation_group_module.md#ansible-collections-community-aws-aws-direct-connect-link-aggregation-group-module) – Manage Direct Connect LAG bundles
- [aws_direct_connect_virtual_interface module](aws_direct_connect_virtual_interface_module.md#ansible-collections-community-aws-aws-direct-connect-virtual-interface-module) – Manage Direct Connect virtual interfaces
- [aws_eks_cluster module](aws_eks_cluster_module.md#ansible-collections-community-aws-aws-eks-cluster-module) – Manage Elastic Kubernetes Service Clusters
- [aws_elasticbeanstalk_app module](aws_elasticbeanstalk_app_module.md#ansible-collections-community-aws-aws-elasticbeanstalk-app-module) – Create, update, and delete an elastic beanstalk application
- [aws_glue_connection module](aws_glue_connection_module.md#ansible-collections-community-aws-aws-glue-connection-module) – Manage an AWS Glue connection
- [aws_glue_job module](aws_glue_job_module.md#ansible-collections-community-aws-aws-glue-job-module) – Manage an AWS Glue job
- [aws_inspector_target module](aws_inspector_target_module.md#ansible-collections-community-aws-aws-inspector-target-module) – Create, Update and Delete Amazon Inspector Assessment Targets
- [aws_kms module](aws_kms_module.md#ansible-collections-community-aws-aws-kms-module) – Perform various KMS management tasks.
- [aws_kms_info module](aws_kms_info_module.md#ansible-collections-community-aws-aws-kms-info-module) – Gather information about AWS KMS keys
- [aws_msk_cluster module](aws_msk_cluster_module.md#ansible-collections-community-aws-aws-msk-cluster-module) – Manage Amazon MSK clusters.
- [aws_msk_config module](aws_msk_config_module.md#ansible-collections-community-aws-aws-msk-config-module) – Manage Amazon MSK cluster configurations.
- [aws_region_info module](aws_region_info_module.md#ansible-collections-community-aws-aws-region-info-module) – Gather information about AWS regions.
- [aws_s3_bucket_info module](aws_s3_bucket_info_module.md#ansible-collections-community-aws-aws-s3-bucket-info-module) – lists S3 buckets in AWS
- [aws_s3_cors module](aws_s3_cors_module.md#ansible-collections-community-aws-aws-s3-cors-module) – Manage CORS for S3 buckets in AWS
- [aws_secret module](aws_secret_module.md#ansible-collections-community-aws-aws-secret-module) – Manage secrets stored in AWS Secrets Manager.
- [aws_ses_identity module](aws_ses_identity_module.md#ansible-collections-community-aws-aws-ses-identity-module) – Manages SES email and domain identity
- [aws_ses_identity_policy module](aws_ses_identity_policy_module.md#ansible-collections-community-aws-aws-ses-identity-policy-module) – Manages SES sending authorization policies
- [aws_ses_rule_set module](aws_ses_rule_set_module.md#ansible-collections-community-aws-aws-ses-rule-set-module) – Manages SES inbound receipt rule sets
- [aws_sgw_info module](aws_sgw_info_module.md#ansible-collections-community-aws-aws-sgw-info-module) – Fetch AWS Storage Gateway information
- [aws_ssm_parameter_store module](aws_ssm_parameter_store_module.md#ansible-collections-community-aws-aws-ssm-parameter-store-module) – Manage key-value pairs in aws parameter store.
- [aws_step_functions_state_machine module](aws_step_functions_state_machine_module.md#ansible-collections-community-aws-aws-step-functions-state-machine-module) – Manage AWS Step Functions state machines
- [aws_step_functions_state_machine_execution module](aws_step_functions_state_machine_execution_module.md#ansible-collections-community-aws-aws-step-functions-state-machine-execution-module) – Start or stop execution of an AWS Step Functions state machine.
- [aws_waf_condition module](aws_waf_condition_module.md#ansible-collections-community-aws-aws-waf-condition-module) – Create and delete WAF Conditions
- [aws_waf_info module](aws_waf_info_module.md#ansible-collections-community-aws-aws-waf-info-module) – Retrieve information for WAF ACLs, Rule , Conditions and Filters.
- [aws_waf_rule module](aws_waf_rule_module.md#ansible-collections-community-aws-aws-waf-rule-module) – Create and delete WAF Rules
- [aws_waf_web_acl module](aws_waf_web_acl_module.md#ansible-collections-community-aws-aws-waf-web-acl-module) – Create and delete WAF Web ACLs
- [cloudformation_exports_info module](cloudformation_exports_info_module.md#ansible-collections-community-aws-cloudformation-exports-info-module) – Read a value from CloudFormation Exports
- [cloudformation_stack_set module](cloudformation_stack_set_module.md#ansible-collections-community-aws-cloudformation-stack-set-module) – Manage groups of CloudFormation stacks
- [cloudfront_distribution module](cloudfront_distribution_module.md#ansible-collections-community-aws-cloudfront-distribution-module) – Create, update and delete AWS CloudFront distributions.
- [cloudfront_info module](cloudfront_info_module.md#ansible-collections-community-aws-cloudfront-info-module) – Obtain facts about an AWS CloudFront distribution
- [cloudfront_invalidation module](cloudfront_invalidation_module.md#ansible-collections-community-aws-cloudfront-invalidation-module) – create invalidations for AWS CloudFront distributions
- [cloudfront_origin_access_identity module](cloudfront_origin_access_identity_module.md#ansible-collections-community-aws-cloudfront-origin-access-identity-module) – Create, update and delete origin access identities for a CloudFront distribution
- [cloudfront_response_headers_policy module](cloudfront_response_headers_policy_module.md#ansible-collections-community-aws-cloudfront-response-headers-policy-module) – Create, update and delete response headers policies to be used in a Cloudfront distribution
- [cloudtrail module](cloudtrail_module.md#ansible-collections-community-aws-cloudtrail-module) – manage CloudTrail create, delete, update
- [cloudwatchevent_rule module](cloudwatchevent_rule_module.md#ansible-collections-community-aws-cloudwatchevent-rule-module) – Manage CloudWatch Event rules and targets
- [cloudwatchlogs_log_group module](cloudwatchlogs_log_group_module.md#ansible-collections-community-aws-cloudwatchlogs-log-group-module) – create or delete log_group in CloudWatchLogs
- [cloudwatchlogs_log_group_info module](cloudwatchlogs_log_group_info_module.md#ansible-collections-community-aws-cloudwatchlogs-log-group-info-module) – Get information about log_group in CloudWatchLogs
- [cloudwatchlogs_log_group_metric_filter module](cloudwatchlogs_log_group_metric_filter_module.md#ansible-collections-community-aws-cloudwatchlogs-log-group-metric-filter-module) – Manage CloudWatch log group metric filter
- [data_pipeline module](data_pipeline_module.md#ansible-collections-community-aws-data-pipeline-module) – Create and manage AWS Datapipelines
- [dms_endpoint module](dms_endpoint_module.md#ansible-collections-community-aws-dms-endpoint-module) – Creates or destroys a data migration services endpoint
- [dms_replication_subnet_group module](dms_replication_subnet_group_module.md#ansible-collections-community-aws-dms-replication-subnet-group-module) – creates or destroys a data migration services subnet group
- [dynamodb_table module](dynamodb_table_module.md#ansible-collections-community-aws-dynamodb-table-module) – Create, update or delete AWS Dynamo DB tables
- [dynamodb_ttl module](dynamodb_ttl_module.md#ansible-collections-community-aws-dynamodb-ttl-module) – Set TTL for a given DynamoDB table
- [ec2_ami_copy module](ec2_ami_copy_module.md#ansible-collections-community-aws-ec2-ami-copy-module) – copies AMI between AWS regions, return new image id
- [ec2_asg module](ec2_asg_module.md#ansible-collections-community-aws-ec2-asg-module) – Create or delete AWS AutoScaling Groups (ASGs)
- [ec2_asg_info module](ec2_asg_info_module.md#ansible-collections-community-aws-ec2-asg-info-module) – Gather information about ec2 Auto Scaling Groups (ASGs) in AWS
- [ec2_asg_instance_refresh module](ec2_asg_instance_refresh_module.md#ansible-collections-community-aws-ec2-asg-instance-refresh-module) – Start or cancel an EC2 Auto Scaling Group (ASG) instance refresh in AWS
- [ec2_asg_instance_refresh_info module](ec2_asg_instance_refresh_info_module.md#ansible-collections-community-aws-ec2-asg-instance-refresh-info-module) – Gather information about ec2 Auto Scaling Group (ASG) Instance Refreshes in AWS
- [ec2_asg_lifecycle_hook module](ec2_asg_lifecycle_hook_module.md#ansible-collections-community-aws-ec2-asg-lifecycle-hook-module) – Create, delete or update AWS ASG Lifecycle Hooks.
- [ec2_asg_scheduled_action module](ec2_asg_scheduled_action_module.md#ansible-collections-community-aws-ec2-asg-scheduled-action-module) – Create, modify and delete ASG scheduled scaling actions.
- [ec2_customer_gateway module](ec2_customer_gateway_module.md#ansible-collections-community-aws-ec2-customer-gateway-module) – Manage an AWS customer gateway
- [ec2_customer_gateway_info module](ec2_customer_gateway_info_module.md#ansible-collections-community-aws-ec2-customer-gateway-info-module) – Gather information about customer gateways in AWS
- [ec2_eip module](ec2_eip_module.md#ansible-collections-community-aws-ec2-eip-module) – manages EC2 elastic IP (EIP) addresses.
- [ec2_eip_info module](ec2_eip_info_module.md#ansible-collections-community-aws-ec2-eip-info-module) – List EC2 EIP details
- [ec2_launch_template module](ec2_launch_template_module.md#ansible-collections-community-aws-ec2-launch-template-module) – Manage EC2 launch templates
- [ec2_lc module](ec2_lc_module.md#ansible-collections-community-aws-ec2-lc-module) – Create or delete AWS Autoscaling Launch Configurations
- [ec2_lc_find module](ec2_lc_find_module.md#ansible-collections-community-aws-ec2-lc-find-module) – Find AWS Autoscaling Launch Configurations
- [ec2_lc_info module](ec2_lc_info_module.md#ansible-collections-community-aws-ec2-lc-info-module) – Gather information about AWS Autoscaling Launch Configurations.
- [ec2_metric_alarm module](ec2_metric_alarm_module.md#ansible-collections-community-aws-ec2-metric-alarm-module) – Create/update or delete AWS Cloudwatch ‘metric alarms’
- [ec2_placement_group module](ec2_placement_group_module.md#ansible-collections-community-aws-ec2-placement-group-module) – Create or delete an EC2 Placement Group
- [ec2_placement_group_info module](ec2_placement_group_info_module.md#ansible-collections-community-aws-ec2-placement-group-info-module) – List EC2 Placement Group(s) details
- [ec2_scaling_policy module](ec2_scaling_policy_module.md#ansible-collections-community-aws-ec2-scaling-policy-module) – Create or delete AWS scaling policies for Autoscaling groups
- [ec2_snapshot_copy module](ec2_snapshot_copy_module.md#ansible-collections-community-aws-ec2-snapshot-copy-module) – Copies an EC2 snapshot and returns the new Snapshot ID.
- [ec2_transit_gateway module](ec2_transit_gateway_module.md#ansible-collections-community-aws-ec2-transit-gateway-module) – Create and delete AWS Transit Gateways
- [ec2_transit_gateway_info module](ec2_transit_gateway_info_module.md#ansible-collections-community-aws-ec2-transit-gateway-info-module) – Gather information about ec2 transit gateways in AWS
- [ec2_vpc_egress_igw module](ec2_vpc_egress_igw_module.md#ansible-collections-community-aws-ec2-vpc-egress-igw-module) – Manage an AWS VPC Egress Only Internet gateway
- [ec2_vpc_nacl module](ec2_vpc_nacl_module.md#ansible-collections-community-aws-ec2-vpc-nacl-module) – create and delete Network ACLs.
- [ec2_vpc_nacl_info module](ec2_vpc_nacl_info_module.md#ansible-collections-community-aws-ec2-vpc-nacl-info-module) – Gather information about Network ACLs in an AWS VPC
- [ec2_vpc_peer module](ec2_vpc_peer_module.md#ansible-collections-community-aws-ec2-vpc-peer-module) – create, delete, accept, and reject VPC peering connections between two VPCs.
- [ec2_vpc_peering_info module](ec2_vpc_peering_info_module.md#ansible-collections-community-aws-ec2-vpc-peering-info-module) – Retrieves AWS VPC Peering details using AWS methods.
- [ec2_vpc_route_table module](ec2_vpc_route_table_module.md#ansible-collections-community-aws-ec2-vpc-route-table-module) – Manage route tables for AWS virtual private clouds
- [ec2_vpc_route_table_info module](ec2_vpc_route_table_info_module.md#ansible-collections-community-aws-ec2-vpc-route-table-info-module) – Gather information about ec2 VPC route tables in AWS
- [ec2_vpc_vgw module](ec2_vpc_vgw_module.md#ansible-collections-community-aws-ec2-vpc-vgw-module) – Create and delete AWS VPN Virtual Gateways.
- [ec2_vpc_vgw_info module](ec2_vpc_vgw_info_module.md#ansible-collections-community-aws-ec2-vpc-vgw-info-module) – Gather information about virtual gateways in AWS
- [ec2_vpc_vpn module](ec2_vpc_vpn_module.md#ansible-collections-community-aws-ec2-vpc-vpn-module) – Create, modify, and delete EC2 VPN connections.
- [ec2_vpc_vpn_info module](ec2_vpc_vpn_info_module.md#ansible-collections-community-aws-ec2-vpc-vpn-info-module) – Gather information about VPN Connections in AWS.
- [ec2_win_password module](ec2_win_password_module.md#ansible-collections-community-aws-ec2-win-password-module) – Gets the default administrator password for EC2 Windows instances
- [ecs_attribute module](ecs_attribute_module.md#ansible-collections-community-aws-ecs-attribute-module) – manage ecs attributes
- [ecs_cluster module](ecs_cluster_module.md#ansible-collections-community-aws-ecs-cluster-module) – Create or terminate ECS clusters.
- [ecs_ecr module](ecs_ecr_module.md#ansible-collections-community-aws-ecs-ecr-module) – Manage Elastic Container Registry repositories
- [ecs_service module](ecs_service_module.md#ansible-collections-community-aws-ecs-service-module) – Create, terminate, start or stop a service in ECS
- [ecs_service_info module](ecs_service_info_module.md#ansible-collections-community-aws-ecs-service-info-module) – List or describe services in ECS
- [ecs_tag module](ecs_tag_module.md#ansible-collections-community-aws-ecs-tag-module) – create and remove tags on Amazon ECS resources
- [ecs_task module](ecs_task_module.md#ansible-collections-community-aws-ecs-task-module) – Run, start or stop a task in ecs
- [ecs_taskdefinition module](ecs_taskdefinition_module.md#ansible-collections-community-aws-ecs-taskdefinition-module) – register a task definition in ecs
- [ecs_taskdefinition_info module](ecs_taskdefinition_info_module.md#ansible-collections-community-aws-ecs-taskdefinition-info-module) – Describe a task definition in ECS
- [efs module](efs_module.md#ansible-collections-community-aws-efs-module) – create and maintain EFS file systems
- [efs_info module](efs_info_module.md#ansible-collections-community-aws-efs-info-module) – Get information about Amazon EFS file systems
- [efs_tag module](efs_tag_module.md#ansible-collections-community-aws-efs-tag-module) – create and remove tags on Amazon EFS resources
- [elasticache module](elasticache_module.md#ansible-collections-community-aws-elasticache-module) – Manage cache clusters in Amazon ElastiCache
- [elasticache_info module](elasticache_info_module.md#ansible-collections-community-aws-elasticache-info-module) – Retrieve information for AWS ElastiCache clusters
- [elasticache_parameter_group module](elasticache_parameter_group_module.md#ansible-collections-community-aws-elasticache-parameter-group-module) – Manage cache parameter groups in Amazon ElastiCache.
- [elasticache_snapshot module](elasticache_snapshot_module.md#ansible-collections-community-aws-elasticache-snapshot-module) – Manage cache snapshots in Amazon ElastiCache
- [elasticache_subnet_group module](elasticache_subnet_group_module.md#ansible-collections-community-aws-elasticache-subnet-group-module) – manage ElastiCache subnet groups
- [elb_application_lb module](elb_application_lb_module.md#ansible-collections-community-aws-elb-application-lb-module) – Manage an Application Load Balancer
- [elb_application_lb_info module](elb_application_lb_info_module.md#ansible-collections-community-aws-elb-application-lb-info-module) – Gather information about Application Load Balancers in AWS
- [elb_classic_lb_info module](elb_classic_lb_info_module.md#ansible-collections-community-aws-elb-classic-lb-info-module) – Gather information about EC2 Elastic Load Balancers in AWS
- [elb_instance module](elb_instance_module.md#ansible-collections-community-aws-elb-instance-module) – De-registers or registers instances from EC2 ELBs
- [elb_network_lb module](elb_network_lb_module.md#ansible-collections-community-aws-elb-network-lb-module) – Manage a Network Load Balancer
- [elb_target module](elb_target_module.md#ansible-collections-community-aws-elb-target-module) – Manage a target in a target group
- [elb_target_group module](elb_target_group_module.md#ansible-collections-community-aws-elb-target-group-module) – Manage a target group for an Application or Network load balancer
- [elb_target_group_info module](elb_target_group_info_module.md#ansible-collections-community-aws-elb-target-group-info-module) – Gather information about ELB target groups in AWS
- [elb_target_info module](elb_target_info_module.md#ansible-collections-community-aws-elb-target-info-module) – Gathers which target groups a target is associated with.
- [execute_lambda module](execute_lambda_module.md#ansible-collections-community-aws-execute-lambda-module) – Execute an AWS Lambda function
- [iam_access_key module](iam_access_key_module.md#ansible-collections-community-aws-iam-access-key-module) – Manage AWS IAM User access keys
- [iam_access_key_info module](iam_access_key_info_module.md#ansible-collections-community-aws-iam-access-key-info-module) – fetch information about AWS IAM User access keys
- [iam_group module](iam_group_module.md#ansible-collections-community-aws-iam-group-module) – Manage AWS IAM groups
- [iam_managed_policy module](iam_managed_policy_module.md#ansible-collections-community-aws-iam-managed-policy-module) – Manage User Managed IAM policies
- [iam_mfa_device_info module](iam_mfa_device_info_module.md#ansible-collections-community-aws-iam-mfa-device-info-module) – List the MFA (Multi-Factor Authentication) devices registered for a user
- [iam_password_policy module](iam_password_policy_module.md#ansible-collections-community-aws-iam-password-policy-module) – Update an IAM Password Policy
- [iam_policy module](iam_policy_module.md#ansible-collections-community-aws-iam-policy-module) – Manage inline IAM policies for users, groups, and roles
- [iam_policy_info module](iam_policy_info_module.md#ansible-collections-community-aws-iam-policy-info-module) – Retrieve inline IAM policies for users, groups, and roles
- [iam_role module](iam_role_module.md#ansible-collections-community-aws-iam-role-module) – Manage AWS IAM roles
- [iam_role_info module](iam_role_info_module.md#ansible-collections-community-aws-iam-role-info-module) – Gather information on IAM roles
- [iam_saml_federation module](iam_saml_federation_module.md#ansible-collections-community-aws-iam-saml-federation-module) – Maintain IAM SAML federation configuration.
- [iam_server_certificate module](iam_server_certificate_module.md#ansible-collections-community-aws-iam-server-certificate-module) – Manage server certificates for use on ELBs and CloudFront
- [iam_server_certificate_info module](iam_server_certificate_info_module.md#ansible-collections-community-aws-iam-server-certificate-info-module) – Retrieve the information of a server certificate
- [iam_user module](iam_user_module.md#ansible-collections-community-aws-iam-user-module) – Manage AWS IAM users
- [iam_user_info module](iam_user_info_module.md#ansible-collections-community-aws-iam-user-info-module) – Gather IAM user(s) facts in AWS
- [kinesis_stream module](kinesis_stream_module.md#ansible-collections-community-aws-kinesis-stream-module) – Manage a Kinesis Stream.
- [lambda module](lambda_module.md#ansible-collections-community-aws-lambda-module) – Manage AWS Lambda functions
- [lambda_alias module](lambda_alias_module.md#ansible-collections-community-aws-lambda-alias-module) – Creates, updates or deletes AWS Lambda function aliases
- [lambda_event module](lambda_event_module.md#ansible-collections-community-aws-lambda-event-module) – Creates, updates or deletes AWS Lambda function event mappings
- [lambda_info module](lambda_info_module.md#ansible-collections-community-aws-lambda-info-module) – Gathers AWS Lambda function details
- [lambda_policy module](lambda_policy_module.md#ansible-collections-community-aws-lambda-policy-module) – Creates, updates or deletes AWS Lambda policy statements.
- [lightsail module](lightsail_module.md#ansible-collections-community-aws-lightsail-module) – Manage instances in AWS Lightsail
- [rds_cluster module](rds_cluster_module.md#ansible-collections-community-aws-rds-cluster-module) – rds_cluster module
- [rds_cluster_info module](rds_cluster_info_module.md#ansible-collections-community-aws-rds-cluster-info-module) – Obtain information about one or more RDS clusters
- [rds_instance module](rds_instance_module.md#ansible-collections-community-aws-rds-instance-module) – Manage RDS instances
- [rds_instance_info module](rds_instance_info_module.md#ansible-collections-community-aws-rds-instance-info-module) – obtain information about one or more RDS instances
- [rds_instance_snapshot module](rds_instance_snapshot_module.md#ansible-collections-community-aws-rds-instance-snapshot-module) – Manage Amazon RDS instance snapshots
- [rds_option_group module](rds_option_group_module.md#ansible-collections-community-aws-rds-option-group-module) – rds_option_group module
- [rds_option_group_info module](rds_option_group_info_module.md#ansible-collections-community-aws-rds-option-group-info-module) – rds_option_group_info module
- [rds_param_group module](rds_param_group_module.md#ansible-collections-community-aws-rds-param-group-module) – manage RDS parameter groups
- [rds_snapshot_info module](rds_snapshot_info_module.md#ansible-collections-community-aws-rds-snapshot-info-module) – obtain information about one or more RDS snapshots
- [rds_subnet_group module](rds_subnet_group_module.md#ansible-collections-community-aws-rds-subnet-group-module) – manage RDS database subnet groups
- [redshift module](redshift_module.md#ansible-collections-community-aws-redshift-module) – create, delete, or modify an Amazon Redshift instance
- [redshift_cross_region_snapshots module](redshift_cross_region_snapshots_module.md#ansible-collections-community-aws-redshift-cross-region-snapshots-module) – Manage Redshift Cross Region Snapshots
- [redshift_info module](redshift_info_module.md#ansible-collections-community-aws-redshift-info-module) – Gather information about Redshift cluster(s)
- [redshift_subnet_group module](redshift_subnet_group_module.md#ansible-collections-community-aws-redshift-subnet-group-module) – manage Redshift cluster subnet groups
- [route53 module](route53_module.md#ansible-collections-community-aws-route53-module) – add or delete entries in Amazons Route 53 DNS service
- [route53_health_check module](route53_health_check_module.md#ansible-collections-community-aws-route53-health-check-module) – Manage health-checks in Amazons Route53 DNS service
- [route53_info module](route53_info_module.md#ansible-collections-community-aws-route53-info-module) – Retrieves route53 details using AWS methods
- [route53_zone module](route53_zone_module.md#ansible-collections-community-aws-route53-zone-module) – add or delete Route53 zones
- [s3_bucket_notification module](s3_bucket_notification_module.md#ansible-collections-community-aws-s3-bucket-notification-module) – Creates, updates or deletes S3 Bucket notifications targeting Lambda functions, SNS or SQS.
- [s3_lifecycle module](s3_lifecycle_module.md#ansible-collections-community-aws-s3-lifecycle-module) – Manage S3 bucket lifecycle rules in AWS
- [s3_logging module](s3_logging_module.md#ansible-collections-community-aws-s3-logging-module) – Manage logging facility of an s3 bucket in AWS
- [s3_metrics_configuration module](s3_metrics_configuration_module.md#ansible-collections-community-aws-s3-metrics-configuration-module) – Manage s3 bucket metrics configuration in AWS
- [s3_sync module](s3_sync_module.md#ansible-collections-community-aws-s3-sync-module) – Efficiently upload multiple files to S3
- [s3_website module](s3_website_module.md#ansible-collections-community-aws-s3-website-module) – Configure an s3 bucket as a website
- [sns module](sns_module.md#ansible-collections-community-aws-sns-module) – Send Amazon Simple Notification Service messages
- [sns_topic module](sns_topic_module.md#ansible-collections-community-aws-sns-topic-module) – Manages AWS SNS topics and subscriptions
- [sns_topic_info module](sns_topic_info_module.md#ansible-collections-community-aws-sns-topic-info-module) – sns_topic_info module
- [sqs_queue module](sqs_queue_module.md#ansible-collections-community-aws-sqs-queue-module) – Creates or deletes AWS SQS queues
- [sts_assume_role module](sts_assume_role_module.md#ansible-collections-community-aws-sts-assume-role-module) – Assume a role using AWS Security Token Service and obtain temporary credentials
- [sts_session_token module](sts_session_token_module.md#ansible-collections-community-aws-sts-session-token-module) – Obtain a session token from the AWS Security Token Service
- [wafv2_ip_set module](wafv2_ip_set_module.md#ansible-collections-community-aws-wafv2-ip-set-module) – wafv2_ip_set
- [wafv2_ip_set_info module](wafv2_ip_set_info_module.md#ansible-collections-community-aws-wafv2-ip-set-info-module) – Get information about wafv2 ip sets
- [wafv2_resources module](wafv2_resources_module.md#ansible-collections-community-aws-wafv2-resources-module) – wafv2_web_acl
- [wafv2_resources_info module](wafv2_resources_info_module.md#ansible-collections-community-aws-wafv2-resources-info-module) – wafv2_resources_info
- [wafv2_rule_group module](wafv2_rule_group_module.md#ansible-collections-community-aws-wafv2-rule-group-module) – wafv2_web_acl
- [wafv2_rule_group_info module](wafv2_rule_group_info_module.md#ansible-collections-community-aws-wafv2-rule-group-info-module) – wafv2_web_acl_info
- [wafv2_web_acl module](wafv2_web_acl_module.md#ansible-collections-community-aws-wafv2-web-acl-module) – Create and delete WAF Web ACLs
- [wafv2_web_acl_info module](wafv2_web_acl_info_module.md#ansible-collections-community-aws-wafv2-web-acl-info-module) – wafv2_web_acl

### Connection Plugins

- [aws_ssm connection](aws_ssm_connection.md#ansible-collections-community-aws-aws-ssm-connection) – execute via AWS Systems Manager

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
