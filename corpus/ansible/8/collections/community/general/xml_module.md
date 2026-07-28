---
collection: ansible
version: "8"
title: "community.general.xml module – Manage bits and pieces of XML files or strings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/xml_module.html
fetched_at: 2026-07-28T01:51:35+00:00
---
# community.general.xml module – Manage bits and pieces of XML files or strings

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](xml_module.md#ansible-collections-community-general-xml-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.xml`.

- [Synopsis](xml_module.md#synopsis)
- [Requirements](xml_module.md#requirements)
- [Parameters](xml_module.md#parameters)
- [Attributes](xml_module.md#attributes)
- [Notes](xml_module.md#notes)
- [See Also](xml_module.md#see-also)
- [Examples](xml_module.md#examples)
- [Return Values](xml_module.md#return-values)

## [Synopsis](xml_module.md#id1)

- A CRUD-like interface to managing bits of XML files.

Aliases: files.xml

## [Requirements](xml_module.md#id2)

The below requirements are needed on the host that executes this module.

- lxml >= 2.3.0

## [Parameters](xml_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **add_children**  list / elements=any | Add additional child-element(s) to a selected element for a given `xpath`.  Child elements must be given in a list and each item may be either a string (for example `children=ansible` to add an empty `<ansible/>` child element), or a hash where the key is an element name and the value is the element value.  This parameter requires `xpath` to be set. |
| **attribute**  any | The attribute to select when using parameter `value`.  This is a string, not prepended with `@`. |
| **backup**  boolean | Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.  **Choices:**   - `false` ← (default) - `true` |
| **content**  string | Search for a given `xpath` and get content.  This parameter requires `xpath` to be set.  **Choices:**   - `"attribute"` - `"text"` |
| **count**  boolean | Search for a given `xpath` and provide the count of any matches.  This parameter requires `xpath` to be set.  **Choices:**   - `false` ← (default) - `true` |
| **input_type**  string | Type of input for `add_children` and `set_children`.  **Choices:**   - `"xml"` - `"yaml"` ← (default) |
| **insertafter**  boolean | Add additional child-element(s) after the last selected element for a given `xpath`.  Child elements must be given in a list and each item may be either a string (for example `children=ansible` to add an empty `<ansible/>` child element), or a hash where the key is an element name and the value is the element value.  This parameter requires `xpath` to be set.  **Choices:**   - `false` ← (default) - `true` |
| **insertbefore**  boolean | Add additional child-element(s) before the first selected element for a given `xpath`.  Child elements must be given in a list and each item may be either a string (for example `children=ansible` to add an empty `<ansible/>` child element), or a hash where the key is an element name and the value is the element value.  This parameter requires `xpath` to be set.  **Choices:**   - `false` ← (default) - `true` |
| **namespaces**  dictionary | The namespace `prefix:uri` mapping for the XPath expression.  Needs to be a `dict`, not a `list` of items.  **Default:** `{}` |
| **path**  aliases: dest, file  path | Path to the file to operate on.  This file must exist ahead of time.  This parameter is required, unless `xmlstring` is given. |
| **pretty_print**  boolean | Pretty print XML output.  **Choices:**   - `false` ← (default) - `true` |
| **print_match**  boolean | Search for a given `xpath` and print out any matches.  This parameter requires `xpath` to be set.  **Choices:**   - `false` ← (default) - `true` |
| **set_children**  list / elements=any | Set the child-element(s) of a selected element for a given `xpath`.  Removes any existing children.  Child elements must be specified as in `add_children`.  This parameter requires `xpath` to be set. |
| **state**  aliases: ensure  string | Set or remove an xpath selection (node(s), attribute(s)).  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **strip_cdata_tags**  boolean | Remove CDATA tags surrounding text values.  Note that this might break your XML file if text values contain characters that could be interpreted as XML.  **Choices:**   - `false` ← (default) - `true` |
| **value**  any | Desired state of the selected attribute.  Either a string, or to unset a value, the Python `None` keyword (YAML Equivalent, `null`).  Elements default to no value (but present).  Attributes default to an empty string. |
| **xmlstring**  string | A string containing XML on which to operate.  This parameter is required, unless `path` is given. |
| **xpath**  string | A valid XPath expression describing the item(s) you want to manipulate.  Operates on the document root, `/`, by default. |

## [Attributes](xml_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](xml_module.md#id5)

> **Note:**
>
> - Use the `--check` and `--diff` options when testing your expressions.
> - The diff output is automatically pretty-printed, so may not reflect the actual file content, only the file structure.
> - This module does not handle complicated xpath expressions, so limit xpath selectors to simple expressions.
> - Beware that in case your XML elements are namespaced, you need to use the `namespaces` parameter, see the examples.
> - Namespaces prefix should be used for all children of an element where namespace is defined, unless another namespace is defined for them.

## [See Also](xml_module.md#id6)

> **See also:**
>
> [Xml module development community wiki](https://github.com/ansible/community/wiki/Module:-xml)
> :   More information related to the development of this xml module.
>
> [Introduction to XPath](https://www.w3schools.com/xml/xpath_intro.asp)
> :   A brief tutorial on XPath (w3schools.com).
>
> [XPath Reference document](https://developer.mozilla.org/en-US/docs/Web/XPath)
> :   The reference documentation on XSLT/XPath (developer.mozilla.org).

## [Examples](xml_module.md#id7)

```yaml+jinja
# Consider the following XML file:
#
# <business type="bar">
#   <name>Tasty Beverage Co.</name>
#     <beers>
#       <beer>Rochefort 10</beer>
#       <beer>St. Bernardus Abbot 12</beer>
#       <beer>Schlitz</beer>
#    </beers>
#   <rating subjective="true">10</rating>
#   <website>
#     <mobilefriendly/>
#     <address>http://tastybeverageco.com</address>
#   </website>
# </business>

- name: Remove the 'subjective' attribute of the 'rating' element
  community.general.xml:
    path: /foo/bar.xml
    xpath: /business/rating/@subjective
    state: absent

- name: Set the rating to '11'
  community.general.xml:
    path: /foo/bar.xml
    xpath: /business/rating
    value: 11

# Retrieve and display the number of nodes
- name: Get count of 'beers' nodes
  community.general.xml:
    path: /foo/bar.xml
    xpath: /business/beers/beer
    count: true
  register: hits

- ansible.builtin.debug:
    var: hits.count

# Example where parent XML nodes are created automatically
- name: Add a 'phonenumber' element to the 'business' element
  community.general.xml:
    path: /foo/bar.xml
    xpath: /business/phonenumber
    value: 555-555-1234

- name: Add several more beers to the 'beers' element
  community.general.xml:
    path: /foo/bar.xml
    xpath: /business/beers
    add_children:
    - beer: Old Rasputin
    - beer: Old Motor Oil
    - beer: Old Curmudgeon

- name: Add several more beers to the 'beers' element and add them before the 'Rochefort 10' element
  community.general.xml:
    path: /foo/bar.xml
    xpath: '/business/beers/beer[text()="Rochefort 10"]'
    insertbefore: true
    add_children:
    - beer: Old Rasputin
    - beer: Old Motor Oil
    - beer: Old Curmudgeon

# NOTE: The 'state' defaults to 'present' and 'value' defaults to 'null' for elements
- name: Add a 'validxhtml' element to the 'website' element
  community.general.xml:
    path: /foo/bar.xml
    xpath: /business/website/validxhtml

- name: Add an empty 'validatedon' attribute to the 'validxhtml' element
  community.general.xml:
    path: /foo/bar.xml
    xpath: /business/website/validxhtml/@validatedon

- name: Add or modify an attribute, add element if needed
  community.general.xml:
    path: /foo/bar.xml
    xpath: /business/website/validxhtml
    attribute: validatedon
    value: 1976-08-05

# How to read an attribute value and access it in Ansible
- name: Read an element's attribute values
  community.general.xml:
    path: /foo/bar.xml
    xpath: /business/website/validxhtml
    content: attribute
  register: xmlresp

- name: Show an attribute value
  ansible.builtin.debug:
    var: xmlresp.matches[0].validxhtml.validatedon

- name: Remove all children from the 'website' element (option 1)
  community.general.xml:
    path: /foo/bar.xml
    xpath: /business/website/*
    state: absent

- name: Remove all children from the 'website' element (option 2)
  community.general.xml:
    path: /foo/bar.xml
    xpath: /business/website
    set_children: []

# In case of namespaces, like in below XML, they have to be explicitly stated.
#
# <foo xmlns="http://x.test" xmlns:attr="http://z.test">
#   <bar>
#     <baz xmlns="http://y.test" attr:my_namespaced_attribute="true" />
#   </bar>
# </foo>

# NOTE: There is the prefix 'x' in front of the 'bar' element, too.
- name: Set namespaced '/x:foo/x:bar/y:baz/@z:my_namespaced_attribute' to 'false'
  community.general.xml:
    path: foo.xml
    xpath: /x:foo/x:bar/y:baz
    namespaces:
      x: http://x.test
      y: http://y.test
      z: http://z.test
    attribute: z:my_namespaced_attribute
    value: 'false'

- name: Adding building nodes with floor subnodes from a YAML variable
  community.general.xml:
    path: /foo/bar.xml
    xpath: /business
    add_children:
      - building:
          # Attributes
          name: Scumm bar
          location: Monkey island
          # Subnodes
          _:
            - floor: Pirate hall
            - floor: Grog storage
            - construction_date: "1990"  # Only strings are valid
      - building: Grog factory

# Consider this XML for following example -
#
# <config>
#   <element name="test1">
#     <text>part to remove</text>
#   </element>
#   <element name="test2">
#     <text>part to keep</text>
#   </element>
# </config>

- name: Delete element node based upon attribute
  community.general.xml:
    path: bar.xml
    xpath: /config/element[@name='test1']
    state: absent
```

## [Return Values](xml_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **actions**  dictionary | A dictionary with the original xpath, namespaces and state.  **Returned:** success  **Sample:** `{"namespaces": ["namespace1", "namespace2"], "state=present": null, "xpath": "xpath"}` |
| **backup_file**  string | The name of the backup file that was created  **Returned:** when `backup=true`  **Sample:** `"/path/to/file.xml.1942.2017-08-24@14:16:01~"` |
| **count**  integer | The count of xpath matches.  **Returned:** when parameter ‘count’ is set  **Sample:** `2` |
| **matches**  list / elements=string | The xpath matches found.  **Returned:** when parameter ‘print_match’ is set |
| **msg**  string | A message related to the performed action(s).  **Returned:** always |
| **xmlstring**  string | An XML string of the resulting output.  **Returned:** when parameter ‘xmlstring’ is set |

### Authors

- Tim Bielawa (@tbielawa)
- Magnus Hedemark (@magnus919)
- Dag Wieers (@dagwieers)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
