---
collection: ansible
version: "6"
title: "sensu.sensu_go.etcd_replicator module – Manage Sensu Go etcd replicators"
source_url: https://docs.ansible.com/projects/ansible/6/collections/sensu/sensu_go/etcd_replicator_module.html
fetched_at: 2026-07-28T00:19:29+00:00
---
# sensu.sensu_go.etcd_replicator module – Manage Sensu Go etcd replicators

> **Note:**
>
> This module is part of the [sensu.sensu_go collection](https://galaxy.ansible.com/sensu/sensu_go) (version 1.13.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install sensu.sensu_go`.
> You need further requirements to be able to use this module,
> see [Requirements](etcd_replicator_module.md#ansible-collections-sensu-sensu-go-etcd-replicator-module-requirements) for details.
>
> To use it in a playbook, specify: `sensu.sensu_go.etcd_replicator`.

New in sensu.sensu_go 1.9.0

- [Synopsis](etcd_replicator_module.md#synopsis)
- [Requirements](etcd_replicator_module.md#requirements)
- [Parameters](etcd_replicator_module.md#parameters)
- [See Also](etcd_replicator_module.md#see-also)
- [Examples](etcd_replicator_module.md#examples)
- [Return Values](etcd_replicator_module.md#return-values)

## [Synopsis](etcd_replicator_module.md#id1)

- Create, update or delete Sensu etcd replicator.
- For more information, refer to the Sensu documentation at <https://docs.sensu.io/sensu-go/latest/operations/deploy-sensu/etcdreplicators/>.

## [Requirements](etcd_replicator_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](etcd_replicator_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  string | Sensu API version of the resource to replicate. |
| **auth**  dictionary | Authentication parameters. Can define each of them with ENV as well. |
| **api_key**  string  added in sensu.sensu_go 1.3.0 | The API key that should be used when authenticating. If this is not set, the value of the SENSU_API_KEY environment variable will be checked.  This replaces *auth.user* and *auth.password* parameters.  For more information about the API key, refer to the official Sensu documentation at <https://docs.sensu.io/sensu-go/latest/guides/use-apikey-feature/>. |
| **ca_path**  path  added in sensu.sensu_go 1.5.0 | Path to the CA bundle that should be used to validate the backend certificate.  If this parameter is not set, module will use the CA bundle that python is using.  It is also possible to set this parameter via the *SENSU_CA_PATH* environment variable. |
| **password**  string | The Sensu user’s password. If this is not set the value of the SENSU_PASSWORD environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"P@ssw0rd!"` |
| **url**  string | Location of the Sensu backend API. If this is not set the value of the SENSU_URL environment variable will be checked.  Default: `"http://localhost:8080"` |
| **user**  string | The username to use for connecting to the Sensu API. If this is not set the value of the SENSU_USER environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"admin"` |
| **verify**  boolean  added in sensu.sensu_go 1.5.0 | Flag that controls the certificate validation.  If you are using self-signed certificates, you can set this parameter to `false`.  ONLY USE THIS PARAMETER IN DEVELOPMENT SCENARIOS! In you use self-signed certificates in production, see the *auth.ca_path* parameter.  It is also possible to set this parameter via the *SENSU_VERIFY* environment variable.  Choices:   - `false` - `true` ← (default) |
| **ca_cert**  string | Path to an the PEM-format CA certificate to use for TLS client authentication.  Required if *insecure* is `false`. |
| **cert**  string | Path to the PEM-format certificate to use for TLS client authentication. This certificate is required for secure client communication.  Required if *insecure* is `false`. |
| **insecure**  boolean | Disable transport security.  Only set to `true` in sandbox and experimental environments.  Choices:   - `false` ← (default) - `true` |
| **key**  string | Path to the PEM-format key file associated with the cert to use for TLS client authentication. This key and its corresponding certificate are required for secure client communication.  Required if *insecure* is `false`. |
| **name**  string / required | The Sensu resource’s name. This name (in combination with the namespace where applicable) uniquely identifies the resource that Ansible operates on.  If the resource with selected name already exists, Ansible module will update it to match the specification in the task.  Consult the *name* metadata attribute specification in the upstream docs on <https://docs.sensu.io/sensu-go/latest/reference/> for more details about valid names and other restrictions. |
| **namespace**  string | Namespace to constrain replication to.  If you do not include namespace, all namespaces for a given resource are replicated. |
| **replication_interval**  integer | Interval at which the resource will be replicated. In seconds. |
| **resource**  string | Name of the resource to replicate.  List of all resources is available at <https://docs.sensu.io/sensu-go/latest/operations/control-access/rbac/#resources>.  Required if *state* is `present`. |
| **state**  string | Target state of the Sensu object.  Choices:   - `"present"` ← (default) - `"absent"` |
| **url**  list / elements=string | Destination cluster URLs.  Required if *state* is `present`. |

## [See Also](etcd_replicator_module.md#id4)

> **See also:**
>
> [sensu.sensu_go.etcd_replicator_info](etcd_replicator_info_module.md#ansible-collections-sensu-sensu-go-etcd-replicator-info-module)
> :   List available Sensu Go etcd replicators.

## [Examples](etcd_replicator_module.md#id5)

```yaml+jinja
- name: Create a minimal replicator
  sensu.sensu_go.etcd_replicator:
    name: cluster_role_replicator
    ca_cert: /etc/sensu/certs/ca.pem
    cert: /etc/sensu/certs/cert.pem
    key: /etc/sensu/certs/key.pem
    url: https://sensu.alpha.example.com:2379
    resource: ClusterRole

- name: Create an insecure minimal replicator
  sensu.sensu_go.etcd_replicator:
    name: role_replicator
    insecure: true
    url:
      - https://sensu.beta.example.com:2379
      - https://sensu.gamma.example.com:2379
    resource: Role

- name: Create a replicator with all parameters set
  sensu.sensu_go.etcd_replicator:
    name: role_binding_replicator
    ca_cert: /etc/sensu/certs/ca.pem
    cert: /etc/sensu/certs/cert.pem
    key: /etc/sensu/certs/key.pem
    insecure: false
    url: https://127.0.0.1:2379
    api_version: core/v2
    resource: RoleBinding
    namespace: default
    replication_interval_seconds: 30

- name: Delete a replicator
  sensu.sensu_go.etcd_replicator:
    name: my_replicator
    state: absent
```

## [Return Values](etcd_replicator_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object**  dictionary | Object representing Sensu etcd replicator.  Returned: success  Sample: `{"api_version": "core/v2", "ca_cert": "/etc/sensu/certs/ca.pem", "cert": "/etc/sensu/certs/cert.pem", "insecure": false, "key": "/etc/sensu/certs/key.pem", "metadata": {"created_by": "admin", "name": "cluster-role-replicator"}, "namespace": "", "replication_interval_seconds": 30, "resource": "ClusterRole", "url": "https://sensu.alpha.example.com:2379"}` |

### Authors

- Tadej Borovsak (@tadeboro)

### Collection links

[Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
[Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
