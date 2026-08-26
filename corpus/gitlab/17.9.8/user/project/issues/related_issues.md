---
collection: gitlab
version: "17.9.8"
title: "Linked issues"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/user/project/issues/related_issues.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated

**History:**

- [Changed](https://gitlab.com/groups/gitlab-org/-/epics/10267) minimum required role from Reporter (if true) to Guest in GitLab 17.0.

Linked issues are a bi-directional relationship between any two issues and appear in a block below
the issue description. You can link issues in different projects.

The relationship only shows up in the UI if the user can see both issues. When you try to close an
issue that has open blockers, a warning is displayed.

> **Note:**
>
> To manage linked issues through our API, see [Issue links API](../../../api/issue_links.md).

## Add a linked issue

Prerequisites:

- You must have at least the Guest role for both projects.

To link one issue to another:

1. In the **Linked items** section of an issue,
   select the add linked issue button ([icon: plus]).
1. Select the relationship between the two issues. Either:
   - **relates to**
   - **[blocks](#blocking-issues)**
   - **[is blocked by](#blocking-issues)**
1. Input the issue number or paste in the full URL of the issue.

   ![Adding a related issue](img/related_issues_add_v15_3.png)

   Issues of the same project can be specified just by the reference number.
   Issues from a different project require additional information like the
   group and the project name. For example:

   - The same project: `#44`
   - The same group: `project#44`
   - Different group: `group/project#44`

   Valid references are added to a temporary list that you can review.

1. When you have added all the linked issues, select **Add**.

When you have finished adding all linked issues, you can see
them categorized so their relationships can be better understood visually.

![Related issue block](img/related_issue_block_v15_3.png)

You can also add a linked issue from a commit message or the description in another issue or MR.
For more information, see [Crosslinking issues](crosslinking_issues.md).

## Remove a linked issue

In the **Linked items** section of an issue, select the remove button ([icon: close]) on the
right-side of each issue token to remove.

Due to the bi-directional relationship, the relationship no longer appears in either issue.

![Removing a related issue](img/related_issues_remove_v15_3.png)

Access our [permissions](../../permissions.md) page for more information.

## Blocking issues

- Tier: Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated

When you [add a linked issue](#add-a-linked-issue), you can show that it **blocks** or
**is blocked by** another issue.

Issues blocked by other issues have an icon ([icon: entity-blocked]) next to their title, shown in the
issue lists and [boards](../issue_board.md).
The icon disappears when the blocking issue is closed or their relationship is changed or
[removed](#remove-a-linked-issue).

If you try to close a blocked issue using the "Close issue" button, a confirmation message appears.
