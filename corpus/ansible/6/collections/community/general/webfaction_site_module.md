---
collection: ansible
version: "6"
title: "community.general.webfaction_site module – Add or remove a website on a Webfaction host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/webfaction_site_module.html
fetched_at: 2026-07-27T17:14:02+00:00
---
# community.general.webfaction_site module – Add or remove a website on a Webfaction host

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
> To use it in a playbook, specify: `community.general.webfaction_site`.

- [Synopsis](webfaction_site_module.md#synopsis)
- [Parameters](webfaction_site_module.md#parameters)
- [Notes](webfaction_site_module.md#notes)
- [Examples](webfaction_site_module.md#examples)

## [Synopsis](webfaction_site_module.md#id1)

- Add or remove a website on a Webfaction host. Further documentation at <https://github.com/quentinsf/ansible-webfaction>.

## [Parameters](webfaction_site_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **host**  string / required | The webfaction host on which the site should be created. |
| **https**  boolean | Whether or not to use HTTPS  Choices:   - `false` ← (default) - `true` |
| **login_name**  string / required | The webfaction account to use |
| **login_password**  string / required | The webfaction password to use |
| **name**  string / required | The name of the website |
| **site_apps**  list / elements=list | A mapping of URLs to apps  Default: `[]` |
| **state**  string | Whether the website should exist  Choices:   - `"present"` ← (default) - `"absent"` |
| **subdomains**  list / elements=string | A list of subdomains associated with this site.  Default: `[]` |

## [Notes](webfaction_site_module.md#id3)

> **Note:**
>
> - Sadly, you *do* need to know your webfaction hostname for the `host` parameter. But at least, unlike the API, you don’t need to know the IP address. You can use a DNS name.
> - If a site of the same name exists in the account but on a different host, the operation will exit.
> - You can run playbooks that use this on a local machine, or on a Webfaction host, or elsewhere, since the scripts use the remote webfaction API. The location is not important. However, running them on multiple hosts *simultaneously* is best avoided. If you don’t specify *localhost* as your host, you may want to add `serial: 1` to the plays.
> - See `the webfaction API <<https://docs.webfaction.com/xmlrpc-api/>>`_ for more info.

## [Examples](webfaction_site_module.md#id4)

```yaml+jinja
- name: Create website
  community.general.webfaction_site:
    name: testsite1
    state: present
    host: myhost.webfaction.com
    subdomains:
      - 'testsite1.my_domain.org'
    site_apps:
      - ['testapp1', '/']
    https: false
    login_name: "{{webfaction_user}}"
    login_password: "{{webfaction_passwd}}"
```

### Authors

- Quentin Stafford-Fraser (@quentinsf)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
