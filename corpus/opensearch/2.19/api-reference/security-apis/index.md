---
collection: "opensearch"
version: "2.19"
title: "Security APIs"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/security-apis.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/security-apis.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/security-apis/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/security/index/"
canonical_route: "/api-reference/security/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 84
---
# Security APIs

Security APIs provide information that can be very useful in troubleshooting connection and configuration issues.

API | Method | Description
:--- | :--- | :---
`/_plugins/_security/whoami` | GET/POST | Returns basic details about the logged-in user.
`/_opendistro/_security/sslinfo` | GET | Returns details about the SSL connection when using certificate authentication.
`/_plugins/_security/api/permissionsinfo` | GET | Returns permission details for the logged-in user.
`/_plugins/_security/authinfo` | GET/POST | Returns the backend roles and OpenSearch roles mapped to the logged-in user.
`/_plugins/_security/api/ssl/certs` | GET | Displays the details and expiration dates of the certificates used on the OpenSearch HTTP and transport communication layers. Can only be called by users with the `superadmin` certificate.
`/_plugins/_security/api/ssl/transport/reloadcerts` | PUT | Reloads the certificates on the `transport` layer. For more information, see [Reload TLS certificates on the transport layer](../../security/configuration/tls/index.md#reload-tls-certificates-on-the-transport-layer).
`/_plugins/_security/api/ssl/http/reloadcerts` | PUT | Reloads the certificates on the `http` layer. For more information, see [Reload TLS certificates on the http layer](../../security/configuration/tls/index.md#reload-tls-certificates-on-the-http-layer).
