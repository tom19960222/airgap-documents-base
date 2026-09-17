---
collection: "opensearch"
version: "2.19"
title: "User impersonation"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_security/access-control/impersonation.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_security/access-control/impersonation.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/security/access-control/impersonation/"
canonical_url: "https://docs.opensearch.org/latest/security/access-control/impersonation/"
canonical_route: "/security/access-control/impersonation/"
redirect_from: ["/security/access-control/impersonation/","/security-plugin/access-control/impersonation/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 100
parent: "Access control"
---
# User impersonation

User impersonation allows specially privileged users to act as another user without knowledge of nor access to the impersonated user's credentials.

Impersonation can be useful for testing and troubleshooting, or for allowing system services to safely act as a user.

Impersonation can occur on either the REST interface or at the transport layer.

## REST interface

To allow one user to impersonate another, add the following to `opensearch.yml`:

```yml
plugins.security.authcz.rest_impersonation_user:
  <AUTHENTICATED_USER>:
    - <IMPERSONATED_USER_1>
    - <IMPERSONATED_USER_2>
```

The impersonated user field supports wildcards. Setting it to `*` allows `AUTHENTICATED_USER` to impersonate any user.

## Transport interface

In a similar fashion, add the following to enable transport layer impersonation:

```yml
plugins.security.authcz.impersonation_dn:
  "CN=spock,OU=client,O=client,L=Test,C=DE":
    - worf
```

## Impersonating users

To impersonate another user, submit a request to the system with the HTTP header `opendistro_security_impersonate_as` set to the name of the user to be impersonated. A good test is to make a GET request to the `_plugins/_security/authinfo` URI:

```bash
curl -XGET -u 'admin:<custom-admin-password>' -k -H "opendistro_security_impersonate_as: user_1" https://localhost:9200/_plugins/_security/authinfo?pretty
```
