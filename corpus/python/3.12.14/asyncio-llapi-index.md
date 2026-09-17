---
collection: python
version: "3.12.14"
title: "Low-level API Index"
source_url: https://docs.python.org/3.12/library/asyncio-llapi-index.html
fetched_at: 2026-09-17T15:36:00+00:00
---
# Low-level API Index

This page lists all low-level asyncio APIs.

## Obtaining the Event Loop

|  |  |
| --- | --- |
| [`asyncio.get_running_loop()`](asyncio-eventloop.md#asyncio.get_running_loop "asyncio.get_running_loop") | The **preferred** function to get the running event loop. |
| [`asyncio.get_event_loop()`](asyncio-eventloop.md#asyncio.get_event_loop "asyncio.get_event_loop") | Get an event loop instance (running or current via the current policy). |
| [`asyncio.set_event_loop()`](asyncio-eventloop.md#asyncio.set_event_loop "asyncio.set_event_loop") | Set the event loop as current via the current policy. |
| [`asyncio.new_event_loop()`](asyncio-eventloop.md#asyncio.new_event_loop "asyncio.new_event_loop") | Create a new event loop. |

Examples

- [Using asyncio.get_running_loop()](asyncio-future.md#asyncio-example-future).

## Event Loop Methods

See also the main documentation section about the
[Event Loop Methods](asyncio-eventloop.md#asyncio-event-loop-methods).

Lifecycle

|  |  |
| --- | --- |
| [`loop.run_until_complete()`](asyncio-eventloop.md#asyncio.loop.run_until_complete "asyncio.loop.run_until_complete") | Run a Future/Task/awaitable until complete. |
| [`loop.run_forever()`](asyncio-eventloop.md#asyncio.loop.run_forever "asyncio.loop.run_forever") | Run the event loop forever. |
| [`loop.stop()`](asyncio-eventloop.md#asyncio.loop.stop "asyncio.loop.stop") | Stop the event loop. |
| [`loop.close()`](asyncio-eventloop.md#asyncio.loop.close "asyncio.loop.close") | Close the event loop. |
| [`loop.is_running()`](asyncio-eventloop.md#asyncio.loop.is_running "asyncio.loop.is_running") | Return `True` if the event loop is running. |
| [`loop.is_closed()`](asyncio-eventloop.md#asyncio.loop.is_closed "asyncio.loop.is_closed") | Return `True` if the event loop is closed. |
| `await` [`loop.shutdown_asyncgens()`](asyncio-eventloop.md#asyncio.loop.shutdown_asyncgens "asyncio.loop.shutdown_asyncgens") | Close asynchronous generators. |

Debugging

|  |  |
| --- | --- |
| [`loop.set_debug()`](asyncio-eventloop.md#asyncio.loop.set_debug "asyncio.loop.set_debug") | Enable or disable the debug mode. |
| [`loop.get_debug()`](asyncio-eventloop.md#asyncio.loop.get_debug "asyncio.loop.get_debug") | Get the current debug mode. |

Scheduling Callbacks

|  |  |
| --- | --- |
| [`loop.call_soon()`](asyncio-eventloop.md#asyncio.loop.call_soon "asyncio.loop.call_soon") | Invoke a callback soon. |
| [`loop.call_soon_threadsafe()`](asyncio-eventloop.md#asyncio.loop.call_soon_threadsafe "asyncio.loop.call_soon_threadsafe") | A thread-safe variant of [`loop.call_soon()`](asyncio-eventloop.md#asyncio.loop.call_soon "asyncio.loop.call_soon"). |
| [`loop.call_later()`](asyncio-eventloop.md#asyncio.loop.call_later "asyncio.loop.call_later") | Invoke a callback *after* the given time. |
| [`loop.call_at()`](asyncio-eventloop.md#asyncio.loop.call_at "asyncio.loop.call_at") | Invoke a callback *at* the given time. |

Thread/Process Pool

|  |  |
| --- | --- |
| `await` [`loop.run_in_executor()`](asyncio-eventloop.md#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor") | Run a CPU-bound or other blocking function in a [`concurrent.futures`](concurrent.futures.md#module-concurrent.futures "concurrent.futures: Execute computations concurrently using threads or processes.") executor. |
| [`loop.set_default_executor()`](asyncio-eventloop.md#asyncio.loop.set_default_executor "asyncio.loop.set_default_executor") | Set the default executor for [`loop.run_in_executor()`](asyncio-eventloop.md#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor"). |

Tasks and Futures

|  |  |
| --- | --- |
| [`loop.create_future()`](asyncio-eventloop.md#asyncio.loop.create_future "asyncio.loop.create_future") | Create a [`Future`](asyncio-future.md#asyncio.Future "asyncio.Future") object. |
| [`loop.create_task()`](asyncio-eventloop.md#asyncio.loop.create_task "asyncio.loop.create_task") | Schedule coroutine as a [`Task`](asyncio-task.md#asyncio.Task "asyncio.Task"). |
| [`loop.set_task_factory()`](asyncio-eventloop.md#asyncio.loop.set_task_factory "asyncio.loop.set_task_factory") | Set a factory used by [`loop.create_task()`](asyncio-eventloop.md#asyncio.loop.create_task "asyncio.loop.create_task") to create [`Tasks`](asyncio-task.md#asyncio.Task "asyncio.Task"). |
| [`loop.get_task_factory()`](asyncio-eventloop.md#asyncio.loop.get_task_factory "asyncio.loop.get_task_factory") | Get the factory [`loop.create_task()`](asyncio-eventloop.md#asyncio.loop.create_task "asyncio.loop.create_task") uses to create [`Tasks`](asyncio-task.md#asyncio.Task "asyncio.Task"). |

DNS

|  |  |
| --- | --- |
| `await` [`loop.getaddrinfo()`](asyncio-eventloop.md#asyncio.loop.getaddrinfo "asyncio.loop.getaddrinfo") | Asynchronous version of [`socket.getaddrinfo()`](socket.md#socket.getaddrinfo "socket.getaddrinfo"). |
| `await` [`loop.getnameinfo()`](asyncio-eventloop.md#asyncio.loop.getnameinfo "asyncio.loop.getnameinfo") | Asynchronous version of [`socket.getnameinfo()`](socket.md#socket.getnameinfo "socket.getnameinfo"). |

Networking and IPC

|  |  |
| --- | --- |
| `await` [`loop.create_connection()`](asyncio-eventloop.md#asyncio.loop.create_connection "asyncio.loop.create_connection") | Open a TCP connection. |
| `await` [`loop.create_server()`](asyncio-eventloop.md#asyncio.loop.create_server "asyncio.loop.create_server") | Create a TCP server. |
| `await` [`loop.create_unix_connection()`](asyncio-eventloop.md#asyncio.loop.create_unix_connection "asyncio.loop.create_unix_connection") | Open a Unix socket connection. |
| `await` [`loop.create_unix_server()`](asyncio-eventloop.md#asyncio.loop.create_unix_server "asyncio.loop.create_unix_server") | Create a Unix socket server. |
| `await` [`loop.connect_accepted_socket()`](asyncio-eventloop.md#asyncio.loop.connect_accepted_socket "asyncio.loop.connect_accepted_socket") | Wrap a [`socket`](socket.md#socket.socket "socket.socket") into a `(transport, protocol)` pair. |
| `await` [`loop.create_datagram_endpoint()`](asyncio-eventloop.md#asyncio.loop.create_datagram_endpoint "asyncio.loop.create_datagram_endpoint") | Open a datagram (UDP) connection. |
| `await` [`loop.sendfile()`](asyncio-eventloop.md#asyncio.loop.sendfile "asyncio.loop.sendfile") | Send a file over a transport. |
| `await` [`loop.start_tls()`](asyncio-eventloop.md#asyncio.loop.start_tls "asyncio.loop.start_tls") | Upgrade an existing connection to TLS. |
| `await` [`loop.connect_read_pipe()`](asyncio-eventloop.md#asyncio.loop.connect_read_pipe "asyncio.loop.connect_read_pipe") | Wrap a read end of a pipe into a `(transport, protocol)` pair. |
| `await` [`loop.connect_write_pipe()`](asyncio-eventloop.md#asyncio.loop.connect_write_pipe "asyncio.loop.connect_write_pipe") | Wrap a write end of a pipe into a `(transport, protocol)` pair. |

Sockets

|  |  |
| --- | --- |
| `await` [`loop.sock_recv()`](asyncio-eventloop.md#asyncio.loop.sock_recv "asyncio.loop.sock_recv") | Receive data from the [`socket`](socket.md#socket.socket "socket.socket"). |
| `await` [`loop.sock_recv_into()`](asyncio-eventloop.md#asyncio.loop.sock_recv_into "asyncio.loop.sock_recv_into") | Receive data from the [`socket`](socket.md#socket.socket "socket.socket") into a buffer. |
| `await` [`loop.sock_recvfrom()`](asyncio-eventloop.md#asyncio.loop.sock_recvfrom "asyncio.loop.sock_recvfrom") | Receive a datagram from the [`socket`](socket.md#socket.socket "socket.socket"). |
| `await` [`loop.sock_recvfrom_into()`](asyncio-eventloop.md#asyncio.loop.sock_recvfrom_into "asyncio.loop.sock_recvfrom_into") | Receive a datagram from the [`socket`](socket.md#socket.socket "socket.socket") into a buffer. |
| `await` [`loop.sock_sendall()`](asyncio-eventloop.md#asyncio.loop.sock_sendall "asyncio.loop.sock_sendall") | Send data to the [`socket`](socket.md#socket.socket "socket.socket"). |
| `await` [`loop.sock_sendto()`](asyncio-eventloop.md#asyncio.loop.sock_sendto "asyncio.loop.sock_sendto") | Send a datagram via the [`socket`](socket.md#socket.socket "socket.socket") to the given address. |
| `await` [`loop.sock_connect()`](asyncio-eventloop.md#asyncio.loop.sock_connect "asyncio.loop.sock_connect") | Connect the [`socket`](socket.md#socket.socket "socket.socket"). |
| `await` [`loop.sock_accept()`](asyncio-eventloop.md#asyncio.loop.sock_accept "asyncio.loop.sock_accept") | Accept a [`socket`](socket.md#socket.socket "socket.socket") connection. |
| `await` [`loop.sock_sendfile()`](asyncio-eventloop.md#asyncio.loop.sock_sendfile "asyncio.loop.sock_sendfile") | Send a file over the [`socket`](socket.md#socket.socket "socket.socket"). |
| [`loop.add_reader()`](asyncio-eventloop.md#asyncio.loop.add_reader "asyncio.loop.add_reader") | Start watching a file descriptor for read availability. |
| [`loop.remove_reader()`](asyncio-eventloop.md#asyncio.loop.remove_reader "asyncio.loop.remove_reader") | Stop watching a file descriptor for read availability. |
| [`loop.add_writer()`](asyncio-eventloop.md#asyncio.loop.add_writer "asyncio.loop.add_writer") | Start watching a file descriptor for write availability. |
| [`loop.remove_writer()`](asyncio-eventloop.md#asyncio.loop.remove_writer "asyncio.loop.remove_writer") | Stop watching a file descriptor for write availability. |

Unix Signals

|  |  |
| --- | --- |
| [`loop.add_signal_handler()`](asyncio-eventloop.md#asyncio.loop.add_signal_handler "asyncio.loop.add_signal_handler") | Add a handler for a [`signal`](signal.md#module-signal "signal: Set handlers for asynchronous events."). |
| [`loop.remove_signal_handler()`](asyncio-eventloop.md#asyncio.loop.remove_signal_handler "asyncio.loop.remove_signal_handler") | Remove a handler for a [`signal`](signal.md#module-signal "signal: Set handlers for asynchronous events."). |

Subprocesses

|  |  |
| --- | --- |
| [`loop.subprocess_exec()`](asyncio-eventloop.md#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec") | Spawn a subprocess. |
| [`loop.subprocess_shell()`](asyncio-eventloop.md#asyncio.loop.subprocess_shell "asyncio.loop.subprocess_shell") | Spawn a subprocess from a shell command. |

Error Handling

|  |  |
| --- | --- |
| [`loop.call_exception_handler()`](asyncio-eventloop.md#asyncio.loop.call_exception_handler "asyncio.loop.call_exception_handler") | Call the exception handler. |
| [`loop.set_exception_handler()`](asyncio-eventloop.md#asyncio.loop.set_exception_handler "asyncio.loop.set_exception_handler") | Set a new exception handler. |
| [`loop.get_exception_handler()`](asyncio-eventloop.md#asyncio.loop.get_exception_handler "asyncio.loop.get_exception_handler") | Get the current exception handler. |
| [`loop.default_exception_handler()`](asyncio-eventloop.md#asyncio.loop.default_exception_handler "asyncio.loop.default_exception_handler") | The default exception handler implementation. |

Examples

- [Using asyncio.new_event_loop() and loop.run_forever()](asyncio-eventloop.md#asyncio-example-lowlevel-helloworld).
- [Using loop.call_later()](asyncio-eventloop.md#asyncio-example-call-later).
- Using `loop.create_connection()` to implement
  [an echo-client](asyncio-protocol.md#asyncio-example-tcp-echo-client-protocol).
- Using `loop.create_connection()` to
  [connect a socket](asyncio-protocol.md#asyncio-example-create-connection).
- [Using add_reader() to watch an FD for read events](asyncio-eventloop.md#asyncio-example-watch-fd).
- [Using loop.add_signal_handler()](asyncio-eventloop.md#asyncio-example-unix-signals).
- [Using loop.subprocess_exec()](asyncio-protocol.md#asyncio-example-subprocess-proto).

## Transports

All transports implement the following methods:

|  |  |
| --- | --- |
| [`transport.close()`](asyncio-protocol.md#asyncio.BaseTransport.close "asyncio.BaseTransport.close") | Close the transport. |
| [`transport.is_closing()`](asyncio-protocol.md#asyncio.BaseTransport.is_closing "asyncio.BaseTransport.is_closing") | Return `True` if the transport is closing or is closed. |
| [`transport.get_extra_info()`](asyncio-protocol.md#asyncio.BaseTransport.get_extra_info "asyncio.BaseTransport.get_extra_info") | Request for information about the transport. |
| [`transport.set_protocol()`](asyncio-protocol.md#asyncio.BaseTransport.set_protocol "asyncio.BaseTransport.set_protocol") | Set a new protocol. |
| [`transport.get_protocol()`](asyncio-protocol.md#asyncio.BaseTransport.get_protocol "asyncio.BaseTransport.get_protocol") | Return the current protocol. |

Transports that can receive data (TCP and Unix connections,
pipes, etc). Returned from methods like
[`loop.create_connection()`](asyncio-eventloop.md#asyncio.loop.create_connection "asyncio.loop.create_connection"), [`loop.create_unix_connection()`](asyncio-eventloop.md#asyncio.loop.create_unix_connection "asyncio.loop.create_unix_connection"),
[`loop.connect_read_pipe()`](asyncio-eventloop.md#asyncio.loop.connect_read_pipe "asyncio.loop.connect_read_pipe"), etc:

Read Transports

|  |  |
| --- | --- |
| [`transport.is_reading()`](asyncio-protocol.md#asyncio.ReadTransport.is_reading "asyncio.ReadTransport.is_reading") | Return `True` if the transport is receiving. |
| [`transport.pause_reading()`](asyncio-protocol.md#asyncio.ReadTransport.pause_reading "asyncio.ReadTransport.pause_reading") | Pause receiving. |
| [`transport.resume_reading()`](asyncio-protocol.md#asyncio.ReadTransport.resume_reading "asyncio.ReadTransport.resume_reading") | Resume receiving. |

Transports that can Send data (TCP and Unix connections,
pipes, etc). Returned from methods like
[`loop.create_connection()`](asyncio-eventloop.md#asyncio.loop.create_connection "asyncio.loop.create_connection"), [`loop.create_unix_connection()`](asyncio-eventloop.md#asyncio.loop.create_unix_connection "asyncio.loop.create_unix_connection"),
[`loop.connect_write_pipe()`](asyncio-eventloop.md#asyncio.loop.connect_write_pipe "asyncio.loop.connect_write_pipe"), etc:

Write Transports

|  |  |
| --- | --- |
| [`transport.write()`](asyncio-protocol.md#asyncio.WriteTransport.write "asyncio.WriteTransport.write") | Write data to the transport. |
| [`transport.writelines()`](asyncio-protocol.md#asyncio.WriteTransport.writelines "asyncio.WriteTransport.writelines") | Write buffers to the transport. |
| [`transport.can_write_eof()`](asyncio-protocol.md#asyncio.WriteTransport.can_write_eof "asyncio.WriteTransport.can_write_eof") | Return [`True`](constants.md#True "True") if the transport supports sending EOF. |
| [`transport.write_eof()`](asyncio-protocol.md#asyncio.WriteTransport.write_eof "asyncio.WriteTransport.write_eof") | Close and send EOF after flushing buffered data. |
| [`transport.abort()`](asyncio-protocol.md#asyncio.WriteTransport.abort "asyncio.WriteTransport.abort") | Close the transport immediately. |
| [`transport.get_write_buffer_size()`](asyncio-protocol.md#asyncio.WriteTransport.get_write_buffer_size "asyncio.WriteTransport.get_write_buffer_size") | Return the current size of the output buffer. |
| [`transport.get_write_buffer_limits()`](asyncio-protocol.md#asyncio.WriteTransport.get_write_buffer_limits "asyncio.WriteTransport.get_write_buffer_limits") | Return high and low water marks for write flow control. |
| [`transport.set_write_buffer_limits()`](asyncio-protocol.md#asyncio.WriteTransport.set_write_buffer_limits "asyncio.WriteTransport.set_write_buffer_limits") | Set new high and low water marks for write flow control. |

Transports returned by [`loop.create_datagram_endpoint()`](asyncio-eventloop.md#asyncio.loop.create_datagram_endpoint "asyncio.loop.create_datagram_endpoint"):

Datagram Transports

|  |  |
| --- | --- |
| [`transport.sendto()`](asyncio-protocol.md#asyncio.DatagramTransport.sendto "asyncio.DatagramTransport.sendto") | Send data to the remote peer. |
| [`transport.abort()`](asyncio-protocol.md#asyncio.DatagramTransport.abort "asyncio.DatagramTransport.abort") | Close the transport immediately. |

Low-level transport abstraction over subprocesses.
Returned by [`loop.subprocess_exec()`](asyncio-eventloop.md#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec") and
[`loop.subprocess_shell()`](asyncio-eventloop.md#asyncio.loop.subprocess_shell "asyncio.loop.subprocess_shell"):

Subprocess Transports

|  |  |
| --- | --- |
| [`transport.get_pid()`](asyncio-protocol.md#asyncio.SubprocessTransport.get_pid "asyncio.SubprocessTransport.get_pid") | Return the subprocess process id. |
| [`transport.get_pipe_transport()`](asyncio-protocol.md#asyncio.SubprocessTransport.get_pipe_transport "asyncio.SubprocessTransport.get_pipe_transport") | Return the transport for the requested communication pipe (*stdin*, *stdout*, or *stderr*). |
| [`transport.get_returncode()`](asyncio-protocol.md#asyncio.SubprocessTransport.get_returncode "asyncio.SubprocessTransport.get_returncode") | Return the subprocess return code. |
| [`transport.kill()`](asyncio-protocol.md#asyncio.SubprocessTransport.kill "asyncio.SubprocessTransport.kill") | Kill the subprocess. |
| [`transport.send_signal()`](asyncio-protocol.md#asyncio.SubprocessTransport.send_signal "asyncio.SubprocessTransport.send_signal") | Send a signal to the subprocess. |
| [`transport.terminate()`](asyncio-protocol.md#asyncio.SubprocessTransport.terminate "asyncio.SubprocessTransport.terminate") | Stop the subprocess. |
| [`transport.close()`](asyncio-protocol.md#asyncio.SubprocessTransport.close "asyncio.SubprocessTransport.close") | Kill the subprocess and close all pipes. |

## Protocols

Protocol classes can implement the following **callback methods**:

|  |  |
| --- | --- |
| `callback` [`connection_made()`](asyncio-protocol.md#asyncio.BaseProtocol.connection_made "asyncio.BaseProtocol.connection_made") | Called when a connection is made. |
| `callback` [`connection_lost()`](asyncio-protocol.md#asyncio.BaseProtocol.connection_lost "asyncio.BaseProtocol.connection_lost") | Called when the connection is lost or closed. |
| `callback` [`pause_writing()`](asyncio-protocol.md#asyncio.BaseProtocol.pause_writing "asyncio.BaseProtocol.pause_writing") | Called when the transport’s buffer goes over the high water mark. |
| `callback` [`resume_writing()`](asyncio-protocol.md#asyncio.BaseProtocol.resume_writing "asyncio.BaseProtocol.resume_writing") | Called when the transport’s buffer drains below the low water mark. |

Streaming Protocols (TCP, Unix Sockets, Pipes)

|  |  |
| --- | --- |
| `callback` [`data_received()`](asyncio-protocol.md#asyncio.Protocol.data_received "asyncio.Protocol.data_received") | Called when some data is received. |
| `callback` [`eof_received()`](asyncio-protocol.md#asyncio.Protocol.eof_received "asyncio.Protocol.eof_received") | Called when an EOF is received. |

Buffered Streaming Protocols

|  |  |
| --- | --- |
| `callback` [`get_buffer()`](asyncio-protocol.md#asyncio.BufferedProtocol.get_buffer "asyncio.BufferedProtocol.get_buffer") | Called to allocate a new receive buffer. |
| `callback` [`buffer_updated()`](asyncio-protocol.md#asyncio.BufferedProtocol.buffer_updated "asyncio.BufferedProtocol.buffer_updated") | Called when the buffer was updated with the received data. |
| `callback` [`eof_received()`](asyncio-protocol.md#asyncio.BufferedProtocol.eof_received "asyncio.BufferedProtocol.eof_received") | Called when an EOF is received. |

Datagram Protocols

|  |  |
| --- | --- |
| `callback` [`datagram_received()`](asyncio-protocol.md#asyncio.DatagramProtocol.datagram_received "asyncio.DatagramProtocol.datagram_received") | Called when a datagram is received. |
| `callback` [`error_received()`](asyncio-protocol.md#asyncio.DatagramProtocol.error_received "asyncio.DatagramProtocol.error_received") | Called when a previous send or receive operation raises an [`OSError`](exceptions.md#OSError "OSError"). |

Subprocess Protocols

|  |  |
| --- | --- |
| `callback` [`pipe_data_received()`](asyncio-protocol.md#asyncio.SubprocessProtocol.pipe_data_received "asyncio.SubprocessProtocol.pipe_data_received") | Called when the child process writes data into its *stdout* or *stderr* pipe. |
| `callback` [`pipe_connection_lost()`](asyncio-protocol.md#asyncio.SubprocessProtocol.pipe_connection_lost "asyncio.SubprocessProtocol.pipe_connection_lost") | Called when one of the pipes communicating with the child process is closed. |
| `callback` [`process_exited()`](asyncio-protocol.md#asyncio.SubprocessProtocol.process_exited "asyncio.SubprocessProtocol.process_exited") | Called when the child process has exited. It can be called before [`pipe_data_received()`](asyncio-protocol.md#asyncio.SubprocessProtocol.pipe_data_received "asyncio.SubprocessProtocol.pipe_data_received") and [`pipe_connection_lost()`](asyncio-protocol.md#asyncio.SubprocessProtocol.pipe_connection_lost "asyncio.SubprocessProtocol.pipe_connection_lost") methods. |

## Event Loop Policies

Policies is a low-level mechanism to alter the behavior of
functions like [`asyncio.get_event_loop()`](asyncio-eventloop.md#asyncio.get_event_loop "asyncio.get_event_loop"). See also
the main [policies section](asyncio-policy.md#asyncio-policies) for more
details.

Accessing Policies

|  |  |
| --- | --- |
| [`asyncio.get_event_loop_policy()`](asyncio-policy.md#asyncio.get_event_loop_policy "asyncio.get_event_loop_policy") | Return the current process-wide policy. |
| [`asyncio.set_event_loop_policy()`](asyncio-policy.md#asyncio.set_event_loop_policy "asyncio.set_event_loop_policy") | Set a new process-wide policy. |
| [`AbstractEventLoopPolicy`](asyncio-policy.md#asyncio.AbstractEventLoopPolicy "asyncio.AbstractEventLoopPolicy") | Base class for policy objects. |
