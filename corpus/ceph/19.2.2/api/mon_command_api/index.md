---
collection: ceph
version: "19.2.2"
title: "cephadm"
source_url: https://docs.ceph.com/en/squid/api/mon_command_api/
fetched_at: 2026-07-27T16:40:57+00:00
---
# cephadm

## cephadm check-host

Check whether we can access and manage a remote host

Example command:
:   ```bash
    ceph cephadm check-host my_host my_addr
    ```

Parameters:
:   - **host**: (string)
    - **addr**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## cephadm clear-key

Clear cluster SSH key

Example command:
:   ```bash
    ceph cephadm clear-key
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## cephadm clear-ssh-config

Clear the ssh_config file

Example command:
:   ```bash
    ceph cephadm clear-ssh-config
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## cephadm config-check disable

Disable a specific configuration check

Example command:
:   ```bash
    ceph cephadm config-check disable my_check_name
    ```

Parameters:
:   - **check_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## cephadm config-check enable

Enable a specific configuration check

Example command:
:   ```bash
    ceph cephadm config-check enable my_check_name
    ```

Parameters:
:   - **check_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## cephadm config-check ls

List the available configuration checks and their current state

Example command:
:   ```bash
    ceph cephadm config-check ls plain
    ```

Parameters:
:   - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## cephadm config-check status

Show whether the configuration checker feature is enabled/disabled

Example command:
:   ```bash
    ceph cephadm config-check status
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## cephadm generate-key

Generate a cluster SSH key (if not present)

Example command:
:   ```bash
    ceph cephadm generate-key
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## cephadm get-extra-ceph-conf

Get extra ceph conf that is appended

Example command:
:   ```bash
    ceph cephadm get-extra-ceph-conf
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## cephadm get-pub-key

Show SSH public key for connecting to cluster hosts

Example command:
:   ```bash
    ceph cephadm get-pub-key
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## cephadm get-signed-cert

Show SSH signed cert for connecting to cluster hosts using CA signed
keys

Example command:
:   ```bash
    ceph cephadm get-signed-cert
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## cephadm get-ssh-config

Returns the ssh config as used by cephadm

Example command:
:   ```bash
    ceph cephadm get-ssh-config
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## cephadm get-user

Show user for SSHing to cluster hosts

Example command:
:   ```bash
    ceph cephadm get-user
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## cephadm osd activate

Start OSD containers for existing OSDs

Example command:
:   ```bash
    ceph cephadm osd activate --host=string
    ```

Parameters:
:   - **host**: (can be repeated)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## cephadm prepare-host

Prepare a remote host for use with cephadm

Example command:
:   ```bash
    ceph cephadm prepare-host my_host my_addr
    ```

Parameters:
:   - **host**: (string)
    - **addr**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## cephadm registry-login

Set custom registry login info by providing url, username and password
or json file with login info (-i <file>)

Example command:
:   ```bash
    ceph cephadm registry-login my_url my_username my_password
    ```

Parameters:
:   - **url**: (string)
    - **username**: (string)
    - **password**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## cephadm set-extra-ceph-conf

Text that is appended to all daemon’s ceph.conf. Mainly a workaround,
till config generate-minimal-conf generates a complete ceph.conf.
Warning: this is a dangerous operation.

Example command:
:   ```bash
    ceph cephadm set-extra-ceph-conf
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## cephadm set-priv-key

Set cluster SSH private key (use -i <private_key>)

Example command:
:   ```bash
    ceph cephadm set-priv-key
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## cephadm set-pub-key

Set cluster SSH public key (use -i <public_key>)

Example command:
:   ```bash
    ceph cephadm set-pub-key
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## cephadm set-signed-cert

Set a signed cert if CA signed keys are being used (use -i
<cert_filename>)

Example command:
:   ```bash
    ceph cephadm set-signed-cert
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## cephadm set-ssh-config

Set the ssh_config file (use -i <ssh_config>)

Example command:
:   ```bash
    ceph cephadm set-ssh-config
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## cephadm set-user

Set user for SSHing to cluster hosts, passwordless sudo will be needed
for non-root users

Example command:
:   ```bash
    ceph cephadm set-user my_user
    ```

Parameters:
:   - **user**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## cephadm systemd-unit ls

Example command:
:   ```bash
    ceph cephadm systemd-unit ls my_hostname my_daemon_type my_daemon_id
    ```

Parameters:
:   - **hostname**: (string)
    - **daemon_type**: (string)
    - **daemon_id**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

# dashboard

## dashboard create-self-signed-cert

Create self signed certificate

Example command:
:   ```bash
    ceph dashboard create-self-signed-cert
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard get-account-lockout-attempts

Get the ACCOUNT_LOCKOUT_ATTEMPTS option value

Example command:
:   ```bash
    ceph dashboard get-account-lockout-attempts
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-alertmanager-api-host

Get the ALERTMANAGER_API_HOST option value

Example command:
:   ```bash
    ceph dashboard get-alertmanager-api-host
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-alertmanager-api-ssl-verify

Get the ALERTMANAGER_API_SSL_VERIFY option value

Example command:
:   ```bash
    ceph dashboard get-alertmanager-api-ssl-verify
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-audit-api-enabled

Get the AUDIT_API_ENABLED option value

Example command:
:   ```bash
    ceph dashboard get-audit-api-enabled
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-audit-api-log-payload

Get the AUDIT_API_LOG_PAYLOAD option value

Example command:
:   ```bash
    ceph dashboard get-audit-api-log-payload
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-enable-browsable-api

Get the ENABLE_BROWSABLE_API option value

Example command:
:   ```bash
    ceph dashboard get-enable-browsable-api
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-ganesha-clusters-rados-pool-namespace

Get the GANESHA_CLUSTERS_RADOS_POOL_NAMESPACE option value

Example command:
:   ```bash
    ceph dashboard get-ganesha-clusters-rados-pool-namespace
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-grafana-api-password

Get the GRAFANA_API_PASSWORD option value

Example command:
:   ```bash
    ceph dashboard get-grafana-api-password
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-grafana-api-ssl-verify

Get the GRAFANA_API_SSL_VERIFY option value

Example command:
:   ```bash
    ceph dashboard get-grafana-api-ssl-verify
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-grafana-api-url

Get the GRAFANA_API_URL option value

Example command:
:   ```bash
    ceph dashboard get-grafana-api-url
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-grafana-api-username

Get the GRAFANA_API_USERNAME option value

Example command:
:   ```bash
    ceph dashboard get-grafana-api-username
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-grafana-frontend-api-url

Get the GRAFANA_FRONTEND_API_URL option value

Example command:
:   ```bash
    ceph dashboard get-grafana-frontend-api-url
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-grafana-update-dashboards

Get the GRAFANA_UPDATE_DASHBOARDS option value

Example command:
:   ```bash
    ceph dashboard get-grafana-update-dashboards
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-iscsi-api-ssl-verification

Get the ISCSI_API_SSL_VERIFICATION option value

Example command:
:   ```bash
    ceph dashboard get-iscsi-api-ssl-verification
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-issue-tracker-api-key

Get the ISSUE_TRACKER_API_KEY option value

Example command:
:   ```bash
    ceph dashboard get-issue-tracker-api-key
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-jwt-token-ttl

Get the JWT token TTL in seconds

Example command:
:   ```bash
    ceph dashboard get-jwt-token-ttl
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-prometheus-api-host

Get the PROMETHEUS_API_HOST option value

Example command:
:   ```bash
    ceph dashboard get-prometheus-api-host
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-prometheus-api-ssl-verify

Get the PROMETHEUS_API_SSL_VERIFY option value

Example command:
:   ```bash
    ceph dashboard get-prometheus-api-ssl-verify
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-pwd-policy-check-complexity-enabled

Get the PWD_POLICY_CHECK_COMPLEXITY_ENABLED option value

Example command:
:   ```bash
    ceph dashboard get-pwd-policy-check-complexity-enabled
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-pwd-policy-check-exclusion-list-enabled

Get the PWD_POLICY_CHECK_EXCLUSION_LIST_ENABLED option value

Example command:
:   ```bash
    ceph dashboard get-pwd-policy-check-exclusion-list-enabled
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-pwd-policy-check-length-enabled

Get the PWD_POLICY_CHECK_LENGTH_ENABLED option value

Example command:
:   ```bash
    ceph dashboard get-pwd-policy-check-length-enabled
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-pwd-policy-check-oldpwd-enabled

Get the PWD_POLICY_CHECK_OLDPWD_ENABLED option value

Example command:
:   ```bash
    ceph dashboard get-pwd-policy-check-oldpwd-enabled
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-pwd-policy-check-repetitive-chars-enabled

Get the PWD_POLICY_CHECK_REPETITIVE_CHARS_ENABLED option value

Example command:
:   ```bash
    ceph dashboard get-pwd-policy-check-repetitive-chars-enabled
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-pwd-policy-check-sequential-chars-enabled

Get the PWD_POLICY_CHECK_SEQUENTIAL_CHARS_ENABLED option value

Example command:
:   ```bash
    ceph dashboard get-pwd-policy-check-sequential-chars-enabled
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-pwd-policy-check-username-enabled

Get the PWD_POLICY_CHECK_USERNAME_ENABLED option value

Example command:
:   ```bash
    ceph dashboard get-pwd-policy-check-username-enabled
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-pwd-policy-enabled

Get the PWD_POLICY_ENABLED option value

Example command:
:   ```bash
    ceph dashboard get-pwd-policy-enabled
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-pwd-policy-exclusion-list

Get the PWD_POLICY_EXCLUSION_LIST option value

Example command:
:   ```bash
    ceph dashboard get-pwd-policy-exclusion-list
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-pwd-policy-min-complexity

Get the PWD_POLICY_MIN_COMPLEXITY option value

Example command:
:   ```bash
    ceph dashboard get-pwd-policy-min-complexity
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-pwd-policy-min-length

Get the PWD_POLICY_MIN_LENGTH option value

Example command:
:   ```bash
    ceph dashboard get-pwd-policy-min-length
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-rest-requests-timeout

Get the REST_REQUESTS_TIMEOUT option value

Example command:
:   ```bash
    ceph dashboard get-rest-requests-timeout
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-rgw-api-access-key

Get the RGW_API_ACCESS_KEY option value

Example command:
:   ```bash
    ceph dashboard get-rgw-api-access-key
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-rgw-api-admin-resource

Get the RGW_API_ADMIN_RESOURCE option value

Example command:
:   ```bash
    ceph dashboard get-rgw-api-admin-resource
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-rgw-api-secret-key

Get the RGW_API_SECRET_KEY option value

Example command:
:   ```bash
    ceph dashboard get-rgw-api-secret-key
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-rgw-api-ssl-verify

Get the RGW_API_SSL_VERIFY option value

Example command:
:   ```bash
    ceph dashboard get-rgw-api-ssl-verify
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-user-pwd-expiration-span

Get the USER_PWD_EXPIRATION_SPAN option value

Example command:
:   ```bash
    ceph dashboard get-user-pwd-expiration-span
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-user-pwd-expiration-warning-1

Get the USER_PWD_EXPIRATION_WARNING_1 option value

Example command:
:   ```bash
    ceph dashboard get-user-pwd-expiration-warning-1
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard get-user-pwd-expiration-warning-2

Get the USER_PWD_EXPIRATION_WARNING_2 option value

Example command:
:   ```bash
    ceph dashboard get-user-pwd-expiration-warning-2
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard grafana dashboards update

Push dashboards to Grafana

Example command:
:   ```bash
    ceph dashboard grafana dashboards update
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-account-lockout-attempts

Reset the ACCOUNT_LOCKOUT_ATTEMPTS option to its default value

Example command:
:   ```bash
    ceph dashboard reset-account-lockout-attempts
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-alertmanager-api-host

Reset the ALERTMANAGER_API_HOST option to its default value

Example command:
:   ```bash
    ceph dashboard reset-alertmanager-api-host
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-alertmanager-api-ssl-verify

Reset the ALERTMANAGER_API_SSL_VERIFY option to its default value

Example command:
:   ```bash
    ceph dashboard reset-alertmanager-api-ssl-verify
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-audit-api-enabled

Reset the AUDIT_API_ENABLED option to its default value

Example command:
:   ```bash
    ceph dashboard reset-audit-api-enabled
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-audit-api-log-payload

Reset the AUDIT_API_LOG_PAYLOAD option to its default value

Example command:
:   ```bash
    ceph dashboard reset-audit-api-log-payload
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-enable-browsable-api

Reset the ENABLE_BROWSABLE_API option to its default value

Example command:
:   ```bash
    ceph dashboard reset-enable-browsable-api
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-ganesha-clusters-rados-pool-namespace

Reset the GANESHA_CLUSTERS_RADOS_POOL_NAMESPACE option to its default
value

Example command:
:   ```bash
    ceph dashboard reset-ganesha-clusters-rados-pool-namespace
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-grafana-api-password

Reset the GRAFANA_API_PASSWORD option to its default value

Example command:
:   ```bash
    ceph dashboard reset-grafana-api-password
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-grafana-api-ssl-verify

Reset the GRAFANA_API_SSL_VERIFY option to its default value

Example command:
:   ```bash
    ceph dashboard reset-grafana-api-ssl-verify
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-grafana-api-url

Reset the GRAFANA_API_URL option to its default value

Example command:
:   ```bash
    ceph dashboard reset-grafana-api-url
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-grafana-api-username

Reset the GRAFANA_API_USERNAME option to its default value

Example command:
:   ```bash
    ceph dashboard reset-grafana-api-username
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-grafana-frontend-api-url

Reset the GRAFANA_FRONTEND_API_URL option to its default value

Example command:
:   ```bash
    ceph dashboard reset-grafana-frontend-api-url
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-grafana-update-dashboards

Reset the GRAFANA_UPDATE_DASHBOARDS option to its default value

Example command:
:   ```bash
    ceph dashboard reset-grafana-update-dashboards
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-iscsi-api-ssl-verification

Reset the ISCSI_API_SSL_VERIFICATION option to its default value

Example command:
:   ```bash
    ceph dashboard reset-iscsi-api-ssl-verification
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-issue-tracker-api-key

Reset the ISSUE_TRACKER_API_KEY option to its default value

Example command:
:   ```bash
    ceph dashboard reset-issue-tracker-api-key
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-prometheus-api-host

Reset the PROMETHEUS_API_HOST option to its default value

Example command:
:   ```bash
    ceph dashboard reset-prometheus-api-host
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-prometheus-api-ssl-verify

Reset the PROMETHEUS_API_SSL_VERIFY option to its default value

Example command:
:   ```bash
    ceph dashboard reset-prometheus-api-ssl-verify
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-pwd-policy-check-complexity-enabled

Reset the PWD_POLICY_CHECK_COMPLEXITY_ENABLED option to its default
value

Example command:
:   ```bash
    ceph dashboard reset-pwd-policy-check-complexity-enabled
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-pwd-policy-check-exclusion-list-enabled

Reset the PWD_POLICY_CHECK_EXCLUSION_LIST_ENABLED option to its
default value

Example command:
:   ```bash
    ceph dashboard reset-pwd-policy-check-exclusion-list-enabled
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-pwd-policy-check-length-enabled

Reset the PWD_POLICY_CHECK_LENGTH_ENABLED option to its default value

Example command:
:   ```bash
    ceph dashboard reset-pwd-policy-check-length-enabled
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-pwd-policy-check-oldpwd-enabled

Reset the PWD_POLICY_CHECK_OLDPWD_ENABLED option to its default value

Example command:
:   ```bash
    ceph dashboard reset-pwd-policy-check-oldpwd-enabled
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-pwd-policy-check-repetitive-chars-enabled

Reset the PWD_POLICY_CHECK_REPETITIVE_CHARS_ENABLED option to its
default value

Example command:
:   ```bash
    ceph dashboard reset-pwd-policy-check-repetitive-chars-enabled
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-pwd-policy-check-sequential-chars-enabled

Reset the PWD_POLICY_CHECK_SEQUENTIAL_CHARS_ENABLED option to its
default value

Example command:
:   ```bash
    ceph dashboard reset-pwd-policy-check-sequential-chars-enabled
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-pwd-policy-check-username-enabled

Reset the PWD_POLICY_CHECK_USERNAME_ENABLED option to its default
value

Example command:
:   ```bash
    ceph dashboard reset-pwd-policy-check-username-enabled
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-pwd-policy-enabled

Reset the PWD_POLICY_ENABLED option to its default value

Example command:
:   ```bash
    ceph dashboard reset-pwd-policy-enabled
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-pwd-policy-exclusion-list

Reset the PWD_POLICY_EXCLUSION_LIST option to its default value

Example command:
:   ```bash
    ceph dashboard reset-pwd-policy-exclusion-list
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-pwd-policy-min-complexity

Reset the PWD_POLICY_MIN_COMPLEXITY option to its default value

Example command:
:   ```bash
    ceph dashboard reset-pwd-policy-min-complexity
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-pwd-policy-min-length

Reset the PWD_POLICY_MIN_LENGTH option to its default value

Example command:
:   ```bash
    ceph dashboard reset-pwd-policy-min-length
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-rest-requests-timeout

Reset the REST_REQUESTS_TIMEOUT option to its default value

Example command:
:   ```bash
    ceph dashboard reset-rest-requests-timeout
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-rgw-api-access-key

Reset the RGW_API_ACCESS_KEY option to its default value

Example command:
:   ```bash
    ceph dashboard reset-rgw-api-access-key
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-rgw-api-admin-resource

Reset the RGW_API_ADMIN_RESOURCE option to its default value

Example command:
:   ```bash
    ceph dashboard reset-rgw-api-admin-resource
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-rgw-api-secret-key

Reset the RGW_API_SECRET_KEY option to its default value

Example command:
:   ```bash
    ceph dashboard reset-rgw-api-secret-key
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-rgw-api-ssl-verify

Reset the RGW_API_SSL_VERIFY option to its default value

Example command:
:   ```bash
    ceph dashboard reset-rgw-api-ssl-verify
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-user-pwd-expiration-span

Reset the USER_PWD_EXPIRATION_SPAN option to its default value

Example command:
:   ```bash
    ceph dashboard reset-user-pwd-expiration-span
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-user-pwd-expiration-warning-1

Reset the USER_PWD_EXPIRATION_WARNING_1 option to its default value

Example command:
:   ```bash
    ceph dashboard reset-user-pwd-expiration-warning-1
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard reset-user-pwd-expiration-warning-2

Reset the USER_PWD_EXPIRATION_WARNING_2 option to its default value

Example command:
:   ```bash
    ceph dashboard reset-user-pwd-expiration-warning-2
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-account-lockout-attempts

Set the ACCOUNT_LOCKOUT_ATTEMPTS option value

Example command:
:   ```bash
    ceph dashboard set-account-lockout-attempts my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-alertmanager-api-host

Set the ALERTMANAGER_API_HOST option value

Example command:
:   ```bash
    ceph dashboard set-alertmanager-api-host my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-alertmanager-api-ssl-verify

Set the ALERTMANAGER_API_SSL_VERIFY option value

Example command:
:   ```bash
    ceph dashboard set-alertmanager-api-ssl-verify my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-audit-api-enabled

Set the AUDIT_API_ENABLED option value

Example command:
:   ```bash
    ceph dashboard set-audit-api-enabled my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-audit-api-log-payload

Set the AUDIT_API_LOG_PAYLOAD option value

Example command:
:   ```bash
    ceph dashboard set-audit-api-log-payload my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-enable-browsable-api

Set the ENABLE_BROWSABLE_API option value

Example command:
:   ```bash
    ceph dashboard set-enable-browsable-api my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-ganesha-clusters-rados-pool-namespace

Set the GANESHA_CLUSTERS_RADOS_POOL_NAMESPACE option value

Example command:
:   ```bash
    ceph dashboard set-ganesha-clusters-rados-pool-namespace my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-grafana-api-password

Set the GRAFANA_API_PASSWORD option value read from -i <file>

Example command:
:   ```bash
    ceph dashboard set-grafana-api-password
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-grafana-api-ssl-verify

Set the GRAFANA_API_SSL_VERIFY option value

Example command:
:   ```bash
    ceph dashboard set-grafana-api-ssl-verify my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-grafana-api-url

Set the GRAFANA_API_URL option value

Example command:
:   ```bash
    ceph dashboard set-grafana-api-url my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-grafana-api-username

Set the GRAFANA_API_USERNAME option value

Example command:
:   ```bash
    ceph dashboard set-grafana-api-username my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-grafana-frontend-api-url

Set the GRAFANA_FRONTEND_API_URL option value

Example command:
:   ```bash
    ceph dashboard set-grafana-frontend-api-url my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-grafana-update-dashboards

Set the GRAFANA_UPDATE_DASHBOARDS option value

Example command:
:   ```bash
    ceph dashboard set-grafana-update-dashboards my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-iscsi-api-ssl-verification

Set the ISCSI_API_SSL_VERIFICATION option value

Example command:
:   ```bash
    ceph dashboard set-iscsi-api-ssl-verification my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-issue-tracker-api-key

Set the ISSUE_TRACKER_API_KEY option value read from -i <file>

Example command:
:   ```bash
    ceph dashboard set-issue-tracker-api-key
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-jwt-token-ttl

Set the JWT token TTL in seconds

Example command:
:   ```bash
    ceph dashboard set-jwt-token-ttl 1
    ```

Parameters:
:   - **seconds**: CephInt

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-prometheus-api-host

Set the PROMETHEUS_API_HOST option value

Example command:
:   ```bash
    ceph dashboard set-prometheus-api-host my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-prometheus-api-ssl-verify

Set the PROMETHEUS_API_SSL_VERIFY option value

Example command:
:   ```bash
    ceph dashboard set-prometheus-api-ssl-verify my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-pwd-policy-check-complexity-enabled

Set the PWD_POLICY_CHECK_COMPLEXITY_ENABLED option value

Example command:
:   ```bash
    ceph dashboard set-pwd-policy-check-complexity-enabled my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-pwd-policy-check-exclusion-list-enabled

Set the PWD_POLICY_CHECK_EXCLUSION_LIST_ENABLED option value

Example command:
:   ```bash
    ceph dashboard set-pwd-policy-check-exclusion-list-enabled my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-pwd-policy-check-length-enabled

Set the PWD_POLICY_CHECK_LENGTH_ENABLED option value

Example command:
:   ```bash
    ceph dashboard set-pwd-policy-check-length-enabled my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-pwd-policy-check-oldpwd-enabled

Set the PWD_POLICY_CHECK_OLDPWD_ENABLED option value

Example command:
:   ```bash
    ceph dashboard set-pwd-policy-check-oldpwd-enabled my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-pwd-policy-check-repetitive-chars-enabled

Set the PWD_POLICY_CHECK_REPETITIVE_CHARS_ENABLED option value

Example command:
:   ```bash
    ceph dashboard set-pwd-policy-check-repetitive-chars-enabled my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-pwd-policy-check-sequential-chars-enabled

Set the PWD_POLICY_CHECK_SEQUENTIAL_CHARS_ENABLED option value

Example command:
:   ```bash
    ceph dashboard set-pwd-policy-check-sequential-chars-enabled my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-pwd-policy-check-username-enabled

Set the PWD_POLICY_CHECK_USERNAME_ENABLED option value

Example command:
:   ```bash
    ceph dashboard set-pwd-policy-check-username-enabled my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-pwd-policy-enabled

Set the PWD_POLICY_ENABLED option value

Example command:
:   ```bash
    ceph dashboard set-pwd-policy-enabled my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-pwd-policy-exclusion-list

Set the PWD_POLICY_EXCLUSION_LIST option value

Example command:
:   ```bash
    ceph dashboard set-pwd-policy-exclusion-list my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-pwd-policy-min-complexity

Set the PWD_POLICY_MIN_COMPLEXITY option value

Example command:
:   ```bash
    ceph dashboard set-pwd-policy-min-complexity my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-pwd-policy-min-length

Set the PWD_POLICY_MIN_LENGTH option value

Example command:
:   ```bash
    ceph dashboard set-pwd-policy-min-length my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-rest-requests-timeout

Set the REST_REQUESTS_TIMEOUT option value

Example command:
:   ```bash
    ceph dashboard set-rest-requests-timeout my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-rgw-api-access-key

Set the RGW_API_ACCESS_KEY option value read from -i <file>

Example command:
:   ```bash
    ceph dashboard set-rgw-api-access-key
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-rgw-api-admin-resource

Set the RGW_API_ADMIN_RESOURCE option value

Example command:
:   ```bash
    ceph dashboard set-rgw-api-admin-resource my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-rgw-api-secret-key

Set the RGW_API_SECRET_KEY option value read from -i <file>

Example command:
:   ```bash
    ceph dashboard set-rgw-api-secret-key
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-rgw-api-ssl-verify

Set the RGW_API_SSL_VERIFY option value

Example command:
:   ```bash
    ceph dashboard set-rgw-api-ssl-verify my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-user-pwd-expiration-span

Set the USER_PWD_EXPIRATION_SPAN option value

Example command:
:   ```bash
    ceph dashboard set-user-pwd-expiration-span my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-user-pwd-expiration-warning-1

Set the USER_PWD_EXPIRATION_WARNING_1 option value

Example command:
:   ```bash
    ceph dashboard set-user-pwd-expiration-warning-1 my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard set-user-pwd-expiration-warning-2

Set the USER_PWD_EXPIRATION_WARNING_2 option value

Example command:
:   ```bash
    ceph dashboard set-user-pwd-expiration-warning-2 my_value
    ```

Parameters:
:   - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard sso disable

Disable Single Sign-On

Example command:
:   ```bash
    ceph dashboard sso disable
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard sso enable saml2

Enable SAML2 Single Sign-On

Example command:
:   ```bash
    ceph dashboard sso enable saml2
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard sso setup saml2

Setup SAML2 Single Sign-On

Example command:
:   ```bash
    ceph dashboard sso setup saml2 --ceph_dashboard_base_url=string
      --idp_metadata=string --idp_username_attribute=string
      --idp_entity_id=string --sp_x_509_cert=/path/to/file
      --sp_private_key=/path/to/file
    ```

Parameters:
:   - **ceph_dashboard_base_url**: (string)
    - **idp_metadata**: (string)
    - **idp_username_attribute**: (string)
    - **idp_entity_id**: (string)
    - **sp_x_509_cert**: CephFilepath
    - **sp_private_key**: CephFilepath

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## dashboard sso show saml2

Show SAML2 configuration

Example command:
:   ```bash
    ceph dashboard sso show saml2
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## dashboard sso status

Get Single Sign-On status

Example command:
:   ```bash
    ceph dashboard sso status
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

# device

## device light

Enable or disable the device light. Default type is ident ‘Usage:
device light (on|off) <devid> [ident|fault] [--force]’

Example command:
:   ```bash
    ceph device light --enable=on --devid=string --light_type=ident
      --force
    ```

Parameters:
:   - **enable**: CephChoices strings=(on off)
    - **devid**: (string)
    - **light_type**: CephChoices strings=(ident fault)
    - **--force**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## device ls-lights

List currently active device indicator lights

Example command:
:   ```bash
    ceph device ls-lights
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

# fs

## fs clone cancel

Cancel an pending or ongoing clone operation.

Example command:
:   ```bash
    ceph fs clone cancel my_vol_name my_clone_name my_group_name
    ```

Parameters:
:   - **vol_name**: (string)
    - **clone_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs clone status

Get status on a cloned subvolume.

Example command:
:   ```bash
    ceph fs clone status my_vol_name my_clone_name my_group_name
    ```

Parameters:
:   - **vol_name**: (string)
    - **clone_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs perf stats

retrieve ceph fs performance stats

Example command:
:   ```bash
    ceph fs perf stats my_mds_rank my_client_id my_client_ip
    ```

Parameters:
:   - **mds_rank**: (string)
    - **client_id**: (string)
    - **client_ip**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs quiesce --

Manage quiesce sets of subvolumes

Example command:
:   ```bash
    ceph fs quiesce -- --vol_name=string --members=string --set_id=string
      --timeout=0 --expiration=0 --await_for=0 --await --if_version=0
      --include --exclude --reset --release --query --all --cancel
      --group_name=string --leader --with_leader=0
    ```

Parameters:
:   - **vol_name**: (string)
    - **members**: (can be repeated)
    - **set_id**: (string)
    - **timeout**: CephFloat range= `0`
    - **expiration**: CephFloat range= `0`
    - **await_for**: CephFloat range= `0`
    - **await**: CephBool
    - **if_version**: CephInt range= `0`
    - **include**: CephBool
    - **exclude**: CephBool
    - **reset**: CephBool
    - **release**: CephBool
    - **query**: CephBool
    - **all**: CephBool
    - **cancel**: CephBool
    - **group_name**: (string)
    - **leader**: CephBool
    - **with_leader**: CephInt range= `0`

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume authorize

Allow a cephx auth ID access to a subvolume

Example command:
:   ```bash
    ceph fs subvolume authorize --vol_name=string --sub_name=string
      --auth_id=string --group_name=string --access_level=string
      --tenant_id=string --allow_existing_id
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **auth_id**: (string)
    - **group_name**: (string)
    - **access_level**: (string)
    - **tenant_id**: (string)
    - **allow_existing_id**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume authorized_list

List auth IDs that have access to a subvolume

Example command:
:   ```bash
    ceph fs subvolume authorized_list my_vol_name my_sub_name
      my_group_name
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs subvolume charmap get

Get charmap settings for subvolumegroup

Example command:
:   ```bash
    ceph fs subvolume charmap get --vol_name=string --sub_name=string
      --setting=casesensitive --group_name=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **setting**: CephChoices strings=(casesensitive normalization encoding)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume charmap rm

Remove charmap settings for subvolume

Example command:
:   ```bash
    ceph fs subvolume charmap rm my_vol_name my_sub_name my_group_name
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume charmap set

Set charmap settings for subvolumegroup

Example command:
:   ```bash
    ceph fs subvolume charmap set --vol_name=string --sub_name=string
      --setting=casesensitive --value=string --group_name=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **setting**: CephChoices strings=(casesensitive normalization encoding)
    - **value**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume create

Create a CephFS subvolume in a volume, and optionally, with a specific
size (in bytes), a specific data pool layout, a specific mode, in a
specific subvolume group and in separate RADOS namespace

Example command:
:   ```bash
    ceph fs subvolume create --vol_name=string --sub_name=string --size=1
      --group_name=string --pool_layout=string --uid=1 --gid=1 --mode=string
      --namespace_isolated --earmark=string --normalization=nfd
      --casesensitive
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: goodchars= `[A-Za-z0-9-_.]`
    - **size**: CephInt
    - **group_name**: (string)
    - **pool_layout**: (string)
    - **uid**: CephInt
    - **gid**: CephInt
    - **mode**: (string)
    - **namespace_isolated**: CephBool
    - **earmark**: (string)
    - **normalization**: CephChoices strings=(nfd nfc nfkd nfkc)
    - **casesensitive**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume deauthorize

Deny a cephx auth ID access to a subvolume

Example command:
:   ```bash
    ceph fs subvolume deauthorize --vol_name=string --sub_name=string
      --auth_id=string --group_name=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **auth_id**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume earmark get

Get earmark for a subvolume

Example command:
:   ```bash
    ceph fs subvolume earmark get my_vol_name my_sub_name my_group_name
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs subvolume earmark rm

Remove earmark from a subvolume

Example command:
:   ```bash
    ceph fs subvolume earmark rm my_vol_name my_sub_name my_group_name
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume earmark set

Set earmark for a subvolume

Example command:
:   ```bash
    ceph fs subvolume earmark set --vol_name=string --sub_name=string
      --earmark=string --group_name=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **earmark**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume evict

Evict clients based on auth IDs and subvolume mounted

Example command:
:   ```bash
    ceph fs subvolume evict --vol_name=string --sub_name=string
      --auth_id=string --group_name=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **auth_id**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume exist

Check a volume for the existence of a subvolume, optionally in a
specified subvolume group

Example command:
:   ```bash
    ceph fs subvolume exist my_vol_name my_group_name
    ```

Parameters:
:   - **vol_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs subvolume getpath

Get the mountpath of a CephFS subvolume in a volume, and optionally,
in a specific subvolume group

Example command:
:   ```bash
    ceph fs subvolume getpath my_vol_name my_sub_name my_group_name
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume info

Get the information of a CephFS subvolume in a volume, and optionally,
in a specific subvolume group

Example command:
:   ```bash
    ceph fs subvolume info my_vol_name my_sub_name my_group_name
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs subvolume ls

List subvolumes

Example command:
:   ```bash
    ceph fs subvolume ls my_vol_name my_group_name
    ```

Parameters:
:   - **vol_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs subvolume metadata get

Get custom metadata associated with the key of a CephFS subvolume in a
volume, and optionally, in a specific subvolume group

Example command:
:   ```bash
    ceph fs subvolume metadata get --vol_name=string --sub_name=string
      --key_name=string --group_name=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **key_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs subvolume metadata ls

List custom metadata (key-value pairs) of a CephFS subvolume in a
volume, and optionally, in a specific subvolume group

Example command:
:   ```bash
    ceph fs subvolume metadata ls my_vol_name my_sub_name my_group_name
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs subvolume metadata rm

Remove custom metadata (key-value) associated with the key of a CephFS
subvolume in a volume, and optionally, in a specific subvolume group

Example command:
:   ```bash
    ceph fs subvolume metadata rm --vol_name=string --sub_name=string
      --key_name=string --group_name=string --force
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **key_name**: (string)
    - **group_name**: (string)
    - **force**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume metadata set

Set custom metadata (key-value) for a CephFS subvolume in a volume,
and optionally, in a specific subvolume group

Example command:
:   ```bash
    ceph fs subvolume metadata set --vol_name=string --sub_name=string
      --key_name=string --value=string --group_name=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **key_name**: (string)
    - **value**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume pin

Set MDS pinning policy for subvolume

Example command:
:   ```bash
    ceph fs subvolume pin --vol_name=string --sub_name=string
      --pin_type=export --pin_setting=string --group_name=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **pin_type**: CephChoices strings=(export distributed random)
    - **pin_setting**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume resize

Resize a CephFS subvolume

Example command:
:   ```bash
    ceph fs subvolume resize --vol_name=string --sub_name=string
      --new_size=string --group_name=string --no_shrink
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **new_size**: (string)
    - **group_name**: (string)
    - **no_shrink**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume rm

Delete a CephFS subvolume in a volume, and optionally, in a specific
subvolume group, force deleting a cancelled or failed clone, and
retaining existing subvolume snapshots

Example command:
:   ```bash
    ceph fs subvolume rm --vol_name=string --sub_name=string
      --group_name=string --force --retain_snapshots
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **group_name**: (string)
    - **force**: CephBool
    - **retain_snapshots**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume snapshot clone

Clone a snapshot to target subvolume

Example command:
:   ```bash
    ceph fs subvolume snapshot clone --vol_name=string --sub_name=string
      --snap_name=string --target_sub_name=string --pool_layout=string
      --group_name=string --target_group_name=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **snap_name**: (string)
    - **target_sub_name**: (string)
    - **pool_layout**: (string)
    - **group_name**: (string)
    - **target_group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume snapshot create

Create a snapshot of a CephFS subvolume in a volume, and optionally,
in a specific subvolume group

Example command:
:   ```bash
    ceph fs subvolume snapshot create --vol_name=string --sub_name=string
      --snap_name=string --group_name=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **snap_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume snapshot getpath

Get path for a snapshot of a CephFS subvolume located in a specific
volume, and optionally, in a specific subvolume group

Example command:
:   ```bash
    ceph fs subvolume snapshot getpath --vol_name=string --sub_name=string
      --snap_name=string --group_name=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **snap_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs subvolume snapshot info

Get the information of a CephFS subvolume snapshot and optionally, in
a specific subvolume group

Example command:
:   ```bash
    ceph fs subvolume snapshot info --vol_name=string --sub_name=string
      --snap_name=string --group_name=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **snap_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs subvolume snapshot ls

List subvolume snapshots

Example command:
:   ```bash
    ceph fs subvolume snapshot ls my_vol_name my_sub_name my_group_name
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs subvolume snapshot metadata get

Get custom metadata associated with the key of a CephFS subvolume
snapshot in a volume, and optionally, in a specific subvolume group

Example command:
:   ```bash
    ceph fs subvolume snapshot metadata get --vol_name=string
      --sub_name=string --snap_name=string --key_name=string
      --group_name=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **snap_name**: (string)
    - **key_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs subvolume snapshot metadata ls

List custom metadata (key-value pairs) of a CephFS subvolume snapshot
in a volume, and optionally, in a specific subvolume group

Example command:
:   ```bash
    ceph fs subvolume snapshot metadata ls --vol_name=string
      --sub_name=string --snap_name=string --group_name=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **snap_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs subvolume snapshot metadata rm

Remove custom metadata (key-value) associated with the key of a CephFS
subvolume snapshot in a volume, and optionally, in a specific
subvolume group

Example command:
:   ```bash
    ceph fs subvolume snapshot metadata rm --vol_name=string
      --sub_name=string --snap_name=string --key_name=string
      --group_name=string --force
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **snap_name**: (string)
    - **key_name**: (string)
    - **group_name**: (string)
    - **force**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume snapshot metadata set

Set custom metadata (key-value) for a CephFS subvolume snapshot in a
volume, and optionally, in a specific subvolume group

Example command:
:   ```bash
    ceph fs subvolume snapshot metadata set --vol_name=string
      --sub_name=string --snap_name=string --key_name=string --value=string
      --group_name=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **snap_name**: (string)
    - **key_name**: (string)
    - **value**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume snapshot protect

(deprecated) Protect snapshot of a CephFS subvolume in a volume, and
optionally, in a specific subvolume group

Example command:
:   ```bash
    ceph fs subvolume snapshot protect --vol_name=string --sub_name=string
      --snap_name=string --group_name=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **snap_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume snapshot rm

Delete a snapshot of a CephFS subvolume in a volume, and optionally,
in a specific subvolume group

Example command:
:   ```bash
    ceph fs subvolume snapshot rm --vol_name=string --sub_name=string
      --snap_name=string --group_name=string --force
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **snap_name**: (string)
    - **group_name**: (string)
    - **force**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolume snapshot unprotect

(deprecated) Unprotect a snapshot of a CephFS subvolume in a volume,
and optionally, in a specific subvolume group

Example command:
:   ```bash
    ceph fs subvolume snapshot unprotect --vol_name=string
      --sub_name=string --snap_name=string --group_name=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **sub_name**: (string)
    - **snap_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolumegroup charmap get

Get charmap settings for subvolumegroup

Example command:
:   ```bash
    ceph fs subvolumegroup charmap get my_vol_name my_group_name
      casesensitive
    ```

Parameters:
:   - **vol_name**: (string)
    - **group_name**: (string)
    - **setting**: CephChoices strings=(casesensitive normalization encoding)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolumegroup charmap rm

Remove charmap settings for subvolumegroup

Example command:
:   ```bash
    ceph fs subvolumegroup charmap rm my_vol_name my_group_name
    ```

Parameters:
:   - **vol_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolumegroup charmap set

Set charmap settings for subvolumegroup

Example command:
:   ```bash
    ceph fs subvolumegroup charmap set --vol_name=string
      --group_name=string --setting=casesensitive --value=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **group_name**: (string)
    - **setting**: CephChoices strings=(casesensitive normalization encoding)
    - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolumegroup create

Create a CephFS subvolume group in a volume, and optionally, with a
specific data pool layout, and a specific numeric mode

Example command:
:   ```bash
    ceph fs subvolumegroup create --vol_name=string --group_name=string
      --size=1 --pool_layout=string --uid=1 --gid=1 --mode=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **group_name**: goodchars= `[A-Za-z0-9-_.]`
    - **size**: CephInt
    - **pool_layout**: (string)
    - **uid**: CephInt
    - **gid**: CephInt
    - **mode**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolumegroup exist

Check a volume for the existence of subvolumegroup

Example command:
:   ```bash
    ceph fs subvolumegroup exist my_vol_name
    ```

Parameters:
:   - **vol_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs subvolumegroup getpath

Get the mountpath of a CephFS subvolume group in a volume

Example command:
:   ```bash
    ceph fs subvolumegroup getpath my_vol_name my_group_name
    ```

Parameters:
:   - **vol_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs subvolumegroup info

Get the metadata of a CephFS subvolume group in a volume,

Example command:
:   ```bash
    ceph fs subvolumegroup info my_vol_name my_group_name
    ```

Parameters:
:   - **vol_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs subvolumegroup ls

List subvolumegroups

Example command:
:   ```bash
    ceph fs subvolumegroup ls my_vol_name
    ```

Parameters:
:   - **vol_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs subvolumegroup pin

Set MDS pinning policy for subvolumegroup

Example command:
:   ```bash
    ceph fs subvolumegroup pin --vol_name=string --group_name=string
      --pin_type=export --pin_setting=string
    ```

Parameters:
:   - **vol_name**: (string)
    - **group_name**: (string)
    - **pin_type**: CephChoices strings=(export distributed random)
    - **pin_setting**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolumegroup resize

Resize a CephFS subvolume group

Example command:
:   ```bash
    ceph fs subvolumegroup resize --vol_name=string --group_name=string
      --new_size=string --no_shrink
    ```

Parameters:
:   - **vol_name**: (string)
    - **group_name**: (string)
    - **new_size**: (string)
    - **no_shrink**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolumegroup rm

Delete a CephFS subvolume group in a volume

Example command:
:   ```bash
    ceph fs subvolumegroup rm my_vol_name my_group_name --force
    ```

Parameters:
:   - **vol_name**: (string)
    - **group_name**: (string)
    - **force**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolumegroup snapshot create

Create a snapshot of a CephFS subvolume group in a volume

Example command:
:   ```bash
    ceph fs subvolumegroup snapshot create my_vol_name my_group_name
      my_snap_name
    ```

Parameters:
:   - **vol_name**: (string)
    - **group_name**: (string)
    - **snap_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs subvolumegroup snapshot ls

List subvolumegroup snapshots

Example command:
:   ```bash
    ceph fs subvolumegroup snapshot ls my_vol_name my_group_name
    ```

Parameters:
:   - **vol_name**: (string)
    - **group_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs subvolumegroup snapshot rm

Delete a snapshot of a CephFS subvolume group in a volume

Example command:
:   ```bash
    ceph fs subvolumegroup snapshot rm --vol_name=string
      --group_name=string --snap_name=string --force
    ```

Parameters:
:   - **vol_name**: (string)
    - **group_name**: (string)
    - **snap_name**: (string)
    - **force**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs volume create

Create a CephFS volume

Example command:
:   ```bash
    ceph fs volume create --name=string --placement=string
      --meta_pool=string --data_pool=string
    ```

Parameters:
:   - **name**: goodchars= `[A-Za-z0-9-_.]`
    - **placement**: (string)
    - **meta_pool**: goodchars= `[A-Za-z0-9-_.]`
    - **data_pool**: goodchars= `[A-Za-z0-9-_.]`

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs volume info

Get the information of a CephFS volume

Example command:
:   ```bash
    ceph fs volume info my_vol_name --human_readable
    ```

Parameters:
:   - **vol_name**: (string)
    - **human_readable**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs volume ls

List volumes

Example command:
:   ```bash
    ceph fs volume ls
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## fs volume rename

Rename a CephFS volume by passing --yes-i-really-mean-it flag

Example command:
:   ```bash
    ceph fs volume rename my_vol_name my_new_vol_name
      --yes_i_really_mean_it
    ```

Parameters:
:   - **vol_name**: goodchars= `[A-Za-z0-9-_.]`
    - **new_vol_name**: goodchars= `[A-Za-z0-9-_.]`
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## fs volume rm

Delete a FS volume by passing --yes-i-really-mean-it flag

Example command:
:   ```bash
    ceph fs volume rm my_vol_name my_yes-i-really-mean-it
    ```

Parameters:
:   - **vol_name**: (string)
    - **yes-i-really-mean-it**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

# influx

## influx config-set

Set a configuration value

Example command:
:   ```bash
    ceph influx config-set my_key my_value
    ```

Parameters:
:   - **key**: (string)
    - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## influx config-show

Show current configuration

Example command:
:   ```bash
    ceph influx config-show
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## influx send

Force sending data to Influx

Example command:
:   ```bash
    ceph influx send
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

# k8sevents

## k8sevents ceph

List Ceph events tracked & sent to the kubernetes cluster

Example command:
:   ```bash
    ceph k8sevents ceph
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## k8sevents clear-config

Clear external kubernetes configuration settings

Example command:
:   ```bash
    ceph k8sevents clear-config
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## k8sevents ls

List all current Kuberenetes events from the Ceph namespace

Example command:
:   ```bash
    ceph k8sevents ls
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## k8sevents set-access

Set kubernetes access credentials. <key> must be cacrt or token and
use -i <filename> syntax (e.g., ceph k8sevents set-access cacrt -i
/root/ca.crt).

Example command:
:   ```bash
    ceph k8sevents set-access my_key
    ```

Parameters:
:   - **key**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## k8sevents set-config

Set kubernetes config paramters. <key> must be server or namespace
(e.g., ceph k8sevents set-config server <https://localhost:30433>).

Example command:
:   ```bash
    ceph k8sevents set-config my_key my_value
    ```

Parameters:
:   - **key**: (string)
    - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## k8sevents status

Show the status of the data gathering threads

Example command:
:   ```bash
    ceph k8sevents status
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

# orch

## orch

Start, stop, restart, redeploy, or reconfig an entire service (i.e.
all daemons)

Example command:
:   ```bash
    ceph orch start my_service_name
    ```

Parameters:
:   - **action**: CephChoices strings=(start stop restart redeploy reconfig rotate-key)
    - **service_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch alertmanager get-credentials

Example command:
:   ```bash
    ceph orch alertmanager get-credentials
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch alertmanager set-credentials

Example command:
:   ```bash
    ceph orch alertmanager set-credentials my_username my_password
    ```

Parameters:
:   - **username**: (string)
    - **password**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch apply

Update the size or placement for a service or apply a large yaml spec

Example command:
:   ```bash
    ceph orch apply --service_type=mon --placement=string --dry_run
      --format=plain --unmanaged --no_overwrite --continue_on_error
    ```

Parameters:
:   - **service_type**: CephChoices strings=(mon mgr rbd-mirror cephfs-mirror crash alertmanager grafana node-exporter ceph-exporter prometheus loki promtail mds rgw nfs iscsi nvmeof snmp-gateway elasticsearch jaeger-agent jaeger-collector jaeger-query)
    - **placement**: (string)
    - **--dry_run**: CephBool
    - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)
    - **--unmanaged**: CephBool
    - **--no_overwrite**: CephBool
    - **--continue_on_error**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch apply iscsi

Scale an iSCSI service

Example command:
:   ```bash
    ceph orch apply iscsi --pool=string --api_user=string
      --api_password=string --trusted_ip_list=string --placement=string
      --unmanaged --dry_run --format=plain --no_overwrite
    ```

Parameters:
:   - **pool**: (string)
    - **api_user**: (string)
    - **api_password**: (string)
    - **trusted_ip_list**: (string)
    - **placement**: (string)
    - **--unmanaged**: CephBool
    - **--dry_run**: CephBool
    - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)
    - **--no_overwrite**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch apply jaeger

Apply jaeger tracing services

Example command:
:   ```bash
    ceph orch apply jaeger --es_nodes=string --without_query
      --placement=string --unmanaged --dry_run --format=plain --no_overwrite
    ```

Parameters:
:   - **es_nodes**: (string)
    - **--without_query**: CephBool
    - **--placement**: (string)
    - **--unmanaged**: CephBool
    - **--dry_run**: CephBool
    - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)
    - **--no_overwrite**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch apply mds

Update the number of MDS instances for the given fs_name

Example command:
:   ```bash
    ceph orch apply mds --fs_name=string --placement=string --dry_run
      --unmanaged --format=plain --no_overwrite
    ```

Parameters:
:   - **fs_name**: (string)
    - **placement**: (string)
    - **--dry_run**: CephBool
    - **--unmanaged**: CephBool
    - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)
    - **--no_overwrite**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch apply nfs

Scale an NFS service

Example command:
:   ```bash
    ceph orch apply nfs --svc_id=string --placement=string --format=plain
      --port=1 --dry_run --unmanaged --no_overwrite
    ```

Parameters:
:   - **svc_id**: (string)
    - **placement**: (string)
    - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)
    - **--port**: CephInt
    - **--dry_run**: CephBool
    - **--unmanaged**: CephBool
    - **--no_overwrite**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch apply nvmeof

Scale an nvmeof service

Example command:
:   ```bash
    ceph orch apply nvmeof --pool=string --group=string --placement=string
      --unmanaged --dry_run --format=plain --no_overwrite
    ```

Parameters:
:   - **pool**: (string)
    - **group**: (string)
    - **placement**: (string)
    - **--unmanaged**: CephBool
    - **--dry_run**: CephBool
    - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)
    - **--no_overwrite**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch apply osd

Create OSD daemon(s) on all available devices

Example command:
:   ```bash
    ceph orch apply osd --all_available_devices --format=plain --unmanaged
      --dry_run --no_overwrite --method=raw
    ```

Parameters:
:   - **--all_available_devices**: CephBool
    - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)
    - **--unmanaged**: CephBool
    - **--dry_run**: CephBool
    - **--no_overwrite**: CephBool
    - **--method**: CephChoices strings=(raw lvm)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch apply rgw

Update the number of RGW instances for the given zone

Example command:
:   ```bash
    ceph orch apply rgw --svc_id=string --placement=string --realm=string
      --zonegroup=string --zone=string --networks=string --port=1 --ssl
      --dry_run --format=plain --unmanaged --no_overwrite
    ```

Parameters:
:   - **svc_id**: (string)
    - **placement**: (string)
    - **--realm**: (string)
    - **--zonegroup**: (string)
    - **--zone**: (string)
    - **--networks**: (can be repeated)
    - **--port**: CephInt
    - **--ssl**: CephBool
    - **--dry_run**: CephBool
    - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)
    - **--unmanaged**: CephBool
    - **--no_overwrite**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch apply smb

Apply an SMB network file system gateway service configuration.

Example command:
:   ```bash
    ceph orch apply smb --cluster_id=string --config_uri=string
      --features=string --join_sources=string --custom_dns=string
      --include_ceph_users=string --placement=string --unmanaged --dry_run
      --format=plain --no_overwrite
    ```

Parameters:
:   - **cluster_id**: (string)
    - **config_uri**: (string)
    - **features**: (string)
    - **join_sources**: (can be repeated)
    - **custom_dns**: (can be repeated)
    - **include_ceph_users**: (can be repeated)
    - **placement**: (string)
    - **--unmanaged**: CephBool
    - **--dry_run**: CephBool
    - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)
    - **--no_overwrite**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch apply snmp-gateway

Add a Prometheus to SNMP gateway service (cephadm only)

Example command:
:   ```bash
    ceph orch apply snmp-gateway --snmp_version=V2c --destination=string
      --port=1 --engine_id=string --auth_protocol=MD5 --privacy_protocol=DES
      --placement=string --unmanaged --dry_run --format=plain --no_overwrite
    ```

Parameters:
:   - **snmp_version**: CephChoices strings=(V2c V3)
    - **destination**: (string)
    - **port**: CephInt
    - **engine_id**: (string)
    - **auth_protocol**: CephChoices strings=(MD5 SHA)
    - **privacy_protocol**: CephChoices strings=(DES AES)
    - **placement**: (string)
    - **--unmanaged**: CephBool
    - **--dry_run**: CephBool
    - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)
    - **--no_overwrite**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch cancel

Cancel ongoing background operations

Example command:
:   ```bash
    ceph orch cancel
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch cert-store cert ls

Example command:
:   ```bash
    ceph orch cert-store cert ls plain
    ```

Parameters:
:   - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## orch cert-store get cert

Example command:
:   ```bash
    ceph orch cert-store get cert --entity=string --service_name=string
      --hostname=string --no_exception_when_missing
    ```

Parameters:
:   - **entity**: (string)
    - **--service_name**: (string)
    - **--hostname**: (string)
    - **--no_exception_when_missing**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## orch cert-store get key

Example command:
:   ```bash
    ceph orch cert-store get key --entity=string --service_name=string
      --hostname=string --no_exception_when_missing
    ```

Parameters:
:   - **entity**: (string)
    - **--service_name**: (string)
    - **--hostname**: (string)
    - **--no_exception_when_missing**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## orch cert-store key ls

Example command:
:   ```bash
    ceph orch cert-store key ls plain
    ```

Parameters:
:   - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## orch client-keyring ls

List client keyrings under cephadm management

Example command:
:   ```bash
    ceph orch client-keyring ls plain
    ```

Parameters:
:   - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## orch client-keyring rm

Remove client keyring from cephadm management

Example command:
:   ```bash
    ceph orch client-keyring rm my_entity
    ```

Parameters:
:   - **entity**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch client-keyring set

Add or update client keyring under cephadm management

Example command:
:   ```bash
    ceph orch client-keyring set --entity=string --placement=string
      --owner=string --mode=string --no_ceph_conf
    ```

Parameters:
:   - **entity**: (string)
    - **placement**: (string)
    - **owner**: (string)
    - **mode**: (string)
    - **--no_ceph_conf**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch daemon

Start, stop, restart, redeploy, reconfig, or rotate-key for a specific
daemon

Example command:
:   ```bash
    ceph orch daemon start my_name
    ```

Parameters:
:   - **action**: CephChoices strings=(start stop restart reconfig rotate-key)
    - **name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch daemon add

Add daemon(s)

Example command:
:   ```bash
    ceph orch daemon add mon my_placement
    ```

Parameters:
:   - **daemon_type**: CephChoices strings=(mon mgr rbd-mirror cephfs-mirror crash alertmanager grafana node-exporter ceph-exporter prometheus loki promtail mds rgw nfs iscsi nvmeof snmp-gateway elasticsearch jaeger-agent jaeger-collector jaeger-query)
    - **placement**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch daemon add iscsi

Start iscsi daemon(s)

Example command:
:   ```bash
    ceph orch daemon add iscsi --pool=string --api_user=string
      --api_password=string --trusted_ip_list=string --placement=string
    ```

Parameters:
:   - **pool**: (string)
    - **api_user**: (string)
    - **api_password**: (string)
    - **trusted_ip_list**: (string)
    - **placement**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch daemon add mds

Start MDS daemon(s)

Example command:
:   ```bash
    ceph orch daemon add mds my_fs_name my_placement
    ```

Parameters:
:   - **fs_name**: (string)
    - **placement**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch daemon add nfs

Start NFS daemon(s)

Example command:
:   ```bash
    ceph orch daemon add nfs my_svc_id my_placement
    ```

Parameters:
:   - **svc_id**: (string)
    - **placement**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch daemon add nvmeof

Start nvmeof daemon(s)

Example command:
:   ```bash
    ceph orch daemon add nvmeof my_pool my_group my_placement
    ```

Parameters:
:   - **pool**: (string)
    - **group**: (string)
    - **placement**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch daemon add osd

Create OSD daemon(s) on specified host and device(s) (e.g., ceph orch
daemon add osd myhost:/dev/sdb)

Example command:
:   ```bash
    ceph orch daemon add osd my_svc_arg raw
    ```

Parameters:
:   - **svc_arg**: (string)
    - **method**: CephChoices strings=(raw lvm)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch daemon add rgw

Start RGW daemon(s)

Example command:
:   ```bash
    ceph orch daemon add rgw --svc_id=string --placement=string --port=1
      --ssl
    ```

Parameters:
:   - **svc_id**: (string)
    - **placement**: (string)
    - **--port**: CephInt
    - **--ssl**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch daemon redeploy

Redeploy a daemon (with a specific image)

Example command:
:   ```bash
    ceph orch daemon redeploy my_name my_image
    ```

Parameters:
:   - **name**: (string)
    - **image**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch daemon rm

Remove specific daemon(s)

Example command:
:   ```bash
    ceph orch daemon rm --names=string --force
    ```

Parameters:
:   - **names**: (can be repeated)
    - **--force**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch device ls

List devices on a host

Example command:
:   ```bash
    ceph orch device ls --hostname=string --format=plain --refresh --wide
      --summary
    ```

Parameters:
:   - **hostname**: (can be repeated)
    - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)
    - **--refresh**: CephBool
    - **--wide**: CephBool
    - **--summary**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## orch device replace

Perform all required operations in order to replace a device.

Example command:
:   ```bash
    ceph orch device replace --hostname=string --device=string --clear
      --yes_i_really_mean_it
    ```

Parameters:
:   - **hostname**: (string)
    - **device**: (string)
    - **--clear**: CephBool
    - **--yes_i_really_mean_it**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## orch device zap

Zap (erase!) a device so it can be re-used

Example command:
:   ```bash
    ceph orch device zap my_hostname my_path --force
    ```

Parameters:
:   - **hostname**: (string)
    - **path**: (string)
    - **--force**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch hardware light

Enable or Disable a device or chassis LED

Example command:
:   ```bash
    ceph orch hardware light --light_type=chassis --action=on
      --hostname=string --device=string
    ```

Parameters:
:   - **light_type**: CephChoices strings=(chassis drive)
    - **action**: CephChoices strings=(on off get)
    - **hostname**: (string)
    - **device**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch hardware powercycle

Reboot a host

Example command:
:   ```bash
    ceph orch hardware powercycle my_hostname --yes_i_really_mean_it
    ```

Parameters:
:   - **hostname**: (string)
    - **--yes_i_really_mean_it**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch hardware shutdown

Shutdown a host

Example command:
:   ```bash
    ceph orch hardware shutdown my_hostname --force --yes_i_really_mean_it
    ```

Parameters:
:   - **hostname**: (string)
    - **--force**: CephBool
    - **--yes_i_really_mean_it**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch hardware status

Display hardware status summary :param hostname: hostname

Example command:
:   ```bash
    ceph orch hardware status my_hostname my_category plain
    ```

Parameters:
:   - **hostname**: (string)
    - **--category**: (string)
    - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch host add

Add a host

Example command:
:   ```bash
    ceph orch host add --hostname=string --addr=string --labels=string
      --maintenance
    ```

Parameters:
:   - **hostname**: (string)
    - **addr**: (string)
    - **labels**: (can be repeated)
    - **--maintenance**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch host drain

drain all daemons from a host

Example command:
:   ```bash
    ceph orch host drain --hostname=string --force --keep_conf_keyring
      --zap_osd_devices
    ```

Parameters:
:   - **hostname**: (string)
    - **--force**: CephBool
    - **--keep_conf_keyring**: CephBool
    - **--zap_osd_devices**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch host label add

Add a host label

Example command:
:   ```bash
    ceph orch host label add my_hostname my_label
    ```

Parameters:
:   - **hostname**: (string)
    - **label**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch host label rm

Remove a host label

Example command:
:   ```bash
    ceph orch host label rm my_hostname my_label --force
    ```

Parameters:
:   - **hostname**: (string)
    - **label**: (string)
    - **--force**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch host ls

List high level host information

Example command:
:   ```bash
    ceph orch host ls --format=plain --host_pattern=string --label=string
      --host_status=string --detail
    ```

Parameters:
:   - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)
    - **--host_pattern**: (string)
    - **--label**: (string)
    - **--host_status**: (string)
    - **--detail**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## orch host maintenance enter

Prepare a host for maintenance by shutting down and disabling all Ceph
daemons (cephadm only)

Example command:
:   ```bash
    ceph orch host maintenance enter my_hostname --force
      --yes_i_really_mean_it
    ```

Parameters:
:   - **hostname**: (string)
    - **--force**: CephBool
    - **--yes_i_really_mean_it**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch host maintenance exit

Return a host from maintenance, restarting all Ceph daemons (cephadm
only)

Example command:
:   ```bash
    ceph orch host maintenance exit my_hostname
    ```

Parameters:
:   - **hostname**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch host ok-to-stop

Check if the specified host can be safely stopped without reducing
availability

Example command:
:   ```bash
    ceph orch host ok-to-stop my_hostname
    ```

Parameters:
:   - **hostname**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch host rescan

Perform a disk rescan on a host

Example command:
:   ```bash
    ceph orch host rescan my_hostname --with_summary
    ```

Parameters:
:   - **hostname**: (string)
    - **--with_summary**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch host rm

Remove a host

Example command:
:   ```bash
    ceph orch host rm --hostname=string --force --offline --rm_crush_entry
    ```

Parameters:
:   - **hostname**: (string)
    - **--force**: CephBool
    - **--offline**: CephBool
    - **--rm_crush_entry**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch host set-addr

Update a host address

Example command:
:   ```bash
    ceph orch host set-addr my_hostname my_addr
    ```

Parameters:
:   - **hostname**: (string)
    - **addr**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch ls

List services known to orchestrator

Example command:
:   ```bash
    ceph orch ls --service_type=string --service_name=string --export
      --format=plain --refresh
    ```

Parameters:
:   - **service_type**: (string)
    - **service_name**: (string)
    - **--export**: CephBool
    - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)
    - **--refresh**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## orch osd rm

Remove OSD daemons

Example command:
:   ```bash
    ceph orch osd rm --osd_id=string --replace --force --zap --no_destroy
    ```

Parameters:
:   - **osd_id**: (can be repeated)
    - **--replace**: CephBool
    - **--force**: CephBool
    - **--zap**: CephBool
    - **--no_destroy**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch osd rm status

Status of OSD removal operation

Example command:
:   ```bash
    ceph orch osd rm status plain
    ```

Parameters:
:   - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch osd rm stop

Cancel ongoing OSD removal operation

Example command:
:   ```bash
    ceph orch osd rm stop --osd_id=string
    ```

Parameters:
:   - **osd_id**: (can be repeated)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch pause

Pause orchestrator background work

Example command:
:   ```bash
    ceph orch pause
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch prometheus get-credentials

Example command:
:   ```bash
    ceph orch prometheus get-credentials
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch prometheus remove-target

Example command:
:   ```bash
    ceph orch prometheus remove-target my_url
    ```

Parameters:
:   - **url**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch prometheus set-credentials

Example command:
:   ```bash
    ceph orch prometheus set-credentials my_username my_password
    ```

Parameters:
:   - **username**: (string)
    - **password**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch prometheus set-custom-alerts

Example command:
:   ```bash
    ceph orch prometheus set-custom-alerts
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch prometheus set-target

Example command:
:   ```bash
    ceph orch prometheus set-target my_url
    ```

Parameters:
:   - **url**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch ps

List daemons known to orchestrator

Example command:
:   ```bash
    ceph orch ps --hostname=string --service_name=string
      --daemon_type=string --daemon_id=string --sort_by=service_name
      --format=plain --refresh
    ```

Parameters:
:   - **hostname**: (string)
    - **--service_name**: (string)
    - **--daemon_type**: (string)
    - **--daemon_id**: (string)
    - **--sort_by**: CephChoices strings=(service_name daemon_type name host status refreshed age mem_use mem_lim image)
    - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)
    - **--refresh**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## orch resume

Resume orchestrator background work (if paused)

Example command:
:   ```bash
    ceph orch resume
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch rm

Remove a service

Example command:
:   ```bash
    ceph orch rm my_service_name --force
    ```

Parameters:
:   - **service_name**: (string)
    - **--force**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch sd dump cert

Returns service discovery server root certificate

Example command:
:   ```bash
    ceph orch sd dump cert
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch set backend

Select orchestrator module backend

Example command:
:   ```bash
    ceph orch set backend my_module_name
    ```

Parameters:
:   - **module_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch set-managed

Set ‘unmanaged: false’ for the given service name

Example command:
:   ```bash
    ceph orch set-managed my_service_name
    ```

Parameters:
:   - **service_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch set-unmanaged

Set ‘unmanaged: true’ for the given service name

Example command:
:   ```bash
    ceph orch set-unmanaged my_service_name
    ```

Parameters:
:   - **service_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch status

Report configured backend and its status

Example command:
:   ```bash
    ceph orch status --detail plain
    ```

Parameters:
:   - **--detail**: CephBool
    - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## orch tuned-profile add-setting

Example command:
:   ```bash
    ceph orch tuned-profile add-setting my_profile_name my_setting
      my_value
    ```

Parameters:
:   - **profile_name**: (string)
    - **setting**: (string)
    - **value**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch tuned-profile apply

Add or update a tuned profile

Example command:
:   ```bash
    ceph orch tuned-profile apply --profile_name=string --placement=string
      --settings=string --no_overwrite
    ```

Parameters:
:   - **profile_name**: (string)
    - **placement**: (string)
    - **settings**: (string)
    - **--no_overwrite**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch tuned-profile ls

Example command:
:   ```bash
    ceph orch tuned-profile ls plain
    ```

Parameters:
:   - **--format**: CephChoices strings=(plain json json-pretty yaml xml-pretty xml)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## orch tuned-profile rm

Example command:
:   ```bash
    ceph orch tuned-profile rm my_profile_name
    ```

Parameters:
:   - **profile_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch tuned-profile rm-setting

Example command:
:   ```bash
    ceph orch tuned-profile rm-setting my_profile_name my_setting
    ```

Parameters:
:   - **profile_name**: (string)
    - **setting**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch upgrade check

Check service versions vs available and target containers

Example command:
:   ```bash
    ceph orch upgrade check my_image my_ceph_version
    ```

Parameters:
:   - **image**: (string)
    - **ceph_version**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch upgrade ls

Check for available versions (or tags) we can upgrade to

Example command:
:   ```bash
    ceph orch upgrade ls my_image --tags --show_all_versions
    ```

Parameters:
:   - **image**: (string)
    - **--tags**: CephBool
    - **--show_all_versions**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## orch upgrade pause

Pause an in-progress upgrade

Example command:
:   ```bash
    ceph orch upgrade pause
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch upgrade resume

Resume paused upgrade

Example command:
:   ```bash
    ceph orch upgrade resume
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch upgrade start

Initiate upgrade

Example command:
:   ```bash
    ceph orch upgrade start --image=string --daemon_types=string
      --hosts=string --services=string --limit=1 --ceph_version=string
    ```

Parameters:
:   - **image**: (string)
    - **--daemon_types**: (string)
    - **--hosts**: (string)
    - **--services**: (string)
    - **--limit**: CephInt
    - **--ceph_version**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch upgrade status

Check the status of any potential ongoing upgrade operation

Example command:
:   ```bash
    ceph orch upgrade status
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## orch upgrade stop

Stop an in-progress upgrade

Example command:
:   ```bash
    ceph orch upgrade stop
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

# osd

## osd perf counters get

fetch osd perf counters

Example command:
:   ```bash
    ceph osd perf counters get 1
    ```

Parameters:
:   - **query_id**: CephInt

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## osd perf query add

add osd perf query

Example command:
:   ```bash
    ceph osd perf query add client_id
    ```

Parameters:
:   - **query**: CephChoices strings=(client_id rbd_image_id all_subkeys)

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

## osd perf query remove

remove osd perf query

Example command:
:   ```bash
    ceph osd perf query remove 1
    ```

Parameters:
:   - **query_id**: CephInt

Ceph Module:
:   mgr

Required Permissions:
:   `w`

Command Flags:
:   `mgr`

# progress

## progress

Show progress of recovery operations

Example command:
:   ```bash
    ceph progress
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## progress clear

Reset progress tracking

Example command:
:   ```bash
    ceph progress clear
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## progress json

Show machine readable progress information

Example command:
:   ```bash
    ceph progress json
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## progress off

Disable progress tracking

Example command:
:   ```bash
    ceph progress off
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## progress on

Enable progress tracking

Example command:
:   ```bash
    ceph progress on
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

# restful

## restful create-key

Create an API key with this name

Example command:
:   ```bash
    ceph restful create-key my_key_name
    ```

Parameters:
:   - **key_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## restful create-self-signed-cert

Create localized self signed certificate

Example command:
:   ```bash
    ceph restful create-self-signed-cert
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## restful delete-key

Delete an API key with this name

Example command:
:   ```bash
    ceph restful delete-key my_key_name
    ```

Parameters:
:   - **key_name**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

## restful list-keys

List all API keys

Example command:
:   ```bash
    ceph restful list-keys
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

Command Flags:
:   `mgr`

## restful restart

Restart API server

Example command:
:   ```bash
    ceph restful restart
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

Command Flags:
:   `mgr`

# add_bootstrap_peer_hint

add peer address as potential bootstrap peer for cluster bringup

Example command:
:   ```bash
    ceph add_bootstrap_peer_hint 0.0.0.0
    ```

Parameters:
:   - **addr**: CephIPAddr

Ceph Module:
:   mon

Required Permissions:
:   `rw`

# add_bootstrap_peer_hintv

add peer address vector as potential bootstrap peer for cluster
bringup

Example command:
:   ```bash
    ceph add_bootstrap_peer_hintv my_addrv
    ```

Parameters:
:   - **addrv**: (string)

Ceph Module:
:   mon

Required Permissions:
:   `rw`

# auth

## auth add

add auth info for <entity> from input file, or random key if no input
is given, and/or any caps specified in the command

Example command:
:   ```bash
    ceph auth add --entity=string --caps=string
    ```

Parameters:
:   - **entity**: (string)
    - **caps**: (can be repeated)

Ceph Module:
:   auth

Required Permissions:
:   `rwx`

## auth caps

update caps for <name> from caps specified in the command

Example command:
:   ```bash
    ceph auth caps --entity=string --caps=string
    ```

Parameters:
:   - **entity**: (string)
    - **caps**: (can be repeated)

Ceph Module:
:   auth

Required Permissions:
:   `rwx`

## auth clear-pending

clear pending key

Example command:
:   ```bash
    ceph auth clear-pending my_entity
    ```

Parameters:
:   - **entity**: (string)

Ceph Module:
:   auth

Required Permissions:
:   `rwx`

## auth commit-pending

rotate pending key into active position

Example command:
:   ```bash
    ceph auth commit-pending my_entity
    ```

Parameters:
:   - **entity**: (string)

Ceph Module:
:   auth

Required Permissions:
:   `rwx`

## auth del

delete all caps for <name>

Example command:
:   ```bash
    ceph auth del my_entity
    ```

Parameters:
:   - **entity**: (string)

Ceph Module:
:   auth

Required Permissions:
:   `rwx`

Command Flags:
:   `deprecated`

## auth export

write keyring for requested entity, or master keyring if none given

Example command:
:   ```bash
    ceph auth export my_entity
    ```

Parameters:
:   - **entity**: (string)

Ceph Module:
:   auth

Required Permissions:
:   `rx`

## auth get

write keyring file with requested key

Example command:
:   ```bash
    ceph auth get my_entity
    ```

Parameters:
:   - **entity**: (string)

Ceph Module:
:   auth

Required Permissions:
:   `rx`

## auth get-key

display requested key

Example command:
:   ```bash
    ceph auth get-key my_entity
    ```

Parameters:
:   - **entity**: (string)

Ceph Module:
:   auth

Required Permissions:
:   `rx`

## auth get-or-create

add auth info for <entity> from input file, or random key if no input
given, and/or any caps specified in the command

Example command:
:   ```bash
    ceph auth get-or-create --entity=string --caps=string
    ```

Parameters:
:   - **entity**: (string)
    - **caps**: (can be repeated)

Ceph Module:
:   auth

Required Permissions:
:   `rwx`

## auth get-or-create-key

get, or add, key for <name> from system/caps pairs specified in the
command. If key already exists, any given caps must match the
existing caps for that key.

Example command:
:   ```bash
    ceph auth get-or-create-key --entity=string --caps=string
    ```

Parameters:
:   - **entity**: (string)
    - **caps**: (can be repeated)

Ceph Module:
:   auth

Required Permissions:
:   `rwx`

## auth get-or-create-pending

generate and/or retrieve existing pending key (rotated into place on
first use)

Example command:
:   ```bash
    ceph auth get-or-create-pending my_entity
    ```

Parameters:
:   - **entity**: (string)

Ceph Module:
:   auth

Required Permissions:
:   `rwx`

## auth import

auth import: read keyring file from -i <file>

Example command:
:   ```bash
    ceph auth import
    ```

Ceph Module:
:   auth

Required Permissions:
:   `rwx`

## auth list

list authentication state

Example command:
:   ```bash
    ceph auth list
    ```

Ceph Module:
:   auth

Required Permissions:
:   `rx`

Command Flags:
:   `deprecated`

## auth ls

list authentication state

Example command:
:   ```bash
    ceph auth ls
    ```

Ceph Module:
:   auth

Required Permissions:
:   `rx`

## auth print-key

display requested key

Example command:
:   ```bash
    ceph auth print-key my_entity
    ```

Parameters:
:   - **entity**: (string)

Ceph Module:
:   auth

Required Permissions:
:   `rx`

## auth print_key

display requested key

Example command:
:   ```bash
    ceph auth print_key my_entity
    ```

Parameters:
:   - **entity**: (string)

Ceph Module:
:   auth

Required Permissions:
:   `rx`

## auth rm

remove all caps for <name>

Example command:
:   ```bash
    ceph auth rm my_entity
    ```

Parameters:
:   - **entity**: (string)

Ceph Module:
:   auth

Required Permissions:
:   `rwx`

## auth rotate

rotate entity key

Example command:
:   ```bash
    ceph auth rotate my_entity
    ```

Parameters:
:   - **entity**: (string)

Ceph Module:
:   auth

Required Permissions:
:   `rwx`

# compact

cause compaction of monitor’s RocksDB storage

Example command:
:   ```bash
    ceph compact
    ```

Ceph Module:
:   mon

Required Permissions:
:   `rw`

# config

## config assimilate-conf

Assimilate options from a conf, and return a new, minimal conf file

Example command:
:   ```bash
    ceph config assimilate-conf
    ```

Ceph Module:
:   config

Required Permissions:
:   `rw`

## config dump

Show all configuration option(s)

Example command:
:   ```bash
    ceph config dump
    ```

Ceph Module:
:   mon

Required Permissions:
:   `r`

## config generate-minimal-conf

Generate a minimal ceph.conf file

Example command:
:   ```bash
    ceph config generate-minimal-conf
    ```

Ceph Module:
:   config

Required Permissions:
:   `r`

## config get

Show configuration option(s) for an entity

Example command:
:   ```bash
    ceph config get string my_key
    ```

Parameters:
:   - **who**: (string)
    - **key**: (string)

Ceph Module:
:   config

Required Permissions:
:   `r`

## config help

Describe a configuration option

Example command:
:   ```bash
    ceph config help my_key
    ```

Parameters:
:   - **key**: (string)

Ceph Module:
:   config

Required Permissions:
:   `r`

## config log

Show recent history of config changes

Example command:
:   ```bash
    ceph config log 1
    ```

Parameters:
:   - **num**: CephInt

Ceph Module:
:   config

Required Permissions:
:   `r`

## config ls

List available configuration options

Example command:
:   ```bash
    ceph config ls
    ```

Ceph Module:
:   config

Required Permissions:
:   `r`

## config reset

Revert configuration to a historical version specified by <num>

Example command:
:   ```bash
    ceph config reset 1
    ```

Parameters:
:   - **num**: CephInt range= `0`

Ceph Module:
:   config

Required Permissions:
:   `rw`

## config rm

Clear a configuration option for one or more entities

Example command:
:   ```bash
    ceph config rm string my_name
    ```

Parameters:
:   - **who**: (string)
    - **name**: (string)

Ceph Module:
:   config

Required Permissions:
:   `rw`

## config set

Set a configuration option for one or more entities

Example command:
:   ```bash
    ceph config set --who=string --name=string --value=string --force
    ```

Parameters:
:   - **who**: (string)
    - **name**: (string)
    - **value**: (string)
    - **force**: CephBool

Ceph Module:
:   config

Required Permissions:
:   `rw`

## config show

Show running configuration

Example command:
:   ```bash
    ceph config show string my_key
    ```

Parameters:
:   - **who**: (string)
    - **key**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

## config show-with-defaults

Show running configuration (including compiled-in defaults)

Example command:
:   ```bash
    ceph config show-with-defaults string
    ```

Parameters:
:   - **who**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

# config-key

## config-key del

delete <key>

Example command:
:   ```bash
    ceph config-key del my_key
    ```

Parameters:
:   - **key**: (string)

Ceph Module:
:   config-key

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## config-key dump

dump keys and values (with optional prefix)

Example command:
:   ```bash
    ceph config-key dump my_key
    ```

Parameters:
:   - **key**: (string)

Ceph Module:
:   config-key

Required Permissions:
:   `r`

## config-key exists

check for <key>’s existence

Example command:
:   ```bash
    ceph config-key exists my_key
    ```

Parameters:
:   - **key**: (string)

Ceph Module:
:   config-key

Required Permissions:
:   `r`

## config-key get

get <key>

Example command:
:   ```bash
    ceph config-key get my_key
    ```

Parameters:
:   - **key**: (string)

Ceph Module:
:   config-key

Required Permissions:
:   `r`

## config-key list

list keys

Example command:
:   ```bash
    ceph config-key list
    ```

Ceph Module:
:   config-key

Required Permissions:
:   `r`

Command Flags:
:   `deprecated`

## config-key ls

list keys

Example command:
:   ```bash
    ceph config-key ls
    ```

Ceph Module:
:   config-key

Required Permissions:
:   `r`

## config-key put

put <key>, value <val>

Example command:
:   ```bash
    ceph config-key put my_key my_val
    ```

Parameters:
:   - **key**: (string)
    - **val**: (string)

Ceph Module:
:   config-key

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## config-key rm

rm <key>

Example command:
:   ```bash
    ceph config-key rm my_key
    ```

Parameters:
:   - **key**: (string)

Ceph Module:
:   config-key

Required Permissions:
:   `rw`

## config-key set

set <key> to value <val>

Example command:
:   ```bash
    ceph config-key set my_key my_val
    ```

Parameters:
:   - **key**: (string)
    - **val**: (string)

Ceph Module:
:   config-key

Required Permissions:
:   `rw`

# connection

## connection scores dump

show the scores used in connectivity-based elections

Example command:
:   ```bash
    ceph connection scores dump
    ```

Ceph Module:
:   mon

Required Permissions:
:   `rwx`

## connection scores reset

reset the scores used in connectivity-based elections

Example command:
:   ```bash
    ceph connection scores reset
    ```

Ceph Module:
:   mon

Required Permissions:
:   `rwx`

# device

## device info

Show information about a device

Example command:
:   ```bash
    ceph device info my_devid
    ```

Parameters:
:   - **devid**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

## device ls

Show devices

Example command:
:   ```bash
    ceph device ls
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

## device ls-by-daemon

Show devices associated with a daemon

Example command:
:   ```bash
    ceph device ls-by-daemon string
    ```

Parameters:
:   - **who**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

## device ls-by-host

Show devices on a host

Example command:
:   ```bash
    ceph device ls-by-host my_host
    ```

Parameters:
:   - **host**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

## device rm-life-expectancy

Clear predicted device life expectancy

Example command:
:   ```bash
    ceph device rm-life-expectancy my_devid
    ```

Parameters:
:   - **devid**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

## device set-life-expectancy

Set predicted device life expectancy

Example command:
:   ```bash
    ceph device set-life-expectancy my_devid my_from my_to
    ```

Parameters:
:   - **devid**: (string)
    - **from**: (string)
    - **to**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

# df

show cluster free space stats

Example command:
:   ```bash
    ceph df detail
    ```

Parameters:
:   - **detail**: CephChoices strings=(detail)

Ceph Module:
:   mon

Required Permissions:
:   `r`

# dump_historic_ops

show recent ops

Example command:
:   ```bash
    ceph dump_historic_ops
    ```

Ceph Module:
:   mon

Required Permissions:
:   `r`

# dump_historic_ops_by_duration

show recent ops sorted by duration

Example command:
:   ```bash
    ceph dump_historic_ops_by_duration
    ```

Ceph Module:
:   mon

Required Permissions:
:   `r`

# dump_historic_slow_ops

show recent slow ops

Example command:
:   ```bash
    ceph dump_historic_slow_ops
    ```

Ceph Module:
:   mon

Required Permissions:
:   `r`

# dump_ops_in_flight

show the ops currently in flight

Example command:
:   ```bash
    ceph dump_ops_in_flight
    ```

Ceph Module:
:   mon

Required Permissions:
:   `r`

# features

report of connected features

Example command:
:   ```bash
    ceph features
    ```

Ceph Module:
:   mon

Required Permissions:
:   `r`

# fs

## fs add_data_pool

add data pool <pool>

Example command:
:   ```bash
    ceph fs add_data_pool my_fs_name my_pool
    ```

Parameters:
:   - **fs_name**: (string)
    - **pool**: (string)

Ceph Module:
:   mds

Required Permissions:
:   `rw`

## fs authorize

add auth for <entity> to access file system <filesystem> based on
following directory and permissions pairs

Example command:
:   ```bash
    ceph fs authorize --filesystem=string --entity=string --caps=string
    ```

Parameters:
:   - **filesystem**: (string)
    - **entity**: (string)
    - **caps**: (can be repeated)

Ceph Module:
:   auth

Required Permissions:
:   `rwx`

## fs compat

manipulate compat settings

Example command:
:   ```bash
    ceph fs compat --fs_name=string --subop=rm_compat --feature=1
      --feature_str=string
    ```

Parameters:
:   - **fs_name**: (string)
    - **subop**: CephChoices strings=(rm_compat rm_incompat add_compat add_incompat)
    - **feature**: CephInt
    - **feature_str**: (string)

Ceph Module:
:   fs

Required Permissions:
:   `rw`

## fs compat show

show fs compatibility settings

Example command:
:   ```bash
    ceph fs compat show my_fs_name
    ```

Parameters:
:   - **fs_name**: (string)

Ceph Module:
:   mds

Required Permissions:
:   `r`

## fs dump

dump all CephFS status, optionally from epoch

Example command:
:   ```bash
    ceph fs dump 1
    ```

Parameters:
:   - **epoch**: CephInt range= `0`

Ceph Module:
:   mds

Required Permissions:
:   `r`

## fs fail

bring the file system down and all of its ranks

Example command:
:   ```bash
    ceph fs fail my_fs_name --yes_i_really_mean_it
    ```

Parameters:
:   - **fs_name**: (string)
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   fs

Required Permissions:
:   `rw`

## fs feature ls

list available cephfs features to be set/unset

Example command:
:   ```bash
    ceph fs feature ls
    ```

Ceph Module:
:   mds

Required Permissions:
:   `r`

## fs flag set

Set a global CephFS flag

Example command:
:   ```bash
    ceph fs flag set enable_multiple my_val --yes_i_really_mean_it
    ```

Parameters:
:   - **flag_name**: CephChoices strings=(enable_multiple)
    - **val**: (string)
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   fs

Required Permissions:
:   `rw`

## fs get

get info about one filesystem

Example command:
:   ```bash
    ceph fs get my_fs_name
    ```

Parameters:
:   - **fs_name**: (string)

Ceph Module:
:   fs

Required Permissions:
:   `r`

## fs ls

list filesystems

Example command:
:   ```bash
    ceph fs ls
    ```

Ceph Module:
:   fs

Required Permissions:
:   `r`

## fs lsflags

list the flags set on a ceph filesystem

Example command:
:   ```bash
    ceph fs lsflags my_fs_name
    ```

Parameters:
:   - **fs_name**: (string)

Ceph Module:
:   fs

Required Permissions:
:   `r`

## fs mirror disable

disable mirroring for a ceph filesystem

Example command:
:   ```bash
    ceph fs mirror disable my_fs_name
    ```

Parameters:
:   - **fs_name**: (string)

Ceph Module:
:   mds

Required Permissions:
:   `rw`

## fs mirror enable

enable mirroring for a ceph filesystem

Example command:
:   ```bash
    ceph fs mirror enable my_fs_name
    ```

Parameters:
:   - **fs_name**: (string)

Ceph Module:
:   mds

Required Permissions:
:   `rw`

## fs mirror peer_add

add a mirror peer for a ceph filesystem

Example command:
:   ```bash
    ceph fs mirror peer_add --fs_name=string --uuid=string
      --remote_cluster_spec=string --remote_fs_name=string
    ```

Parameters:
:   - **fs_name**: (string)
    - **uuid**: (string)
    - **remote_cluster_spec**: (string)
    - **remote_fs_name**: (string)

Ceph Module:
:   mds

Required Permissions:
:   `rw`

## fs mirror peer_remove

remove a mirror peer for a ceph filesystem

Example command:
:   ```bash
    ceph fs mirror peer_remove my_fs_name my_uuid
    ```

Parameters:
:   - **fs_name**: (string)
    - **uuid**: (string)

Ceph Module:
:   mds

Required Permissions:
:   `rw`

## fs new

make new filesystem using named pools <metadata> and <data>

Example command:
:   ```bash
    ceph fs new --fs_name=string --metadata=string --data=string --force
      --allow_dangerous_metadata_overlay --fscid=0 --recover
    ```

Parameters:
:   - **fs_name**: goodchars= `[A-Za-z0-9-_.]`
    - **metadata**: (string)
    - **data**: (string)
    - **force**: CephBool
    - **allow_dangerous_metadata_overlay**: CephBool
    - **fscid**: CephInt range= `0`
    - **recover**: CephBool

Ceph Module:
:   fs

Required Permissions:
:   `rw`

## fs rename

rename a ceph file system

Example command:
:   ```bash
    ceph fs rename my_fs_name my_new_fs_name --yes_i_really_mean_it
    ```

Parameters:
:   - **fs_name**: (string)
    - **new_fs_name**: goodchars= `[A-Za-z0-9-_.]`
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   mds

Required Permissions:
:   `rw`

## fs required_client_features

add/remove required features of clients

Example command:
:   ```bash
    ceph fs required_client_features my_fs_name add my_val
    ```

Parameters:
:   - **fs_name**: (string)
    - **subop**: CephChoices strings=(add rm)
    - **val**: (string)

Ceph Module:
:   mds

Required Permissions:
:   `rw`

## fs reset

disaster recovery only: reset to a single-MDS map

Example command:
:   ```bash
    ceph fs reset my_fs_name --yes_i_really_mean_it
    ```

Parameters:
:   - **fs_name**: (string)
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   fs

Required Permissions:
:   `rw`

## fs rm

disable the named filesystem

Example command:
:   ```bash
    ceph fs rm my_fs_name --yes_i_really_mean_it
    ```

Parameters:
:   - **fs_name**: (string)
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   fs

Required Permissions:
:   `rw`

## fs rm_data_pool

remove data pool <pool>

Example command:
:   ```bash
    ceph fs rm_data_pool my_fs_name my_pool
    ```

Parameters:
:   - **fs_name**: (string)
    - **pool**: (string)

Ceph Module:
:   mds

Required Permissions:
:   `rw`

## fs set

set fs parameter <var> to <val>

Example command:
:   ```bash
    ceph fs set --fs_name=string --var=max_mds --val=string
      --yes_i_really_mean_it --yes_i_really_really_mean_it
    ```

Parameters:
:   - **fs_name**: (string)
    - **var**: CephChoices strings=(max_mds allow_dirfrags allow_new_snaps allow_standby_replay bal_rank_mask balance_automate balancer cluster_down down inline_data joinable max_file_size max_xattr_size min_compat_client refuse_client_session refuse_standby_for_another_fs session_autoclose session_timeout standby_count_wanted)
    - **val**: (string)
    - **yes_i_really_mean_it**: CephBool
    - **yes_i_really_really_mean_it**: CephBool

Ceph Module:
:   mds

Required Permissions:
:   `rw`

## fs set-default

set the default to the named filesystem

Example command:
:   ```bash
    ceph fs set-default my_fs_name
    ```

Parameters:
:   - **fs_name**: (string)

Ceph Module:
:   fs

Required Permissions:
:   `rw`

## fs set_default

set the default to the named filesystem

Example command:
:   ```bash
    ceph fs set_default my_fs_name
    ```

Parameters:
:   - **fs_name**: (string)

Ceph Module:
:   fs

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## fs swap

swap ceph file system names

Example command:
:   ```bash
    ceph fs swap --fs1_name=string --fs1_id=0 --fs2_name=string --fs2_id=0
      --swap_fscids=yes --yes_i_really_mean_it
    ```

Parameters:
:   - **fs1_name**: (string)
    - **fs1_id**: CephInt range= `0`
    - **fs2_name**: (string)
    - **fs2_id**: CephInt range= `0`
    - **swap_fscids**: CephChoices strings=(yes no)
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   mds

Required Permissions:
:   `rw`

# fsid

show cluster FSID/UUID

Example command:
:   ```bash
    ceph fsid
    ```

Ceph Module:
:   mon

Required Permissions:
:   `r`

# health

## health

show cluster health

Example command:
:   ```bash
    ceph health detail
    ```

Parameters:
:   - **detail**: CephChoices strings=(detail)

Ceph Module:
:   mon

Required Permissions:
:   `r`

## health mute

mute health alert

Example command:
:   ```bash
    ceph health mute my_code my_ttl --sticky
    ```

Parameters:
:   - **code**: (string)
    - **ttl**: (string)
    - **sticky**: CephBool

Ceph Module:
:   mon

Required Permissions:
:   `w`

## health unmute

unmute existing health alert mute(s)

Example command:
:   ```bash
    ceph health unmute my_code
    ```

Parameters:
:   - **code**: (string)

Ceph Module:
:   mon

Required Permissions:
:   `w`

# heap

show heap usage info (available only if compiled with tcmalloc)

Example command:
:   ```bash
    ceph heap dump my_value
    ```

Parameters:
:   - **heapcmd**: CephChoices strings=(dump start_profiler stop_profiler release stats)
    - **value**: (string)

Ceph Module:
:   mon

Required Permissions:
:   `rw`

# injectargs

inject config arguments into monitor

Example command:
:   ```bash
    ceph injectargs --injected_args=string
    ```

Parameters:
:   - **injected_args**: (can be repeated)

Ceph Module:
:   mon

Required Permissions:
:   `rw`

# log

## log

log supplied text to the monitor log

Example command:
:   ```bash
    ceph log --logtext=string
    ```

Parameters:
:   - **logtext**: (can be repeated)

Ceph Module:
:   mon

Required Permissions:
:   `rw`

## log last

print last few lines of the cluster log

Example command:
:   ```bash
    ceph log last 1 debug *
    ```

Parameters:
:   - **num**: CephInt range= `1`
    - **level**: CephChoices strings=(debug info sec warn error)
    - **channel**: CephChoices strings=(\* cluster audit cephadm)

Ceph Module:
:   mon

Required Permissions:
:   `r`

# mds

## mds compat rm_compat

remove compatible feature

Example command:
:   ```bash
    ceph mds compat rm_compat 1
    ```

Parameters:
:   - **feature**: CephInt range= `0`

Ceph Module:
:   mds

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## mds compat rm_incompat

remove incompatible feature

Example command:
:   ```bash
    ceph mds compat rm_incompat 1
    ```

Parameters:
:   - **feature**: CephInt range= `0`

Ceph Module:
:   mds

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## mds compat show

show mds compatibility settings

Example command:
:   ```bash
    ceph mds compat show
    ```

Ceph Module:
:   mds

Required Permissions:
:   `r`

Command Flags:
:   `deprecated`

## mds count-metadata

count MDSs by metadata field property

Example command:
:   ```bash
    ceph mds count-metadata my_property
    ```

Parameters:
:   - **property**: (string)

Ceph Module:
:   mds

Required Permissions:
:   `r`

## mds fail

Mark MDS failed: trigger a failover if a standby is available

Example command:
:   ```bash
    ceph mds fail my_role_or_gid --yes_i_really_mean_it
    ```

Parameters:
:   - **role_or_gid**: (string)
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   mds

Required Permissions:
:   `rw`

## mds last-seen

fetch metadata for mds <id>

Example command:
:   ```bash
    ceph mds last-seen my_id
    ```

Parameters:
:   - **id**: (string)

Ceph Module:
:   mds

Required Permissions:
:   `r`

## mds metadata

fetch metadata for mds <role>

Example command:
:   ```bash
    ceph mds metadata string
    ```

Parameters:
:   - **who**: (string)

Ceph Module:
:   mds

Required Permissions:
:   `r`

## mds ok-to-stop

check whether stopping the specified MDS would reduce immediate
availability

Example command:
:   ```bash
    ceph mds ok-to-stop --ids=string
    ```

Parameters:
:   - **ids**: (can be repeated)

Ceph Module:
:   mds

Required Permissions:
:   `r`

## mds repaired

mark a damaged MDS rank as no longer damaged

Example command:
:   ```bash
    ceph mds repaired my_role
    ```

Parameters:
:   - **role**: (string)

Ceph Module:
:   mds

Required Permissions:
:   `rw`

## mds rm

remove nonactive mds

Example command:
:   ```bash
    ceph mds rm 1
    ```

Parameters:
:   - **gid**: CephInt range= `0`

Ceph Module:
:   mds

Required Permissions:
:   `rw`

## mds versions

check running versions of MDSs

Example command:
:   ```bash
    ceph mds versions
    ```

Ceph Module:
:   mds

Required Permissions:
:   `r`

# mgr

## mgr count-metadata

count ceph-mgr daemons by metadata field property

Example command:
:   ```bash
    ceph mgr count-metadata my_property
    ```

Parameters:
:   - **property**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

## mgr dump

dump the latest MgrMap

Example command:
:   ```bash
    ceph mgr dump 1
    ```

Parameters:
:   - **epoch**: CephInt range= `0`

Ceph Module:
:   mgr

Required Permissions:
:   `r`

## mgr fail

treat the named manager daemon as failed

Example command:
:   ```bash
    ceph mgr fail string
    ```

Parameters:
:   - **who**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

## mgr metadata

dump metadata for all daemons or a specific daemon

Example command:
:   ```bash
    ceph mgr metadata string
    ```

Parameters:
:   - **who**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `r`

## mgr module disable

disable mgr module

Example command:
:   ```bash
    ceph mgr module disable my_module
    ```

Parameters:
:   - **module**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

## mgr module enable

enable mgr module

Example command:
:   ```bash
    ceph mgr module enable my_module --force
    ```

Parameters:
:   - **module**: (string)
    - **force**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

## mgr module force disable

force disable a always-on mgr module

Example command:
:   ```bash
    ceph mgr module force disable my_module --yes_i_really_mean_it
    ```

Parameters:
:   - **module**: (string)
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

## mgr module ls

list active mgr modules

Example command:
:   ```bash
    ceph mgr module ls
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

## mgr services

list service endpoints provided by mgr modules

Example command:
:   ```bash
    ceph mgr services
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

## mgr set

set mgr parameter <var> to <val>

Example command:
:   ```bash
    ceph mgr set down my_val
    ```

Parameters:
:   - **var**: CephChoices strings=(down)
    - **val**: (string)

Ceph Module:
:   mgr

Required Permissions:
:   `rw`

## mgr stat

dump basic info about the mgr cluster state

Example command:
:   ```bash
    ceph mgr stat
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

## mgr versions

check running versions of ceph-mgr daemons

Example command:
:   ```bash
    ceph mgr versions
    ```

Ceph Module:
:   mgr

Required Permissions:
:   `r`

# mon

## mon add

add new monitor named <name> at <addr>, possibly with CRUSH location
<location>

Example command:
:   ```bash
    ceph mon add --name=string --addr=0.0.0.0 --location=string
    ```

Parameters:
:   - **name**: (string)
    - **addr**: CephIPAddr
    - **location**: goodchars= `[A-Za-z0-9-_.=]` (can be repeated)

Ceph Module:
:   mon

Required Permissions:
:   `rw`

## mon add disallowed_leader

prevent the named mon from being a leader

Example command:
:   ```bash
    ceph mon add disallowed_leader my_name
    ```

Parameters:
:   - **name**: (string)

Ceph Module:
:   mon

Required Permissions:
:   `rw`

## mon count-metadata

count mons by metadata field property

Example command:
:   ```bash
    ceph mon count-metadata my_property
    ```

Parameters:
:   - **property**: (string)

Ceph Module:
:   mon

Required Permissions:
:   `r`

## mon disable_stretch_mode

disable stretch mode, reverting to normal peering rules

Example command:
:   ```bash
    ceph mon disable_stretch_mode my_crush_rule --yes_i_really_mean_it
    ```

Parameters:
:   - **crush_rule**: (string)
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   mon

Required Permissions:
:   `rw`

## mon dump

dump formatted monmap (optionally from epoch)

Example command:
:   ```bash
    ceph mon dump 1
    ```

Parameters:
:   - **epoch**: CephInt range= `0`

Ceph Module:
:   mon

Required Permissions:
:   `r`

## mon enable-msgr2

enable the msgr2 protocol on port 3300

Example command:
:   ```bash
    ceph mon enable-msgr2
    ```

Ceph Module:
:   mon

Required Permissions:
:   `rw`

## mon enable_stretch_mode

enable stretch mode, changing the peering rules and failure handling
on all pools with <tiebreaker_mon> as the tiebreaker and setting
<dividing_bucket> locations as the units for stretching across

Example command:
:   ```bash
    ceph mon enable_stretch_mode my_tiebreaker_mon my_new_crush_rule
      my_dividing_bucket
    ```

Parameters:
:   - **tiebreaker_mon**: (string)
    - **new_crush_rule**: (string)
    - **dividing_bucket**: (string)

Ceph Module:
:   mon

Required Permissions:
:   `rw`

## mon feature ls

list available mon map features to be set/unset

Example command:
:   ```bash
    ceph mon feature ls --with_value
    ```

Parameters:
:   - **with_value**: CephBool

Ceph Module:
:   mon

Required Permissions:
:   `r`

## mon feature set

set provided feature on mon map

Example command:
:   ```bash
    ceph mon feature set my_feature_name --yes_i_really_mean_it
    ```

Parameters:
:   - **feature_name**: (string)
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   mon

Required Permissions:
:   `rw`

## mon getmap

get monmap

Example command:
:   ```bash
    ceph mon getmap 1
    ```

Parameters:
:   - **epoch**: CephInt range= `0`

Ceph Module:
:   mon

Required Permissions:
:   `r`

## mon metadata

fetch metadata for mon <id>

Example command:
:   ```bash
    ceph mon metadata my_id
    ```

Parameters:
:   - **id**: (string)

Ceph Module:
:   mon

Required Permissions:
:   `r`

## mon ok-to-add-offline

check whether adding a mon and not starting it would break quorum

Example command:
:   ```bash
    ceph mon ok-to-add-offline
    ```

Ceph Module:
:   mon

Required Permissions:
:   `r`

## mon ok-to-rm

check whether removing the specified mon would break quorum

Example command:
:   ```bash
    ceph mon ok-to-rm my_id
    ```

Parameters:
:   - **id**: (string)

Ceph Module:
:   mon

Required Permissions:
:   `r`

## mon ok-to-stop

check whether mon(s) can be safely stopped without reducing immediate
availability

Example command:
:   ```bash
    ceph mon ok-to-stop --ids=string
    ```

Parameters:
:   - **ids**: (can be repeated)

Ceph Module:
:   mon

Required Permissions:
:   `r`

## mon remove

remove monitor named <name>

Example command:
:   ```bash
    ceph mon remove my_name
    ```

Parameters:
:   - **name**: (string)

Ceph Module:
:   mon

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## mon rm

remove monitor named <name>

Example command:
:   ```bash
    ceph mon rm my_name
    ```

Parameters:
:   - **name**: (string)

Ceph Module:
:   mon

Required Permissions:
:   `rw`

## mon rm disallowed_leader

allow the named mon to be a leader again

Example command:
:   ```bash
    ceph mon rm disallowed_leader my_name
    ```

Parameters:
:   - **name**: (string)

Ceph Module:
:   mon

Required Permissions:
:   `rw`

## mon scrub

scrub the monitor stores

Example command:
:   ```bash
    ceph mon scrub
    ```

Ceph Module:
:   mon

Required Permissions:
:   `rw`

## mon set election_strategy

set the election strategy to use; choices classic, disallow,
connectivity

Example command:
:   ```bash
    ceph mon set election_strategy my_strategy
    ```

Parameters:
:   - **strategy**: (string)

Ceph Module:
:   mon

Required Permissions:
:   `rw`

## mon set-addrs

set the addrs (IPs and ports) a specific monitor binds to

Example command:
:   ```bash
    ceph mon set-addrs my_name my_addrs
    ```

Parameters:
:   - **name**: (string)
    - **addrs**: (string)

Ceph Module:
:   mon

Required Permissions:
:   `rw`

## mon set-rank

set the rank for the specified mon

Example command:
:   ```bash
    ceph mon set-rank my_name 1
    ```

Parameters:
:   - **name**: (string)
    - **rank**: CephInt

Ceph Module:
:   mon

Required Permissions:
:   `rw`

## mon set-weight

set the weight for the specified mon

Example command:
:   ```bash
    ceph mon set-weight my_name 1
    ```

Parameters:
:   - **name**: (string)
    - **weight**: CephInt range= `0..65535`

Ceph Module:
:   mon

Required Permissions:
:   `rw`

## mon set_location

specify location <args> for the monitor <name>, using CRUSH bucket
names

Example command:
:   ```bash
    ceph mon set_location --name=string --args=string
    ```

Parameters:
:   - **name**: (string)
    - **args**: goodchars= `[A-Za-z0-9-_.=]` (can be repeated)

Ceph Module:
:   mon

Required Permissions:
:   `rw`

## mon set_new_tiebreaker

switch the stretch tiebreaker to be the named mon

Example command:
:   ```bash
    ceph mon set_new_tiebreaker my_name --yes_i_really_mean_it
    ```

Parameters:
:   - **name**: (string)
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   mon

Required Permissions:
:   `rw`

## mon stat

summarize monitor status

Example command:
:   ```bash
    ceph mon stat
    ```

Ceph Module:
:   mon

Required Permissions:
:   `r`

## mon versions

check running versions of monitors

Example command:
:   ```bash
    ceph mon versions
    ```

Ceph Module:
:   mon

Required Permissions:
:   `r`

# mon_status

report status of monitors

Example command:
:   ```bash
    ceph mon_status
    ```

Ceph Module:
:   mon

Required Permissions:
:   `r`

# node ls

list all nodes in cluster [type]

Example command:
:   ```bash
    ceph node ls all
    ```

Parameters:
:   - **type**: CephChoices strings=(all osd mon mds mgr)

Ceph Module:
:   mon

Required Permissions:
:   `r`

# ops

show the ops currently in flight

Example command:
:   ```bash
    ceph ops
    ```

Ceph Module:
:   mon

Required Permissions:
:   `r`

# osd

## osd add-nodown

mark osd(s) <id> [<id>…] as nodown, or use <all|any> to mark all
osds as nodown

Example command:
:   ```bash
    ceph osd add-nodown --ids=string
    ```

Parameters:
:   - **ids**: (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## osd add-noin

mark osd(s) <id> [<id>…] as noin, or use <all|any> to mark all osds
as noin

Example command:
:   ```bash
    ceph osd add-noin --ids=string
    ```

Parameters:
:   - **ids**: (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## osd add-noout

mark osd(s) <id> [<id>…] as noout, or use <all|any> to mark all osds
as noout

Example command:
:   ```bash
    ceph osd add-noout --ids=string
    ```

Parameters:
:   - **ids**: (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## osd add-noup

mark osd(s) <id> [<id>…] as noup, or use <all|any> to mark all osds
as noup

Example command:
:   ```bash
    ceph osd add-noup --ids=string
    ```

Parameters:
:   - **ids**: (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## osd blacklist

add (optionally until <expire> seconds from now) or remove <addr> from
blacklist

Example command:
:   ```bash
    ceph osd blacklist add entityaddr 0.0
    ```

Parameters:
:   - **blacklistop**: CephChoices strings=(add rm)
    - **addr**: CephEntityAddr
    - **expire**: CephFloat range= `0.0`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## osd blacklist clear

clear all blacklisted clients

Example command:
:   ```bash
    ceph osd blacklist clear
    ```

Ceph Module:
:   osd

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## osd blacklist ls

show blacklisted clients

Example command:
:   ```bash
    ceph osd blacklist ls
    ```

Ceph Module:
:   osd

Required Permissions:
:   `r`

Command Flags:
:   `deprecated`

## osd blocked-by

print histogram of which OSDs are blocking their peers

Example command:
:   ```bash
    ceph osd blocked-by
    ```

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd blocklist

add (optionally until <expire> seconds from now) or remove <addr> from
blocklist

Example command:
:   ```bash
    ceph osd blocklist --blocklistop=add --addr=entityaddr --range=string
      --expire=0.0
    ```

Parameters:
:   - **blocklistop**: CephChoices strings=(add rm)
    - **addr**: CephEntityAddr
    - **range**: goodchars= `[range]`
    - **expire**: CephFloat range= `0.0`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd blocklist clear

clear all blocklisted clients

Example command:
:   ```bash
    ceph osd blocklist clear
    ```

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd blocklist ls

show blocklisted clients

Example command:
:   ```bash
    ceph osd blocklist ls
    ```

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd count-metadata

count OSDs by metadata field property

Example command:
:   ```bash
    ceph osd count-metadata my_property
    ```

Parameters:
:   - **property**: (string)

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd create

create new osd (with optional UUID and ID)

Example command:
:   ```bash
    ceph osd create uuid osd.0
    ```

Parameters:
:   - **uuid**: CephUUID
    - **id**: CephOsdName

Ceph Module:
:   osd

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## osd crush add

add or update crushmap position and weight for <name> with <weight>
and location <args>

Example command:
:   ```bash
    ceph osd crush add --id=osd.0 --weight=0.0 --args=string
    ```

Parameters:
:   - **id**: CephOsdName
    - **weight**: CephFloat range= `0.0`
    - **args**: goodchars= `[A-Za-z0-9-_.=]` (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush add-bucket

add no-parent (probably root) crush bucket <name> of type <type> to
location <args>

Example command:
:   ```bash
    ceph osd crush add-bucket --name=string --type=string --args=string
    ```

Parameters:
:   - **name**: goodchars= `[A-Za-z0-9-_.]`
    - **type**: (string)
    - **args**: goodchars= `[A-Za-z0-9-_.=]` (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush class create

create crush device class <class>

Example command:
:   ```bash
    ceph osd crush class create my_class
    ```

Parameters:
:   - **class**: goodchars= `[A-Za-z0-9-_]`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush class ls

list all crush device classes

Example command:
:   ```bash
    ceph osd crush class ls
    ```

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd crush class ls-osd

list all osds belonging to the specific <class>

Example command:
:   ```bash
    ceph osd crush class ls-osd my_class
    ```

Parameters:
:   - **class**: goodchars= `[A-Za-z0-9-_]`

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd crush class rename

rename crush device class <srcname> to <dstname>

Example command:
:   ```bash
    ceph osd crush class rename my_srcname my_dstname
    ```

Parameters:
:   - **srcname**: goodchars= `[A-Za-z0-9-_]`
    - **dstname**: goodchars= `[A-Za-z0-9-_]`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush class rm

remove crush device class <class>

Example command:
:   ```bash
    ceph osd crush class rm my_class
    ```

Parameters:
:   - **class**: goodchars= `[A-Za-z0-9-_]`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush create-or-move

create entry or move existing entry for <name> <weight> at/to location
<args>

Example command:
:   ```bash
    ceph osd crush create-or-move --id=osd.0 --weight=0.0 --args=string
    ```

Parameters:
:   - **id**: CephOsdName
    - **weight**: CephFloat range= `0.0`
    - **args**: goodchars= `[A-Za-z0-9-_.=]` (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush dump

dump crush map

Example command:
:   ```bash
    ceph osd crush dump
    ```

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd crush get-device-class

get classes of specified osd(s) <id> [<id>…]

Example command:
:   ```bash
    ceph osd crush get-device-class --ids=string
    ```

Parameters:
:   - **ids**: (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd crush get-tunable

get crush tunable <tunable>

Example command:
:   ```bash
    ceph osd crush get-tunable straw_calc_version
    ```

Parameters:
:   - **tunable**: CephChoices strings=(straw_calc_version)

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd crush link

link existing entry for <name> under location <args>

Example command:
:   ```bash
    ceph osd crush link --name=string --args=string
    ```

Parameters:
:   - **name**: (string)
    - **args**: goodchars= `[A-Za-z0-9-_.=]` (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush ls

list items beneath a node in the CRUSH tree

Example command:
:   ```bash
    ceph osd crush ls my_node
    ```

Parameters:
:   - **node**: goodchars= `[A-Za-z0-9-_.]`

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd crush move

move existing entry for <name> to location <args>

Example command:
:   ```bash
    ceph osd crush move --name=string --args=string
    ```

Parameters:
:   - **name**: goodchars= `[A-Za-z0-9-_.]`
    - **args**: goodchars= `[A-Za-z0-9-_.=]` (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush remove

remove <name> from crush map (everywhere, or just at <ancestor>)

Example command:
:   ```bash
    ceph osd crush remove my_name my_ancestor
    ```

Parameters:
:   - **name**: goodchars= `[A-Za-z0-9-_.]`
    - **ancestor**: goodchars= `[A-Za-z0-9-_.]`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## osd crush rename-bucket

rename bucket <srcname> to <dstname>

Example command:
:   ```bash
    ceph osd crush rename-bucket my_srcname my_dstname
    ```

Parameters:
:   - **srcname**: goodchars= `[A-Za-z0-9-_.]`
    - **dstname**: goodchars= `[A-Za-z0-9-_.]`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush reweight

change <name>’s weight to <weight> in crush map

Example command:
:   ```bash
    ceph osd crush reweight my_name 0.0
    ```

Parameters:
:   - **name**: goodchars= `[A-Za-z0-9-_.]`
    - **weight**: CephFloat range= `0.0`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush reweight-all

recalculate the weights for the tree to ensure they sum correctly

Example command:
:   ```bash
    ceph osd crush reweight-all
    ```

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush reweight-subtree

change all leaf items beneath <name> to <weight> in crush map

Example command:
:   ```bash
    ceph osd crush reweight-subtree my_name 0.0
    ```

Parameters:
:   - **name**: goodchars= `[A-Za-z0-9-_.]`
    - **weight**: CephFloat range= `0.0`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush rm

remove <name> from crush map (everywhere, or just at <ancestor>)

Example command:
:   ```bash
    ceph osd crush rm my_name my_ancestor
    ```

Parameters:
:   - **name**: goodchars= `[A-Za-z0-9-_.]`
    - **ancestor**: goodchars= `[A-Za-z0-9-_.]`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush rm-device-class

remove class of the osd(s) <id> [<id>…],or use <all|any> to remove
all.

Example command:
:   ```bash
    ceph osd crush rm-device-class --ids=string
    ```

Parameters:
:   - **ids**: (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush rule create-erasure

create crush rule <name> for erasure coded pool created with <profile>
(default default)

Example command:
:   ```bash
    ceph osd crush rule create-erasure my_name my_profile
    ```

Parameters:
:   - **name**: goodchars= `[A-Za-z0-9-_.]`
    - **profile**: goodchars= `[A-Za-z0-9-_.=]`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush rule create-replicated

create crush rule <name> for replicated pool to start from <root>,
replicate across buckets of type <type>, use devices of type <class>
(ssd or hdd)

Example command:
:   ```bash
    ceph osd crush rule create-replicated --name=string --root=string
      --type=string --class=string
    ```

Parameters:
:   - **name**: goodchars= `[A-Za-z0-9-_.]`
    - **root**: goodchars= `[A-Za-z0-9-_.]`
    - **type**: goodchars= `[A-Za-z0-9-_.]`
    - **class**: goodchars= `[A-Za-z0-9-_.]`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush rule create-simple

create crush rule <name> to start from <root>, replicate across
buckets of type <type>, using a choose mode of <firstn|indep> (default
firstn; indep best for erasure pools)

Example command:
:   ```bash
    ceph osd crush rule create-simple --name=string --root=string
      --type=string --mode=firstn
    ```

Parameters:
:   - **name**: goodchars= `[A-Za-z0-9-_.]`
    - **root**: goodchars= `[A-Za-z0-9-_.]`
    - **type**: goodchars= `[A-Za-z0-9-_.]`
    - **mode**: CephChoices strings=(firstn indep)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush rule dump

dump crush rule <name> (default all)

Example command:
:   ```bash
    ceph osd crush rule dump my_name
    ```

Parameters:
:   - **name**: goodchars= `[A-Za-z0-9-_.]`

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd crush rule list

list crush rules

Example command:
:   ```bash
    ceph osd crush rule list
    ```

Ceph Module:
:   osd

Required Permissions:
:   `r`

Command Flags:
:   `deprecated`

## osd crush rule ls

list crush rules

Example command:
:   ```bash
    ceph osd crush rule ls
    ```

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd crush rule ls-by-class

list all crush rules that reference the same <class>

Example command:
:   ```bash
    ceph osd crush rule ls-by-class my_class
    ```

Parameters:
:   - **class**: goodchars= `[A-Za-z0-9-_.]`

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd crush rule rename

rename crush rule <srcname> to <dstname>

Example command:
:   ```bash
    ceph osd crush rule rename my_srcname my_dstname
    ```

Parameters:
:   - **srcname**: goodchars= `[A-Za-z0-9-_.]`
    - **dstname**: goodchars= `[A-Za-z0-9-_.]`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush rule rm

remove crush rule <name>

Example command:
:   ```bash
    ceph osd crush rule rm my_name
    ```

Parameters:
:   - **name**: goodchars= `[A-Za-z0-9-_.]`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush set

set crush map from input file

Example command:
:   ```bash
    ceph osd crush set 1
    ```

Parameters:
:   - **prior_version**: CephInt

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush set

update crushmap position and weight for <name> to <weight> with
location <args>

Example command:
:   ```bash
    ceph osd crush set --id=osd.0 --weight=0.0 --args=string
    ```

Parameters:
:   - **id**: CephOsdName
    - **weight**: CephFloat range= `0.0`
    - **args**: goodchars= `[A-Za-z0-9-_.=]` (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush set-all-straw-buckets-to-straw2

convert all CRUSH current straw buckets to use the straw2 algorithm

Example command:
:   ```bash
    ceph osd crush set-all-straw-buckets-to-straw2
    ```

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush set-device-class

set the <class> of the osd(s) <id> [<id>…],or use <all|any> to set
all.

Example command:
:   ```bash
    ceph osd crush set-device-class --class=string --ids=string
    ```

Parameters:
:   - **class**: (string)
    - **ids**: (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush set-tunable

set crush tunable <tunable> to <value>

Example command:
:   ```bash
    ceph osd crush set-tunable straw_calc_version 1
    ```

Parameters:
:   - **tunable**: CephChoices strings=(straw_calc_version)
    - **value**: CephInt

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush show-tunables

show current crush tunables

Example command:
:   ```bash
    ceph osd crush show-tunables
    ```

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd crush swap-bucket

swap existing bucket contents from (orphan) bucket <source> and
<target>

Example command:
:   ```bash
    ceph osd crush swap-bucket my_source my_dest --yes_i_really_mean_it
    ```

Parameters:
:   - **source**: goodchars= `[A-Za-z0-9-_.]`
    - **dest**: goodchars= `[A-Za-z0-9-_.]`
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush tree

dump crush buckets and items in a tree view

Example command:
:   ```bash
    ceph osd crush tree --show_shadow
    ```

Parameters:
:   - **show_shadow**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd crush tunables

set crush tunables values to <profile>

Example command:
:   ```bash
    ceph osd crush tunables legacy
    ```

Parameters:
:   - **profile**: CephChoices strings=(legacy argonaut bobtail firefly hammer jewel optimal default)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush unlink

unlink <name> from crush map (everywhere, or just at <ancestor>)

Example command:
:   ```bash
    ceph osd crush unlink my_name my_ancestor
    ```

Parameters:
:   - **name**: goodchars= `[A-Za-z0-9-_.]`
    - **ancestor**: goodchars= `[A-Za-z0-9-_.]`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush weight-set create

create a weight-set for a given pool

Example command:
:   ```bash
    ceph osd crush weight-set create poolname flat
    ```

Parameters:
:   - **pool**: CephPoolname
    - **mode**: CephChoices strings=(flat positional)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush weight-set create-compat

create a default backward-compatible weight-set

Example command:
:   ```bash
    ceph osd crush weight-set create-compat
    ```

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush weight-set dump

dump crush weight sets

Example command:
:   ```bash
    ceph osd crush weight-set dump
    ```

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd crush weight-set ls

list crush weight sets

Example command:
:   ```bash
    ceph osd crush weight-set ls
    ```

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd crush weight-set reweight

set weight for an item (bucket or osd) in a pool’s weight-set

Example command:
:   ```bash
    ceph osd crush weight-set reweight --pool=poolname --item=string
      --weight=0.0
    ```

Parameters:
:   - **pool**: CephPoolname
    - **item**: (string)
    - **weight**: CephFloat range= `0.0` (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush weight-set reweight-compat

set weight for an item (bucket or osd) in the backward-compatible
weight-set

Example command:
:   ```bash
    ceph osd crush weight-set reweight-compat --item=string --weight=0.0
    ```

Parameters:
:   - **item**: (string)
    - **weight**: CephFloat range= `0.0` (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush weight-set rm

remove the weight-set for a given pool

Example command:
:   ```bash
    ceph osd crush weight-set rm poolname
    ```

Parameters:
:   - **pool**: CephPoolname

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd crush weight-set rm-compat

remove the backward-compatible weight-set

Example command:
:   ```bash
    ceph osd crush weight-set rm-compat
    ```

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd deep-scrub

initiate deep scrub on osd <who>, or use <all|any> to deep scrub all

Example command:
:   ```bash
    ceph osd deep-scrub string
    ```

Parameters:
:   - **who**: (string)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd destroy

mark osd as being destroyed. Keeps the ID intact (allowing reuse), but
removes cephx keys, config-key data and lockbox keys, rendering data
permanently unreadable.

Example command:
:   ```bash
    ceph osd destroy osd.0 --force --yes_i_really_mean_it
    ```

Parameters:
:   - **id**: CephOsdName
    - **force**: CephBool
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd df

show OSD utilization

Example command:
:   ```bash
    ceph osd df plain class my_filter
    ```

Parameters:
:   - **output_method**: CephChoices strings=(plain tree)
    - **filter_by**: CephChoices strings=(class name)
    - **filter**: (string)

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd down

set osd(s) <id> [<id>…] down, or use <any|all> to set all osds down

Example command:
:   ```bash
    ceph osd down --ids=string --definitely_dead
    ```

Parameters:
:   - **ids**: (can be repeated)
    - **definitely_dead**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd dump

print summary of OSD map

Example command:
:   ```bash
    ceph osd dump 1
    ```

Parameters:
:   - **epoch**: CephInt range= `0`

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd erasure-code-profile get

get erasure code profile <name>

Example command:
:   ```bash
    ceph osd erasure-code-profile get my_name
    ```

Parameters:
:   - **name**: goodchars= `[A-Za-z0-9-_.]`

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd erasure-code-profile ls

list all erasure code profiles

Example command:
:   ```bash
    ceph osd erasure-code-profile ls
    ```

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd erasure-code-profile rm

remove erasure code profile <name>

Example command:
:   ```bash
    ceph osd erasure-code-profile rm my_name
    ```

Parameters:
:   - **name**: goodchars= `[A-Za-z0-9-_.]`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd erasure-code-profile set

create erasure code profile <name> with [<key[=value]> …] pairs. Add
a --force at the end to override an existing profile (VERY DANGEROUS)

Example command:
:   ```bash
    ceph osd erasure-code-profile set --name=string --profile=string
      --force --yes_i_really_mean_it
    ```

Parameters:
:   - **name**: goodchars= `[A-Za-z0-9-_.]`
    - **profile**: (can be repeated)
    - **force**: CephBool
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd find

find osd <id> in the CRUSH map and show its location

Example command:
:   ```bash
    ceph osd find osd.0
    ```

Parameters:
:   - **id**: CephOsdName

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd force-create-pg

force creation of pg <pgid>

Example command:
:   ```bash
    ceph osd force-create-pg 0 --yes_i_really_mean_it
    ```

Parameters:
:   - **pgid**: CephPgid
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd force_healthy_stretch_mode

force a healthy stretch mode, requiring the full number of CRUSH
buckets to peer and letting all non-tiebreaker monitors be elected
leader

Example command:
:   ```bash
    ceph osd force_healthy_stretch_mode --yes_i_really_mean_it
    ```

Parameters:
:   - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd force_recovery_stretch_mode

try and force a recovery stretch mode, increasing the pool size to its
non-failure value if currently degraded and all monitor buckets are up

Example command:
:   ```bash
    ceph osd force_recovery_stretch_mode --yes_i_really_mean_it
    ```

Parameters:
:   - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd get-require-min-compat-client

get the minimum client version we will maintain compatibility with

Example command:
:   ```bash
    ceph osd get-require-min-compat-client
    ```

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd getcrushmap

get CRUSH map

Example command:
:   ```bash
    ceph osd getcrushmap 1
    ```

Parameters:
:   - **epoch**: CephInt range= `0`

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd getmap

get OSD map

Example command:
:   ```bash
    ceph osd getmap 1
    ```

Parameters:
:   - **epoch**: CephInt range= `0`

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd getmaxosd

show largest OSD id

Example command:
:   ```bash
    ceph osd getmaxosd
    ```

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd in

set osd(s) <id> [<id>…] in, can use <any|all> to automatically set
all previously out osds in

Example command:
:   ```bash
    ceph osd in --ids=string
    ```

Parameters:
:   - **ids**: (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd info

print osd’s {id} information (instead of all osds from map)

Example command:
:   ```bash
    ceph osd info osd.0
    ```

Parameters:
:   - **id**: CephOsdName

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd last-stat-seq

get the last pg stats sequence number reported for this osd

Example command:
:   ```bash
    ceph osd last-stat-seq osd.0
    ```

Parameters:
:   - **id**: CephOsdName

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd lost

mark osd as permanently lost. THIS DESTROYS DATA IF NO MORE REPLICAS
EXIST, BE CAREFUL

Example command:
:   ```bash
    ceph osd lost osd.0 --yes_i_really_mean_it
    ```

Parameters:
:   - **id**: CephOsdName
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd ls

show all OSD ids

Example command:
:   ```bash
    ceph osd ls 1
    ```

Parameters:
:   - **epoch**: CephInt range= `0`

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd ls-tree

show OSD ids under bucket <name> in the CRUSH map

Example command:
:   ```bash
    ceph osd ls-tree my_name 1
    ```

Parameters:
:   - **name**: (string)
    - **epoch**: CephInt range= `0`

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd lspools

list pools

Example command:
:   ```bash
    ceph osd lspools
    ```

Ceph Module:
:   osd

Required Permissions:
:   `r`

Command Flags:
:   `deprecated`

## osd map

find pg for <object> in <pool> with [namespace]

Example command:
:   ```bash
    ceph osd map poolname objectname my_nspace
    ```

Parameters:
:   - **pool**: CephPoolname
    - **object**: CephObjectname
    - **nspace**: (string)

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd metadata

fetch metadata for osd {id} (default all)

Example command:
:   ```bash
    ceph osd metadata osd.0
    ```

Parameters:
:   - **id**: CephOsdName

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd new

Create a new OSD. If supplied, the id to be replaced needs to exist
and have been previously destroyed. Reads secrets from JSON file via
-i <file> (see man page).

Example command:
:   ```bash
    ceph osd new uuid osd.0
    ```

Parameters:
:   - **uuid**: CephUUID
    - **id**: CephOsdName

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd numa-status

show NUMA status of OSDs

Example command:
:   ```bash
    ceph osd numa-status
    ```

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd ok-to-stop

check whether osd(s) can be safely stopped without reducing immediate
data availability

Example command:
:   ```bash
    ceph osd ok-to-stop --ids=string --max=1
    ```

Parameters:
:   - **ids**: (can be repeated)
    - **max**: CephInt

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd out

set osd(s) <id> [<id>…] out, or use <any|all> to set all osds out

Example command:
:   ```bash
    ceph osd out --ids=string
    ```

Parameters:
:   - **ids**: (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pause

pause osd

Example command:
:   ```bash
    ceph osd pause
    ```

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd perf

print dump of OSD perf summary stats

Example command:
:   ```bash
    ceph osd perf
    ```

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd pg-temp

set pg_temp mapping <pgid>:[<id> [<id>…]] (developers only)

Example command:
:   ```bash
    ceph osd pg-temp --pgid=0 --id=osd.0
    ```

Parameters:
:   - **pgid**: CephPgid
    - **id**: CephOsdName (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pg-upmap

set pg_upmap mapping <pgid>:[<id> [<id>…]] (developers only)

Example command:
:   ```bash
    ceph osd pg-upmap --pgid=0 --id=osd.0
    ```

Parameters:
:   - **pgid**: CephPgid
    - **id**: CephOsdName (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pg-upmap-items

set pg_upmap_items mapping <pgid>:{<id> to <id>, […]} (developers
only)

Example command:
:   ```bash
    ceph osd pg-upmap-items --pgid=0 --id=osd.0
    ```

Parameters:
:   - **pgid**: CephPgid
    - **id**: CephOsdName (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pg-upmap-primary

set pg primary osd <pgid>:<id> (id (osd) must be part of pgid)

Example command:
:   ```bash
    ceph osd pg-upmap-primary 0 osd.0
    ```

Parameters:
:   - **pgid**: CephPgid
    - **id**: CephOsdName

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool application disable

disables use of an application <app> on pool <poolname>

Example command:
:   ```bash
    ceph osd pool application disable poolname my_app
      --yes_i_really_mean_it
    ```

Parameters:
:   - **pool**: CephPoolname
    - **app**: (string)
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool application enable

enable use of an application <app> [cephfs,rbd,rgw] on pool <poolname>

Example command:
:   ```bash
    ceph osd pool application enable poolname my_app
      --yes_i_really_mean_it
    ```

Parameters:
:   - **pool**: CephPoolname
    - **app**: goodchars= `[A-Za-z0-9-_.]`
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool application get

get value of key <key> of application <app> on pool <poolname>

Example command:
:   ```bash
    ceph osd pool application get poolname my_app my_key
    ```

Parameters:
:   - **pool**: CephPoolname
    - **app**: (string)
    - **key**: (string)

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd pool application rm

removes application <app> metadata key <key> on pool <poolname>

Example command:
:   ```bash
    ceph osd pool application rm poolname my_app my_key
    ```

Parameters:
:   - **pool**: CephPoolname
    - **app**: (string)
    - **key**: (string)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool application set

sets application <app> metadata key <key> to <value> on pool
<poolname>

Example command:
:   ```bash
    ceph osd pool application set --pool=poolname --app=string
      --key=string --value=string
    ```

Parameters:
:   - **pool**: CephPoolname
    - **app**: (string)
    - **key**: goodchars= `[A-Za-z0-9-_.]`
    - **value**: goodchars= `[A-Za-z0-9-_.=]`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool cancel-force-backfill

restore normal recovery priority of specified pool <who>

Example command:
:   ```bash
    ceph osd pool cancel-force-backfill --who=poolname
    ```

Parameters:
:   - **who**: CephPoolname (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool cancel-force-recovery

restore normal recovery priority of specified pool <who>

Example command:
:   ```bash
    ceph osd pool cancel-force-recovery --who=poolname
    ```

Parameters:
:   - **who**: CephPoolname (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool create

create pool

Example command:
:   ```bash
    ceph osd pool create --pool=poolname --pg_num=0 --pgp_num=0
      --pool_type=replicated --erasure_code_profile=string --rule=string
      --expected_num_objects=0 --size=0 --pg_num_min=0 --pg_num_max=0
      --autoscale_mode=on --bulk --target_size_bytes=0
      --target_size_ratio=0.0 --yes_i_really_mean_it
    ```

Parameters:
:   - **pool**: CephPoolname
    - **pg_num**: CephInt range= `0`
    - **pgp_num**: CephInt range= `0`
    - **pool_type**: CephChoices strings=(replicated erasure)
    - **erasure_code_profile**: goodchars= `[A-Za-z0-9-_.]`
    - **rule**: (string)
    - **expected_num_objects**: CephInt range= `0`
    - **size**: CephInt range= `0`
    - **pg_num_min**: CephInt range= `0`
    - **pg_num_max**: CephInt range= `0`
    - **autoscale_mode**: CephChoices strings=(on off warn)
    - **bulk**: CephBool
    - **target_size_bytes**: CephInt range= `0`
    - **target_size_ratio**: CephFloat range= `0.0`
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool deep-scrub

initiate deep-scrub on pool <who>

Example command:
:   ```bash
    ceph osd pool deep-scrub --who=poolname
    ```

Parameters:
:   - **who**: CephPoolname (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool delete

delete pool

Example command:
:   ```bash
    ceph osd pool delete --pool=poolname --pool2=poolname
      --yes_i_really_really_mean_it --yes_i_really_really_mean_it_not_faking
    ```

Parameters:
:   - **pool**: CephPoolname
    - **pool2**: CephPoolname
    - **yes_i_really_really_mean_it**: CephBool
    - **yes_i_really_really_mean_it_not_faking**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## osd pool force-backfill

force backfill of specified pool <who> first

Example command:
:   ```bash
    ceph osd pool force-backfill --who=poolname
    ```

Parameters:
:   - **who**: CephPoolname (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool force-recovery

force recovery of specified pool <who> first

Example command:
:   ```bash
    ceph osd pool force-recovery --who=poolname
    ```

Parameters:
:   - **who**: CephPoolname (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool force-remove-snap

Forces removal of snapshots in the range [lower_snapid_bound,
upper_snapid_bound) on pool <pool> in order to cause OSDs to re-trim
them.

Example command:
:   ```bash
    ceph osd pool force-remove-snap --pool=poolname --lower_snapid_bound=0
      --upper_snapid_bound=0 --dry_run
    ```

Parameters:
:   - **pool**: CephPoolname
    - **lower_snapid_bound**: CephInt range= `0`
    - **upper_snapid_bound**: CephInt range= `0`
    - **dry_run**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool get

get pool parameter <var>

Example command:
:   ```bash
    ceph osd pool get poolname size
    ```

Parameters:
:   - **pool**: CephPoolname
    - **var**: CephChoices strings=(size min_size pg_num pgp_num crush_rule hashpspool nodelete nopgchange nosizechange write_fadvise_dontneed noscrub nodeep-scrub hit_set_type hit_set_period hit_set_count hit_set_fpp use_gmt_hitset target_max_objects target_max_bytes cache_target_dirty_ratio cache_target_dirty_high_ratio cache_target_full_ratio cache_min_flush_age cache_min_evict_age erasure_code_profile min_read_recency_for_promote all min_write_recency_for_promote fast_read hit_set_grade_decay_rate hit_set_search_last_n scrub_min_interval scrub_max_interval deep_scrub_interval recovery_priority recovery_op_priority scrub_priority compression_mode compression_algorithm compression_required_ratio compression_max_blob_size compression_min_blob_size csum_type csum_min_block csum_max_block allow_ec_overwrites fingerprint_algorithm pg_autoscale_mode pg_autoscale_bias pg_num_min pg_num_max target_size_bytes target_size_ratio dedup_tier dedup_chunk_algorithm dedup_cdc_chunk_size eio bulk read_ratio)

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd pool get-quota

obtain object or byte limits for pool

Example command:
:   ```bash
    ceph osd pool get-quota poolname
    ```

Parameters:
:   - **pool**: CephPoolname

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd pool ls

list pools

Example command:
:   ```bash
    ceph osd pool ls detail
    ```

Parameters:
:   - **detail**: CephChoices strings=(detail)

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd pool mksnap

make snapshot <snap> in <pool>

Example command:
:   ```bash
    ceph osd pool mksnap poolname my_snap
    ```

Parameters:
:   - **pool**: CephPoolname
    - **snap**: (string)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool rename

rename <srcpool> to <destpool>

Example command:
:   ```bash
    ceph osd pool rename poolname poolname --yes_i_really_mean_it
    ```

Parameters:
:   - **srcpool**: CephPoolname
    - **destpool**: CephPoolname
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool repair

initiate repair on pool <who>

Example command:
:   ```bash
    ceph osd pool repair --who=poolname
    ```

Parameters:
:   - **who**: CephPoolname (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool rm

remove pool

Example command:
:   ```bash
    ceph osd pool rm --pool=poolname --pool2=poolname
      --yes_i_really_really_mean_it --yes_i_really_really_mean_it_not_faking
    ```

Parameters:
:   - **pool**: CephPoolname
    - **pool2**: CephPoolname
    - **yes_i_really_really_mean_it**: CephBool
    - **yes_i_really_really_mean_it_not_faking**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool rmsnap

remove snapshot <snap> from <pool>

Example command:
:   ```bash
    ceph osd pool rmsnap poolname my_snap
    ```

Parameters:
:   - **pool**: CephPoolname
    - **snap**: (string)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool scrub

initiate scrub on pool <who>

Example command:
:   ```bash
    ceph osd pool scrub --who=poolname
    ```

Parameters:
:   - **who**: CephPoolname (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool set

set pool parameter <var> to <val>

Example command:
:   ```bash
    ceph osd pool set --pool=poolname --var=size --val=string
      --yes_i_really_mean_it
    ```

Parameters:
:   - **pool**: CephPoolname
    - **var**: CephChoices strings=(size min_size pg_num pgp_num pgp_num_actual crush_rule hashpspool nodelete nopgchange nosizechange write_fadvise_dontneed noscrub nodeep-scrub hit_set_type hit_set_period hit_set_count hit_set_fpp use_gmt_hitset target_max_bytes target_max_objects cache_target_dirty_ratio cache_target_dirty_high_ratio cache_target_full_ratio cache_min_flush_age cache_min_evict_age min_read_recency_for_promote min_write_recency_for_promote fast_read hit_set_grade_decay_rate hit_set_search_last_n scrub_min_interval scrub_max_interval deep_scrub_interval recovery_priority recovery_op_priority scrub_priority compression_mode compression_algorithm compression_required_ratio compression_max_blob_size compression_min_blob_size csum_type csum_min_block csum_max_block allow_ec_overwrites fingerprint_algorithm pg_autoscale_mode pg_autoscale_bias pg_num_min pg_num_max target_size_bytes target_size_ratio dedup_tier dedup_chunk_algorithm dedup_cdc_chunk_size eio bulk read_ratio)
    - **val**: (string)
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool set-quota

set object or byte limit on pool

Example command:
:   ```bash
    ceph osd pool set-quota poolname max_objects my_val
    ```

Parameters:
:   - **pool**: CephPoolname
    - **field**: CephChoices strings=(max_objects max_bytes)
    - **val**: (string)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool stats

obtain stats from all pools, or from specified pool

Example command:
:   ```bash
    ceph osd pool stats poolname
    ```

Parameters:
:   - **pool_name**: CephPoolname

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd pool stretch set

make the pool stretched across the specified number of CRUSH buckets

Example command:
:   ```bash
    ceph osd pool stretch set --pool=poolname
      --peering_crush_bucket_count=0 --peering_crush_bucket_target=0
      --peering_crush_bucket_barrier=string --crush_rule=string --size=0
      --min_size=0 --yes_i_really_mean_it
    ```

Parameters:
:   - **pool**: CephPoolname
    - **peering_crush_bucket_count**: CephInt range= `0`
    - **peering_crush_bucket_target**: CephInt range= `0`
    - **peering_crush_bucket_barrier**: (string)
    - **crush_rule**: (string)
    - **size**: CephInt range= `0`
    - **min_size**: CephInt range= `0`
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd pool stretch show

show all the stretch related information for the pool

Example command:
:   ```bash
    ceph osd pool stretch show poolname
    ```

Parameters:
:   - **pool**: CephPoolname

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd pool stretch unset

unset the stretch mode for the pool

Example command:
:   ```bash
    ceph osd pool stretch unset poolname
    ```

Parameters:
:   - **pool**: CephPoolname

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd primary-affinity

adjust osd primary-affinity from 0.0 <= <weight> <= 1.0

Example command:
:   ```bash
    ceph osd primary-affinity osd.0 0.0
    ```

Parameters:
:   - **id**: CephOsdName
    - **weight**: CephFloat range= `0.0..1.0`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd primary-temp

set primary_temp mapping pgid:<id> (developers only)

Example command:
:   ```bash
    ceph osd primary-temp 0 osd.0
    ```

Parameters:
:   - **pgid**: CephPgid
    - **id**: CephOsdName

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd purge

purge all osd data from the monitors including the OSD id and CRUSH
position

Example command:
:   ```bash
    ceph osd purge osd.0 --force --yes_i_really_mean_it
    ```

Parameters:
:   - **id**: CephOsdName
    - **force**: CephBool
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd purge-new

purge all traces of an OSD that was partially created but never
started

Example command:
:   ```bash
    ceph osd purge-new osd.0 --yes_i_really_mean_it
    ```

Parameters:
:   - **id**: CephOsdName
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd repair

initiate repair on osd <who>, or use <all|any> to repair all

Example command:
:   ```bash
    ceph osd repair string
    ```

Parameters:
:   - **who**: (string)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd require-osd-release

set the minimum allowed OSD release to participate in the cluster

Example command:
:   ```bash
    ceph osd require-osd-release octopus --yes_i_really_mean_it
    ```

Parameters:
:   - **release**: CephChoices strings=(octopus pacific quincy reef squid)
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd reweight

reweight osd to 0.0 < <weight> < 1.0

Example command:
:   ```bash
    ceph osd reweight osd.0 0.0
    ```

Parameters:
:   - **id**: CephOsdName
    - **weight**: CephFloat range= `0.0..1.0`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd reweight-by-pg

reweight OSDs by PG distribution [overload-percentage-for-
consideration, default 120]

Example command:
:   ```bash
    ceph osd reweight-by-pg --oload=1 --max_change=0.0 --max_osds=1
      --pools=poolname
    ```

Parameters:
:   - **oload**: CephInt
    - **max_change**: CephFloat
    - **max_osds**: CephInt
    - **pools**: CephPoolname (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd reweight-by-utilization

reweight OSDs by utilization [overload-percentage-for-consideration,
default 120]

Example command:
:   ```bash
    ceph osd reweight-by-utilization --oload=1 --max_change=0.0
      --max_osds=1 --no_increasing
    ```

Parameters:
:   - **oload**: CephInt
    - **max_change**: CephFloat
    - **max_osds**: CephInt
    - **no_increasing**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd reweightn

reweight osds with {<id>: <weight>,…}

Example command:
:   ```bash
    ceph osd reweightn my_weights
    ```

Parameters:
:   - **weights**: (string)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd rm

remove osd(s) <id> [<id>…], or use <any|all> to remove all osds

Example command:
:   ```bash
    ceph osd rm --ids=string
    ```

Parameters:
:   - **ids**: (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## osd rm-nodown

allow osd(s) <id> [<id>…] to be marked down (if they are currently
marked as nodown), can use <all|any> to automatically filter out all
nodown osds

Example command:
:   ```bash
    ceph osd rm-nodown --ids=string
    ```

Parameters:
:   - **ids**: (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## osd rm-noin

allow osd(s) <id> [<id>…] to be marked in (if they are currently
marked as noin), can use <all|any> to automatically filter out all
noin osds

Example command:
:   ```bash
    ceph osd rm-noin --ids=string
    ```

Parameters:
:   - **ids**: (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## osd rm-noout

allow osd(s) <id> [<id>…] to be marked out (if they are currently
marked as noout), can use <all|any> to automatically filter out all
noout osds

Example command:
:   ```bash
    ceph osd rm-noout --ids=string
    ```

Parameters:
:   - **ids**: (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## osd rm-noup

allow osd(s) <id> [<id>…] to be marked up (if they are currently
marked as noup), can use <all|any> to automatically filter out all
noup osds

Example command:
:   ```bash
    ceph osd rm-noup --ids=string
    ```

Parameters:
:   - **ids**: (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## osd rm-pg-upmap

clear pg_upmap mapping for <pgid> (developers only)

Example command:
:   ```bash
    ceph osd rm-pg-upmap 0
    ```

Parameters:
:   - **pgid**: CephPgid

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd rm-pg-upmap-items

clear pg_upmap_items mapping for <pgid> (developers only)

Example command:
:   ```bash
    ceph osd rm-pg-upmap-items 0
    ```

Parameters:
:   - **pgid**: CephPgid

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd rm-pg-upmap-primary

clear pg primary setting for <pgid>

Example command:
:   ```bash
    ceph osd rm-pg-upmap-primary 0
    ```

Parameters:
:   - **pgid**: CephPgid

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd rm-pg-upmap-primary-all

clear all pg primary entries (developers only)

Example command:
:   ```bash
    ceph osd rm-pg-upmap-primary-all
    ```

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd rm-primary-temp

clear primary_temp mapping pgid (developers only)

Example command:
:   ```bash
    ceph osd rm-primary-temp 0
    ```

Parameters:
:   - **pgid**: CephPgid

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd safe-to-destroy

check whether osd(s) can be safely destroyed without reducing data
durability

Example command:
:   ```bash
    ceph osd safe-to-destroy --ids=string
    ```

Parameters:
:   - **ids**: (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd scrub

initiate scrub on osd <who>, or use <all|any> to scrub all

Example command:
:   ```bash
    ceph osd scrub string
    ```

Parameters:
:   - **who**: (string)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd set

set <key>

Example command:
:   ```bash
    ceph osd set full --yes_i_really_mean_it
    ```

Parameters:
:   - **key**: CephChoices strings=(full pause noup nodown noout noin nobackfill norebalance norecover noscrub nodeep-scrub notieragent nosnaptrim pglog_hardlimit noautoscale)
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd set-allow-crimson

Allow crimson-osds to boot and join the cluster. Note, crimson-osd is
not yet considered stable and may crash or cause data loss -- should
be avoided outside of testing and development. This setting is
irrevocable

Example command:
:   ```bash
    ceph osd set-allow-crimson --yes_i_really_mean_it
    ```

Parameters:
:   - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd set-backfillfull-ratio

set usage ratio at which OSDs are marked too full to backfill

Example command:
:   ```bash
    ceph osd set-backfillfull-ratio 0.0
    ```

Parameters:
:   - **ratio**: CephFloat range= `0.0..1.0`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd set-full-ratio

set usage ratio at which OSDs are marked full

Example command:
:   ```bash
    ceph osd set-full-ratio 0.0
    ```

Parameters:
:   - **ratio**: CephFloat range= `0.0..1.0`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd set-group

set <flags> for batch osds or crush nodes, <flags> must be a comma-
separated subset of {noup,nodown,noin,noout}

Example command:
:   ```bash
    ceph osd set-group --flags=string --who=string
    ```

Parameters:
:   - **flags**: (string)
    - **who**: (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd set-nearfull-ratio

set usage ratio at which OSDs are marked near-full

Example command:
:   ```bash
    ceph osd set-nearfull-ratio 0.0
    ```

Parameters:
:   - **ratio**: CephFloat range= `0.0..1.0`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd set-require-min-compat-client

set the minimum client version we will maintain compatibility with

Example command:
:   ```bash
    ceph osd set-require-min-compat-client my_version
      --yes_i_really_mean_it
    ```

Parameters:
:   - **version**: (string)
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd setcrushmap

set crush map from input file

Example command:
:   ```bash
    ceph osd setcrushmap 1
    ```

Parameters:
:   - **prior_version**: CephInt

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd setmaxosd

set new maximum osd value

Example command:
:   ```bash
    ceph osd setmaxosd 1
    ```

Parameters:
:   - **newmax**: CephInt range= `0`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd stat

print summary of OSD map

Example command:
:   ```bash
    ceph osd stat
    ```

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd stop

stop the corresponding osd daemons and mark them as down

Example command:
:   ```bash
    ceph osd stop --ids=string
    ```

Parameters:
:   - **ids**: (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd test-reweight-by-pg

dry run of reweight OSDs by PG distribution [overload-percentage-for-
consideration, default 120]

Example command:
:   ```bash
    ceph osd test-reweight-by-pg --oload=1 --max_change=0.0 --max_osds=1
      --pools=poolname
    ```

Parameters:
:   - **oload**: CephInt
    - **max_change**: CephFloat
    - **max_osds**: CephInt
    - **pools**: CephPoolname (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd test-reweight-by-utilization

dry run of reweight OSDs by utilization [overload-percentage-for-
consideration, default 120]

Example command:
:   ```bash
    ceph osd test-reweight-by-utilization --oload=1 --max_change=0.0
      --max_osds=1 --no_increasing
    ```

Parameters:
:   - **oload**: CephInt
    - **max_change**: CephFloat
    - **max_osds**: CephInt
    - **no_increasing**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd tier add

add the tier <tierpool> (the second one) to base pool <pool> (the
first one)

Example command:
:   ```bash
    ceph osd tier add poolname poolname --force_nonempty
    ```

Parameters:
:   - **pool**: CephPoolname
    - **tierpool**: CephPoolname
    - **force_nonempty**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd tier add-cache

add a cache <tierpool> (the second one) of size <size> to existing
pool <pool> (the first one)

Example command:
:   ```bash
    ceph osd tier add-cache poolname poolname 1
    ```

Parameters:
:   - **pool**: CephPoolname
    - **tierpool**: CephPoolname
    - **size**: CephInt range= `0`

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd tier cache-mode

specify the caching mode for cache tier <pool>

Example command:
:   ```bash
    ceph osd tier cache-mode poolname writeback --yes_i_really_mean_it
    ```

Parameters:
:   - **pool**: CephPoolname
    - **mode**: CephChoices strings=(writeback proxy readproxy readonly none)
    - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd tier remove

remove the tier <tierpool> (the second one) from base pool <pool> (the
first one)

Example command:
:   ```bash
    ceph osd tier remove poolname poolname
    ```

Parameters:
:   - **pool**: CephPoolname
    - **tierpool**: CephPoolname

Ceph Module:
:   osd

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## osd tier remove-overlay

remove the overlay pool for base pool <pool>

Example command:
:   ```bash
    ceph osd tier remove-overlay poolname
    ```

Parameters:
:   - **pool**: CephPoolname

Ceph Module:
:   osd

Required Permissions:
:   `rw`

Command Flags:
:   `deprecated`

## osd tier rm

remove the tier <tierpool> (the second one) from base pool <pool> (the
first one)

Example command:
:   ```bash
    ceph osd tier rm poolname poolname
    ```

Parameters:
:   - **pool**: CephPoolname
    - **tierpool**: CephPoolname

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd tier rm-overlay

remove the overlay pool for base pool <pool>

Example command:
:   ```bash
    ceph osd tier rm-overlay poolname
    ```

Parameters:
:   - **pool**: CephPoolname

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd tier set-overlay

set the overlay pool for base pool <pool> to be <overlaypool>

Example command:
:   ```bash
    ceph osd tier set-overlay poolname poolname
    ```

Parameters:
:   - **pool**: CephPoolname
    - **overlaypool**: CephPoolname

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd tree

print OSD tree

Example command:
:   ```bash
    ceph osd tree --epoch=0 --states=up
    ```

Parameters:
:   - **epoch**: CephInt range= `0`
    - **states**: CephChoices strings=(up down in out destroyed) (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd tree-from

print OSD tree in bucket

Example command:
:   ```bash
    ceph osd tree-from --bucket=string --epoch=0 --states=up
    ```

Parameters:
:   - **bucket**: (string)
    - **epoch**: CephInt range= `0`
    - **states**: CephChoices strings=(up down in out destroyed) (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd unpause

unpause osd

Example command:
:   ```bash
    ceph osd unpause
    ```

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd unset

unset <key>

Example command:
:   ```bash
    ceph osd unset full
    ```

Parameters:
:   - **key**: CephChoices strings=(full pause noup nodown noout noin nobackfill norebalance norecover noscrub nodeep-scrub notieragent nosnaptrim noautoscale)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd unset-group

unset <flags> for batch osds or crush nodes, <flags> must be a comma-
separated subset of {noup,nodown,noin,noout}

Example command:
:   ```bash
    ceph osd unset-group --flags=string --who=string
    ```

Parameters:
:   - **flags**: (string)
    - **who**: (can be repeated)

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## osd utilization

get basic pg distribution stats

Example command:
:   ```bash
    ceph osd utilization
    ```

Ceph Module:
:   osd

Required Permissions:
:   `r`

## osd versions

check running versions of OSDs

Example command:
:   ```bash
    ceph osd versions
    ```

Ceph Module:
:   osd

Required Permissions:
:   `r`

# pg

## pg cancel-force-backfill

restore normal backfill priority of <pgid>

Example command:
:   ```bash
    ceph pg cancel-force-backfill --pgid=0
    ```

Parameters:
:   - **pgid**: CephPgid (can be repeated)

Ceph Module:
:   pg

Required Permissions:
:   `rw`

## pg cancel-force-recovery

restore normal recovery priority of <pgid>

Example command:
:   ```bash
    ceph pg cancel-force-recovery --pgid=0
    ```

Parameters:
:   - **pgid**: CephPgid (can be repeated)

Ceph Module:
:   pg

Required Permissions:
:   `rw`

## pg debug

show debug info about pgs

Example command:
:   ```bash
    ceph pg debug unfound_objects_exist
    ```

Parameters:
:   - **debugop**: CephChoices strings=(unfound_objects_exist degraded_pgs_exist)

Ceph Module:
:   pg

Required Permissions:
:   `r`

## pg deep-scrub

start deep-scrub on <pgid>

Example command:
:   ```bash
    ceph pg deep-scrub 0
    ```

Parameters:
:   - **pgid**: CephPgid

Ceph Module:
:   pg

Required Permissions:
:   `rw`

## pg dump

show human-readable versions of pg map (only ‘all’ valid with plain)

Example command:
:   ```bash
    ceph pg dump --dumpcontents=all
    ```

Parameters:
:   - **dumpcontents**: CephChoices strings=(all summary sum delta pools osds pgs pgs_brief) (can be repeated)

Ceph Module:
:   pg

Required Permissions:
:   `r`

## pg dump_json

show human-readable version of pg map in json only

Example command:
:   ```bash
    ceph pg dump_json --dumpcontents=all
    ```

Parameters:
:   - **dumpcontents**: CephChoices strings=(all summary sum pools osds pgs) (can be repeated)

Ceph Module:
:   pg

Required Permissions:
:   `r`

## pg dump_pools_json

show pg pools info in json only

Example command:
:   ```bash
    ceph pg dump_pools_json
    ```

Ceph Module:
:   pg

Required Permissions:
:   `r`

## pg dump_stuck

show information about stuck pgs

Example command:
:   ```bash
    ceph pg dump_stuck --stuckops=inactive --threshold=1
    ```

Parameters:
:   - **stuckops**: CephChoices strings=(inactive unclean stale undersized degraded) (can be repeated)
    - **threshold**: CephInt

Ceph Module:
:   pg

Required Permissions:
:   `r`

## pg force-backfill

force backfill of <pgid> first

Example command:
:   ```bash
    ceph pg force-backfill --pgid=0
    ```

Parameters:
:   - **pgid**: CephPgid (can be repeated)

Ceph Module:
:   pg

Required Permissions:
:   `rw`

## pg force-recovery

force recovery of <pgid> first

Example command:
:   ```bash
    ceph pg force-recovery --pgid=0
    ```

Parameters:
:   - **pgid**: CephPgid (can be repeated)

Ceph Module:
:   pg

Required Permissions:
:   `rw`

## pg getmap

get binary pg map to -o/stdout

Example command:
:   ```bash
    ceph pg getmap
    ```

Ceph Module:
:   pg

Required Permissions:
:   `r`

## pg ls

list pg with specific pool, osd, state

Example command:
:   ```bash
    ceph pg ls --pool=1 --states=string
    ```

Parameters:
:   - **pool**: CephInt
    - **states**: (can be repeated)

Ceph Module:
:   pg

Required Permissions:
:   `r`

## pg ls-by-osd

list pg on osd [osd]

Example command:
:   ```bash
    ceph pg ls-by-osd --osd=osd.0 --pool=1 --states=string
    ```

Parameters:
:   - **osd**: CephOsdName
    - **pool**: CephInt
    - **states**: (can be repeated)

Ceph Module:
:   pg

Required Permissions:
:   `r`

## pg ls-by-pool

list pg with pool = [poolname]

Example command:
:   ```bash
    ceph pg ls-by-pool --poolstr=string --states=string
    ```

Parameters:
:   - **poolstr**: (string)
    - **states**: (can be repeated)

Ceph Module:
:   pg

Required Permissions:
:   `r`

## pg ls-by-primary

list pg with primary = [osd]

Example command:
:   ```bash
    ceph pg ls-by-primary --osd=osd.0 --pool=1 --states=string
    ```

Parameters:
:   - **osd**: CephOsdName
    - **pool**: CephInt
    - **states**: (can be repeated)

Ceph Module:
:   pg

Required Permissions:
:   `r`

## pg map

show mapping of pg to osds

Example command:
:   ```bash
    ceph pg map 0
    ```

Parameters:
:   - **pgid**: CephPgid

Ceph Module:
:   pg

Required Permissions:
:   `r`

## pg repair

start repair on <pgid>

Example command:
:   ```bash
    ceph pg repair 0
    ```

Parameters:
:   - **pgid**: CephPgid

Ceph Module:
:   pg

Required Permissions:
:   `rw`

## pg repeer

force a PG to repeer

Example command:
:   ```bash
    ceph pg repeer 0
    ```

Parameters:
:   - **pgid**: CephPgid

Ceph Module:
:   osd

Required Permissions:
:   `rw`

## pg scrub

start scrub on <pgid>

Example command:
:   ```bash
    ceph pg scrub 0
    ```

Parameters:
:   - **pgid**: CephPgid

Ceph Module:
:   pg

Required Permissions:
:   `rw`

## pg stat

show placement group status.

Example command:
:   ```bash
    ceph pg stat
    ```

Ceph Module:
:   pg

Required Permissions:
:   `r`

# quorum

## quorum enter

force monitor back into quorum

Example command:
:   ```bash
    ceph quorum enter
    ```

Ceph Module:
:   mon

Required Permissions:
:   `rw`

## quorum exit

force monitor out of the quorum

Example command:
:   ```bash
    ceph quorum exit
    ```

Ceph Module:
:   mon

Required Permissions:
:   `rw`

# quorum_status

report status of monitor quorum

Example command:
:   ```bash
    ceph quorum_status
    ```

Ceph Module:
:   mon

Required Permissions:
:   `r`

# report

report full status of cluster, optional title tag strings

Example command:
:   ```bash
    ceph report --tags=string
    ```

Parameters:
:   - **tags**: (can be repeated)

Ceph Module:
:   mon

Required Permissions:
:   `r`

# service

## service dump

dump service map

Example command:
:   ```bash
    ceph service dump
    ```

Ceph Module:
:   service

Required Permissions:
:   `r`

## service status

dump service state

Example command:
:   ```bash
    ceph service status
    ```

Ceph Module:
:   service

Required Permissions:
:   `r`

# sessions

list existing sessions

Example command:
:   ```bash
    ceph sessions
    ```

Ceph Module:
:   mon

Required Permissions:
:   `r`

# smart

Query health metrics for underlying device

Example command:
:   ```bash
    ceph smart my_devid
    ```

Parameters:
:   - **devid**: (string)

Ceph Module:
:   mon

Required Permissions:
:   `rw`

# status

show cluster status

Example command:
:   ```bash
    ceph status
    ```

Ceph Module:
:   mon

Required Permissions:
:   `r`

# sync_force

force sync of and clear monitor store

Example command:
:   ```bash
    ceph sync_force --yes_i_really_mean_it
    ```

Parameters:
:   - **yes_i_really_mean_it**: CephBool

Ceph Module:
:   mon

Required Permissions:
:   `rw`

# tell

send a command to a specific daemon

Example command:
:   ```bash
    ceph tell --target=name --args=string
    ```

Parameters:
:   - **target**: CephName
    - **args**: (can be repeated)

Ceph Module:
:   mon

Required Permissions:
:   `rw`

# time-sync-status

show time sync status

Example command:
:   ```bash
    ceph time-sync-status
    ```

Ceph Module:
:   mon

Required Permissions:
:   `r`

# version

show mon daemon version

Example command:
:   ```bash
    ceph version
    ```

Ceph Module:
:   mon

Required Permissions:
:   `r`

# versions

check running versions of ceph daemons

Example command:
:   ```bash
    ceph versions
    ```

Ceph Module:
:   mon

Required Permissions:
:   `r`

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
