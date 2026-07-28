---
collection: ansible
version: "6"
title: "community.general.jira module – Create and modify issues in a JIRA instance"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/jira_module.html
fetched_at: 2026-07-27T17:10:15+00:00
---
# community.general.jira module – Create and modify issues in a JIRA instance

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.jira`.

- [Synopsis](jira_module.md#synopsis)
- [Parameters](jira_module.md#parameters)
- [Notes](jira_module.md#notes)
- [Examples](jira_module.md#examples)

## [Synopsis](jira_module.md#id1)

- Create and modify issues in a JIRA instance.

## [Parameters](jira_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **account_id**  string  added in community.general 2.5.0 | Sets the account identifier for the assignee when *operation* is `create`, `transition` or `edit`.  Note that JIRA may not allow changing field values on specific transitions or states. |
| **assignee**  string | Sets the the assignee when *operation* is `create`, `transition` or `edit`.  Recent versions of JIRA no longer accept a user name as a user identifier. In that case, use *account_id* instead.  Note that JIRA may not allow changing field values on specific transitions or states. |
| **attachment**  dictionary  added in community.general 2.5.0 | Information about the attachment being uploaded. |
| **content**  string | The Base64 encoded contents of the file to attach. If not specified, the contents of *filename* will be used instead. |
| **filename**  path / required | The path to the file to upload (from the remote node) or, if *content* is specified, the filename to use for the attachment. |
| **mimetype**  string | The MIME type to supply for the upload. If not specified, best-effort detection will be done. |
| **comment**  string | The comment text to add.  Note that JIRA may not allow changing field values on specific transitions or states. |
| **comment_visibility**  dictionary  added in community.general 3.2.0 | Used to specify comment comment visibility.  See <https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issue-comments/#api-rest-api-2-issue-issueidorkey-comment-post> for details. |
| **type**  string / required | Use type to specify which of the JIRA visibility restriction types will be used.  Choices:   - `"group"` - `"role"` |
| **value**  string / required | Use value to specify value corresponding to the type of visibility restriction. For example name of the group or role. |
| **description**  string | The issue description, where appropriate.  Note that JIRA may not allow changing field values on specific transitions or states. |
| **fields**  dictionary | This is a free-form data structure that can contain arbitrary data. This is passed directly to the JIRA REST API (possibly after merging with other required data, as when passed to create). See examples for more information, and the JIRA REST API for the structure required for various fields.  When passed to comment, the data structure is merged at the first level since community.general 4.6.0. Useful to add JIRA properties for example.  Note that JIRA may not allow changing field values on specific transitions or states.  Default: `{}` |
| **inwardissue**  string | Set issue from which link will be created. |
| **issue**  aliases: ticket  string | An existing issue key to operate on. |
| **issuetype**  string | The issue type, for issue creation. |
| **jql**  string  added in community.general 0.2.0 | Query JIRA in JQL Syntax, e.g. ‘CMDB Hostname’=’test.example.com’. |
| **linktype**  string | Set type of link, when action ‘link’ selected. |
| **maxresults**  integer  added in community.general 0.2.0 | Limit the result of *operation=search*. If no value is specified, the default jira limit will be used.  Used when *operation=search* only, ignored otherwise. |
| **operation**  aliases: command  string / required | The operation to perform.  Choices:   - `"attach"` - `"comment"` - `"create"` - `"edit"` - `"fetch"` - `"link"` - `"search"` - `"transition"` - `"update"` |
| **outwardissue**  string | Set issue to which link will be created. |
| **password**  string | The password to log-in with.  Must be used with *username*. Mutually exclusive with *token*. |
| **project**  string | The project for this operation. Required for issue creation. |
| **status**  string | Only used when *operation* is `transition`, and a bit of a misnomer, it actually refers to the transition name. |
| **summary**  string | The issue summary, where appropriate.  Note that JIRA may not allow changing field values on specific transitions or states. |
| **timeout**  float | Set timeout, in seconds, on requests to JIRA API.  Default: `10.0` |
| **token**  string  added in community.general 4.2.0 | The personal access token to log-in with.  Mutually exclusive with *username* and *password*. |
| **uri**  string / required | Base URI for the JIRA instance. |
| **username**  string | The username to log-in with.  Must be used with *password*. Mutually exclusive with *token*. |
| **validate_certs**  boolean | Require valid SSL certificates (set to `false` if you’d like to use self-signed certificates)  Choices:   - `false` - `true` ← (default) |

## [Notes](jira_module.md#id3)

> **Note:**
>
> - Currently this only works with basic-auth, or tokens.
> - To use with JIRA Cloud, pass the login e-mail as the *username* and the API token as *password*.

## [Examples](jira_module.md#id4)

```yaml+jinja
# Create a new issue and add a comment to it:
- name: Create an issue
  community.general.jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    project: ANS
    operation: create
    summary: Example Issue
    description: Created using Ansible
    issuetype: Task
  args:
    fields:
        customfield_13225: "test"
        customfield_12931: {"value": "Test"}
  register: issue

- name: Comment on issue
  community.general.jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    issue: '{{ issue.meta.key }}'
    operation: comment
    comment: A comment added by Ansible

- name: Comment on issue with restricted visibility
  community.general.jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    issue: '{{ issue.meta.key }}'
    operation: comment
    comment: A comment added by Ansible
    comment_visibility:
      type: role
      value: Developers

- name: Comment on issue with property to mark it internal
  community.general.jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    issue: '{{ issue.meta.key }}'
    operation: comment
    comment: A comment added by Ansible
    fields:
      properties:
        - key: 'sd.public.comment'
          value:
            internal: true

# Assign an existing issue using edit
- name: Assign an issue using free-form fields
  community.general.jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    issue: '{{ issue.meta.key}}'
    operation: edit
    assignee: ssmith

# Create an issue with an existing assignee
- name: Create an assigned issue
  community.general.jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    project: ANS
    operation: create
    summary: Assigned issue
    description: Created and assigned using Ansible
    issuetype: Task
    assignee: ssmith

# Edit an issue
- name: Set the labels on an issue using free-form fields
  community.general.jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    issue: '{{ issue.meta.key }}'
    operation: edit
  args:
    fields:
        labels:
          - autocreated
          - ansible

# Updating a field using operations: add, set & remove
- name: Change the value of a Select dropdown
  community.general.jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    issue: '{{ issue.meta.key }}'
    operation: update
  args:
    fields:
      customfield_12931: [ {'set': {'value': 'Virtual'}} ]
      customfield_13820: [ {'set': {'value':'Manually'}} ]
  register: cmdb_issue
  delegate_to: localhost

# Retrieve metadata for an issue and use it to create an account
- name: Get an issue
  community.general.jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    project: ANS
    operation: fetch
    issue: ANS-63
  register: issue

# Search for an issue
# You can limit the search for specific fields by adding optional args. Note! It must be a dict, hence, lastViewed: null
- name: Search for an issue
  community.general.jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    project: ANS
    operation: search
    maxresults: 10
    jql: project=cmdb AND cf[13225]="test"
  args:
    fields:
      lastViewed: null
  register: issue

- name: Create a unix account for the reporter
  become: true
  user:
    name: '{{ issue.meta.fields.creator.name }}'
    comment: '{{ issue.meta.fields.creator.displayName }}'

# You can get list of valid linktypes at /rest/api/2/issueLinkType
# url of your jira installation.
- name: Create link from HSP-1 to MKY-1
  community.general.jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    operation: link
    linktype: Relates
    inwardissue: HSP-1
    outwardissue: MKY-1

# Transition an issue
- name: Resolve the issue
  community.general.jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    issue: '{{ issue.meta.key }}'
    operation: transition
    status: Resolve Issue
    account_id: 112233445566778899aabbcc
    fields:
      resolution:
        name: Done
      description: I am done! This is the last description I will ever give you.

# Attach a file to an issue
- name: Attach a file
  community.general.jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    issue: HSP-1
    operation: attach
    attachment:
      filename: topsecretreport.xlsx
```

### Authors

- Steve Smith (@tarka)
- Per Abildgaard Toft (@pertoft)
- Brandon McNama (@DWSR)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
