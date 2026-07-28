---
collection: ansible
version: "6"
title: "Working with Unicode"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/docsite/filter_guide_working_with_unicode.html
fetched_at: 2026-07-28T00:24:58+00:00
---
# Working with Unicode

[Unicode](https://unicode.org/main.html) makes it possible to produce two strings which may be visually equivalent, but are comprised of distinctly different characters/character sequences. To address this `Unicode` defines [normalization forms](https://unicode.org/reports/tr15/) which avoid these distinctions by choosing a unique character sequence for a given visual representation.

You can use the `community.general.unicode_normalize` filter to normalize `Unicode` strings within your playbooks.

```yaml+jinja
- name: Compare Unicode representations
  debug:
    msg: "{{ with_combining_character | community.general.unicode_normalize == without_combining_character }}"
  vars:
    with_combining_character: "{{ 'Mayagu\u0308ez' }}"
    without_combining_character: Mayagüez
```

This produces:

```ansible-output
TASK [Compare Unicode representations] ********************************************************
ok: [localhost] => {
    "msg": true
}
```

The `community.general.unicode_normalize` filter accepts a keyword argument to select the `Unicode` form used to normalize the input string.

form:
:   One of `'NFC'` (default), `'NFD'`, `'NFKC'`, or `'NFKD'`. See the [Unicode reference](https://unicode.org/reports/tr15/) for more information.

New in version 3.7.0.
