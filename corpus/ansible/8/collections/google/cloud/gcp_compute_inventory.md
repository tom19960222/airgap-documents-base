---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute inventory – Google Cloud Compute Engine inventory source"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_inventory.html
fetched_at: 2026-07-28T01:05:44+00:00
---
# google.cloud.gcp_compute inventory – Google Cloud Compute Engine inventory source

> **Note:**
>
> This inventory plugin is part of the [google.cloud collection](https://galaxy.ansible.com/ui/repo/published/google/cloud/) (version 1.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install google.cloud`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](gcp_compute_inventory.md#ansible-collections-google-cloud-gcp-compute-inventory-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute`.

- [Synopsis](gcp_compute_inventory.md#synopsis)
- [Requirements](gcp_compute_inventory.md#requirements)
- [Parameters](gcp_compute_inventory.md#parameters)
- [Examples](gcp_compute_inventory.md#examples)

## [Synopsis](gcp_compute_inventory.md#id1)

- Get inventory hosts from Google Cloud Platform GCE.
- Uses a YAML configuration file that ends with gcp_compute.(yml|yaml) or gcp.(yml|yaml).

## [Requirements](gcp_compute_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken.  **Configuration:**   - Environment variable: [`GCP_ACCESS_TOKEN`](../../environment_variables.md#envvar-GCP_ACCESS_TOKEN) |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"serviceaccount"` - `"machineaccount"` - `"accesstoken"`   **Configuration:**   - Environment variable: [`GCP_AUTH_KIND`](../../environment_variables.md#envvar-GCP_AUTH_KIND) |
| **cache**  boolean | Toggle to enable/disable the caching of the inventory’s source data, requires a cache plugin setup to work.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory]   cache = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_CACHE`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE) |
| **cache_connection**  string | Cache connection data or path, read cache plugin documentation for specifics.  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ```  ```YAML+Jinja   [inventory]   cache_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_CONNECTION) |
| **cache_plugin**  string | Cache plugin to use for the inventory’s source data.  **Default:** `"memory"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching = memory   ```  ```YAML+Jinja   [inventory]   cache_plugin = memory   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN) |
| **cache_prefix**  string | Prefix to use for cache plugin files/tables  **Default:** `"ansible_inventory_"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [default]   fact_caching_prefix = ansible_inventory_   ```  Removed in: version 2.16 of ansible.builtin  Why: Fixes typing error in INI section name  Alternative: Use the ‘defaults’ section instead  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_inventory_   ```  ```YAML+Jinja   [inventory]   cache_prefix = ansible_inventory_   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX) |
| **cache_timeout**  integer | Cache duration in seconds  **Default:** `3600`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 3600   ```  ```YAML+Jinja   [inventory]   cache_timeout = 3600   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_TIMEOUT) |
| **compose**  dictionary | Create vars from jinja2 expressions.  **Default:** `{}` |
| **filters**  list / elements=string | A list of filter value pairs. Available filters are listed here <https://cloud.google.com/compute/docs/reference/rest/v1/instances/aggregatedList>. Each additional filter in the list will be added as an AND condition (filter1 and filter2) |
| **folders**  list / elements=string | A folder that contains many projects |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **hostnames**  list / elements=string | A list of options that describe the ordering for which hostnames should be assigned. Currently supported hostnames are ‘public_ip’, ‘private_ip’, ‘name’ or ‘labels.vm_name’.  **Default:** `["public_ip", "private_ip", "name"]` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  **Default:** `[]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **name_suffix**  string | Custom domain suffix. If set, this string will be appended to all hosts.  **Default:** `""` |
| **plugin**  string / required | token that ensures this is a source file for the ‘gcp_compute’ plugin.  **Choices:**   - `"google.cloud.gcp_compute"` - `"gcp_compute"` |
| **projects**  list / elements=string | A list of projects in which to describe GCE instances. |
| **retrieve_image_info**  boolean | Populate the `image` host fact for the instances returned with the GCP image name  By default this plugin does not attempt to resolve the boot image of an instance to the image name cataloged in GCP because of the performance overhead of the task.  Unless this option is enabled, the `image` host variable will be `null`  **Choices:**   - `false` ← (default) - `true` |
| **scopes**  list / elements=string | list of authentication scopes  **Default:** `["https://www.googleapis.com/auth/compute"]`  **Configuration:**   - Environment variable: [`GCP_SCOPES`](../../environment_variables.md#envvar-GCP_SCOPES) |
| **service_account_contents**  string | A string representing the contents of a Service Account JSON file. This should not be passed in as a dictionary, but a string that has the exact contents of a service account json file (valid JSON).  **Configuration:**   - Environment variable: [`GCP_SERVICE_ACCOUNT_CONTENTS`](../../environment_variables.md#envvar-GCP_SERVICE_ACCOUNT_CONTENTS) |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email.  **Configuration:**   - Environment variable: [`GCP_SERVICE_ACCOUNT_EMAIL`](../../environment_variables.md#envvar-GCP_SERVICE_ACCOUNT_EMAIL) |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type.  **Configuration:**   - Environment variable: [`GCP_SERVICE_ACCOUNT_FILE`](../../environment_variables.md#envvar-GCP_SERVICE_ACCOUNT_FILE) - Environment variable: [`GCE_CREDENTIALS_FILE_PATH`](../../environment_variables.md#envvar-GCE_CREDENTIALS_FILE_PATH) |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **use_contrib_script_compatible_sanitization**  boolean | By default this plugin is using a general group name sanitization to create safe and usable group names for use in Ansible. This option allows you to override that, in efforts to allow migration from the old inventory script.  For this to work you should also turn off the TRANSFORM_INVALID_GROUP_CHARS setting, otherwise the core engine will just use the standard sanitization on top.  This is not the default as such names break certain functionality as not all characters are valid Python identifiers which group names end up being used as.  **Choices:**   - `false` ← (default) - `true` |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **vars_prefix**  string | prefix to apply to host variables, does not include facts nor params  **Default:** `""` |
| **zones**  list / elements=string | A list of regions in which to describe GCE instances. If none provided, it defaults to all zones available to a given project. |

## [Examples](gcp_compute_inventory.md#id4)

```yaml+jinja
plugin: google.cloud.gcp_compute
zones: # populate inventory with instances in these regions
  - us-east1-a
projects:
  - gcp-prod-gke-100
  - gcp-cicd-101
filters:
  - status = RUNNING
  - scheduling.automaticRestart = true AND status = RUNNING
service_account_file: /tmp/service_account.json
auth_kind: serviceaccount
scopes:
 - 'https://www.googleapis.com/auth/cloud-platform'
 - 'https://www.googleapis.com/auth/compute.readonly'
keyed_groups:
  # Create groups from GCE labels
  - prefix: gcp
    key: labels
name_suffix: .example.com
hostnames:
  # List host by name instead of the default public ip
  - name
compose:
  # Set an inventory parameter to use the Public IP address to connect to the host
  # For Private ip use "networkInterfaces[0].networkIP"
  ansible_host: networkInterfaces[0].accessConfigs[0].natIP
```

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
