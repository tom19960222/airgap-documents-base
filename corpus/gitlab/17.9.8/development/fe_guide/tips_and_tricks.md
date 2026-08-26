---
collection: gitlab
version: "17.9.8"
title: "Tips and tricks"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/development/fe_guide/tips_and_tricks.md
fetched_at: 2025-05-07T10:05:15Z
---
## Code deletion checklist

When your merge request deletes code, it's important to also delete all
related code that is no longer used.
When deleting Haml and Vue code, check whether it contains the following types of
code that is unused:

- CSS.

  For example, we've deleted a Vue component that contained the `.mr-card` class, which is now unused.
  The `.mr-card` CSS rule set should then be deleted from `merge_requests.scss`.

- Ruby variables.

  Deleting unused Ruby variables is important so we don't continue instantiating them with
  potentially expensive code.

  For example, we've deleted a Haml template that used the `@total_count` Ruby variable.
  The `@total_count` variable was no longer used in the remaining templates for the page.
  The instantiation of `@total_count` in `issues_controller.rb` should then be deleted so that we
  don't make unnecessary database calls to calculate the count of issues.

- Ruby methods.
