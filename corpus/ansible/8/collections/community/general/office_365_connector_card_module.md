---
collection: ansible
version: "8"
title: "community.general.office_365_connector_card module – Use webhooks to create Connector Card messages within an Office 365 group"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/office_365_connector_card_module.html
fetched_at: 2026-07-28T01:48:17+00:00
---
# community.general.office_365_connector_card module – Use webhooks to create Connector Card messages within an Office 365 group

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
> To use it in a playbook, specify: `community.general.office_365_connector_card`.

- [Synopsis](office_365_connector_card_module.md#synopsis)
- [Parameters](office_365_connector_card_module.md#parameters)
- [Attributes](office_365_connector_card_module.md#attributes)
- [Notes](office_365_connector_card_module.md#notes)
- [Examples](office_365_connector_card_module.md#examples)

## [Synopsis](office_365_connector_card_module.md#id1)

- Creates Connector Card messages through Office 365 Connectors <https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-reference#connector-card-for-microsoft-365-groups>.

Aliases: notification.office_365_connector_card

## [Parameters](office_365_connector_card_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **actions**  list / elements=dictionary | This array of objects will power the action links  found at the bottom of the card. |
| **color**  string | Accent color used for branding or indicating status in the card. |
| **sections**  list / elements=dictionary | Contains a list of sections to display in the card.  For more information see <https://learn.microsoft.com/en-us/outlook/actionable-messages/message-card-reference#section-fields>. |
| **summary**  string | A string used for summarizing card content.  This will be shown as the message subject.  This is required if the text parameter isn’t populated. |
| **text**  string | The main text of the card.  This will be rendered below the sender information and optional title,  and above any sections or actions present. |
| **title**  string | A title for the Connector message. Shown at the top of the message. |
| **webhook**  string / required | The webhook URL is given to you when you create a new Connector. |

## [Attributes](office_365_connector_card_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](office_365_connector_card_module.md#id4)

> **Note:**
>
> - This module is not idempotent, therefore if the same task is run twice there will be two Connector Cards created

## [Examples](office_365_connector_card_module.md#id5)

```yaml+jinja
- name: Create a simple Connector Card
  community.general.office_365_connector_card:
    webhook: https://outlook.office.com/webhook/GUID/IncomingWebhook/GUID/GUID
    text: 'Hello, World!'

- name: Create a Connector Card with the full format
  community.general.office_365_connector_card:
    webhook: https://outlook.office.com/webhook/GUID/IncomingWebhook/GUID/GUID
    summary: This is the summary property
    title: This is the **card's title** property
    text: This is the **card's text** property. Lorem ipsum dolor sit amet, consectetur
      adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    color: E81123
    sections:
    - title: This is the **section's title** property
      activity_image: http://connectorsdemo.azurewebsites.net/images/MSC12_Oscar_002.jpg
      activity_title: This is the section's **activityTitle** property
      activity_subtitle: This is the section's **activitySubtitle** property
      activity_text: This is the section's **activityText** property.
      hero_image:
        image: http://connectorsdemo.azurewebsites.net/images/WIN12_Scene_01.jpg
        title: This is the image's alternate text
      text: This is the section's text property. Lorem ipsum dolor sit amet, consectetur
        adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
      facts:
      - name: This is a fact name
        value: This is a fact value
      - name: This is a fact name
        value: This is a fact value
      - name: This is a fact name
        value: This is a fact value
      images:
      - image: http://connectorsdemo.azurewebsites.net/images/MicrosoftSurface_024_Cafe_OH-06315_VS_R1c.jpg
        title: This is the image's alternate text
      - image: http://connectorsdemo.azurewebsites.net/images/WIN12_Scene_01.jpg
        title: This is the image's alternate text
      - image: http://connectorsdemo.azurewebsites.net/images/WIN12_Anthony_02.jpg
        title: This is the image's alternate text
      actions:
      - "@type": ActionCard
        name: Comment
        inputs:
        - "@type": TextInput
          id: comment
          is_multiline: true
          title: Input's title property
        actions:
        - "@type": HttpPOST
          name: Save
          target: http://...
      - "@type": ActionCard
        name: Due Date
        inputs:
        - "@type": DateInput
          id: dueDate
          title: Input's title property
        actions:
        - "@type": HttpPOST
          name: Save
          target: http://...
      - "@type": HttpPOST
        name: Action's name prop.
        target: http://...
      - "@type": OpenUri
        name: Action's name prop
        targets:
        - os: default
          uri: http://...
    - start_group: true
      title: This is the title of a **second section**
      text: This second section is visually separated from the first one by setting its
        **startGroup** property to true.
```

### Authors

- Marc Sensenich (@marc-sensenich)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
