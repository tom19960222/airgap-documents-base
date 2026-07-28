---
collection: ansible
version: "8"
title: "community.aws.waf_condition module – Create and delete WAF Conditions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/waf_condition_module.html
fetched_at: 2026-07-28T01:42:05+00:00
---
# community.aws.waf_condition module – Create and delete WAF Conditions

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
> see [Requirements](waf_condition_module.md#ansible-collections-community-aws-waf-condition-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.waf_condition`.

New in community.aws 1.0.0

- [Synopsis](waf_condition_module.md#synopsis)
- [Requirements](waf_condition_module.md#requirements)
- [Parameters](waf_condition_module.md#parameters)
- [Notes](waf_condition_module.md#notes)
- [Examples](waf_condition_module.md#examples)
- [Return Values](waf_condition_module.md#return-values)

## [Synopsis](waf_condition_module.md#id1)

- Read the AWS documentation for WAF <https://aws.amazon.com/documentation/waf/>
- Prior to release 5.0.0 this module was called `community.aws.aws_waf_condition`. The usage did not change.

Aliases: aws_waf_condition

## [Requirements](waf_condition_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](waf_condition_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **filters**  list / elements=dictionary | A list of the filters against which to match.  For *type=byte*, valid keys are *field_to_match*, *position*, *header*, *transformation* and *target_string*.  For *type=geo*, the only valid key is *country*.  For *type=ip*, the only valid key is *ip_address*.  For *type=regex*, valid keys are *field_to_match*, *transformation* and *regex_pattern*.  For *type=size*, valid keys are *field_to_match*, *transformation*, *comparison* and *size*.  For *type=sql*, valid keys are *field_to_match* and *transformation*.  For *type=xss*, valid keys are *field_to_match* and *transformation*.  Required when *state=present*. |
| **comparison**  string | What type of comparison to perform.  Only valid key when *type=size*.  **Choices:**   - `"EQ"` - `"NE"` - `"LE"` - `"LT"` - `"GE"` - `"GT"` |
| **country**  string | Value of geo constraint (typically a two letter country code).  The only valid key when *type=geo*. |
| **field_to_match**  string | The field upon which to perform the match.  Valid when *type=byte*, *type=regex*, *type=sql* or *type=xss*.  **Choices:**   - `"uri"` - `"query_string"` - `"header"` - `"method"` - `"body"` |
| **header**  string | Which specific header should be matched.  Required when *field_to_match=header*.  Valid when *type=byte*. |
| **ip_address**  string | An IP Address or CIDR to match.  The only valid key when *type=ip*. |
| **position**  string | Where in the field the match needs to occur.  Only valid when *type=byte*.  **Choices:**   - `"exactly"` - `"starts_with"` - `"ends_with"` - `"contains"` - `"contains_word"` |
| **regex_pattern**  dictionary | A dict describing the regular expressions used to perform the match.  Only valid when *type=regex*. |
| **name**  string | A name to describe the set of patterns. |
| **regex_strings**  list / elements=string | A list of regular expressions to match. |
| **size**  integer | The size of the field (in bytes).  Only valid key when *type=size*. |
| **target_string**  string | The string to search for.  May be up to 50 bytes.  Valid when *type=byte*. |
| **transformation**  string | A transform to apply on the field prior to performing the match.  Valid when *type=byte*, *type=regex*, *type=sql* or *type=xss*.  **Choices:**   - `"none"` - `"compress_white_space"` - `"html_entity_decode"` - `"lowercase"` - `"cmd_line"` - `"url_decode"` |
| **name**  string / required | Name of the Web Application Firewall condition to manage. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_filters**  boolean | Whether to remove existing filters from a condition if not passed in *filters*.  **Choices:**   - `false` ← (default) - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Whether the condition should be `present` or `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **type**  string / required | The type of matching to perform.  **Choices:**   - `"byte"` - `"geo"` - `"ip"` - `"regex"` - `"size"` - `"sql"` - `"xss"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **waf_regional**  boolean | Whether to use `waf-regional` module.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](waf_condition_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](waf_condition_module.md#id5)

```yaml+jinja
- name: create WAF byte condition
  community.aws.waf_condition:
    name: my_byte_condition
    filters:
    - field_to_match: header
      position: STARTS_WITH
      target_string: Hello
      header: Content-type
    type: byte

- name: create WAF geo condition
  community.aws.waf_condition:
    name: my_geo_condition
    filters:
      - country: US
      - country: AU
      - country: AT
    type: geo

- name: create IP address condition
  community.aws.waf_condition:
    name: "{{ resource_prefix }}_ip_condition"
    filters:
      - ip_address: "10.0.0.0/8"
      - ip_address: "192.168.0.0/24"
    type: ip

- name: create WAF regex condition
  community.aws.waf_condition:
    name: my_regex_condition
    filters:
      - field_to_match: query_string
        regex_pattern:
          name: greetings
          regex_strings:
            - '[hH]ello'
            - '^Hi there'
            - '.*Good Day to You'
    type: regex

- name: create WAF size condition
  community.aws.waf_condition:
    name: my_size_condition
    filters:
      - field_to_match: query_string
        size: 300
        comparison: GT
    type: size

- name: create WAF sql injection condition
  community.aws.waf_condition:
    name: my_sql_condition
    filters:
      - field_to_match: query_string
        transformation: url_decode
    type: sql

- name: create WAF xss condition
  community.aws.waf_condition:
    name: my_xss_condition
    filters:
      - field_to_match: query_string
        transformation: url_decode
    type: xss
```

## [Return Values](waf_condition_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **condition**  complex | Condition returned by operation.  **Returned:** always |
| **byte_match_set_id**  string | ID for byte match set.  **Returned:** always  **Sample:** `"c4882c96-837b-44a2-a762-4ea87dbf812b"` |
| **byte_match_tuples**  complex | List of byte match tuples.  **Returned:** always |
| **field_to_match**  complex | Field to match.  **Returned:** always |
| **data**  string | Which specific header (if type is header).  **Returned:** success  **Sample:** `"content-type"` |
| **type**  string | Type of field  **Returned:** success  **Sample:** `"HEADER"` |
| **positional_constraint**  string | Position in the field to match.  **Returned:** success  **Sample:** `"STARTS_WITH"` |
| **target_string**  string | String to look for.  **Returned:** success  **Sample:** `"Hello"` |
| **text_transformation**  string | Transformation to apply to the field before matching.  **Returned:** success  **Sample:** `"NONE"` |
| **condition_id**  string | Type-agnostic ID for the condition.  **Returned:** when state is present  **Sample:** `"dd74b1ff-8c06-4a4f-897a-6b23605de413"` |
| **geo_match_constraints**  complex | List of geographical constraints.  **Returned:** when type is geo and state is present |
| **type**  string | Type of geo constraint.  **Returned:** success  **Sample:** `"Country"` |
| **value**  string | Value of geo constraint (typically a country code).  **Returned:** success  **Sample:** `"AT"` |
| **geo_match_set_id**  string | ID of the geo match set.  **Returned:** when type is geo and state is present  **Sample:** `"dd74b1ff-8c06-4a4f-897a-6b23605de413"` |
| **ip_set_descriptors**  complex | list of IP address filters  **Returned:** when type is ip and state is present |
| **type**  string | Type of IP address (IPV4 or IPV6).  **Returned:** always  **Sample:** `"IPV4"` |
| **value**  string | IP address.  **Returned:** always  **Sample:** `"10.0.0.0/8"` |
| **ip_set_id**  string | ID of condition.  **Returned:** when type is ip and state is present  **Sample:** `"78ad334a-3535-4036-85e6-8e11e745217b"` |
| **name**  string | Name of condition.  **Returned:** when state is present  **Sample:** `"my_waf_condition"` |
| **regex_match_set_id**  string | ID of the regex match set.  **Returned:** when type is regex and state is present  **Sample:** `"5ea3f6a8-3cd3-488b-b637-17b79ce7089c"` |
| **regex_match_tuples**  complex | List of regex matches.  **Returned:** when type is regex and state is present |
| **field_to_match**  complex | Field on which the regex match is applied.  **Returned:** success |
| **type**  string | The field name.  **Returned:** when type is regex and state is present  **Sample:** `"QUERY_STRING"` |
| **regex_pattern_set_id**  string | ID of the regex pattern.  **Returned:** success  **Sample:** `"6fdf7f2d-9091-445c-aef2-98f3c051ac9e"` |
| **text_transformation**  string | transformation applied to the text before matching  **Returned:** success  **Sample:** `"NONE"` |
| **size_constraint_set_id**  string | ID of the size constraint set.  **Returned:** when type is size and state is present  **Sample:** `"de84b4b3-578b-447e-a9a0-0db35c995656"` |
| **size_constraints**  complex | List of size constraints to apply.  **Returned:** when type is size and state is present |
| **comparison_operator**  string | Comparison operator to apply.  **Returned:** success  **Sample:** `"GT"` |
| **field_to_match**  complex | Field on which the size constraint is applied.  **Returned:** success |
| **type**  string | Field name.  **Returned:** success  **Sample:** `"QUERY_STRING"` |
| **size**  integer | Size to compare against the field.  **Returned:** success  **Sample:** `300` |
| **text_transformation**  string | Transformation applied to the text before matching.  **Returned:** success  **Sample:** `"NONE"` |
| **sql_injection_match_set_id**  string | ID of the SQL injection match set.  **Returned:** when type is sql and state is present  **Sample:** `"de84b4b3-578b-447e-a9a0-0db35c995656"` |
| **sql_injection_match_tuples**  complex | List of SQL injection match sets.  **Returned:** when type is sql and state is present |
| **field_to_match**  complex | Field on which the SQL injection match is applied.  **Returned:** success |
| **type**  string | Field name.  **Returned:** success  **Sample:** `"QUERY_STRING"` |
| **text_transformation**  string | Transformation applied to the text before matching.  **Returned:** success  **Sample:** `"URL_DECODE"` |
| **xss_match_set_id**  string | ID of the XSS match set.  **Returned:** when type is xss and state is present  **Sample:** `"de84b4b3-578b-447e-a9a0-0db35c995656"` |
| **xss_match_tuples**  complex | List of XSS match sets.  **Returned:** when type is xss and state is present |
| **field_to_match**  complex | Field on which the XSS match is applied.  **Returned:** success |
| **type**  string | Field name  **Returned:** success  **Sample:** `"QUERY_STRING"` |
| **text_transformation**  string | transformation applied to the text before matching.  **Returned:** success  **Sample:** `"URL_DECODE"` |

### Authors

- Will Thames (@willthames)
- Mike Mochan (@mmochan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
