---
collection: ansible
version: "8"
title: "amazon.aws.aws_collection_constants lookup – expose various collection related constants"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/aws_collection_constants_lookup.html
fetched_at: 2026-07-28T01:07:19+00:00
---
# amazon.aws.aws_collection_constants lookup – expose various collection related constants

> **Note:**
>
> This lookup plugin is part of the [amazon.aws collection](https://galaxy.ansible.com/ui/repo/published/amazon/aws/) (version 6.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install amazon.aws`.
>
> To use it in a playbook, specify: `amazon.aws.aws_collection_constants`.

New in amazon.aws 6.0.0

- [Synopsis](aws_collection_constants_lookup.md#synopsis)
- [Terms](aws_collection_constants_lookup.md#terms)
- [Examples](aws_collection_constants_lookup.md#examples)
- [Return Value](aws_collection_constants_lookup.md#return-value)

## [Synopsis](aws_collection_constants_lookup.md#id1)

- Exposes various collection related constants for use in integration tests.

## [Terms](aws_collection_constants_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | Name of the constant.  **Choices:**   - `"MINIMUM_BOTOCORE_VERSION"` - `"MINIMUM_BOTO3_VERSION"` - `"HAS_BOTO3"` - `"AMAZON_AWS_COLLECTION_VERSION"` - `"AMAZON_AWS_COLLECTION_NAME"` - `"COMMUNITY_AWS_COLLECTION_VERSION"` - `"COMMUNITY_AWS_COLLECTION_NAME"` |

## [Examples](aws_collection_constants_lookup.md#id3)

```yaml+jinja

```

## [Return Value](aws_collection_constants_lookup.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  string | value  **Returned:** success |

### Authors

- Mark Chappell (@tremble)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
