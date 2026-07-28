---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_user_setting module – Configure user authentication setting in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_user_setting_module.html
fetched_at: 2026-07-28T02:30:05+00:00
---
# fortinet.fortios.fortios_user_setting module – Configure user authentication setting in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortios/) (version 2.3.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_user_setting_module.md#ansible-collections-fortinet-fortios-fortios-user-setting-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_user_setting`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_user_setting_module.md#synopsis)
- [Requirements](fortios_user_setting_module.md#requirements)
- [Parameters](fortios_user_setting_module.md#parameters)
- [Notes](fortios_user_setting_module.md#notes)
- [Examples](fortios_user_setting_module.md#examples)
- [Return Values](fortios_user_setting_module.md#return-values)

## [Synopsis](fortios_user_setting_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify user feature and setting category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_user_setting_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_user_setting_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **user_setting**  dictionary | Configure user authentication setting. |
| **auth_blackout_time**  integer | Time in seconds an IP address is denied access after failing to authenticate five times within one minute. |
| **auth_ca_cert**  string | HTTPS CA certificate for policy authentication. Source vpn.certificate.local.name. |
| **auth_cert**  string | HTTPS server certificate for policy authentication. Source vpn.certificate.local.name. |
| **auth_http_basic**  string | Enable/disable use of HTTP basic authentication for identity-based firewall policies.  **Choices:**   - `"enable"` - `"disable"` |
| **auth_invalid_max**  integer | Maximum number of failed authentication attempts before the user is blocked. |
| **auth_lockout_duration**  integer | Lockout period in seconds after too many login failures. |
| **auth_lockout_threshold**  integer | Maximum number of failed login attempts before login lockout is triggered. |
| **auth_on_demand**  string | Always/implicitly trigger firewall authentication on demand.  **Choices:**   - `"always"` - `"implicitly"` |
| **auth_portal_timeout**  integer | Time in minutes before captive portal user have to re-authenticate (1 - 30 min). |
| **auth_ports**  list / elements=dictionary | Set up non-standard ports for authentication with HTTP, HTTPS, FTP, and TELNET. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **port**  integer | Non-standard port for firewall user authentication. |
| **type**  string | Service type.  **Choices:**   - `"http"` - `"https"` - `"ftp"` - `"telnet"` |
| **auth_secure_http**  string | Enable/disable redirecting HTTP user authentication to more secure HTTPS.  **Choices:**   - `"enable"` - `"disable"` |
| **auth_src_mac**  string | Enable/disable source MAC for user identity.  **Choices:**   - `"enable"` - `"disable"` |
| **auth_ssl_allow_renegotiation**  string | Allow/forbid SSL re-negotiation for HTTPS authentication.  **Choices:**   - `"enable"` - `"disable"` |
| **auth_ssl_max_proto_version**  string | Maximum supported protocol version for SSL/TLS connections .  **Choices:**   - `"sslv3"` - `"tlsv1"` - `"tlsv1-1"` - `"tlsv1-2"` - `"tlsv1-3"` |
| **auth_ssl_min_proto_version**  string | Minimum supported protocol version for SSL/TLS connections .  **Choices:**   - `"default"` - `"SSLv3"` - `"TLSv1"` - `"TLSv1-1"` - `"TLSv1-2"` - `"TLSv1-3"` |
| **auth_ssl_sigalgs**  string | Set signature algorithms related to HTTPS authentication (affects TLS version <= 1.2 only).  **Choices:**   - `"no-rsa-pss"` - `"all"` |
| **auth_timeout**  integer | Time in minutes before the firewall user authentication timeout requires the user to re-authenticate. |
| **auth_timeout_type**  string | Control if authenticated users have to login again after a hard timeout, after an idle timeout, or after a session timeout.  **Choices:**   - `"idle-timeout"` - `"hard-timeout"` - `"new-session"` |
| **auth_type**  list / elements=string | Supported firewall policy authentication protocols/methods.  **Choices:**   - `"http"` - `"https"` - `"ftp"` - `"telnet"` |
| **default_user_password_policy**  string | Default password policy to apply to all local users unless otherwise specified, as defined in config user password-policy. Source user .password-policy.name. |
| **per_policy_disclaimer**  string | Enable/disable per policy disclaimer.  **Choices:**   - `"enable"` - `"disable"` |
| **radius_ses_timeout_act**  string | Set the RADIUS session timeout to a hard timeout or to ignore RADIUS server session timeouts.  **Choices:**   - `"hard-timeout"` - `"ignore-timeout"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_user_setting_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_user_setting_module.md#id5)

```yaml+jinja
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure user authentication setting.
    fortios_user_setting:
      vdom:  "{{ vdom }}"
      user_setting:
        auth_blackout_time: "0"
        auth_ca_cert: "<your_own_value> (source vpn.certificate.local.name)"
        auth_cert: "<your_own_value> (source vpn.certificate.local.name)"
        auth_http_basic: "enable"
        auth_invalid_max: "5"
        auth_lockout_duration: "0"
        auth_lockout_threshold: "3"
        auth_on_demand: "always"
        auth_portal_timeout: "3"
        auth_ports:
         -
            id:  "13"
            port: "1024"
            type: "http"
        auth_secure_http: "enable"
        auth_src_mac: "enable"
        auth_ssl_allow_renegotiation: "enable"
        auth_ssl_max_proto_version: "sslv3"
        auth_ssl_min_proto_version: "default"
        auth_ssl_sigalgs: "no-rsa-pss"
        auth_timeout: "5"
        auth_timeout_type: "idle-timeout"
        auth_type: "http"
        default_user_password_policy: "<your_own_value> (source user.password-policy.name)"
        per_policy_disclaimer: "enable"
        radius_ses_timeout_act: "hard-timeout"
```

## [Return Values](fortios_user_setting_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  **Returned:** always  **Sample:** `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  **Returned:** always  **Sample:** `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  **Returned:** always  **Sample:** `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  **Returned:** success  **Sample:** `"id"` |
| **name**  string | Name of the table used to fulfill the request  **Returned:** always  **Sample:** `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  **Returned:** always  **Sample:** `"webfilter"` |
| **revision**  string | Internal revision number  **Returned:** always  **Sample:** `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  **Returned:** always  **Sample:** `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  **Returned:** always  **Sample:** `"success"` |
| **vdom**  string | Virtual domain used  **Returned:** always  **Sample:** `"root"` |
| **version**  string | Version of the FortiGate  **Returned:** always  **Sample:** `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
- [Homepage](https://www.fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
