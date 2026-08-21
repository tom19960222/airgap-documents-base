---
collection: libvirt
version: "12.7.0"
title: "Contributing to libvirt"
source_url: https://libvirt.org/contribute.html
fetched_at: 2026-08-21T04:09:20+00:00
---
# Contributing to libvirt

This page provides guidance on how to contribute to the libvirt project.

Contents

- [Contributions required](contribute.md#contributions-required)
- [Communication](contribute.md#communication)

  - [Mailing lists](contribute.md#mailing-lists)
  - [Instant messaging / chat](contribute.md#instant-messaging-chat)
- [Student / outreach coding programs](contribute.md#student-outreach-coding-programs)

# [Contributions required](contribute.md#id1)

The libvirt project is always looking for new contributors to participate in
ongoing activities. While code development is a major part of the project,
assistance is needed in many other areas including documentation writing, bug
triage, testing, application integration, website / wiki content management,
translation, branding, social media and more. The only requirement is an
interest in virtualization and desire to help.

The following is a non-exhaustive list of areas in which people can contribute
to libvirt. If you have ideas for other contributions feel free to follow them.

- **Software development**. The official upstream code are kept in various [Git
  repositories](https://gitlab.com/libvirt/). The core library / daemon (and
  thus the bulk of coding) is written in C, but there are language bindings
  written in Python, Perl, Java, Ruby, Php, OCaml and Go. There are also higher
  level wrappers mapping libvirt into other object frameworks, such GLib, CIM
  and SNMP. For those interested in working on the core parts of libvirt, the
  [contributor guidelines](hacking.md) are mandatory reading.
- **Translation**. All the libvirt modules aim to support translations where
  appropriate. All translation is handling outside of the normal libvirt review
  process, using the [Fedora
  instance](https://translate.fedoraproject.org/projects/libvirt/libvirt) of
  the Weblate tool. Thus people wishing to contribute to translation should
  join the Fedora translation team.
- **Documentation**. There are docbook guides on various aspects of libvirt,
  particularly application development guides for the C library and Python, and
  a virsh command reference. There is thus scope for work by people who are
  familiar with using or developing against libvirt, to write further content
  for these guides. There is also a need for people to review existing content
  for copy editing and identifying gaps in the docs.
- **Website / wiki curation**. The bulk of the website is maintained in the
  primary GIT repository, while the wiki site uses mediawiki. In both cases
  there is a need for people to both write new content and curate existing
  content to identify outdated information, improve its organization and target
  gaps.
- **Testing**. There are a number of tests suites that can run automated tests
  against libvirt. The coverage of the tests is never complete, so there is a
  need for people to create new test suites and / or provide environments to
  actually run the tests in a variety of deployment scenarios.
- **Code analysis**. The libvirt project has access to the coverity tool to run
  static analysis against the codebase, however, there are other types of code
  analysis that can be useful. In particular fuzzing of the inputs can be very
  effective at identifying problematic edge cases.
- **Security handling**. Downstream (operating system) vendors who distribute
  libvirt may wish to propose a person to be part of the security handling
  team, to get early access to information about forthcoming vulnerability
  fixes.
- **Evangelism**. Work done by the project is of no benefit unless the
  (potential) user community knows that it exists. Thus it is critically
  important to the health and future growth of the project, that there are a
  people who evangelize the work created by the project. This can take many
  forms, writing blog posts (about usage of features, personal user
  experiences, areas for future work, and more), syndicating docs and blogs via
  social media, giving user group and/or conference talks about libvirt.
- **User assistance**. Since documentation is never perfect, there are
  inevitably cases where users will struggle to attain a deployment goal they
  have, or run into trouble with managing an existing deployment. While some
  users may be able to contact a software vendor to obtain support, it is
  common to rely on community help forums such as [libvirt users mailing
  list](https://libvirt.org/contact.html#mailing-lists), or sites such as
  [stackoverflow.](https://stackoverflow.com/questions/tagged/libvirt)
  People who are familiar with libvirt and have ability & desire to help other
  users are encouraged to participate in these help forums.

# [Communication](contribute.md#id2)

For full details on contacting other project contributors read the
[contact](https://libvirt.org/contact.html) page. There are two main channels that libvirt uses
for communication between contributors:

## [Mailing lists](contribute.md#id3)

The project has a number of [mailing lists](https://libvirt.org/contact.html#mailing-lists) for
general communication between contributors. In general any design discussions
and review of contributions will take place on the mailing lists, so it is
important for all contributors to follow the traffic.

## [Instant messaging / chat](contribute.md#id4)

Contributors to libvirt are encouraged to join the [IRC
channel](https://libvirt.org/contact.html#irc) used by the project, where they can have live
conversations with others members.

# [Student / outreach coding programs](contribute.md#id5)

Since 2016, the libvirt project directly participates as an organization in the
[Google Summer of Code
program](https://wiki.libvirt.org/page/Google_Summer_of_Code_Ideas). Prior to
this the project had a number of students in the program via a joint application
with the QEMU project. People are encouraged to look at both the libvirt and
QEMU programs to identify potentially interesting projects to work on.
