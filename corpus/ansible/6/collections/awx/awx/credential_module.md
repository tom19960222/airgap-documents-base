---
collection: ansible
version: "6"
title: "awx.awx.credential module – create, update, or destroy Automation Platform Controller credential."
source_url: https://docs.ansible.com/projects/ansible/6/collections/awx/awx/credential_module.html
fetched_at: 2026-07-27T16:45:23+00:00
---
# awx.awx.credential module – create, update, or destroy Automation Platform Controller credential.

> **Note:**
>
> This module is part of the [awx.awx collection](https://galaxy.ansible.com/awx/awx) (version 21.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install awx.awx`.
>
> To use it in a playbook, specify: `awx.awx.credential`.

- [Synopsis](credential_module.md#synopsis)
- [Parameters](credential_module.md#parameters)
- [Notes](credential_module.md#notes)
- [Examples](credential_module.md#examples)

## [Synopsis](credential_module.md#id1)

- Create, update, or destroy Automation Platform Controller credentials. See <https://www.ansible.com/tower> for an overview.

## [Parameters](credential_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  added in awx.awx 3.7.0 | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **copy_from**  string | Name or id to copy the credential from.  This will copy an existing credential and change any parameters supplied.  The new credential name will be the one provided in the name parameter.  The organization parameter is not used in this, to facilitate copy from one organization to another.  Provide the id or use the lookup plugin to provide the id if multiple credentials share the same name. |
| **credential_type**  string | The credential type being created.  Can be a built-in credential type such as “Machine”, or a custom credential type such as “My Credential Type”  Choices include Amazon Web Services, Ansible Galaxy/Automation Hub API Token, Centrify Vault Credential Provider Lookup, Container Registry, CyberArk AIM Central Credential Provider Lookup, CyberArk Conjur Secrets Manager Lookup, Google Compute Engine, GitHub Personal Access Token, GitLab Personal Access Token, GPG Public Key, HashiCorp Vault Secret Lookup, HashiCorp Vault Signed SSH, Insights, Machine, Microsoft Azure Key Vault, Microsoft Azure Resource Manager, Network, OpenShift or Kubernetes API Bearer Token, OpenStack, Red Hat Ansible Automation Platform, Red Hat Satellite 6, Red Hat Virtualization, Source Control, Thycotic DevOps Secrets Vault, Thycotic Secret Server, Vault, VMware vCenter, or a custom credential type |
| **description**  string | The description to use for the credential. |
| **inputs**  dictionary | Credential inputs where the keys are var names used in templating. Refer to the Automation Platform Controller documentation for example syntax.  authorize (use this for net type)  authorize_password (password for net credentials that require authorize)  client (client or application ID for azure_rm type)  security_token (STS token for aws type)  secret (secret token for azure_rm type)  tenant (tenant ID for azure_rm type)  subscription (subscription ID for azure_rm type)  domain (domain for openstack type)  become_method (become method to use for privilege escalation; some examples are “None”, “sudo”, “su”, “pbrun”)  become_username (become username; use “ASK” and launch job to be prompted)  become_password (become password; use “ASK” and launch job to be prompted)  vault_password (the vault password; use “ASK” and launch job to be prompted)  project (project that should use this credential for GCP)  host (the host for this credential)  username (the username for this credential; ``access_key`` for AWS)  password (the password for this credential; ``secret_key`` for AWS, ``api_key`` for RAX)  ssh_key_data (SSH private key content; to extract the content from a file path, use the lookup function (see examples))  vault_id (the vault identifier; this parameter is only valid if `kind` is specified as `vault`.)  ssh_key_unlock (unlock password for ssh_key; use “ASK” and launch job to be prompted)  gpg_public_key (GPG Public Key used for signature validation) |
| **name**  string / required | The name to use for the credential. |
| **new_name**  string | Setting this option will change the existing name (looked up via the name field. |
| **organization**  string | Organization that should own the credential. |
| **state**  string | Desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **team**  string | Team that should own this credential. |
| **update_secrets**  boolean | `true` will always update encrypted values.  `false` will only updated encrypted values if a change is absolutely known to be needed.  Choices:   - `false` - `true` ← (default) |
| **user**  string | User that should own this credential. |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  Choices:   - `false` - `true` |

## [Notes](credential_module.md#id3)

> **Note:**
>
> - Values `inputs` and the other deprecated fields (such as `tenant`) are replacements of existing values. See the last 4 examples for details.
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](credential_module.md#id4)

```yaml+jinja
- name: Add machine credential
  credential:
    name: Team Name
    description: Team Description
    organization: test-org
    credential_type: Machine
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Create a valid SCM credential from a private_key file
  credential:
    name: SCM Credential
    organization: Default
    state: present
    credential_type: Source Control
    inputs:
      username: joe
      password: secret
      ssh_key_data: "{{ lookup('file', '/tmp/id_rsa') }}"
      ssh_key_unlock: "passphrase"

- name: Fetch private key
  slurp:
    src: '$HOME/.ssh/aws-private.pem'
  register: aws_ssh_key

- name: Add Credential
  credential:
    name: Workshop Credential
    credential_type: Machine
    organization: Default
    inputs:
      ssh_key_data: "{{ aws_ssh_key['content'] | b64decode }}"
  run_once: true
  delegate_to: localhost

- name: Add Credential with Custom Credential Type
  credential:
    name: Workshop Credential
    credential_type: MyCloudCredential
    organization: Default
    controller_username: admin
    controller_password: ansible
    controller_host: https://localhost

- name: Create a Vault credential (example for notes)
  credential:
    name: Example password
    credential_type: Vault
    organization: Default
    inputs:
      vault_password: 'hello'
      vault_id: 'My ID'

- name: Bad password update (will replace vault_id)
  credential:
    name: Example password
    credential_type: Vault
    organization: Default
    inputs:
      vault_password: 'new_password'

- name: Another bad password update (will replace vault_id)
  credential:
    name: Example password
    credential_type: Vault
    organization: Default
    vault_password: 'new_password'

- name: A safe way to update a password and keep vault_id
  credential:
    name: Example password
    credential_type: Vault
    organization: Default
    inputs:
      vault_password: 'new_password'
      vault_id: 'My ID'

- name: Copy Credential
  credential:
    name: Copy password
    copy_from: Example password
    credential_type: Vault
    organization: Foo
```

### Authors

- Wayne Witzel III (@wwitzel3)

### Collection links

[Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
[Homepage](https://www.ansible.com/)
[Repository (Sources)](https://github.com/ansible/awx)
