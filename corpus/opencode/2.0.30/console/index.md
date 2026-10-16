---
collection: opencode
version: "2.0.30"
title: "Intro"
source_url: https://github.com/anomalyco/opencode/blob/f16ef9ad8878279ea2be3cfab7baeed97aef61aa/services/www/src/docs/content/console/index.mdx
fetched_at: 2026-10-15T19:48:22Z
---
The [OpenCode Console](https://opencode.ai/console) is an optional service that provides additional benefits to
using OpenCode, on your own or as a team.

- [Workspaces](workspaces.md) for sharing access with your [team](members.md)
- [Inference](models.md) for both proprietary and open source models
- [Providers](providers.md) for connecting your own provider accounts through the Console gateway
- Usage tracking and [budget](budgets.md) controls
- Deploy team wide policies to control OpenCode behavior
- [Web search](websearch.md)
- [OpenCode Go and Go Plus](go.md), $10 and $40 monthly subscriptions for open source model access

## Get started

You don't need a team to use the Console. Every account starts with a **Personal** workspace where you are the only
member.

1. Sign in to the [Console](https://opencode.ai/console).
2. Subscribe to [Go](go.md), add [credits](billing.md#add-credits), or connect a [provider](providers.md).
3. Run `/connect` in OpenCode and choose the workspace.
4. Optionally, [invite](members.md#invite-members) your team.

```text
/connect
```

## Policies

Providers and Tools rules from the Policies page apply to every OpenCode V2 client
connected to the workspace. They are delivered as [policy](../policies.md#console)
statements with final authority over the member's own configuration and take effect
within about a minute.
