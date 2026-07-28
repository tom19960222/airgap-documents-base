---
collection: ansible
version: "6"
title: "community.grafana.grafana_datasource module – Manage Grafana datasources"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/grafana/grafana_datasource_module.html
fetched_at: 2026-07-27T17:15:26+00:00
---
# community.grafana.grafana_datasource module – Manage Grafana datasources

> **Note:**
>
> This module is part of the [community.grafana collection](https://galaxy.ansible.com/community/grafana) (version 1.5.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.grafana`.
>
> To use it in a playbook, specify: `community.grafana.grafana_datasource`.

- [Synopsis](grafana_datasource_module.md#synopsis)
- [Parameters](grafana_datasource_module.md#parameters)
- [Notes](grafana_datasource_module.md#notes)
- [Examples](grafana_datasource_module.md#examples)
- [Return Values](grafana_datasource_module.md#return-values)

## [Synopsis](grafana_datasource_module.md#id1)

- Create/update/delete Grafana datasources via API.

## [Parameters](grafana_datasource_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access**  string | The access mode for this datasource.  Choices:   - `"direct"` - `"proxy"` ← (default) |
| **additional_json_data**  dictionary | Defined data is used for datasource jsonData  Data may be overridden by specifically defined parameters (like zabbix_user)  Default: `{}` |
| **additional_secure_json_data**  dictionary | Defined data is used for datasource secureJsonData  Data may be overridden by specifically defined parameters (like tls_client_cert)  Stored as secure data, see `enforce_secure_data` and notes!  Default: `{}` |
| **aws_access_key**  string | AWS access key for CloudWatch datasource type when `aws_auth_type` is `keys`  Stored as secure data, see `enforce_secure_data` and notes!  Default: `""` |
| **aws_assume_role_arn**  string | AWS IAM role arn to assume for CloudWatch datasource type when `aws_auth_type` is `arn`  Default: `""` |
| **aws_auth_type**  string | Type for AWS authentication for CloudWatch datasource type (authType of grafana api)  Choices:   - `"keys"` ← (default) - `"credentials"` - `"arn"` - `"default"` |
| **aws_credentials_profile**  string | Profile for AWS credentials for CloudWatch datasource type when `aws_auth_type` is `credentials`  Default: `""` |
| **aws_custom_metrics_namespaces**  string | Namespaces of Custom Metrics for CloudWatch datasource type  Default: `""` |
| **aws_default_region**  string | AWS default region for CloudWatch datasource type  Choices:   - `"ap-northeast-1"` - `"ap-northeast-2"` - `"ap-southeast-1"` - `"ap-southeast-2"` - `"ap-south-1"` - `"ca-central-1"` - `"cn-north-1"` - `"cn-northwest-1"` - `"eu-central-1"` - `"eu-west-1"` - `"eu-west-2"` - `"eu-west-3"` - `"sa-east-1"` - `"us-east-1"` ← (default) - `"us-east-2"` - `"us-gov-west-1"` - `"us-west-1"` - `"us-west-2"` |
| **aws_secret_key**  string | AWS secret key for CloudWatch datasource type when `aws_auth_type` is `keys`  Stored as secure data, see `enforce_secure_data` and notes!  Default: `""` |
| **azure_client**  string | The application/client ID for the Azure AD app registration to use for authentication. |
| **azure_cloud**  string | The national cloud for your Azure account  Choices:   - `"azuremonitor"` ← (default) - `"chinaazuremonitor"` - `"govazuremonitor"` - `"germanyazuremonitor"` |
| **azure_secret**  string | The application client secret for the Azure AD app registration to use for auth |
| **azure_tenant**  string | The directory/tenant ID for the Azure AD app registration to use for authentication |
| **basic_auth_password**  string | The datasource basic auth password, when `basic auth` is `yes`.  Stored as secure data, see `enforce_secure_data` and notes! |
| **basic_auth_user**  string | The datasource basic auth user.  Setting this option with basic_auth_password will enable basic auth. |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, *client_key* is not required |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If *client_cert* contains both the certificate and key, this option is not required. |
| **database**  string | Name of the database for the datasource.  This options is required when the `ds_type` is `influxdb`, `elasticsearch` (index name), `mysql` or `postgres`. |
| **ds_type**  string | The type of the datasource.  Required when `state=present`.  Choices:   - `"graphite"` - `"prometheus"` - `"elasticsearch"` - `"influxdb"` - `"opentsdb"` - `"mysql"` - `"postgres"` - `"cloudwatch"` - `"alexanderzobnin-zabbix-datasource"` - `"grafana-azure-monitor-datasource"` - `"sni-thruk-datasource"` - `"camptocamp-prometheus-alertmanager-datasource"` - `"loki"` - `"redis-datasource"` |
| **ds_url**  string | The URL of the datasource.  Required when `state=present`. |
| **enforce_secure_data**  boolean | Secure data is not updated per default (see notes!)  To update secure data you have to enable this option!  Enabling this, the task will always report changed=True  Choices:   - `false` ← (default) - `true` |
| **es_version**  string | Elasticsearch version (for `ds_type = elasticsearch` only)  Version 56 is for elasticsearch 5.6+ where you can specify the `max_concurrent_shard_requests` option.  Choices:   - `"2"` - `"5"` - `"56"` - `"60"` - `"70"` - `"7.7+"` - `"7.10+"` ← (default) - `"8.0+"` |
| **grafana_api_key**  string | The Grafana API key.  If set, `url_username` and `url_password` will be ignored. |
| **interval**  string | For elasticsearch `ds_type`, this is the index pattern used.  Choices:   - `""` - `"Hourly"` - `"Daily"` - `"Weekly"` - `"Monthly"` - `"Yearly"` |
| **is_default**  boolean | Make this datasource the default one.  Choices:   - `false` ← (default) - `true` |
| **max_concurrent_shard_requests**  integer | Starting with elasticsearch 5.6, you can specify the max concurrent shard per requests.  Default: `256` |
| **name**  string / required | The name of the datasource. |
| **org_id**  integer | Grafana Organisation ID in which the datasource should be created.  Not used when `grafana_api_key` is set, because the `grafana_api_key` only belong to one organisation.  Default: `1` |
| **password**  string | The datasource password.  Stored as secure data, see `enforce_secure_data` and notes! |
| **sslmode**  string | SSL mode for `postgres` datasource type.  Choices:   - `"disable"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **state**  string | Status of the datasource  Choices:   - `"absent"` - `"present"` ← (default) |
| **time_field**  string | Name of the time field in elasticsearch ds.  For example `@timestamp`.  Default: `"@timestamp"` |
| **time_interval**  string | Minimum group by interval for `influxdb` or `elasticsearch` datasources.  for example `>10s`. |
| **tls_ca_cert**  string | The TLS CA certificate for self signed certificates.  Only used when `tls_client_cert` and `tls_client_key` are set.  Stored as secure data, see `enforce_secure_data` and notes! |
| **tls_client_cert**  string | The client TLS certificate.  If `tls_client_cert` and `tls_client_key` are set, this will enable TLS authentication.  Starts with —– BEGIN CERTIFICATE —–  Stored as secure data, see `enforce_secure_data` and notes! |
| **tls_client_key**  string | The client TLS private key  Starts with —– BEGIN RSA PRIVATE KEY —–  Stored as secure data, see `enforce_secure_data` and notes! |
| **tls_skip_verify**  boolean | Skip the TLS datasource certificate verification.  Choices:   - `false` ← (default) - `true` |
| **trends**  boolean | Use trends or not for zabbix datasource type.  Choices:   - `false` ← (default) - `true` |
| **tsdb_resolution**  string | The opentsdb time resolution.  Choices:   - `"millisecond"` - `"second"` ← (default) |
| **tsdb_version**  integer | The opentsdb version.  Use `1` for <=2.1, `2` for ==2.2, `3` for ==2.3.  Choices:   - `1` ← (default) - `2` - `3` |
| **url**  aliases: grafana_url  string / required | The Grafana URL. |
| **url_password**  aliases: grafana_password  string | The Grafana password for API authentication.  Default: `"admin"` |
| **url_username**  aliases: grafana_user  string | The Grafana user for API authentication.  Default: `"admin"` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` - `true` ← (default) |
| **user**  string | The datasource login user for influxdb datasources. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **with_credentials**  boolean | Whether credentials such as cookies or auth headers should be sent with cross-site requests.  Choices:   - `false` ← (default) - `true` |
| **zabbix_password**  string | Password for Zabbix API |
| **zabbix_user**  string | User for Zabbix API |

## [Notes](grafana_datasource_module.md#id3)

> **Note:**
>
> - Secure data will get encrypted by the Grafana API, thus it can not be compared on subsequent runs. To workaround this, secure data will not be updated after initial creation! To force the secure data update you have to set *enforce_secure_data=True*.
> - Hint, with the `enforce_secure_data` always reporting changed=True, you might just do one Task updating the datasource without any secure data and make a separate playbook/task also changing the secure data. This way it will not break any workflow.

## [Examples](grafana_datasource_module.md#id4)

```yaml+jinja
---
- name: Create elasticsearch datasource
  community.grafana.grafana_datasource:
    name: "datasource-elastic"
    grafana_url: "https://grafana.company.com"
    grafana_user: "admin"
    grafana_password: "xxxxxx"
    org_id: "1"
    ds_type: "elasticsearch"
    ds_url: "https://elastic.company.com:9200"
    database: "[logstash_]YYYY.MM.DD"
    basic_auth_user: "grafana"
    basic_auth_password: "******"
    time_field: "@timestamp"
    time_interval: "1m"
    interval: "Daily"
    es_version: 56
    max_concurrent_shard_requests: 42
    tls_ca_cert: "/etc/ssl/certs/ca.pem"

- name: Create influxdb datasource
  community.grafana.grafana_datasource:
    name: "datasource-influxdb"
    grafana_url: "https://grafana.company.com"
    grafana_user: "admin"
    grafana_password: "xxxxxx"
    org_id: "1"
    ds_type: "influxdb"
    ds_url: "https://influx.company.com:8086"
    database: "telegraf"
    time_interval: ">10s"
    tls_ca_cert: "/etc/ssl/certs/ca.pem"

- name: Create postgres datasource
  community.grafana.grafana_datasource:
    name: "datasource-postgres"
    grafana_url: "https://grafana.company.com"
    grafana_user: "admin"
    grafana_password: "xxxxxx"
    org_id: "1"
    ds_type: "postgres"
    ds_url: "postgres.company.com:5432"
    database: "db"
    user: "postgres"
    sslmode: "verify-full"
    additional_json_data:
      postgresVersion: 12
      timescaledb: false
    additional_secure_json_data:
      password: "iampgroot"

- name: Create cloudwatch datasource
  community.grafana.grafana_datasource:
    name: "datasource-cloudwatch"
    grafana_url: "https://grafana.company.com"
    grafana_user: "admin"
    grafana_password: "xxxxxx"
    org_id: "1"
    ds_type: "cloudwatch"
    ds_url: "http://monitoring.us-west-1.amazonaws.com"
    aws_auth_type: "keys"
    aws_default_region: "us-west-1"
    aws_access_key: "speakFriendAndEnter"
    aws_secret_key: "mel10n"
    aws_custom_metrics_namespaces: "n1,n2"

- name: grafana - add thruk datasource
  community.grafana.grafana_datasource:
    name: "datasource-thruk"
    grafana_url: "https://grafana.company.com"
    grafana_user: "admin"
    grafana_password: "xxxxxx"
    org_id: "1"
    ds_type: "sni-thruk-datasource"
    ds_url: "https://thruk.company.com/sitename/thruk"
    basic_auth_user: "thruk-user"
    basic_auth_password: "******"

# handle secure data - workflow example
# this will create/update the datasource but dont update the secure data on updates
# so you can assert if all tasks are changed=False
- name: create prometheus datasource
  community.grafana.grafana_datasource:
    name: openshift_prometheus
    ds_type: prometheus
    ds_url: https://openshift-monitoring.company.com
    access: proxy
    tls_skip_verify: true
    additional_json_data:
      httpHeaderName1: "Authorization"
    additional_secure_json_data:
      httpHeaderValue1: "Bearer ihavenogroot"

# in a separate task or even play you then can force to update
# and assert if each datasource is reporting changed=True
- name: update prometheus datasource
  community.grafana.grafana_datasource:
    name: openshift_prometheus
    ds_type: prometheus
    ds_url: https://openshift-monitoring.company.com
    access: proxy
    tls_skip_verify: true
    additional_json_data:
      httpHeaderName1: "Authorization"
    additional_secure_json_data:
      httpHeaderValue1: "Bearer ihavenogroot"
    enforce_secure_data: true
```

## [Return Values](grafana_datasource_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **datasource**  dictionary | datasource created/updated by module  Returned: changed  Sample: `{"access": "proxy", "basicAuth": false, "database": "test_*", "id": 1035, "isDefault": false, "jsonData": {"esVersion": 5, "timeField": "@timestamp", "timeInterval": "10s"}, "name": "grafana_datasource_test", "orgId": 1, "password": "", "secureJsonFields": {"JustASecureTest": true}, "type": "elasticsearch", "url": "http://elastic.company.com:9200", "user": "", "withCredentials": false}` |

### Authors

- Thierry Sallé (@seuf)
- Martin Wang (@martinwangjian)
- Rémi REY (@rrey)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/grafana/issues)
[Homepage](https://github.com/ansible-collections/grafana)
[Repository (Sources)](https://github.com/ansible-collections/grafana.git)
