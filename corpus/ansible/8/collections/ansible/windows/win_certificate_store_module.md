---
collection: ansible
version: "8"
title: "ansible.windows.win_certificate_store module – Manages the certificate store"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/win_certificate_store_module.html
fetched_at: 2026-07-28T01:10:29+00:00
---
# ansible.windows.win_certificate_store module – Manages the certificate store

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ui/repo/published/ansible/windows/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_certificate_store`.

- [Synopsis](win_certificate_store_module.md#synopsis)
- [Parameters](win_certificate_store_module.md#parameters)
- [Notes](win_certificate_store_module.md#notes)
- [Examples](win_certificate_store_module.md#examples)
- [Return Values](win_certificate_store_module.md#return-values)

## [Synopsis](win_certificate_store_module.md#id1)

- Used to import/export and remove certificates and keys from the local certificate store.
- This module is not used to create certificates and will only manage existing certs as a file or in the store.
- It can be used to import PEM, DER, P7B, PKCS12 (PFX) certificates and export PEM, DER and PKCS12 certificates.

## [Parameters](win_certificate_store_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **file_type**  string | The file type to export the certificate as when `state=exported`.  `der` is a binary ASN.1 encoded file.  `pem` is a base64 encoded file of a der file in the OpenSSL form.  `pkcs12` (also known as pfx) is a binary container that contains both the certificate and private key unlike the other options.  When `pkcs12` is set and the private key is not exportable or accessible by the current user, it will throw an exception.  **Choices:**   - `"der"` ← (default) - `"pem"` - `"pkcs12"` |
| **key_exportable**  boolean | Whether to allow the private key to be exported.  If `false`, then this module and other process will only be able to export the certificate and the private key cannot be exported.  Used when `state=present` only.  **Choices:**   - `false` - `true` ← (default) |
| **key_storage**  string | Specifies where Windows will store the private key when it is imported.  When set to `default`, the default option as set by Windows is used, typically `user`.  When set to `machine`, the key is stored in a path accessible by various users.  When set to `user`, the key is stored in a path only accessible by the current user.  Used when `state=present` only and cannot be changed once imported.  See <https://msdn.microsoft.com/en-us/library/system.security.cryptography.x509certificates.x509keystorageflags.aspx> for more details.  **Choices:**   - `"default"` ← (default) - `"machine"` - `"user"` |
| **password**  string | The password of the pkcs12 certificate key.  This is used when reading a pkcs12 certificate file or the password to set when `state=exported` and `file_type=pkcs12`.  If the pkcs12 file has no password set or no password should be set on the exported file, do not set this option. |
| **path**  path | The path to a certificate file.  This is required when *state* is `present` or `exported`.  When *state* is `absent` and *thumbprint* is not specified, the thumbprint is derived from the certificate at this path. |
| **state**  string | If `present`, will ensure that the certificate at *path* is imported into the certificate store specified.  If `absent`, will ensure that the certificate specified by *thumbprint* or the thumbprint of the cert at *path* is removed from the store specified.  If `exported`, will ensure the file at *path* is a certificate specified by *thumbprint*.  When exporting a certificate, if *path* is a directory then the module will fail, otherwise the file will be replaced if needed.  **Choices:**   - `"absent"` - `"exported"` - `"present"` ← (default) |
| **store_location**  string | The store location to use when importing a certificate or searching for a certificate.  Can be set to `CurrentUser` or `LocalMachine` when `store_type=system`.  Defaults to `LocalMachine` when `store_type=system`.  Must be set to any service name when `store_type=service`.  **Default:** `"LocalMachine"` |
| **store_name**  string | The store name to use when importing a certificate or searching for a certificate.  `AddressBook`: The X.509 certificate store for other users  `AuthRoot`: The X.509 certificate store for third-party certificate authorities (CAs)  `CertificateAuthority`: The X.509 certificate store for intermediate certificate authorities (CAs)  `Disallowed`: The X.509 certificate store for revoked certificates  `My`: The X.509 certificate store for personal certificates  `Root`: The X.509 certificate store for trusted root certificate authorities (CAs)  `TrustedPeople`: The X.509 certificate store for directly trusted people and resources  `TrustedPublisher`: The X.509 certificate store for directly trusted publishers  **Default:** `"My"` |
| **store_type**  string  *added in ansible.windows 1.5.0* | The store type to manage.  Use `system` to manage locations in the system store, `LocalMachine` and `CurrentUser`.  Use `service` to manage the store of a service account specified by *store_location*.  **Choices:**   - `"system"` ← (default) - `"service"` |
| **thumbprint**  string | The thumbprint as a hex string to either export or remove.  See the examples for how to specify the thumbprint. |

## [Notes](win_certificate_store_module.md#id3)

> **Note:**
>
> - Some actions on PKCS12 certificates and keys may fail with the error `the specified network password is not correct`, either use CredSSP or Kerberos with credential delegation, or use `become` to bypass these restrictions.
> - The certificates must be located on the Windows host to be set with *path*.
> - When importing a certificate for usage in IIS, it is generally required to use the `machine` key_storage option, as both `default` and `user` will make the private key unreadable to IIS APPPOOL identities and prevent binding the certificate to the https endpoint.

## [Examples](win_certificate_store_module.md#id4)

```yaml+jinja
- name: Import a certificate
  ansible.windows.win_certificate_store:
    path: C:\Temp\cert.pem
    state: present

- name: Import pfx certificate that is password protected
  ansible.windows.win_certificate_store:
    path: C:\Temp\cert.pfx
    state: present
    password: VeryStrongPasswordHere!
  become: true
  become_method: runas

- name: Import pfx certificate without password and set private key as un-exportable
  ansible.windows.win_certificate_store:
    path: C:\Temp\cert.pfx
    state: present
    key_exportable: false
  # usually you don't set this here but it is for illustrative purposes
  vars:
    ansible_winrm_transport: credssp

- name: Remove a certificate based on file thumbprint
  ansible.windows.win_certificate_store:
    path: C:\Temp\cert.pem
    state: absent

- name: Remove a certificate based on thumbprint
  ansible.windows.win_certificate_store:
    thumbprint: BD7AF104CF1872BDB518D95C9534EA941665FD27
    state: absent

- name: Remove certificate based on thumbprint is CurrentUser/TrustedPublishers store
  ansible.windows.win_certificate_store:
    thumbprint: BD7AF104CF1872BDB518D95C9534EA941665FD27
    state: absent
    store_location: CurrentUser
    store_name: TrustedPublisher

- name: Export certificate as der encoded file
  ansible.windows.win_certificate_store:
    path: C:\Temp\cert.cer
    state: exported
    file_type: der

- name: Export certificate and key as pfx encoded file
  ansible.windows.win_certificate_store:
    path: C:\Temp\cert.pfx
    state: exported
    file_type: pkcs12
    password: AnotherStrongPass!
  become: true
  become_method: runas
  become_user: SYSTEM

- name: Import certificate be used by IIS
  ansible.windows.win_certificate_store:
    path: C:\Temp\cert.pfx
    file_type: pkcs12
    password: StrongPassword!
    store_location: LocalMachine
    key_storage: machine
    state: present
  become: true
  become_method: runas
  become_user: SYSTEM

- name: Import certificate to be used for LDAPS
  ansible.windows.win_certificate_store:
    path: C:\Temp\cert.pfx
    password: StrongPassword!
    store_type: service
    store_location: NTDS
    key_exportable: false
    key_storage: machine
    state: present
```

## [Return Values](win_certificate_store_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **thumbprints**  list / elements=string | A list of certificate thumbprints that were touched by the module.  **Returned:** success  **Sample:** `["BC05633694E675449136679A658281F17A191087"]` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)
