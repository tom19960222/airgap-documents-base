---
collection: ansible
version: "8"
title: "Dictionaries"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/docsite/filter_guide_abstract_informations_dictionaries.html
fetched_at: 2026-07-28T03:00:41+00:00
---
# Dictionaries

You can use the [community.general.dict_kv filter](../dict_kv_filter.md#ansible-collections-community-general-dict-kv-filter) to create a single-entry dictionary with `value | community.general.dict_kv(key)`:

```yaml+jinja
- name: Create a single-entry dictionary
  debug:
    msg: "{{ myvar | community.general.dict_kv('thatsmyvar') }}"
  vars:
    myvar: myvalue

- name: Create a list of dictionaries where the 'server' field is taken from a list
  debug:
    msg: >-
      {{ myservers | map('community.general.dict_kv', 'server')
                   | map('combine', common_config) }}
  vars:
    common_config:
      type: host
      database: all
    myservers:
    - server1
    - server2
```

This produces:

```ansible-output
TASK [Create a single-entry dictionary]  **************************************************
ok: [localhost] => {
    "msg": {
        "thatsmyvar": "myvalue"
    }
}

TASK [Create a list of dictionaries where the 'server' field is taken from a list]  *******
ok: [localhost] => {
    "msg": [
        {
            "database": "all",
            "server": "server1",
            "type": "host"
        },
        {
            "database": "all",
            "server": "server2",
            "type": "host"
        }
    ]
}
```

New in version 2.0.0.

If you need to convert a list of key-value pairs to a dictionary, you can use the `dict` function. Unfortunately, this function cannot be used with `map`. For this, the [community.general.dict filter](../dict_filter.md#ansible-collections-community-general-dict-filter) can be used:

```yaml+jinja
- name: Create a dictionary with the dict function
  debug:
    msg: "{{ dict([[1, 2], ['a', 'b']]) }}"

- name: Create a dictionary with the community.general.dict filter
  debug:
    msg: "{{ [[1, 2], ['a', 'b']] | community.general.dict }}"

- name: Create a list of dictionaries with map and the community.general.dict filter
  debug:
    msg: >-
      {{ values | map('zip', ['k1', 'k2', 'k3'])
                | map('map', 'reverse')
                | map('community.general.dict') }}
  vars:
    values:
      - - foo
        - 23
        - a
      - - bar
        - 42
        - b
```

This produces:

```ansible-output
TASK [Create a dictionary with the dict function]  ****************************************
ok: [localhost] => {
    "msg": {
        "1": 2,
        "a": "b"
    }
}

TASK [Create a dictionary with the community.general.dict filter]  ************************
ok: [localhost] => {
    "msg": {
        "1": 2,
        "a": "b"
    }
}

TASK [Create a list of dictionaries with map and the community.general.dict filter]  ******
ok: [localhost] => {
    "msg": [
        {
            "k1": "foo",
            "k2": 23,
            "k3": "a"
        },
        {
            "k1": "bar",
            "k2": 42,
            "k3": "b"
        }
    ]
}
```

New in version 3.0.0.
