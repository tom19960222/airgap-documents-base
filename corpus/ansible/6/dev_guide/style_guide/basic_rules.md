---
collection: ansible
version: "6"
title: "Basic rules"
source_url: https://docs.ansible.com/projects/ansible/6/dev_guide/style_guide/basic_rules.html
fetched_at: 2026-07-27T16:40:51+00:00
---
# Basic rules

- [Use standard American English](basic_rules.md#use-standard-american-english)
- [Write for a global audience](basic_rules.md#write-for-a-global-audience)
- [Follow naming conventions](basic_rules.md#follow-naming-conventions)
- [Use clear sentence structure](basic_rules.md#use-clear-sentence-structure)
- [Avoid verbosity](basic_rules.md#avoid-verbosity)
- [Highlight menu items and commands](basic_rules.md#highlight-menu-items-and-commands)

## [Use standard American English](basic_rules.md#id1)

Ansible uses Standard American English. Watch for common words that are spelled differently in American English (color vs colour, organize vs organise, and so on).

## [Write for a global audience](basic_rules.md#id2)

Everything you say should be understandable by people of different backgrounds and cultures. Avoid idioms and regionalism and maintain a neutral tone that cannot be misinterpreted. Avoid attempts at humor.

## [Follow naming conventions](basic_rules.md#id3)

Always follow naming conventions and trademarks.

## [Use clear sentence structure](basic_rules.md#id4)

Clear sentence structure means:

- Start with the important information first.
- Avoid padding/adding extra words that make the sentence harder to understand.
- Keep it short - Longer sentences are harder to understand.

Some examples of improving sentences:

Bad:
:   The unwise walking about upon the area near the cliff edge may result in a dangerous fall and therefore it is recommended that one remains a safe distance to maintain personal safety.

Better:
:   Danger! Stay away from the cliff.

Bad:
:   Furthermore, large volumes of water are also required for the process of extraction.

Better:
:   Extraction also requires large volumes of water.

## [Avoid verbosity](basic_rules.md#id5)

Write short, succinct sentences. Avoid terms like:

- “…as has been said before,”
- “..each and every,”
- “…point in time,”
- “…in order to,”

## [Highlight menu items and commands](basic_rules.md#id6)

When documenting menus or commands, it helps to **bold** what is important.

For menu procedures, bold the menu names, button names, and so on to help the user find them on the GUI:

1. On the **File** menu, click **Open**.
2. Type a name in the **User Name** field.
3. In the **Open** dialog box, click **Save**.
4. On the toolbar, click the **Open File** icon.

For code or command snippets, use the RST [code-block directive](https://www.sphinx-doc.org/en/1.5/markup/code.html#directive-code-block):

```YAML+Jinja
.. code-block:: bash

  ssh my_vyos_user@vyos.example.net
  show config
```
