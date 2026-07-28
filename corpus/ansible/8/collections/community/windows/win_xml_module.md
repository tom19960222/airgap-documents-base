---
collection: ansible
version: "8"
title: "community.windows.win_xml module – Manages XML file content on Windows hosts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_xml_module.html
fetched_at: 2026-07-28T02:02:36+00:00
---
# community.windows.win_xml module – Manages XML file content on Windows hosts

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_xml`.

- [Synopsis](win_xml_module.md#synopsis)
- [Parameters](win_xml_module.md#parameters)
- [Notes](win_xml_module.md#notes)
- [See Also](win_xml_module.md#see-also)
- [Examples](win_xml_module.md#examples)
- [Return Values](win_xml_module.md#return-values)

## [Synopsis](win_xml_module.md#id1)

- Manages XML nodes, attributes and text, using xpath to select which xml nodes need to be managed.
- XML fragments, formatted as strings, are used to specify the desired state of a part or parts of XML files on remote Windows servers.
- For non-Windows targets, use the [community.general.xml](../general/xml_module.md#ansible-collections-community-general-xml-module) module instead.

## [Parameters](win_xml_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attribute**  string | The attribute name if the type is ‘attribute’.  Required if `type=attribute`. |
| **backup**  boolean | Determine whether a backup should be created.  When set to `yes`, create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.  **Choices:**   - `false` ← (default) - `true` |
| **count**  boolean | When set to `yes`, return the number of nodes matched by *xpath*.  **Choices:**   - `false` ← (default) - `true` |
| **fragment**  aliases: xmlstring  string | The string representation of the XML fragment expected at xpath. Since ansible 2.9 not required when *state=absent*, or when *count=yes*. |
| **path**  aliases: dest, file  path / required | Path to the file to operate on. |
| **state**  string | Set or remove the nodes (or attributes) matched by *xpath*.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **type**  string | The type of XML node you are working with.  **Choices:**   - `"attribute"` - `"element"` ← (default) - `"text"` |
| **xpath**  string / required | Xpath to select the node or nodes to operate on. |

## [Notes](win_xml_module.md#id3)

> **Note:**
>
> - Only supports operating on xml elements, attributes and text.
> - Namespace, processing-instruction, command and document node types cannot be modified with this module.

## [See Also](win_xml_module.md#id4)

> **See also:**
>
> [community.general.xml](../general/xml_module.md#ansible-collections-community-general-xml-module)
> :   XML manipulation for Posix hosts.
>
> [w3shools XPath tutorial](https://www.w3schools.com/xml/xpath_intro.asp)
> :   A useful tutorial on XPath

## [Examples](win_xml_module.md#id5)

```yaml+jinja
- name: Apply our filter to Tomcat web.xml
  community.windows.win_xml:
   path: C:\apache-tomcat\webapps\myapp\WEB-INF\web.xml
   fragment: '<filter><filter-name>MyFilter</filter-name><filter-class>com.example.MyFilter</filter-class></filter>'
   xpath: '/*'

- name: Apply sslEnabledProtocols to Tomcat's server.xml
  community.windows.win_xml:
   path: C:\Tomcat\conf\server.xml
   xpath: '//Server/Service[@name="Catalina"]/Connector[@port="9443"]'
   attribute: 'sslEnabledProtocols'
   fragment: 'TLSv1,TLSv1.1,TLSv1.2'
   type: attribute

- name: remove debug configuration nodes from nlog.conf
  community.windows.win_xml:
   path: C:\IISApplication\nlog.conf
   xpath: /nlog/rules/logger[@name="debug"]/descendant::*
   state: absent

- name: count configured connectors in Tomcat's server.xml
  community.windows.win_xml:
   path: C:\Tomcat\conf\server.xml
   xpath: //Server/Service/Connector
   count: yes
  register: connector_count

- name: show connector count
  debug:
    msg="Connector count is {{connector_count.count}}"

- name: ensure all lang=en attributes to lang=nl
  community.windows.win_xml:
   path: C:\Data\Books.xml
   xpath: //@[lang="en"]
   attribute: lang
   fragment: nl
   type: attribute
```

## [Return Values](win_xml_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_file**  string | Name of the backup file that was created.  **Returned:** if backup=yes  **Sample:** `"C:\\Path\\To\\File.txt.11540.20150212-220915.bak"` |
| **count**  integer | Number of nodes matched by xpath.  **Returned:** if count=yes  **Sample:** `33` |
| **err**  list / elements=string | XML comparison exceptions.  **Returned:** always, for type element and -vvv or more  **Sample:** `["attribute mismatch for actual=string"]` |
| **msg**  string | What was done.  **Returned:** always  **Sample:** `"xml added"` |

### Authors

- Richard Levenberg (@richardcs)
- Jon Hawkesworth (@jhawkesworth)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
