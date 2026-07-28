---
collection: ansible
version: "8"
title: "community.general.json_query filter – Select a single element or a data subset from a complex data structure"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/json_query_filter.html
fetched_at: 2026-07-28T01:04:51+00:00
---
# community.general.json_query filter – Select a single element or a data subset from a complex data structure

> **Note:**
>
> This filter plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this filter plugin,
> see [Requirements](json_query_filter.md#ansible-collections-community-general-json-query-filter-requirements) for details.
>
> To use it in a playbook, specify: `community.general.json_query`.

- [Synopsis](json_query_filter.md#synopsis)
- [Requirements](json_query_filter.md#requirements)
- [Input](json_query_filter.md#input)
- [Positional parameters](json_query_filter.md#positional-parameters)
- [Examples](json_query_filter.md#examples)
- [Return Value](json_query_filter.md#return-value)

## [Synopsis](json_query_filter.md#id1)

- This filter lets you query a complex JSON structure and iterate over it using a loop structure.

## [Requirements](json_query_filter.md#id2)

The below requirements are needed on the local controller node that executes this filter.

- jmespath

## [Input](json_query_filter.md#id3)

This describes the input of the filter, the value before `| community.general.json_query`.

| Parameter | Comments |
| --- | --- |
| **Input**  any / required | The JSON data to query. |

## [Positional parameters](json_query_filter.md#id4)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | community.general.json_query(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **expr**  string / required | The query expression.  See <http://jmespath.org/examples.html> for examples. |

## [Examples](json_query_filter.md#id5)

```yaml+jinja
- name: Define data to work on in the examples below
  ansible.builtin.set_fact:
    domain_definition:
      domain:
        cluster:
          - name: cluster1
          - name: cluster2
        server:
          - name: server11
            cluster: cluster1
            port: '8080'
          - name: server12
            cluster: cluster1
            port: '8090'
          - name: server21
            cluster: cluster2
            port: '9080'
          - name: server22
            cluster: cluster2
            port: '9090'
        library:
          - name: lib1
            target: cluster1
          - name: lib2
            target: cluster2

- name: Display all cluster names
  ansible.builtin.debug:
    var: item
  loop: "{{ domain_definition | community.general.json_query('domain.cluster[*].name') }}"

- name: Display all server names
  ansible.builtin.debug:
    var: item
  loop: "{{ domain_definition | community.general.json_query('domain.server[*].name') }}"

- name: Display all ports from cluster1
  ansible.builtin.debug:
    var: item
  loop: "{{ domain_definition | community.general.json_query(server_name_cluster1_query) }}"
  vars:
    server_name_cluster1_query: "domain.server[?cluster=='cluster1'].port"

- name: Display all ports from cluster1 as a string
  ansible.builtin.debug:
    msg: "{{ domain_definition | community.general.json_query('domain.server[?cluster==`cluster1`].port') | join(', ') }}"

- name: Display all ports from cluster1
  ansible.builtin.debug:
    var: item
  loop: "{{ domain_definition | community.general.json_query('domain.server[?cluster==''cluster1''].port') }}"

- name: Display all server ports and names from cluster1
  ansible.builtin.debug:
    var: item
  loop: "{{ domain_definition | community.general.json_query(server_name_cluster1_query) }}"
  vars:
    server_name_cluster1_query: "domain.server[?cluster=='cluster2'].{name: name, port: port}"

- name: Display all ports from cluster1
  ansible.builtin.debug:
    msg: "{{ domain_definition | to_json | from_json | community.general.json_query(server_name_query) }}"
  vars:
    server_name_query: "domain.server[?starts_with(name,'server1')].port"

- name: Display all ports from cluster1
  ansible.builtin.debug:
    msg: "{{ domain_definition | to_json | from_json | community.general.json_query(server_name_query) }}"
  vars:
    server_name_query: "domain.server[?contains(name,'server1')].port"
```

## [Return Value](json_query_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  any | The result of the query.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
