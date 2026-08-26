---
collection: gitlab
version: "17.9.8"
title: "Group Activity Analytics API"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/api/group_activity_analytics.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated

## Get count of recently created issues for group

```plaintext
GET /analytics/group_activity/issues_count
```

Parameters:

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `group_path` | string | yes | Group path |

Example request:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/analytics/group_activity/issues_count?group_path=gitlab-org"
```

Example response:

```json
{ "issues_count": 10 }
```

## Get count of recently created merge requests for group

```plaintext
GET /analytics/group_activity/merge_requests_count
```

Parameters:

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `group_path` | string | yes | Group path |

Example request:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/analytics/group_activity/merge_requests_count?group_path=gitlab-org"
```

Example response:

```json
{ "merge_requests_count": 10 }
```

## Get count of members recently added to group

```plaintext
GET /analytics/group_activity/new_members_count
```

Parameters:

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `group_path` | string | yes | Group path |

Example request:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/analytics/group_activity/new_members_count?group_path=gitlab-org"
```

Example response:

```json
{ "new_members_count": 10 }
```
