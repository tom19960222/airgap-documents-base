---
collection: gitlab
version: "17.9.8"
title: "Cleartext authentication"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/user/application_security/api_security_testing/checks/cleartext_authentication_check.md
fetched_at: 2025-05-07T10:05:15Z
---
## Description

This check looks for cleartext authentication such as HTTP Basic auth with no-TLS.

## Remediation

Authentication credentials are transported via unencrypted channel (HTTP). This exposes the transmitted credentials to any attacker who can monitor (sniff) the network traffic during transmission. Sensitive information such as credentials should always be transmitted via encrypted channels such as HTTPS.

## Links

- [OWASP](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/)
- [CWE](https://cwe.mitre.org/data/definitions/319.html)
