---
collection: ansible
version: "8"
title: "community.general.twilio module – Sends a text message to a mobile phone through Twilio"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/twilio_module.html
fetched_at: 2026-07-28T01:50:59+00:00
---
# community.general.twilio module – Sends a text message to a mobile phone through Twilio

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.twilio`.

- [Synopsis](twilio_module.md#synopsis)
- [Parameters](twilio_module.md#parameters)
- [Attributes](twilio_module.md#attributes)
- [Notes](twilio_module.md#notes)
- [Examples](twilio_module.md#examples)

## [Synopsis](twilio_module.md#id1)

- Sends a text message to a phone number through the Twilio messaging API.

Aliases: notification.twilio

## [Parameters](twilio_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **account_sid**  string / required | User’s Twilio account token found on the account page. |
| **auth_token**  string / required | User’s Twilio authentication token. |
| **from_number**  string / required | The Twilio number to send the text message from, format `+15551112222`. |
| **media_url**  string | A URL with a picture, video or sound clip to send with an MMS (multimedia message) instead of a plain SMS. |
| **msg**  string / required | The body of the text message. |
| **to_numbers**  aliases: to_number  list / elements=string / required | One or more phone numbers to send the text message to, format `+15551112222`. |

## [Attributes](twilio_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](twilio_module.md#id4)

> **Note:**
>
> - This module is non-idempotent because it sends an email through the external API. It is idempotent only in the case that the module fails.
> - Like the other notification modules, this one requires an external dependency to work. In this case, you’ll need a Twilio account with a purchased or verified phone number to send the text message.

## [Examples](twilio_module.md#id5)

```yaml+jinja
# send an SMS about the build status to (555) 303 5681
# note: replace account_sid and auth_token values with your credentials
# and you have to have the 'from_number' on your Twilio account
- name: Send a text message to a mobile phone through Twilio
  community.general.twilio:
    msg: All servers with webserver role are now configured.
    account_sid: ACXXXXXXXXXXXXXXXXX
    auth_token: ACXXXXXXXXXXXXXXXXX
    from_number: +15552014545
    to_number: +15553035681
  delegate_to: localhost

# send an SMS to multiple phone numbers about the deployment
# note: replace account_sid and auth_token values with your credentials
# and you have to have the 'from_number' on your Twilio account
- name: Send a text message to a mobile phone through Twilio
  community.general.twilio:
    msg: This server configuration is now complete.
    account_sid: ACXXXXXXXXXXXXXXXXX
    auth_token: ACXXXXXXXXXXXXXXXXX
    from_number: +15553258899
    to_numbers:
      - +15551113232
      - +12025551235
      - +19735559010
  delegate_to: localhost

# send an MMS to a single recipient with an update on the deployment
# and an image of the results
# note: replace account_sid and auth_token values with your credentials
# and you have to have the 'from_number' on your Twilio account
- name: Send a text message to a mobile phone through Twilio
  community.general.twilio:
    msg: Deployment complete!
    account_sid: ACXXXXXXXXXXXXXXXXX
    auth_token: ACXXXXXXXXXXXXXXXXX
    from_number: +15552014545
    to_number: +15553035681
    media_url: https://demo.twilio.com/logo.png
  delegate_to: localhost
```

### Authors

- Matt Makai (@makaimc)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
