---
collection: netbox
version: "4.2.9"
title: "Redis Installation"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/installation/2-redis.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Redis Installation

## Install Redis

[Redis](https://redis.io/) is an in-memory key-value store which NetBox employs for caching and queuing. This section entails the installation and configuration of a local Redis instance. If you already have a Redis service in place, skip to [the next section](3-netbox.md).

=== "Ubuntu"

    ```no-highlight
    sudo apt install -y redis-server
    ```

=== "CentOS"

    ```no-highlight
    sudo yum install -y redis
    sudo systemctl enable --now redis
    ```

Before continuing, verify that your installed version of Redis is at least v4.0:

```no-highlight
redis-server -v
```

You may wish to modify the Redis configuration at `/etc/redis.conf` or `/etc/redis/redis.conf`, however in most cases the default configuration is sufficient.

## Verify Service Status

Use the `redis-cli` utility to ensure the Redis service is functional:

```no-highlight
redis-cli ping
```

If successful, you should receive a `PONG` response from the server.
