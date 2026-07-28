---
collection: ansible
version: "8"
title: "amazon.aws.aws_rds inventory – RDS instance inventory source"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/aws_rds_inventory.html
fetched_at: 2026-07-28T01:07:18+00:00
---
# amazon.aws.aws_rds inventory – RDS instance inventory source

> **Note:**
>
> This inventory plugin is part of the [amazon.aws collection](https://galaxy.ansible.com/ui/repo/published/amazon/aws/) (version 6.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install amazon.aws`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](aws_rds_inventory.md#ansible-collections-amazon-aws-aws-rds-inventory-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.aws_rds`.

- [Synopsis](aws_rds_inventory.md#synopsis)
- [Requirements](aws_rds_inventory.md#requirements)
- [Parameters](aws_rds_inventory.md#parameters)
- [Notes](aws_rds_inventory.md#notes)
- [Examples](aws_rds_inventory.md#examples)

## [Synopsis](aws_rds_inventory.md#id1)

- Get instances and clusters from Amazon Web Services RDS.
- Uses a YAML configuration file that ends with aws_rds.(yml|yaml).

## [Requirements](aws_rds_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](aws_rds_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_ACCESS_KEY_ID`](../../environment_variables.md#envvar-AWS_ACCESS_KEY_ID) - Environment variable: [`AWS_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_ACCESS_KEY) - Environment variable: [`EC2_ACCESS_KEY`](../../environment_variables.md#envvar-EC2_ACCESS_KEY)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_ACCESS_KEY_ID |
| **assume_role_arn**  aliases: iam_role_arn  string | The ARN of the IAM role to assume to perform the lookup.  You should still provide AWS credentials with enough privilege to perform the AssumeRole action. |
| **cache**  boolean | Toggle to enable/disable the caching of the inventory’s source data, requires a cache plugin setup to work.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory]   cache = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_CACHE`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE) |
| **cache_connection**  string | Cache connection data or path, read cache plugin documentation for specifics.  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ```  ```YAML+Jinja   [inventory]   cache_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_CONNECTION) |
| **cache_plugin**  string | Cache plugin to use for the inventory’s source data.  **Default:** `"memory"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching = memory   ```  ```YAML+Jinja   [inventory]   cache_plugin = memory   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN) |
| **cache_prefix**  string | Prefix to use for cache plugin files/tables  **Default:** `"ansible_inventory_"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [default]   fact_caching_prefix = ansible_inventory_   ```  Removed in: version 2.16 of ansible.builtin  Why: Fixes typing error in INI section name  Alternative: Use the ‘defaults’ section instead  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_inventory_   ```  ```YAML+Jinja   [inventory]   cache_prefix = ansible_inventory_   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX) |
| **cache_timeout**  integer | Cache duration in seconds  **Default:** `3600`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 3600   ```  ```YAML+Jinja   [inventory]   cache_timeout = 3600   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_TIMEOUT) |
| **compose**  dictionary | Create vars from jinja2 expressions.  **Default:** `{}` |
| **endpoint_url**  aliases: aws_endpoint_url, endpoint  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The *endpoint* alias has been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_URL`](../../environment_variables.md#envvar-AWS_URL) - Environment variable: [`EC2_URL`](../../environment_variables.md#envvar-EC2_URL)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_URL |
| **filters**  string | A dictionary of filter value pairs. Available filters are listed here <https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html#options>. If you filter by db-cluster-id and *include_clusters* is True it will apply to clusters as well.  **Default:** `{}` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **hostvars_prefix**  string  *added in amazon.aws 3.1.0* | The prefix for host variables names coming from AWS. |
| **hostvars_suffix**  string  *added in amazon.aws 3.1.0* | The suffix for host variables names coming from AWS. |
| **include_clusters**  boolean | Whether or not to query for Aurora clusters as well as instances.  **Choices:**   - `false` ← (default) - `true` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  **Default:** `[]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **profile**  aliases: aws_profile, boto_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options.  The *boto_profile* alias has been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_PROFILE`](../../environment_variables.md#envvar-AWS_PROFILE) - Environment variable: [`AWS_DEFAULT_PROFILE`](../../environment_variables.md#envvar-AWS_DEFAULT_PROFILE) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  **Configuration:**   - Environment variable: [`AWS_REGION`](../../environment_variables.md#envvar-AWS_REGION) - Environment variable: [`EC2_REGION`](../../environment_variables.md#envvar-EC2_REGION)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources, when it is used for all connections  Alternative: |
| **regions**  string | A list of regions in which to describe RDS instances and clusters. Available regions are listed here <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html>.  **Default:** `[]` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_SECRET_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_SECRET_ACCESS_KEY) - Environment variable: [`AWS_SECRET_KEY`](../../environment_variables.md#envvar-AWS_SECRET_KEY) - Environment variable: [`EC2_SECRET_KEY`](../../environment_variables.md#envvar-EC2_SECRET_KEY)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_SECRET_ACCESS_KEY |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_SESSION_TOKEN`](../../environment_variables.md#envvar-AWS_SESSION_TOKEN) - Environment variable: [`AWS_SECURITY_TOKEN`](../../environment_variables.md#envvar-AWS_SECURITY_TOKEN)  Removed in: major release after 2024-12-01  Why: AWS_SECURITY_TOKEN was used for compatibility with the original boto SDK, support for which has been dropped  Alternative: AWS_SESSION_TOKEN - Environment variable: [`EC2_SECURITY_TOKEN`](../../environment_variables.md#envvar-EC2_SECURITY_TOKEN)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_SESSION_TOKEN |
| **statuses**  list / elements=string | A list of desired states for instances/clusters to be added to inventory. Set to [‘all’] as a shorthand to find everything.  **Default:** `["creating", "available"]` |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **strict_permissions**  boolean | By default if an AccessDenied exception is encountered this plugin will fail. You can set strict_permissions to False in the inventory config file which will allow the restrictions to be gracefully skipped.  **Choices:**   - `false` - `true` ← (default) |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |

## [Notes](aws_rds_inventory.md#id4)

> **Note:**
>
> - Ansible versions prior to 2.10 should use the fully qualified plugin name ‘amazon.aws.aws_rds’.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](aws_rds_inventory.md#id5)

```yaml+jinja
plugin: aws_rds
regions:
  - us-east-1
  - ca-central-1
keyed_groups:
  - key: 'db_parameter_groups|json_query("[].db_parameter_group_name")'
    prefix: rds_parameter_group
  - key: engine
    prefix: rds
  - key: tags
  - key: region
hostvars_prefix: aws_
hostvars_suffix: _rds
```

### Authors

- Sloane Hertel (@s-hertel)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
