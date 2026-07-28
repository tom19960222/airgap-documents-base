---
collection: ansible
version: "6"
title: "community.general.pulp_repo module – Add or remove Pulp repos from a remote host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/pulp_repo_module.html
fetched_at: 2026-07-27T17:12:14+00:00
---
# community.general.pulp_repo module – Add or remove Pulp repos from a remote host

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
> To use it in a playbook, specify: `community.general.pulp_repo`.

- [Synopsis](pulp_repo_module.md#synopsis)
- [Parameters](pulp_repo_module.md#parameters)
- [Notes](pulp_repo_module.md#notes)
- [Examples](pulp_repo_module.md#examples)
- [Return Values](pulp_repo_module.md#return-values)

## [Synopsis](pulp_repo_module.md#id1)

- Add or remove Pulp repos from a remote host.
- Note, this is for Pulp 2 only.

## [Parameters](pulp_repo_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **add_export_distributor**  boolean | Whether or not to add the export distributor to new `rpm` repositories.  Choices:   - `false` ← (default) - `true` |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **feed**  string | Upstream feed URL to receive updates from. |
| **feed_ca_cert**  aliases: importer_ssl_ca_cert  string | CA certificate string used to validate the feed source SSL certificate. This can be the file content or the path to the file. |
| **feed_client_cert**  aliases: importer_ssl_client_cert  string | Certificate used as the client certificate when synchronizing the repository. This is used to communicate authentication information to the feed source. The value to this option must be the full path to the certificate. The specified file may be the certificate itself or a single file containing both the certificate and private key. This can be the file content or the path to the file. |
| **feed_client_key**  aliases: importer_ssl_client_key  string | Private key to the certificate specified in *importer_ssl_client_cert*, assuming it is not included in the certificate file itself. This can be the file content or the path to the file. |
| **force**  boolean | If `yes` do not get a cached copy.  Choices:   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | httplib2, the library used by the [ansible.builtin.uri](../../ansible/builtin/uri_module.md#ansible-collections-ansible-builtin-uri-module) module only sends authentication information when a webservice responds to an initial request with a 401 status. Since some basic auth services do not properly send a 401, logins will fail. This option forces the sending of the Basic authentication header upon initial request.  Choices:   - `false` ← (default) - `true` |
| **generate_sqlite**  boolean | Boolean flag to indicate whether sqlite files should be generated during a repository publish.  Choices:   - `false` ← (default) - `true` |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  Default: `"ansible-httpget"` |
| **name**  aliases: repo  string / required | Name of the repo to add or remove. This correlates to repo-id in Pulp. |
| **proxy_host**  string | Proxy url setting for the pulp repository importer. This is in the format scheme://host. |
| **proxy_password**  string | Proxy password for the pulp repository importer. |
| **proxy_port**  string | Proxy port setting for the pulp repository importer. |
| **proxy_username**  string | Proxy username for the pulp repository importer. |
| **publish_distributor**  string | Distributor to use when state is `publish`. The default is to publish all distributors. |
| **pulp_host**  string | URL of the pulp server to connect to.  Default: `"https://127.0.0.1"` |
| **relative_url**  string | Relative URL for the local repository. It’s required when state=present. |
| **repo_type**  string | Repo plugin type to use (i.e. `rpm`, `docker`).  Default: `"rpm"` |
| **repoview**  boolean | Whether to generate repoview files for a published repository. Setting this to `true` automatically activates `generate_sqlite`.  Choices:   - `false` ← (default) - `true` |
| **serve_http**  boolean | Make the repo available over HTTP.  Choices:   - `false` ← (default) - `true` |
| **serve_https**  boolean | Make the repo available over HTTPS.  Choices:   - `false` - `true` ← (default) |
| **state**  string | The repo state. A state of `sync` will queue a sync of the repo. This is asynchronous but not delayed like a scheduled sync. A state of `publish` will use the repository’s distributor to publish the content.  Choices:   - `"present"` ← (default) - `"absent"` - `"sync"` - `"publish"` |
| **url**  string | HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path |
| **url_password**  string | The password for use in HTTP basic authentication to the pulp API. If the *url_username* parameter is not specified, the *url_password* parameter will not be used. |
| **url_username**  string | The username for use in HTTP basic authentication to the pulp API. |
| **use_gssapi**  boolean  added in ansible-core 2.11 | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  Choices:   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **wait_for_completion**  boolean | Wait for asynchronous tasks to complete before returning.  Choices:   - `false` ← (default) - `true` |

## [Notes](pulp_repo_module.md#id3)

> **Note:**
>
> - This module can currently only create distributors and importers on rpm repositories. Contributions to support other repo types are welcome.

## [Examples](pulp_repo_module.md#id4)

```yaml+jinja
- name: Create a new repo with name 'my_repo'
  community.general.pulp_repo:
    name: my_repo
    relative_url: my/repo
    state: present

- name: Create a repo with a feed and a relative URL
  community.general.pulp_repo:
    name: my_centos_updates
    repo_type: rpm
    feed: http://mirror.centos.org/centos/6/updates/x86_64/
    relative_url: centos/6/updates
    url_username: admin
    url_password: admin
    force_basic_auth: true
    state: present

- name: Remove a repo from the pulp server
  community.general.pulp_repo:
    name: my_old_repo
    repo_type: rpm
    state: absent
```

## [Return Values](pulp_repo_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **repo**  string | Name of the repo that the action was performed on.  Returned: success  Sample: `"my_repo"` |

### Authors

- Joe Adams (@sysadmind)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
