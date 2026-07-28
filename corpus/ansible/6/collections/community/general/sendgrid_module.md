---
collection: ansible
version: "6"
title: "community.general.sendgrid module – Sends an email with the SendGrid API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/sendgrid_module.html
fetched_at: 2026-07-27T17:13:08+00:00
---
# community.general.sendgrid module – Sends an email with the SendGrid API

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](sendgrid_module.md#ansible-collections-community-general-sendgrid-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.sendgrid`.

- [Synopsis](sendgrid_module.md#synopsis)
- [Requirements](sendgrid_module.md#requirements)
- [Parameters](sendgrid_module.md#parameters)
- [Notes](sendgrid_module.md#notes)
- [Examples](sendgrid_module.md#examples)

## [Synopsis](sendgrid_module.md#id1)

- Sends an email with a SendGrid account through their API, not through the SMTP service.

## [Requirements](sendgrid_module.md#id2)

The below requirements are needed on the host that executes this module.

- sendgrid Python library 1.6.22 or lower (Sendgrid API V2 supported)

## [Parameters](sendgrid_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string | Sendgrid API key to use instead of username/password. |
| **attachments**  list / elements=path | A list of relative or explicit paths of files you want to attach (7MB limit as per SendGrid docs). |
| **bcc**  list / elements=string | A list of email addresses to bcc. |
| **body**  string / required | The e-mail body content. |
| **cc**  list / elements=string | A list of email addresses to cc. |
| **from_address**  string / required | The address in the “from” field for the email. |
| **from_name**  string | The name you want to appear in the from field, i.e ‘John Doe’. |
| **headers**  dictionary | A dict to pass on as headers. |
| **html_body**  boolean | Whether the body is html content that should be rendered.  Choices:   - `false` ← (default) - `true` |
| **password**  string | Password that corresponds to the username.  Since 2.2 it is only required if *api_key* is not supplied. |
| **subject**  string / required | The desired subject for the email. |
| **to_addresses**  list / elements=string / required | A list with one or more recipient email addresses. |
| **username**  string | Username for logging into the SendGrid account.  Since 2.2 it is only required if *api_key* is not supplied. |

## [Notes](sendgrid_module.md#id4)

> **Note:**
>
> - This module is non-idempotent because it sends an email through the external API. It is idempotent only in the case that the module fails.
> - Like the other notification modules, this one requires an external dependency to work. In this case, you’ll need an active SendGrid account.
> - In order to use api_key, cc, bcc, attachments, from_name, html_body, headers you must pip install sendgrid
> - since 2.2 *username* and *password* are not required if you supply an *api_key*

## [Examples](sendgrid_module.md#id5)

```yaml+jinja
- name: Send an email to a single recipient that the deployment was successful
  community.general.sendgrid:
    username: "{{ sendgrid_username }}"
    password: "{{ sendgrid_password }}"
    from_address: "ansible@mycompany.com"
    to_addresses:
      - "ops@mycompany.com"
    subject: "Deployment success."
    body: "The most recent Ansible deployment was successful."
  delegate_to: localhost

- name: Send an email to more than one recipient that the build failed
  community.general.sendgrid:
      username: "{{ sendgrid_username }}"
      password: "{{ sendgrid_password }}"
      from_address: "build@mycompany.com"
      to_addresses:
        - "ops@mycompany.com"
        - "devteam@mycompany.com"
      subject: "Build failure!."
      body: "Unable to pull source repository from Git server."
  delegate_to: localhost
```

### Authors

- Matt Makai (@makaimc)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
