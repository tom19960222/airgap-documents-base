---
collection: ansible
version: "8"
title: "amazon.aws.aws_ec2 inventory – EC2 inventory source"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/aws_ec2_inventory.html
fetched_at: 2026-07-28T01:07:17+00:00
---
# amazon.aws.aws_ec2 inventory – EC2 inventory source

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
> see [Requirements](aws_ec2_inventory.md#ansible-collections-amazon-aws-aws-ec2-inventory-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.aws_ec2`.

- [Synopsis](aws_ec2_inventory.md#synopsis)
- [Requirements](aws_ec2_inventory.md#requirements)
- [Parameters](aws_ec2_inventory.md#parameters)
- [Notes](aws_ec2_inventory.md#notes)
- [Examples](aws_ec2_inventory.md#examples)

## [Synopsis](aws_ec2_inventory.md#id1)

- Get inventory hosts from Amazon Web Services EC2.
- The inventory file is a YAML configuration file and must end with `aws_ec2.{yml|yaml}`. Example: `my_inventory.aws_ec2.yml`.

## [Requirements](aws_ec2_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](aws_ec2_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_ACCESS_KEY_ID`](../../environment_variables.md#envvar-AWS_ACCESS_KEY_ID) - Environment variable: [`AWS_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_ACCESS_KEY) - Environment variable: [`EC2_ACCESS_KEY`](../../environment_variables.md#envvar-EC2_ACCESS_KEY)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_ACCESS_KEY_ID |
| **allow_duplicated_hosts**  boolean  *added in amazon.aws 5.0.0* | By default, the first name that matches an entry of the *hostnames* list is returned.  Turn this flag on if you don’t mind having duplicated entries in the inventory and you want to get all the hostnames that match.  **Choices:**   - `false` ← (default) - `true` |
| **assume_role_arn**  aliases: iam_role_arn  string | The ARN of the IAM role to assume to perform the lookup.  You should still provide AWS credentials with enough privilege to perform the AssumeRole action. |
| **cache**  boolean | Toggle to enable/disable the caching of the inventory’s source data, requires a cache plugin setup to work.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory]   cache = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_CACHE`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE) |
| **cache_connection**  string | Cache connection data or path, read cache plugin documentation for specifics.  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ```  ```YAML+Jinja   [inventory]   cache_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_CONNECTION) |
| **cache_plugin**  string | Cache plugin to use for the inventory’s source data.  **Default:** `"memory"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching = memory   ```  ```YAML+Jinja   [inventory]   cache_plugin = memory   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN) |
| **cache_prefix**  string | Prefix to use for cache plugin files/tables  **Default:** `"ansible_inventory_"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [default]   fact_caching_prefix = ansible_inventory_   ```  Removed in: version 2.16 of ansible.builtin  Why: Fixes typing error in INI section name  Alternative: Use the ‘defaults’ section instead  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_inventory_   ```  ```YAML+Jinja   [inventory]   cache_prefix = ansible_inventory_   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX) |
| **cache_timeout**  integer | Cache duration in seconds  **Default:** `3600`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 3600   ```  ```YAML+Jinja   [inventory]   cache_timeout = 3600   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_TIMEOUT) |
| **compose**  dictionary | Create vars from jinja2 expressions.  **Default:** `{}` |
| **endpoint_url**  aliases: aws_endpoint_url, endpoint  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The *endpoint* alias has been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_URL`](../../environment_variables.md#envvar-AWS_URL) - Environment variable: [`EC2_URL`](../../environment_variables.md#envvar-EC2_URL)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_URL |
| **exclude_filters**  list / elements=dictionary  *added in amazon.aws 1.5.0* | A list of filters. Any instances matching one of the filters are excluded from the result.  The filters from `exclude_filters` take priority over the `include_filters` and `filters` keys  Available filters are listed here <http://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html#options>.  Every entry in this list triggers a search query. As such, from a performance point of view, it’s better to keep the list as short as possible.  **Default:** `[]` |
| **filters**  dictionary | A dictionary of filter value pairs.  Available filters are listed here <http://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html#options>.  **Default:** `{}` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **hostnames**  list / elements=any | A list in order of precedence for hostname variables.  The elements of the list can be a dict with the keys mentioned below or a string.  Can be one of the options specified in <http://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html#options>.  If value provided does not exist in the above options, it will be used as a literal string.  To use tags as hostnames use the syntax <tag:Name=Value> to use the hostname Name_Value, or <tag:Name> to use the value of the Name tag.  **Default:** `[]` |
| **name**  string / required | Name of the host. |
| **prefix**  string | Prefix to prepend to *name*. Same options as *name*.  If *prefix* is specified, final hostname will be *prefix* + *separator* + *name*.  **Default:** `""` |
| **separator**  string | Value to separate *prefix* and *name* when *prefix* is specified.  **Default:** `"_"` |
| **hostvars_prefix**  string  *added in amazon.aws 3.1.0* | The prefix for host variables names coming from AWS. |
| **hostvars_suffix**  string  *added in amazon.aws 3.1.0* | The suffix for host variables names coming from AWS. |
| **include_extra_api_calls**  boolean | Add two additional API calls for every instance to include ‘persistent’ and ‘events’ host variables.  Spot instances may be persistent and instances may have associated events.  The *include_extra_api_calls* option had been deprecated and will be removed in release 6.0.0.  **Choices:**   - `false` ← (default) - `true` |
| **include_filters**  list / elements=dictionary  *added in amazon.aws 1.5.0* | A list of filters. Any instances matching at least one of the filters are included in the result.  Available filters are listed here <http://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html#options>.  Every entry in this list triggers a search query. As such, from a performance point of view, it’s better to keep the list as short as possible.  **Default:** `[]` |
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
| **regions**  list / elements=string | A list of regions in which to describe EC2 instances.  If empty (the default) default this will include all regions, except possibly restricted ones like us-gov-west-1 and cn-north-1.  **Default:** `[]` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_SECRET_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_SECRET_ACCESS_KEY) - Environment variable: [`AWS_SECRET_KEY`](../../environment_variables.md#envvar-AWS_SECRET_KEY) - Environment variable: [`EC2_SECRET_KEY`](../../environment_variables.md#envvar-EC2_SECRET_KEY)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_SECRET_ACCESS_KEY |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_SESSION_TOKEN`](../../environment_variables.md#envvar-AWS_SESSION_TOKEN) - Environment variable: [`AWS_SECURITY_TOKEN`](../../environment_variables.md#envvar-AWS_SECURITY_TOKEN)  Removed in: major release after 2024-12-01  Why: AWS_SECURITY_TOKEN was used for compatibility with the original boto SDK, support for which has been dropped  Alternative: AWS_SESSION_TOKEN - Environment variable: [`EC2_SECURITY_TOKEN`](../../environment_variables.md#envvar-EC2_SECURITY_TOKEN)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_SESSION_TOKEN |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **strict_permissions**  boolean | By default if a 403 (Forbidden) error code is encountered this plugin will fail.  You can set this option to False in the inventory config file which will allow 403 errors to be gracefully skipped.  **Choices:**   - `false` - `true` ← (default) |
| **use_contrib_script_compatible_ec2_tag_keys**  boolean  *added in amazon.aws 1.5.0* | Expose the host tags with ec2_tag_TAGNAME keys like the old ec2.py inventory script.  The use of this feature is discouraged and we advise to migrate to the new ``tags`` structure.  **Choices:**   - `false` ← (default) - `true` |
| **use_contrib_script_compatible_sanitization**  boolean | By default this plugin is using a general group name sanitization to create safe and usable group names for use in Ansible. This option allows you to override that, in efforts to allow migration from the old inventory script and matches the sanitization of groups when the script’s ``replace_dash_in_groups`` option is set to ``False``. To replicate behavior of ``replace_dash_in_groups = True`` with constructed groups, you will need to replace hyphens with underscores via the regex_replace filter for those entries.  For this to work you should also turn off the TRANSFORM_INVALID_GROUP_CHARS setting, otherwise the core engine will just use the standard sanitization on top.  This is not the default as such names break certain functionality as not all characters are valid Python identifiers which group names end up being used as.  **Choices:**   - `false` ← (default) - `true` |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **use_ssm_inventory**  boolean  *added in amazon.aws 6.0.0* | Enables fetching additional EC2 instance information from the AWS Systems Manager (SSM) inventory service into hostvars.  By leveraging the SSM inventory data, the *use_ssm_inventory* option provides additional details and attributes about the EC2 instances in your inventory. These details can include operating system information, installed software, network configurations, and custom inventory attributes defined in SSM.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](aws_ec2_inventory.md#id4)

> **Note:**
>
> - If no credentials are provided and the control node has an associated IAM instance profile then the role will be used for authentication.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](aws_ec2_inventory.md#id5)

```yaml+jinja
# Minimal example using environment vars or instance role credentials
# Fetch all hosts in us-east-1, the hostname is the public DNS if it exists, otherwise the private IP address
plugin: amazon.aws.aws_ec2
regions:
  - us-east-1

# Example using filters, ignoring permission errors, and specifying the hostname precedence
plugin: amazon.aws.aws_ec2
# The values for profile, access key, secret key and token can be hardcoded like:
profile: aws_profile
# or you could use Jinja as:
# profile: "{{ lookup('env', 'AWS_PROFILE') | default('aws_profile', true) }}"
# Populate inventory with instances in these regions
regions:
  - us-east-1
  - us-east-2
filters:
  # All instances with their `Environment` tag set to `dev`
  tag:Environment: dev
  # All dev and QA hosts
  tag:Environment:
    - dev
    - qa
  instance.group-id: sg-xxxxxxxx
# Ignores 403 errors rather than failing
strict_permissions: False
# Note: I(hostnames) sets the inventory_hostname. To modify ansible_host without modifying
# inventory_hostname use compose (see example below).
hostnames:
  - tag:Name=Tag1,Name=Tag2  # Return specific hosts only
  - tag:CustomDNSName
  - dns-name
  - name: 'tag:Name=Tag1,Name=Tag2'
  - name: 'private-ip-address'
    separator: '_'
    prefix: 'tag:Name'
  - name: 'test_literal' # Using literal values for hostname
    separator: '-'       # Hostname will be aws-test_literal
    prefix: 'aws'

# Returns all the hostnames for a given instance
allow_duplicated_hosts: False

# Example using constructed features to create groups and set ansible_host
plugin: amazon.aws.aws_ec2
regions:
  - us-east-1
  - us-west-1
# keyed_groups may be used to create custom groups
strict: False
keyed_groups:
  # Add e.g. x86_64 hosts to an arch_x86_64 group
  - prefix: arch
    key: 'architecture'
  # Add hosts to tag_Name_Value groups for each Name/Value tag pair
  - prefix: tag
    key: tags
  # Add hosts to e.g. instance_type_z3_tiny
  - prefix: instance_type
    key: instance_type
  # Create security_groups_sg_abcd1234 group for each SG
  - key: 'security_groups|json_query("[].group_id")'
    prefix: 'security_groups'
  # Create a group for each value of the Application tag
  - key: tags.Application
    separator: ''
  # Create a group per region e.g. aws_region_us_east_2
  - key: placement.region
    prefix: aws_region
  # Create a group (or groups) based on the value of a custom tag "Role" and add them to a metagroup called "project"
  - key: tags['Role']
    prefix: foo
    parent_group: "project"
# Set individual variables with compose
compose:
  # Use the private IP address to connect to the host
  # (note: this does not modify inventory_hostname, which is set via I(hostnames))
  ansible_host: private_ip_address

# Example using include_filters and exclude_filters to compose the inventory.
plugin: amazon.aws.aws_ec2
regions:
  - us-east-1
  - us-west-1
include_filters:
- tag:Name:
  - 'my_second_tag'
- tag:Name:
  - 'my_third_tag'
exclude_filters:
- tag:Name:
  - 'my_first_tag'

# Example using groups to assign the running hosts to a group based on vpc_id
plugin: amazon.aws.aws_ec2
profile: aws_profile
# Populate inventory with instances in these regions
regions:
  - us-east-2
filters:
  # All instances with their state as `running`
  instance-state-name: running
keyed_groups:
  - prefix: tag
    key: tags
compose:
  ansible_host: public_dns_name
groups:
  libvpc: vpc_id == 'vpc-####'
# Define prefix and suffix for host variables coming from AWS.
plugin: amazon.aws.aws_ec2
regions:
  - us-east-1
hostvars_prefix: 'aws_'
hostvars_suffix: '_ec2'
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
