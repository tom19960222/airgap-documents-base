---
collection: gitlab
version: "17.9.8"
title: "Verifying Database Capabilities"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/development/database/verifying_database_capabilities.md
fetched_at: 2025-05-07T10:05:15Z
---
Sometimes certain bits of code may only work on a certain database
version. While we try to avoid such code as much as possible sometimes it is
necessary to add database (version) specific behavior.

To facilitate this we have the following methods that you can use:

- `ApplicationRecord.database.version`: returns the PostgreSQL version number as a string
  in the format `X.Y.Z`.

This allows you to write code such as:

```ruby
if ApplicationRecord.database.version.to_f >= 11.7
  run_really_fast_query
else
  run_fast_query
end
```

## Read-only database

The database can be used in read-only mode. In this case we have to
make sure all GET requests don't attempt any write operations to the
database. If one of those requests wants to write to the database, it needs
to be wrapped in a `Gitlab::Database.read_only?` or `Gitlab::Database.read_write?`
guard, to make sure it doesn't for read-only databases.

We have a Rails Middleware that filters any potentially writing
operations (the `CUD` operations of CRUD) and prevent the user from trying
to update the database and getting a 500 error (see `Gitlab::Middleware::ReadOnly`).
