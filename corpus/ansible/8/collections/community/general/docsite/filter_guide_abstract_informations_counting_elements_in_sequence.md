---
collection: ansible
version: "8"
title: "Counting elements in a sequence"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/docsite/filter_guide_abstract_informations_counting_elements_in_sequence.html
fetched_at: 2026-07-28T03:00:43+00:00
---
# Counting elements in a sequence

The [community.general.counter filter plugin](../counter_filter.md#ansible-collections-community-general-counter-filter) allows you to count (hashable) elements in a sequence. Elements are returned as dictionary keys and their counts are stored as dictionary values.

```yaml+jinja
- name: Count character occurrences in a string
  debug:
    msg: "{{ 'abccbaabca' | community.general.counter }}"

- name: Count items in a list
  debug:
    msg: "{{ ['car', 'car', 'bike', 'plane', 'bike'] | community.general.counter }}"
```

This produces:

```ansible-output
TASK [Count character occurrences in a string] ********************************************
ok: [localhost] => {
    "msg": {
        "a": 4,
        "b": 3,
        "c": 3
    }
}

TASK [Count items in a list] **************************************************************
ok: [localhost] => {
    "msg": {
        "bike": 2,
        "car": 2,
        "plane": 1
    }
}
```

This plugin is useful for selecting resources based on current allocation:

```yaml+jinja
- name: Get ID of SCSI controller(s) with less than 4 disks attached and choose the one with the least disks
  debug:
    msg: >-
      {{
         ( disks | dict2items | map(attribute='value.adapter') | list
           | community.general.counter | dict2items
           | rejectattr('value', '>=', 4) | sort(attribute='value') | first
         ).key
      }}
  vars:
    disks:
      sda:
        adapter: scsi_1
      sdb:
        adapter: scsi_1
      sdc:
        adapter: scsi_1
      sdd:
        adapter: scsi_1
      sde:
        adapter: scsi_2
      sdf:
        adapter: scsi_3
      sdg:
        adapter: scsi_3
```

This produces:

```ansible-output
TASK [Get ID of SCSI controller(s) with less than 4 disks attached and choose the one with the least disks]
ok: [localhost] => {
    "msg": "scsi_2"
}
```

New in version 4.3.0.
