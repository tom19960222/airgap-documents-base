---
collection: gitlab
version: "17.9.8"
title: "Troubleshooting workspaces"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/user/workspace/workspaces_troubleshooting.md
fetched_at: 2025-05-07T10:05:15Z
---
When working with GitLab workspaces, you might encounter the following issues.

## Error: `Failed to renew lease`

When creating a workspace, you might encounter the following error message in the agent's log:

```plaintext
{"level":"info","time":"2023-01-01T00:00:00.000Z","msg":"failed to renew lease gitlab-agent-remote-dev-dev/agent-123XX-lock: timed out waiting for the condition\n","agent_id":XXXX}
```

The error is because of a known issue in the GitLab agent for Kubernetes.
This error occurs when an agent instance cannot renew its leadership lease, causing leader-only modules like `remote_development` to shut down.

To resolve this issue:

1. Restart the agent instance.
1. If the issue persists, check your Kubernetes cluster's health and connectivity.

## Error: `No agents available to create workspaces`

When you create a workspace in a project, you might get the following error:

```plaintext
No agents available to create workspaces. Please consult Workspaces documentation for troubleshooting.
```

To resolve this issue:

1. Check agent configuration:

   - Verify the `remote_development` module is enabled in your agent configuration:

     ```yaml
     remote_development:
       enabled: true
     ```

     - If the `remote_development` module is disabled for the GitLab agent,
     set [`enabled`](settings.md#enabled) to `true`.

1. Check permissions:

   - Ensure you have at least the Developer role for both the workspace project and agent project.
     - If you do not have at least the Developer role for the workspace and agent projects, contact your administrator.
   - Verify the agent is allowed in an ancestor group of your workspace project.
     - If the ancestor groups of the project do not have an allowed agent,
    [allow an agent](gitlab_agent_configuration.md#allow-a-cluster-agent-for-workspaces-in-a-group)
    for any of these groups.

1. Check agent logs:

   ```shell
   kubectl logs -f -l app=gitlab-agent -n gitlab-workspaces
   ```

<!--- Other suggested topics:

## DNS configuration

## Workspace stops unexpectedly

## Workspace creation fails due to quotas

## Network connectivity

## SSH connection failures

### Network policy restrictions

-->
