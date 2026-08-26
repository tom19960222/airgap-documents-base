---
collection: gitlab
version: "17.9.8"
title: "JSON injection"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/user/application_security/api_security_testing/checks/json_injection_check.md
fetched_at: 2025-05-07T10:05:15Z
---
## Description

Check for JSON serialization/injection vulnerabilities.

## Remediation

JSON injection is an attack technique used to manipulate or compromise the logic of a JSON application or service. The injection of unintended JSON content and/or structures into an JSON message can alter the intend logic of the application. Further, JSON injection can cause the insertion of malicious content into the resulting message/document.

## Links

- [OWASP](https://owasp.org/Top10/A03_2021-Injection/)
- [CWE](https://cwe.mitre.org/data/definitions/929.html)
