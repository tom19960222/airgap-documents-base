---
collection: gitlab
version: "17.9.8"
title: "Generated passwords for users created through integrated authentication"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/security/passwords_for_integrated_authentication_methods.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated

GitLab allows users to set up accounts through integration with external [authentication and authorization providers](../administration/auth/_index.md).

These authentication methods do not require the user to explicitly create a password for their accounts.
However, to maintain data consistency, GitLab requires passwords for all user accounts.

For such accounts, we use the [`friendly_token`](https://github.com/heartcombo/devise/blob/f26e05c20079c9acded3c0ee16da0df435a28997/lib/devise.rb#L492) method provided by the Devise gem to generate a random, unique and secure password and sets it as the account password during sign up.

The length of the generated password is [128 characters](password_length_limits.md).
