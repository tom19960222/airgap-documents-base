---
collection: ansible
version: "8"
title: "Creating identifiers"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/docsite/filter_guide_creating_identifiers.html
fetched_at: 2026-07-28T03:00:45+00:00
---
# Creating identifiers

The following filters allow to create identifiers.

## Hashids

[Hashids](https://hashids.org/) allow to convert sequences of integers to short unique string identifiers. The [community.general.hashids_encode](../hashids_encode_filter.md#ansible-collections-community-general-hashids-encode-filter) and [community.general.hashids_decode](../hashids_decode_filter.md#ansible-collections-community-general-hashids-decode-filter) filters need the [hashids Python library](https://pypi.org/project/hashids/) installed on the controller.

```yaml+jinja
- name: "Create hashid"
  debug:
    msg: "{{ [1234, 5, 6] | community.general.hashids_encode }}"

- name: "Decode hashid"
  debug:
    msg: "{{ 'jm2Cytn' | community.general.hashids_decode }}"
```

This produces:

```ansible-output
TASK [Create hashid] **********************************************************************
ok: [localhost] => {
    "msg": "jm2Cytn"
}

TASK [Decode hashid] **********************************************************************
ok: [localhost] => {
    "msg": [
        1234,
        5,
        6
    ]
}
```

The hashids filters accept keyword arguments to allow fine-tuning the hashids generated:

salt:
:   String to use as salt when hashing.

alphabet:
:   String of 16 or more unique characters to produce a hash.

min_length:
:   Minimum length of hash produced.

## Random MACs

You can use the [community.general.random_mac filter](../random_mac_filter.md#ansible-collections-community-general-random-mac-filter) to complete a partial [MAC address](https://en.wikipedia.org/wiki/MAC_address) to a random 6-byte MAC address.

```yaml+jinja
- name: "Create a random MAC starting with ff:"
  debug:
    msg: "{{ 'FF' | community.general.random_mac }}"

- name: "Create a random MAC starting with 00:11:22:"
  debug:
    msg: "{{ '00:11:22' | community.general.random_mac }}"
```

This produces:

```ansible-output
TASK [Create a random MAC starting with ff:] **********************************************
ok: [localhost] => {
    "msg": "ff:69:d3:78:7f:b4"
}

TASK [Create a random MAC starting with 00:11:22:] ****************************************
ok: [localhost] => {
    "msg": "00:11:22:71:5d:3b"
}
```

You can also initialize the random number generator from a seed to create random-but-idempotent MAC addresses:

```yaml+jinja
"{{ '52:54:00' | community.general.random_mac(seed=inventory_hostname) }}"
```
