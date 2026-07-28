---
collection: ansible
version: "6"
title: "community.google.gce_lb module – create/destroy GCE load-balancer resources"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/google/gce_lb_module.html
fetched_at: 2026-07-27T17:15:18+00:00
---
# community.google.gce_lb module – create/destroy GCE load-balancer resources

> **Note:**
>
> This module is part of the [community.google collection](https://galaxy.ansible.com/community/google) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.google`.
> You need further requirements to be able to use this module,
> see [Requirements](gce_lb_module.md#ansible-collections-community-google-gce-lb-module-requirements) for details.
>
> To use it in a playbook, specify: `community.google.gce_lb`.

- [Synopsis](gce_lb_module.md#synopsis)
- [Requirements](gce_lb_module.md#requirements)
- [Parameters](gce_lb_module.md#parameters)
- [Examples](gce_lb_module.md#examples)

## [Synopsis](gce_lb_module.md#id1)

- This module can create and destroy Google Compute Engine `loadbalancer` and `httphealthcheck` resources. The primary LB resource is the `load_balancer` resource and the health check parameters are all prefixed with *httphealthcheck*. The full documentation for Google Compute Engine load balancing is at <https://developers.google.com/compute/docs/load-balancing/>. However, the ansible module simplifies the configuration by following the libcloud model. Full install/configuration instructions for the gce\* modules can be found in the comments of ansible/test/gce_tests.py.

## [Requirements](gce_lb_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- apache-libcloud >= 0.13.3, >= 0.17.0 if using JSON credentials

## [Parameters](gce_lb_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **credentials_file**  path | path to the JSON file associated with the service account email |
| **external_ip**  string | the external static IPv4 (or auto-assigned) address for the LB |
| **httphealthcheck_healthy_count**  integer | number of consecutive successful checks before marking a node healthy  Default: `2` |
| **httphealthcheck_host**  string | host header to pass through on HTTP check requests |
| **httphealthcheck_interval**  integer | the duration in seconds between each health check request  Default: `5` |
| **httphealthcheck_name**  string | the name identifier for the HTTP health check |
| **httphealthcheck_path**  string | the url path to use for HTTP health checking  Default: `"/"` |
| **httphealthcheck_port**  integer | the TCP port to use for HTTP health checking  Default: `80` |
| **httphealthcheck_timeout**  integer | the timeout in seconds before a request is considered a failed check  Default: `5` |
| **httphealthcheck_unhealthy_count**  integer | number of consecutive failed checks before marking a node unhealthy  Default: `2` |
| **members**  list / elements=string | a list of zone/nodename pairs, e.g [‘us-central1-a/www-a’, …] |
| **name**  string | name of the load-balancer resource |
| **pem_file**  path | path to the pem file associated with the service account email This option is deprecated. Use ‘credentials_file’. |
| **port_range**  string | the port (range) to forward, e.g. 80 or 8000-8888 defaults to all ports |
| **project_id**  string | your GCE project ID |
| **protocol**  string | the protocol used for the load-balancer packet forwarding, tcp or udp  the available choices are: `tcp` or `udp`.  Default: `"tcp"` |
| **region**  string | the GCE region where the load-balancer is defined |
| **service_account_email**  string | service account email |
| **state**  string | desired state of the LB  the available choices are: `active`, `present`, `absent`, `deleted`.  Default: `"present"` |

## [Examples](gce_lb_module.md#id4)

```yaml+jinja
- name: Simple example of creating a new LB, adding members, and a health check
  local_action:
    module: gce_lb
    name: testlb
    region: us-central1
    members: ["us-central1-a/www-a", "us-central1-b/www-b"]
    httphealthcheck_name: hc
    httphealthcheck_port: 80
    httphealthcheck_path: "/up"
```

### Authors

- Eric Johnson (@erjohnso)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.google/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.google)
