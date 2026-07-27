---
collection: ceph
version: "19.2.2"
title: "ceph-mgr module developer’s guide"
source_url: https://docs.ceph.com/en/squid/mgr/modules/
fetched_at: 2026-07-27T16:40:48+00:00
---
# ceph-mgr module developer’s guide

> **Warning:**
>
> This is developer documentation, describing Ceph internals that
> are relevant only to people writing ceph-mgr modules.

## Creating a module

In `pybind/mgr/`, create a python module. Within your module, create a class
that inherits from `MgrModule`. For ceph-mgr to detect your module, your
directory must contain a file named `module.py`.

The most important methods to override are:

- a `serve` member function for server-type modules. This
  function should block forever.
- a `notify` member function if your module needs to
  take action when new cluster data is available.
- a `handle_command` member function if your module
  exposes CLI commands. But this approach for exposing commands
  is deprecated. For more details, see [Exposing commands](index.md#mgr-module-exposing-commands).

Some modules interface with external orchestrators to deploy
Ceph services. These also inherit from `Orchestrator`, which adds
additional methods to the base `MgrModule` class. See
[Orchestrator modules](../orchestrator_modules/index.md#orchestrator-modules) for more on
creating these modules.

## Installing a module

Once your module is present in the location set by the `mgr module path`
configuration setting, you can enable it via the `ceph mgr module enable`
command:

```
ceph mgr module enable mymodule
```

Note that the MgrModule interface is not stable, so any modules maintained
outside of the Ceph tree are liable to break when run against any newer
or older versions of Ceph.

## Logging

Logging in Ceph manager modules is done as in any other Python program. Just
import the `logging` package and get a logger instance with the
`logging.getLogger` function.

Each module has a `log_level` option that specifies the current Python
logging level of the module.

To change or query the logging level of the module use the following Ceph
commands:

```
ceph config get mgr mgr/<module_name>/log_level
ceph config set mgr mgr/<module_name>/log_level <info|debug|critical|error|warning|>
```

The logging level used upon the module’s start is determined by the current
logging level of the mgr daemon, unless if the `log_level` option was
previously set with the `config set ...` command. The mgr daemon logging
level is mapped to the module python logging level as follows:

- <= 0 is CRITICAL
- <= 1 is WARNING
- <= 4 is INFO
- <= +inf is DEBUG

We can unset the module log level and fallback to the mgr daemon logging level
by running the following command:

```
ceph config set mgr mgr/<module_name>/log_level ''
```

By default, modules’ logging messages are processed by the Ceph logging layer
where they will be recorded in the mgr daemon’s log file. But it’s also
possible to send a module’s logging message to its own file.

The module’s log file is located in the same directory as the Manager daemon’s
log file with the following name pattern:

```
<mgr_daemon_log_file_name>.<module_name>.log
```

To enable the file logging on a module, use the following command:

```
ceph config set mgr mgr/<module_name>/log_to_file true
```

When the module’s file logging is enabled, the module’s logging messages stop
being written to the Manager daemon’s log file and are written only to the
module’s log file.

It’s also possible to check the status and disable the file logging with the
following commands:

```
ceph config get mgr mgr/<module_name>/log_to_file
ceph config set mgr mgr/<module_name>/log_to_file false
```

## Exposing commands

There are two approaches for exposing a command. The first method involves
using the `@CLICommand` decorator to decorate the methods needed to handle a
command. The second method uses a `COMMANDS` attribute defined for the
module class.

### The CLICommand approach

```python
@CLICommand('antigravity send to blackhole',
            perm='rw')
def send_to_blackhole(self, oid: str, blackhole: Optional[str] = None, inbuf: Optional[str] = None):
    '''
    Send the specified object to black hole
    '''
    obj = self.find_object(oid)
    if obj is None:
        return HandleCommandResult(-errno.ENOENT, stderr=f"object '{oid}' not found")
    if blackhole is not None and inbuf is not None:
        try:
            location = self.decrypt(blackhole, passphrase=inbuf)
        except ValueError:
            return HandleCommandResult(-errno.EINVAL, stderr='unable to decrypt location')
    else:
        location = blackhole
    self.send_object_to(obj, location)
    return HandleCommandResult(stdout=f"the black hole swallowed '{oid}'")
```

The first parameter passed to `CLICommand` is the “name” of the command.
Since there are lots of commands in Ceph, we tend to group related commands
with a common prefix. In this case, “antigravity” is used for this purpose.
As the author is probably designing a module which is also able to launch
rockets into the deep space.

The [type annotations](https://www.python.org/dev/peps/pep-0484/) for the
method parameters are mandatory here, so the usage of the command can be
properly reported to the `ceph` CLI, and the manager daemon can convert
the serialized command parameters sent by the clients to the expected type
before passing them to the handler method. With properly implemented types,
one can also perform some sanity checks against the parameters!

The names of the parameters are part of the command interface, so please
try to take the backward compatibility into consideration when changing
them. But you **cannot** change name of `inbuf` parameter, it is used
to pass the content of the file specified by `ceph --in-file` option.

The docstring of the method is used for the description of the command.

The manager daemon cooks the usage of the command from these ingredients,
like:

```
antigravity send to blackhole <oid> [<blackhole>]  Send the specified object to black hole
```

as part of the output of `ceph --help`.

In addition to `@CLICommand`, you could also use `@CLIReadCommand` or
`@CLIWriteCommand` if your command only requires read permissions or
write permissions respectively.

### The COMMANDS Approach

This method uses the `COMMANDS` class attribute of your module to define
a list of dicts like this:

```
COMMANDS = [
    {
        "cmd": "foobar name=myarg,type=CephString",
        "desc": "Do something awesome",
        "perm": "rw",
        # optional:
        "poll": "true"
    }
]
```

The `cmd` part of each entry is parsed in the same way as internal
Ceph mon and admin socket commands (see mon/MonCommands.h in
the Ceph source for examples). Note that the “poll” field is optional,
and is set to False by default; this indicates to the `ceph` CLI
that it should call this command repeatedly and output results (see
`ceph -h` and its `--period` option).

Each command is expected to return a tuple `(retval, stdout, stderr)`.
`retval` is an integer representing a libc error code (e.g. EINVAL,
EPERM, or 0 for no error), `stdout` is a string containing any
non-error output, and `stderr` is a string containing any progress or
error explanation output. Either or both of the two strings may be empty.

Implement the `handle_command` function to respond to the commands
when they are sent:

MgrModule.handle_command(*inbuf*, *cmd*)
:   Called by ceph-mgr to request the plugin to handle one
    of the commands that it declared in self.COMMANDS

    Return a status code, an output buffer, and an
    output string. The output buffer is for data results,
    the output string is for informative text.

    Parameters:
    :   - **inbuf** (*str*) -- content of any “-i <file>” supplied to ceph cli
        - **cmd** (*dict*) -- from Ceph’s cmdmap_t

    Return type:
    :   `Union`[`HandleCommandResult`, `Tuple`[`int`, `str`, `str`]]

    Returns:
    :   HandleCommandResult or a 3-tuple of (int, str, str)

### Responses and Formatting

Functions that handle manager commands are expected to return a three element
tuple with the type signature `Tuple[int, str, str]`. The first element is a
return value/error code, where zero indicates no error and a negative [errno](https://man7.org/linux/man-pages/man3/errno.3.html)
is typically used for error conditions. The second element corresponds to the
command’s “output”. The third element corresponds to the command’s “error
output” (akin to stderr) and is frequently used to report textual error details
when the return code is non-zero. The `mgr_module.HandleCommandResult` type
can also be used in lieu of a response tuple.

When the implementation of a command raises an exception one of two possible
approaches to handling the exception exist. First, the command function can do
nothing and let the exception bubble up to the manager. When this happens the
manager will automatically set a return code to -EINVAL and record a trace-back
in the error output. This trace-back can be very long in some cases. The second
approach is to handle an exception within a try-except block and convert the
exception to an error code that better fits the exception (converting a
KeyError to -ENOENT, for example). In this case the error output may also be
set to something more specific and actionable by the one calling the command.

In many cases, especially in more recent versions of Ceph, manager commands are
designed to return structured output to the caller. Structured output includes
machine-parsable data such as JSON, YAML, XML, etc. JSON is the most common
structured output format returned by manager commands. As of Ceph Reef, there
are a number of new decorators available from the `object_format` module that
help manage formatting output and handling exceptions automatically. The
intent is that most of the implementation of a manager command can be written in
an idiomatic (aka “Pythonic”) style and the decorators will take care of most of
the work needed to format the output and return manager response tuples.

In most cases, net new code should use the `Responder` decorator. Example:

```python
@CLICommand('antigravity list wormholes', perm='r')
@Responder()
def list_wormholes(self, oid: str, details: bool = False) -> List[Dict[str, Any]]:
    '''List wormholes associated with the supplied oid.
    '''
    with self.open_wormhole_db() as db:
        wormholes = db.query(oid=oid)
    if not details:
        return [{'name': wh.name} for wh in wormholes]
    return [{'name': wh.name, 'age': wh.get_age(), 'destination': wh.dest}
            for wh in wormholes]
```

#### Formatting

The `Responder` decorator automatically takes care of converting Python
objects into a response tuple with formatted output. By default, this decorator
can automatically return JSON and YAML. When invoked from the command line the
`--format` flag can be used to select the response format. If left
unspecified, JSON will be returned. The automatic formatting can be applied to
any basic Python type: lists, dicts, str, int, etc. Other objects can be
formatted automatically if they meet the `SimpleDataProvider` protocol - they
provide a `to_simplified` method. The `to_simplified` function must return
a simplified representation of the object made out of basic types.

```python
class MyCleverObject:
    def to_simplified(self) -> Dict[str, int]:
        # returns a python object(s) made up from basic types
        return {"gravitons": 999, "tachyons": 404}

@CLICommand('antigravity list wormholes', perm='r')
@Responder()
def list_wormholes(self, oid: str, details: bool = False) -> MyCleverObject:
    '''List wormholes associated with the supplied oid.
    '''
    ...
```

The behavior of the automatic output formatting can be customized and extednted
to other types of formatting (XML, Plain Text, etc). As this is a complex
topic, please refer to the module documentation for the `object_format`
module.

#### Error Handling

Additionally, the `Responder` decorator can automatically handle converting
some exceptions into response tuples. Any raised exception inheriting from
`ErrorResponseBase` will be automatically converted into a response tuple.
The common approach will be to use `ErrorResponse`, an exception type that
can be used directly and has arguments for the error output and return value or
it can be constructed from an existing exception using the `wrap`
classmethod. The wrap classmethod will automatically use the exception text and
if available the `errno` property of other exceptions.

Converting our previous example to use this exception handling approach:

```python
@CLICommand('antigravity list wormholes', perm='r')
@Responder()
def list_wormholes(self, oid: str, details: bool = False) -> List[Dict[str, Any]]:
    '''List wormholes associated with the supplied oid.
    '''
    try:
        with self.open_wormhole_db() as db:
            wormholes = db.query(oid=oid)
    except UnknownOIDError:
         raise ErrorResponse(f"Unknown oid: {oid}", return_value=-errno.ENOENT)
    except WormholeDBError as err:
        raise ErrorResponse.wrap(err)
    if not details:
        return [{'name': wh.name} for wh in wormholes]
    return [{'name': wh.name, 'age': wh.get_age(), 'destination': wh.dest}
            for wh in wormholes]
```

> **Note:**
>
> Because the decorator can not determine the difference between a
> programming mistake and an expected error condition it does not try to
> catch all exceptions.

#### Additional Decorators

The `object_format` module provides additional decorators to complement
`Responder` but for cases where `Responder` is insufficient or too “heavy
weight”.

The `ErrorResponseHandler` decorator exists for cases where you *must* still
return a manager response tuple but want to handle errors as exceptions (as in
typical Python code). In short, it works like `Responder` but only with
regards to exceptions. Just like `Responder` it handles exceptions that
inherit from `ErrorResponseBase`. This can be useful in cases where you need
to return raw data in the output. Example:

```python
@CLICommand('antigravity dump config', perm='r')
@ErrorResponseHandler()
def dump_config(self, oid: str) -> Tuple[int, str, str]:
    '''Dump configuration
    '''
    # we have no control over what data is inside the blob!
    try:
         blob = self.fetch_raw_config_blob(oid)
         return 0, blob, ''
    except KeyError:
         raise ErrorResponse("Blob does not exist", return_value=-errno.ENOENT)
```

The `EmptyResponder` decorator exists for cases where, on a success
condition, no output should be generated at all. If you used `Responder` and
default JSON formatting you may always see outputs like `{}` or `[]` if the
command completes without error. Instead, `EmptyResponder` helps you create
manager commands that obey the [Rule of Silence](http://www.linfo.org/rule_of_silence.html) when the command has no
interesting output to emit on success. The functions that `EmptyResponder`
decorate should always return `None`. Like both `Responder` and
`ErrorResponseHandler` exceptions that inhert from `ErrorResponseBase` will
be automatically processed. Example:

```python
@CLICommand('antigravity create wormhole', perm='rw')
@EmptyResponder()
def create_wormhole(self, oid: str, name: str) -> None:
    '''Create a new wormhole.
    '''
    try:
        with self.open_wormhole_db() as db:
            wh = Wormhole(name)
            db.insert(oid=oid, wormhole=wh)
    except UnknownOIDError:
        raise ErrorResponse(f"Unknown oid: {oid}", return_value=-errno.ENOENT)
    except InvalidWormholeError as err:
        raise ErrorResponse.wrap(err)
    except WormholeDBError as err:
        raise ErrorResponse.wrap(err)
```

## Configuration options

Modules can load and store configuration options using the
`set_module_option` and `get_module_option` methods.

> **Note:**
>
> Use `set_module_option` and `get_module_option` to
> manage user-visible configuration options that are not blobs (like
> certificates). If you want to persist module-internal data or
> binary configuration data consider using the [KV store](index.md#kv-store).

Configuration options must be declared in the `MODULE_OPTIONS` class attribute:

```python
MODULE_OPTIONS = [
    Option(name="check_interval",
           level=OptionLevel.ADVANCED,
           default=60,
           type="secs",
           desc="The interval in seconds to check the inbox",
           long_desc="The interval in seconds to check the inbox. Set to 0 to disable the check",
           min=0,
           runtime=True)
]
```

The example above demonstrates most supported properties, though typically only
a subset is needed. The following properties are supported:

**name**
:   The option’s name. This is the only required property.

**type** (optional, default: `str`)
:   The option’s data type. Supported types:

    - `uint` - unsigned 64-bit integer
    - `int` - signed 64-bit integer
    - `str` - string
    - `float` - double-precision floating point
    - `bool` - boolean
    - `addr` - Ceph messenger address for peer communication
    - `addrvec` - comma-separated list of Ceph messenger addresses
    - `uuid` - UUID as defined by [RFC 4122](https://www.ietf.org/rfc/rfc4122.txt)
    - `size` - size value (stored as uint64_t)
    - `secs` - timespan in format `"<number><unit>..."`, e.g., `"3h 2m 1s"` or `"3weeks"`

      Supported units: `s`, `sec`, `second(s)`, `m`, `min`, `minute(s)`,
      `h`, `hr`, `hour(s)`, `d`, `day(s)`, `w`, `wk`, `week(s)`,
      `mo`, `month(s)`, `y`, `yr`, `year(s)`
    - `millisecs` - timespan in milliseconds

**desc**
:   Short description (can be a sentence fragment).

**long_desc**
:   Detailed description using complete sentences or paragraphs.

**default**
:   Default value for the option.

**min** / **max**
:   Minimum and maximum allowed values.

**enum_allowed**
:   For `str` type options, a list of allowed string values. Values outside this set are rejected.

**see_also**
:   List of related option names (used in documentation only).

**tags**
:   List of tags for categorizing the option (used in documentation only).

**runtime** (default: `False`)
:   Whether the option can be updated after module loading.

If you try to use `set_module_option` or `get_module_option` on options
not declared in `MODULE_OPTIONS`, an exception will be raised.

You may choose to provide setter commands in your module to perform
high-level validation. Users can also modify configuration using
the normal `ceph config set` command, where the configuration options
for a Manager module have names of the form `mgr/<module name>/<option>`.

If a configuration option is different, depending on which node the Manager
is running on, then use *localized* configuration (
`get_localized_module_option`, `set_localized_module_option`).
This may be necessary for options such as what address to listen on.
Localized options may also be set externally with `ceph config set`,
where they key name is like `mgr/<module name>/<mgr id>/<option>`

If you need to load and store data (e.g. something larger, binary, or
multiline), use the KV store instead of configuration options (see next
section).

Hints for using config options:

- Reads are fast: ceph-mgr keeps a local in-memory copy, so in many cases you
  can just do a `get_module_option` every time you use a option, rather than
  copying it out into a variable.
- Writes block until the value is persisted (i.e. round trip to the monitor),
  but reads from another thread will see the new value immediately.
- If a user has used `config set` from the command line, then the new
  value will become visible to `get_module_option` immediately, although the
  mon->mgr update is asynchronous, so `config set` will return a fraction
  of a second before the new value is visible on the mgr.
- To delete a config value (i.e. revert to default), just pass `None` to
  set_module_option.

MgrModule.get_module_option(*key*, *default=None*)
:   Retrieve the value of a persistent configuration setting

    Return type:
    :   `Union`[`bool`, `int`, `float`, `str`, `None`]

MgrModule.set_module_option(*key*, *val*)
:   Set the value of a persistent configuration setting

    Parameters:
    :   **key** (*str*) --

    Raises:
    :   **ValueError** -- if val cannot be parsed or it is out of the specified range

    Return type:
    :   `None`

MgrModule.get_localized_module_option(*key*, *default=None*)
:   Retrieve localized configuration for this ceph-mgr instance

    Return type:
    :   `Union`[`bool`, `int`, `float`, `str`, `None`]

MgrModule.set_localized_module_option(*key*, *val*)
:   Set localized configuration for this ceph-mgr instance.

    Parameters:
    :   - **key** (*str*) --
        - **val** (*str*) --

    Return type:
    :   `None`

    Returns:
    :   str

## KV store

Modules have access to a private (per-module) key value store, which
is implemented using the monitor’s “config-key” commands. Use
the `set_store` and `get_store` methods to access the KV store from
your module.

The KV store commands work in a similar way to the configuration
commands. Reads are fast, operating from a local cache. Writes block
on persistence and do a round trip to the monitor.

This data can be access from outside of ceph-mgr using the
`ceph config-key [get|set]` commands. Key names follow the same
conventions as configuration options. Note that any values updated
from outside of ceph-mgr will not be seen by running modules until
the next restart. Users should be discouraged from accessing module KV
data externally -- if it is necessary for users to populate data, modules
should provide special commands to set the data via the module.

Use the `get_store_prefix` function to enumerate keys within
a particular prefix (i.e. all keys starting with a particular substring).

MgrModule.get_store(*key*, *default=None*)
:   Get a value from this module’s persistent key value store

    Return type:
    :   `Optional`[`str`]

MgrModule.set_store(*key*, *val*)
:   Set a value in this module’s persistent key value store.
    If val is None, remove key from store

    Return type:
    :   `None`

MgrModule.get_localized_store(*key*, *default=None*)
:   Return type:
    :   `Optional`[`str`]

MgrModule.set_localized_store(*key*, *val*)
:   Return type:
    :   `None`

MgrModule.get_store_prefix(*key_prefix*)
:   Retrieve a dict of KV store keys to values, where the keys
    have the given prefix

    Parameters:
    :   **key_prefix** (*str*) --

    Return type:
    :   `Dict`[`str`, `str`]

    Returns:
    :   str

## Accessing cluster data

Modules have access to the in-memory copies of the Ceph cluster’s
state that the mgr maintains. Accessor functions as exposed
as members of MgrModule.

Calls that access the cluster or daemon state are generally going
from Python into native C++ routines. There is some overhead to this,
but much less than for example calling into a REST API or calling into
an SQL database.

There are no consistency rules about access to cluster structures or
daemon metadata. For example, an OSD might exist in OSDMap but
have no metadata, or vice versa. On a healthy cluster these
will be very rare transient states, but modules should be written
to cope with the possibility.

Note that these accessors must not be called in the modules `__init__`
function. This will result in a circular locking exception.

MgrModule.get(*data_name*)
:   Called by the plugin to fetch named cluster-wide objects from ceph-mgr.

    Parameters:
    :   **data_name** (*str*) -- Valid things to fetch are osdmap_crush_map_text,
        osd_map, osd_map_tree, osd_map_crush, config, mon_map, fs_map,
        osd_metadata, pg_summary, io_rate, pg_dump, df, osd_stats,
        health, mon_status, devices, device <devid>, pg_stats,
        pool_stats, pg_ready, osd_ping_times, mgr_map, mgr_ips,
        modified_config_options, service_map, mds_metadata,
        have_local_config_map, osd_pool_stats, pg_status.

    Note:
    :   All these structures have their own JSON representations: experiment
        or look at the C++ `dump()` methods to learn about them.

    Return type:
    :   `Any`

MgrModule.get_server(*hostname*)
:   Called by the plugin to fetch metadata about a particular hostname from
    ceph-mgr.

    This is information that ceph-mgr has gleaned from the daemon metadata
    reported by daemons running on a particular server.

    Parameters:
    :   **hostname** (`str`) -- a hostname

    Return type:
    :   `Dict`[`str`, `Union`[`str`, `List`[`Dict`[`str`, `str`]]]]

MgrModule.list_servers()
:   Like `get_server`, but gives information about all servers (i.e. all
    unique hostnames that have been mentioned in daemon metadata)

    Returns:
    :   a list of information about all servers

    Return type:
    :   list

MgrModule.get_metadata(*svc_type*, *svc_id*, *default=None*)
:   Fetch the daemon metadata for a particular service.

    ceph-mgr fetches metadata asynchronously, so are windows of time during
    addition/removal of services where the metadata is not available to
    modules. `None` is returned if no metadata is available.

    Parameters:
    :   - **svc_type** (*str*) -- service type (e.g., ‘mds’, ‘osd’, ‘mon’)
        - **svc_id** (*str*) -- service id. convert OSD integer IDs to strings when
          calling this

    Return type:
    :   dict, or None if no metadata found

MgrModule.get_daemon_status(*svc_type*, *svc_id*)
:   Fetch the latest status for a particular service daemon.

    This method may return `None` if no status information is
    available, for example because the daemon hasn’t fully started yet.

    Parameters:
    :   - **svc_type** (`str`) -- string (e.g., ‘rgw’)
        - **svc_id** (`str`) -- string

    Return type:
    :   `Dict`[`str`, `str`]

    Returns:
    :   dict, or None if the service is not found

MgrModule.get_perf_schema(*svc_type*, *svc_name*)
:   Called by the plugin to fetch perf counter schema info.
    svc_name can be nullptr, as can svc_type, in which case
    they are wildcards

    Parameters:
    :   - **svc_type** (*str*) --
        - **svc_name** (*str*) --

    Return type:
    :   `Dict`[`str`, `Dict`[`str`, `Dict`[`str`, `Union`[`str`, `int`]]]]

    Returns:
    :   list of dicts describing the counters requested

MgrModule.get_counter(*svc_type*, *svc_name*, *path*)
:   Called by the plugin to fetch the latest performance counter data for a
    particular counter on a particular service.

    Parameters:
    :   - **svc_type** (*str*) --
        - **svc_name** (*str*) --
        - **path** (*str*) -- a period-separated concatenation of the subsystem and the
          counter name, for example “mds.inodes”.

    Return type:
    :   `Dict`[`str`, `List`[`Tuple`[`float`, `int`]]]

    Returns:
    :   A dict of counter names to their values. each value is a list of
        of two-tuples of (timestamp, value). This may be empty if no data is
        available.

MgrModule.get_mgr_id()
:   Retrieve the name of the manager daemon where this plugin
    is currently being executed (i.e. the active manager).

    Return type:
    :   `str`

    Returns:
    :   str

MgrModule.get_daemon_health_metrics()
:   Get the list of health metrics per daemon. This includes SLOW_OPS health metrics
    in MON and OSD daemons, and PENDING_CREATING_PGS health metrics for OSDs.

    Return type:
    :   `Dict`[`str`, `List`[`Dict`[`str`, `Any`]]]

## Exposing health checks

Modules can raise first class Ceph health checks, which will be reported
in the output of `ceph status` and in other places that report on the
cluster’s health.

If you use `set_health_checks` to report a problem, be sure to call
it again with an empty dict to clear your health check when the problem
goes away.

MgrModule.set_health_checks(*checks*)
:   Set the module’s current map of health checks. Argument is a
    dict of check names to info, in this form:

    ```
    {
      'CHECK_FOO': {
        'severity': 'warning',           # or 'error'
        'summary': 'summary string',
        'count': 4,                      # quantify badness
        'detail': [ 'list', 'of', 'detail', 'strings' ],
       },
      'CHECK_BAR': {
        'severity': 'error',
        'summary': 'bars are bad',
        'detail': [ 'too hard' ],
      },
    }
    ```

    Parameters:
    :   **list** -- dict of health check dicts

    Return type:
    :   `None`

## What if the mons are down?

The manager daemon gets much of its state (such as the cluster maps)
from the monitor. If the monitor cluster is inaccessible, whichever
manager was active will continue to run, with the latest state it saw
still in memory.

However, if you are creating a module that shows the cluster state
to the user then you may well not want to mislead them by showing
them that out of date state.

To check if the manager daemon currently has a connection to
the monitor cluster, use this function:

MgrModule.have_mon_connection()
:   Check whether this ceph-mgr daemon has an open connection
    to a monitor. If it doesn’t, then it’s likely that the
    information we have about the cluster is out of date,
    and/or the monitor cluster is down.

    Return type:
    :   `bool`

## Reporting if your module cannot run

If your module cannot be run for any reason (such as a missing dependency),
then you can report that by implementing the `can_run` function.

*static* MgrModule.can_run()
:   Implement this function to report whether the module’s dependencies
    are met. For example, if the module needs to import a particular
    dependency to work, then use a try/except around the import at
    file scope, and then report here if the import failed.

    This will be called in a blocking way from the C++ code, so do not
    do any I/O that could block in this function.

    :return a 2-tuple consisting of a boolean and explanatory string

    Return type:
    :   `Tuple`[`bool`, `str`]

Note that this will only work properly if your module can always be imported:
if you are importing a dependency that may be absent, then do it in a
try/except block so that your module can be loaded far enough to use
`can_run` even if the dependency is absent.

## Sending commands

A non-blocking facility is provided for sending monitor commands
to the cluster.

MgrModule.send_command(*result*, *svc_type*, *svc_id*, *command*, *tag*, *inbuf=None*, *\**, *one_shot=False*)
:   Called by the plugin to send a command to the mon
    cluster.

    Parameters:
    :   - **result** (*CommandResult*) -- an instance of the `CommandResult`
          class, defined in the same module as MgrModule. This acts as a
          completion and stores the output of the command. Use
          `CommandResult.wait()` if you want to block on completion.
        - **svc_type** (*str*) --
        - **svc_id** (*str*) --
        - **command** (*str*) -- a JSON-serialized command. This uses the same
          format as the ceph command line, which is a dictionary of command
          arguments, with the extra `prefix` key containing the command
          name itself. Consult MonCommands.h for available commands and
          their expected arguments.
        - **tag** (*str*) -- used for nonblocking operation: when a command
          completes, the `notify()` callback on the MgrModule instance is
          triggered, with notify_type set to “command”, and notify_id set to
          the tag of the command.
        - **inbuf** (*str*) -- input buffer for sending additional data.
        - **one_shot** (*bool*) -- a keyword-only param to make the command abort
          with EPIPE when the target resets or refuses to reconnect

    Return type:
    :   `None`

## Receiving notifications

The manager daemon can call the `notify` method on active modules
when key pieces of cluster state are update such as the cluster maps.

> **Important:**
>
> Only modules that explicitly declare interest in a given
> notification type will receive it.

To receive notifications, a module must declare the NOTIFY_TYPES list:

```python
NOTIFY_TYPES = [
    NotifyType.mon_map,
    NotifyType.osd_map,
    NotifyType.crush_map,
    ...
]
```

The manager will call the module `notify` method only for types listed
in that array. Internally, it checks `should_notify` before dispatching
the notification.

The notification does not include the actual data - it’s just a cue to
tell the module that something has changed. It’s up to the module to retrieve
fresh data using mgr.get(…) if needed.

MgrModule.notify(*notify_type*, *notify_id*)
:   Called by the ceph-mgr service to notify the Python plugin
    that new state is available. This method is *only* called for
    notify_types that are listed in the NOTIFY_TYPES string list
    member of the module class.

    Parameters:
    :   - **notify_type** (`NotifyType`) -- string indicating what kind of notification,
          such as osd_map, mon_map, fs_map, mon_status,
          health, pg_summary, command, service_map
        - **notify_id** (`str`) -- string (may be empty) that optionally specifies
          which entity is being notified about. With
          “command” notifications this is set to the tag
          `from send_command`.

    Return type:
    :   `None`

## Accessing RADOS or CephFS

If you want to use the librados python API to access data stored in
the Ceph cluster, you can access the `rados` attribute of your
`MgrModule` instance. This is an instance of `rados.Rados` which
has been constructed for you using the existing Ceph context (an internal
detail of the C++ Ceph code) of the mgr daemon.

Always use this specially constructed librados instance instead of
constructing one by hand.

Similarly, if you are using libcephfs to access the file system, then
use the libcephfs `create_with_rados` to construct it from the
`MgrModule.rados` librados instance, and thereby inherit the correct context.

Remember that your module may be running while other parts of the cluster
are down: do not assume that librados or libcephfs calls will return
promptly -- consider whether to use timeouts or to block if the rest of
the cluster is not fully available.

## Implementing standby mode

For some modules, it is useful to run on standby manager daemons as well
as on the active daemon. For example, an HTTP server can usefully
serve HTTP redirect responses from the standby managers so that
the user can point his browser at any of the manager daemons without
having to worry about which one is active.

Standby manager daemons look for a subclass of `StandbyModule`
in each module. If the class is not found then the module is not
used at all on standby daemons. If the class is found, then
its `serve` method is called. Implementations of `StandbyModule`
must inherit from `mgr_module.MgrStandbyModule`.

The interface of `MgrStandbyModule` is much restricted compared to
`MgrModule` -- none of the Ceph cluster state is available to
the module. `serve` and `shutdown` methods are used in the same
way as a normal module class. The `get_active_uri` method enables
the standby module to discover the address of its active peer in
order to make redirects. See the `MgrStandbyModule` definition
in the Ceph source code for the full list of methods.

For an example of how to use this interface, look at the source code
of the `dashboard` module.

## Communicating between modules

Modules can invoke member functions of other modules.

MgrModule.remote(*module_name*, *method_name*, *\*args*, *\*\*kwargs*)
:   Invoke a method on another module. All arguments, and the return
    value from the other module must be serializable.

    Limitation: Do not import any modules within the called method.
    Otherwise you will get an error in Python 2:

    ```
    RuntimeError('cannot unmarshal code objects in restricted execution mode',)
    ```

    Parameters:
    :   - **module_name** (`str`) -- Name of other module. If module isn’t loaded,
          an ImportError exception is raised.
        - **method_name** (`str`) -- Method name. If it does not exist, a NameError
          exception is raised.
        - **args** (`Any`) -- Argument tuple
        - **kwargs** (`Any`) -- Keyword argument dict

    Raises:
    :   - **RuntimeError** -- **Any** error raised within the method is converted to a RuntimeError
        - **ImportError** -- No such module

    Return type:
    :   `Any`

Be sure to handle `ImportError` to deal with the case that the desired
module is not enabled.

If the remote method raises a python exception, this will be converted
to a RuntimeError on the calling side, where the message string describes
the exception that was originally thrown. If your logic intends
to handle certain errors cleanly, it is better to modify the remote method
to return an error value instead of raising an exception.

At time of writing, inter-module calls are implemented without
copies or serialization, so when you return a python object, you’re
returning a reference to that object to the calling module. It
is recommend *not* to rely on this reference passing, as in future the
implementation may change to serialize arguments and return
values.

## Shutting down cleanly

If a module implements the `serve()` method, it should also implement
the `shutdown()` method to shutdown cleanly: misbehaving modules
may otherwise prevent clean shutdown of ceph-mgr.

## Limitations

It is not possible to call back into C++ code from a module’s
`__init__()` method. For example calling `self.get_module_option()` at
this point will result in an assertion failure in ceph-mgr. For modules
that implement the `serve()` method, it usually makes sense to do most
initialization inside that method instead.

## Debugging

Apparently, we can always use the [Logging](index.md#mgr-module-dev-logging) facility
for debugging a ceph-mgr module. But some of us might miss [PDB](https://docs.python.org/3/library/pdb.html) and the
interactive Python interpreter. Yes, we can have them as well when developing
ceph-mgr modules! `ceph_mgr_repl.py` can drop you into an interactive shell
talking to `selftest` module. With this tool, one can peek and poke the
ceph-mgr module, and use all the exposed facilities in quite the same way
how we use the Python command line interpreter. For using `ceph_mgr_repl.py`,
we need to

1. ready a Ceph cluster
2. enable the `selftest` module
3. setup the necessary environment variables
4. launch the tool

Following is a sample session, in which the Ceph version is queried by
inputting `print(mgr.version)` at the prompt. And later
`timeit` module is imported to measure the execution time of
`mgr.get_mgr_id()`.

```console
$ cd build
$ MDS=0 MGR=1 OSD=3 MON=1 ../src/vstart.sh -n -x
$ bin/ceph mgr module enable selftest
$ ../src/pybind/ceph_mgr_repl.py --show-env
   $ export PYTHONPATH=/home/me/ceph/src/pybind:/home/me/ceph/build/lib/cython_modules/lib.3:/home/me/ceph/src/python-common:$PYTHONPATH
   $ export LD_LIBRARY_PATH=/home/me/ceph/build/lib:$LD_LIBRARY_PATH
$ export PYTHONPATH=/home/me/ceph/src/pybind:/home/me/ceph/build/lib/cython_modules/lib.3:/home/me/ceph/src/python-common:$PYTHONPATH
$ export LD_LIBRARY_PATH=/home/me/ceph/build/lib:$LD_LIBRARY_PATH
$ ../src/pybind/ceph_mgr_repl.py
$ ../src/pybind/ceph_mgr_repl.py
Python 3.9.2 (default, Feb 28 2021, 17:03:44)
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
(MgrModuleInteractiveConsole)
[mgr self-test eval] >>> print(mgr.version)
ceph version Development (no_version) quincy (dev)
[mgr self-test eval] >>> from timeit import timeit
[mgr self-test eval] >>> timeit(mgr.get_mgr_id)
0.16303414600042743
[mgr self-test eval] >>>
```

If you want to “talk” to a ceph-mgr module other than `selftest` using
this tool, you can either add a command to the module you want to debug
exactly like how `mgr self-test eval` command was added to `selftest`. Or
we can make this simpler by promoting the `eval()` method to a dedicated
[Mixin](_https:/en.wikipedia.org/wiki/Mixin.md) class and inherit your `MgrModule` subclass from it. And define
a command with it. Assuming the prefix of the command is `mgr my-module eval`,
one can just put

```
../src/pybind/ceph_mgr_repl.py --prefix "mgr my-module eval"
```

## Is something missing?

The ceph-mgr python interface is not set in stone. If you have a need
that is not satisfied by the current interface, please bring it up
on the ceph-devel mailing list. While it is desired to avoid bloating
the interface, it is not generally very hard to expose existing data
to the Python code when there is a good reason.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
