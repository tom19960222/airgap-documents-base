---
collection: python
version: "3.12.14"
title: "Cryptographic Services"
source_url: https://docs.python.org/3.12/library/crypto.html
fetched_at: 2026-09-17T15:33:07+00:00
---
# Cryptographic Services

The modules described in this chapter implement various algorithms of a
cryptographic nature. They are available at the discretion of the installation.
On Unix systems, the [`crypt`](crypt.md#module-crypt "crypt: The crypt() function used to check Unix passwords. (deprecated) (Unix)") module may also be available.
Here’s an overview:

- [`hashlib` — Secure hashes and message digests](hashlib.md)
  - [Hash algorithms](hashlib.md#hash-algorithms)
  - [Usage](hashlib.md#usage)
  - [Constructors](hashlib.md#constructors)
  - [Attributes](hashlib.md#attributes)
  - [Hash Objects](hashlib.md#hash-objects)
  - [SHAKE variable length digests](hashlib.md#shake-variable-length-digests)
  - [File hashing](hashlib.md#file-hashing)
  - [Key derivation](hashlib.md#key-derivation)
  - [BLAKE2](hashlib.md#blake2)
    - [Creating hash objects](hashlib.md#creating-hash-objects)
    - [Constants](hashlib.md#constants)
    - [Examples](hashlib.md#examples)
      - [Simple hashing](hashlib.md#simple-hashing)
      - [Using different digest sizes](hashlib.md#using-different-digest-sizes)
      - [Keyed hashing](hashlib.md#keyed-hashing)
      - [Randomized hashing](hashlib.md#randomized-hashing)
      - [Personalization](hashlib.md#personalization)
      - [Tree mode](hashlib.md#tree-mode)
    - [Credits](hashlib.md#credits)
- [`hmac` — Keyed-Hashing for Message Authentication](hmac.md)
- [`secrets` — Generate secure random numbers for managing secrets](secrets.md)
  - [Random numbers](secrets.md#random-numbers)
  - [Generating tokens](secrets.md#generating-tokens)
    - [How many bytes should tokens use?](secrets.md#how-many-bytes-should-tokens-use)
  - [Other functions](secrets.md#other-functions)
  - [Recipes and best practices](secrets.md#recipes-and-best-practices)
