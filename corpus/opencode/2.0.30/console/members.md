---
collection: opencode
version: "2.0.30"
title: "Members"
source_url: https://github.com/anomalyco/opencode/blob/f16ef9ad8878279ea2be3cfab7baeed97aef61aa/services/www/src/docs/content/console/members.mdx
fetched_at: 2026-10-15T19:48:22Z
description: "Invite people to an OpenCode Console workspace, manage their roles, and remove them."
---
Owners and admins manage people from the **Members** page. Each row shows the member's role, join date, monthly
usage, and budget limit.

## Invite members

1. Open **Members** and click **Invite Members**.
2. Add one or more email addresses. Separate them with spaces, commas, or semicolons, or paste a list.
3. Click **Send invitations**.

Each person receives an email titled **Join Acme Inc. on OpenCode** with a **Join workspace** button.

Invitations expire after 7 days. Everyone joins as **Member**; [change their role](#change-a-role) after they join.

**Note:**

  Workspaces with an [OpenCode Go](go.md) subscription cannot invite members. Create a separate workspace for your
  team.

Members can also join automatically:

- [SSO](sso.md#automatic-membership) adds people on your verified email domains when they first sign in.
- [Directory sync](scim.md) adds and removes people as you assign them in your identity provider.

## Accept an invitation

The invitee must sign in with the email address the invitation was sent to. There are two ways to accept:

- Click **Join workspace** in the invitation email, then sign in or create an account.
- Sign in to the Console, open the workspace menu, and click **Join** under **Pending invitations**.

If they are signed in with a different account, Console asks them to **Sign out and continue** with the invited email.

## Manage pending invitations

Pending invitations appear in the Members table as **Pending · Expires** followed by the date, or **Expired**.

| Action | How                                                                                       |
| ------ | ----------------------------------------------------------------------------------------- |
| Resend | **⋯ › Resend invitation**. Sends a new link valid for 7 days; the old link stops working. |
| Revoke | **⋯ › Remove...**. The link stops working immediately.                                    |

## Change a role

Open the role menu in a member's row and pick **Member**, **Admin**, or **Owner**.

You can only grant roles up to your own, and the workspace always keeps at least one owner. See
[Roles](workspaces.md#roles).

## Remove a member

1. Click **⋯ › Remove...** in the member's row.
2. Confirm with **Remove member**.

Access is revoked immediately, and you can invite them again later. Their past usage stays in the workspace's reports.

Service accounts and their API keys belong to the workspace, so removing the member who created them does not revoke
them. Revoke keys from **Keys** if needed. See [Service accounts](api/index.md#service-accounts).

## Member details

Click a member to see their monthly budget, models and clients they use, usage charts, and request logs. From here
you can set their [budget](budgets.md#member-budgets) and export their usage as CSV.
