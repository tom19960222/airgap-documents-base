---
collection: ansible
version: "8"
title: "community.aws.elb_target_info module – Gathers which target groups a target is associated with."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/elb_target_info_module.html
fetched_at: 2026-07-28T01:41:16+00:00
---
# community.aws.elb_target_info module – Gathers which target groups a target is associated with.

> **Note:**
>
> This module is part of the [community.aws collection](https://galaxy.ansible.com/ui/repo/published/community/aws/) (version 6.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.aws`.
> You need further requirements to be able to use this module,
> see [Requirements](elb_target_info_module.md#ansible-collections-community-aws-elb-target-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.elb_target_info`.

New in community.aws 1.0.0

- [Synopsis](elb_target_info_module.md#synopsis)
- [Requirements](elb_target_info_module.md#requirements)
- [Parameters](elb_target_info_module.md#parameters)
- [Notes](elb_target_info_module.md#notes)
- [Examples](elb_target_info_module.md#examples)
- [Return Values](elb_target_info_module.md#return-values)

## [Synopsis](elb_target_info_module.md#id1)

- This module will search through every target group in a region to find which ones have registered a given instance ID or IP.

## [Requirements](elb_target_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](elb_target_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **get_unused_target_groups**  boolean | Whether or not to get target groups not used by any load balancers.  **Choices:**   - `false` - `true` ← (default) |
| **instance_id**  string / required | What instance ID to get information for. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](elb_target_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](elb_target_info_module.md#id5)

```yaml+jinja
# practical use case - dynamically de-registering and re-registering nodes

  - name: Get EC2 Metadata
    amazon.aws.ec2_metadata_facts:

  - name: Get initial list of target groups
    delegate_to: localhost
    community.aws.elb_target_info:
      instance_id: "{{ ansible_ec2_instance_id }}"
      region: "{{ ansible_ec2_placement_region }}"
    register: target_info

  - name: save fact for later
    ansible.builtin.set_fact:
      original_tgs: "{{ target_info.instance_target_groups }}"

  - name: Deregister instance from all target groups
    delegate_to: localhost
    community.aws.elb_target:
        target_group_arn: "{{ item.0.target_group_arn }}"
        target_port: "{{ item.1.target_port }}"
        target_az: "{{ item.1.target_az }}"
        target_id: "{{ item.1.target_id }}"
        state: absent
        target_status: "draining"
        region: "{{ ansible_ec2_placement_region }}"
    with_subelements:
      - "{{ original_tgs }}"
      - "targets"

    # This avoids having to wait for 'elb_target' to serially deregister each
    # target group.  An alternative would be to run all of the 'elb_target'
    # tasks async and wait for them to finish.

  - name: wait for all targets to deregister simultaneously
    delegate_to: localhost
    community.aws.elb_target_info:
      get_unused_target_groups: false
      instance_id: "{{ ansible_ec2_instance_id }}"
      region: "{{ ansible_ec2_placement_region }}"
    register: target_info
    until: (target_info.instance_target_groups | length) == 0
    retries: 60
    delay: 10

  - name: reregister in elbv2s
    community.aws.elb_target:
      region: "{{ ansible_ec2_placement_region }}"
      target_group_arn: "{{ item.0.target_group_arn }}"
      target_port: "{{ item.1.target_port }}"
      target_az: "{{ item.1.target_az }}"
      target_id: "{{ item.1.target_id }}"
      state: present
      target_status: "initial"
    with_subelements:
      - "{{ original_tgs }}"
      - "targets"

  # wait until all groups associated with this instance are 'healthy' or
  # 'unused'
  - name: wait for registration
    community.aws.elb_target_info:
      get_unused_target_groups: false
      instance_id: "{{ ansible_ec2_instance_id }}"
      region: "{{ ansible_ec2_placement_region }}"
    register: target_info
    until: (target_info.instance_target_groups |
            map(attribute='targets') |
            flatten |
            map(attribute='target_health') |
            rejectattr('state', 'equalto', 'healthy') |
            rejectattr('state', 'equalto', 'unused') |
            list |
            length) == 0
    retries: 61
    delay: 10

# using the target groups to generate AWS CLI commands to reregister the
# instance - useful in case the playbook fails mid-run and manual
#            rollback is required
  - name: "reregistration commands: ELBv2s"
    ansible.builtin.debug:
      msg: >
             aws --region {{ansible_ec2_placement_region}} elbv2
             register-targets --target-group-arn {{item.target_group_arn}}
             --targets{%for target in item.targets%}
             Id={{target.target_id}},
             Port={{target.target_port}}{%if target.target_az%},AvailabilityZone={{target.target_az}}
             {%endif%}
             {%endfor%}
    loop: "{{target_info.instance_target_groups}}"
```

## [Return Values](elb_target_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instance_target_groups**  complex | a list of target groups to which the instance is registered to  **Returned:** always |
| **target_group_arn**  string | The ARN of the target group  **Returned:** always  **Sample:** `"['arn:aws:elasticloadbalancing:eu-west-1:123456789012:targetgroup/target-group/deadbeefdeadbeef']"` |
| **target_group_type**  string | Which target type is used for this group  **Returned:** always  **Sample:** `"['ip', 'instance']"` |
| **targets**  complex | A list of targets that point to this instance ID  **Returned:** always |
| **target_az**  string | which availability zone is explicitly associated with this target  **Returned:** when an AZ is associated with this instance  **Sample:** `"['us-west-2a']"` |
| **target_health**  complex | The target health description.  See following link for all the possible values <https://boto3.readthedocs.io/en/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_target_health>  **Returned:** always |
| **description**  string | description of target health  **Returned:** if *state!=present*  **Sample:** `"['Target desregistration is in progress']"` |
| **reason**  string | reason code for target health  **Returned:** if *state!=healthy*  **Sample:** `"['Target.Deregistration in progress']"` |
| **state**  string | health state  **Returned:** always  **Sample:** `"['healthy', 'draining', 'initial', 'unhealthy', 'unused', 'unavailable']"` |
| **target_id**  string | the target ID referring to this instance  **Returned:** always  **Sample:** `"['i-deadbeef', '1.2.3.4']"` |
| **target_port**  string | which port this target is listening on  **Returned:** always  **Sample:** `"[80]"` |

### Authors

- Yaakov Kuperman (@yaakov-github)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
