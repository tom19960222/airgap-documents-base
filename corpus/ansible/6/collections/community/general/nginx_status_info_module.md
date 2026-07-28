---
collection: ansible
version: "6"
title: "community.general.nginx_status_info module – Retrieve information on nginx status"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/nginx_status_info_module.html
fetched_at: 2026-07-27T17:11:05+00:00
---
# community.general.nginx_status_info module – Retrieve information on nginx status

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.nginx_status_info`.

- [Synopsis](nginx_status_info_module.md#synopsis)
- [Parameters](nginx_status_info_module.md#parameters)
- [Notes](nginx_status_info_module.md#notes)
- [Examples](nginx_status_info_module.md#examples)
- [Return Values](nginx_status_info_module.md#return-values)

## [Synopsis](nginx_status_info_module.md#id1)

- Gathers information from nginx from an URL having `stub_status` enabled.

## [Parameters](nginx_status_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **timeout**  integer | HTTP connection timeout in seconds.  Default: `10` |
| **url**  string / required | URL of the nginx status. |

## [Notes](nginx_status_info_module.md#id3)

> **Note:**
>
> - See <http://nginx.org/en/docs/http/ngx_http_stub_status_module.html> for more information.

## [Examples](nginx_status_info_module.md#id4)

```yaml+jinja
# Gather status info from nginx on localhost
- name: Get current http stats
  community.general.nginx_status_info:
    url: http://localhost/nginx_status
  register: result

# Gather status info from nginx on localhost with a custom timeout of 20 seconds
- name: Get current http stats
  community.general.nginx_status_info:
    url: http://localhost/nginx_status
    timeout: 20
  register: result
```

## [Return Values](nginx_status_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **accepts**  integer | The total number of accepted client connections.  Returned: success  Sample: `81769947` |
| **active_connections**  integer | Active connections.  Returned: success  Sample: `2340` |
| **data**  string | HTTP response as is.  Returned: success  Sample: `"Active connections: 2340 \nserver accepts handled requests\n 81769947 81769947 144332345 \nReading: 0 Writing: 241 Waiting: 2092 \n"` |
| **handled**  integer | The total number of handled connections. Generally, the parameter value is the same as accepts unless some resource limits have been reached.  Returned: success  Sample: `81769947` |
| **reading**  integer | The current number of connections where nginx is reading the request header.  Returned: success  Sample: `0` |
| **requests**  integer | The total number of client requests.  Returned: success  Sample: `144332345` |
| **waiting**  integer | The current number of idle client connections waiting for a request.  Returned: success  Sample: `2092` |
| **writing**  integer | The current number of connections where nginx is writing the response back to the client.  Returned: success  Sample: `241` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
