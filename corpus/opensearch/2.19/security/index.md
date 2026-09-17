---
collection: "opensearch"
version: "2.19"
title: "About Security"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_security/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_security/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/security/"
canonical_url: "https://docs.opensearch.org/latest/security/"
canonical_route: "/security/"
redirect_from: ["/security-plugin/","/security/index/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
has_toc: false
layout: "default"
nav_exclude: true
nav_order: 1
---
# About Security in OpenSearch

Security in OpenSearch is built around four main features that work together to safeguard data and track activity within a cluster. Separately, these features are:

* Encryption.
* Authentication.
* Access control.
* Audit logging and compliance.

Used together they provide effective protection of sensitive data by placing it behind multiple layers of defense and granting or restricting access to the data at different levels in the OpenSearch data structure. Most implementations use a combination of options for these features to meet specific security needs.

## Features at a glance

The following topics provide a general description of the features that define security in OpenSearch.

### Encryption

Encryption typically addresses the protection of data both at rest and in transit. OpenSearch Security is responsible for managing encryption in transit.

In transit, Security encrypts data moving to, from, and within the cluster. OpenSearch uses the TLS protocol, which covers both client-to-node encryption (the REST layer) and node-to-node encryption (the transport layer). This combination of in-transit encryption helps ensure that both requests to OpenSearch and the movement of data among different nodes are safe from tampering.

You can find out more about configuring TLS in the [Configuring TLS certificates](configuration/tls/index.md) section.

Encryption at rest, on the other hand, protects data stored in the cluster, including indexes, logs, swap files, automated snapshots, and all data in the application directory. This type of encryption is managed by the operating system on each OpenSearch node. For information about enabling encryption at rest, see [Encryption at rest](../troubleshoot/index.md#encryption-at-rest).

### Authentication

Authentication is used to validate the identity of users and works by verifying an end user’s credentials against a backend configuration. These credentials can be a simple name and password, a JSON web token, or a TLS certificate. Once the authentication domain extracts those credentials from a user’s request, it can check their validity against the authentication backend.

The backend used for validation can be OpenSearch's built-in internal user database—used for storing user and role configurations and hashed passwords—or one of a wide range of industry-standard identification protocols such as LDAP, Active Directory, SAML, or OpenID Connect. A common practice is to chain together more than one authentication method to create a more robust defense against unauthorized access. This might involve, for example, HTTP basic authentication followed by a backend configuration that specifies the LDAP protocol. See the [Configuring the Security backend](configuration/configuration/index.md) section to learn more about setting up the backend.

### Access control

Access control (or authorization) generally involves selectively assigning permissions to users that allow them to perform specific tasks, such as clearing the cache for a particular index or taking a snapshot of a cluster. However, rather than assign individual permissions directly to users, OpenSearch assigns these permissions to roles and then maps the roles to users. For more on setting up these relationships, see [Users and roles](access-control/users-roles/index.md). Roles, therefore, define the actions that users can perform, including the data they can read, the cluster settings they can modify, the indexes to which they can write, and so on. Roles are reusable across multiple users, and users can have multiple roles.

Another notable characteristic of access control in OpenSearch is the ability to assign user access through levels of increasing granularity. Fine-grained access control (FGAC) means that a role can control permissions for users at not only the cluster level but also the index level, the document level, and even the field level. For example, a role may provide a user access to certain cluster-level permissions but at the same time prevent the user from accessing a given group of indexes. Likewise, that role may grant access to certain types of documents but not others, or it may even include access to specific fields within a document but exclude access to other sensitive fields. Field masking further extends FGAC by providing options to mask certain types of data, such as a list of emails, which can still be aggregated but not made viewable to a role.

To learn more about this feature, see the [Access control](access-control/index.md) section of the security documentation.

### Audit logging and compliance

Finally, audit logging and compliance refer to mechanisms that allow for tracking and analysis of activity within a cluster. This is important after data breaches (unauthorized access) or when data suffers unintended exposure, as could happen when the data is left vulnerable in an unsecured location. However, audit logging can be just as valuable a tool for assessing excessive loads on a cluster or surveying trends for a given task. This feature allows you to review changes made anywhere in a cluster and track access patterns and API requests of all types, whether valid or invalid.

How OpenSearch archives logging is configurable at many levels of detail, and there are a number of options for where those logs are stored. Compliance features also ensure that all data is available if and when compliance auditing is required. In this case, the logging can be automated to focus on data especially pertinent to those compliance requirements.

See the [Audit logs](audit-logs/index.md) section of the security documentation to read more about this feature.

## Other features and functionality

OpenSearch includes other features that complement the security infrastructure.

### Dashboards multi-tenancy

One such feature is OpenSearch Dashboards multi-tenancy. Tenants are work spaces that include visualizations, index patterns, and other Dashboards objects. Multi-tenancy allows for the sharing of tenants among users of Dashboards and leverages OpenSearch roles to manage access to tenants and safely make them available to others.
For more information about creating tenants, see [OpenSearch Dashboards multi-tenancy](multi-tenancy/tenant-index/index.md).

### Cross-cluster search

Another notable feature is cross-cluster search. This feature provides users with the ability to perform searches from one node in a cluster across other clusters that have been set up to coordinate this type of search. As with other features, cross-cluster search is supported by the OpenSearch access control infrastructure, which defines the permissions users have for working with this feature.
To learn more, see [Cross-cluster search](../search-plugins/cross-cluster-search/index.md).

## Next steps

The [Best practices for OpenSearch security](configuration/best-practices/index.md)  guide covers 10 things to consider when getting started with OpenSearch security.

The [Security configuration](configuration/index.md) overview provides the basic steps for setting up security in your OpenSearch implementation and includes links to information about customizing security for your business needs.
