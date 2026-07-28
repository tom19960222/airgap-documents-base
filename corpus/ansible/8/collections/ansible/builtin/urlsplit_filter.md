---
collection: ansible
version: "8"
title: "ansible.builtin.urlsplit filter – get components from URL"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/urlsplit_filter.html
fetched_at: 2026-07-28T01:04:59+00:00
---
# ansible.builtin.urlsplit filter – get components from URL

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `urlsplit`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.urlsplit` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](urlsplit_filter.md#synopsis)
- [Input](urlsplit_filter.md#input)
- [Positional parameters](urlsplit_filter.md#positional-parameters)
- [Examples](urlsplit_filter.md#examples)
- [Return Value](urlsplit_filter.md#return-value)

## [Synopsis](urlsplit_filter.md#id1)

- Split a URL into its component parts.

Aliases: urldecode

## [Input](urlsplit_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.urlsplit`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | URL string to split. |

## [Positional parameters](urlsplit_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.urlsplit(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **query**  string | Specify a single component to return.  **Choices:**   - `"fragment"` - `"hostname"` - `"netloc"` - `"password"` - `"path"` - `"port"` - `"query"` - `"scheme"` - `"username"` |

## [Examples](urlsplit_filter.md#id4)

```yaml+jinja
parts: '{{ "http://user:password@www.acme.com:9000/dir/index.html?query=term#fragment" | urlsplit }}'
# =>
#   {
#       "fragment": "fragment",
#       "hostname": "www.acme.com",
#       "netloc": "user:password@www.acme.com:9000",
#       "password": "password",
#       "path": "/dir/index.html",
#       "port": 9000,
#       "query": "query=term",
#       "scheme": "http",
#       "username": "user"
#   }

hostname: '{{ "http://user:password@www.acme.com:9000/dir/index.html?query=term#fragment" | urlsplit("hostname") }}'
# => 'www.acme.com'

query: '{{ "http://user:password@www.acme.com:9000/dir/index.html?query=term#fragment" | urlsplit("query") }}'
# => 'query=term'

path: '{{ "http://user:password@www.acme.com:9000/dir/index.html?query=term#fragment" | urlsplit("path") }}'
# => '/dir/index.html'
```

## [Return Value](urlsplit_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  any | A dictionary with components as keyword and their value.  If *query* is provided, a string or integer will be returned instead, depending on *query*.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
