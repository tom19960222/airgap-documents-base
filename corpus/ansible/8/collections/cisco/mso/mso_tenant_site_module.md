---
collection: ansible
version: "8"
title: "cisco.mso.mso_tenant_site module – Manage tenants with cloud sites."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/mso/mso_tenant_site_module.html
fetched_at: 2026-07-28T01:38:18+00:00
---
# cisco.mso.mso_tenant_site module – Manage tenants with cloud sites.

> **Note:**
>
> This module is part of the [cisco.mso collection](https://galaxy.ansible.com/ui/repo/published/cisco/mso/) (version 2.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.mso`.
> You need further requirements to be able to use this module,
> see [Requirements](mso_tenant_site_module.md#ansible-collections-cisco-mso-mso-tenant-site-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.mso.mso_tenant_site`.

- [Synopsis](mso_tenant_site_module.md#synopsis)
- [Requirements](mso_tenant_site_module.md#requirements)
- [Parameters](mso_tenant_site_module.md#parameters)
- [Notes](mso_tenant_site_module.md#notes)
- [Examples](mso_tenant_site_module.md#examples)

## [Synopsis](mso_tenant_site_module.md#id1)

- Manage tenants with cloud sites on Cisco ACI Multi-Site.

## [Requirements](mso_tenant_site_module.md#id2)

The below requirements are needed on the host that executes this module.

- Multi Site Orchestrator v2.1 or newer

## [Parameters](mso_tenant_site_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  string | AWS account’s access key id. This is required when aws_trusted is set to false. |
| **aws_account_org**  boolean | AWS account for organization.  **Choices:**   - `false` ← (default) - `true` |
| **aws_trusted**  boolean | AWS account’s access in trusted mode. Credentials are required, when set to false.  **Choices:**   - `false` - `true` |
| **azure_access_type**  string | Managed mode for Azure.  Unmanaged mode for Azure.  Shared mode if the attribute is not specified.  **Choices:**   - `"managed"` - `"unmanaged"` - `"shared"` ← (default) |
| **azure_active_directory_id**  string | Azure account’s active directory id.  This attribute is required when azure_access_type is in unmanaged mode. |
| **azure_active_directory_name**  string | Azure account’s active directory name. Example being ‘CiscoINSBUAd’ as active directory name.  This attribute is required when azure_access_type is in unmanaged mode. |
| **azure_application_id**  string | Azure account’s application id.  This attribute is required when azure_access_type is either in managed mode or unmanaged mode. |
| **azure_credential_name**  string | Azure account’s credential name.  This attribute is required when azure_access_type is in unmanaged mode. |
| **azure_subscription_id**  string | Azure account’s subscription id.  This attribute is required when azure_access_type is either in managed mode or unmanaged mode. |
| **cloud_account**  string | Required for cloud site.  Account id of AWS in the form ‘000000000000’.  Account id of Azure in the form ‘uni/tn-(tenant_name)/act-[(subscription_id)]-azure_vendor-azure’.  Example values inside account id of Azure ‘(tenant_name)=tenant_test and (subscription_id)=10’. |
| **host**  aliases: hostname  string | IP Address or hostname of the ACI Multi Site Orchestrator host.  If the value is not specified in the task, the value of environment variable `MSO_HOST` will be used instead. |
| **login_domain**  string | The login domain name to use for authentication.  The default value is Local.  If the value is not specified in the task, the value of environment variable `MSO_LOGIN_DOMAIN` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_login_domain` will be used if this attribute is not specified. |
| **output_level**  string | Influence the output of this MSO module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `MSO_OUTPUT_LEVEL` will be used instead.  **Choices:**   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **password**  string | The password to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for the REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `MSO_PORT` will be used instead. |
| **secret_key**  string | secret key of AWS for untrusted account. Required when aws_trusted is set to false.  secret key of Azure account for unmanaged identity. Required in unmanaged mode of Azure account. |
| **security_domains**  list / elements=string | List of security domains for sites.  **Default:** `[]` |
| **site**  aliases: name  string | The name of the site.  This can either be cloud site or non-cloud site. |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"query"` |
| **tenant**  string / required | The name of the tenant. |
| **timeout**  integer | The socket level timeout in seconds.  The default value is 30 seconds.  If the value is not specified in the task, the value of environment variable `MSO_TIMEOUT` will be used instead. |
| **use_proxy**  boolean | If `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `MSO_USE_PROXY` will be used instead.  The default is `true`.  **Choices:**   - `false` - `true` |
| **use_ssl**  boolean | If `false`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `MSO_USE_SSL` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_use_ssl` will be used if this attribute is not specified.  The default is `false` when using a HTTPAPI connection plugin (mso or nd) and `true` when using the legacy connection method (only for mso).  **Choices:**   - `false` - `true` |
| **username**  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only set to `false` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `MSO_VALIDATE_CERTS` will be used instead.  The default is `true`.  **Choices:**   - `false` - `true` |

## [Notes](mso_tenant_site_module.md#id4)

> **Note:**
>
> - This module was written to support Multi Site Orchestrator v2.1 or newer. Some or all functionality may not work on earlier versions.

## [Examples](mso_tenant_site_module.md#id5)

```yaml+jinja
- name: Associate a non-cloud site with a tenant
  cisco.mso.mso_tenant_site:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    tenant: tenant_name
    site: site_name
    state: present
  delegate_to: localhost

- name: Associate AWS site with a tenant, with aws_trusted set to true
  cisco.mso.mso_tenant_site:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    tenant: tenant_name
    site: site_name
    cloud_account: '000000000000'
    aws_trusted: true
    state: present
  delegate_to: localhost

- name: Associate AWS site with a tenant, with aws_trusted set to false
  cisco.mso.mso_tenant_site:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    tenant: tenant_name
    site: AWS
    cloud_account: '000000000000'
    aws_trusted: false
    aws_access_key: '1'
    secret_key: '0'
    aws_account_org: false
    state: present
  delegate_to: localhost

- name: Associate Azure site in managed mode
  mso.cisco.mso_tenant_site:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    tenant: tenant_name
    site: site_name
    cloud_account: uni/tn-ansible_test/act-[9]-azure_vendor-azure
    azure_access_type: managed
    azure_subscription_id: '9'
    azure_application_id: '100'
    state: present
  delegate_to: localhost

- name: Associate Azure site in unmanaged mode
  mso.cisco.mso_tenant_site:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    tenant: tenant_name
    site: site_name
    cloud_account: uni/tn-ansible_test/act-[9]-azure_vendor-azure
    azure_access_type: unmanaged
    azure_subscription_id: '9'
    azure_application_id: '100'
    azure_credential_name: cApicApp
    secret_key: iins
    azure_active_directory_id: '32'
    azure_active_directory_name: CiscoINSBUAd
    state: present
  delegate_to: localhost

- name: Dissociate a site
  cisco.mso.mso_tenant_site:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    tenant: tenant_name
    site: site_name
    state: absent
  delegate_to: localhost

- name: Query a site
  cisco.mso.mso_tenant_site:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    tenant: tenant_name
    site: site_name
    state: query
  delegate_to: localhost

- name: Query all sites of a tenant
  cisco.mso.mso_tenant_site:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    tenant: tenant_name
    state: query
  delegate_to: localhost
  register: query_result
```

### Authors

- Shreyas Srish (@shrsr)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-mso/issues)
- [Homepage](https://cisco.com/go/aci)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-mso)
