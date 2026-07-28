---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_kubernetes_info module – Returns information about an existing DigitalOcean Kubernetes cluster"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_kubernetes_info_module.html
fetched_at: 2026-07-27T17:06:47+00:00
---
# community.digitalocean.digital_ocean_kubernetes_info module – Returns information about an existing DigitalOcean Kubernetes cluster

> **Note:**
>
> This module is part of the [community.digitalocean collection](https://galaxy.ansible.com/community/digitalocean) (version 1.22.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_kubernetes_info`.

New in community.digitalocean 1.3.0

- [Synopsis](digital_ocean_kubernetes_info_module.md#synopsis)
- [Parameters](digital_ocean_kubernetes_info_module.md#parameters)
- [Examples](digital_ocean_kubernetes_info_module.md#examples)
- [Return Values](digital_ocean_kubernetes_info_module.md#return-values)

## [Synopsis](digital_ocean_kubernetes_info_module.md#id1)

- Returns information about an existing DigitalOcean Kubernetes cluster.

## [Parameters](digital_ocean_kubernetes_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | A human-readable name for a Kubernetes cluster. |
| **oauth_token**  aliases: API_TOKEN  string / required | DigitalOcean OAuth token; can be specified in `DO_API_KEY`, `DO_API_TOKEN`, or `DO_OAUTH_TOKEN` environment variables |
| **return_kubeconfig**  boolean | Controls whether or not to return the `kubeconfig`.  Choices:   - `false` ← (default) - `true` |

## [Examples](digital_ocean_kubernetes_info_module.md#id3)

```yaml+jinja
- name: Get information about an existing DigitalOcean Kubernetes cluster
  community.digitalocean.digital_ocean_kubernetes_info:
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    name: hacktoberfest
    return_kubeconfig: yes
  register: my_cluster

- ansible.builtin.debug:
    msg: "Cluster name is {{ my_cluster.data.name }}, ID is {{ my_cluster.data.id }}"

- ansible.builtin.debug:
    msg: "Cluster kubeconfig is {{ my_cluster.data.kubeconfig }}"
```

## [Return Values](digital_ocean_kubernetes_info_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | A DigitalOcean Kubernetes cluster (and optional `kubeconfig`)  Returned: changed  Sample: `{"auto_upgrade": false, "cluster_subnet": "10.244.0.0/16", "created_at": "2020-09-26T21:36:18Z", "endpoint": "https://REDACTED.k8s.ondigitalocean.com", "id": "REDACTED", "ipv4": "REDACTED", "kubeconfig": "apiVersion: v1\nclusters:\n- cluster:\n    certificate-authority-data: REDACTED\n    server: https://REDACTED.k8s.ondigitalocean.com\n  name: do-nyc1-hacktoberfest\ncontexts:\n- context:\n    cluster: do-nyc1-hacktoberfest\n    user: do-nyc1-hacktoberfest-admin\n  name: do-nyc1-hacktoberfest\ncurrent-context: do-nyc1-hacktoberfest\nkind: Config\npreferences: {}\nusers:\n- name: do-nyc1-hacktoberfest-admin\n  user:\n    token: REDACTED", "maintenance_policy": {"day": "any", "duration": "4h0m0s", "start_time": "13:00"}, "name": "hacktoberfest", "node_pools": [{"auto_scale": false, "count": 1, "id": "REDACTED", "labels": null, "max_nodes": 0, "min_nodes": 0, "name": "hacktoberfest-workers", "nodes": [{"created_at": "2020-09-26T21:36:18Z", "droplet_id": "REDACTED", "id": "REDACTED", "name": "hacktoberfest-workers-3tv46", "status": {"state": "running"}, "updated_at": "2020-09-26T21:40:28Z"}], "size": "s-1vcpu-2gb", "tags": ["k8s", "k8s:REDACTED", "k8s:worker"], "taints": []}], "region": "nyc1", "service_subnet": "10.245.0.0/16", "status": {"state": "running"}, "surge_upgrade": false, "tags": ["k8s", "k8s:REDACTED"], "updated_at": "2020-09-26T21:42:29Z", "version": "1.18.8-do.0", "vpc_uuid": "REDACTED"}` |

### Authors

- Mark Mercado (@mamercad)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
