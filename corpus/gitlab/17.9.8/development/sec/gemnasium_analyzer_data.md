---
collection: gitlab
version: "17.9.8"
title: "Gemnasium analyzer data"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/development/sec/gemnasium_analyzer_data.md
fetched_at: 2025-05-07T10:05:15Z
---
The following table lists the data available for the Gemnasium analyzer.

| Property \ Tool                               | Gemnasium |
|:----------------------------------------------|:---------:|
| Severity                                      | [icon: check-circle] Yes |
| Title                                         | [icon: check-circle] Yes |
| File                                          | [icon: check-circle] Yes |
| Start line                                    | [icon: dotted-circle] No |
| End line                                      | [icon: dotted-circle] No |
| External ID (for example, CVE)                | [icon: check-circle] Yes |
| URLs                                          | [icon: check-circle] Yes |
| Internal doc/explanation                      | [icon: check-circle] Yes |
| Solution                                      | [icon: check-circle] Yes |
| Confidence                                    | [icon: dotted-circle] No |
| Affected item (for example, class or package) | [icon: check-circle] Yes |
| Source code extract                           | [icon: dotted-circle] No |
| Internal ID                                   | [icon: check-circle] Yes |
| Date                                          | [icon: check-circle] Yes |
| Credits                                       | [icon: check-circle] Yes |

- [icon: check-circle] Yes => we have that data
- [icon: dotted-circle] No => we don't have that data, or it would need to develop specific or inefficient/unreliable logic to obtain it.

The values provided by these tools are heterogeneous, so they are sometimes normalized into common
values (for example, `severity`, `confidence`, etc).
