---
collection: ansible
version: "8"
title: "community.aws.cloudfront_distribution module – Create, update and delete AWS CloudFront distributions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/cloudfront_distribution_module.html
fetched_at: 2026-07-28T01:40:20+00:00
---
# community.aws.cloudfront_distribution module – Create, update and delete AWS CloudFront distributions

> **Note:**
>
> This module is part of the [community.aws collection](https://galaxy.ansible.com/ui/repo/published/community/aws/) (version 6.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.aws`.
> You need further requirements to be able to use this module,
> see [Requirements](cloudfront_distribution_module.md#ansible-collections-community-aws-cloudfront-distribution-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.cloudfront_distribution`.

New in community.aws 1.0.0

- [Synopsis](cloudfront_distribution_module.md#synopsis)
- [Requirements](cloudfront_distribution_module.md#requirements)
- [Parameters](cloudfront_distribution_module.md#parameters)
- [Notes](cloudfront_distribution_module.md#notes)
- [Examples](cloudfront_distribution_module.md#examples)
- [Return Values](cloudfront_distribution_module.md#return-values)

## [Synopsis](cloudfront_distribution_module.md#id1)

- Allows for easy creation, updating and deletion of CloudFront distributions.

## [Requirements](cloudfront_distribution_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](cloudfront_distribution_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **alias**  string | The name of an alias (CNAME) that is used in a distribution. This is used to effectively reference a distribution by its alias as an alias can only be used by one distribution per AWS account. This variable avoids having to provide the *distribution_id* as well as the *e_tag*, or *caller_reference* of an existing distribution. |
| **aliases**  list / elements=string | A list of domain name aliases (CNAMEs) as strings to be used for the distribution.  Each alias must be unique across all distribution for the AWS account.  **Default:** `[]` |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **cache_behaviors**  list / elements=dictionary | A list of dictionaries describing the cache behaviors for the distribution.  The order of the list is preserved across runs unless *purge_cache_behaviors* is enabled. |
| **forwarded_values**  dictionary | A dict that specifies how CloudFront handles query strings and cookies. |
| **allowed_methods**  dictionary | A dict that controls which HTTP methods CloudFront processes and forwards. |
| **cached_methods**  list / elements=string | A list of HTTP methods that you want CloudFront to apply caching to.  This can either be `[GET,HEAD]`, or `[GET,HEAD,OPTIONS]`. |
| **items**  list / elements=string | A list of HTTP methods that you want CloudFront to process and forward. |
| **compress**  boolean | Whether you want CloudFront to automatically compress files.  **Choices:**   - `false` - `true` |
| **cookies**  dictionary | A dict that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. |
| **forward**  string | Specifies which cookies to forward to the origin for this cache behavior.  Valid values are `all`, `none`, or `whitelist`. |
| **whitelisted_names**  list / elements=string | A list of cookies to forward to the origin for this cache behavior. |
| **default_ttl**  integer | The default amount of time that you want objects to stay in CloudFront caches. |
| **field_level_encryption_id**  string | The field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data. |
| **headers**  list / elements=string | A list of headers to forward to the origin for this cache behavior.  To forward all headers use a list containing a single element ‘\*’ (`['*']`) |
| **lambda_function_associations**  list / elements=dictionary | A list of Lambda function associations to use for this cache behavior. |
| **event_type**  string | Specifies the event type that triggers a Lambda function invocation.  This can be `viewer-request`, `origin-request`, `origin-response` or `viewer-response`. |
| **lambda_function_arn**  string | The ARN of the Lambda function. |
| **max_ttl**  integer | The maximum amount of time that you want objects to stay in CloudFront caches. |
| **min_ttl**  integer | The minimum amount of time that you want objects to stay in CloudFront caches. |
| **query_string**  boolean | Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior.  **Choices:**   - `false` - `true` |
| **query_string_cache_keys**  list / elements=string | A list that contains the query string parameters you want CloudFront to use as a basis for caching for a cache behavior. |
| **smooth_streaming**  boolean | Whether you want to distribute media files in the Microsoft Smooth Streaming format.  **Choices:**   - `false` - `true` |
| **trusted_signers**  dictionary | A dict that specifies the AWS accounts that you want to allow to create signed URLs for private content. |
| **enabled**  boolean | Whether you want to require viewers to use signed URLs to access the files specified by *path_pattern* and *target_origin_id*  **Choices:**   - `false` - `true` |
| **items**  list / elements=string | A list of trusted signers for this cache behavior. |
| **viewer_protocol_policy**  string | The protocol that viewers can use to access the files in the origin specified by *target_origin_id* when a request matches *path_pattern*.  Valid values are `allow-all`, `redirect-to-https` and `https-only`. |
| **path_pattern**  string | The pattern that specifies which requests to apply the behavior to. |
| **response_headers_policy_id**  string | The ID of the header policy that CloudFront adds to responses that it sends to viewers. |
| **target_origin_id**  string | The ID of the origin that you want CloudFront to route requests to by default. |
| **caller_reference**  string | A unique identifier for creating and updating CloudFront distributions.  Each caller reference must be unique across all distributions. e.g. a caller reference used in a web distribution cannot be reused in a streaming distribution. This parameter can be used instead of *distribution_id* to reference an existing distribution. If not specified, this defaults to a datetime stamp of the format `YYYY-MM-DDTHH:MM:SS.ffffff`. |
| **comment**  string | A comment that describes the CloudFront distribution.  If not specified, it defaults to a generic message that it has been created with Ansible, and a datetime stamp. |
| **custom_error_responses**  list / elements=dictionary | A config element that is a *list[]* of complex custom error responses to be specified for the distribution.  This attribute configures custom http error messages returned to the user. |
| **error_caching_min_ttl**  integer | The length of time (in seconds) that CloudFront will cache status codes for. |
| **error_code**  integer | The error code the custom error page is for. |
| **response_code**  integer | The HTTP status code that CloudFront should return to a user when the origin returns the HTTP status code specified by *error_code*. |
| **response_page_path**  string | The path to the custom error page that you want CloudFront to return to a viewer when your origin returns the HTTP status code specified by *error_code*. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **default_cache_behavior**  dictionary | A dict specifying the default cache behavior of the distribution.  If not specified, the *target_origin_id* is defined as the *target_origin_id* of the first valid cache_behavior in *cache_behaviors* with defaults. |
| **forwarded_values**  dictionary | A dict that specifies how CloudFront handles query strings and cookies. |
| **allowed_methods**  dictionary | A dict that controls which HTTP methods CloudFront processes and forwards. |
| **cached_methods**  list / elements=string | A list of HTTP methods that you want CloudFront to apply caching to.  This can either be `[GET,HEAD]`, or `[GET,HEAD,OPTIONS]`. |
| **items**  list / elements=string | A list of HTTP methods that you want CloudFront to process and forward. |
| **compress**  boolean | Whether you want CloudFront to automatically compress files.  **Choices:**   - `false` - `true` |
| **cookies**  dictionary | A dict that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. |
| **forward**  string | Specifies which cookies to forward to the origin for this cache behavior.  Valid values are `all`, `none`, or `whitelist`. |
| **whitelisted_names**  list / elements=string | A list of cookies to forward to the origin for this cache behavior. |
| **default_ttl**  integer | The default amount of time that you want objects to stay in CloudFront caches. |
| **field_level_encryption_id**  string | The field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data. |
| **headers**  list / elements=string | A list of headers to forward to the origin for this cache behavior.  To forward all headers use a list containing a single element ‘\*’ (`['*']`) |
| **lambda_function_associations**  list / elements=dictionary | A list of Lambda function associations to use for this cache behavior. |
| **event_type**  string | Specifies the event type that triggers a Lambda function invocation.  This can be `viewer-request`, `origin-request`, `origin-response` or `viewer-response`. |
| **lambda_function_arn**  string | The ARN of the Lambda function. |
| **max_ttl**  integer | The maximum amount of time that you want objects to stay in CloudFront caches. |
| **min_ttl**  integer | The minimum amount of time that you want objects to stay in CloudFront caches. |
| **query_string**  boolean | Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior.  **Choices:**   - `false` - `true` |
| **query_string_cache_keys**  list / elements=string | A list that contains the query string parameters you want CloudFront to use as a basis for caching for a cache behavior. |
| **smooth_streaming**  boolean | Whether you want to distribute media files in the Microsoft Smooth Streaming format.  **Choices:**   - `false` - `true` |
| **trusted_signers**  dictionary | A dict that specifies the AWS accounts that you want to allow to create signed URLs for private content. |
| **enabled**  boolean | Whether you want to require viewers to use signed URLs to access the files specified by *target_origin_id*  **Choices:**   - `false` - `true` |
| **items**  list / elements=string | A list of trusted signers for this cache behavior. |
| **viewer_protocol_policy**  string | The protocol that viewers can use to access the files in the origin specified by *target_origin_id*.  Valid values are `allow-all`, `redirect-to-https` and `https-only`. |
| **response_headers_policy_id**  string | The ID of the header policy that CloudFront adds to responses that it sends to viewers. |
| **target_origin_id**  string | The ID of the origin that you want CloudFront to route requests to by default. |
| **default_origin_domain_name**  string | The domain name to use for an origin if no *origins* have been specified.  Should only be used on a first run of generating a distribution and not on subsequent runs.  Should not be used in conjunction with *distribution_id*, *caller_reference* or *alias*. |
| **default_origin_path**  string | The default origin path to specify for an origin if no *origins* have been specified. Defaults to empty if not specified. |
| **default_root_object**  string | A config element that specifies the path to request when the user requests the origin.  e.g. if specified as ‘index.html’, this maps to www.example.com/index.html when www.example.com is called by the user.  This prevents the entire distribution origin from being exposed at the root. |
| **distribution_id**  string | The ID of the CloudFront distribution.  This parameter can be exchanged with *alias* or *caller_reference* and is used in conjunction with *e_tag*. |
| **e_tag**  string | A unique identifier of a modified or existing distribution. Used in conjunction with *distribution_id*.  Is determined automatically if not specified. |
| **enabled**  boolean | A boolean value that specifies whether the distribution is enabled or disabled.  Defaults to `false`.  **Choices:**   - `false` - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **http_version**  string | The version of the http protocol to use for the distribution.  AWS defaults this to `http2`.  Valid values are `http1.1`, `http2`, `http3` and `http2and3`. |
| **ipv6_enabled**  boolean | Determines whether IPv6 support is enabled or not.  Defaults to `false`.  **Choices:**   - `false` - `true` |
| **logging**  dictionary | A config element that is a complex object that defines logging for the distribution. |
| **bucket**  string | The S3 bucket to store the log in. |
| **enabled**  boolean | When *enabled=true* CloudFront will log access to an S3 bucket.  **Choices:**   - `false` - `true` |
| **include_cookies**  boolean | When *include_cookies=true* CloudFront will include cookies in the logs.  **Choices:**   - `false` - `true` |
| **prefix**  string | A prefix to include in the S3 object names. |
| **origins**  list / elements=dictionary | A config element that is a list of complex origin objects to be specified for the distribution. Used for creating and updating distributions. |
| **connection_attempts**  integer  *added in community.aws 6.0.0* | The number of times that CloudFront attempts to connect to the origin. The minimum number is `1`, the maximum is `3`.  **Default:** `3` |
| **connection_timeout**  integer  *added in community.aws 6.0.0* | The number of seconds that CloudFront waits when trying to establish a connection to the origin. The minimum timeout is `1` second, the maximum is `10` seconds.  **Default:** `10` |
| **custom_headers**  list / elements=dictionary | Custom headers you wish to add to the request before passing it to the origin.  For more information see the CloudFront documentation at <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html>. |
| **header_name**  string | The name of a header that you want CloudFront to forward to your origin. |
| **header_value**  string | The value for the header that you specified in the *header_name* field. |
| **custom_origin_config**  dictionary | Connection information about the origin. |
| **http_port**  integer | The HTTP port the custom origin listens on. |
| **https_port**  integer | The HTTPS port the custom origin listens on. |
| **origin_keepalive_timeout**  integer | A keep-alive timeout (in seconds). |
| **origin_protocol_policy**  string | The origin protocol policy to apply to your origin. |
| **origin_read_timeout**  integer | A timeout (in seconds) when reading from your origin. |
| **origin_ssl_protocols**  list / elements=string | A list of SSL/TLS protocols that you want CloudFront to use when communicating to the origin over HTTPS. |
| **domain_name**  string | The domain name which CloudFront will query as the origin.  For more information see the CloudFront documentation at <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesDomainName> |
| **id**  string | A unique identifier for the origin or origin group. *id* must be unique within the distribution. |
| **origin_path**  string | Tells CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. |
| **origin_shield**  dictionary  *added in community.aws 6.0.0* | Specify origin shield options for the origin. |
| **enabled**  boolean | Indicate whether you want the origin to have Origin Shield enabled or not.  **Choices:**   - `false` - `true` |
| **origin_shield_region**  string | Specify which AWS region will be used for Origin Shield. Required if Origin Shield is enabled. |
| **s3_origin_access_identity_enabled**  boolean | Use an origin access identity to configure the origin so that viewers can only access objects in an Amazon S3 bucket through CloudFront.  Will automatically create an Identity for you if no *s3_origin_config* is specified.  See also <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>.  **Choices:**   - `false` - `true` |
| **s3_origin_config**  dictionary | Specify origin access identity for S3 origins. |
| **origin_access_identity**  string | Existing origin access identity in the format `origin-access-identity/cloudfront/OID_ID`. |
| **price_class**  string | A string that specifies the pricing class of the distribution. As per <https://aws.amazon.com/cloudfront/pricing/>  *price_class=PriceClass_100* consists of the areas United States, Canada and Europe.  *price_class=PriceClass_200* consists of the areas United States, Canada, Europe, Japan, India, Hong Kong, Philippines, S. Korea, Singapore & Taiwan.  *price_class=PriceClass_All* consists of the areas United States, Canada, Europe, Japan, India, South America, Australia, Hong Kong, Philippines, S. Korea, Singapore & Taiwan.  AWS defaults this to `PriceClass_All`.  Valid values are `PriceClass_100`, `PriceClass_200` and `PriceClass_All` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_aliases**  boolean | Specifies whether existing aliases will be removed before adding new aliases.  When *purge_aliases=true*, existing aliases are removed and *aliases* are added.  **Choices:**   - `false` ← (default) - `true` |
| **purge_cache_behaviors**  boolean | Whether to remove any cache behaviors that aren’t listed in *cache_behaviors*.  This switch also allows the reordering of *cache_behaviors*.  **Choices:**   - `false` ← (default) - `true` |
| **purge_custom_error_responses**  boolean | Whether to remove any custom error responses that aren’t listed in *custom_error_responses*.  **Choices:**   - `false` ← (default) - `true` |
| **purge_origins**  boolean | Whether to remove any origins that aren’t listed in *origins*.  **Choices:**   - `false` ← (default) - `true` |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **restrictions**  dictionary | A config element that is a complex object that describes how a distribution should restrict it’s content. |
| **geo_restriction**  dictionary | Apply a restriction based on the location of the requester. |
| **items**  list / elements=string | A list of ISO 3166-1 two letter (Alpha 2) country codes that the restriction should apply to.  See the ISO website for a full list of codes <https://www.iso.org/obp/ui/#search/code/>. |
| **restriction_type**  string | The method that you want to use to restrict distribution of your content by country.  Valid values are `none`, `whitelist`, `blacklist`. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | The desired state of the distribution.  *state=present* creates a new distribution or updates an existing distribution.  *state=absent* deletes an existing distribution.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **viewer_certificate**  dictionary | A dict that specifies the encryption details of the distribution. |
| **acm_certificate_arn**  string | The ID of a certificate stored in ACM to use for HTTPS connections.  If *acm_certificate_id* is set then you must also specify *ssl_support_method*. |
| **cloudfront_default_certificate**  boolean | If you’re using the CloudFront domain name for your distribution, such as `123456789abcde.cloudfront.net` you should set *cloudfront_default_certificate=true*.  If *cloudfront_default_certificate=true* do not set *ssl_support_method*.  **Choices:**   - `false` - `true` |
| **iam_certificate_id**  string | The ID of a certificate stored in IAM to use for HTTPS connections.  If *iam_certificate_id* is set then you must also specify *ssl_support_method*. |
| **minimum_protocol_version**  string | The security policy that you want CloudFront to use for HTTPS connections.  See <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html> for supported security policies. |
| **ssl_support_method**  string | How CloudFront should serve SSL certificates.  Valid values are `sni-only` for SNI, and `vip` if CloudFront is configured to use a dedicated IP for your content. |
| **wait**  boolean | Specifies whether the module waits until the distribution has completed processing the creation or update.  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | Specifies the duration in seconds to wait for a timeout of a cloudfront create or update.  **Default:** `1800` |
| **web_acl_id**  string | The ID of a Web Application Firewall (WAF) Access Control List (ACL). |

## [Notes](cloudfront_distribution_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](cloudfront_distribution_module.md#id5)

```yaml+jinja
- name: create a basic distribution with defaults and tags
  community.aws.cloudfront_distribution:
    state: present
    default_origin_domain_name: www.my-cloudfront-origin.com
    tags:
      Name: example distribution
      Project: example project
      Priority: '1'

- name: update a distribution comment by distribution_id
  community.aws.cloudfront_distribution:
    state: present
    distribution_id: E1RP5A2MJ8073O
    comment: modified by ansible cloudfront.py

- name: update a distribution comment by caller_reference
  community.aws.cloudfront_distribution:
    state: present
    caller_reference: my cloudfront distribution 001
    comment: modified by ansible cloudfront.py

- name: update a distribution's aliases and comment using the distribution_id as a reference
  community.aws.cloudfront_distribution:
    state: present
    distribution_id: E1RP5A2MJ8073O
    comment: modified by cloudfront.py again
    aliases: [ 'www.my-distribution-source.com', 'zzz.aaa.io' ]

- name: update a distribution's aliases and comment using an alias as a reference
  community.aws.cloudfront_distribution:
    state: present
    caller_reference: my test distribution
    comment: modified by cloudfront.py again
    aliases:
      - www.my-distribution-source.com
      - zzz.aaa.io

- name: update a distribution's comment and aliases and tags and remove existing tags
  community.aws.cloudfront_distribution:
    state: present
    distribution_id: E15BU8SDCGSG57
    comment: modified by cloudfront.py again
    aliases:
      - tested.com
    tags:
      Project: distribution 1.2
    purge_tags: true

- name: create a distribution with an origin, logging and default cache behavior
  community.aws.cloudfront_distribution:
    state: present
    caller_reference: unique test distribution ID
    origins:
        - id: 'my test origin-000111'
          domain_name: www.example.com
          origin_path: /production
          custom_headers:
            - header_name: MyCustomHeaderName
              header_value: MyCustomHeaderValue
    default_cache_behavior:
      target_origin_id: 'my test origin-000111'
      forwarded_values:
        query_string: true
        cookies:
          forward: all
        headers:
         - '*'
      viewer_protocol_policy: allow-all
      smooth_streaming: true
      compress: true
      allowed_methods:
        items:
          - GET
          - HEAD
        cached_methods:
          - GET
          - HEAD
    logging:
      enabled: true
      include_cookies: false
      bucket: mylogbucket.s3.amazonaws.com
      prefix: myprefix/
    enabled: false
    comment: this is a CloudFront distribution with logging

- name: delete a distribution
  community.aws.cloudfront_distribution:
    state: absent
    caller_reference: replaceable distribution
```

## [Return Values](cloudfront_distribution_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **active_trusted_signers**  complex | Key pair IDs that CloudFront is aware of for each trusted signer.  **Returned:** always |
| **enabled**  boolean | Whether trusted signers are in use.  **Returned:** always  **Sample:** `false` |
| **items**  list / elements=string | Number of trusted signers.  **Returned:** when there are trusted signers  **Sample:** `["key_pair_id"]` |
| **quantity**  integer | Number of trusted signers.  **Returned:** always  **Sample:** `1` |
| **aliases**  complex | Aliases that refer to the distribution.  **Returned:** always |
| **items**  list / elements=string | List of aliases.  **Returned:** always  **Sample:** `["test.example.com"]` |
| **quantity**  integer | Number of aliases.  **Returned:** always  **Sample:** `1` |
| **arn**  string | Amazon Resource Name of the distribution.  **Returned:** always  **Sample:** `"arn:aws:cloudfront::123456789012:distribution/E1234ABCDEFGHI"` |
| **cache_behaviors**  complex | CloudFront cache behaviors.  **Returned:** always |
| **items**  complex | List of cache behaviors.  **Returned:** always |
| **allowed_methods**  complex | Methods allowed by the cache behavior.  **Returned:** always |
| **cached_methods**  complex | Methods cached by the cache behavior.  **Returned:** always |
| **items**  list / elements=string | List of cached methods.  **Returned:** always  **Sample:** `["HEAD", "GET"]` |
| **quantity**  integer | Count of cached methods.  **Returned:** always  **Sample:** `2` |
| **items**  list / elements=string | List of methods allowed by the cache behavior.  **Returned:** always  **Sample:** `["HEAD", "GET"]` |
| **quantity**  integer | Count of methods allowed by the cache behavior.  **Returned:** always  **Sample:** `2` |
| **compress**  boolean | Whether compression is turned on for the cache behavior.  **Returned:** always  **Sample:** `false` |
| **default_ttl**  integer | Default Time to Live of the cache behavior.  **Returned:** always  **Sample:** `86400` |
| **forwarded_values**  complex | Values forwarded to the origin for this cache behavior.  **Returned:** always |
| **cookies**  complex | Cookies to forward to the origin.  **Returned:** always |
| **forward**  string | Which cookies to forward to the origin for this cache behavior.  **Returned:** always  **Sample:** `"none"` |
| **whitelisted_names**  complex | The names of the cookies to forward to the origin for this cache behavior.  **Returned:** when *forward=whitelist* |
| **items**  list / elements=string | List of cookies to forward.  **Returned:** when list is not empty  **Sample:** `["my_cookie"]` |
| **quantity**  integer | Count of cookies to forward.  **Returned:** always  **Sample:** `1` |
| **headers**  complex | Which headers are used to vary on cache retrievals.  **Returned:** always |
| **items**  list / elements=string | List of headers to vary on.  **Returned:** when list is not empty  **Sample:** `["Host"]` |
| **quantity**  integer | Count of headers to vary on.  **Returned:** always  **Sample:** `1` |
| **query_string**  boolean | Whether the query string is used in cache lookups.  **Returned:** always  **Sample:** `false` |
| **query_string_cache_keys**  complex | Which query string keys to use in cache lookups.  **Returned:** always |
| **items**  list / elements=string | List of query string cache keys to use in cache lookups.  **Returned:** when list is not empty |
| **quantity**  integer | Count of query string cache keys to use in cache lookups.  **Returned:** always  **Sample:** `1` |
| **lambda_function_associations**  complex | Lambda function associations for a cache behavior.  **Returned:** always |
| **items**  list / elements=string | List of lambda function associations.  **Returned:** when list is not empty  **Sample:** `[{"event_type": "viewer-response", "lambda_function_arn": "arn:aws:lambda:123456789012:us-east-1/lambda/lambda-function"}]` |
| **quantity**  integer | Count of lambda function associations.  **Returned:** always  **Sample:** `1` |
| **max_ttl**  integer | Maximum Time to Live.  **Returned:** always  **Sample:** `31536000` |
| **min_ttl**  integer | Minimum Time to Live.  **Returned:** always  **Sample:** `0` |
| **path_pattern**  string | Path pattern that determines this cache behavior.  **Returned:** always  **Sample:** `"/path/to/files/*"` |
| **smooth_streaming**  boolean | Whether smooth streaming is enabled.  **Returned:** always  **Sample:** `false` |
| **target_origin_id**  string | ID of origin reference by this cache behavior.  **Returned:** always  **Sample:** `"origin_abcd"` |
| **trusted_signers**  complex | Trusted signers.  **Returned:** always |
| **enabled**  boolean | Whether trusted signers are enabled for this cache behavior.  **Returned:** always  **Sample:** `false` |
| **quantity**  integer | Count of trusted signers.  **Returned:** always  **Sample:** `1` |
| **viewer_protocol_policy**  string | Policy of how to handle http/https.  **Returned:** always  **Sample:** `"redirect-to-https"` |
| **quantity**  integer | Count of cache behaviors.  **Returned:** always  **Sample:** `1` |
| **caller_reference**  string | Idempotency reference given when creating CloudFront distribution.  **Returned:** always  **Sample:** `"1484796016700"` |
| **comment**  string | Any comments you want to include about the distribution.  **Returned:** always  **Sample:** `"my first CloudFront distribution"` |
| **custom_error_responses**  complex | Custom error responses to use for error handling.  **Returned:** always |
| **items**  complex | List of custom error responses.  **Returned:** always |
| **error_caching_min_ttl**  integer | Minimum time to cache this error response.  **Returned:** always  **Sample:** `300` |
| **error_code**  integer | Origin response code that triggers this error response.  **Returned:** always  **Sample:** `500` |
| **response_code**  string | Response code to return to the requester.  **Returned:** always  **Sample:** `"500"` |
| **response_page_path**  string | Path that contains the error page to display.  **Returned:** always  **Sample:** `"/errors/5xx.html"` |
| **quantity**  integer | Count of custom error response items  **Returned:** always  **Sample:** `1` |
| **default_cache_behavior**  complex | Default cache behavior.  **Returned:** always |
| **allowed_methods**  complex | Methods allowed by the cache behavior.  **Returned:** always |
| **cached_methods**  complex | Methods cached by the cache behavior.  **Returned:** always |
| **items**  list / elements=string | List of cached methods.  **Returned:** always  **Sample:** `["HEAD", "GET"]` |
| **quantity**  integer | Count of cached methods.  **Returned:** always  **Sample:** `2` |
| **items**  list / elements=string | List of methods allowed by the cache behavior.  **Returned:** always  **Sample:** `["HEAD", "GET"]` |
| **quantity**  integer | Count of methods allowed by the cache behavior.  **Returned:** always  **Sample:** `2` |
| **compress**  boolean | Whether compression is turned on for the cache behavior.  **Returned:** always  **Sample:** `false` |
| **default_ttl**  integer | Default Time to Live of the cache behavior.  **Returned:** always  **Sample:** `86400` |
| **forwarded_values**  complex | Values forwarded to the origin for this cache behavior.  **Returned:** always |
| **cookies**  complex | Cookies to forward to the origin.  **Returned:** always |
| **forward**  string | Which cookies to forward to the origin for this cache behavior.  **Returned:** always  **Sample:** `"none"` |
| **whitelisted_names**  complex | The names of the cookies to forward to the origin for this cache behavior.  **Returned:** when *forward=whitelist* |
| **items**  list / elements=string | List of cookies to forward.  **Returned:** when list is not empty  **Sample:** `["my_cookie"]` |
| **quantity**  integer | Count of cookies to forward.  **Returned:** always  **Sample:** `1` |
| **headers**  complex | Which headers are used to vary on cache retrievals.  **Returned:** always |
| **items**  list / elements=string | List of headers to vary on.  **Returned:** when list is not empty  **Sample:** `["Host"]` |
| **quantity**  integer | Count of headers to vary on.  **Returned:** always  **Sample:** `1` |
| **query_string**  boolean | Whether the query string is used in cache lookups.  **Returned:** always  **Sample:** `false` |
| **query_string_cache_keys**  complex | Which query string keys to use in cache lookups.  **Returned:** always |
| **items**  list / elements=string | List of query string cache keys to use in cache lookups.  **Returned:** when list is not empty |
| **quantity**  integer | Count of query string cache keys to use in cache lookups.  **Returned:** always  **Sample:** `1` |
| **lambda_function_associations**  complex | Lambda function associations for a cache behavior.  **Returned:** always |
| **items**  list / elements=string | List of lambda function associations.  **Returned:** when list is not empty  **Sample:** `[{"event_type": "viewer-response", "lambda_function_arn": "arn:aws:lambda:123456789012:us-east-1/lambda/lambda-function"}]` |
| **quantity**  integer | Count of lambda function associations.  **Returned:** always  **Sample:** `1` |
| **max_ttl**  integer | Maximum Time to Live.  **Returned:** always  **Sample:** `31536000` |
| **min_ttl**  integer | Minimum Time to Live.  **Returned:** always  **Sample:** `0` |
| **path_pattern**  string | Path pattern that determines this cache behavior.  **Returned:** always  **Sample:** `"/path/to/files/*"` |
| **smooth_streaming**  boolean | Whether smooth streaming is enabled.  **Returned:** always  **Sample:** `false` |
| **target_origin_id**  string | ID of origin reference by this cache behavior.  **Returned:** always  **Sample:** `"origin_abcd"` |
| **trusted_signers**  complex | Trusted signers.  **Returned:** always |
| **enabled**  boolean | Whether trusted signers are enabled for this cache behavior.  **Returned:** always  **Sample:** `false` |
| **quantity**  integer | Count of trusted signers.  **Returned:** always  **Sample:** `1` |
| **viewer_protocol_policy**  string | Policy of how to handle http/https.  **Returned:** always  **Sample:** `"redirect-to-https"` |
| **default_root_object**  string | The object that you want CloudFront to request from your origin (for example, index.html) when a viewer requests the root URL for your distribution.  **Returned:** always  **Sample:** `""` |
| **diff**  dictionary | Difference between previous configuration and new configuration.  **Returned:** always  **Sample:** `{}` |
| **domain_name**  string | Domain name of CloudFront distribution.  **Returned:** always  **Sample:** `"d1vz8pzgurxosf.cloudfront.net"` |
| **enabled**  boolean | Whether the CloudFront distribution is enabled or not.  **Returned:** always  **Sample:** `true` |
| **http_version**  string | Version of HTTP supported by the distribution.  **Returned:** always  **Sample:** `"http2"` |
| **id**  string | CloudFront distribution ID.  **Returned:** always  **Sample:** `"E123456ABCDEFG"` |
| **in_progress_invalidation_batches**  integer | The number of invalidation batches currently in progress.  **Returned:** always  **Sample:** `0` |
| **is_ipv6_enabled**  boolean | Whether IPv6 is enabled.  **Returned:** always  **Sample:** `true` |
| **last_modified_time**  string | Date and time distribution was last modified.  **Returned:** always  **Sample:** `"2017-10-13T01:51:12.656000+00:00"` |
| **logging**  complex | Logging information.  **Returned:** always |
| **bucket**  string | S3 bucket logging destination.  **Returned:** always  **Sample:** `"logs-example-com.s3.amazonaws.com"` |
| **enabled**  boolean | Whether logging is enabled.  **Returned:** always  **Sample:** `true` |
| **include_cookies**  boolean | Whether to log cookies.  **Returned:** always  **Sample:** `false` |
| **prefix**  string | Prefix added to logging object names.  **Returned:** always  **Sample:** `"cloudfront/test"` |
| **origins**  complex | Origins in the CloudFront distribution.  **Returned:** always |
| **items**  complex | List of origins.  **Returned:** always |
| **connection_attempts**  integer | The number of times that CloudFront attempts to connect to the origin.  **Returned:** always  **Sample:** `3` |
| **connection_timeout**  integer | The number of seconds that CloudFront waits when trying to establish a connection to the origin.  **Returned:** always  **Sample:** `10` |
| **custom_headers**  complex | Custom headers passed to the origin.  **Returned:** always |
| **quantity**  integer | Count of headers.  **Returned:** always  **Sample:** `1` |
| **custom_origin_config**  complex | Configuration of the origin.  **Returned:** always |
| **http_port**  integer | Port on which HTTP is listening.  **Returned:** always  **Sample:** `80` |
| **https_port**  integer | Port on which HTTPS is listening.  **Returned:** always  **Sample:** `443` |
| **origin_keepalive_timeout**  integer | Keep-alive timeout.  **Returned:** always  **Sample:** `5` |
| **origin_protocol_policy**  string | Policy of which protocols are supported.  **Returned:** always  **Sample:** `"https-only"` |
| **origin_read_timeout**  integer | Timeout for reads to the origin.  **Returned:** always  **Sample:** `30` |
| **origin_ssl_protocols**  complex | SSL protocols allowed by the origin.  **Returned:** always |
| **items**  list / elements=string | List of SSL protocols.  **Returned:** always  **Sample:** `["TLSv1", "TLSv1.1", "TLSv1.2"]` |
| **quantity**  integer | Count of SSL protocols.  **Returned:** always  **Sample:** `3` |
| **domain_name**  string | Domain name of the origin.  **Returned:** always  **Sample:** `"test-origin.example.com"` |
| **id**  string | ID of the origin.  **Returned:** always  **Sample:** `"test-origin.example.com"` |
| **origin_path**  string | Subdirectory to prefix the request from the S3 or HTTP origin.  **Returned:** always  **Sample:** `""` |
| **origin_shield**  complex  *added in community.aws 6.0.0* | Configuration of the origin Origin Shield.  **Returned:** always |
| **enabled**  boolean | Whether Origin Shield is enabled or not.  **Returned:** always  **Sample:** `false` |
| **origin_shield_region**  string | Which region is used by Origin Shield.  **Returned:** when enabled is true  **Sample:** `"us-east-1"` |
| **s3_origin_config**  dictionary | Origin access identity configuration for S3 Origin.  **Returned:** when s3_origin_access_identity_enabled is true |
| **origin_access_identity**  string | The origin access id as a path.  **Returned:** success  **Sample:** `"origin-access-identity/cloudfront/EXAMPLEID"` |
| **quantity**  integer | Count of origins.  **Returned:** always  **Sample:** `1` |
| **price_class**  string | Price class of CloudFront distribution.  **Returned:** always  **Sample:** `"PriceClass_All"` |
| **restrictions**  complex | Restrictions in use by CloudFront.  **Returned:** always |
| **geo_restriction**  complex | Controls the countries in which your content is distributed.  **Returned:** always |
| **items**  list / elements=string | List of country codes allowed or disallowed.  **Returned:** always  **Sample:** `["xy"]` |
| **quantity**  integer | Count of restrictions.  **Returned:** always  **Sample:** `1` |
| **restriction_type**  string | Type of restriction.  **Returned:** always  **Sample:** `"blacklist"` |
| **status**  string | Status of the CloudFront distribution.  **Returned:** always  **Sample:** `"InProgress"` |
| **tags**  dictionary | Distribution tags.  **Returned:** always  **Sample:** `{"Hello": "World"}` |
| **viewer_certificate**  complex | Certificate used by CloudFront distribution.  **Returned:** always |
| **acm_certificate_arn**  string | ARN of ACM certificate.  **Returned:** when certificate comes from ACM  **Sample:** `"arn:aws:acm:us-east-1:123456789012:certificate/abcd1234-1234-1234-abcd-123456abcdef"` |
| **certificate**  string | Reference to certificate.  **Returned:** always  **Sample:** `"arn:aws:acm:us-east-1:123456789012:certificate/abcd1234-1234-1234-abcd-123456abcdef"` |
| **certificate_source**  string | Where certificate comes from.  **Returned:** always  **Sample:** `"acm"` |
| **minimum_protocol_version**  string | Minimum SSL/TLS protocol supported by this distribution.  **Returned:** always  **Sample:** `"TLSv1"` |
| **ssl_support_method**  string | Support for pre-SNI browsers or not.  **Returned:** always  **Sample:** `"sni-only"` |
| **web_acl_id**  string | ID of Web Access Control List (from WAF service).  **Returned:** always  **Sample:** `"abcd1234-1234-abcd-abcd-abcd12345678"` |

### Authors

- Willem van Ketwich (@wilvk)
- Will Thames (@willthames)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
