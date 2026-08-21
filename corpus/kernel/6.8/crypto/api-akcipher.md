---
collection: kernel
version: "6.8"
title: "Asymmetric Cipher Algorithm Definitions"
source_url: https://www.kernel.org/doc/html/v6.8/crypto/api-akcipher.html
fetched_at: 2026-08-21T03:38:35+00:00
---
# Asymmetric Cipher Algorithm Definitions

struct akcipher_request
:   public key request

**Definition**:

```
struct akcipher_request {
    struct crypto_async_request base;
    struct scatterlist *src;
    struct scatterlist *dst;
    unsigned int src_len;
    unsigned int dst_len;
    void *__ctx[] ;
};
```

**Members**

`base`
:   Common attributes for async crypto requests

`src`
:   Source data
    For verify op this is signature + digest, in that case
    total size of **src** is **src_len** + **dst_len**.

`dst`
:   Destination data (Should be NULL for verify op)

`src_len`
:   Size of the input buffer
    For verify op it's size of signature part of **src**, this part
    is supposed to be operated by cipher.

`dst_len`
:   Size of **dst** buffer (for all ops except verify).
    It needs to be at least as big as the expected result
    depending on the operation.
    After operation it will be updated with the actual size of the
    result.
    In case of error where the dst sgl size was insufficient,
    it will be updated to the size required for the operation.
    For verify op this is size of digest part in **src**.

`__ctx`
:   Start of private context data

struct akcipher_alg
:   generic public key algorithm

**Definition**:

```
struct akcipher_alg {
    int (*sign)(struct akcipher_request *req);
    int (*verify)(struct akcipher_request *req);
    int (*encrypt)(struct akcipher_request *req);
    int (*decrypt)(struct akcipher_request *req);
    int (*set_pub_key)(struct crypto_akcipher *tfm, const void *key, unsigned int keylen);
    int (*set_priv_key)(struct crypto_akcipher *tfm, const void *key, unsigned int keylen);
    unsigned int (*max_size)(struct crypto_akcipher *tfm);
    int (*init)(struct crypto_akcipher *tfm);
    void (*exit)(struct crypto_akcipher *tfm);
#ifdef CONFIG_CRYPTO_STATS;
    struct crypto_istat_akcipher stat;
#endif;
    struct crypto_alg base;
};
```

**Members**

`sign`
:   Function performs a sign operation as defined by public key
    algorithm. In case of error, where the dst_len was insufficient,
    the req->dst_len will be updated to the size required for the
    operation

`verify`
:   Function performs a complete verify operation as defined by
    public key algorithm, returning verification status. Requires
    digest value as input parameter.

`encrypt`
:   Function performs an encrypt operation as defined by public key
    algorithm. In case of error, where the dst_len was insufficient,
    the req->dst_len will be updated to the size required for the
    operation

`decrypt`
:   Function performs a decrypt operation as defined by public key
    algorithm. In case of error, where the dst_len was insufficient,
    the req->dst_len will be updated to the size required for the
    operation

`set_pub_key`
:   Function invokes the algorithm specific set public key
    function, which knows how to decode and interpret
    the BER encoded public key and parameters

`set_priv_key`
:   Function invokes the algorithm specific set private key
    function, which knows how to decode and interpret
    the BER encoded private key and parameters

`max_size`
:   Function returns dest buffer size required for a given key.

`init`
:   Initialize the cryptographic transformation object.
    This function is used to initialize the cryptographic
    transformation object. This function is called only once at
    the instantiation time, right after the transformation context
    was allocated. In case the cryptographic hardware has some
    special requirements which need to be handled by software, this
    function shall check for the precise requirement of the
    transformation and put any software fallbacks in place.

`exit`
:   Deinitialize the cryptographic transformation object. This is a
    counterpart to **init**, used to remove various changes set in
    **init**.

`stat`
:   Statistics for akcipher algorithm

`base`
:   Common crypto API algorithm data structure

# Asymmetric Cipher API

The Public Key API is used with the algorithms of type
CRYPTO_ALG_TYPE_AKCIPHER (listed as type "akcipher" in /proc/crypto)

struct crypto_akcipher \*crypto_alloc_akcipher(const char \*alg_name, u32 type, u32 mask)
:   allocate AKCIPHER tfm handle

**Parameters**

`const char *alg_name`
:   is the cra_name / name or cra_driver_name / driver name of the
    public key algorithm e.g. "rsa"

`u32 type`
:   specifies the type of the algorithm

`u32 mask`
:   specifies the mask for the algorithm

**Description**

Allocate a handle for public key algorithm. The returned struct
crypto_akcipher is the handle that is required for any subsequent
API invocation for the public key operations.

**Return**

allocated handle in case of success; IS_ERR() is true in case
:   of an error, [`PTR_ERR()`](../core-api/kernel-api.md#c.PTR_ERR "PTR_ERR") returns the error code.

void crypto_free_akcipher(struct crypto_akcipher \*tfm)
:   free AKCIPHER tfm handle

**Parameters**

`struct crypto_akcipher *tfm`
:   AKCIPHER tfm handle allocated with [`crypto_alloc_akcipher()`](api-akcipher.md#c.crypto_alloc_akcipher "crypto_alloc_akcipher")

**Description**

If **tfm** is a NULL or error pointer, this function does nothing.

unsigned int crypto_akcipher_maxsize(struct crypto_akcipher \*tfm)
:   Get len for output buffer

**Parameters**

`struct crypto_akcipher *tfm`
:   AKCIPHER tfm handle allocated with [`crypto_alloc_akcipher()`](api-akcipher.md#c.crypto_alloc_akcipher "crypto_alloc_akcipher")

**Description**

Function returns the dest buffer size required for a given key.
Function assumes that the key is already set in the transformation. If this
function is called without a setkey or with a failed setkey, you will end up
in a NULL dereference.

int crypto_akcipher_encrypt(struct [akcipher_request](api-akcipher.md#c.akcipher_request "akcipher_request") \*req)
:   Invoke public key encrypt operation

**Parameters**

`struct akcipher_request *req`
:   asymmetric key request

**Description**

Function invokes the specific public key encrypt operation for a given
public key algorithm

**Return**

zero on success; error code in case of error

int crypto_akcipher_decrypt(struct [akcipher_request](api-akcipher.md#c.akcipher_request "akcipher_request") \*req)
:   Invoke public key decrypt operation

**Parameters**

`struct akcipher_request *req`
:   asymmetric key request

**Description**

Function invokes the specific public key decrypt operation for a given
public key algorithm

**Return**

zero on success; error code in case of error

int crypto_akcipher_sign(struct [akcipher_request](api-akcipher.md#c.akcipher_request "akcipher_request") \*req)
:   Invoke public key sign operation

**Parameters**

`struct akcipher_request *req`
:   asymmetric key request

**Description**

Function invokes the specific public key sign operation for a given
public key algorithm

**Return**

zero on success; error code in case of error

int crypto_akcipher_verify(struct [akcipher_request](api-akcipher.md#c.akcipher_request "akcipher_request") \*req)
:   Invoke public key signature verification

**Parameters**

`struct akcipher_request *req`
:   asymmetric key request

**Description**

Function invokes the specific public key signature verification operation
for a given public key algorithm.

**Note**

req->dst should be NULL, req->src should point to SG of size
(req->src_size + req->dst_size), containing signature (of req->src_size
length) with appended digest (of req->dst_size length).

**Return**

zero on verification success; error code in case of error.

int crypto_akcipher_set_pub_key(struct crypto_akcipher \*tfm, const void \*key, unsigned int keylen)
:   Invoke set public key operation

**Parameters**

`struct crypto_akcipher *tfm`
:   tfm handle

`const void *key`
:   BER encoded public key, algo OID, paramlen, BER encoded
    parameters

`unsigned int keylen`
:   length of the key (not including other data)

**Description**

Function invokes the algorithm specific set key function, which knows
how to decode and interpret the encoded key and parameters

**Return**

zero on success; error code in case of error

int crypto_akcipher_set_priv_key(struct crypto_akcipher \*tfm, const void \*key, unsigned int keylen)
:   Invoke set private key operation

**Parameters**

`struct crypto_akcipher *tfm`
:   tfm handle

`const void *key`
:   BER encoded private key, algo OID, paramlen, BER encoded
    parameters

`unsigned int keylen`
:   length of the key (not including other data)

**Description**

Function invokes the algorithm specific set key function, which knows
how to decode and interpret the encoded key and parameters

**Return**

zero on success; error code in case of error

# Asymmetric Cipher Request Handle

struct [akcipher_request](api-akcipher.md#c.akcipher_request "akcipher_request") \*akcipher_request_alloc(struct crypto_akcipher \*tfm, gfp_t gfp)
:   allocates public key request

**Parameters**

`struct crypto_akcipher *tfm`
:   AKCIPHER tfm handle allocated with [`crypto_alloc_akcipher()`](api-akcipher.md#c.crypto_alloc_akcipher "crypto_alloc_akcipher")

`gfp_t gfp`
:   allocation flags

**Return**

allocated handle in case of success or NULL in case of an error.

void akcipher_request_free(struct [akcipher_request](api-akcipher.md#c.akcipher_request "akcipher_request") \*req)
:   zeroize and free public key request

**Parameters**

`struct akcipher_request *req`
:   request to free

void akcipher_request_set_callback(struct [akcipher_request](api-akcipher.md#c.akcipher_request "akcipher_request") \*req, u32 flgs, crypto_completion_t cmpl, void \*data)
:   Sets an asynchronous callback.

**Parameters**

`struct akcipher_request *req`
:   request that the callback will be set for

`u32 flgs`
:   specify for instance if the operation may backlog

`crypto_completion_t cmpl`
:   callback which will be called

`void *data`
:   private data used by the caller

**Description**

Callback will be called when an asynchronous operation on a given
request is finished.

void akcipher_request_set_crypt(struct [akcipher_request](api-akcipher.md#c.akcipher_request "akcipher_request") \*req, struct scatterlist \*src, struct scatterlist \*dst, unsigned int src_len, unsigned int dst_len)
:   Sets request parameters

**Parameters**

`struct akcipher_request *req`
:   public key request

`struct scatterlist *src`
:   ptr to input scatter list

`struct scatterlist *dst`
:   ptr to output scatter list or NULL for verify op

`unsigned int src_len`
:   size of the src input scatter list to be processed

`unsigned int dst_len`
:   size of the dst output scatter list or size of signature
    portion in **src** for verify op

**Description**

Sets parameters required by crypto operation
