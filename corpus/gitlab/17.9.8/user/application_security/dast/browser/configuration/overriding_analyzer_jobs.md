---
collection: gitlab
version: "17.9.8"
title: "Overriding DAST jobs"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/user/application_security/dast/browser/configuration/overriding_analyzer_jobs.md
fetched_at: 2025-05-07T10:05:15Z
---
To override a job definition, (for example, change properties like `variables`, `dependencies`, or [`rules`](../../../../../ci/yaml/_index.md#rules)),
declare a job with the same name as the DAST job to override. Place this new job after the template
inclusion and specify any additional keys under it. For example, this enables authentication debug logging for the analyzer:

```yaml
include:
  - template: Security/DAST.gitlab-ci.yml

dast:
  variables:
    DAST_LOG_CONFIG: auth:debug
```
