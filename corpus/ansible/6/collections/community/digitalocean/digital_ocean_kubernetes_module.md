---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_kubernetes module – Create and delete a DigitalOcean Kubernetes cluster"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_kubernetes_module.html
fetched_at: 2026-07-27T17:06:46+00:00
---
# community.digitalocean.digital_ocean_kubernetes module – Create and delete a DigitalOcean Kubernetes cluster

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
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_kubernetes`.

New in community.digitalocean 1.3.0

- [Synopsis](digital_ocean_kubernetes_module.md#synopsis)
- [Parameters](digital_ocean_kubernetes_module.md#parameters)
- [Examples](digital_ocean_kubernetes_module.md#examples)
- [Return Values](digital_ocean_kubernetes_module.md#return-values)

## [Synopsis](digital_ocean_kubernetes_module.md#id1)

- Create and delete a Kubernetes cluster in DigitalOcean (and optionally wait for it to be running).

## [Parameters](digital_ocean_kubernetes_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_upgrade**  boolean | A boolean value indicating whether the cluster will be automatically upgraded to new patch releases during its maintenance window.  Choices:   - `false` ← (default) - `true` |
| **ha**  boolean | A boolean value indicating whether the control plane is run in a highly available configuration in the cluster.  Highly available control planes incur less downtime.  Choices:   - `false` ← (default) - `true` |
| **maintenance_policy**  dictionary | An object specifying the maintenance window policy for the Kubernetes cluster (see table below). |
| **name**  string / required | A human-readable name for a Kubernetes cluster. |
| **node_pools**  list / elements=dictionary | An object specifying the details of the worker nodes available to the Kubernetes cluster (see table below).  Default: `[{"auto_scale": false, "count": 1, "labels": {}, "max_nodes": 0, "min_nodes": 0, "name": "worker-pool", "size": "s-1vcpu-2gb", "tags": [], "taints": []}]` |
| **auto_scale**  boolean | A boolean value indicating whether auto-scaling is enabled for this node pool.  Choices:   - `false` - `true` |
| **count**  integer | The number of Droplet instances in the node pool. |
| **labels**  dictionary | An object containing a set of Kubernetes labels. The keys are user-defined. |
| **max_nodes**  integer | The maximum number of nodes that this node pool can be auto-scaled to.  The value will be `0` if `auto_scale` is set to `false`. |
| **min_nodes**  integer | The minimum number of nodes that this node pool can be auto-scaled to.  The value will be `0` if `auto_scale` is set to `false`. |
| **name**  string | A human-readable name for the node pool. |
| **size**  string | The slug identifier for the type of Droplet used as workers in the node pool. |
| **tags**  list / elements=string | An array containing the tags applied to the node pool.  All node pools are automatically tagged `"k8s"`, `"k8s-worker"`, and `"k8s:$K8S_CLUSTER_ID"`. |
| **taints**  list / elements=dictionary | An array of taints to apply to all nodes in a pool.  Taints will automatically be applied to all existing nodes and any subsequent nodes added to the pool.  When a taint is removed, it is removed from all nodes in the pool. |
| **oauth_token**  aliases: API_TOKEN  string / required | DigitalOcean OAuth token; can be specified in `DO_API_KEY`, `DO_API_TOKEN`, or `DO_OAUTH_TOKEN` environment variables |
| **region**  aliases: region_id  string | The slug identifier for the region where the Kubernetes cluster will be created.  Default: `"nyc1"` |
| **return_kubeconfig**  boolean | Controls whether or not to return the `kubeconfig`.  Choices:   - `false` ← (default) - `true` |
| **state**  string | The usual, `present` to create, `absent` to destroy  Choices:   - `"present"` ← (default) - `"absent"` |
| **surge_upgrade**  boolean | A boolean value indicating whether surge upgrade is enabled/disabled for the cluster.  Surge upgrade makes cluster upgrades fast and reliable by bringing up new nodes before destroying the outdated nodes.  Choices:   - `false` ← (default) - `true` |
| **tags**  list / elements=string | A flat array of tag names as strings to be applied to the Kubernetes cluster.  All clusters will be automatically tagged “k8s” and “k8s:$K8S_CLUSTER_ID” in addition to any tags provided by the user. |
| **version**  string | The slug identifier for the version of Kubernetes used for the cluster. See the /v2/kubernetes/options endpoint for available versions.  Default: `"latest"` |
| **vpc_uuid**  string | A string specifying the UUID of the VPC to which the Kubernetes cluster will be assigned.  If excluded, the cluster will be assigned to your account’s default VPC for the region. |
| **wait**  boolean | Wait for the cluster to be running before returning.  Choices:   - `false` - `true` ← (default) |
| **wait_timeout**  integer | How long before wait gives up, in seconds, when creating a cluster.  Default: `600` |

## [Examples](digital_ocean_kubernetes_module.md#id3)

```yaml+jinja
- name: Create a new DigitalOcean Kubernetes cluster in New York 1
  community.digitalocean.digital_ocean_kubernetes:
    state: present
    oauth_token: "{{ lookup('env', 'DO_API_TOKEN') }}"
    name: hacktoberfest
    region: nyc1
    node_pools:
      - name: hacktoberfest-workers
        size: s-1vcpu-2gb
        count: 3
    return_kubeconfig: yes
    wait_timeout: 600
    register: my_cluster

- name: Show the kubeconfig for the cluster we just created
  debug:
    msg: "{{ my_cluster.data.kubeconfig }}"

- name: Destroy (delete) an existing DigitalOcean Kubernetes cluster
  community.digitalocean.digital_ocean_kubernetes:
    state: absent
    oauth_token: "{{ lookup('env', 'DO_API_TOKEN') }}"
    name: hacktoberfest
```

## [Return Values](digital_ocean_kubernetes_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | A DigitalOcean Kubernetes cluster (and optional `kubeconfig`)  Returned: changed  Sample: `{"kubeconfig": "apiVersion: v1\nclusters:\n- cluster:\n    certificate-authority-data: REDACTED\n    server: https://REDACTED.k8s.ondigitalocean.com\n  name: do-nyc1-hacktoberfest\ncontexts:\n- context:\n    cluster: do-nyc1-hacktoberfest\n    user: do-nyc1-hacktoberfest-admin\n  name: do-nyc1-hacktoberfest\ncurrent-context: do-nyc1-hacktoberfest\nkind: Config\npreferences: {}\nusers:\n- name: do-nyc1-hacktoberfest-admin\n  user:\n    token: REDACTED", "kubernetes_cluster": {"auto_upgrade": false, "cluster_subnet": "10.244.0.0/16", "created_at": "2020-09-27T00:55:37Z", "endpoint": "https://REDACTED.k8s.ondigitalocean.com", "id": "REDACTED", "ipv4": "REDACTED", "maintenance_policy": {"day": "any", "duration": "4h0m0s", "start_time": "15:00"}, "name": "hacktoberfest", "node_pools": [{"auto_scale": false, "count": 1, "id": "REDACTED", "labels": null, "max_nodes": 0, "min_nodes": 0, "name": "hacktoberfest-workers", "nodes": [{"created_at": "2020-09-27T00:55:37Z", "droplet_id": "209555245", "id": "REDACTED", "name": "hacktoberfest-workers-3tdq1", "status": {"state": "running"}, "updated_at": "2020-09-27T00:58:36Z"}], "size": "s-1vcpu-2gb", "tags": ["k8s", "k8s:REDACTED", "k8s:worker"], "taints": []}], "region": "nyc1", "service_subnet": "10.245.0.0/16", "status": {"state": "running"}, "surge_upgrade": false, "tags": ["k8s", "k8s:REDACTED"], "updated_at": "2020-09-27T01:00:37Z", "version": "1.18.8-do.1", "vpc_uuid": "REDACTED"}}` |

### Authors

- Mark Mercado (@mamercad)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
