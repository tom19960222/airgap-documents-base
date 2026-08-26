---
collection: gitlab
version: "17.9.8"
title: "Overriding API Fuzzing jobs"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/user/application_security/api_fuzzing/configuration/overriding_analyzer_jobs.md
fetched_at: 2025-05-07T10:05:15Z
---
To override a job definition, (for example, change properties like `variables`, `dependencies`, or [`rules`](../../../../ci/yaml/_index.md#rules)),
declare a job with the same name as the DAST job to override. Place this new job after the template
inclusion and specify any additional keys under it. For example, this sets the target APIs base URL:

```yaml
include:
  - template: Security/API-Fuzzing.gitlab-ci.yml

apifuzzing_fuzz:
  variables:
    FUZZAPI_TARGET_URL: https://target/api
```
