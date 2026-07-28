---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_firewall_profile_protocol_options module – Configure protocol options in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_firewall_profile_protocol_options_module.html
fetched_at: 2026-07-27T17:41:21+00:00
---
# fortinet.fortios.fortios_firewall_profile_protocol_options module – Configure protocol options in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_firewall_profile_protocol_options_module.md#ansible-collections-fortinet-fortios-fortios-firewall-profile-protocol-options-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_profile_protocol_options`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_profile_protocol_options_module.md#synopsis)
- [Requirements](fortios_firewall_profile_protocol_options_module.md#requirements)
- [Parameters](fortios_firewall_profile_protocol_options_module.md#parameters)
- [Notes](fortios_firewall_profile_protocol_options_module.md#notes)
- [Examples](fortios_firewall_profile_protocol_options_module.md#examples)
- [Return Values](fortios_firewall_profile_protocol_options_module.md#return-values)

## [Synopsis](fortios_firewall_profile_protocol_options_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and profile_protocol_options category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_profile_protocol_options_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_firewall_profile_protocol_options_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **firewall_profile_protocol_options**  dictionary | Configure protocol options. |
| **cifs**  dictionary | Configure CIFS protocol options. |
| **domain_controller**  string | Domain for which to decrypt CIFS traffic. Source user.domain-controller.name credential-store.domain-controller.server-name. |
| **options**  list / elements=string | One or more options that can be applied to the session.  Choices:   - `"oversize"` |
| **oversize_limit**  integer | Maximum in-memory file size that can be scanned (1 - 383 MB). |
| **ports**  list / elements=integer | Ports to scan for content (1 - 65535). |
| **scan_bzip2**  string | Enable/disable scanning of BZip2 compressed files.  Choices:   - `"enable"` - `"disable"` |
| **server_credential_type**  string | CIFS server credential type.  Choices:   - `"none"` - `"credential-replication"` - `"credential-keytab"` |
| **server_keytab**  list / elements=dictionary | Server keytab. |
| **keytab**  string | Base64 encoded keytab file containing credential of the server. |
| **principal**  string | Service principal. For example, [host/cifsserver.example.com@example.com](mailto:host/cifsserver.example.com%40example.com). |
| **status**  string | Enable/disable the active status of scanning for this protocol.  Choices:   - `"enable"` - `"disable"` |
| **tcp_window_maximum**  integer | Maximum dynamic TCP window size. |
| **tcp_window_minimum**  integer | Minimum dynamic TCP window size. |
| **tcp_window_size**  integer | Set TCP static window size. |
| **tcp_window_type**  string | TCP window type to use for this protocol.  Choices:   - `"auto-tuning"` - `"system"` - `"static"` - `"dynamic"` |
| **uncompressed_nest_limit**  integer | Maximum nested levels of compression that can be uncompressed and scanned (2 - 100). |
| **uncompressed_oversize_limit**  integer | Maximum in-memory uncompressed file size that can be scanned (1 - 383 MB). |
| **comment**  string | Optional comments. |
| **dns**  dictionary | Configure DNS protocol options. |
| **ports**  list / elements=integer | Ports to scan for content (1 - 65535). |
| **status**  string | Enable/disable the active status of scanning for this protocol.  Choices:   - `"enable"` - `"disable"` |
| **ftp**  dictionary | Configure FTP protocol options. |
| **comfort_amount**  integer | Amount of data to send in a transmission for client comforting (1 - 65535 bytes). |
| **comfort_interval**  integer | Period of time between start, or last transmission, and the next client comfort transmission of data (1 - 900 sec). |
| **explicit_ftp_tls**  string | Enable/disable FTP redirection for explicit FTPS.  Choices:   - `"enable"` - `"disable"` |
| **inspect_all**  string | Enable/disable the inspection of all ports for the protocol.  Choices:   - `"enable"` - `"disable"` |
| **options**  list / elements=string | One or more options that can be applied to the session.  Choices:   - `"clientcomfort"` - `"oversize"` - `"splice"` - `"bypass-rest-command"` - `"bypass-mode-command"` |
| **oversize_limit**  integer | Maximum in-memory file size that can be scanned (1 - 383 MB). |
| **ports**  list / elements=integer | Ports to scan for content (1 - 65535). |
| **scan_bzip2**  string | Enable/disable scanning of BZip2 compressed files.  Choices:   - `"enable"` - `"disable"` |
| **ssl_offloaded**  string | SSL decryption and encryption performed by an external device.  Choices:   - `"no"` - `"yes"` |
| **status**  string | Enable/disable the active status of scanning for this protocol.  Choices:   - `"enable"` - `"disable"` |
| **stream_based_uncompressed_limit**  integer | Maximum stream-based uncompressed data size that will be scanned in megabytes. Stream-based uncompression used only under certain conditions (unlimited = 0). |
| **tcp_window_maximum**  integer | Maximum dynamic TCP window size. |
| **tcp_window_minimum**  integer | Minimum dynamic TCP window size. |
| **tcp_window_size**  integer | Set TCP static window size. |
| **tcp_window_type**  string | TCP window type to use for this protocol.  Choices:   - `"auto-tuning"` - `"system"` - `"static"` - `"dynamic"` |
| **uncompressed_nest_limit**  integer | Maximum nested levels of compression that can be uncompressed and scanned (2 - 100). |
| **uncompressed_oversize_limit**  integer | Maximum in-memory uncompressed file size that can be scanned (1 - 383 MB). |
| **http**  dictionary | Configure HTTP protocol options. |
| **address_ip_rating**  string | Enable/disable IP based URL rating.  Choices:   - `"enable"` - `"disable"` |
| **block_page_status_code**  integer | Code number returned for blocked HTTP pages (non-FortiGuard only) (100 - 599). |
| **comfort_amount**  integer | Amount of data to send in a transmission for client comforting (1 - 65535 bytes). |
| **comfort_interval**  integer | Period of time between start, or last transmission, and the next client comfort transmission of data (1 - 900 sec). |
| **fortinet_bar**  string | Enable/disable Fortinet bar on HTML content.  Choices:   - `"enable"` - `"disable"` |
| **fortinet_bar_port**  integer | Port for use by Fortinet Bar (1 - 65535). |
| **h2c**  string | Enable/disable h2c HTTP connection upgrade.  Choices:   - `"enable"` - `"disable"` |
| **http_policy**  string | Enable/disable HTTP policy check.  Choices:   - `"disable"` - `"enable"` |
| **inspect_all**  string | Enable/disable the inspection of all ports for the protocol.  Choices:   - `"enable"` - `"disable"` |
| **options**  list / elements=string | One or more options that can be applied to the session.  Choices:   - `"clientcomfort"` - `"servercomfort"` - `"oversize"` - `"chunkedbypass"` |
| **oversize_limit**  integer | Maximum in-memory file size that can be scanned (1 - 383 MB). |
| **ports**  list / elements=integer | Ports to scan for content (1 - 65535). |
| **post_lang**  list / elements=string | ID codes for character sets to be used to convert to UTF-8 for banned words and DLP on HTTP posts (maximum of 5 character sets).  Choices:   - `"jisx0201"` - `"jisx0208"` - `"jisx0212"` - `"gb2312"` - `"ksc5601-ex"` - `"euc-jp"` - `"sjis"` - `"iso2022-jp"` - `"iso2022-jp-1"` - `"iso2022-jp-2"` - `"euc-cn"` - `"ces-gbk"` - `"hz"` - `"ces-big5"` - `"euc-kr"` - `"iso2022-jp-3"` - `"iso8859-1"` - `"tis620"` - `"cp874"` - `"cp1252"` - `"cp1251"` |
| **proxy_after_tcp_handshake**  string | Proxy traffic after the TCP 3-way handshake has been established (not before).  Choices:   - `"enable"` - `"disable"` |
| **range_block**  string | Enable/disable blocking of partial downloads.  Choices:   - `"disable"` - `"enable"` |
| **retry_count**  integer | Number of attempts to retry HTTP connection (0 - 100). |
| **scan_bzip2**  string | Enable/disable scanning of BZip2 compressed files.  Choices:   - `"enable"` - `"disable"` |
| **ssl_offloaded**  string | SSL decryption and encryption performed by an external device.  Choices:   - `"no"` - `"yes"` |
| **status**  string | Enable/disable the active status of scanning for this protocol.  Choices:   - `"enable"` - `"disable"` |
| **stream_based_uncompressed_limit**  integer | Maximum stream-based uncompressed data size that will be scanned in megabytes. Stream-based uncompression used only under certain conditions (unlimited = 0). |
| **streaming_content_bypass**  string | Enable/disable bypassing of streaming content from buffering.  Choices:   - `"enable"` - `"disable"` |
| **strip_x_forwarded_for**  string | Enable/disable stripping of HTTP X-Forwarded-For header.  Choices:   - `"disable"` - `"enable"` |
| **switching_protocols**  string | Bypass from scanning, or block a connection that attempts to switch protocol.  Choices:   - `"bypass"` - `"block"` |
| **tcp_window_maximum**  integer | Maximum dynamic TCP window size. |
| **tcp_window_minimum**  integer | Minimum dynamic TCP window size. |
| **tcp_window_size**  integer | Set TCP static window size. |
| **tcp_window_type**  string | TCP window type to use for this protocol.  Choices:   - `"auto-tuning"` - `"system"` - `"static"` - `"dynamic"` |
| **tunnel_non_http**  string | Configure how to process non-HTTP traffic when a profile configured for HTTP traffic accepts a non-HTTP session. Can occur if an application sends non-HTTP traffic using an HTTP destination port.  Choices:   - `"enable"` - `"disable"` |
| **uncompressed_nest_limit**  integer | Maximum nested levels of compression that can be uncompressed and scanned (2 - 100). |
| **uncompressed_oversize_limit**  integer | Maximum in-memory uncompressed file size that can be scanned (1 - 383 MB). |
| **unknown_http_version**  string | How to handle HTTP sessions that do not comply with HTTP 0.9, 1.0, or 1.1.  Choices:   - `"reject"` - `"tunnel"` - `"best-effort"` |
| **verify_dns_for_policy_matching**  string | Enable/disable verification of DNS for policy matching.  Choices:   - `"enable"` - `"disable"` |
| **imap**  dictionary | Configure IMAP protocol options. |
| **inspect_all**  string | Enable/disable the inspection of all ports for the protocol.  Choices:   - `"enable"` - `"disable"` |
| **options**  list / elements=string | One or more options that can be applied to the session.  Choices:   - `"fragmail"` - `"oversize"` |
| **oversize_limit**  integer | Maximum in-memory file size that can be scanned (1 - 383 MB). |
| **ports**  list / elements=integer | Ports to scan for content (1 - 65535). |
| **proxy_after_tcp_handshake**  string | Proxy traffic after the TCP 3-way handshake has been established (not before).  Choices:   - `"enable"` - `"disable"` |
| **scan_bzip2**  string | Enable/disable scanning of BZip2 compressed files.  Choices:   - `"enable"` - `"disable"` |
| **ssl_offloaded**  string | SSL decryption and encryption performed by an external device.  Choices:   - `"no"` - `"yes"` |
| **status**  string | Enable/disable the active status of scanning for this protocol.  Choices:   - `"enable"` - `"disable"` |
| **uncompressed_nest_limit**  integer | Maximum nested levels of compression that can be uncompressed and scanned (2 - 100). |
| **uncompressed_oversize_limit**  integer | Maximum in-memory uncompressed file size that can be scanned (1 - 383 MB). |
| **mail_signature**  dictionary | Configure Mail signature. |
| **signature**  string | Email signature to be added to outgoing email (if the signature contains spaces, enclose with quotation marks). |
| **status**  string | Enable/disable adding an email signature to SMTP email messages as they pass through the FortiGate.  Choices:   - `"disable"` - `"enable"` |
| **mapi**  dictionary | Configure MAPI protocol options. |
| **options**  list / elements=string | One or more options that can be applied to the session.  Choices:   - `"fragmail"` - `"oversize"` |
| **oversize_limit**  integer | Maximum in-memory file size that can be scanned (1 - 383 MB). |
| **ports**  list / elements=integer | Ports to scan for content (1 - 65535). |
| **scan_bzip2**  string | Enable/disable scanning of BZip2 compressed files.  Choices:   - `"enable"` - `"disable"` |
| **status**  string | Enable/disable the active status of scanning for this protocol.  Choices:   - `"enable"` - `"disable"` |
| **uncompressed_nest_limit**  integer | Maximum nested levels of compression that can be uncompressed and scanned (2 - 100). |
| **uncompressed_oversize_limit**  integer | Maximum in-memory uncompressed file size that can be scanned (1 - 383 MB). |
| **name**  string / required | Name. |
| **nntp**  dictionary | Configure NNTP protocol options. |
| **inspect_all**  string | Enable/disable the inspection of all ports for the protocol.  Choices:   - `"enable"` - `"disable"` |
| **options**  list / elements=string | One or more options that can be applied to the session.  Choices:   - `"oversize"` - `"splice"` |
| **oversize_limit**  integer | Maximum in-memory file size that can be scanned (1 - 383 MB). |
| **ports**  list / elements=integer | Ports to scan for content (1 - 65535). |
| **proxy_after_tcp_handshake**  string | Proxy traffic after the TCP 3-way handshake has been established (not before).  Choices:   - `"enable"` - `"disable"` |
| **scan_bzip2**  string | Enable/disable scanning of BZip2 compressed files.  Choices:   - `"enable"` - `"disable"` |
| **status**  string | Enable/disable the active status of scanning for this protocol.  Choices:   - `"enable"` - `"disable"` |
| **uncompressed_nest_limit**  integer | Maximum nested levels of compression that can be uncompressed and scanned (2 - 100). |
| **uncompressed_oversize_limit**  integer | Maximum in-memory uncompressed file size that can be scanned (1 - 383 MB). |
| **oversize_log**  string | Enable/disable logging for antivirus oversize file blocking.  Choices:   - `"disable"` - `"enable"` |
| **pop3**  dictionary | Configure POP3 protocol options. |
| **inspect_all**  string | Enable/disable the inspection of all ports for the protocol.  Choices:   - `"enable"` - `"disable"` |
| **options**  list / elements=string | One or more options that can be applied to the session.  Choices:   - `"fragmail"` - `"oversize"` |
| **oversize_limit**  integer | Maximum in-memory file size that can be scanned (1 - 383 MB). |
| **ports**  list / elements=integer | Ports to scan for content (1 - 65535). |
| **proxy_after_tcp_handshake**  string | Proxy traffic after the TCP 3-way handshake has been established (not before).  Choices:   - `"enable"` - `"disable"` |
| **scan_bzip2**  string | Enable/disable scanning of BZip2 compressed files.  Choices:   - `"enable"` - `"disable"` |
| **ssl_offloaded**  string | SSL decryption and encryption performed by an external device.  Choices:   - `"no"` - `"yes"` |
| **status**  string | Enable/disable the active status of scanning for this protocol.  Choices:   - `"enable"` - `"disable"` |
| **uncompressed_nest_limit**  integer | Maximum nested levels of compression that can be uncompressed and scanned (2 - 100). |
| **uncompressed_oversize_limit**  integer | Maximum in-memory uncompressed file size that can be scanned (1 - 383 MB). |
| **replacemsg_group**  string | Name of the replacement message group to be used. Source system.replacemsg-group.name. |
| **rpc_over_http**  string | Enable/disable inspection of RPC over HTTP.  Choices:   - `"enable"` - `"disable"` |
| **smtp**  dictionary | Configure SMTP protocol options. |
| **inspect_all**  string | Enable/disable the inspection of all ports for the protocol.  Choices:   - `"enable"` - `"disable"` |
| **options**  list / elements=string | One or more options that can be applied to the session.  Choices:   - `"fragmail"` - `"oversize"` - `"splice"` |
| **oversize_limit**  integer | Maximum in-memory file size that can be scanned (1 - 383 MB). |
| **ports**  list / elements=integer | Ports to scan for content (1 - 65535). |
| **proxy_after_tcp_handshake**  string | Proxy traffic after the TCP 3-way handshake has been established (not before).  Choices:   - `"enable"` - `"disable"` |
| **scan_bzip2**  string | Enable/disable scanning of BZip2 compressed files.  Choices:   - `"enable"` - `"disable"` |
| **server_busy**  string | Enable/disable SMTP server busy when server not available.  Choices:   - `"enable"` - `"disable"` |
| **ssl_offloaded**  string | SSL decryption and encryption performed by an external device.  Choices:   - `"no"` - `"yes"` |
| **status**  string | Enable/disable the active status of scanning for this protocol.  Choices:   - `"enable"` - `"disable"` |
| **uncompressed_nest_limit**  integer | Maximum nested levels of compression that can be uncompressed and scanned (2 - 100). |
| **uncompressed_oversize_limit**  integer | Maximum in-memory uncompressed file size that can be scanned (1 - 383 MB). |
| **ssh**  dictionary | Configure SFTP and SCP protocol options. |
| **comfort_amount**  integer | Amount of data to send in a transmission for client comforting (1 - 65535 bytes). |
| **comfort_interval**  integer | Period of time between start, or last transmission, and the next client comfort transmission of data (1 - 900 sec). |
| **options**  list / elements=string | One or more options that can be applied to the session.  Choices:   - `"oversize"` - `"clientcomfort"` - `"servercomfort"` |
| **oversize_limit**  integer | Maximum in-memory file size that can be scanned (1 - 383 MB). |
| **scan_bzip2**  string | Enable/disable scanning of BZip2 compressed files.  Choices:   - `"enable"` - `"disable"` |
| **ssl_offloaded**  string | SSL decryption and encryption performed by an external device.  Choices:   - `"no"` - `"yes"` |
| **stream_based_uncompressed_limit**  integer | Maximum stream-based uncompressed data size that will be scanned in megabytes. Stream-based uncompression used only under certain conditions (unlimited = 0). |
| **tcp_window_maximum**  integer | Maximum dynamic TCP window size. |
| **tcp_window_minimum**  integer | Minimum dynamic TCP window size. |
| **tcp_window_size**  integer | Set TCP static window size. |
| **tcp_window_type**  string | TCP window type to use for this protocol.  Choices:   - `"auto-tuning"` - `"system"` - `"static"` - `"dynamic"` |
| **uncompressed_nest_limit**  integer | Maximum nested levels of compression that can be uncompressed and scanned (2 - 100). |
| **uncompressed_oversize_limit**  integer | Maximum in-memory uncompressed file size that can be scanned (1 - 383 MB). |
| **switching_protocols_log**  string | Enable/disable logging for HTTP/HTTPS switching protocols.  Choices:   - `"disable"` - `"enable"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_firewall_profile_protocol_options_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_profile_protocol_options_module.md#id5)

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
  - name: Configure protocol options.
    fortios_firewall_profile_protocol_options:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_profile_protocol_options:
        cifs:
            domain_controller: "<your_own_value> (source user.domain-controller.name credential-store.domain-controller.server-name)"
            options: "oversize"
            oversize_limit: "10"
            ports: "<your_own_value>"
            scan_bzip2: "enable"
            server_credential_type: "none"
            server_keytab:
             -
                keytab: "<your_own_value>"
                principal: "<your_own_value>"
            status: "enable"
            tcp_window_maximum: "8388608"
            tcp_window_minimum: "131072"
            tcp_window_size: "262144"
            tcp_window_type: "auto-tuning"
            uncompressed_nest_limit: "12"
            uncompressed_oversize_limit: "10"
        comment: "Optional comments."
        dns:
            ports: "<your_own_value>"
            status: "enable"
        ftp:
            comfort_amount: "1"
            comfort_interval: "10"
            explicit_ftp_tls: "enable"
            inspect_all: "enable"
            options: "clientcomfort"
            oversize_limit: "10"
            ports: "<your_own_value>"
            scan_bzip2: "enable"
            ssl_offloaded: "no"
            status: "enable"
            stream_based_uncompressed_limit: "0"
            tcp_window_maximum: "8388608"
            tcp_window_minimum: "131072"
            tcp_window_size: "262144"
            tcp_window_type: "auto-tuning"
            uncompressed_nest_limit: "12"
            uncompressed_oversize_limit: "10"
        http:
            address_ip_rating: "enable"
            block_page_status_code: "403"
            comfort_amount: "1"
            comfort_interval: "10"
            fortinet_bar: "enable"
            fortinet_bar_port: "32767"
            h2c: "enable"
            http_policy: "disable"
            inspect_all: "enable"
            options: "clientcomfort"
            oversize_limit: "10"
            ports: "<your_own_value>"
            post_lang: "jisx0201"
            proxy_after_tcp_handshake: "enable"
            range_block: "disable"
            retry_count: "0"
            scan_bzip2: "enable"
            ssl_offloaded: "no"
            status: "enable"
            stream_based_uncompressed_limit: "0"
            streaming_content_bypass: "enable"
            strip_x_forwarded_for: "disable"
            switching_protocols: "bypass"
            tcp_window_maximum: "8388608"
            tcp_window_minimum: "131072"
            tcp_window_size: "262144"
            tcp_window_type: "auto-tuning"
            tunnel_non_http: "enable"
            uncompressed_nest_limit: "12"
            uncompressed_oversize_limit: "10"
            unknown_http_version: "reject"
            verify_dns_for_policy_matching: "enable"
        imap:
            inspect_all: "enable"
            options: "fragmail"
            oversize_limit: "10"
            ports: "<your_own_value>"
            proxy_after_tcp_handshake: "enable"
            scan_bzip2: "enable"
            ssl_offloaded: "no"
            status: "enable"
            uncompressed_nest_limit: "12"
            uncompressed_oversize_limit: "10"
        mail_signature:
            signature: "<your_own_value>"
            status: "disable"
        mapi:
            options: "fragmail"
            oversize_limit: "10"
            ports: "<your_own_value>"
            scan_bzip2: "enable"
            status: "enable"
            uncompressed_nest_limit: "12"
            uncompressed_oversize_limit: "10"
        name: "default_name_97"
        nntp:
            inspect_all: "enable"
            options: "oversize"
            oversize_limit: "10"
            ports: "<your_own_value>"
            proxy_after_tcp_handshake: "enable"
            scan_bzip2: "enable"
            status: "enable"
            uncompressed_nest_limit: "12"
            uncompressed_oversize_limit: "10"
        oversize_log: "disable"
        pop3:
            inspect_all: "enable"
            options: "fragmail"
            oversize_limit: "10"
            ports: "<your_own_value>"
            proxy_after_tcp_handshake: "enable"
            scan_bzip2: "enable"
            ssl_offloaded: "no"
            status: "enable"
            uncompressed_nest_limit: "12"
            uncompressed_oversize_limit: "10"
        replacemsg_group: "<your_own_value> (source system.replacemsg-group.name)"
        rpc_over_http: "enable"
        smtp:
            inspect_all: "enable"
            options: "fragmail"
            oversize_limit: "10"
            ports: "<your_own_value>"
            proxy_after_tcp_handshake: "enable"
            scan_bzip2: "enable"
            server_busy: "enable"
            ssl_offloaded: "no"
            status: "enable"
            uncompressed_nest_limit: "12"
            uncompressed_oversize_limit: "10"
        ssh:
            comfort_amount: "1"
            comfort_interval: "10"
            options: "oversize"
            oversize_limit: "10"
            scan_bzip2: "enable"
            ssl_offloaded: "no"
            stream_based_uncompressed_limit: "0"
            tcp_window_maximum: "8388608"
            tcp_window_minimum: "131072"
            tcp_window_size: "262144"
            tcp_window_type: "auto-tuning"
            uncompressed_nest_limit: "12"
            uncompressed_oversize_limit: "10"
        switching_protocols_log: "disable"
```

## [Return Values](fortios_firewall_profile_protocol_options_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
