---
collection: ansible
version: "6"
title: "amazon.aws.aws_ssm lookup – Get the value for a SSM parameter or all parameters under a path."
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/aws_ssm_lookup.html
fetched_at: 2026-07-27T16:43:21+00:00
---
# amazon.aws.aws_ssm lookup – Get the value for a SSM parameter or all parameters under a path.

> **Note:**
>
> This lookup plugin is part of the [amazon.aws collection](https://galaxy.ansible.com/amazon/aws) (version 3.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install amazon.aws`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](aws_ssm_lookup.md#ansible-collections-amazon-aws-aws-ssm-lookup-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.aws_ssm`.

- [Synopsis](aws_ssm_lookup.md#synopsis)
- [Requirements](aws_ssm_lookup.md#requirements)
- [Keyword parameters](aws_ssm_lookup.md#keyword-parameters)
- [Examples](aws_ssm_lookup.md#examples)

## [Synopsis](aws_ssm_lookup.md#id1)

- Get the value for an Amazon Simple Systems Manager parameter or a hierarchy of parameters. The first argument you pass the lookup can either be a parameter name or a hierarchy of parameters. Hierarchies start with a forward slash and end with the parameter name. Up to 5 layers may be specified.
- If looking up an explicitly listed parameter by name which does not exist then the lookup will return a None value which will be interpreted by Jinja2 as an empty string. You can use the ```default``` filter to give a default value in this case but must set the second parameter to true (see examples below)
- When looking up a path for parameters under it a dictionary will be returned for each path. If there is no parameter under that path then the return will be successful but the dictionary will be empty.
- If the lookup fails due to lack of permissions or due to an AWS client error then the aws_ssm will generate an error, normally crashing the current ansible task. This is normally the right thing since ignoring a value that IAM isn’t giving access to could cause bigger problems and wrong behaviour or loss of data. If you want to continue in this case then you will have to set up two ansible tasks, one which sets a variable and ignores failures one which uses the value of that variable with a default. See the examples below.

## [Requirements](aws_ssm_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Keyword parameters](aws_ssm_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('amazon.aws.aws_ssm', key1=value1, key2=value2, ...)` and `query('amazon.aws.aws_ssm', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **bypath**  boolean | A boolean to indicate whether the parameter is provided as a hierarchy.  Choices:   - `false` ← (default) - `true` |
| **decrypt**  boolean | A boolean to indicate whether to decrypt the parameter.  Choices:   - `false` - `true` ← (default) |
| **endpoint**  string  added in amazon.aws 3.3.0 | Use a custom endpoint when connecting to SSM service. |
| **on_denied**  string  added in amazon.aws 2.0.0 | Action to take if access to the SSM parameter is denied.  `error` will raise a fatal error when access to the SSM parameter is denied.  `skip` will silently ignore the denied SSM parameter.  `warn` will skip over the denied SSM parameter but issue a warning.  Choices:   - `"error"` ← (default) - `"skip"` - `"warn"` |
| **on_missing**  string  added in amazon.aws 2.0.0 | Action to take if the SSM parameter is missing.  `error` will raise a fatal error when the SSM parameter is missing.  `skip` will silently ignore the missing SSM parameter.  `warn` will skip over the missing SSM parameter but issue a warning.  Choices:   - `"error"` ← (default) - `"skip"` - `"warn"` |
| **recursive**  boolean | A boolean to indicate whether to retrieve all parameters within a hierarchy.  Choices:   - `false` ← (default) - `true` |
| **shortnames**  boolean | Indicates whether to return the name only without path if using a parameter hierarchy.  Choices:   - `false` ← (default) - `true` |

## [Examples](aws_ssm_lookup.md#id4)

```yaml+jinja
# lookup sample:
- name: lookup ssm parameter store in the current region
  debug: msg="{{ lookup('aws_ssm', 'Hello' ) }}"

- name: lookup ssm parameter store in nominated region
  debug: msg="{{ lookup('aws_ssm', 'Hello', region='us-east-2' ) }}"

- name: lookup ssm parameter store without decrypted
  debug: msg="{{ lookup('aws_ssm', 'Hello', decrypt=False ) }}"

- name: lookup ssm parameter store in nominated aws profile
  debug: msg="{{ lookup('aws_ssm', 'Hello', aws_profile='myprofile' ) }}"

- name: lookup ssm parameter store using explicit aws credentials
  debug: msg="{{ lookup('aws_ssm', 'Hello', aws_access_key=my_aws_access_key, aws_secret_key=my_aws_secret_key, aws_security_token=my_security_token ) }}"

- name: lookup ssm parameter store with all options.
  debug: msg="{{ lookup('aws_ssm', 'Hello', decrypt=false, region='us-east-2', aws_profile='myprofile') }}"

- name: lookup a key which doesn't exist, returns ""
  debug: msg="{{ lookup('aws_ssm', 'NoKey') }}"

- name: lookup a key which doesn't exist, returning a default ('root')
  debug: msg="{{ lookup('aws_ssm', 'AdminID') | default('root', true) }}"

- name: lookup a key which doesn't exist failing to store it in a fact
  set_fact:
    temp_secret: "{{ lookup('aws_ssm', '/NoAccess/hiddensecret') }}"
  ignore_errors: true

- name: show fact default to "access failed" if we don't have access
  debug: msg="{{ 'the secret was:' ~ temp_secret | default('could not access secret') }}"

- name: return a dictionary of ssm parameters from a hierarchy path
  debug: msg="{{ lookup('aws_ssm', '/PATH/to/params', region='ap-southeast-2', bypath=true, recursive=true ) }}"

- name: return a dictionary of ssm parameters from a hierarchy path with shortened names (param instead of /PATH/to/param)
  debug: msg="{{ lookup('aws_ssm', '/PATH/to/params', region='ap-southeast-2', shortnames=true, bypath=true, recursive=true ) }}"

- name: Iterate over a parameter hierarchy (one iteration per parameter)
  debug: msg='Key contains {{ item.key }} , with value {{ item.value }}'
  loop: '{{ lookup("aws_ssm", "/demo/", region="ap-southeast-2", bypath=True) | dict2items }}'

- name: Iterate over multiple paths as dictionaries (one iteration per path)
  debug: msg='Path contains {{ item }}'
  loop: '{{ lookup("aws_ssm", "/demo/", "/demo1/", bypath=True)}}'

- name: lookup ssm parameter and fail if missing
  debug: msg="{{ lookup('aws_ssm', 'missing-parameter', on_missing="error" ) }}"

- name: lookup ssm parameter warn if access is denied
  debug: msg="{{ lookup('aws_ssm', 'missing-parameter', on_denied="warn" ) }}"
```

### Authors

- Bill Wang <ozbillwang(at)gmail.com>
- Marat Bakeev <hawara(at)gmail.com>
- Michael De La Rue

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
