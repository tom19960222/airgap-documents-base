---
collection: ansible
version: "8"
title: "microsoft.ad.ldap inventory – Inventory plugin for Active Directory"
source_url: https://docs.ansible.com/projects/ansible/8/collections/microsoft/ad/ldap_inventory.html
fetched_at: 2026-07-28T01:05:52+00:00
---
# microsoft.ad.ldap inventory – Inventory plugin for Active Directory

> **Note:**
>
> This inventory plugin is part of the [microsoft.ad collection](https://galaxy.ansible.com/ui/repo/published/microsoft/ad/) (version 1.4.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install microsoft.ad`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](ldap_inventory.md#ansible-collections-microsoft-ad-ldap-inventory-requirements) for details.
>
> To use it in a playbook, specify: `microsoft.ad.ldap`.

New in microsoft.ad 1.1.0

- [Synopsis](ldap_inventory.md#synopsis)
- [Requirements](ldap_inventory.md#requirements)
- [Parameters](ldap_inventory.md#parameters)
- [Notes](ldap_inventory.md#notes)
- [Examples](ldap_inventory.md#examples)

## [Synopsis](ldap_inventory.md#id1)

- Inventory plugin for Active Directory or other LDAP sources.
- Uses a YAML configuration file that ends with `microsoft.ad.ldap.{yml|yaml}`.
- Each host that is added will set the `inventory_hostname` to the `name` of the LDAP computer object and `ansible_host` to the value of the `dNSHostName` LDAP attribute if set. If the `dNSHostName` attribute is not set on the computer object then `ansible_host` is not set. See [LDAP inventory hostname](docsite/guide_ldap_inventory.md#ansible-collections-microsoft-ad-docsite-guide-ldap-inventory-inventory-hostname) for more information on how these values are set and how to adjust them.
- The host fact `microsoft_ad_distinguished_name` will also be set to the distinguished name of the host that was used to derive the host entry.
- Any other fact that is needed, needs to be defined in the *attributes* option.

## [Requirements](ldap_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- dnspython - For option server lookup support
- pyspnego >= 0.8.0
- pyspnego[kerberos] - For Kerberos and server lookup support
- sansldap

## [Parameters](ldap_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  dictionary | The LDAP attributes to retrieve.  The keys specified are the LDAP attributes requested and the values for each attribute is a dictionary that reflects what host var to set it to and how.  Each key of the inner dictionary value is the host variable name to set and the value is the template to use to derive the value. If no value is explicitly set then it will use the coerced value as returned from the LDAP attribute.  Attributes that are denoted as single value in the LDAP schema are returned as that single value, multi valued attributes are returned as a list of values.  See [LDAP inventory attributes](docsite/guide_ldap_inventory.md#ansible-collections-microsoft-ad-docsite-guide-ldap-inventory-attributes) for more information.  **Default:** `{}` |
| **auth_protocol**  string | The authentication protocol to use when connecting to the LDAP host.  Defaults to `certificate` if LDAPS/StartTLS is used and *certificate* has been specified. Otherwise it defaults to `negotiate`.  `simple` is simple authentication where the user and password are sent in plaintext. It does not support any encryption so either must be used with LDAPS, or StartTLS. If using over a plaintext LDAP connection without TLS, `encrypt=False` must be specified to explicitly opt into no encryption.  `certificate` is TLS client certificate authentication. It can only be used with LDAPS or StartTLS. See *certificate* for more information on how to specify the client certificate used for authentication.  `negotiate` will attempt to negotiate Kerberos authentication with a fallback to NTLM. If Kerberos is available the Kerberos credential cache can be used if no username or password is specified.  `kerberos` will use Kerberos authentication with no NTLM fallback.  `ntlm` will use NTLM authentication with no Kerberos attempt.  `negotiate`, `kerberos`, and `ntlm` support encryption over LDAP.  Kerberos support requires the `pyspnego[kerberos]` extras to be installed.  See [LDAP authentication](docsite/guide_ldap_connection.md#ansible-collections-microsoft-ad-docsite-guide-ldap-connection-authentication) for more information.  **Choices:**   - `"simple"` - `"certificate"` - `"negotiate"` - `"kerberos"` - `"ntlm"`   **Configuration:**   - Environment variable: [`MICROSOFT_AD_LDAP_AUTH_PROTOCOL`](../../environment_variables.md#envvar-MICROSOFT_AD_LDAP_AUTH_PROTOCOL) |
| **ca_cert**  string | Can be the path to a CA certificate PEM or DER file, directory of PEM certificates, or the CA certificate PEM string that is used for certificate validation.  If omitted, the default CA store used for validation is dependent on the current Python settings.  **Configuration:**   - Environment variable: [`MICROSOFT_AD_LDAP_CA_CERT`](../../environment_variables.md#envvar-MICROSOFT_AD_LDAP_CA_CERT) |
| **cert_validation**  string | The certificate validation behaviour when using a TLS connection.  This can be set to `always`, `ignore`, `ignore_hostname`.  `always` will perform certificate hostname and CA validation.  `ignore` will ignore any certificate errors.  `ignore_hostname` will validate the CA trust chain but will ignore any hostname checks performed by TLS.  See [Certificate validation](docsite/guide_ldap_connection.md#ansible-collections-microsoft-ad-docsite-guide-ldap-connection-cert-validation) for more information.  **Choices:**   - `"always"` ← (default) - `"ignore"` - `"ignore_hostname"`   **Configuration:**   - Environment variable: [`MICROSOFT_AD_LDAP_CERT_VALIDATION`](../../environment_variables.md#envvar-MICROSOFT_AD_LDAP_CERT_VALIDATION) |
| **certificate**  string | The certificate or certificate with key bundle that is used for certificate authentication.  The value can either be a path to a file containing the certificate or string of the PEM encoded certificate.  If using a path to a certificate file, the file can be a PEM encoded certificate, a PEM encoded certificate and key bundle, a DER encoded certificate, or a PFX/PKCS12 encoded certificate and key bundle.  Use *certificate_key* if the certificate specified does not contain the key.  Use *certificate_password* if the key is encrypted with a password.  **Configuration:**   - Environment variable: [`MICROSOFT_AD_LDAP_CERTIFICATE`](../../environment_variables.md#envvar-MICROSOFT_AD_LDAP_CERTIFICATE) |
| **certificate_key**  string | The certificate key that is used for certificate authentication.  The value can either be a path to a file containing the key in the PEM or DER encoded form, or it can be the string of a PEM encoded key.  Use *certificate_password* if the key is encrypted with a password.  **Configuration:**   - Environment variable: [`MICROSOFT_AD_LDAP_CERTIFICATE_KEY`](../../environment_variables.md#envvar-MICROSOFT_AD_LDAP_CERTIFICATE_KEY) |
| **certificate_password**  string | The password used to decrypt the certificate key specified by *certificate* or *certificate_key*.  **Configuration:**   - Environment variable: [`MICROSOFT_AD_LDAP_CERTIFICATE_PASSWORD`](../../environment_variables.md#envvar-MICROSOFT_AD_LDAP_CERTIFICATE_PASSWORD) |
| **compose**  dictionary | Create vars from jinja2 expressions.  **Default:** `{}` |
| **connection_timeout**  integer | The timeout in seconds to wait until the connection is established before failing.  **Default:** `5`  **Configuration:**   - Environment variable: [`MICROSOFT_AD_LDAP_CONNECTION_TIMEOUT`](../../environment_variables.md#envvar-MICROSOFT_AD_LDAP_CONNECTION_TIMEOUT) |
| **encrypt**  boolean | Whether encryption is required for the connection.  Encryption can either be performed using the authentication protocol or through TLS.  The *auth_protocol* `negotiate`, `kerberos`, and `ntlm` all support encryption over LDAP whereas `simple` does not.  If using `auth_protocol=simple` over LDAP without TLS then this must be set to `False`. As no encryption is used, all traffic will be in plaintext and should be avoided.  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - Environment variable: [`MICROSOFT_AD_LDAP_ENCRYPT`](../../environment_variables.md#envvar-MICROSOFT_AD_LDAP_ENCRYPT) |
| **filter**  string | The LDAP filter string used to query the computer objects.  By default, this will be combined with the filter “(objectClass=computer)”. Use *filter_without_computer* to override this behavior and have *filter* be the only filter used. |
| **filter_without_computer**  boolean  *added in microsoft.ad 1.3.0* | Will not combine the *filter* value with the filter “(objectClass=computer)”.  In most cases this should be `false` but can be set to `true` to have the *filter* value specified be the only filter used.  **Choices:**   - `false` ← (default) - `true` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  **Default:** `[]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **password**  string | The password to authenticate with.  If *auth_protocol* is `simple` and no password is specified, the bind will be performed as an unauthenticated bind.  If *auth_protocol* is `negotiate`, `kerberos`, or `ntlm` and no password is specified, it will attempt to use the local cached credential specified by *username* if available.  **Configuration:**   - Environment variable: [`MICROSOFT_AD_LDAP_PASSWORD`](../../environment_variables.md#envvar-MICROSOFT_AD_LDAP_PASSWORD) |
| **port**  integer | The LDAP port to use for the connection.  Port 389 is used for LDAP and port 686 is used for LDAPS.  Defaults to port `636` if `tls_mode=ldaps` otherwise `389`.  **Configuration:**   - Environment variable: [`MICROSOFT_AD_LDAP_PORT`](../../environment_variables.md#envvar-MICROSOFT_AD_LDAP_PORT) |
| **search_base**  string | The LDAP search base to find the computer objects in.  Defaults to the `defaultNamingContext` of the Active Directory server if not specified.  If searching a larger Active Directory database, it is recommended to narrow the search base to speed up the queries. |
| **search_scope**  string | The scope of the LDAP search to perform.  `base` will search only the current path or object specified by *search_base*. This is typically not useful for inventory plugins.  `one_level` will search only the immediate child objects in *search_base*.  `subtree` will search the immediate child objects and any nested objects in *search_base*.  **Choices:**   - `"base"` - `"one_level"` - `"subtree"` ← (default) |
| **server**  string | The domain controller/server to connect to.  If not specified the server will be derived from the current krb5.conf `default_realm` setting and with an SRV DNS lookup.  See [Server lookup](docsite/guide_ldap_connection.md#ansible-collections-microsoft-ad-docsite-guide-ldap-connection-server-lookup) for more information.  **Configuration:**   - Environment variable: [`MICROSOFT_AD_LDAP_SERVER`](../../environment_variables.md#envvar-MICROSOFT_AD_LDAP_SERVER) |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **tls_mode**  string | The TLS operation to use.  If an explicit *port* is set to `636` then this defaults to `ldaps`.  `ldaps` will connect over LDAPS (port 636).  `start_tls` will connect over LDAP (port 389) and perform the StartTLS operation before the authentication bind.  It is recommended to use `ldaps` over `start_tls` if TLS is going to be used.  **Choices:**   - `"ldaps"` - `"start_tls"`   **Configuration:**   - Environment variable: [`MICROSOFT_AD_LDAP_TLS_MODE`](../../environment_variables.md#envvar-MICROSOFT_AD_LDAP_TLS_MODE) |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **username**  string | The username to authenticate with.  If *auth_protocol* is `simple` and no username is specified, anonymous authentication is used.  If *auth_protocol* is `negotiate`, `kerberos`, or `ntlm` and no username is specified, it will attempt to use the local cached credential if available, for example one retrieved by `kinit`.  **Configuration:**   - Environment variable: [`MICROSOFT_AD_LDAP_USERNAME`](../../environment_variables.md#envvar-MICROSOFT_AD_LDAP_USERNAME) |

## [Notes](ldap_inventory.md#id4)

> **Note:**
>
> - See [LDAP inventory](docsite/guide_ldap_inventory.md#ansible-collections-microsoft-ad-docsite-guide-ldap-inventory) for more details on how to use this inventory plugin.
> - See [LAPS](docsite/guide_ldap_inventory.md#ansible-collections-microsoft-ad-docsite-guide-ldap-inventory-laps) for more details on how this plugin can retrieve the LAPS password information.
> - This plugin is a tech preview and the module options are subject to change based on feedback received.
> - See [LDAP connection help](docsite/guide_ldap_connection.md#ansible-collections-microsoft-ad-docsite-guide-ldap-connection) for more information about LDAP connections.

## [Examples](ldap_inventory.md#id5)

```yaml+jinja
# Set in the file ending with microsoft.ad.ldap.yml or microsoft.ad.ldap.yaml
plugin: microsoft.ad.ldap

####################################################################
#                        Connection Options                        #
#                                                                  #
# These options control how the plugin connects to the LDAP server #
####################################################################

# Connects to ldap://dc01.domain.com:389
server: dc01.domain.com
port: 389

# Connects to ldaps://dc01.domain.com:636
server: dc01.domain.com
tls_mode: ldaps

# Connects to the global catalog
# ldap://dc01.domain.com:3268
server: dc01.domain.com
port: 3268

# Provides explicit user, will use the current Kerberos ticket if no credential
# is provided.
username: domain-user@DOMAIN.COM
password: Password123!

# Only allow Kerberos authentication.
auth_protocol: kerberos

# Verify LDAPS CA chain with custom CA chain.
tls_mode: ldaps
ca_cert: /home/user/certs/ldap.pem

##############################################
#               Search Options               #
#                                            #
# These options control the searching rules  #
##############################################

# Search for computer accounts in the Workshop OU.
search_base: OU=Workshop A,DC=domain,DC=com

# Filter the computer accounts returned for only ones with the dNSDomainName
# attribute set.
filter: (dNSDomainName=*)

# Filter computer accounts returned for ones starting with PROD and with the
# LAPS password set.
filter: (&(sAMAccountName=PROD*)(ms-Mcs-AdmPwd=*))

# See documentation for more details
attributes:
  sAMAccountName:
    sam_account_name:
  objectSid:
    computer_sid:
  pwdLastSet:
    password_last_set: this | microsoft.ad.as_datetime
  comment:
    host_comment
  memberOf:
    computer_membership: this | map("regex_search", '^CN=(?P<name>.+?)((?<!\\),)', '\g<name>') | flatten
  location:

############################################################################
#                             LAPS Integration                             #
#                                                                          #
# Examples on how to use the new Windows LAPS values as connection options #
############################################################################

attributes:
  # msLAPS-Password is used if no encryption has been configured.
  # Currently an encrypted LAPS password is not supported.
  msLAPS-Password:
    ansible_user: (this | from_json).n
    ansible_password: (this | from_json).p

  # msLAPS-EncryptedPassword is used if encryption has been configured.
  # If the Python dpapi-ng library is installed the `this`` value will
  # contain the entry `value` which is the decrypted value. The ``info``
  # entry will contain the reason why the value could not be decrypted.
  msLAPS-EncryptedPassword:
    ansible_user: (this.value | from_json).n
    ansible_password: (this.value | from_json).p

  # ms-Mcs-AdmPwd is used for Legacy LAPS and stores just the password.
  # The username needs to be hardcoded as a string value for this template.
  ms-Mcs-AdmPwd:
    ansible_user: '"Administrator"'
    ansible_password: this

#####################################################################
#                        Constructed Options                        #
#                                                                   #
# These options control the constructed values like vars and groups #
#####################################################################

# Build composed host variables. Requires attributes to be set in the
# attributes option to be referenced here.
compose:
  host_var: computer_sid

# Conditionals that adds found hosts to the groups specified.
groups:
  # Adds all hosts to the windows group
  windows: true

  # Uses the memberOf fact documented above to place the host in the production
  # group if it's a member of that group
  production: '"Production Group" in computer_membership'

# Adds the host to a group site_{{ location }} with the default group of
# site_unknown if the location isn't defined
keyed_groups:
- key: location | default(omit)
  prefix: site
  default_value: unknown
```

### Authors

- Jordan Borean (@jborean93)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/microsoft.ad/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/microsoft.ad)
- [Report an issue](https://github.com/ansible-collections/microsoft.ad/issues/new/choose)
- [Communication](index.md#communication-for-microsoft-ad)
