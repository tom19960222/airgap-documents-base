---
collection: ceph
version: "19.2.2"
title: "Ruby Swift Examples"
source_url: https://docs.ceph.com/en/squid/radosgw/swift/ruby/
fetched_at: 2026-07-27T16:42:52+00:00
---
# Ruby Swift Examples

## Create a Connection

This creates a connection so that you can interact with the server:

```ruby
require 'cloudfiles'
username = 'account_name:user_name'
api_key  = 'your_secret_key'

conn = CloudFiles::Connection.new(
        :username => username,
        :api_key  => api_key,
        :auth_url => 'http://objects.dreamhost.com/auth'
)
```

## Create a Container

This creates a new container called `my-new-container`

```ruby
container = conn.create_container('my-new-container')
```

## Create an Object

This creates a file `hello.txt` from the file named `my_hello.txt`

```ruby
obj = container.create_object('hello.txt')
obj.load_from_filename('./my_hello.txt')
obj.content_type = 'text/plain'
```

## List Owned Containers

This gets a list of Containers that you own, and also prints out
the container name:

```ruby
conn.containers.each do |container|
        puts container
end
```

The output will look something like this:

```
mahbuckat1
mahbuckat2
mahbuckat3
```

## List a Container’s Contents

This gets a list of objects in the container, and prints out each
object’s name, the file size, and last modified date:

```ruby
require 'date'  # not necessary in the next version

container.objects_detail.each do |name, data|
        puts "#{name}\t#{data[:bytes]}\t#{data[:last_modified]}"
end
```

The output will look something like this:

```
myphoto1.jpg 251262  2011-08-08T21:35:48.000Z
myphoto2.jpg 262518  2011-08-08T21:38:01.000Z
```

## Retrieve an Object

This downloads the object `hello.txt` and saves it in
`./my_hello.txt`:

```ruby
obj = container.object('hello.txt')
obj.save_to_filename('./my_hello.txt')
```

## Delete an Object

This deletes the object `goodbye.txt`:

```ruby
container.delete_object('goodbye.txt')
```

## Delete a Container

> **Note:**
>
> The container must be empty! Otherwise the request won’t work!

```ruby
container.delete_container('my-new-container')
```

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
