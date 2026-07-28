---
collection: ansible
version: "8"
title: "community.crypto.luks_device module – Manage encrypted (LUKS) devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/luks_device_module.html
fetched_at: 2026-07-28T01:42:27+00:00
---
# community.crypto.luks_device module – Manage encrypted (LUKS) devices

> **Note:**
>
> This module is part of the [community.crypto collection](https://galaxy.ansible.com/ui/repo/published/community/crypto/) (version 2.16.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.crypto`.
> You need further requirements to be able to use this module,
> see [Requirements](luks_device_module.md#ansible-collections-community-crypto-luks-device-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.luks_device`.

- [Synopsis](luks_device_module.md#synopsis)
- [Requirements](luks_device_module.md#requirements)
- [Parameters](luks_device_module.md#parameters)
- [Attributes](luks_device_module.md#attributes)
- [Examples](luks_device_module.md#examples)
- [Return Values](luks_device_module.md#return-values)

## [Synopsis](luks_device_module.md#id1)

- Module manages [LUKS](https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup) on given device. Supports creating, destroying, opening and closing of LUKS container and adding or removing new keys and passphrases.

## [Requirements](luks_device_module.md#id2)

The below requirements are needed on the host that executes this module.

- cryptsetup
- wipefs (when `state` is `absent`)
- lsblk
- blkid (when `label` or `uuid` options are used)

## [Parameters](luks_device_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cipher**  string  *added in community.crypto 1.1.0* | This option allows the user to define the cipher specification string for the LUKS container.  Will only be used on container creation.  For pre-2.6.10 kernels, use `aes-plain` as they do not understand the new cipher spec strings. To use ESSIV, use `aes-cbc-essiv:sha256`. |
| **device**  string | Device to work with (for example `/dev/sda1`). Needed in most cases. Can be omitted only when `state=closed` together with `name` is provided. |
| **force_remove_last_key**  boolean | If set to `true`, allows removing the last key from a container.  BEWARE that when the last key has been removed from a container, the container can no longer be opened!  **Choices:**   - `false` ← (default) - `true` |
| **hash**  string  *added in community.crypto 1.1.0* | This option allows the user to specify the hash function used in LUKS key setup scheme and volume key digest.  Will only be used on container creation. |
| **keyfile**  path | Used to unlock the container. Either a `keyfile` or a `passphrase` is needed for most of the operations. Parameter value is the path to the keyfile with the passphrase.  BEWARE that working with keyfiles in plaintext is dangerous. Make sure that they are protected. |
| **keysize**  integer  *added in community.crypto 1.0.0* | Sets the key size only if LUKS container does not exist. |
| **keyslot**  integer  *added in community.crypto 2.16.0* | Adds the `keyfile` or `passphrase` to a specific keyslot when creating a new container on `device`. Parameter value is the number of the keyslot.  **Note** that a device of `type=luks1` supports the keyslot numbers `0`-`7` and a device of `type=luks2` supports the keyslot numbers `0`-`31`. In order to use the keyslots `8`-`31` when creating a new container, setting `type` to `luks2` is required. |
| **label**  string  *added in community.crypto 1.0.0* | This option allow the user to create a LUKS2 format container with label support, respectively to identify the container by label on later usages.  Will only be used on container creation, or when `device` is not specified.  This cannot be specified if `type` is set to `luks1`. |
| **name**  string | Sets container name when `state=opened`. Can be used instead of `device` when closing the existing container (that is, when `state=closed`). |
| **new_keyfile**  path | Adds additional key to given container on `device`. Needs `keyfile` or `passphrase` option for authorization. LUKS container supports up to 8 keyslots. Parameter value is the path to the keyfile with the passphrase.  NOTE that adding additional keys is idempotent only since community.crypto 1.4.0. For older versions, a new keyslot will be used even if another keyslot already exists for this keyfile.  BEWARE that working with keyfiles in plaintext is dangerous. Make sure that they are protected. |
| **new_keyslot**  integer  *added in community.crypto 2.16.0* | Adds the additional `new_keyfile` or `new_passphrase` to a specific keyslot on the given `device`. Parameter value is the number of the keyslot.  **Note** that a device of `type=luks1` supports the keyslot numbers `0`-`7` and a device of `type=luks2` supports the keyslot numbers `0`-`31`. |
| **new_passphrase**  string  *added in community.crypto 1.0.0* | Adds additional passphrase to given container on `device`. Needs `keyfile` or `passphrase` option for authorization. LUKS container supports up to 8 keyslots. Parameter value is a string with the new passphrase.  NOTE that adding additional passphrase is idempotent only since community.crypto 1.4.0. For older versions, a new keyslot will be used even if another keyslot already exists for this passphrase. |
| **passphrase**  string  *added in community.crypto 1.0.0* | Used to unlock the container. Either a `passphrase` or a `keyfile` is needed for most of the operations. Parameter value is a string with the passphrase. |
| **pbkdf**  dictionary  *added in community.crypto 1.4.0* | This option allows the user to configure the Password-Based Key Derivation Function (PBKDF) used.  Will only be used on container creation, and when adding keys to an existing container. |
| **algorithm**  string | The algorithm to use.  Only available for the LUKS 2 format.  **Choices:**   - `"argon2i"` - `"argon2id"` - `"pbkdf2"` |
| **iteration_count**  integer | Specify the iteration count used for the PBKDF.  Mutually exclusive with `pbkdf.iteration_time`. |
| **iteration_time**  float | Specify the iteration time used for the PBKDF.  Note that this is in **seconds**, not in milliseconds as on the command line.  Mutually exclusive with `pbkdf.iteration_count`. |
| **memory**  integer | The memory cost limit in kilobytes for the PBKDF.  This is not used for PBKDF2, but only for the Argon PBKDFs. |
| **parallel**  integer | The parallel cost for the PBKDF. This is the number of threads that run in parallel.  This is not used for PBKDF2, but only for the Argon PBKDFs. |
| **perf_no_read_workqueue**  boolean  *added in community.crypto 2.3.0* | Allows the user to bypass dm-crypt internal workqueue and process read requests synchronously.  Will only be used when opening containers.  **Choices:**   - `false` ← (default) - `true` |
| **perf_no_write_workqueue**  boolean  *added in community.crypto 2.3.0* | Allows the user to bypass dm-crypt internal workqueue and process write requests synchronously.  Will only be used when opening containers.  **Choices:**   - `false` ← (default) - `true` |
| **perf_same_cpu_crypt**  boolean  *added in community.crypto 2.3.0* | Allows the user to perform encryption using the same CPU that IO was submitted on.  The default is to use an unbound workqueue so that encryption work is automatically balanced between available CPUs.  Will only be used when opening containers.  **Choices:**   - `false` ← (default) - `true` |
| **perf_submit_from_crypt_cpus**  boolean  *added in community.crypto 2.3.0* | Allows the user to disable offloading writes to a separate thread after encryption.  There are some situations where offloading block write IO operations from the encryption threads to a single thread degrades performance significantly.  The default is to offload block write IO operations to the same thread.  Will only be used when opening containers.  **Choices:**   - `false` ← (default) - `true` |
| **persistent**  boolean  *added in community.crypto 2.3.0* | Allows the user to store options into container’s metadata persistently and automatically use them next time. Only `perf_same_cpu_crypt`, `perf_submit_from_crypt_cpus`, `perf_no_read_workqueue`, and `perf_no_write_workqueue` can be stored persistently.  Will only work with LUKS2 containers.  Will only be used when opening containers.  **Choices:**   - `false` ← (default) - `true` |
| **remove_keyfile**  path | Removes given key from the container on `device`. Does not remove the keyfile from filesystem. Parameter value is the path to the keyfile with the passphrase.  NOTE that removing keys is idempotent only since community.crypto 1.4.0. For older versions, trying to remove a key which no longer exists results in an error.  NOTE that to remove the last key from a LUKS container, the `force_remove_last_key` option must be set to `true`.  BEWARE that working with keyfiles in plaintext is dangerous. Make sure that they are protected. |
| **remove_keyslot**  integer  *added in community.crypto 2.16.0* | Removes the key in the given slot on `device`. Needs `keyfile` or `passphrase` for authorization.  **Note** that a device of `type=luks1` supports the keyslot numbers `0`-`7` and a device of `type=luks2` supports the keyslot numbers `0`-`31`.  **Note** that the given `keyfile` or `passphrase` must not be in the slot to be removed. |
| **remove_passphrase**  string  *added in community.crypto 1.0.0* | Removes given passphrase from the container on `device`. Parameter value is a string with the passphrase to remove.  NOTE that removing passphrases is idempotent only since community.crypto 1.4.0. For older versions, trying to remove a passphrase which no longer exists results in an error.  NOTE that to remove the last keyslot from a LUKS container, the `force_remove_last_key` option must be set to `true`. |
| **sector_size**  integer  *added in community.crypto 1.5.0* | This option allows the user to specify the sector size (in bytes) used for LUKS2 containers.  Will only be used on container creation. |
| **state**  string | Desired state of the LUKS container. Based on its value creates, destroys, opens or closes the LUKS container on a given device.  `present` will create LUKS container unless already present. Requires `device` and either `keyfile` or `passphrase` options to be provided.  `absent` will remove existing LUKS container if it exists. Requires `device` or `name` to be specified.  `opened` will unlock the LUKS container. If it does not exist it will be created first. Requires `device` and either `keyfile` or `passphrase` to be specified. Use the `name` option to set the name of the opened container. Otherwise the name will be generated automatically and returned as a part of the result.  `closed` will lock the LUKS container. However if the container does not exist it will be created. Requires `device` and either `keyfile` or `passphrase` options to be provided. If container does already exist `device` or `name` will suffice.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"opened"` - `"closed"` |
| **type**  string  *added in community.crypto 1.0.0* | This option allow the user explicit define the format of LUKS container that wants to work with. Options are `luks1` or `luks2`  **Choices:**   - `"luks1"` - `"luks2"` |
| **uuid**  string  *added in community.crypto 1.0.0* | With this option user can identify the LUKS container by UUID.  Will only be used when `device` and `label` are not specified. |

## [Attributes](luks_device_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](luks_device_module.md#id5)

```yaml+jinja
- name: Create LUKS container (remains unchanged if it already exists)
  community.crypto.luks_device:
    device: "/dev/loop0"
    state: "present"
    keyfile: "/vault/keyfile"

- name: Create LUKS container with a passphrase
  community.crypto.luks_device:
    device: "/dev/loop0"
    state: "present"
    passphrase: "foo"

- name: Create LUKS container with specific encryption
  community.crypto.luks_device:
    device: "/dev/loop0"
    state: "present"
    cipher: "aes"
    hash: "sha256"

- name: (Create and) open the LUKS container; name it "mycrypt"
  community.crypto.luks_device:
    device: "/dev/loop0"
    state: "opened"
    name: "mycrypt"
    keyfile: "/vault/keyfile"

- name: Close the existing LUKS container "mycrypt"
  community.crypto.luks_device:
    state: "closed"
    name: "mycrypt"

- name: Make sure LUKS container exists and is closed
  community.crypto.luks_device:
    device: "/dev/loop0"
    state: "closed"
    keyfile: "/vault/keyfile"

- name: Create container if it does not exist and add new key to it
  community.crypto.luks_device:
    device: "/dev/loop0"
    state: "present"
    keyfile: "/vault/keyfile"
    new_keyfile: "/vault/keyfile2"

- name: Add new key to the LUKS container (container has to exist)
  community.crypto.luks_device:
    device: "/dev/loop0"
    keyfile: "/vault/keyfile"
    new_keyfile: "/vault/keyfile2"

- name: Add new passphrase to the LUKS container
  community.crypto.luks_device:
    device: "/dev/loop0"
    keyfile: "/vault/keyfile"
    new_passphrase: "foo"

- name: Remove existing keyfile from the LUKS container
  community.crypto.luks_device:
    device: "/dev/loop0"
    remove_keyfile: "/vault/keyfile2"

- name: Remove existing passphrase from the LUKS container
  community.crypto.luks_device:
    device: "/dev/loop0"
    remove_passphrase: "foo"

- name: Completely remove the LUKS container and its contents
  community.crypto.luks_device:
    device: "/dev/loop0"
    state: "absent"

- name: Create a container with label
  community.crypto.luks_device:
    device: "/dev/loop0"
    state: "present"
    keyfile: "/vault/keyfile"
    label: personalLabelName

- name: Open the LUKS container based on label without device; name it "mycrypt"
  community.crypto.luks_device:
    label: "personalLabelName"
    state: "opened"
    name: "mycrypt"
    keyfile: "/vault/keyfile"

- name: Close container based on UUID
  community.crypto.luks_device:
    uuid: 03ecd578-fad4-4e6c-9348-842e3e8fa340
    state: "closed"
    name: "mycrypt"

- name: Create a container using luks2 format
  community.crypto.luks_device:
    device: "/dev/loop0"
    state: "present"
    keyfile: "/vault/keyfile"
    type: luks2

- name: Create a container with key in slot 4
  community.crypto.luks_device:
    device: "/dev/loop0"
    state: "present"
    keyfile: "/vault/keyfile"
    keyslot: 4

- name: Add a new key in slot 5
  community.crypto.luks_device:
    device: "/dev/loop0"
    keyfile: "/vault/keyfile"
    new_keyfile: "/vault/keyfile"
    new_keyslot: 5

- name: Remove the key from slot 4 (given keyfile must not be slot 4)
  community.crypto.luks_device:
    device: "/dev/loop0"
    keyfile: "/vault/keyfile"
    remove_keyslot: 4
```

## [Return Values](luks_device_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **name**  string | When `state=opened` returns (generated or given) name of LUKS container. Returns None if no name is supplied.  **Returned:** success  **Sample:** `"luks-c1da9a58-2fde-4256-9d9f-6ab008b4dd1b"` |

### Authors

- Jan Pokorny (@japokorn)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.crypto)
- [Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-crypto)
