---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_ike_peer module – Manage IPSec IKE Peer configuration on BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_ike_peer_module.html
fetched_at: 2026-07-28T02:06:27+00:00
---
# f5networks.f5_modules.bigip_ike_peer module – Manage IPSec IKE Peer configuration on BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_ike_peer`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_ike_peer_module.md#synopsis)
- [Parameters](bigip_ike_peer_module.md#parameters)
- [Notes](bigip_ike_peer_module.md#notes)
- [Examples](bigip_ike_peer_module.md#examples)
- [Return Values](bigip_ike_peer_module.md#return-values)

## [Synopsis](bigip_ike_peer_module.md#id1)

- Manage IPSec IKE Peer configuration on a BIG-IP device.

## [Parameters](bigip_ike_peer_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | Description of the IKE peer. |
| **name**  string / required | Specifies the name of the IKE peer. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **phase1_auth_method**  string | Specifies the authentication method for phase 1 negotiation.  When creating a new IKE peer, if this value is not specified, the default is `rsa-signature`.  **Choices:**   - `"pre-shared-key"` - `"rsa-signature"` |
| **phase1_cert**  string | Specifies the digital certificate to use for the RSA signature.  When creating a new IKE peer, if this value is not specified, and `phase1_auth_method` is `rsa-signature`, the default is `default.crt`.  This parameter is invalid when `phase1_auth_method` is `pre-shared-key`. |
| **phase1_encryption_algorithm**  string | Specifies the algorithm to use for IKE encryption.  IKE `version` `v2` does not support `blowfish`, `camellia`, or `cast128`.  **Choices:**   - `"3des"` - `"des"` - `"blowfish"` - `"cast128"` - `"aes128"` - `"aes192"` - `"aes256"` - `"camellia"` |
| **phase1_hash_algorithm**  string | Specifies the algorithm to use for IKE authentication.  **Choices:**   - `"sha1"` - `"md5"` - `"sha256"` - `"sha384"` - `"sha512"` |
| **phase1_key**  string | Specifies the public key the digital certificate contains.  When creating a new IKE peer, if this value is not specified, and `phase1_auth_method` is `rsa-signature`, the default is `default.key`.  This parameter is invalid when `phase1_auth_method` is `pre-shared-key`. |
| **phase1_lifetime**  integer  *added in f5networks.f5_modules 1.1.0* | Defines the lifetime in minutes of an IKE SA which will be proposed in the phase 1 negotiations.  The accepted value range is `1 - 4294967295` minutes.  When creating a new IKE peer, if this value is not specified, the default value set by the system is `1440` minutes. |
| **phase1_perfect_forward_secrecy**  string | Specifies the Diffie-Hellman group to use for IKE Phase 1 and Phase 2 negotiations.  **Choices:**   - `"ecp256"` - `"ecp384"` - `"ecp521"` - `"modp768"` - `"modp1024"` - `"modp1536"` - `"modp2048"` - `"modp3072"` - `"modp4096"` - `"modp6144"` - `"modp8192"` |
| **phase1_verify_peer_cert**  boolean | In IKEv2, specifies whether the certificate sent by the IKE peer is verified using the Trusted Certificate Authorities, a CRL, and/or a peer certificate.  In IKEv1, specifies whether the identifier sent by the peer is verified with the credentials in the certificate, in the following manner - ASN1DN; specifies that the entire certificate subject name is compared with the identifier. Address, FQDN, or User FQDN; specifies that the certificate’s subjectAltName is compared with the identifier. If the two do not match, the negotiation fails.  When creating a new IKE peer, if this value is not specified, and `phase1_auth_method` is `rsa-signature`, the default is `false`.  This parameter is invalid when `phase1_auth_method` is `pre-shared-key`.  **Choices:**   - `false` - `true` |
| **presented_id_type**  string | Specifies the identifier type the local system uses to identify itself to the peer during IKE Phase 1 negotiations.  **Choices:**   - `"address"` - `"asn1dn"` - `"fqdn"` - `"keyid-tag"` - `"user-fqdn"` - `"override"` |
| **presented_id_value**  string | Specifies a value for the identity when using a `presented_id_type` of `override`.  This is a required value when `version` includes (Cv2). |
| **preshared_key**  string | Specifies a string the IKE peers share for authenticating each other.  This parameter is only relevant when `phase1_auth_method` is `pre-shared-key`.  This parameter is invalid when `phase1_auth_method` is `rsa-signature`. |
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
| **remote_address**  string | Displays the IP address of the BIG-IP system that is remote to the system you are configuring. |
| **state**  string | When `present`, ensures the resource exists.  When `absent`, ensures the resource is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **update_password**  string | `always` allows updating passwords if the user chooses to do so. `on_create` only sets the password for newly created IKE peers.  **Choices:**   - `"always"` ← (default) - `"on_create"` |
| **verified_id_type**  string | Specifies the identifier type the local system uses to identify the peer during IKE Phase 1 negotiation.  This is a required value when `version` includes (Cv2).  When `user-fqdn`, value of `verified_id_value` must be in the form of User @ DNS domain string.  **Choices:**   - `"address"` - `"asn1dn"` - `"fqdn"` - `"keyid-tag"` - `"user-fqdn"` - `"override"` |
| **verified_id_value**  string | Specifies a value for the identity when using a `verified_id_type` of `override`.  This is a required value when `version` includes (Cv2). |
| **version**  list / elements=string | Specifies which version of IKE (Internet Key Exchange) is used.  If the system you are configuring is the IPsec initiator, and you select both versions, the system tries using IKEv2 for negotiation. If the remote peer does not support IKEv2, the IPsec tunnel fails. To use IKEv1 in this case, you must deselect Version 2 and try again.  If the system you are configuring is the IPsec responder, and you select both versions, the IPsec initiator system determines which IKE version to use.  When creating a new IKE peer, this value is required.  **Choices:**   - `"v1"` - `"v2"` |

## [Notes](bigip_ike_peer_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_ike_peer_module.md#id4)

```yaml+jinja
- name: Create new IKE peer
  bigip_ike_peer:
    name: ike1
    remote_address: 1.2.3.4
    version:
      - v1
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Change presented id type - keyid-tag
  bigip_ike_peer:
    name: ike1
    presented_id_type: keyid-tag
    presented_id_value: key1
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove IKE peer
  bigip_ike_peer:
    name: ike1
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_ike_peer_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **phase1_auth_method**  string | The new IKE Phase 1 Credentials Authentication Method value of the resource.  **Returned:** changed  **Sample:** `"rsa-signature"` |
| **phase1_cert**  string | The new IKE Phase 1 Certificate Credentials.  **Returned:** changed  **Sample:** `"/Common/cert1.crt"` |
| **phase1_encryption_algorithm**  string | The new IKE Phase 1 Encryption Algorithm.  **Returned:** changed  **Sample:** `"3des"` |
| **phase1_hash_algorithm**  string | The new IKE Phase 1 Authentication Algorithm.  **Returned:** changed  **Sample:** `"sha256"` |
| **phase1_key**  string | The new IKE Phase 1 Key Credentials.  **Returned:** changed  **Sample:** `"/Common/cert1.key"` |
| **phase1_perfect_forward_secrecy**  string | The new IKE Phase 1 Perfect Forward Secrecy.  **Returned:** changed  **Sample:** `"modp1024"` |
| **phase1_verify_peer_cert**  boolean | The new IKE Phase 1 Key Verify Peer Certificate setting.  **Returned:** changed  **Sample:** `true` |
| **presented_id_type**  string | The new Presented ID Type value of the resource.  **Returned:** changed  **Sample:** `"address"` |
| **presented_id_value**  string | The new Presented ID Value setting for the Presented ID Type.  **Returned:** changed  **Sample:** `"1.2.3.1"` |
| **remote_address**  string | The new Remote Address value of the resource.  **Returned:** changed  **Sample:** `"1.2.2.1"` |
| **verified_id_type**  string | The new Verified ID Type value of the resource.  **Returned:** changed  **Sample:** `"address"` |
| **verified_id_value**  string | The new Verified ID Value setting for the Verified ID Type.  **Returned:** changed  **Sample:** `"1.2.3.1"` |
| **version**  list / elements=string | The new list of IKE versions.  **Returned:** changed  **Sample:** `["v1", "v2"]` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
