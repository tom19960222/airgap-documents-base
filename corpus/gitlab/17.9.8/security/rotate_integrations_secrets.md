---
collection: gitlab
version: "17.9.8"
title: "Rotate secrets of third-party integrations"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/security/rotate_integrations_secrets.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab Self-Managed

Rotating secrets of third-party integrations is an important security practice
that helps mitigate the risks associated with leaked secrets, such as
unauthorized access and potential data breaches.

You should rotate the secrets of all third-party integrations at least yearly.
An incomplete list of such secrets:

- [FortiAuthenticator](../user/profile/account/two_factor_authentication.md#enable-a-one-time-password-authenticator-using-fortiauthenticator)
- [FortiToken Cloud](../user/profile/account/two_factor_authentication.md#enable-a-one-time-password-authenticator-using-fortitoken-cloud)
