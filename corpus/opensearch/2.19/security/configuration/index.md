---
collection: "opensearch"
version: "2.19"
title: "Configuration"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_security/configuration/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_security/configuration/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/security/configuration/"
canonical_url: "https://docs.opensearch.org/latest/security/configuration/index/"
canonical_route: "/security/configuration/"
redirect_from: ["/security-plugin/configuration/","/security/configuration/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: true
layout: "default"
nav_order: 2
---
# Security configuration

The Security plugin includes demo certificates so that you can get up and running quickly. To use OpenSearch with the Security plugin in a production environment, you must make changes to the demo certificates and other configuration options manually.

## Replace the demo certificates

OpenSearch ships with demo certificates intended for quick setup and demonstration purposes. For a production environment, it's critical to replace these with your own trusted certificates, using the following steps, to ensure secure communication:

1. **Generate your own certificates:** Use tools like OpenSSL or a certificate authority (CA) to generate your own certificates. For more information about generating certificates with OpenSSL, see [Generating self-signed certificates](generate-certificates/index.md).
2. **Store the generated certificates and private key in the appropriate directory:** Generated certificates are typically stored in `<OPENSEARCH_HOME>/config/`. For more information, see [Add certificate files to opensearch.yml](generate-certificates/index.md#add-certificate-files-to-opensearchyml).
3. **Set the following file permissions:**
    - Private key (.key files): Set the file mode to `600`. This restricts access so that only the file owner (the OpenSearch user) can read and write to the file, ensuring that the private key remains secure and inaccessible to unauthorized users.
    - Public certificates (.crt, .pem files): Set the file mode to `644`. This allows the file owner to read and write to the file, while other users can only read it.

For additional guidance on file modes, see the following table.

        | Item        | Sample              | Numeric | Bitwise      |
        |-------------|---------------------|---------|--------------|
        | Public key  | `~/.ssh/id_rsa.pub` | `644`   | `-rw-r--r--` |
        | Private key | `~/.ssh/id_rsa`     | `600`   | `-rw-------` |
        | SSH folder  | `~/.ssh`            | `700`   | `drwx------` |

For more information, see [Configuring basic security settings](../../install-and-configure/install-opensearch/docker/index.md#configuring-basic-security-settings).

## Reconfigure `opensearch.yml` to use your certificates

The `opensearch.yml` file is the main configuration file for OpenSearch; you can find the file at `<OPENSEARCH_HOME>/config/opensearch.yml`. Use the following steps to update this file to point to your custom certificates:

In `opensearch.yml`, set the correct paths for your certificates and keys, as shown in the following example:
   ```
   plugins.security.ssl.transport.pemcert_filepath: /path/to/your/cert.pem
   plugins.security.ssl.transport.pemkey_filepath: /path/to/your/key.pem
   plugins.security.ssl.transport.pemtrustedcas_filepath: /path/to/your/ca.pem
   plugins.security.ssl.http.enabled: true
   plugins.security.ssl.http.pemcert_filepath: /path/to/your/cert.pem
   plugins.security.ssl.http.pemkey_filepath: /path/to/your/key.pem
   plugins.security.ssl.http.pemtrustedcas_filepath: /path/to/your/ca.pem
   ```
For more information, see [Configuring TLS certificates](tls/index.md).

## Reconfigure `config.yml` to use your authentication backend

The `config.yml` file allows you to configure the authentication and authorization mechanisms for OpenSearch. Update the authentication backend settings in `<OPENSEARCH_HOME>/config/opensearch-security/config.yml` according to your requirements.

For example, to use the internal authentication backend, add the following settings:

  ```
    authc:
      basic_internal_auth:
        http_enabled: true
        transport_enabled: true
        order: 1
        http_authenticator:
          type: basic
          challenge: true
        authentication_backend:
          type: internal
   ```
For more information, see [Configuring the Security backend](configuration/index.md).

## Modify the configuration YAML files

Determine whether any additional YAML files need modification, for example, the `roles.yml`, `roles_mapping.yml`, or `internal_users.yml` files. Update the files with any additional configuration information. For more information, see [Modifying the YAML files](yaml/index.md).

## Set a password policy

When using the internal user database, we recommend enforcing a password policy to ensure that strong passwords are used. For information about strong password policies, see [Password settings](yaml/index.md#password-settings).

## Apply changes using the `securityadmin` script

The following steps do not apply to first-time users because the security index is automatically initialized from the YAML configuration files when OpenSearch starts.
{: .note}

After initial setup, if you make changes to your security configuration or disable automatic initialization by setting `plugins.security.allow_default_init_securityindex` to `false` (which prevents security index initialization from `yaml` files), you need to manually apply changes using the `securityadmin` script:

1. Find the `securityadmin` script. The script is typically stored in the OpenSearch plugins directory, `plugins/opensearch-security/tools/securityadmin.[sh|bat]`.
   - Note: If you're using OpenSearch 1.x, the `securityadmin` script is located in the `plugins/opendistro_security/tools/` directory.
   - For more information, see [Basic usage](security-admin/index.md#basic-usage).
2. Run the script by using the following command:
   ```
    ./plugins/opensearch-security/tools/securityadmin.[sh|bat]
   ```
3. Check the OpenSearch logs and configuration to ensure that the changes have been successfully applied.

For more information about using the `securityadmin` script, see [Applying changes to configuration files](security-admin/index.md).

## Add users, roles, role mappings, and tenants

If you don't want to use the Security plugin, you can disable it by adding the following setting to the `opensearch.yml` file:

```
plugins.security.disabled: true
```

You can then enable the plugin by removing the `plugins.security.disabled` setting.

For more information about disabling the Security plugin, see [Disable security](disable-enable-security/index.md).

The Security plugin has several default users, roles, action groups, permissions, and settings for OpenSearch Dashboards that contain "Kibana" in their names. We will change these names in a future version.
{: .note }

For a full list of `opensearch.yml` Security plugin settings, see [Security settings](../../install-and-configure/configuring-opensearch/security-settings/index.md).
{: .note}
