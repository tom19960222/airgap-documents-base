---
collection: gitlab
version: "17.9.8"
title: "GitLab Language Server"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/editor_extensions/language_server/_index.md
fetched_at: 2025-05-07T10:05:15Z
---
The [GitLab Language Server](https://gitlab.com/gitlab-org/editor-extensions/gitlab-lsp)
powers various GitLab editor extensions across IDEs.

## Configure the Language Server to use a proxy

The `gitlab-lsp` child process uses the [`proxy-from-env`](https://www.npmjs.com/package/proxy-from-env?activeTab=readme)
NPM module to determine proxy settings from these environment variables:

- `NO_PROXY`
- `HTTPS_PROXY`
- `http_proxy` (in lower case)

To configure the Language Server to use a proxy:

**Tab: Visual Studio Code**

1. In Visual Studio Code, open your [user or workspace settings](https://code.visualstudio.com/docs/getstarted/settings).
1. Configure [`http.proxy`](https://code.visualstudio.com/docs/setup/network#_legacy-proxy-server-support)
   to point at your HTTP proxy.
1. Restart Visual Studio Code to ensure connections to GitLab use the latest proxy settings.

**Tab: JetBrains IDEs**

1. In your JetBrains IDE, configure the [HTTP Proxy](https://www.jetbrains.com/help/idea/settings-http-proxy.html) settings.
1. Restart your IDE to ensure connections to GitLab use the latest proxy settings.
1. From the **Tools > GitLab Duo** menu, select **Verify setup**. Make sure the health check passes.

## Troubleshooting

### Enable proxy authentication

You might encounter a `407 Access Denied (authentication_failed)` error when using an authenticated proxy:

```plaintext
Request failed: Can't add GitLab account for https://gitlab.com. Check your instance URL and network connection.
Fetching resource from https://gitlab.com/api/v4/personal_access_tokens/self failed
```

To enable proxy authentication in the Language Server, follow the steps for your IDE:

**Tab: Visual Studio Code**

1. Open your user or workspace [settings](https://code.visualstudio.com/docs/getstarted/settings).
1. Configure [`http.proxy`](https://code.visualstudio.com/docs/setup/network#_legacy-proxy-server-support),
   including username and password, to authenticate with your HTTP proxy.
1. Restart Visual Studio Code to ensure connections to GitLab use the latest proxy settings.

> **Note:**
>
> The VS Code extension does not support the legacy
> [`http.proxyAuthorization`](https://code.visualstudio.com/docs/setup/network#_legacy-proxy-server-support)
> setting in VS Code for authenticating the language server with an HTTP proxy. Support is proposed in
> [issue 1672](https://gitlab.com/gitlab-org/gitlab-vscode-extension/-/issues/1672).

**Tab: JetBrains IDEs**

1. Configure [HTTP Proxy](https://www.jetbrains.com/help/idea/settings-http-proxy.html) settings in your JetBrains IDE.
   1. If using **Manual proxy configuration**, enter your credentials under **Proxy authentication** and select **Remember**.
1. Restart your JetBrains IDE to ensure connections to GitLab use the latest proxy settings.
1. From the **Tools > GitLab Duo** menu, select **Verify setup**. Make sure the health check passes.

> **Note:**
>
> Bearer authentication is proposed in [issue 548](https://gitlab.com/gitlab-org/editor-extensions/gitlab-lsp/-/issues/548).
