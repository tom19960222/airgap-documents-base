---
collection: gitlab
version: "17.9.8"
title: "Mass inserting Rails models"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/development/mass_insert.md
fetched_at: 2025-05-07T10:05:15Z
---
Setting the environment variable [`MASS_INSERT=1`](rake_tasks.md#environment-variables)
when running [`rake setup`](rake_tasks.md) creates millions of records, but these records
aren't visible to the `root` user by default.

To make any number of the mass-inserted projects visible to the `root` user, run
the following snippet in the rails console.

```ruby
u = User.find(1)
Project.last(100).each { |p| p.send(:set_timestamps_for_create) && p.add_maintainer(u, current_user: u) } # Change 100 to whatever number of projects you need access to
```
