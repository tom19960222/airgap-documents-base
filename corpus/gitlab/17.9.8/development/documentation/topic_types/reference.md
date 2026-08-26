---
collection: gitlab
version: "17.9.8"
title: "Reference topic type"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/development/documentation/topic_types/reference.md
fetched_at: 2025-05-07T10:05:15Z
---
Reference information should be in an easily-scannable format,
like a table or list. It's similar to a dictionary or encyclopedia entry.

## Format

Reference topics should be in this format:

```markdown
title: Title (a noun, like "Pipeline settings" or "Administrator options")
---

Introductory sentence.

| Setting | Description |
|---------|-------------|
| **Name** | Descriptive sentence about the setting. |
```

## Reference topic titles

Reference topic titles are usually nouns.

Avoid these topic titles:

- `Important notes`. Instead, incorporate this information
  closer to where it belongs. For example, this information might be a prerequisite
  for a task, or information about a concept.
- `Limitations`. Instead, move the content near other similar information.
  If you must, you can use the title `Known issues`.
