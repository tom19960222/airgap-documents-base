---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_asm_dos_application module – Manage application settings for a DOS profile"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_asm_dos_application_module.html
fetched_at: 2026-07-28T02:05:37+00:00
---
# f5networks.f5_modules.bigip_asm_dos_application module – Manage application settings for a DOS profile

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/ui/repo/published/f5networks/f5_modules/) (version 1.27.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_asm_dos_application`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_asm_dos_application_module.md#synopsis)
- [Parameters](bigip_asm_dos_application_module.md#parameters)
- [Notes](bigip_asm_dos_application_module.md#notes)
- [Examples](bigip_asm_dos_application_module.md#examples)
- [Return Values](bigip_asm_dos_application_module.md#return-values)

## [Synopsis](bigip_asm_dos_application_module.md#id1)

- Manages Application settings for an ASM/AFM DOS profile.

## [Parameters](bigip_asm_dos_application_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **geolocations**  dictionary | Manages the geolocations countries whitelist, blacklist. |
| **blacklist**  list / elements=string | A list of countries to be put on the blacklist, must not have overlapping elements with `whitelist`. |
| **whitelist**  list / elements=string | A list of countries to be put on the whitelist, must not have overlapping elements with `blacklist`. |
| **heavy_urls**  dictionary | Manages Heavy URL protection.  Heavy URLs are a small number of site URLs that might consume considerable server resources per request. |
| **auto_detect**  boolean | Enables or disables automatic heavy URL detection.  **Choices:**   - `false` - `true` |
| **exclude**  list / elements=string | Specifies a list of URLs or wildcards to exclude from the heavy URLs. |
| **include**  list / elements=dictionary | Configures additional URLs to include in the heavy URLs that were auto-detected. |
| **threshold**  string | Specifies the threshold of requests per second, where the URL in question is considered under attack.  The acceptable range is between 1 and 4294967295 inclusive, or `auto`. |
| **url**  string / required | Specifies the URL to be added to the list of heavy URLs, in addition to those automatically detected. |
| **latency_threshold**  integer | Specifies the latency threshold for automatic heavy URL detection.  The acceptable range is between 0 and 4294967295 miliseconds inclusive. |
| **mobile_detection**  dictionary | Configures detection of mobile applications built with the Anti-Bot Mobile SDK and defines how requests from these mobile application clients are handled. |
| **allow_android_rooted_device**  boolean | When `true`, the device allows traffic from rooted Android devices.  **Choices:**   - `false` - `true` |
| **allow_any_android_package**  boolean | When `true`, allows any application publisher.  A publisher is identified by the certificate used to sign the application.  **Choices:**   - `false` - `true` |
| **allow_any_ios_package**  boolean | When `true`, allows any iOS package.  A package name is the unique identifier of the mobile application.  **Choices:**   - `false` - `true` |
| **allow_emulators**  boolean | When `true`, allows traffic from applications run on emulators.  **Choices:**   - `false` - `true` |
| **allow_jailbroken_devices**  boolean | When `true`, allows traffic from jailbroken iOS devices.  **Choices:**   - `false` - `true` |
| **android_publishers**  list / elements=string | This option has no effect when `allow_any_android_package` is set to `true`.  Specifies the allowed publisher certificates for android applications.  The publisher certificate needs to be installed on the BIG-IP beforehand.  The certificate name located on a different partition than the one specified in the `partition` parameter needs to be provided in `full_path` format, e.g. `/Foo/cert.crt`. |
| **client_side_challenge_mode**  string | Action to take when a CAPTCHA or Client Side Integrity challenge needs to be presented.  The mobile application user will not see a CAPTCHA challenge and the mobile application will not be presented with the Client Side Integrity challenge. The such options for mobile applications are `pass` or `cshui`.  When `pass` the traffic is passed without incident.  When `cshui` the SDK checks for human interactions with the screen in the last few seconds. If none are detected, the traffic is blocked.  **Choices:**   - `"pass"` - `"cshui"` |
| **enabled**  boolean | When `true`, requests from mobile applications built with Anti-Bot Mobile SDK are detected and handled according to the parameters set.  When `false`, these requests are handled like any other request which may let attacks in, or cause false positives.  **Choices:**   - `false` - `true` |
| **ios_allowed_package_names**  list / elements=string | Specifies the names of iOS packages to allow traffic on.  This option has no effect when `allow_any_ios_package` is set to `true`. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **profile**  string / required | Specifies the name of the profile to manage application settings in. |
| **provider**  dictionary  *added in f5networks.f5_modules 1.0.0* | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  **Choices:**   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP or the BIG-IQ.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host or the BIG-IQ host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  **Default:** `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  **Choices:**   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP or the BIG-IQ. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  **Choices:**   - `false` - `true` ← (default) |
| **rtbh_duration**  integer | Specifies the duration of the RTBH BGP route advertisement, in seconds.  The acceptable range is between 0 and 4294967295 inclusive. |
| **rtbh_enable**  boolean | Specifies whether to enable Remote Triggered Black Hole `RTBH` of attacking IPs by advertising BGP routes.  **Choices:**   - `false` - `true` |
| **scrubbing_duration**  integer | Specifies the duration of the Traffic Scrubbing BGP route advertisement, in seconds.  The acceptable range is between 0 and 4294967295 inclusive. |
| **scrubbing_enable**  boolean | Specifies whether to enable Traffic Scrubbing during attacks by advertising BGP routes.  **Choices:**   - `false` - `true` |
| **single_page_application**  boolean | When `true`, specifies the system supports a Single Page Applications.  **Choices:**   - `false` - `true` |
| **state**  string | When `state` is `present`, ensures that the Application object exists.  When `state` is `absent`, ensures that the Application object is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **trigger_irule**  boolean | When `true`, specifies the system activates an Application DoS iRule event.  **Choices:**   - `false` - `true` |

## [Notes](bigip_asm_dos_application_module.md#id3)

> **Note:**
>
> - Requires BIG-IP >= 13.1.0
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_asm_dos_application_module.md#id4)

```yaml+jinja
- name: Create an ASM dos application profile
  bigip_asm_dos_application:
    profile: dos_foo
    geolocations:
      blacklist:
        - Afghanistan
        - Andora
      whitelist:
        - Cuba
    heavy_urls:
      auto_detect: true
      latency_threshold: 1000
    rtbh_duration: 3600
    rtbh_enable: true
    single_page_application: true
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Update an ASM dos application profile
  bigip_asm_dos_application:
    profile: dos_foo
    mobile_detection:
      enabled: true
      allow_any_ios_package: true
      allow_emulators: true
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove an ASM dos application profile
  bigip_asm_dos_application:
    profile: dos_foo
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_asm_dos_application_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **geolocations**  complex | Specifies geolocations countries whitelist, blacklist.  **Returned:** changed  **Sample:** `"hash/dictionary of values"` |
| **blacklist**  list / elements=string | A list of countries to be put on the blacklist.  **Returned:** changed  **Sample:** `["Russia", "Germany"]` |
| **whitelist**  list / elements=string | A list of countries to be put on the whitelist.  **Returned:** changed  **Sample:** `["United States, United Kingdom"]` |
| **heavy_urls**  complex | Manages Heavy URL protection.  **Returned:** changed  **Sample:** `"hash/dictionary of values"` |
| **auto_detect**  boolean | Enables or disables automatic heavy URL detection.  **Returned:** changed  **Sample:** `true` |
| **exclude**  list / elements=string | Specifies a list of URLs or wildcards to exclude from the heavy URLs.  **Returned:** changed  **Sample:** `["/exclude.html", "/exclude2.html"]` |
| **include**  complex | Configures additional URLs to include in the heavy URLs.  **Returned:** changed  **Sample:** `"hash/dictionary of values"` |
| **threshold**  string | The threshold of requests per second.  **Returned:** changed  **Sample:** `"auto"` |
| **url**  string | The URL to be added to the list of heavy URLs.  **Returned:** changed  **Sample:** `"/include.html"` |
| **latency_threshold**  integer | Specifies the latency threshold for automatic heavy URL detection.  **Returned:** changed  **Sample:** `2000` |
| **mobile_detection**  complex | Configures detection of mobile applications built with the Anti-Bot Mobile SDK.  **Returned:** changed  **Sample:** `"hash/dictionary of values"` |
| **allow_android_rooted_device**  boolean | Allows traffic from rooted Android devices.  **Returned:** changed  **Sample:** `false` |
| **allow_any_android_package**  boolean | Allows any application publisher.  **Returned:** changed  **Sample:** `false` |
| **allow_any_ios_package**  boolean | Allows any iOS package.  **Returned:** changed  **Sample:** `true` |
| **allow_emulators**  boolean | Allows traffic from applications run on emulators.  **Returned:** changed  **Sample:** `true` |
| **allow_jailbroken_devices**  boolean | Allows traffic from jailbroken iOS devices.  **Returned:** changed  **Sample:** `false` |
| **android_publishers**  list / elements=string | The allowed publisher certificates for android applications.  **Returned:** changed  **Sample:** `["/Common/cert1.crt", "/Common/cert2.crt"]` |
| **client_side_challenge_mode**  string | Action to take when a CAPTCHA or Client Side Integrity challenge needs to be presented.  **Returned:** changed  **Sample:** `"pass"` |
| **enable**  boolean | Enables or disables automatic mobile detection.  **Returned:** changed  **Sample:** `true` |
| **ios_allowed_package_names**  list / elements=string | The names of iOS packages to allow traffic on.  **Returned:** changed  **Sample:** `["package1", "package2"]` |
| **rtbh_duration**  integer | The duration of the RTBH BGP route advertisement.  **Returned:** changed  **Sample:** `3600` |
| **rtbh_enable**  boolean | Enables Remote Triggered Black Hole of attacking IPs.  **Returned:** changed  **Sample:** `false` |
| **scrubbing_duration**  integer | The duration of the Traffic Scrubbing BGP route advertisement.  **Returned:** changed  **Sample:** `3600` |
| **scrubbing_enable**  boolean | Enables Traffic Scrubbing during attacks.  **Returned:** changed  **Sample:** `true` |
| **single_page_application**  boolean | Enables support of Single Page Applications.  **Returned:** changed  **Sample:** `false` |
| **trigger_irule**  boolean | Activates an Application DoS iRule event.  **Returned:** changed  **Sample:** `true` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
