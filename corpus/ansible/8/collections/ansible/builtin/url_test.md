---
collection: ansible
version: "8"
title: "ansible.builtin.url test – is the string a valid URL"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/url_test.html
fetched_at: 2026-07-28T01:09:01+00:00
---
# ansible.builtin.url test – is the string a valid URL

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `url`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.url` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

New in ansible-core 2.14

- [Synopsis](url_test.md#synopsis)
- [Input](url_test.md#input)
- [Keyword parameters](url_test.md#keyword-parameters)
- [Examples](url_test.md#examples)
- [Return Value](url_test.md#return-value)

## [Synopsis](url_test.md#id1)

- Validates a string to conform to the URL standard.

## [Input](url_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.url` or `is not ansible.builtin.url`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | Possible URL. |

## [Keyword parameters](url_test.md#id3)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.builtin.url(key1=value1, key2=value2, ...)` and `input is not ansible.builtin.url(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **schemes**  list / elements=string | Subset of URI schemas to validate against, otherwise **any** scheme is considered valid. |

## [Examples](url_test.md#id4)

```yaml+jinja
# simple URL
{{ 'http://example.com' is url }}
# looking only for file transfers URIs
{{ 'mailto://nowone@example.com' is not uri(schemes=['ftp', 'ftps', 'sftp', 'file']) }}
#  but it is according to standard
{{ 'mailto://nowone@example.com' is not uri }}
# more complex URL
{{ 'ftp://admin:secret@example.com/path/to/myfile.yml' is url }}
```

## [Return Value](url_test.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `false` if the string is not a URL, `true` otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
