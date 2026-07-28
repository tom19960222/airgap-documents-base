---
collection: ansible
version: "8"
title: "ansible.builtin.uri test – is the string a valid URI"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/uri_test.html
fetched_at: 2026-07-28T01:09:00+00:00
---
# ansible.builtin.uri test – is the string a valid URI

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `uri`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.uri` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

New in ansible-core 2.14

- [Synopsis](uri_test.md#synopsis)
- [Input](uri_test.md#input)
- [Keyword parameters](uri_test.md#keyword-parameters)
- [Examples](uri_test.md#examples)
- [Return Value](uri_test.md#return-value)

## [Synopsis](uri_test.md#id1)

- Validates that the input string conforms to the URI standard, optionally that is also in the list of schemas provided.

## [Input](uri_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.uri` or `is not ansible.builtin.uri`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | Possible URI. |

## [Keyword parameters](uri_test.md#id3)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.builtin.uri(key1=value1, key2=value2, ...)` and `input is not ansible.builtin.uri(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **schemes**  list / elements=string | Subset of URI schemas to validate against, otherwise **any** scheme is considered valid. |

## [Examples](uri_test.md#id4)

```yaml+jinja
# URLs are URIs
{{ 'http://example.com' is uri }}
# but not all URIs are URLs
{{ 'mailto://nowone@example.com' is uri }}
# looking only for file transfers URIs
{{ 'mailto://nowone@example.com' is not uri(schemes=['ftp', 'ftps', 'sftp', 'file']) }}
# make sure URL conforms to the 'special schemas'
{{ 'http://nobody:secret@example.com' is uri(['ftp', 'ftps', 'http', 'https', 'ws', 'wss']) }}
```

## [Return Value](uri_test.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `false` if the string is not a URI or the schema extracted does not match the supplied list.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
