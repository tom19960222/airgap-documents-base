---
collection: ansible
version: "8"
title: "community.general.manageiq_provider module – Management of provider in ManageIQ"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/manageiq_provider_module.html
fetched_at: 2026-07-28T01:47:49+00:00
---
# community.general.manageiq_provider module – Management of provider in ManageIQ

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](manageiq_provider_module.md#ansible-collections-community-general-manageiq-provider-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.manageiq_provider`.

- [Synopsis](manageiq_provider_module.md#synopsis)
- [Requirements](manageiq_provider_module.md#requirements)
- [Parameters](manageiq_provider_module.md#parameters)
- [Attributes](manageiq_provider_module.md#attributes)
- [Examples](manageiq_provider_module.md#examples)

## [Synopsis](manageiq_provider_module.md#id1)

- The manageiq_provider module supports adding, updating, and deleting provider in ManageIQ.

Aliases: remote_management.manageiq.manageiq_provider

## [Requirements](manageiq_provider_module.md#id2)

The below requirements are needed on the host that executes this module.

- manageiq-client <https://github.com/ManageIQ/manageiq-api-client-python/>

## [Parameters](manageiq_provider_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **alerts**  string | Alerts endpoint connection information. |
| **auth_key**  string | Provider’s api endpoint authentication bearer token. defaults to None. |
| **certificate_authority**  string | The CA bundle string with custom certificates. defaults to None. |
| **hostname**  string / required | The provider’s api hostname. |
| **password**  string | Provider’s api endpoint authentication password. defaults to None. |
| **port**  integer | The provider’s api port. |
| **security_protocol**  string | How SSL certificates should be used for HTTPS requests. defaults to None.  **Choices:**   - `"ssl-with-validation"` - `"ssl-with-validation-custom-ca"` - `"ssl-without-validation"` - `"non-ssl"` |
| **userid**  string | Provider’s api endpoint authentication userid. defaults to None. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether SSL certificates should be verified for HTTPS requests (deprecated). defaults to True.  **Choices:**   - `false` - `true` ← (default) |
| **api_version**  string | The OpenStack Keystone API version. defaults to None.  **Choices:**   - `"v2"` - `"v3"` |
| **azure_tenant_id**  aliases: keystone_v3_domain_id  string | Tenant ID. defaults to None. |
| **host_default_vnc_port_end**  string | The last port in the host VNC range. defaults to None. |
| **host_default_vnc_port_start**  string | The first port in the host VNC range. defaults to None. |
| **manageiq_connection**  dictionary | ManageIQ connection configuration information. |
| **ca_cert**  aliases: ca_bundle_path  string | The path to a CA bundle file or directory with certificates. |
| **password**  string | ManageIQ password. `MIQ_PASSWORD` environment variable if set. Otherwise, required if no token is passed in. |
| **token**  string | ManageIQ token. `MIQ_TOKEN` environment variable if set. Otherwise, required if no username or password is passed in. |
| **url**  string | ManageIQ environment URL. `MIQ_URL` environment variable if set. Otherwise, it is required to pass it. |
| **username**  string | ManageIQ username. `MIQ_USERNAME` environment variable if set. Otherwise, required if no token is passed in. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether SSL certificates should be verified for HTTPS requests.  **Choices:**   - `false` - `true` ← (default) |
| **metrics**  string | Metrics endpoint connection information. |
| **auth_key**  string | Provider’s api endpoint authentication bearer token. defaults to None. |
| **certificate_authority**  string | The CA bundle string with custom certificates. defaults to None. |
| **hostname**  string / required | The provider’s api hostname. |
| **password**  string | Provider’s api endpoint authentication password. defaults to None. |
| **path**  string | Database name for oVirt metrics. Defaults to `ovirt_engine_history`. |
| **port**  integer | The provider’s api port. |
| **security_protocol**  string | How SSL certificates should be used for HTTPS requests. defaults to None.  **Choices:**   - `"ssl-with-validation"` - `"ssl-with-validation-custom-ca"` - `"ssl-without-validation"` - `"non-ssl"` |
| **userid**  string | Provider’s api endpoint authentication userid. defaults to None. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether SSL certificates should be verified for HTTPS requests (deprecated). defaults to True.  **Choices:**   - `false` - `true` ← (default) |
| **name**  string / required | The provider’s name. |
| **project**  string | Google Compute Engine Project ID. defaults to None. |
| **provider**  string | Default endpoint connection information, required if state is true. |
| **auth_key**  string | Provider’s api endpoint authentication bearer token. defaults to None. |
| **certificate_authority**  string | The CA bundle string with custom certificates. defaults to None. |
| **hostname**  string / required | The provider’s api hostname. |
| **password**  string | Provider’s api endpoint authentication password. defaults to None. |
| **port**  integer | The provider’s api port. |
| **security_protocol**  string | How SSL certificates should be used for HTTPS requests. defaults to None.  **Choices:**   - `"ssl-with-validation"` - `"ssl-with-validation-custom-ca"` - `"ssl-without-validation"` - `"non-ssl"` |
| **userid**  string | Provider’s api endpoint authentication userid. defaults to None. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether SSL certificates should be verified for HTTPS requests (deprecated). defaults to True.  **Choices:**   - `false` - `true` ← (default) |
| **provider_region**  string | The provider region name to connect to (e.g. AWS region for Amazon). |
| **ssh_keypair**  string | SSH key pair used for SSH connections to all hosts in this provider. |
| **auth_key**  string | SSH private key. |
| **hostname**  string / required | Director hostname. |
| **userid**  string | SSH username. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether certificates should be verified for connections.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | absent - provider should not exist, present - provider should be present, refresh - provider will be refreshed  **Choices:**   - `"absent"` - `"present"` ← (default) - `"refresh"` |
| **subscription**  string | Microsoft Azure subscription ID. defaults to None. |
| **tenant_mapping_enabled**  boolean | Whether to enable mapping of existing tenants. defaults to False.  **Choices:**   - `false` ← (default) - `true` |
| **type**  string | The provider’s type.  **Choices:**   - `"Openshift"` - `"Amazon"` - `"oVirt"` - `"VMware"` - `"Azure"` - `"Director"` - `"OpenStack"` - `"GCE"` |
| **zone**  string | The ManageIQ zone name that will manage the provider.  **Default:** `"default"` |

## [Attributes](manageiq_provider_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](manageiq_provider_module.md#id5)

```yaml+jinja
- name: Create a new provider in ManageIQ ('Hawkular' metrics)
  community.general.manageiq_provider:
    name: 'EngLab'
    type: 'OpenShift'
    state: 'present'
    provider:
      auth_key: 'topSecret'
      hostname: 'example.com'
      port: 8443
      validate_certs: true
      security_protocol: 'ssl-with-validation-custom-ca'
      certificate_authority: |
        -----BEGIN CERTIFICATE-----
        FAKECERTsdKgAwIBAgIBATANBgkqhkiG9w0BAQsFADAmMSQwIgYDVQQDDBtvcGVu
        c2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkwHhcNMTcwODIxMTI1NTE5WhcNMjIwODIw
        MTI1NTIwWjAmMSQwIgYDVQQDDBtvcGVuc2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkw
        ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUDnL2tQ2xf/zO7F7hmZ4S
        ZuwKENdI4IYuWSxye4i3hPhKg6eKPzGzmDNWkIMDOrDAj1EgVSNPtPwsOL8OWvJm
        AaTjr070D7ZGWWnrrDrWEClBx9Rx/6JAM38RT8Pu7c1hXBm0J81KufSLLYiZ/gOw
        Znks5v5RUSGcAXvLkBJeATbsbh6fKX0RgQ3fFTvqQaE/r8LxcTN1uehPX1g5AaRa
        z/SNDHaFtQlE3XcqAAukyMn4N5kdNcuwF3GlQ+tJnJv8SstPkfQcZbTMUQ7I2KpJ
        ajXnMxmBhV5fCN4rb0QUNCrk2/B+EUMBY4MnxIakqNxnN1kvgI7FBbFgrHUe6QvJ
        AgMBAAGjIzAhMA4GA1UdDwEB/wQEAwICpDAPBgNVHRMBAf8EBTADAQH/MA0GCSqG
        SIb3DQEBCwUAA4IBAQAYRV57LUsqznSLZHA77o9+0fQetIE115DYP7wea42PODJI
        QJ+JETEfoCr0+YOMAbVmznP9GH5cMTKEWHExcIpbMBU7nMZp6A3htcJgF2fgPzOA
        aTUtzkuVCSrV//mbbYVxoFOc6sR3Br0wBs5+5iz3dBSt7xmgpMzZvqsQl655i051
        gGSTIY3z5EJmBZBjwuTjal9mMoPGA4eoTPqlITJDHQ2bdCV2oDbc7zqupGrUfZFA
        qzgieEyGzdCSRwjr1/PibA3bpwHyhD9CGD0PRVVTLhw6h6L5kuN1jA20OfzWxf/o
        XUsdmRaWiF+l4s6Dcd56SuRp5SGNa2+vP9Of/FX5
        -----END CERTIFICATE-----
    metrics:
      auth_key: 'topSecret'
      role: 'hawkular'
      hostname: 'example.com'
      port: 443
      validate_certs: true
      security_protocol: 'ssl-with-validation-custom-ca'
      certificate_authority: |
        -----BEGIN CERTIFICATE-----
        FAKECERTsdKgAwIBAgIBATANBgkqhkiG9w0BAQsFADAmMSQwIgYDVQQDDBtvcGVu
        c2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkwHhcNMTcwODIxMTI1NTE5WhcNMjIwODIw
        MTI1NTIwWjAmMSQwIgYDVQQDDBtvcGVuc2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkw
        ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUDnL2tQ2xf/zO7F7hmZ4S
        ZuwKENdI4IYuWSxye4i3hPhKg6eKPzGzmDNWkIMDOrDAj1EgVSNPtPwsOL8OWvJm
        AaTjr070D7ZGWWnrrDrWEClBx9Rx/6JAM38RT8Pu7c1hXBm0J81KufSLLYiZ/gOw
        Znks5v5RUSGcAXvLkBJeATbsbh6fKX0RgQ3fFTvqQaE/r8LxcTN1uehPX1g5AaRa
        z/SNDHaFtQlE3XcqAAukyMn4N5kdNcuwF3GlQ+tJnJv8SstPkfQcZbTMUQ7I2KpJ
        ajXnMxmBhV5fCN4rb0QUNCrk2/B+EUMBY4MnxIakqNxnN1kvgI7FBbFgrHUe6QvJ
        AgMBAAGjIzAhMA4GA1UdDwEB/wQEAwICpDAPBgNVHRMBAf8EBTADAQH/MA0GCSqG
        SIb3DQEBCwUAA4IBAQAYRV57LUsqznSLZHA77o9+0fQetIE115DYP7wea42PODJI
        QJ+JETEfoCr0+YOMAbVmznP9GH5cMTKEWHExcIpbMBU7nMZp6A3htcJgF2fgPzOA
        aTUtzkuVCSrV//mbbYVxoFOc6sR3Br0wBs5+5iz3dBSt7xmgpMzZvqsQl655i051
        gGSTIY3z5EJmBZBjwuTjal9mMoPGA4eoTPqlITJDHQ2bdCV2oDbc7zqupGrUfZFA
        qzgieEyGzdCSRwjr1/PibA3bpwHyhD9CGD0PRVVTLhw6h6L5kuN1jA20OfzWxf/o
        XUsdmRaWiF+l4s6Dcd56SuRp5SGNa2+vP9Of/FX5
        -----END CERTIFICATE-----
    manageiq_connection:
      url: 'https://127.0.0.1:80'
      username: 'admin'
      password: 'password'
      validate_certs: true

- name: Update an existing provider named 'EngLab' (defaults to 'Prometheus' metrics)
  community.general.manageiq_provider:
    name: 'EngLab'
    type: 'Openshift'
    state: 'present'
    provider:
      auth_key: 'topSecret'
      hostname: 'next.example.com'
      port: 8443
      validate_certs: true
      security_protocol: 'ssl-with-validation-custom-ca'
      certificate_authority: |
        -----BEGIN CERTIFICATE-----
        FAKECERTsdKgAwIBAgIBATANBgkqhkiG9w0BAQsFADAmMSQwIgYDVQQDDBtvcGVu
        c2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkwHhcNMTcwODIxMTI1NTE5WhcNMjIwODIw
        MTI1NTIwWjAmMSQwIgYDVQQDDBtvcGVuc2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkw
        ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUDnL2tQ2xf/zO7F7hmZ4S
        ZuwKENdI4IYuWSxye4i3hPhKg6eKPzGzmDNWkIMDOrDAj1EgVSNPtPwsOL8OWvJm
        AaTjr070D7ZGWWnrrDrWEClBx9Rx/6JAM38RT8Pu7c1hXBm0J81KufSLLYiZ/gOw
        Znks5v5RUSGcAXvLkBJeATbsbh6fKX0RgQ3fFTvqQaE/r8LxcTN1uehPX1g5AaRa
        z/SNDHaFtQlE3XcqAAukyMn4N5kdNcuwF3GlQ+tJnJv8SstPkfQcZbTMUQ7I2KpJ
        ajXnMxmBhV5fCN4rb0QUNCrk2/B+EUMBY4MnxIakqNxnN1kvgI7FBbFgrHUe6QvJ
        AgMBAAGjIzAhMA4GA1UdDwEB/wQEAwICpDAPBgNVHRMBAf8EBTADAQH/MA0GCSqG
        SIb3DQEBCwUAA4IBAQAYRV57LUsqznSLZHA77o9+0fQetIE115DYP7wea42PODJI
        QJ+JETEfoCr0+YOMAbVmznP9GH5cMTKEWHExcIpbMBU7nMZp6A3htcJgF2fgPzOA
        aTUtzkuVCSrV//mbbYVxoFOc6sR3Br0wBs5+5iz3dBSt7xmgpMzZvqsQl655i051
        gGSTIY3z5EJmBZBjwuTjal9mMoPGA4eoTPqlITJDHQ2bdCV2oDbc7zqupGrUfZFA
        qzgieEyGzdCSRwjr1/PibA3bpwHyhD9CGD0PRVVTLhw6h6L5kuN1jA20OfzWxf/o
        XUsdmRaWiF+l4s6Dcd56SuRp5SGNa2+vP9Of/FX5
        -----END CERTIFICATE-----
    metrics:
      auth_key: 'topSecret'
      hostname: 'next.example.com'
      port: 443
      validate_certs: true
      security_protocol: 'ssl-with-validation-custom-ca'
      certificate_authority: |
        -----BEGIN CERTIFICATE-----
        FAKECERTsdKgAwIBAgIBATANBgkqhkiG9w0BAQsFADAmMSQwIgYDVQQDDBtvcGVu
        c2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkwHhcNMTcwODIxMTI1NTE5WhcNMjIwODIw
        MTI1NTIwWjAmMSQwIgYDVQQDDBtvcGVuc2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkw
        ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUDnL2tQ2xf/zO7F7hmZ4S
        ZuwKENdI4IYuWSxye4i3hPhKg6eKPzGzmDNWkIMDOrDAj1EgVSNPtPwsOL8OWvJm
        AaTjr070D7ZGWWnrrDrWEClBx9Rx/6JAM38RT8Pu7c1hXBm0J81KufSLLYiZ/gOw
        Znks5v5RUSGcAXvLkBJeATbsbh6fKX0RgQ3fFTvqQaE/r8LxcTN1uehPX1g5AaRa
        z/SNDHaFtQlE3XcqAAukyMn4N5kdNcuwF3GlQ+tJnJv8SstPkfQcZbTMUQ7I2KpJ
        ajXnMxmBhV5fCN4rb0QUNCrk2/B+EUMBY4MnxIakqNxnN1kvgI7FBbFgrHUe6QvJ
        AgMBAAGjIzAhMA4GA1UdDwEB/wQEAwICpDAPBgNVHRMBAf8EBTADAQH/MA0GCSqG
        SIb3DQEBCwUAA4IBAQAYRV57LUsqznSLZHA77o9+0fQetIE115DYP7wea42PODJI
        QJ+JETEfoCr0+YOMAbVmznP9GH5cMTKEWHExcIpbMBU7nMZp6A3htcJgF2fgPzOA
        aTUtzkuVCSrV//mbbYVxoFOc6sR3Br0wBs5+5iz3dBSt7xmgpMzZvqsQl655i051
        gGSTIY3z5EJmBZBjwuTjal9mMoPGA4eoTPqlITJDHQ2bdCV2oDbc7zqupGrUfZFA
        qzgieEyGzdCSRwjr1/PibA3bpwHyhD9CGD0PRVVTLhw6h6L5kuN1jA20OfzWxf/o
        XUsdmRaWiF+l4s6Dcd56SuRp5SGNa2+vP9Of/FX5
        -----END CERTIFICATE-----
    manageiq_connection:
      url: 'https://127.0.0.1'
      username: 'admin'
      password: 'password'
      validate_certs: true

- name: Delete a provider in ManageIQ
  community.general.manageiq_provider:
    name: 'EngLab'
    type: 'Openshift'
    state: 'absent'
    manageiq_connection:
      url: 'https://127.0.0.1'
      username: 'admin'
      password: 'password'
      validate_certs: true

- name: Create a new Amazon provider in ManageIQ using token authentication
  community.general.manageiq_provider:
    name: 'EngAmazon'
    type: 'Amazon'
    state: 'present'
    provider:
      hostname: 'amazon.example.com'
      userid: 'hello'
      password: 'world'
    manageiq_connection:
      url: 'https://127.0.0.1'
      token: 'VeryLongToken'
      validate_certs: true

- name: Create a new oVirt provider in ManageIQ
  community.general.manageiq_provider:
    name: 'RHEV'
    type: 'oVirt'
    state: 'present'
    provider:
      hostname: 'rhev01.example.com'
      userid: 'admin@internal'
      password: 'password'
      validate_certs: true
      certificate_authority: |
        -----BEGIN CERTIFICATE-----
        FAKECERTsdKgAwIBAgIBATANBgkqhkiG9w0BAQsFADAmMSQwIgYDVQQDDBtvcGVu
        c2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkwHhcNMTcwODIxMTI1NTE5WhcNMjIwODIw
        MTI1NTIwWjAmMSQwIgYDVQQDDBtvcGVuc2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkw
        ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUDnL2tQ2xf/zO7F7hmZ4S
        ZuwKENdI4IYuWSxye4i3hPhKg6eKPzGzmDNWkIMDOrDAj1EgVSNPtPwsOL8OWvJm
        AaTjr070D7ZGWWnrrDrWEClBx9Rx/6JAM38RT8Pu7c1hXBm0J81KufSLLYiZ/gOw
        Znks5v5RUSGcAXvLkBJeATbsbh6fKX0RgQ3fFTvqQaE/r8LxcTN1uehPX1g5AaRa
        z/SNDHaFtQlE3XcqAAukyMn4N5kdNcuwF3GlQ+tJnJv8SstPkfQcZbTMUQ7I2KpJ
        ajXnMxmBhV5fCN4rb0QUNCrk2/B+EUMBY4MnxIakqNxnN1kvgI7FBbFgrHUe6QvJ
        AgMBAAGjIzAhMA4GA1UdDwEB/wQEAwICpDAPBgNVHRMBAf8EBTADAQH/MA0GCSqG
        SIb3DQEBCwUAA4IBAQAYRV57LUsqznSLZHA77o9+0fQetIE115DYP7wea42PODJI
        QJ+JETEfoCr0+YOMAbVmznP9GH5cMTKEWHExcIpbMBU7nMZp6A3htcJgF2fgPzOA
        aTUtzkuVCSrV//mbbYVxoFOc6sR3Br0wBs5+5iz3dBSt7xmgpMzZvqsQl655i051
        gGSTIY3z5EJmBZBjwuTjal9mMoPGA4eoTPqlITJDHQ2bdCV2oDbc7zqupGrUfZFA
        qzgieEyGzdCSRwjr1/PibA3bpwHyhD9CGD0PRVVTLhw6h6L5kuN1jA20OfzWxf/o
        XUsdmRaWiF+l4s6Dcd56SuRp5SGNa2+vP9Of/FX5
        -----END CERTIFICATE-----
    metrics:
      hostname: 'metrics.example.com'
      path: 'ovirt_engine_history'
      userid: 'user_id_metrics'
      password: 'password_metrics'
      validate_certs: true
      certificate_authority: |
        -----BEGIN CERTIFICATE-----
        FAKECERTsdKgAwIBAgIBATANBgkqhkiG9w0BAQsFADAmMSQwIgYDVQQDDBtvcGVu
        c2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkwHhcNMTcwODIxMTI1NTE5WhcNMjIwODIw
        MTI1NTIwWjAmMSQwIgYDVQQDDBtvcGVuc2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkw
        ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUDnL2tQ2xf/zO7F7hmZ4S
        ZuwKENdI4IYuWSxye4i3hPhKg6eKPzGzmDNWkIMDOrDAj1EgVSNPtPwsOL8OWvJm
        AaTjr070D7ZGWWnrrDrWEClBx9Rx/6JAM38RT8Pu7c1hXBm0J81KufSLLYiZ/gOw
        Znks5v5RUSGcAXvLkBJeATbsbh6fKX0RgQ3fFTvqQaE/r8LxcTN1uehPX1g5AaRa
        z/SNDHaFtQlE3XcqAAukyMn4N5kdNcuwF3GlQ+tJnJv8SstPkfQcZbTMUQ7I2KpJ
        ajXnMxmBhV5fCN4rb0QUNCrk2/B+EUMBY4MnxIakqNxnN1kvgI7FBbFgrHUe6QvJ
        AgMBAAGjIzAhMA4GA1UdDwEB/wQEAwICpDAPBgNVHRMBAf8EBTADAQH/MA0GCSqG
        SIb3DQEBCwUAA4IBAQAYRV57LUsqznSLZHA77o9+0fQetIE115DYP7wea42PODJI
        QJ+JETEfoCr0+YOMAbVmznP9GH5cMTKEWHExcIpbMBU7nMZp6A3htcJgF2fgPzOA
        aTUtzkuVCSrV//mbbYVxoFOc6sR3Br0wBs5+5iz3dBSt7xmgpMzZvqsQl655i051
        gGSTIY3z5EJmBZBjwuTjal9mMoPGA4eoTPqlITJDHQ2bdCV2oDbc7zqupGrUfZFA
        qzgieEyGzdCSRwjr1/PibA3bpwHyhD9CGD0PRVVTLhw6h6L5kuN1jA20OfzWxf/o
        XUsdmRaWiF+l4s6Dcd56SuRp5SGNa2+vP9Of/FX5
        -----END CERTIFICATE-----
    manageiq_connection:
      url: 'https://127.0.0.1'
      username: 'admin'
      password: 'password'
      validate_certs: true

- name: Create a new VMware provider in ManageIQ
  community.general.manageiq_provider:
    name: 'EngVMware'
    type: 'VMware'
    state: 'present'
    provider:
      hostname: 'vcenter.example.com'
      host_default_vnc_port_start: 5800
      host_default_vnc_port_end: 5801
      userid: 'root'
      password: 'password'
    manageiq_connection:
      url: 'https://127.0.0.1'
      token: 'VeryLongToken'
      validate_certs: true

- name: Create a new Azure provider in ManageIQ
  community.general.manageiq_provider:
    name: 'EngAzure'
    type: 'Azure'
    provider_region: 'northeurope'
    subscription: 'e272bd74-f661-484f-b223-88dd128a4049'
    azure_tenant_id: 'e272bd74-f661-484f-b223-88dd128a4048'
    state: 'present'
    provider:
      hostname: 'azure.example.com'
      userid: 'e272bd74-f661-484f-b223-88dd128a4049'
      password: 'password'
    manageiq_connection:
      url: 'https://cf-6af0.rhpds.opentlc.com'
      username: 'admin'
      password: 'password'
      validate_certs: false

- name: Create a new OpenStack Director provider in ManageIQ with rsa keypair
  community.general.manageiq_provider:
    name: 'EngDirector'
    type: 'Director'
    api_version: 'v3'
    state: 'present'
    provider:
      hostname: 'director.example.com'
      userid: 'admin'
      password: 'password'
      security_protocol: 'ssl-with-validation'
      validate_certs: 'true'
      certificate_authority: |
        -----BEGIN CERTIFICATE-----
        FAKECERTsdKgAwIBAgIBATANBgkqhkiG9w0BAQsFADAmMSQwIgYDVQQDDBtvcGVu
        c2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkwHhcNMTcwODIxMTI1NTE5WhcNMjIwODIw
        MTI1NTIwWjAmMSQwIgYDVQQDDBtvcGVuc2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkw
        ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUDnL2tQ2xf/zO7F7hmZ4S
        ZuwKENdI4IYuWSxye4i3hPhKg6eKPzGzmDNWkIMDOrDAj1EgVSNPtPwsOL8OWvJm
        AaTjr070D7ZGWWnrrDrWEClBx9Rx/6JAM38RT8Pu7c1hXBm0J81KufSLLYiZ/gOw
        Znks5v5RUSGcAXvLkBJeATbsbh6fKX0RgQ3fFTvqQaE/r8LxcTN1uehPX1g5AaRa
        z/SNDHaFtQlE3XcqAAukyMn4N5kdNcuwF3GlQ+tJnJv8SstPkfQcZbTMUQ7I2KpJ
        ajXnMxmBhV5fCN4rb0QUNCrk2/B+EUMBY4MnxIakqNxnN1kvgI7FBbFgrHUe6QvJ
        AgMBAAGjIzAhMA4GA1UdDwEB/wQEAwICpDAPBgNVHRMBAf8EBTADAQH/MA0GCSqG
        SIb3DQEBCwUAA4IBAQAYRV57LUsqznSLZHA77o9+0fQetIE115DYP7wea42PODJI
        QJ+JETEfoCr0+YOMAbVmznP9GH5cMTKEWHExcIpbMBU7nMZp6A3htcJgF2fgPzOA
        aTUtzkuVCSrV//mbbYVxoFOc6sR3Br0wBs5+5iz3dBSt7xmgpMzZvqsQl655i051
        gGSTIY3z5EJmBZBjwuTjal9mMoPGA4eoTPqlITJDHQ2bdCV2oDbc7zqupGrUfZFA
        qzgieEyGzdCSRwjr1/PibA3bpwHyhD9CGD0PRVVTLhw6h6L5kuN1jA20OfzWxf/o
        XUsdmRaWiF+l4s6Dcd56SuRp5SGNa2+vP9Of/FX5
        -----END CERTIFICATE-----
    ssh_keypair:
      hostname: director.example.com
      userid: heat-admin
      auth_key: 'SecretSSHPrivateKey'

- name: Create a new OpenStack provider in ManageIQ with amqp metrics
  community.general.manageiq_provider:
    name: 'EngOpenStack'
    type: 'OpenStack'
    api_version: 'v3'
    state: 'present'
    provider_region: 'europe'
    tenant_mapping_enabled: 'False'
    keystone_v3_domain_id: 'mydomain'
    provider:
      hostname: 'openstack.example.com'
      userid: 'admin'
      password: 'password'
      security_protocol: 'ssl-with-validation'
      validate_certs: 'true'
      certificate_authority: |
        -----BEGIN CERTIFICATE-----
        FAKECERTsdKgAwIBAgIBATANBgkqhkiG9w0BAQsFADAmMSQwIgYDVQQDDBtvcGVu
        c2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkwHhcNMTcwODIxMTI1NTE5WhcNMjIwODIw
        MTI1NTIwWjAmMSQwIgYDVQQDDBtvcGVuc2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkw
        ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUDnL2tQ2xf/zO7F7hmZ4S
        ZuwKENdI4IYuWSxye4i3hPhKg6eKPzGzmDNWkIMDOrDAj1EgVSNPtPwsOL8OWvJm
        AaTjr070D7ZGWWnrrDrWEClBx9Rx/6JAM38RT8Pu7c1hXBm0J81KufSLLYiZ/gOw
        Znks5v5RUSGcAXvLkBJeATbsbh6fKX0RgQ3fFTvqQaE/r8LxcTN1uehPX1g5AaRa
        z/SNDHaFtQlE3XcqAAukyMn4N5kdNcuwF3GlQ+tJnJv8SstPkfQcZbTMUQ7I2KpJ
        ajXnMxmBhV5fCN4rb0QUNCrk2/B+EUMBY4MnxIakqNxnN1kvgI7FBbFgrHUe6QvJ
        AgMBAAGjIzAhMA4GA1UdDwEB/wQEAwICpDAPBgNVHRMBAf8EBTADAQH/MA0GCSqG
        SIb3DQEBCwUAA4IBAQAYRV57LUsqznSLZHA77o9+0fQetIE115DYP7wea42PODJI
        QJ+JETEfoCr0+YOMAbVmznP9GH5cMTKEWHExcIpbMBU7nMZp6A3htcJgF2fgPzOA
        aTUtzkuVCSrV//mbbYVxoFOc6sR3Br0wBs5+5iz3dBSt7xmgpMzZvqsQl655i051
        gGSTIY3z5EJmBZBjwuTjal9mMoPGA4eoTPqlITJDHQ2bdCV2oDbc7zqupGrUfZFA
        qzgieEyGzdCSRwjr1/PibA3bpwHyhD9CGD0PRVVTLhw6h6L5kuN1jA20OfzWxf/o
        XUsdmRaWiF+l4s6Dcd56SuRp5SGNa2+vP9Of/FX5
        -----END CERTIFICATE-----
    metrics:
      role: amqp
      hostname: 'amqp.example.com'
      security_protocol: 'non-ssl'
      port: 5666
      userid: admin
      password: password

- name: Create a new GCE provider in ManageIQ
  community.general.manageiq_provider:
    name: 'EngGoogle'
    type: 'GCE'
    provider_region: 'europe-west1'
    project: 'project1'
    state: 'present'
    provider:
      hostname: 'gce.example.com'
      auth_key: 'google_json_key'
      validate_certs: 'false'
```

### Authors

- Daniel Korn (@dkorn)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
