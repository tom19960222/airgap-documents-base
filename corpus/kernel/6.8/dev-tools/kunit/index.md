---
collection: kernel
version: "6.8"
title: "KUnit - Linux Kernel Unit Testing"
source_url: https://www.kernel.org/doc/html/v6.8/dev-tools/kunit/index.html
fetched_at: 2026-08-21T03:33:37+00:00
---
# KUnit - Linux Kernel Unit Testing

Contents:

- [Getting Started](start.md)
  - [Installing Dependencies](start.md#installing-dependencies)
  - [Running tests with kunit_tool](start.md#running-tests-with-kunit-tool)
  - [Running Tests without the KUnit Wrapper](start.md#running-tests-without-the-kunit-wrapper)
  - [Writing Your First Test](start.md#writing-your-first-test)
  - [Next Steps](start.md#next-steps)
- [KUnit Architecture](architecture.md)
  - [In-Kernel Testing Framework](architecture.md#in-kernel-testing-framework)
  - [kunit_tool (Command-line Test Harness)](architecture.md#kunit-tool-command-line-test-harness)
- [Running tests with kunit_tool](run_wrapper.md)
  - [Creating a `.kunitconfig` file](run_wrapper.md#creating-a-kunitconfig-file)
  - [Configuring, building, and running tests](run_wrapper.md#configuring-building-and-running-tests)
  - [Parsing test results](run_wrapper.md#parsing-test-results)
  - [Filtering tests](run_wrapper.md#filtering-tests)
  - [Running tests on QEMU](run_wrapper.md#running-tests-on-qemu)
  - [Running command-line arguments](run_wrapper.md#running-command-line-arguments)
- [Run Tests without kunit_tool](run_manual.md)
  - [Configure the Kernel](run_manual.md#configure-the-kernel)
  - [debugfs](run_manual.md#debugfs)
  - [Retrieve Test Results](run_manual.md#retrieve-test-results)
  - [Run Tests After Kernel Has Booted](run_manual.md#run-tests-after-kernel-has-booted)
- [Writing Tests](usage.md)
  - [Test Cases](usage.md#test-cases)
  - [Customizing error messages](usage.md#customizing-error-messages)
  - [Writing Tests For Other Architectures](usage.md#writing-tests-for-other-architectures)
- [Common Patterns](usage.md#common-patterns)
  - [Isolating Behavior](usage.md#isolating-behavior)
  - [Testing Against Multiple Inputs](usage.md#testing-against-multiple-inputs)
  - [Allocating Memory](usage.md#allocating-memory)
  - [Registering Cleanup Actions](usage.md#registering-cleanup-actions)
  - [Testing Static Functions](usage.md#testing-static-functions)
  - [Injecting Test-Only Code](usage.md#injecting-test-only-code)
  - [Accessing The Current Test](usage.md#accessing-the-current-test)
  - [Failing The Current Test](usage.md#failing-the-current-test)
  - [Managing Fake Devices and Drivers](usage.md#managing-fake-devices-and-drivers)
- [API Reference](api/index.md)
- [Test Style and Nomenclature](style.md)
  - [Subsystems, Suites, and Tests](style.md#subsystems-suites-and-tests)
  - [Test Kconfig Entries](style.md#test-kconfig-entries)
  - [Test File and Module Names](style.md#test-file-and-module-names)
- [Frequently Asked Questions](faq.md)
  - [How is this different from Autotest, kselftest, and so on?](faq.md#how-is-this-different-from-autotest-kselftest-and-so-on)
  - [Does KUnit support running on architectures other than UML?](faq.md#does-kunit-support-running-on-architectures-other-than-uml)
  - [What is the difference between a unit test and other kinds of tests?](faq.md#what-is-the-difference-between-a-unit-test-and-other-kinds-of-tests)
  - [KUnit is not working, what should I do?](faq.md#kunit-is-not-working-what-should-i-do)
- [Tips For Running KUnit Tests](running_tips.md)
  - [Using `kunit.py run` ("kunit tool")](running_tips.md#using-kunit-py-run-kunit-tool)
  - [Running tests manually](running_tips.md#running-tests-manually)
  - [Test Attributes and Filtering](running_tips.md#test-attributes-and-filtering)

This section details the kernel unit testing framework.

## Introduction

KUnit (Kernel unit testing framework) provides a common framework for
unit tests within the Linux kernel. Using KUnit, you can define groups
of test cases called test suites. The tests either run on kernel boot
if built-in, or load as a module. KUnit automatically flags and reports
failed test cases in the kernel log. The test results appear in
[KTAP (Kernel - Test Anything Protocol) format](../ktap.md).
It is inspired by JUnit, Python’s unittest.mock, and GoogleTest/GoogleMock
(C++ unit testing framework).

KUnit tests are part of the kernel, written in the C (programming)
language, and test parts of the Kernel implementation (example: a C
language function). Excluding build time, from invocation to
completion, KUnit can run around 100 tests in less than 10 seconds.
KUnit can test any kernel component, for example: file system, system
calls, memory management, device drivers and so on.

KUnit follows the white-box testing approach. The test has access to
internal system functionality. KUnit runs in kernel space and is not
restricted to things exposed to user-space.

In addition, KUnit has kunit_tool, a script (`tools/testing/kunit/kunit.py`)
that configures the Linux kernel, runs KUnit tests under QEMU or UML
([User Mode Linux](../../virt/uml/user_mode_linux_howto_v2.md)),
parses the test results and
displays them in a user friendly manner.

### Features

- Provides a framework for writing unit tests.
- Runs tests on any kernel architecture.
- Runs a test in milliseconds.

### Prerequisites

- Any Linux kernel compatible hardware.
- For Kernel under test, Linux kernel version 5.5 or greater.

## Unit Testing

A unit test tests a single unit of code in isolation. A unit test is the finest
granularity of testing and allows all possible code paths to be tested in the
code under test. This is possible if the code under test is small and does not
have any external dependencies outside of the test's control like hardware.

### Write Unit Tests

To write good unit tests, there is a simple but powerful pattern:
Arrange-Act-Assert. This is a great way to structure test cases and
defines an order of operations.

- Arrange inputs and targets: At the start of the test, arrange the data
  that allows a function to work. Example: initialize a statement or
  object.
- Act on the target behavior: Call your function/code under test.
- Assert expected outcome: Verify that the result (or resulting state) is as
  expected.

### Unit Testing Advantages

- Increases testing speed and development in the long run.
- Detects bugs at initial stage and therefore decreases bug fix cost
  compared to acceptance testing.
- Improves code quality.
- Encourages writing testable code.

Read also [What is the difference between a unit test and other kinds of tests?](faq.md#kinds-of-tests).

## How do I use it?

You can find a step-by-step guide to writing and running KUnit tests in
[Getting Started](start.md)

Alternatively, feel free to look through the rest of the KUnit documentation,
or to experiment with tools/testing/kunit/kunit.py and the example test under
lib/kunit/kunit-example-test.c

Happy testing!
