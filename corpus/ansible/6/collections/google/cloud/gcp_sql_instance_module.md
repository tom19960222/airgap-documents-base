---
collection: ansible
version: "6"
title: "google.cloud.gcp_sql_instance module – Creates a GCP Instance"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_sql_instance_module.html
fetched_at: 2026-07-27T17:49:29+00:00
---
# google.cloud.gcp_sql_instance module – Creates a GCP Instance

> **Note:**
>
> This module is part of the [google.cloud collection](https://galaxy.ansible.com/google/cloud) (version 1.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install google.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](gcp_sql_instance_module.md#ansible-collections-google-cloud-gcp-sql-instance-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_sql_instance`.

- [Synopsis](gcp_sql_instance_module.md#synopsis)
- [Requirements](gcp_sql_instance_module.md#requirements)
- [Parameters](gcp_sql_instance_module.md#parameters)
- [Examples](gcp_sql_instance_module.md#examples)
- [Return Values](gcp_sql_instance_module.md#return-values)

## [Synopsis](gcp_sql_instance_module.md#id1)

- Represents a Cloud SQL instance. Cloud SQL instances are SQL databases hosted in Google’s cloud. The Instances resource provides methods for common configuration and management tasks.

## [Requirements](gcp_sql_instance_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_sql_instance_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **backend_type**  string | \* FIRST_GEN: First Generation instance. MySQL only.  \* SECOND_GEN: Second Generation instance or PostgreSQL instance.  \* EXTERNAL: A database server that is not managed by Google.  Some valid choices include: “FIRST_GEN”, “SECOND_GEN”, “EXTERNAL” |
| **connection_name**  string | Connection name of the Cloud SQL instance used in connection strings. |
| **database_version**  string | The database engine type and version. For First Generation instances, can be MYSQL_5_5, or MYSQL_5_6. For Second Generation instances, can be MYSQL_5_6 or MYSQL_5_7. Defaults to MYSQL_5_6.  PostgreSQL instances: POSTGRES_9_6 The databaseVersion property can not be changed after instance creation.  Some valid choices include: “MYSQL_5_5”, “MYSQL_5_6”, “MYSQL_5_7”, “POSTGRES_9_6” |
| **disk_encryption_configuration**  dictionary | Disk encryption settings. |
| **kms_key_name**  string | The KMS key used to encrypt the Cloud SQL instance . |
| **disk_encryption_status**  dictionary | Disk encryption status. |
| **kms_key_version_name**  string | The KMS key version used to encrypt the Cloud SQL instance . |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **failover_replica**  dictionary | The name and status of the failover replica. This property is applicable only to Second Generation instances. |
| **name**  string | The name of the failover replica. If specified at instance creation, a failover replica is created for the instance. The name doesn’t include the project ID. This property is applicable only to Second Generation instances. |
| **instance_type**  string | The instance type. This can be one of the following.  \* CLOUD_SQL_INSTANCE: A Cloud SQL instance that is not replicating from a master.  \* ON_PREMISES_INSTANCE: An instance running on the customer’s premises.  \* READ_REPLICA_INSTANCE: A Cloud SQL instance configured as a read-replica.  Some valid choices include: “CLOUD_SQL_INSTANCE”, “ON_PREMISES_INSTANCE”, “READ_REPLICA_INSTANCE” |
| **ipv6_address**  string | The IPv6 address assigned to the instance. This property is applicable only to First Generation instances. |
| **master_instance_name**  string | The name of the instance which will act as master in the replication setup. |
| **max_disk_size**  integer | The maximum disk size of the instance in bytes. |
| **name**  string / required | Name of the Cloud SQL instance. This does not include the project ID. |
| **project**  string | The Google Cloud Platform project to use. |
| **region**  string | The geographical region. Defaults to us-central or us-central1 depending on the instance type (First Generation or Second Generation/PostgreSQL). |
| **replica_configuration**  dictionary | Configuration specific to failover replicas and read replicas. |
| **failover_target**  boolean | Specifies if the replica is the failover target. If the field is set to true the replica will be designated as a failover replica.  In case the master instance fails, the replica instance will be promoted as the new master instance.  Only one replica can be specified as failover target, and the replica has to be in different zone with the master instance.  Choices:   - `false` - `true` |
| **mysql_replica_configuration**  dictionary | MySQL specific configuration when replicating from a MySQL on-premises master. Replication configuration information such as the username, password, certificates, and keys are not stored in the instance metadata. The configuration information is used only to set up the replication connection and is stored by MySQL in a file named master.info in the data directory. |
| **ca_certificate**  string | PEM representation of the trusted CA’s x509 certificate. |
| **client_certificate**  string | PEM representation of the replica’s x509 certificate . |
| **client_key**  string | PEM representation of the replica’s private key. The corresponding public key is encoded in the client’s certificate. |
| **connect_retry_interval**  integer | Seconds to wait between connect retries. MySQL’s default is 60 seconds. |
| **dump_file_path**  string | Path to a SQL dump file in Google Cloud Storage from which the replica instance is to be created. The URI is in the form gs://bucketName/fileName. Compressed gzip files (.gz) are also supported. Dumps should have the binlog coordinates from which replication should begin. This can be accomplished by setting –master-data to 1 when using mysqldump. |
| **master_heartbeat_period**  integer | Interval in milliseconds between replication heartbeats. |
| **password**  string | The password for the replication connection. |
| **ssl_cipher**  string | A list of permissible ciphers to use for SSL encryption. |
| **username**  string | The username for the replication connection. |
| **verify_server_certificate**  boolean | Whether or not to check the master’s Common Name value in the certificate that it sends during the SSL handshake.  Choices:   - `false` - `true` |
| **replica_names**  list / elements=string | The replicas of the instance. |
| **service_account_email_address**  string | The service account email address assigned to the instance. This property is applicable only to Second Generation instances. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **settings**  dictionary | The user settings. |
| **availability_type**  string | The availabilityType define if your postgres instance is run zonal or regional.  Some valid choices include: “ZONAL”, “REGIONAL” |
| **backup_configuration**  dictionary | The daily backup configuration for the instance. |
| **binary_log_enabled**  boolean | Whether binary log is enabled. If backup configuration is disabled, binary log must be disabled as well. MySQL only.  Choices:   - `false` - `true` |
| **enabled**  boolean | Enable Autobackup for your instance.  Choices:   - `false` - `true` |
| **start_time**  string | Define the backup start time in UTC (HH:MM) . |
| **database_flags**  list / elements=dictionary | The database flags passed to the instance at startup. |
| **name**  string | The name of the flag. These flags are passed at instance startup, so include both server options and system variables for MySQL. Flags should be specified with underscores, not hyphens. |
| **value**  string | The value of the flag. Booleans should be set to on for true and off for false. This field must be omitted if the flag doesn’t take a value. |
| **ip_configuration**  dictionary | The settings for IP Management. This allows to enable or disable the instance IP and manage which external networks can connect to the instance. The IPv4 address cannot be disabled for Second Generation instances. |
| **authorized_networks**  list / elements=dictionary | The list of external networks that are allowed to connect to the instance using the IP. In CIDR notation, also known as ‘slash’ notation (e.g. 192.168.100.0/24). |
| **expiration_time**  string | The time when this access control entry expires in RFC 3339 format, for example 2012-11-15T16:19:00.094Z. |
| **name**  string | An optional label to identify this entry. |
| **value**  string | The whitelisted value for the access control list. For example, to grant access to a client from an external IP (IPv4 or IPv6) address or subnet, use that address or subnet here. |
| **ipv4_enabled**  boolean | Whether the instance should be assigned an IP address or not.  Choices:   - `false` - `true` |
| **require_ssl**  boolean | Whether the mysqld should default to ‘REQUIRE X509’ for users connecting over IP.  Choices:   - `false` - `true` |
| **tier**  string | The tier or machine type for this instance, for example db-n1-standard-1. For MySQL instances, this field determines whether the instance is Second Generation (recommended) or First Generation. |
| **user_labels**  dictionary | User-provided labels, represented as a dictionary where each label is a single key value pair. |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |

## [Examples](gcp_sql_instance_module.md#id4)

```yaml+jinja
- name: create a instance
  google.cloud.gcp_sql_instance:
    name: "{{resource_name}}-2"
    settings:
      ip_configuration:
        authorized_networks:
        - name: google dns server
          value: 8.8.8.8/32
      tier: db-n1-standard-1
    region: us-central1
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_sql_instance_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backendType**  string | \* FIRST_GEN: First Generation instance. MySQL only.  \* SECOND_GEN: Second Generation instance or PostgreSQL instance.  \* EXTERNAL: A database server that is not managed by Google.  Returned: success |
| **connectionName**  string | Connection name of the Cloud SQL instance used in connection strings.  Returned: success |
| **databaseVersion**  string | The database engine type and version. For First Generation instances, can be MYSQL_5_5, or MYSQL_5_6. For Second Generation instances, can be MYSQL_5_6 or MYSQL_5_7. Defaults to MYSQL_5_6.  PostgreSQL instances: POSTGRES_9_6 The databaseVersion property can not be changed after instance creation.  Returned: success |
| **diskEncryptionConfiguration**  complex | Disk encryption settings.  Returned: success |
| **kmsKeyName**  string | The KMS key used to encrypt the Cloud SQL instance .  Returned: success |
| **diskEncryptionStatus**  complex | Disk encryption status.  Returned: success |
| **kmsKeyVersionName**  string | The KMS key version used to encrypt the Cloud SQL instance .  Returned: success |
| **failoverReplica**  complex | The name and status of the failover replica. This property is applicable only to Second Generation instances.  Returned: success |
| **available**  boolean | The availability status of the failover replica. A false status indicates that the failover replica is out of sync. The master can only failover to the failover replica when the status is true.  Returned: success |
| **name**  string | The name of the failover replica. If specified at instance creation, a failover replica is created for the instance. The name doesn’t include the project ID. This property is applicable only to Second Generation instances.  Returned: success |
| **gceZone**  string | The Compute Engine zone that the instance is currently serving from. This value could be different from the zone that was specified when the instance was created if the instance has failed over to its secondary zone.  Returned: success |
| **instanceType**  string | The instance type. This can be one of the following.  \* CLOUD_SQL_INSTANCE: A Cloud SQL instance that is not replicating from a master.  \* ON_PREMISES_INSTANCE: An instance running on the customer’s premises.  \* READ_REPLICA_INSTANCE: A Cloud SQL instance configured as a read-replica.  Returned: success |
| **ipAddresses**  complex | The assigned IP addresses for the instance.  Returned: success |
| **ipAddress**  string | The IP address assigned.  Returned: success |
| **timeToRetire**  string | The due time for this IP to be retired in RFC 3339 format, for example 2012-11-15T16:19:00.094Z. This field is only available when the IP is scheduled to be retired.  Returned: success |
| **type**  string | The type of this IP address. A PRIMARY address is an address that can accept incoming connections. An OUTGOING address is the source address of connections originating from the instance, if supported.  Returned: success |
| **ipv6Address**  string | The IPv6 address assigned to the instance. This property is applicable only to First Generation instances.  Returned: success |
| **masterInstanceName**  string | The name of the instance which will act as master in the replication setup.  Returned: success |
| **maxDiskSize**  integer | The maximum disk size of the instance in bytes.  Returned: success |
| **name**  string | Name of the Cloud SQL instance. This does not include the project ID.  Returned: success |
| **region**  string | The geographical region. Defaults to us-central or us-central1 depending on the instance type (First Generation or Second Generation/PostgreSQL).  Returned: success |
| **replicaConfiguration**  complex | Configuration specific to failover replicas and read replicas.  Returned: success |
| **failoverTarget**  boolean | Specifies if the replica is the failover target. If the field is set to true the replica will be designated as a failover replica.  In case the master instance fails, the replica instance will be promoted as the new master instance.  Only one replica can be specified as failover target, and the replica has to be in different zone with the master instance.  Returned: success |
| **mysqlReplicaConfiguration**  complex | MySQL specific configuration when replicating from a MySQL on-premises master. Replication configuration information such as the username, password, certificates, and keys are not stored in the instance metadata. The configuration information is used only to set up the replication connection and is stored by MySQL in a file named master.info in the data directory.  Returned: success |
| **caCertificate**  string | PEM representation of the trusted CA’s x509 certificate.  Returned: success |
| **clientCertificate**  string | PEM representation of the replica’s x509 certificate .  Returned: success |
| **clientKey**  string | PEM representation of the replica’s private key. The corresponding public key is encoded in the client’s certificate.  Returned: success |
| **connectRetryInterval**  integer | Seconds to wait between connect retries. MySQL’s default is 60 seconds.  Returned: success |
| **dumpFilePath**  string | Path to a SQL dump file in Google Cloud Storage from which the replica instance is to be created. The URI is in the form gs://bucketName/fileName. Compressed gzip files (.gz) are also supported. Dumps should have the binlog coordinates from which replication should begin. This can be accomplished by setting –master-data to 1 when using mysqldump.  Returned: success |
| **masterHeartbeatPeriod**  integer | Interval in milliseconds between replication heartbeats.  Returned: success |
| **password**  string | The password for the replication connection.  Returned: success |
| **sslCipher**  string | A list of permissible ciphers to use for SSL encryption.  Returned: success |
| **username**  string | The username for the replication connection.  Returned: success |
| **verifyServerCertificate**  boolean | Whether or not to check the master’s Common Name value in the certificate that it sends during the SSL handshake.  Returned: success |
| **replicaNames**  list / elements=string | The replicas of the instance.  Returned: success |
| **serviceAccountEmailAddress**  string | The service account email address assigned to the instance. This property is applicable only to Second Generation instances.  Returned: success |
| **serverCaCert**  complex | SSL configuration.  Returned: success |
| **cert**  string | PEM representation of the X.509 certificate.  Returned: success |
| **certSerialNumber**  string | Serial number, as extracted from the certificate.  Returned: success |
| **commonName**  string | User supplied name. Constrained to [a-zA-Z.-_ ]+.  Returned: success |
| **createTime**  string | The time when the certificate was created in RFC 3339 format, for example 2012-11-15T16:19:00.094Z.  Returned: success |
| **expirationTime**  string | The time when the certificate expires in RFC 3339 format, for example 2012-11-15T16:19:00.094Z.  Returned: success |
| **sha1Fingerprint**  string | SHA-1 fingerprint of the certificate.  Returned: success |
| **settings**  complex | The user settings.  Returned: success |
| **availabilityType**  string | The availabilityType define if your postgres instance is run zonal or regional.  Returned: success |
| **backupConfiguration**  complex | The daily backup configuration for the instance.  Returned: success |
| **binaryLogEnabled**  boolean | Whether binary log is enabled. If backup configuration is disabled, binary log must be disabled as well. MySQL only.  Returned: success |
| **enabled**  boolean | Enable Autobackup for your instance.  Returned: success |
| **startTime**  string | Define the backup start time in UTC (HH:MM) .  Returned: success |
| **databaseFlags**  complex | The database flags passed to the instance at startup.  Returned: success |
| **name**  string | The name of the flag. These flags are passed at instance startup, so include both server options and system variables for MySQL. Flags should be specified with underscores, not hyphens.  Returned: success |
| **value**  string | The value of the flag. Booleans should be set to on for true and off for false. This field must be omitted if the flag doesn’t take a value.  Returned: success |
| **ipConfiguration**  complex | The settings for IP Management. This allows to enable or disable the instance IP and manage which external networks can connect to the instance. The IPv4 address cannot be disabled for Second Generation instances.  Returned: success |
| **authorizedNetworks**  complex | The list of external networks that are allowed to connect to the instance using the IP. In CIDR notation, also known as ‘slash’ notation (e.g. 192.168.100.0/24).  Returned: success |
| **expirationTime**  string | The time when this access control entry expires in RFC 3339 format, for example 2012-11-15T16:19:00.094Z.  Returned: success |
| **name**  string | An optional label to identify this entry.  Returned: success |
| **value**  string | The whitelisted value for the access control list. For example, to grant access to a client from an external IP (IPv4 or IPv6) address or subnet, use that address or subnet here.  Returned: success |
| **ipv4Enabled**  boolean | Whether the instance should be assigned an IP address or not.  Returned: success |
| **requireSsl**  boolean | Whether the mysqld should default to ‘REQUIRE X509’ for users connecting over IP.  Returned: success |
| **settingsVersion**  integer | The version of instance settings. This is a required field for update method to make sure concurrent updates are handled properly.  During update, use the most recent settingsVersion value for this instance and do not try to update this value.  Returned: success |
| **tier**  string | The tier or machine type for this instance, for example db-n1-standard-1. For MySQL instances, this field determines whether the instance is Second Generation (recommended) or First Generation.  Returned: success |
| **userLabels**  dictionary | User-provided labels, represented as a dictionary where each label is a single key value pair.  Returned: success |
| **state**  string | The current serving state of the database instance.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
