---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm inventory – Azure Resource Manager inventory plugin"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_inventory.html
fetched_at: 2026-07-27T16:47:29+00:00
---
# azure.azcollection.azure_rm inventory – Azure Resource Manager inventory plugin

> **Note:**
>
> This inventory plugin is part of the [azure.azcollection collection](https://galaxy.ansible.com/azure/azcollection) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install azure.azcollection`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](azure_rm_inventory.md#ansible-collections-azure-azcollection-azure-rm-inventory-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm`.

- [Synopsis](azure_rm_inventory.md#synopsis)
- [Requirements](azure_rm_inventory.md#requirements)
- [Parameters](azure_rm_inventory.md#parameters)
- [Notes](azure_rm_inventory.md#notes)
- [See Also](azure_rm_inventory.md#see-also)
- [Examples](azure_rm_inventory.md#examples)

## [Synopsis](azure_rm_inventory.md#id1)

- Query VM details from Azure Resource Manager
- Requires a YAML configuration file whose name ends with ‘azure_rm.(yml|yaml)’
- By default, sets `ansible_host` to the first public IP address found (preferring the primary NIC). If no public IPs are found, the first private IP (also preferring the primary NIC). The default may be overridden via `hostvar_expressions`; see examples.

## [Requirements](azure_rm_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  added in azure.azcollection 0.0.1 | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  added in azure.azcollection 0.0.1 | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  Default: `"latest"` |
| **auth_source**  string  added in azure.azcollection 0.0.1 | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  Choices:   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **batch_fetch**  string | To improve performance, results are fetched using an unsupported batch API. Disabling `batch_fetch` uses a much slower serial fetch, resulting in many more round-trips. Generally only useful for troubleshooting.  Default: `true` |
| **cert_validation_mode**  string  added in azure.azcollection 0.0.1 | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  Choices:   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  added in azure.azcollection 0.0.1 | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  Default: `"AzureCloud"` |
| **compose**  dictionary | Create vars from jinja2 expressions.  Default: `{}` |
| **conditional_groups**  string | A mapping of group names to Jinja2 expressions. When the mapped expression is true, the host is added to the named group. |
| **default_host_filters**  string | A default set of filters that is applied in addition to the conditions in `exclude_host_filters` to exclude powered-off and not-fully-provisioned hosts. Set this to a different value or empty list if you need to include hosts in these states.  Default: `["powerstate != \"running\"", "provisioning_state != \"succeeded\""]` |
| **exclude_host_filters**  string | Excludes hosts from the inventory with a list of Jinja2 conditional expressions. Each expression in the list is evaluated for each host; when the expression is true, the host is excluded from the inventory.  Default: `[]` |
| **fail_on_template_errors**  string | When false, template failures during group and filter processing are silently ignored (eg, if a filter or group expression refers to an undefined host variable)  Choices:   - `true` ← (default) - `false` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  Default: `{}` |
| **hostnames**  list / elements=string | A list of Jinja2 expressions in order of precedence to compose inventory_hostname.  Ignores expression if result is an empty string or None value.  By default, inventory_hostname is generated to be globally unique based on the VM host name. See `plain_host_names` for more details on the default.  An expression of ‘default’ will force using the default hostname generator if no previous hostname expression resulted in a valid hostname.  Use ``default_inventory_hostname`` to access the default hostname generator’s value in any of the Jinja2 expressions.  Default: `["default"]` |
| **hostvar_expressions**  string | A mapping of hostvar names to Jinja2 expressions. The value for each host is the result of the Jinja2 expression (which may refer to any of the host’s existing variables at the time this inventory plugin runs). |
| **include_vm_resource_groups**  string | A list of resource group names to search for virtual machines. ‘\\*’ will include all resource groups in the subscription.  Default: `["*"]` |
| **include_vmss_resource_groups**  string | A list of resource group names to search for virtual machine scale sets (VMSSs). ‘\\*’ will include all resource groups in the subscription.  Default: `[]` |
| **keyed_groups**  list / elements=dictionary | Creates groups based on the value of a host variable. Requires a list of dictionaries, defining `key` (the source dictionary-typed variable), `prefix` (the prefix to use for the new group name), and optionally `separator` (which defaults to `_`)  Default: `[]` |
| **default_value**  string  added in ansible-core 2.12 | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  Default: `""` |
| **separator**  string | separator used to build the keyed group name  Default: `"_"` |
| **trailing_separator**  boolean  added in ansible-core 2.12 | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  Choices:   - `false` - `true` ← (default) |
| **leading_separator**  boolean  added in ansible-core 2.11 | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  Choices:   - `false` - `true` ← (default) |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **plain_host_names**  boolean  added in azure.azcollection 0.0.1 | By default this plugin will use globally unique host names. This option allows you to override that, and use the name that matches the old inventory script naming.  This is not the default, as these names are not truly unique, and can conflict with other hosts. The default behavior will add extra hashing to the end of the hostname to prevent such conflicts.  Choices:   - `false` ← (default) - `true` |
| **plugin**  string / required | marks this as an instance of the ‘azure_rm’ plugin  Choices:   - `"azure_rm"` - `"azure.azcollection.azure_rm"` |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  Choices:   - `false` ← (default) - `true` |
| **subscription_id**  string | Your Azure subscription Id. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **use_contrib_script_compatible_sanitization**  boolean  added in azure.azcollection 0.0.1 | By default this plugin is using a general group name sanitization to create safe and usable group names for use in Ansible. This option allows you to override that, in efforts to allow migration from the old inventory script and matches the sanitization of groups when the script’s ``replace_dash_in_groups`` option is set to ``False``. To replicate behavior of ``replace_dash_in_groups = True`` with constructed groups, you will need to replace hyphens with underscores via the regex_replace filter for those entries.  For this to work you should also turn off the TRANSFORM_INVALID_GROUP_CHARS setting, otherwise the core engine will just use the standard sanitization on top.  This is not the default as such names break certain functionality as not all characters are valid Python identifiers which group names end up being used as.  Choices:   - `false` ← (default) - `true` |
| **use_extra_vars**  boolean  added in ansible-core 2.11 | Merge extra vars into the available variables for composition (highest precedence).  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_inventory.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_inventory.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_inventory.md#id6)

```yaml+jinja
# The following host variables are always available:
# public_ipv4_addresses: all public IP addresses, with the primary IP config from the primary NIC first
# public_dns_hostnames: all public DNS hostnames, with the primary IP config from the primary NIC first
# private_ipv4_addresses: all private IP addressses, with the primary IP config from the primary NIC first
# id: the VM's Azure resource ID, eg /subscriptions/00000000-0000-0000-1111-1111aaaabb/resourceGroups/my_rg/providers/Microsoft.Compute/virtualMachines/my_vm
# location: the VM's Azure location, eg 'westus', 'eastus'
# name: the VM's resource name, eg 'myvm'
# os_profile: The VM OS properties, a dictionary, only system is currently available, eg 'os_profile.system not in ['linux']'
# powerstate: the VM's current power state, eg: 'running', 'stopped', 'deallocated'
# provisioning_state: the VM's current provisioning state, eg: 'succeeded'
# tags: dictionary of the VM's defined tag values
# resource_type: the VM's resource type, eg: 'Microsoft.Compute/virtualMachine', 'Microsoft.Compute/virtualMachineScaleSets/virtualMachines'
# vmid: the VM's internal SMBIOS ID, eg: '36bca69d-c365-4584-8c06-a62f4a1dc5d2'
# vmss: if the VM is a member of a scaleset (vmss), a dictionary including the id and name of the parent scaleset
# availability_zone: availability zone in which VM is deployed, eg '1','2','3'
#
# The following host variables are sometimes availble:
# computer_name: the Operating System's hostname. Will not be available if azure agent is not available and picking it up.

# sample 'myazuresub.azure_rm.yaml'

# required for all azure_rm inventory plugin configs
plugin: azure.azcollection.azure_rm

# forces this plugin to use a CLI auth session instead of the automatic auth source selection (eg, prevents the
# presence of 'ANSIBLE_AZURE_RM_X' environment variables from overriding CLI auth)
auth_source: cli

# fetches VMs from an explicit list of resource groups instead of default all (- '*')
include_vm_resource_groups:
- myrg1
- myrg2

# fetches VMs from VMSSs in all resource groups (defaults to no VMSS fetch)
include_vmss_resource_groups:
- '*'

# places a host in the named group if the associated condition evaluates to true
conditional_groups:
  # since this will be true for every host, every host sourced from this inventory plugin config will be in the
  # group 'all_the_hosts'
  all_the_hosts: true
  # if the VM's "name" variable contains "dbserver", it will be placed in the 'db_hosts' group
  db_hosts: "'dbserver' in name"

# adds variables to each host found by this inventory plugin, whose values are the result of the associated expression
hostvar_expressions:
  my_host_var:
  # A statically-valued expression has to be both single and double-quoted, or use escaped quotes, since the outer
  # layer of quotes will be consumed by YAML. Without the second set of quotes, it interprets 'staticvalue' as a
  # variable instead of a string literal.
  some_statically_valued_var: "'staticvalue'"
  # overrides the default ansible_host value with a custom Jinja2 expression, in this case, the first DNS hostname, or
  # if none are found, the first public IP address.
  ansible_host: (public_dns_hostnames + public_ipv4_addresses) | first

# change how inventory_hostname is generated. Each item is a jinja2 expression similar to hostvar_expressions.
hostnames:
  - tags.vm_name
  - default  # special var that uses the default hashed name

# places hosts in dynamically-created groups based on a variable value.
keyed_groups:
# places each host in a group named 'tag_(tag name)_(tag value)' for each tag on a VM.
- prefix: tag
  key: tags
# places each host in a group named 'azure_loc_(location name)', depending on the VM's location
- prefix: azure_loc
  key: location
# places host in a group named 'some_tag_X' using the value of the 'sometag' tag on a VM as X, and defaulting to the
# value 'none' (eg, the group 'some_tag_none') if the 'sometag' tag is not defined for a VM.
- prefix: some_tag
  key: tags.sometag | default('none')

# excludes a host from the inventory when any of these expressions is true, can refer to any vars defined on the host
exclude_host_filters:
# excludes hosts in the eastus region
- location in ['eastus']
- tags['tagkey'] is defined and tags['tagkey'] == 'tagkey'
- tags['tagkey2'] is defined and tags['tagkey2'] == 'tagkey2'
# excludes hosts that are powered off
- powerstate != 'running'
```

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
