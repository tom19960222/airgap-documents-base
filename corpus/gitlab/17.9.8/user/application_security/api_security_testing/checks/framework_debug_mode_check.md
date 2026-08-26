---
collection: gitlab
version: "17.9.8"
title: "Framework debug mode"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/user/application_security/api_security_testing/checks/framework_debug_mode_check.md
fetched_at: 2025-05-07T10:05:15Z
---
## Description

Checks to see if debug mode is enabled in various frameworks such as Flask and ASP.NET. This check has a low false positive rate.

## Remediation

The Flask or ASP .NET framework was identified with debug mode enabled. This allows an attacker the ability to download any file on the file system and other capabilities. This is a high severity issue that is easy for an attacker to exploit.

## Links

- [OWASP](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)
- [CWE-23: Relative Path Traversal](https://cwe.mitre.org/data/definitions/23.html)
- [CWE-285: Improper Authorization](https://cwe.mitre.org/data/definitions/285.html)
