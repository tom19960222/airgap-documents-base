---
collection: kernel
version: "6.8"
title: "Linux Kernel Selftests"
source_url: https://www.kernel.org/doc/html/v6.8/dev-tools/kselftest.html
fetched_at: 2026-08-21T03:33:36+00:00
---
# Linux Kernel Selftests

The kernel contains a set of "self tests" under the tools/testing/selftests/
directory. These are intended to be small tests to exercise individual code
paths in the kernel. Tests are intended to be run after building, installing
and booting a kernel.

Kselftest from mainline can be run on older stable kernels. Running tests
from mainline offers the best coverage. Several test rings run mainline
kselftest suite on stable releases. The reason is that when a new test
gets added to test existing code to regression test a bug, we should be
able to run that test on an older kernel. Hence, it is important to keep
code that can still test an older kernel and make sure it skips the test
gracefully on newer releases.

You can find additional information on Kselftest framework, how to
write new tests using the framework on Kselftest wiki:

<https://kselftest.wiki.kernel.org/>

On some systems, hot-plug tests could hang forever waiting for cpu and
memory to be ready to be offlined. A special hot-plug target is created
to run the full range of hot-plug tests. In default mode, hot-plug tests run
in safe mode with a limited scope. In limited mode, cpu-hotplug test is
run on a single cpu as opposed to all hotplug capable cpus, and memory
hotplug test is run on 2% of hotplug capable memory instead of 10%.

kselftest runs as a userspace process. Tests that can be written/run in
userspace may wish to use the [Test Harness](kselftest.md#test-harness). Tests that need to be
run in kernel space may wish to use a [Test Module](kselftest.md#test-module).

## Running the selftests (hotplug tests are run in limited mode)

To build the tests:

```
$ make headers
$ make -C tools/testing/selftests
```

To run the tests:

```
$ make -C tools/testing/selftests run_tests
```

To build and run the tests with a single command, use:

```
$ make kselftest
```

Note that some tests will require root privileges.

Kselftest supports saving output files in a separate directory and then
running tests. To locate output files in a separate directory two syntaxes
are supported. In both cases the working directory must be the root of the
kernel src. This is applicable to "Running a subset of selftests" section
below.

To build, save output files in a separate directory with O=

```
$ make O=/tmp/kselftest kselftest
```

To build, save output files in a separate directory with KBUILD_OUTPUT

```
$ export KBUILD_OUTPUT=/tmp/kselftest; make kselftest
```

The O= assignment takes precedence over the KBUILD_OUTPUT environment
variable.

The above commands by default run the tests and print full pass/fail report.
Kselftest supports "summary" option to make it easier to understand the test
results. Please find the detailed individual test results for each test in
/tmp/testname file(s) when summary option is specified. This is applicable
to "Running a subset of selftests" section below.

To run kselftest with summary option enabled

```
$ make summary=1 kselftest
```

## Running a subset of selftests

You can use the "TARGETS" variable on the make command line to specify
single test to run, or a list of tests to run.

To run only tests targeted for a single subsystem:

```
$ make -C tools/testing/selftests TARGETS=ptrace run_tests
```

You can specify multiple tests to build and run:

```
$  make TARGETS="size timers" kselftest
```

To build, save output files in a separate directory with O=

```
$ make O=/tmp/kselftest TARGETS="size timers" kselftest
```

To build, save output files in a separate directory with KBUILD_OUTPUT

```
$ export KBUILD_OUTPUT=/tmp/kselftest; make TARGETS="size timers" kselftest
```

Additionally you can use the "SKIP_TARGETS" variable on the make command
line to specify one or more targets to exclude from the TARGETS list.

To run all tests but a single subsystem:

```
$ make -C tools/testing/selftests SKIP_TARGETS=ptrace run_tests
```

You can specify multiple tests to skip:

```
$  make SKIP_TARGETS="size timers" kselftest
```

You can also specify a restricted list of tests to run together with a
dedicated skiplist:

```
$  make TARGETS="breakpoints size timers" SKIP_TARGETS=size kselftest
```

See the top-level tools/testing/selftests/Makefile for the list of all
possible targets.

## Running the full range hotplug selftests

To build the hotplug tests:

```
$ make -C tools/testing/selftests hotplug
```

To run the hotplug tests:

```
$ make -C tools/testing/selftests run_hotplug
```

Note that some tests will require root privileges.

## Install selftests

You can use the "install" target of "make" (which calls the kselftest_install.sh
tool) to install selftests in the default location (tools/testing/selftests/kselftest_install),
or in a user specified location via the INSTALL_PATH "make" variable.

To install selftests in default location:

```
$ make -C tools/testing/selftests install
```

To install selftests in a user specified location:

```
$ make -C tools/testing/selftests install INSTALL_PATH=/some/other/path
```

## Running installed selftests

Found in the install directory, as well as in the Kselftest tarball,
is a script named run_kselftest.sh to run the tests.

You can simply do the following to run the installed Kselftests. Please
note some tests will require root privileges:

```
$ cd kselftest_install
$ ./run_kselftest.sh
```

To see the list of available tests, the -l option can be used:

```
$ ./run_kselftest.sh -l
```

The -c option can be used to run all the tests from a test collection, or
the -t option for specific single tests. Either can be used multiple times:

```
$ ./run_kselftest.sh -c size -c seccomp -t timers:posix_timers -t timer:nanosleep
```

For other features see the script usage output, seen with the -h option.

## Timeout for selftests

Selftests are designed to be quick and so a default timeout is used of 45
seconds for each test. Tests can override the default timeout by adding
a settings file in their directory and set a timeout variable there to the
configured a desired upper timeout for the test. Only a few tests override
the timeout with a value higher than 45 seconds, selftests strives to keep
it that way. Timeouts in selftests are not considered fatal because the
system under which a test runs may change and this can also modify the
expected time it takes to run a test. If you have control over the systems
which will run the tests you can configure a test runner on those systems to
use a greater or lower timeout on the command line as with the -o or
the --override-timeout argument. For example to use 165 seconds instead
one would use:

> $ ./run_kselftest.sh --override-timeout 165

You can look at the TAP output to see if you ran into the timeout. Test
runners which know a test must run under a specific time can then optionally
treat these timeouts then as fatal.

## Packaging selftests

In some cases packaging is desired, such as when tests need to run on a
different system. To package selftests, run:

```
$ make -C tools/testing/selftests gen_tar
```

This generates a tarball in the INSTALL_PATH/kselftest-packages directory. By
default, .gz format is used. The tar compression format can be overridden by
specifying a FORMAT make variable. Any value recognized by [tar's auto-compress](https://www.gnu.org/software/tar/manual/html_node/gzip.html#auto_002dcompress)
option is supported, such as:

```
$ make -C tools/testing/selftests gen_tar FORMAT=.xz
```

make gen_tar invokes make install so you can use it to package a subset of
tests by using variables specified in [Running a subset of selftests](kselftest.md#running-a-subset-of-selftests)
section:

```
$ make -C tools/testing/selftests gen_tar TARGETS="size" FORMAT=.xz
```

## Contributing new tests

In general, the rules for selftests are

> - Do as much as you can if you're not root;
> - Don't take too long;
> - Don't break the build on any architecture, and
> - Don't cause the top-level "make run_tests" to fail if your feature is
>   unconfigured.

## Contributing new tests (details)

> - In your Makefile, use facilities from lib.mk by including it instead of
>   reinventing the wheel. Specify flags and binaries generation flags on
>   need basis before including lib.mk.
>
>   ```
>   CFLAGS = $(KHDR_INCLUDES)
>   TEST_GEN_PROGS := close_range_test
>   include ../lib.mk
>   ```
> - Use TEST_GEN_XXX if such binaries or files are generated during
>   compiling.
>
>   TEST_PROGS, TEST_GEN_PROGS mean it is the executable tested by
>   default.
>
>   TEST_CUSTOM_PROGS should be used by tests that require custom build
>   rules and prevent common build rule use.
>
>   TEST_PROGS are for test shell scripts. Please ensure shell script has
>   its exec bit set. Otherwise, lib.mk run_tests will generate a warning.
>
>   TEST_CUSTOM_PROGS and TEST_PROGS will be run by common run_tests.
>
>   TEST_PROGS_EXTENDED, TEST_GEN_PROGS_EXTENDED mean it is the
>   executable which is not tested by default.
>   TEST_FILES, TEST_GEN_FILES mean it is the file which is used by
>   test.
> - First use the headers inside the kernel source and/or git repo, and then the
>   system headers. Headers for the kernel release as opposed to headers
>   installed by the distro on the system should be the primary focus to be able
>   to find regressions. Use KHDR_INCLUDES in Makefile to include headers from
>   the kernel source.
> - If a test needs specific kernel config options enabled, add a config file in
>   the test directory to enable them.
>
>   e.g: tools/testing/selftests/android/config
> - Create a .gitignore file inside test directory and add all generated objects
>   in it.
> - Add new test name in TARGETS in selftests/Makefile:
>
>   ```
>   TARGETS += android
>   ```
> - All changes should pass:
>
>   ```
>   kselftest-{all,install,clean,gen_tar}
>   kselftest-{all,install,clean,gen_tar} O=abo_path
>   kselftest-{all,install,clean,gen_tar} O=rel_path
>   make -C tools/testing/selftests {all,install,clean,gen_tar}
>   make -C tools/testing/selftests {all,install,clean,gen_tar} O=abs_path
>   make -C tools/testing/selftests {all,install,clean,gen_tar} O=rel_path
>   ```

## Test Module

Kselftest tests the kernel from userspace. Sometimes things need
testing from within the kernel, one method of doing this is to create a
test module. We can tie the module into the kselftest framework by
using a shell script test runner. `kselftest/module.sh` is designed
to facilitate this process. There is also a header file provided to
assist writing kernel modules that are for use with kselftest:

- `tools/testing/selftests/kselftest_module.h`
- `tools/testing/selftests/kselftest/module.sh`

Note that test modules should taint the kernel with TAINT_TEST. This will
happen automatically for modules which are in the `tools/testing/`
directory, or for modules which use the `kselftest_module.h` header above.
Otherwise, you'll need to add `MODULE_INFO(test, "Y")` to your module
source. selftests which do not load modules typically should not taint the
kernel, but in cases where a non-test module is loaded, TEST_TAINT can be
applied from userspace by writing to `/proc/sys/kernel/tainted`.

### How to use

Here we show the typical steps to create a test module and tie it into
kselftest. We use kselftests for lib/ as an example.

1. Create the test module
2. Create the test script that will run (load/unload) the module
   e.g. `tools/testing/selftests/lib/printf.sh`
3. Add line to config file e.g. `tools/testing/selftests/lib/config`
4. Add test script to makefile e.g. `tools/testing/selftests/lib/Makefile`
5. Verify it works:

```sh
# Assumes you have booted a fresh build of this kernel tree
cd /path/to/linux/tree
make kselftest-merge
make modules
sudo make modules_install
make TARGETS=lib kselftest
```

### Example Module

A bare bones test module might look like this:

```c
// SPDX-License-Identifier: GPL-2.0+

#define pr_fmt(fmt) KBUILD_MODNAME ": " fmt

#include "../tools/testing/selftests/kselftest_module.h"

KSTM_MODULE_GLOBALS();

/*
 * Kernel module for testing the foobinator
 */

static int __init test_function()
{
        ...
}

static void __init selftest(void)
{
        KSTM_CHECK_ZERO(do_test_case("", 0));
}

KSTM_MODULE_LOADERS(test_foo);
MODULE_AUTHOR("John Developer <jd@fooman.org>");
MODULE_LICENSE("GPL");
MODULE_INFO(test, "Y");
```

### Example test script

```sh
#!/bin/bash
# SPDX-License-Identifier: GPL-2.0+
$(dirname $0)/../kselftest/module.sh "foo" test_foo
```

## Test Harness

The kselftest_harness.h file contains useful helpers to build tests. The
test harness is for userspace testing, for kernel space testing see [Test
Module](kselftest.md#test-module) above.

The tests from tools/testing/selftests/seccomp/seccomp_bpf.c can be used as
example.

### Example

```c
#include "../kselftest_harness.h"

TEST(standalone_test) {
  do_some_stuff;
  EXPECT_GT(10, stuff) {
     stuff_state_t state;
     enumerate_stuff_state(&state);
     TH_LOG("expectation failed with state: %s", state.msg);
  }
  more_stuff;
  ASSERT_NE(some_stuff, NULL) TH_LOG("how did it happen?!");
  last_stuff;
  EXPECT_EQ(0, last_stuff);
}

FIXTURE(my_fixture) {
  mytype_t *data;
  int awesomeness_level;
};
FIXTURE_SETUP(my_fixture) {
  self->data = mytype_new();
  ASSERT_NE(NULL, self->data);
}
FIXTURE_TEARDOWN(my_fixture) {
  mytype_free(self->data);
}
TEST_F(my_fixture, data_is_good) {
  EXPECT_EQ(1, is_my_data_good(self->data));
}

TEST_HARNESS_MAIN
```

### Helpers

TH_LOG

`TH_LOG (fmt, ...)`

**Parameters**

`fmt`
:   format string

`...`
:   optional arguments

**Description**

```c
TH_LOG(format, ...)
```

Optional debug logging function available for use in tests.
Logging may be enabled or disabled by defining TH_LOG_ENABLED.
E.g., #define TH_LOG_ENABLED 1

If no definition is provided, logging is enabled by default.

If there is no way to print an error message for the process running the
test (e.g. not allowed to write to stderr), it is still possible to get the
ASSERT_\* number for which the test failed. This behavior can be enabled by
writing _metadata->no_print = true; before the check sequence that is
unable to print. When an error occur, instead of printing an error message
and calling abort(3), the test process call _exit(2) with the assert
number as argument, which is then printed by the parent process.

TEST

`TEST (test_name)`

> Defines the test function and creates the registration stub

**Parameters**

`test_name`
:   test name

**Description**

```c
TEST(name) { implementation }
```

Defines a test by name.
Names must be unique and tests must not be run in parallel. The
implementation containing block is a function and scoping should be treated
as such. Returning early may be performed with a bare "return;" statement.

EXPECT_\* and ASSERT_\* are valid in a [`TEST()`](kselftest.md#c.TEST "TEST") { } context.

TEST_SIGNAL

`TEST_SIGNAL (test_name, signal)`

**Parameters**

`test_name`
:   test name

`signal`
:   signal number

**Description**

```c
TEST_SIGNAL(name, signal) { implementation }
```

Defines a test by name and the expected term signal.
Names must be unique and tests must not be run in parallel. The
implementation containing block is a function and scoping should be treated
as such. Returning early may be performed with a bare "return;" statement.

EXPECT_\* and ASSERT_\* are valid in a [`TEST()`](kselftest.md#c.TEST "TEST") { } context.

FIXTURE_DATA

`FIXTURE_DATA (datatype_name)`

> Wraps the struct name so we have one less argument to pass around

**Parameters**

`datatype_name`
:   datatype name

**Description**

```c
FIXTURE_DATA(datatype_name)
```

Almost always, you want just [`FIXTURE()`](kselftest.md#c.FIXTURE "FIXTURE") instead (see below).
This call may be used when the type of the fixture data
is needed. In general, this should not be needed unless
the *self* is being passed to a helper directly.

FIXTURE

`FIXTURE (fixture_name)`

> Called once per fixture to setup the data and register

**Parameters**

`fixture_name`
:   fixture name

**Description**

```c
FIXTURE(fixture_name) {
  type property1;
  ...
};
```

Defines the data provided to [`TEST_F()`](kselftest.md#c.TEST_F "TEST_F")-defined tests as *self*. It should be
populated and cleaned up using [`FIXTURE_SETUP()`](kselftest.md#c.FIXTURE_SETUP "FIXTURE_SETUP") and [`FIXTURE_TEARDOWN()`](kselftest.md#c.FIXTURE_TEARDOWN "FIXTURE_TEARDOWN").

FIXTURE_SETUP

`FIXTURE_SETUP (fixture_name)`

> Prepares the setup function for the fixture. *_metadata* is included so that EXPECT_\*, ASSERT_\* etc. work correctly.

**Parameters**

`fixture_name`
:   fixture name

**Description**

```c
FIXTURE_SETUP(fixture_name) { implementation }
```

Populates the required "setup" function for a fixture. An instance of the
datatype defined with [`FIXTURE_DATA()`](kselftest.md#c.FIXTURE_DATA "FIXTURE_DATA") will be exposed as *self* for the
implementation.

ASSERT_\* are valid for use in this context and will prempt the execution
of any dependent fixture tests.

A bare "return;" statement may be used to return early.

FIXTURE_TEARDOWN

`FIXTURE_TEARDOWN (fixture_name)`

**Parameters**

`fixture_name`
:   fixture name

**Description**

*_metadata* is included so that EXPECT_\*, ASSERT_\* etc. work correctly.

```c
FIXTURE_TEARDOWN(fixture_name) { implementation }
```

Populates the required "teardown" function for a fixture. An instance of the
datatype defined with [`FIXTURE_DATA()`](kselftest.md#c.FIXTURE_DATA "FIXTURE_DATA") will be exposed as *self* for the
implementation to clean up.

A bare "return;" statement may be used to return early.

FIXTURE_VARIANT

`FIXTURE_VARIANT (fixture_name)`

> Optionally called once per fixture to declare fixture variant

**Parameters**

`fixture_name`
:   fixture name

**Description**

```c
FIXTURE_VARIANT(fixture_name) {
  type property1;
  ...
};
```

Defines type of constant parameters provided to [`FIXTURE_SETUP()`](kselftest.md#c.FIXTURE_SETUP "FIXTURE_SETUP"), [`TEST_F()`](kselftest.md#c.TEST_F "TEST_F") and
FIXTURE_TEARDOWN as *variant*. Variants allow the same tests to be run with
different arguments.

FIXTURE_VARIANT_ADD

`FIXTURE_VARIANT_ADD (fixture_name, variant_name)`

> Called once per fixture variant to setup and register the data

**Parameters**

`fixture_name`
:   fixture name

`variant_name`
:   name of the parameter set

**Description**

```c
FIXTURE_VARIANT_ADD(fixture_name, variant_name) {
  .property1 = val1,
  ...
};
```

Defines a variant of the test fixture, provided to [`FIXTURE_SETUP()`](kselftest.md#c.FIXTURE_SETUP "FIXTURE_SETUP") and
[`TEST_F()`](kselftest.md#c.TEST_F "TEST_F") as *variant*. Tests of each fixture will be run once for each
variant.

TEST_F

`TEST_F (fixture_name, test_name)`

> Emits test registration and helpers for fixture-based test cases

**Parameters**

`fixture_name`
:   fixture name

`test_name`
:   test name

**Description**

```c
TEST_F(fixture, name) { implementation }
```

Defines a test that depends on a fixture (e.g., is part of a test case).
Very similar to [`TEST()`](kselftest.md#c.TEST "TEST") except that *self* is the setup instance of fixture's
datatype exposed for use by the implementation.

TEST_HARNESS_MAIN

`TEST_HARNESS_MAIN ()`

> Simple wrapper to run the test harness

**Parameters**

**Description**

```c
TEST_HARNESS_MAIN
```

Use once to append a main() to the test file.

### Operators

Operators for use in [`TEST()`](kselftest.md#c.TEST "TEST") and [`TEST_F()`](kselftest.md#c.TEST_F "TEST_F").
ASSERT_\* calls will stop test execution immediately.
EXPECT_\* calls will emit a failure warning, note it, and continue.

ASSERT_EQ

`ASSERT_EQ (expected, seen)`

**Parameters**

`expected`
:   expected value

`seen`
:   measured value

**Description**

ASSERT_EQ(expected, measured): expected == measured

ASSERT_NE

`ASSERT_NE (expected, seen)`

**Parameters**

`expected`
:   expected value

`seen`
:   measured value

**Description**

ASSERT_NE(expected, measured): expected != measured

ASSERT_LT

`ASSERT_LT (expected, seen)`

**Parameters**

`expected`
:   expected value

`seen`
:   measured value

**Description**

ASSERT_LT(expected, measured): expected < measured

ASSERT_LE

`ASSERT_LE (expected, seen)`

**Parameters**

`expected`
:   expected value

`seen`
:   measured value

**Description**

ASSERT_LE(expected, measured): expected <= measured

ASSERT_GT

`ASSERT_GT (expected, seen)`

**Parameters**

`expected`
:   expected value

`seen`
:   measured value

**Description**

ASSERT_GT(expected, measured): expected > measured

ASSERT_GE

`ASSERT_GE (expected, seen)`

**Parameters**

`expected`
:   expected value

`seen`
:   measured value

**Description**

ASSERT_GE(expected, measured): expected >= measured

ASSERT_NULL

`ASSERT_NULL (seen)`

**Parameters**

`seen`
:   measured value

**Description**

ASSERT_NULL(measured): NULL == measured

ASSERT_TRUE

`ASSERT_TRUE (seen)`

**Parameters**

`seen`
:   measured value

**Description**

ASSERT_TRUE(measured): measured != 0

ASSERT_FALSE

`ASSERT_FALSE (seen)`

**Parameters**

`seen`
:   measured value

**Description**

ASSERT_FALSE(measured): measured == 0

ASSERT_STREQ

`ASSERT_STREQ (expected, seen)`

**Parameters**

`expected`
:   expected value

`seen`
:   measured value

**Description**

ASSERT_STREQ(expected, measured): !strcmp(expected, measured)

ASSERT_STRNE

`ASSERT_STRNE (expected, seen)`

**Parameters**

`expected`
:   expected value

`seen`
:   measured value

**Description**

ASSERT_STRNE(expected, measured): strcmp(expected, measured)

EXPECT_EQ

`EXPECT_EQ (expected, seen)`

**Parameters**

`expected`
:   expected value

`seen`
:   measured value

**Description**

EXPECT_EQ(expected, measured): expected == measured

EXPECT_NE

`EXPECT_NE (expected, seen)`

**Parameters**

`expected`
:   expected value

`seen`
:   measured value

**Description**

EXPECT_NE(expected, measured): expected != measured

EXPECT_LT

`EXPECT_LT (expected, seen)`

**Parameters**

`expected`
:   expected value

`seen`
:   measured value

**Description**

EXPECT_LT(expected, measured): expected < measured

EXPECT_LE

`EXPECT_LE (expected, seen)`

**Parameters**

`expected`
:   expected value

`seen`
:   measured value

**Description**

EXPECT_LE(expected, measured): expected <= measured

EXPECT_GT

`EXPECT_GT (expected, seen)`

**Parameters**

`expected`
:   expected value

`seen`
:   measured value

**Description**

EXPECT_GT(expected, measured): expected > measured

EXPECT_GE

`EXPECT_GE (expected, seen)`

**Parameters**

`expected`
:   expected value

`seen`
:   measured value

**Description**

EXPECT_GE(expected, measured): expected >= measured

EXPECT_NULL

`EXPECT_NULL (seen)`

**Parameters**

`seen`
:   measured value

**Description**

EXPECT_NULL(measured): NULL == measured

EXPECT_TRUE

`EXPECT_TRUE (seen)`

**Parameters**

`seen`
:   measured value

**Description**

EXPECT_TRUE(measured): 0 != measured

EXPECT_FALSE

`EXPECT_FALSE (seen)`

**Parameters**

`seen`
:   measured value

**Description**

EXPECT_FALSE(measured): 0 == measured

EXPECT_STREQ

`EXPECT_STREQ (expected, seen)`

**Parameters**

`expected`
:   expected value

`seen`
:   measured value

**Description**

EXPECT_STREQ(expected, measured): !strcmp(expected, measured)

EXPECT_STRNE

`EXPECT_STRNE (expected, seen)`

**Parameters**

`expected`
:   expected value

`seen`
:   measured value

**Description**

EXPECT_STRNE(expected, measured): strcmp(expected, measured)
