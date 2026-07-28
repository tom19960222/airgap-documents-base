---
collection: ansible
version: "6"
title: "community.aws.elb_target_info module – Gathers which target groups a target is associated with."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/elb_target_info_module.html
fetched_at: 2026-07-27T17:04:32+00:00
---
# community.aws.elb_target_info module – Gathers which target groups a target is associated with.

> **Note:**
>
> This module is part of the [community.aws collection](https://galaxy.ansible.com/community/aws) (version 3.6.0).
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
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](elb_target_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **get_unused_target_groups**  boolean | Whether or not to get target groups not used by any load balancers.  Choices:   - `false` - `true` ← (default) |
| **instance_id**  string / required | What instance ID to get information for. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](elb_target_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

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
| **instance_target_groups**  complex | a list of target groups to which the instance is registered to  Returned: always |
| **target_group_arn**  string | The ARN of the target group  Returned: always  Sample: `"['arn:aws:elasticloadbalancing:eu-west-1:111111111111:targetgroup/target-group/deadbeefdeadbeef']"` |
| **target_group_type**  string | Which target type is used for this group  Returned: always  Sample: `"['ip', 'instance']"` |
| **targets**  complex | A list of targets that point to this instance ID  Returned: always |
| **target_az**  string | which availability zone is explicitly associated with this target  Returned: when an AZ is associated with this instance  Sample: `"['us-west-2a']"` |
| **target_health**  complex | The target health description.  See following link for all the possible values <https://boto3.readthedocs.io/en/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_target_health>  Returned: always |
| **description**  string | description of target health  Returned: if *state!=present*  Sample: `"['Target desregistration is in progress']"` |
| **reason**  string | reason code for target health  Returned: if *state!=healthy*  Sample: `"['Target.Deregistration in progress']"` |
| **state**  string | health state  Returned: always  Sample: `"['healthy', 'draining', 'initial', 'unhealthy', 'unused', 'unavailable']"` |
| **target_id**  string | the target ID referring to this instance  Returned: always  Sample: `"['i-deadbeef', '1.2.3.4']"` |
| **target_port**  string | which port this target is listening on  Returned: always  Sample: `"[80]"` |

### Authors

- Yaakov Kuperman (@yaakov-github)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
