---
collection: ansible
version: "6"
title: "cisco.meraki.meraki_mx_content_filtering module – Edit Meraki MX content filtering policies"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/meraki_mx_content_filtering_module.html
fetched_at: 2026-07-27T17:00:32+00:00
---
# cisco.meraki.meraki_mx_content_filtering module – Edit Meraki MX content filtering policies

> **Note:**
>
> This module is part of the [cisco.meraki collection](https://galaxy.ansible.com/cisco/meraki) (version 2.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.meraki`.
>
> To use it in a playbook, specify: `cisco.meraki.meraki_mx_content_filtering`.

- [Synopsis](meraki_mx_content_filtering_module.md#synopsis)
- [Parameters](meraki_mx_content_filtering_module.md#parameters)
- [Notes](meraki_mx_content_filtering_module.md#notes)
- [Examples](meraki_mx_content_filtering_module.md#examples)
- [Return Values](meraki_mx_content_filtering_module.md#return-values)

## [Synopsis](meraki_mx_content_filtering_module.md#id1)

- Allows for setting policy on content filtering.

## [Parameters](meraki_mx_content_filtering_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allowed_urls**  list / elements=string | List of URL patterns which should be allowed. |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable MERAKI_KEY is not set. |
| **blocked_categories**  list / elements=string | List of content categories which should be blocked.  Use the `meraki_content_filtering_facts` module for a full list of categories. |
| **blocked_urls**  list / elements=string | List of URL patterns which should be blocked. |
| **category_list_size**  string | Determines whether a network filters fo rall URLs in a category or only the list of top blocked sites.  Choices:   - `"top sites"` - `"full list"` |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  Default: `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  Default: `60` |
| **net_id**  string | ID number of a network. |
| **net_name**  aliases: network  string | Name of a network. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  Choices:   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  Choices:   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  Default: `165` |
| **state**  string | States that a policy should be created or modified.  Choices:   - `"present"` ← (default) - `"query"` |
| **subset**  string | Display only certain facts.  Choices:   - `"categories"` - `"policy"` |
| **timeout**  integer | Time to timeout for HTTP requests.  Default: `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](meraki_mx_content_filtering_module.md#id3)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_mx_content_filtering_module.md#id4)

```yaml+jinja
- name: Set single allowed URL pattern
  meraki_content_filtering:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourMXNet
    allowed_urls:
      - "http://www.ansible.com/*"

- name: Set blocked URL category
  meraki_content_filtering:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourMXNet
    state: present
    category_list_size: full list
    blocked_categories:
      - "Adult and Pornography"

- name: Remove match patterns and categories
  meraki_content_filtering:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourMXNet
    state: present
    category_list_size: full list
    allowed_urls: []
    blocked_urls: []
```

## [Return Values](meraki_mx_content_filtering_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information about the created or manipulated object.  Returned: info |
| **allowed_url_patterns**  list / elements=string | Explicitly permitted URL patterns  Returned: query for policy  Sample: `["http://www.ansible.com"]` |
| **blocked_url_categories**  complex | List of blocked URL categories  Returned: query for policy |
| **id**  list / elements=string | Unique ID of category to filter  Returned: query for policy  Sample: `["meraki:contentFiltering/category/1"]` |
| **name**  list / elements=string | Name of category to filter  Returned: query for policy  Sample: `["Real Estate"]` |
| **blocked_url_patterns**  list / elements=string | Explicitly denied URL patterns  Returned: query for policy  Sample: `["http://www.ansible.net"]` |
| **categories**  complex | List of available content filtering categories.  Returned: query for categories |
| **id**  string | Unique ID of content filtering category.  Returned: query for categories  Sample: `"meraki:contentFiltering/category/1"` |
| **name**  string | Name of content filtering category.  Returned: query for categories  Sample: `"Real Estate"` |
| **url_cateogory_list_size**  string | Size of categories to cache on MX appliance  Returned: query for policy  Sample: `"topSites"` |

### Authors

- Kevin Breit (@kbreit)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)
