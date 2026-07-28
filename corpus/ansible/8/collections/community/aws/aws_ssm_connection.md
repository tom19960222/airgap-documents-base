---
collection: ansible
version: "8"
title: "community.aws.aws_ssm connection – connect to EC2 instances via AWS Systems Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/aws_ssm_connection.html
fetched_at: 2026-07-28T01:42:14+00:00
---
# community.aws.aws_ssm connection – connect to EC2 instances via AWS Systems Manager

> **Note:**
>
> This connection plugin is part of the [community.aws collection](https://galaxy.ansible.com/ui/repo/published/community/aws/) (version 6.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.aws`.
> You need further requirements to be able to use this connection plugin,
> see [Requirements](aws_ssm_connection.md#ansible-collections-community-aws-aws-ssm-connection-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_ssm`.

- [Synopsis](aws_ssm_connection.md#synopsis)
- [Requirements](aws_ssm_connection.md#requirements)
- [Parameters](aws_ssm_connection.md#parameters)
- [Notes](aws_ssm_connection.md#notes)
- [Examples](aws_ssm_connection.md#examples)

## [Synopsis](aws_ssm_connection.md#id1)

- This connection plugin allows Ansible to execute tasks on an EC2 instance via an AWS SSM Session.

## [Requirements](aws_ssm_connection.md#id2)

The below requirements are needed on the local controller node that executes this connection.

- The remote EC2 instance must be running the AWS Systems Manager Agent (SSM Agent). <https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started.html>
- The control machine must have the AWS session manager plugin installed. <https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html>
- The remote EC2 Linux instance must have curl installed.

## [Parameters](aws_ssm_connection.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key_id**  string  *added in community.aws 1.3.0* | The STS access key to use when connecting via session-manager.  **Configuration:**   - Environment variable: [`AWS_ACCESS_KEY_ID`](../../environment_variables.md#envvar-AWS_ACCESS_KEY_ID) - Variable: ansible_aws_ssm_access_key_id |
| **bucket_endpoint_url**  string  *added in community.aws 5.3.0* | The S3 endpoint URL of the bucket used for file transfers.  **Configuration:**   - Variable: ansible_aws_ssm_bucket_endpoint_url |
| **bucket_name**  string | The name of the S3 bucket used for file transfers.  **Configuration:**   - Variable: ansible_aws_ssm_bucket_name |
| **bucket_sse_kms_key_id**  string  *added in community.aws 2.2.0* | KMS key id to use when encrypting objects using `bucket_sse_mode=aws:kms`. Ignored otherwise.  **Configuration:**   - Variable: ansible_aws_ssm_bucket_sse_kms_key_id |
| **bucket_sse_mode**  string  *added in community.aws 2.2.0* | Server-side encryption mode to use for uploads on the S3 bucket used for file transfer.  **Choices:**   - `"AES256"` - `"aws:kms"`   **Configuration:**   - Variable: ansible_aws_ssm_bucket_sse_mode |
| **instance_id**  string | The EC2 instance ID.  **Configuration:**   - Variable: ansible_aws_ssm_instance_id |
| **plugin**  string | This defines the location of the session-manager-plugin binary.  **Default:** `"/usr/local/bin/session-manager-plugin"`  **Configuration:**   - Variable: ansible_aws_ssm_plugin |
| **profile**  string  *added in community.aws 1.5.0* | Sets AWS profile to use.  **Configuration:**   - Environment variable: [`AWS_PROFILE`](../../environment_variables.md#envvar-AWS_PROFILE) - Variable: ansible_aws_ssm_profile |
| **reconnection_retries**  integer | Number of attempts to connect.  **Default:** `3`  **Configuration:**   - Variable: ansible_aws_ssm_retries |
| **region**  string | The region the EC2 instance is located.  **Default:** `"us-east-1"`  **Configuration:**   - Environment variable: [`AWS_REGION`](../../environment_variables.md#envvar-AWS_REGION) - Environment variable: [`AWS_DEFAULT_REGION`](../../environment_variables.md#envvar-AWS_DEFAULT_REGION) - Variable: ansible_aws_ssm_region |
| **s3_addressing_style**  string  *added in community.aws 5.2.0* | The addressing style to use when using S3 URLs.  When the S3 bucket isn’t in the same region as the Instance explicitly setting the addressing style to ‘virtual’ may be necessary <https://repost.aws/knowledge-center/s3-http-307-response> as this forces the use of a specific endpoint.  **Choices:**   - `"path"` - `"virtual"` - `"auto"` ← (default)   **Configuration:**   - Variable: ansible_aws_ssm_s3_addressing_style |
| **secret_access_key**  string  *added in community.aws 1.3.0* | The STS secret key to use when connecting via session-manager.  **Configuration:**   - Environment variable: [`AWS_SECRET_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_SECRET_ACCESS_KEY) - Variable: ansible_aws_ssm_secret_access_key |
| **session_token**  string  *added in community.aws 1.3.0* | The STS session token to use when connecting via session-manager.  **Configuration:**   - Environment variable: [`AWS_SESSION_TOKEN`](../../environment_variables.md#envvar-AWS_SESSION_TOKEN) - Variable: ansible_aws_ssm_session_token |
| **ssm_document**  string  *added in community.aws 5.2.0* | SSM Session document to use when connecting.  To configure the remote_user (when `become=False`, it is possible to use an SSM Session document and define the `runAsEnabled` and `runAsDefaultUser` parameters. See also <https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-schema.html>  **Configuration:**   - Variable: ansible_aws_ssm_document |
| **ssm_timeout**  integer | Connection timeout seconds.  **Default:** `60`  **Configuration:**   - Variable: ansible_aws_ssm_timeout |

## [Notes](aws_ssm_connection.md#id4)

> **Note:**
>
> - The `community.aws.aws_ssm` connection plugin does not support using the ``remote_user`` and ``ansible_user`` variables to configure the remote user. The ``become_user`` parameter should be used to configure which user to run commands as. Remote commands will often default to running as the ``ssm-agent`` user, however this will also depend on how SSM has been configured.

## [Examples](aws_ssm_connection.md#id5)

```yaml+jinja
# Wait for SSM Agent to be available on the Instance
- name: Wait for connection to be available
  vars:
    ansible_connection: aws_ssm
    ansible_aws_ssm_bucket_name: nameofthebucket
    ansible_aws_ssm_region: us-west-2
    # When the S3 bucket isn't in the same region as the Instance
    # Explicitly setting the addressing style to 'virtual' may be necessary
    # https://repost.aws/knowledge-center/s3-http-307-response
    ansible_aws_ssm_s3_addressing_style: virtual
  tasks:
    - name: Wait for connection
      wait_for_connection:

# Stop Spooler Process on Windows Instances
- name: Stop Spooler Service on Windows Instances
  vars:
    ansible_connection: aws_ssm
    ansible_shell_type: powershell
    ansible_aws_ssm_bucket_name: nameofthebucket
    ansible_aws_ssm_region: us-east-1
  tasks:
    - name: Stop spooler service
      win_service:
        name: spooler
        state: stopped

# Install a Nginx Package on Linux Instance
- name: Install a Nginx Package
  vars:
    ansible_connection: aws_ssm
    ansible_aws_ssm_bucket_name: nameofthebucket
    ansible_aws_ssm_region: us-west-2
  tasks:
    - name: Install a Nginx Package
      yum:
        name: nginx
        state: present

# Create a directory in Windows Instances
- name: Create a directory in Windows Instance
  vars:
    ansible_connection: aws_ssm
    ansible_shell_type: powershell
    ansible_aws_ssm_bucket_name: nameofthebucket
    ansible_aws_ssm_region: us-east-1
  tasks:
    - name: Create a Directory
      win_file:
        path: C:\Windows\temp
        state: directory

# Making use of Dynamic Inventory Plugin
# =======================================
# aws_ec2.yml (Dynamic Inventory - Linux)
# This will return the Instance IDs matching the filter
#plugin: aws_ec2
#regions:
#    - us-east-1
#hostnames:
#    - instance-id
#filters:
#    tag:SSMTag: ssmlinux
# -----------------------
- name: install aws-cli
  hosts: all
  gather_facts: false
  vars:
    ansible_connection: aws_ssm
    ansible_aws_ssm_bucket_name: nameofthebucket
    ansible_aws_ssm_region: us-east-1
  tasks:
  - name: aws-cli
    raw: yum install -y awscli
    tags: aws-cli
# Execution: ansible-playbook linux.yaml -i aws_ec2.yml
# The playbook tasks will get executed on the instance ids returned from the dynamic inventory plugin using ssm connection.
# =====================================================
# aws_ec2.yml (Dynamic Inventory - Windows)
#plugin: aws_ec2
#regions:
#    - us-east-1
#hostnames:
#    - instance-id
#filters:
#    tag:SSMTag: ssmwindows
# -----------------------
- name: Create a dir.
  hosts: all
  gather_facts: false
  vars:
    ansible_connection: aws_ssm
    ansible_shell_type: powershell
    ansible_aws_ssm_bucket_name: nameofthebucket
    ansible_aws_ssm_region: us-east-1
  tasks:
    - name: Create the directory
      win_file:
        path: C:\Temp\SSM_Testing5
        state: directory
# Execution:  ansible-playbook win_file.yaml -i aws_ec2.yml
# The playbook tasks will get executed on the instance ids returned from the dynamic inventory plugin using ssm connection.

# Install a Nginx Package on Linux Instance; with specific SSE for file transfer
- name: Install a Nginx Package
  vars:
    ansible_connection: aws_ssm
    ansible_aws_ssm_bucket_name: nameofthebucket
    ansible_aws_ssm_region: us-west-2
    ansible_aws_ssm_bucket_sse_mode: 'aws:kms'
    ansible_aws_ssm_bucket_sse_kms_key_id: alias/kms-key-alias
  tasks:
    - name: Install a Nginx Package
      yum:
        name: nginx
        state: present

# Install a Nginx Package on Linux Instance; with dedicated SSM document
- name: Install a Nginx Package
  vars:
    ansible_connection: aws_ssm
    ansible_aws_ssm_bucket_name: nameofthebucket
    ansible_aws_ssm_region: us-west-2
    ansible_aws_ssm_document: nameofthecustomdocument
  tasks:
    - name: Install a Nginx Package
      yum:
        name: nginx
        state: present
```

### Authors

- Pat Sharkey (@psharkey)
- HanumanthaRao MVL (@hanumantharaomvl)
- Gaurav Ashtikar (@gau1991)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
