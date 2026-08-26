---
collection: gitlab
version: "17.9.8"
title: "Maintenance operations"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/development/database/maintenance_operations.md
fetched_at: 2025-05-07T10:05:15Z
---
This page details various database related operations that may relate to development.

## Disabling an index is not safe

> **Warning:**
>
> Previously, this section described a procedure to mark the index as invalid before removing it.
> It's no longer recommended, as [it is not safe](https://gitlab.com/groups/gitlab-org/-/epics/11543#note_1570734906).

There are certain situations in which you might want to disable an index before removing it:

- The index is on a large table and rebuilding it in the case of a revert would take a long time.
- It is uncertain whether or not the index is being used in ways that are not fully visible.

In such situations, the index was disabled in a coordinated manner with
the infrastructure team and the database team
by opening a [production infrastructure issue](https://gitlab.com/gitlab-com/gl-infra/production/-/issues/new)
with the "Production Change" template and
then running the following commands:

```sql
-- Disable the index then run an EXPLAIN command known to use the index:
UPDATE pg_index SET indisvalid = false WHERE indexrelid = 'index_issues_on_foo'::regclass;
-- Verify the index is invalid on replicas:
SELECT indisvalid FROM pg_index WHERE indexrelid = 'index_issues_on_foo'::regclass;

-- Rollback the invalidation:
UPDATE pg_index SET indisvalid = true WHERE indexrelid = 'index_issues_on_foo'::regclass;
```

See this [example infrastructure issue](https://gitlab.com/gitlab-com/gl-infra/production/-/issues/2795) for reference.
