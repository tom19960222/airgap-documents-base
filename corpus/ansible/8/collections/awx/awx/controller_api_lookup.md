---
collection: ansible
version: "8"
title: "awx.awx.controller_api lookup – Search the API for objects"
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/controller_api_lookup.html
fetched_at: 2026-07-28T01:11:51+00:00
---
# awx.awx.controller_api lookup – Search the API for objects

> **Note:**
>
> This lookup plugin is part of the [awx.awx collection](https://galaxy.ansible.com/ui/repo/published/awx/awx/) (version 22.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install awx.awx`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](controller_api_lookup.md#ansible-collections-awx-awx-controller-api-lookup-requirements) for details.
>
> To use it in a playbook, specify: `awx.awx.controller_api`.

- [Synopsis](controller_api_lookup.md#synopsis)
- [Requirements](controller_api_lookup.md#requirements)
- [Terms](controller_api_lookup.md#terms)
- [Keyword parameters](controller_api_lookup.md#keyword-parameters)
- [Notes](controller_api_lookup.md#notes)
- [Examples](controller_api_lookup.md#examples)
- [Return Value](controller_api_lookup.md#return-value)

## [Synopsis](controller_api_lookup.md#id1)

- Returns GET requests from the Automation Platform Controller API. See <https://docs.ansible.com/ansible-tower/latest/html/towerapi/index.html> for API usage.
- For use that is cross-compatible between the awx.awx and ansible.controller collection see the controller_meta module

Aliases: tower_api

## [Requirements](controller_api_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- None

## [Terms](controller_api_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | The endpoint to query, i.e. teams, users, tokens, job_templates, etc. |

## [Keyword parameters](controller_api_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('awx.awx.controller_api', key1=value1, key2=value2, ...)` and `query('awx.awx.controller_api', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **expect_objects**  aliases: expect_object  boolean | Error if the response does not contain either a detail view or a list view.  **Choices:**   - `false` ← (default) - `true` |
| **expect_one**  boolean | Error if the response contains more than one object.  **Choices:**   - `false` ← (default) - `true` |
| **host**  string | The network address of your Automation Platform Controller host.  **Configuration:**   - Environment variable: [`CONTROLLER_HOST`](../../environment_variables.md#envvar-CONTROLLER_HOST) - Environment variable: [`TOWER_HOST`](../../environment_variables.md#envvar-TOWER_HOST)  Removed in: version 4.0.0  Why: Collection name change  Alternative: CONTROLLER_HOST |
| **max_objects**  integer | if `return_all` is true, this is the maximum of number of objects to return from the list.  If a list view returns more an max_objects an exception will be raised  **Default:** `1000` |
| **oauth_token**  string | The OAuth token to use.  **Configuration:**   - Environment variable: [`CONTROLLER_OAUTH_TOKEN`](../../environment_variables.md#envvar-CONTROLLER_OAUTH_TOKEN) - Environment variable: [`TOWER_OAUTH_TOKEN`](../../environment_variables.md#envvar-TOWER_OAUTH_TOKEN)  Removed in: version 4.0.0  Why: Collection name change  Alternative: CONTROLLER_OAUTH_TOKEN |
| **password**  string | The password for your controller user.  **Configuration:**   - Environment variable: [`CONTROLLER_PASSWORD`](../../environment_variables.md#envvar-CONTROLLER_PASSWORD) - Environment variable: [`TOWER_PASSWORD`](../../environment_variables.md#envvar-TOWER_PASSWORD)  Removed in: version 4.0.0  Why: Collection name change  Alternative: CONTROLLER_PASSWORD |
| **query_params**  aliases: query, data, filter, params  dictionary | The query parameters to search for in the form of key/value pairs. |
| **request_timeout**  float | Specify the timeout Ansible should use in requests to the controller host.  Defaults to 10 seconds  This will not work with the export or import modules.  **Configuration:**   - Environment variable: [`CONTROLLER_REQUEST_TIMEOUT`](../../environment_variables.md#envvar-CONTROLLER_REQUEST_TIMEOUT) |
| **return_all**  boolean | If the response is paginated, return all pages.  **Choices:**   - `false` ← (default) - `true` |
| **return_ids**  aliases: return_id  boolean | If response contains objects, promote the id key to the top-level entries in the list.  Allows looking up a related object and passing it as a parameter to another module.  This will convert the return to a string or list of strings depending on the number of selected items.  **Choices:**   - `false` ← (default) - `true` |
| **return_objects**  boolean | If a list view is returned, promote the list of results to the top-level of list returned.  Allows using this lookup plugin to loop over objects without additional work.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | The user that you plan to use to access inventories on the controller.  **Configuration:**   - Environment variable: [`CONTROLLER_USERNAME`](../../environment_variables.md#envvar-CONTROLLER_USERNAME) - Environment variable: [`TOWER_USERNAME`](../../environment_variables.md#envvar-TOWER_USERNAME)  Removed in: version 4.0.0  Why: Collection name change  Alternative: CONTROLLER_USERNAME |
| **verify_ssl**  aliases: validate_certs  boolean | Specify whether Ansible should verify the SSL certificate of the controller host.  Defaults to True, but this is handled by the shared module_utils code  **Choices:**   - `false` - `true`   **Configuration:**   - Environment variable: [`CONTROLLER_VERIFY_SSL`](../../environment_variables.md#envvar-CONTROLLER_VERIFY_SSL) - Environment variable: [`TOWER_VERIFY_SSL`](../../environment_variables.md#envvar-TOWER_VERIFY_SSL)  Removed in: version 4.0.0  Why: Collection name change  Alternative: CONTROLLER_VERIFY_SSL |

## [Notes](controller_api_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('awx.awx.controller_api', term1, term2, key1=value1, key2=value2)` and `query('awx.awx.controller_api', term1, term2, key1=value1, key2=value2)`
> - If the query is not filtered properly this can cause a performance impact.
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](controller_api_lookup.md#id6)

```yaml+jinja
- name: Load the UI settings
  set_fact:
    controller_settings: "{{ lookup('awx.awx.controller_api', 'settings/ui') }}"

- name: Load the UI settings specifying the connection info
  set_fact:
    controller_settings: "{{ lookup('awx.awx.controller_api', 'settings/ui', host='controller.example.com',
                             username='admin', password=my_pass_var, verify_ssl=False) }}"

- name: Report the usernames of all users with admin privs
  debug:
    msg: "Admin users: {{ query('awx.awx.controller_api', 'users', query_params={ 'is_superuser': true }) | map(attribute='username') | join(', ') }}"

- name: debug all organizations in a loop  # use query to return a list
  debug:
    msg: "Organization description={{ item['description'] }} id={{ item['id'] }}"
  loop: "{{ query('awx.awx.controller_api', 'organizations') }}"
  loop_control:
    label: "{{ item['name'] }}"

- name: Make sure user 'john' is an org admin of the default org if the user exists
  role:
    organization: Default
    role: admin
    user: john
  when: "lookup('awx.awx.controller_api', 'users', query_params={ 'username': 'john' }) | length == 1"

- name: Create an inventory group with all 'foo' hosts
  group:
    name: "Foo Group"
    inventory: "Demo Inventory"
    hosts: >-
      {{ query(
           'awx.awx.controller_api',
            'hosts',
            query_params={ 'name__startswith' : 'foo', },
        ) | map(attribute='name') | list }}
  register: group_creation
```

## [Return Value](controller_api_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  dictionary | Response from the API  **Returned:** on successful request |

### Authors

- John Westcott IV (@john-westcott-iv)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
