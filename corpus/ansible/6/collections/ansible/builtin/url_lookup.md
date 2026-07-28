---
collection: ansible
version: "6"
title: "ansible.builtin.url lookup – return contents from URL"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/url_lookup.html
fetched_at: 2026-07-27T16:44:25+00:00
---
# ansible.builtin.url lookup – return contents from URL

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `url` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](url_lookup.md#synopsis)
- [Terms](url_lookup.md#terms)
- [Keyword parameters](url_lookup.md#keyword-parameters)
- [Notes](url_lookup.md#notes)
- [Examples](url_lookup.md#examples)
- [Return Value](url_lookup.md#return-value)

## [Synopsis](url_lookup.md#id1)

- Returns the content of the URL requested to be used as data in play.

## [Terms](url_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string | urls to query |

## [Keyword parameters](url_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('ansible.builtin.url', key1=value1, key2=value2, ...)` and `query('ansible.builtin.url', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **ca_path**  string  added in ansible-base 2.10 | String of file system path to CA cert bundle to use  Configuration:   - INI entry:  ```YAML+Jinja   [url_lookup]   ca_path = VALUE   ``` - Environment variable: [`ANSIBLE_LOOKUP_URL_CA_PATH`](../../environment_variables.md#envvar-ANSIBLE_LOOKUP_URL_CA_PATH) - Variable: ansible_lookup_url_ca_path |
| **follow_redirects**  string  added in ansible-base 2.10 | String of urllib2, all/yes, safe, none to determine how redirects are followed, see RedirectHandlerFactory for more information  Default: `"urllib2"`  Configuration:   - INI entry:  ```YAML+Jinja   [url_lookup]   follow_redirects = urllib2   ``` - Environment variable: [`ANSIBLE_LOOKUP_URL_FOLLOW_REDIRECTS`](../../environment_variables.md#envvar-ANSIBLE_LOOKUP_URL_FOLLOW_REDIRECTS) - Variable: ansible_lookup_url_follow_redirects |
| **force**  boolean  added in ansible-base 2.10 | Whether or not to set “cache-control” header with value “no-cache”  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [url_lookup]   force = false   ``` - Environment variable: [`ANSIBLE_LOOKUP_URL_FORCE`](../../environment_variables.md#envvar-ANSIBLE_LOOKUP_URL_FORCE) - Variable: ansible_lookup_url_force |
| **force_basic_auth**  boolean  added in ansible-base 2.10 | Force basic authentication  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [url_lookup]   agent = false   ``` - Environment variable: [`ANSIBLE_LOOKUP_URL_AGENT`](../../environment_variables.md#envvar-ANSIBLE_LOOKUP_URL_AGENT) - Variable: ansible_lookup_url_agent |
| **headers**  dictionary  added in Ansible 2.9 | HTTP request headers  Default: `{}` |
| **http_agent**  string  added in ansible-base 2.10 | User-Agent to use in the request. The default was changed in 2.11 to `ansible-httpget`.  Default: `"ansible-httpget"`  Configuration:   - INI entry:  ```YAML+Jinja   [url_lookup]   agent = ansible-httpget   ``` - Environment variable: [`ANSIBLE_LOOKUP_URL_AGENT`](../../environment_variables.md#envvar-ANSIBLE_LOOKUP_URL_AGENT) - Variable: ansible_lookup_url_agent |
| **password**  string  added in Ansible 2.8 | Password to use for HTTP authentication. |
| **split_lines**  boolean | Flag to control if content is returned as a list of lines or as a single text blob  Choices:   - `false` - `true` ← (default) |
| **timeout**  float  added in ansible-base 2.10 | How long to wait for the server to send data before giving up  Default: `10.0`  Configuration:   - INI entry:  ```YAML+Jinja   [url_lookup]   timeout = 10.0   ``` - Environment variable: [`ANSIBLE_LOOKUP_URL_TIMEOUT`](../../environment_variables.md#envvar-ANSIBLE_LOOKUP_URL_TIMEOUT) - Variable: ansible_lookup_url_timeout |
| **unix_socket**  string  added in ansible-base 2.10 | String of file system path to unix socket file to use when establishing connection to the provided url  Configuration:   - INI entry:  ```YAML+Jinja   [url_lookup]   unix_socket = VALUE   ``` - Environment variable: [`ANSIBLE_LOOKUP_URL_UNIX_SOCKET`](../../environment_variables.md#envvar-ANSIBLE_LOOKUP_URL_UNIX_SOCKET) - Variable: ansible_lookup_url_unix_socket |
| **unredirected_headers**  list / elements=string  added in ansible-base 2.10 | A list of headers to not attach on a redirected request  Configuration:   - INI entry:  ```YAML+Jinja   [url_lookup]   unredirected_headers = VALUE   ``` - Environment variable: [`ANSIBLE_LOOKUP_URL_UNREDIR_HEADERS`](../../environment_variables.md#envvar-ANSIBLE_LOOKUP_URL_UNREDIR_HEADERS) - Variable: ansible_lookup_url_unredir_headers |
| **use_gssapi**  boolean  added in ansible-base 2.10 | Use GSSAPI handler of requests  As of Ansible 2.11, GSSAPI credentials can be specified with *username* and *password*.  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [url_lookup]   use_gssapi = false   ``` - Environment variable: [`ANSIBLE_LOOKUP_URL_USE_GSSAPI`](../../environment_variables.md#envvar-ANSIBLE_LOOKUP_URL_USE_GSSAPI) - Variable: ansible_lookup_url_use_gssapi |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  Choices:   - `false` - `true` ← (default) |
| **username**  string  added in Ansible 2.8 | Username to use for HTTP authentication. |
| **validate_certs**  boolean | Flag to control SSL certificate validation  Choices:   - `false` - `true` ← (default) |

## [Notes](url_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('ansible.builtin.url', term1, term2, key1=value1, key2=value2)` and `query('ansible.builtin.url', term1, term2, key1=value1, key2=value2)`

## [Examples](url_lookup.md#id5)

```yaml+jinja
- name: url lookup splits lines by default
  ansible.builtin.debug: msg="{{item}}"
  loop: "{{ lookup('ansible.builtin.url', 'https://github.com/gremlin.keys', wantlist=True) }}"

- name: display ip ranges
  ansible.builtin.debug: msg="{{ lookup('ansible.builtin.url', 'https://ip-ranges.amazonaws.com/ip-ranges.json', split_lines=False) }}"

- name: url lookup using authentication
  ansible.builtin.debug: msg="{{ lookup('ansible.builtin.url', 'https://some.private.site.com/file.txt', username='bob', password='hunter2') }}"

- name: url lookup using basic authentication
  ansible.builtin.debug:
    msg: "{{ lookup('ansible.builtin.url', 'https://some.private.site.com/file.txt', username='bob', password='hunter2', force_basic_auth='True') }}"

- name: url lookup using headers
  ansible.builtin.debug:
    msg: "{{ lookup('ansible.builtin.url', 'https://some.private.site.com/api/service', headers={'header1':'value1', 'header2':'value2'} ) }}"
```

## [Return Value](url_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | list of list of lines or content of url(s)  Returned: success |

### Authors

- Brian Coca (@bcoca)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
