---
collection: gitlab
version: "17.9.8"
title: "Custom password length limits"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/security/password_length_limits.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab Self-Managed, GitLab Dedicated

By default, GitLab supports passwords with the following lengths:

- Minimum: 8 characters
- Maximum: 128 characters

You can only change the minimum password length. Changing the minimum length does not affect existing user passwords.
Existing users are not asked to reset their password to adhere to the new limits. The new limit restriction applies only
during new user sign-ups and when an existing user performs a password reset.

## Modify minimum password length

The user password length is set to a minimum of 8 characters by default.

To change the minimum password length using GitLab UI:

1. On the left sidebar, at the bottom, select **Admin**.
1. Select **Settings > General**.
1. Expand **Sign-up restrictions**.
1. Enter a **Minimum password length** value greater than or equal to `8`.
1. Select **Save changes**.

<!-- ## Troubleshooting

Include any troubleshooting steps that you can foresee. If you know beforehand what issues
one might have when setting this up, or when something is changed, or on upgrading, it's
important to describe those, too. Think of things that may go wrong and include them here.
This is important to minimize requests for support, and to avoid doc comments with
questions that you know someone might ask.

Each scenario can be a third-level heading, for example `### Getting error message X`.
If you have none to add when creating a doc, leave this section in place
but commented out to help encourage others to add to it in the future. -->
