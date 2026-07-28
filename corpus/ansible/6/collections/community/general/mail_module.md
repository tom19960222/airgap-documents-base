---
collection: ansible
version: "6"
title: "community.general.mail module – Send an email"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/mail_module.html
fetched_at: 2026-07-27T17:10:44+00:00
---
# community.general.mail module – Send an email

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
> To use it in a playbook, specify: `community.general.mail`.

- [Synopsis](mail_module.md#synopsis)
- [Parameters](mail_module.md#parameters)
- [Examples](mail_module.md#examples)

## [Synopsis](mail_module.md#id1)

- This module is useful for sending emails from playbooks.
- One may wonder why automate sending emails? In complex environments there are from time to time processes that cannot be automated, either because you lack the authority to make it so, or because not everyone agrees to a common approach.
- If you cannot automate a specific step, but the step is non-blocking, sending out an email to the responsible party to make them perform their part of the bargain is an elegant way to put the responsibility in someone else’s lap.
- Of course sending out a mail can be equally useful as a way to notify one or more people in a team that a specific action has been (successfully) taken.

## [Parameters](mail_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attach**  list / elements=path | A list of pathnames of files to attach to the message.  Attached files will have their content-type set to `application/octet-stream`.  Default: `[]` |
| **bcc**  list / elements=string | The email-address(es) the mail is being ‘blind’ copied to.  This is a list, which may contain address and phrase portions.  Default: `[]` |
| **body**  string | The body of the email being sent. |
| **cc**  list / elements=string | The email-address(es) the mail is being copied to.  This is a list, which may contain address and phrase portions.  Default: `[]` |
| **charset**  string | The character set of email being sent.  Default: `"utf-8"` |
| **ehlohost**  string  added in community.general 3.8.0 | Allows for manual specification of host for EHLO. |
| **headers**  list / elements=string | A list of headers which should be added to the message.  Each individual header is specified as `header=value` (see example below).  Default: `[]` |
| **host**  string | The mail server.  Default: `"localhost"` |
| **password**  string | If SMTP requires password. |
| **port**  integer | The mail server port.  This must be a valid integer between 1 and 65534  Default: `25` |
| **secure**  string | If `always`, the connection will only send email if the connection is Encrypted. If the server doesn’t accept the encrypted connection it will fail.  If `try`, the connection will attempt to setup a secure SSL/TLS session, before trying to send.  If `never`, the connection will not attempt to setup a secure SSL/TLS session, before sending  If `starttls`, the connection will try to upgrade to a secure SSL/TLS connection, before sending. If it is unable to do so it will fail.  Choices:   - `"always"` - `"never"` - `"starttls"` - `"try"` ← (default) |
| **sender**  aliases: from  string | The email-address the mail is sent from. May contain address and phrase.  Default: `"root"` |
| **subject**  aliases: msg  string / required | The subject of the email being sent. |
| **subtype**  string | The minor mime type, can be either `plain` or `html`.  The major type is always `text`.  Choices:   - `"html"` - `"plain"` ← (default) |
| **timeout**  integer | Sets the timeout in seconds for connection attempts.  Default: `20` |
| **to**  aliases: recipients  list / elements=string | The email-address(es) the mail is being sent to.  This is a list, which may contain address and phrase portions.  Default: `["root"]` |
| **username**  string | If SMTP requires username. |

## [Examples](mail_module.md#id3)

```yaml+jinja
- name: Example playbook sending mail to root
  community.general.mail:
    subject: System {{ ansible_hostname }} has been successfully provisioned.
  delegate_to: localhost

- name: Sending an e-mail using Gmail SMTP servers
  community.general.mail:
    host: smtp.gmail.com
    port: 587
    username: username@gmail.com
    password: mysecret
    to: John Smith <john.smith@example.com>
    subject: Ansible-report
    body: System {{ ansible_hostname }} has been successfully provisioned.
  delegate_to: localhost

- name: Send e-mail to a bunch of users, attaching files
  community.general.mail:
    host: 127.0.0.1
    port: 2025
    subject: Ansible-report
    body: Hello, this is an e-mail. I hope you like it ;-)
    from: jane@example.net (Jane Jolie)
    to:
    - John Doe <j.d@example.org>
    - Suzie Something <sue@example.com>
    cc: Charlie Root <root@localhost>
    attach:
    - /etc/group
    - /tmp/avatar2.png
    headers:
    - Reply-To=john@example.com
    - X-Special="Something or other"
    charset: us-ascii
  delegate_to: localhost

- name: Sending an e-mail using the remote machine, not the Ansible controller node
  community.general.mail:
    host: localhost
    port: 25
    to: John Smith <john.smith@example.com>
    subject: Ansible-report
    body: System {{ ansible_hostname }} has been successfully provisioned.

- name: Sending an e-mail using Legacy SSL to the remote machine
  community.general.mail:
    host: localhost
    port: 25
    to: John Smith <john.smith@example.com>
    subject: Ansible-report
    body: System {{ ansible_hostname }} has been successfully provisioned.
    secure: always

- name: Sending an e-mail using StartTLS to the remote machine
  community.general.mail:
    host: localhost
    port: 25
    to: John Smith <john.smith@example.com>
    subject: Ansible-report
    body: System {{ ansible_hostname }} has been successfully provisioned.
    secure: starttls

- name: Sending an e-mail using StartTLS, remote server, custom EHLO
  community.general.mail:
    host: some.smtp.host.tld
    port: 25
    ehlohost: my-resolvable-hostname.tld
    to: John Smith <john.smith@example.com>
    subject: Ansible-report
    body: System {{ ansible_hostname }} has been successfully provisioned.
    secure: starttls
```

### Authors

- Dag Wieers (@dagwieers)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
