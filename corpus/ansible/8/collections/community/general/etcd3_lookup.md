---
collection: ansible
version: "8"
title: "community.general.etcd3 lookup – Get key values from etcd3 server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/etcd3_lookup.html
fetched_at: 2026-07-28T01:52:49+00:00
---
# community.general.etcd3 lookup – Get key values from etcd3 server

> **Note:**
>
> This lookup plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](etcd3_lookup.md#ansible-collections-community-general-etcd3-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.etcd3`.

New in community.general 0.2.0

- [Synopsis](etcd3_lookup.md#synopsis)
- [Requirements](etcd3_lookup.md#requirements)
- [Terms](etcd3_lookup.md#terms)
- [Keyword parameters](etcd3_lookup.md#keyword-parameters)
- [Notes](etcd3_lookup.md#notes)
- [See Also](etcd3_lookup.md#see-also)
- [Examples](etcd3_lookup.md#examples)
- [Return Value](etcd3_lookup.md#return-value)

## [Synopsis](etcd3_lookup.md#id1)

- Retrieves key values and/or key prefixes from etcd3 server using its native gRPC API.
- Try to reuse [community.general.etcd3](etcd3_module.md#ansible-collections-community-general-etcd3-module) options for connection parameters, but add support for some `ETCDCTL_*` environment variables.
- See <https://github.com/etcd-io/etcd/tree/master/Documentation/op-guide> for etcd overview.

## [Requirements](etcd3_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- etcd3 >= 0.10

## [Terms](etcd3_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  list / elements=string / required | The list of keys (or key prefixes) to look up on the etcd3 server. |

## [Keyword parameters](etcd3_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.etcd3', key1=value1, key2=value2, ...)` and `query('community.general.etcd3', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **ca_cert**  string | etcd3 CA authority.  **Configuration:**   - Environment variable: [`ETCDCTL_CACERT`](../../environment_variables.md#envvar-ETCDCTL_CACERT) |
| **cert_cert**  string | etcd3 client certificate.  **Configuration:**   - Environment variable: [`ETCDCTL_CERT`](../../environment_variables.md#envvar-ETCDCTL_CERT) |
| **cert_key**  string | etcd3 client private key.  **Configuration:**   - Environment variable: [`ETCDCTL_KEY`](../../environment_variables.md#envvar-ETCDCTL_KEY) |
| **endpoints**  string | Counterpart of [`ETCDCTL_ENDPOINTS`](../../environment_variables.md#envvar-ETCDCTL_ENDPOINTS) environment variable. Specify the etcd3 connection with and URL form, for example `https://hostname:2379`, or `<host>:<port>` form.  The `host` part is overwritten by `host` option, if defined.  The `port` part is overwritten by `port` option, if defined.  **Default:** `"127.0.0.1:2379"`  **Configuration:**   - Environment variable: [`ETCDCTL_ENDPOINTS`](../../environment_variables.md#envvar-ETCDCTL_ENDPOINTS) |
| **host**  string | etcd3 listening client host.  Takes precedence over `endpoints`. |
| **password**  string | Authenticated user password.  **Configuration:**   - Environment variable: [`ETCDCTL_PASSWORD`](../../environment_variables.md#envvar-ETCDCTL_PASSWORD) |
| **port**  integer | etcd3 listening client port.  Takes precedence over `endpoints`. |
| **prefix**  boolean | Look for key or prefix key.  **Choices:**   - `false` ← (default) - `true` |
| **timeout**  integer | Client timeout.  **Default:** `60`  **Configuration:**   - Environment variable: [`ETCDCTL_DIAL_TIMEOUT`](../../environment_variables.md#envvar-ETCDCTL_DIAL_TIMEOUT) |
| **user**  string | Authenticated user name.  **Configuration:**   - Environment variable: [`ETCDCTL_USER`](../../environment_variables.md#envvar-ETCDCTL_USER) |

## [Notes](etcd3_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.etcd3', term1, term2, key1=value1, key2=value2)` and `query('community.general.etcd3', term1, term2, key1=value1, key2=value2)`
> - `host` and `port` options take precedence over (endpoints) option.
> - The recommended way to connect to etcd3 server is using `ETCDCTL_ENDPOINT` environment variable and keep `endpoints`, `host`, and `port` unused.

## [See Also](etcd3_lookup.md#id6)

> **See also:**
>
> [community.general.etcd3](etcd3_module.md#ansible-collections-community-general-etcd3-module)
> :   Set or delete key value pairs from an etcd3 cluster.
>
> [community.general.etcd](etcd_lookup.md#ansible-collections-community-general-etcd-lookup) lookup plugin
> :   get info from an etcd server.

## [Examples](etcd3_lookup.md#id7)

```yaml+jinja
- name: "a value from a locally running etcd"
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.etcd3', 'foo/bar') }}"

- name: "values from multiple folders on a locally running etcd"
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.etcd3', 'foo', 'bar', 'baz') }}"

- name: "look for a key prefix"
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.etcd3', '/foo/bar', prefix=True) }}"

- name: "connect to etcd3 with a client certificate"
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.etcd3', 'foo/bar', cert_cert='/etc/ssl/etcd/client.pem', cert_key='/etc/ssl/etcd/client.key') }}"
```

## [Return Value](etcd3_lookup.md#id8)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=dictionary | List of keys and associated values.  **Returned:** success |
| **key**  string | The element’s key.  **Returned:** success |
| **value**  string | The element’s value.  **Returned:** success |

### Authors

- Eric Belhomme (@eric-belhomme)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
