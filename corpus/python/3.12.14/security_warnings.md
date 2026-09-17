---
collection: python
version: "3.12.14"
title: "Security Considerations"
source_url: https://docs.python.org/3.12/library/security_warnings.html
fetched_at: 2026-09-17T15:35:48+00:00
---
# Security Considerations

The following modules have specific security considerations:

- [`base64`](base64.md#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85"): [base64 security considerations](base64.md#base64-security) in
  [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
- [`cgi`](cgi.md#module-cgi "cgi: Helpers for running Python scripts via the Common Gateway Interface. (deprecated)"): [CGI security considerations](cgi.md#cgi-security)
- [`hashlib`](hashlib.md#module-hashlib "hashlib: Secure hash and message digest algorithms."): [all constructors take a “usedforsecurity” keyword-only
  argument disabling known insecure and blocked algorithms](hashlib.md#hashlib-usedforsecurity)
- [`http.server`](http.server.md#module-http.server "http.server: HTTP server and request handlers.") is not suitable for production use, only implementing
  basic security checks. See the [security considerations](http.server.md#http-server-security).
- [`logging`](logging.md#module-logging "logging: Flexible event logging system for applications."): [Logging configuration uses eval()](logging.config.md#logging-eval-security)
- [`multiprocessing`](multiprocessing.md#module-multiprocessing "multiprocessing: Process-based parallelism."): [Connection.recv() uses pickle](multiprocessing.md#multiprocessing-recv-pickle-security)
- [`pickle`](pickle.md#module-pickle "pickle: Convert Python objects to streams of bytes and back."): [Restricting globals in pickle](pickle.md#pickle-restrict)
- [`random`](random.md#module-random "random: Generate pseudo-random numbers with various common distributions.") shouldn’t be used for security purposes, use [`secrets`](secrets.md#module-secrets "secrets: Generate secure random numbers for managing secrets.")
  instead
- [`shelve`](shelve.md#module-shelve "shelve: Python object persistence."): [shelve is based on pickle and thus unsuitable for
  dealing with untrusted sources](shelve.md#shelve-security)
- [`ssl`](ssl.md#module-ssl "ssl: TLS/SSL wrapper for socket objects"): [SSL/TLS security considerations](ssl.md#ssl-security)
- [`subprocess`](subprocess.md#module-subprocess "subprocess: Subprocess management."): [Subprocess security considerations](subprocess.md#subprocess-security)
- [`tempfile`](tempfile.md#module-tempfile "tempfile: Generate temporary files and directories."): [mktemp is deprecated due to vulnerability to race
  conditions](tempfile.md#tempfile-mktemp-deprecated)
- [`xml`](xml.md#module-xml "xml: Package containing XML processing modules"): [XML vulnerabilities](xml.md#xml-vulnerabilities)
- [`zipfile`](zipfile.md#module-zipfile "zipfile: Read and write ZIP-format archive files."): [maliciously prepared .zip files can cause disk volume
  exhaustion](zipfile.md#zipfile-resources-limitations)

The [`-I`](https://docs.python.org/3.12/using/cmdline.html#cmdoption-I) command line option can be used to run Python in isolated
mode. When it cannot be used, the [`-P`](https://docs.python.org/3.12/using/cmdline.html#cmdoption-P) option or the
[`PYTHONSAFEPATH`](https://docs.python.org/3.12/using/cmdline.html#envvar-PYTHONSAFEPATH) environment variable can be used to not prepend a
potentially unsafe path to [`sys.path`](sys.md#sys.path "sys.path") such as the current directory, the
script’s directory or an empty string.
