---
collection: ansible
version: "6"
title: "ansible.builtin.psrp connection – Run tasks over Microsoft PowerShell Remoting Protocol"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/psrp_connection.html
fetched_at: 2026-07-27T16:44:16+00:00
---
# ansible.builtin.psrp connection – Run tasks over Microsoft PowerShell Remoting Protocol

> **Note:**
>
> This connection plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `psrp` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same connection plugin name.

New in Ansible 2.7

- [Synopsis](psrp_connection.md#synopsis)
- [Requirements](psrp_connection.md#requirements)
- [Parameters](psrp_connection.md#parameters)

## [Synopsis](psrp_connection.md#id1)

- Run commands or put/fetch on a target via PSRP (WinRM plugin)
- This is similar to the *winrm* connection plugin which uses the same underlying transport but instead runs in a PowerShell interpreter.

## [Requirements](psrp_connection.md#id2)

The below requirements are needed on the local controller node that executes this connection.

- pypsrp>=0.4.0 (Python library)

## [Parameters](psrp_connection.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth**  string | The authentication protocol to use when authenticating the remote user.  The default, `negotiate`, will attempt to use `Kerberos` if it is available and fall back to `NTLM` if it isn’t.  Choices:   - `"basic"` - `"certificate"` - `"negotiate"` ← (default) - `"kerberos"` - `"ntlm"` - `"credssp"`   Configuration:   - Variable: ansible_psrp_auth |
| **ca_cert**  aliases: cert_trust_path  path | The path to a PEM certificate chain to use when validating the server’s certificate.  This value is ignored if *cert_validation* is set to `ignore`.  Configuration:   - Variable: ansible_psrp_cert_trust_path - Variable: ansible_psrp_ca_cert |
| **cert_validation**  string | Whether to validate the remote server’s certificate or not.  Set to `ignore` to not validate any certificates.  *ca_cert* can be set to the path of a PEM certificate chain to use in the validation.  Choices:   - `"validate"` ← (default) - `"ignore"`   Configuration:   - Variable: ansible_psrp_cert_validation |
| **certificate_key_pem**  path | The local path to an X509 certificate key to use with certificate auth.  Configuration:   - Variable: ansible_psrp_certificate_key_pem |
| **certificate_pem**  path | The local path to an X509 certificate to use with certificate auth.  Configuration:   - Variable: ansible_psrp_certificate_pem |
| **configuration_name**  string | The name of the PowerShell configuration endpoint to connect to.  Default: `"Microsoft.PowerShell"`  Configuration:   - Variable: ansible_psrp_configuration_name |
| **connection_timeout**  integer | The connection timeout for making the request to the remote host.  This is measured in seconds.  Default: `30`  Configuration:   - Variable: ansible_psrp_connection_timeout |
| **credssp_auth_mechanism**  string | The sub authentication mechanism to use with CredSSP auth.  When `auto`, both Kerberos and NTLM is attempted with kerberos being preferred.  Choices:   - `"auto"` ← (default) - `"kerberos"` - `"ntlm"`   Configuration:   - Variable: ansible_psrp_credssp_auth_mechanism |
| **credssp_disable_tlsv1_2**  boolean | Disables the use of TLSv1.2 on the CredSSP authentication channel.  This should not be set to `yes` unless dealing with a host that does not have TLSv1.2.  Choices:   - `false` ← (default) - `true`   Configuration:   - Variable: ansible_psrp_credssp_disable_tlsv1_2 |
| **credssp_minimum_version**  integer | The minimum CredSSP server authentication version that will be accepted.  Set to `5` to ensure the server has been patched and is not vulnerable to CVE 2018-0886.  Default: `2`  Configuration:   - Variable: ansible_psrp_credssp_minimum_version |
| **ignore_proxy**  boolean | Will disable any environment proxy settings and connect directly to the remote host.  This option is ignored if `proxy` is set.  Choices:   - `false` ← (default) - `true`   Configuration:   - Variable: ansible_psrp_ignore_proxy |
| **max_envelope_size**  integer | Sets the maximum size of each WSMan message sent to the remote host.  This is measured in bytes.  Defaults to `150KiB` for compatibility with older hosts.  Default: `153600`  Configuration:   - Variable: ansible_psrp_max_envelope_size |
| **message_encryption**  string | Controls the message encryption settings, this is different from TLS encryption when *ansible_psrp_protocol* is `https`.  Only the auth protocols `negotiate`, `kerberos`, `ntlm`, and `credssp` can do message encryption. The other authentication protocols only support encryption when `protocol` is set to `https`.  `auto` means means message encryption is only used when not using TLS/HTTPS.  `always` is the same as `auto` but message encryption is always used even when running over TLS/HTTPS.  `never` disables any encryption checks that are in place when running over HTTP and disables any authentication encryption processes.  Choices:   - `"auto"` ← (default) - `"always"` - `"never"`   Configuration:   - Variable: ansible_psrp_message_encryption |
| **negotiate_delegate**  boolean | Allow the remote user the ability to delegate it’s credentials to another server, i.e. credential delegation.  Only valid when Kerberos was the negotiated auth or was explicitly set as the authentication.  Ignored when NTLM was the negotiated auth.  Choices:   - `false` - `true`   Configuration:   - Variable: ansible_psrp_negotiate_delegate |
| **negotiate_hostname_override**  string | Override the remote hostname when searching for the host in the Kerberos lookup.  This allows Ansible to connect over IP but authenticate with the remote server using it’s DNS name.  Only valid when Kerberos was the negotiated auth or was explicitly set as the authentication.  Ignored when NTLM was the negotiated auth.  Configuration:   - Variable: ansible_psrp_negotiate_hostname_override |
| **negotiate_send_cbt**  boolean | Send the Channel Binding Token (CBT) structure when authenticating.  CBT is used to provide extra protection against Man in the Middle `MitM` attacks by binding the outer transport channel to the auth channel.  CBT is not used when using just `HTTP`, only `HTTPS`.  Choices:   - `false` - `true` ← (default)   Configuration:   - Variable: ansible_psrp_negotiate_send_cbt |
| **negotiate_service**  string | Override the service part of the SPN used during Kerberos authentication.  Only valid when Kerberos was the negotiated auth or was explicitly set as the authentication.  Ignored when NTLM was the negotiated auth.  Default: `"WSMAN"`  Configuration:   - Variable: ansible_psrp_negotiate_service |
| **operation_timeout**  integer | Sets the WSMan timeout for each operation.  This is measured in seconds.  This should not exceed the value for `connection_timeout`.  Default: `20`  Configuration:   - Variable: ansible_psrp_operation_timeout |
| **path**  string | The URI path to connect to.  Default: `"wsman"`  Configuration:   - Variable: ansible_psrp_path |
| **pipelining**  boolean | Pipelining reduces the number of connection operations required to execute a module on the remote server, by executing many Ansible modules without actual file transfers.  This can result in a very significant performance improvement when enabled.  However this can conflict with privilege escalation (become). For example, when using sudo operations you must first disable ‘requiretty’ in the sudoers file for the target hosts, which is why this feature is disabled by default.  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entries:  ```YAML+Jinja   [defaults]   pipelining = false   ```  ```YAML+Jinja   [connection]   pipelining = false   ``` - Environment variable: [`ANSIBLE_PIPELINING`](../../../reference_appendices/config.md#envvar-ANSIBLE_PIPELINING) - Variable: ansible_pipelining |
| **port**  integer | The port for PSRP to connect on the remote target.  Default is `5986` if *protocol* is not defined or is `https`, otherwise the port is `5985`.  Configuration:   - Variable: ansible_port - Variable: ansible_psrp_port - Keyword: port |
| **protocol**  string | Set the protocol to use for the connection.  Default is `https` if *port* is not defined or *port* is not `5985`.  Choices:   - `"http"` - `"https"`   Configuration:   - Variable: ansible_psrp_protocol |
| **proxy**  string | Set the proxy URL to use when connecting to the remote host.  Configuration:   - Variable: ansible_psrp_proxy |
| **read_timeout**  integer  added in Ansible 2.8 | The read timeout for receiving data from the remote host.  This value must always be greater than *operation_timeout*.  This option requires pypsrp >= 0.3.  This is measured in seconds.  Default: `30`  Configuration:   - Variable: ansible_psrp_read_timeout |
| **reconnection_backoff**  integer  added in Ansible 2.8 | The backoff time to use in between reconnection attempts. (First sleeps X, then sleeps 2\*X, then sleeps 4\*X, …)  This is measured in seconds.  The `ansible_psrp_reconnection_backoff` variable was added in Ansible 2.9.  Default: `2`  Configuration:   - Variable: ansible_psrp_connection_backoff - Variable: ansible_psrp_reconnection_backoff |
| **reconnection_retries**  integer  added in Ansible 2.8 | The number of retries on connection errors.  Default: `0`  Configuration:   - Variable: ansible_psrp_reconnection_retries |
| **remote_addr**  string | The hostname or IP address of the remote host.  Default: `"inventory_hostname"`  Configuration:   - Variable: inventory_hostname - Variable: ansible_host - Variable: ansible_psrp_host |
| **remote_password**  aliases: password  string | Authentication password for the `remote_user`. Can be supplied as CLI option.  Configuration:   - Variable: ansible_password - Variable: ansible_winrm_pass - Variable: ansible_winrm_password |
| **remote_user**  string | The user to log in as.  Configuration:   - Variable: ansible_user - Variable: ansible_psrp_user - Keyword: remote_user |

### Authors

- Ansible Core Team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
