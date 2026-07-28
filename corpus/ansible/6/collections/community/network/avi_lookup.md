---
collection: ansible
version: "6"
title: "community.network.avi lookup – Look up ``Avi`` objects."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/avi_lookup.html
fetched_at: 2026-07-27T17:20:05+00:00
---
# community.network.avi lookup – Look up ``Avi`` objects.

> **Note:**
>
> This lookup plugin is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.avi`.

- [Synopsis](avi_lookup.md#synopsis)
- [Keyword parameters](avi_lookup.md#keyword-parameters)
- [Notes](avi_lookup.md#notes)
- [Examples](avi_lookup.md#examples)
- [Return Value](avi_lookup.md#return-value)

## [Synopsis](avi_lookup.md#id1)

- Given an object_type, fetch all the objects of that type or fetch the specific object that matches the name/uuid given via options.
- For single object lookup. If you want the output to be a list, you may want to pass option wantlist=True to the plugin.

## [Keyword parameters](avi_lookup.md#id2)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.network.avi', key1=value1, key2=value2, ...)` and `query('community.network.avi', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **api_context**  dictionary | Avi API context that includes current session ID and CSRF Token.  This allows user to perform single login and re-use the session. |
| **api_version**  string | Avi API version of to use for Avi API and objects.  Default: `"16.4.4"` |
| **avi_credentials**  dictionary | Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details. |
| **api_version**  string | Avi controller version  Default: `"16.4.4"` |
| **controller**  string | Avi controller IP or SQDN |
| **csrftoken**  string | Avi controller API csrftoken to reuse existing session with session id  Default: `""` |
| **password**  string | Avi controller password |
| **port**  string | Avi controller port |
| **session_id**  string | Avi controller API session id to reuse existing session with csrftoken  Default: `""` |
| **tenant**  string | Avi controller tenant  Default: `"admin"` |
| **tenant_uuid**  string | Avi controller tenant UUID  Default: `""` |
| **timeout**  string | Avi controller request timeout  Default: `300` |
| **token**  string | Avi controller API token  Default: `""` |
| **username**  string | Avi controller username |
| **avi_disable_session_cache_as_fact**  boolean | It disables avi session information to be cached as a fact.  Choices:   - `false` ← (default) - `true` |
| **controller**  string | IP address or hostname of the controller. The default value is the environment variable `AVI_CONTROLLER`. |
| **obj_name**  string | name of the object to query |
| **obj_type**  string / required | type of object to query |
| **obj_uuid**  string | UUID of the object to query |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  Default: `"admin"` |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  Default: `""` |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |

## [Notes](avi_lookup.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_lookup.md#id4)

```yaml+jinja
# Lookup query for all the objects of a specific type.
- ansible.builtin.debug: msg="{{ lookup('community.network.avi', avi_credentials=avi_credentials, obj_type='virtualservice') }}"
# Lookup query for an object with the given name and type.
- ansible.builtin.debug: msg="{{ lookup('community.network.avi', avi_credentials=avi_credentials, obj_name='vs1', obj_type='virtualservice', wantlist=True) }}"
# Lookup query for an object with the given UUID and type.
- ansible.builtin.debug: msg="{{ lookup('community.network.avi', obj_uuid='virtualservice-5c0e183a-690a-45d8-8d6f-88c30a52550d', obj_type='virtualservice') }}"
# We can replace lookup with query function to always the get the output as list.
# This is helpful for looping.
- ansible.builtin.debug: msg="{{ query('community.network.avi', obj_uuid='virtualservice-5c0e183a-690a-45d8-8d6f-88c30a52550d', obj_type='virtualservice') }}"
```

## [Return Value](avi_lookup.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=dictionary | One ore more objects returned from ``Avi`` API.  Returned: success |

### Authors

- Sandeep Bandi (@sabandi)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
