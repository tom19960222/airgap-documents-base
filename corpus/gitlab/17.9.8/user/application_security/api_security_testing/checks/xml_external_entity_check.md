---
collection: gitlab
version: "17.9.8"
title: "XML external entity"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/user/application_security/api_security_testing/checks/xml_external_entity_check.md
fetched_at: 2025-05-07T10:05:15Z
---
## Description

Check for XML DTD processing vulnerabilities.

## Remediation

XML external entity Attack is a type of attack against an application that parses XML input. This attack occurs when XML input containing a reference to an external entity is processed by a weakly configured XML parser. This attack may lead to the disclosure of confidential data, denial of service, server side request forgery, port scanning from the perspective of the machine where the parser is located, and other system impacts.

## Links

- [OWASP](https://owasp.org/Top10/A03_2021-Injection/)
- [CWE](https://cwe.mitre.org/data/definitions/611.html)
