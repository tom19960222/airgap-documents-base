---
collection: "opensearch"
version: "2.19"
title: "Common issues"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_troubleshoot/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_troubleshoot/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/troubleshoot/"
canonical_url: "https://docs.opensearch.org/latest/troubleshoot/"
canonical_route: "/troubleshoot/"
redirect_from: ["/troubleshoot/index/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_toc: false
layout: "default"
nav_exclude: true
nav_order: 1
---
# Common issues

This page contains a list of common issues and workarounds.

## OpenSearch Dashboards fails to start

If you encounter the error `FATAL  Error: Request Timeout after 30000ms` during startup, try running OpenSearch Dashboards on a more powerful machine. We recommend four CPU cores and 8 GB of RAM.

## Requests to OpenSearch Dashboards fail with "Request must contain a osd-xsrf header"

If you run legacy Kibana OSS scripts against OpenSearch Dashboards---for example, curl commands that import saved objects from a file---they might fail with the following error:

```json
{"status": 400, "body": "Request must contain a osd-xsrf header."}
```

In this case, your scripts likely include the `"kbn-xsrf: true"` header. Switch it to the `osd-xsrf: true` header:

```
curl -XPOST -u 'admin:<custom-admin-password>' 'https://DASHBOARDS_ENDPOINT/api/saved_objects/_import' -H 'osd-xsrf:true' --form file=@export.ndjson
```

## Multi-tenancy issues in OpenSearch Dashboards

If you're testing multiple users in OpenSearch Dashboards and encounter unexpected changes in tenant, use Google Chrome in an Incognito window or Firefox in a Private window.

## Expired certificates

If your certificates have expired, you might receive the following error or something similar:

```
ERROR org.opensearch.security.ssl.transport.SecuritySSLNettyTransport - Exception during establishing a SSL connection: javax.net.ssl.SSLHandshakeException: PKIX path validation failed: java.security.cert.CertPathValidatorException: validity check failed
Caused by: java.security.cert.CertificateExpiredException: NotAfter: Thu Sep 16 11:27:55 PDT 2021
```

To check the expiration date for a certificate, run this command:

```bash
openssl x509 -enddate -noout -in <certificate>
```

## Encryption at rest

The operating system for each OpenSearch node handles encryption of data at rest. To enable encryption at rest in most Linux distributions, use the `cryptsetup` command:

```bash
cryptsetup luksFormat --key-file <key> <partition>
```

For full documentation about the command, see [cryptsetup(8) — Linux manual page](https://man7.org/linux/man-pages/man8/cryptsetup.8.html).

## Can't update by script when FLS, DLS, or field masking is active

The Security plugin blocks the update by script operation (`POST <index>/_update/<id>`) when field-level security, document-level security, or field masking are active. You can still update documents using the standard index operation (`PUT <index>/_doc/<id>`).

## Illegal reflective access operation in logs

This is a known issue with Performance Analyzer that shouldn't affect functionality.
