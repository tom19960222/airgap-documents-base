---
collection: libvirt
version: "12.7.0"
title: "Handling of gitlab issues"
source_url: https://libvirt.org/issue-handling.html
fetched_at: 2026-08-21T04:10:16+00:00
---
# Handling of gitlab issues

Contents

- [Types of issues](issue-handling.md#types-of-issues)

  - [Bugs - kind::bug](issue-handling.md#bugs-kind-bug)
  - [Feature requests - kind::enhancement](issue-handling.md#feature-requests-kind-enhancement)
  - [User support queries - kind::support](issue-handling.md#user-support-queries-kind-support)
  - [Discussions - kind::discussion](issue-handling.md#discussions-kind-discussion)
- [States of issues](issue-handling.md#states-of-issues)

  - [Confirmed issues - state::confirmed](issue-handling.md#confirmed-issues-state-confirmed)
  - [Unconfirmed issues - state::unconfirmed](issue-handling.md#unconfirmed-issues-state-unconfirmed)
  - [Issues needing additional information from reporter - state::needinfo](issue-handling.md#issues-needing-additional-information-from-reporter-state-needinfo)
- [Triage process](issue-handling.md#triage-process)
- [Issues needing attention](issue-handling.md#issues-needing-attention)
- [Assigning issues](issue-handling.md#assigning-issues)
- [Contribution possibility for non-members of the project](issue-handling.md#contribution-possibility-for-non-members-of-the-project)
- [Disclaimer](issue-handling.md#disclaimer)

This document describes the life cycle and handling of upstream gitlab issues.
Issue is an aggregate term for bug reports, feature requests, user questions
and discussions.

For members of the project this is a guideline how to handle issues and how to
transition them between states based on the interaction with the reporter.

It is imperative we collaboratively keep the issues organized and labeled,
otherwise we'll end up creating an unnecessary maintenance burden for us.

For others, this article should only server as an outline what to expect when
filing an issue.

# [Types of issues](issue-handling.md#id1)

Every issue in our GitLab tracker bears the kind:: namespace prefix. Once
triaged, each issue will have one of the following types assigned to it.

Note that issues can be moved freely between the different issue kinds if
needed.

## [Bugs - kind::bug](issue-handling.md#id2)

This issue describes a flaw in the functionality. The user is expected to
describe how to reproduce the issue and add [debug logs](kbase/debuglogs.md) or a backtrace of all
daemon threads in case any of the components crashed.

## [Feature requests - kind::enhancement](issue-handling.md#id3)

This issue type describes non-existing functionality the user would like to add
to libvirt. Generally the issue should first focus on what the user wants to
achieve rather than any form of technical detail so that it's obvious what the
end goal is.

Detailed technical aspects can be described later but should not be the main
focus of the initial report. With a clear end-goal it's sometimes possible to
recommend another solution with the same impact.

## [User support queries - kind::support](issue-handling.md#id4)

This label is used with issues which don't directly correspond to a flaw or
a missing feature in the project like usage-related queries.

## [Discussions - kind::discussion](issue-handling.md#id5)

Any form of discussion which isn't related to any existing bug or feature
request.

# [States of issues](issue-handling.md#id6)

States allow project maintainers filtering out issues which need attention, so
please keep the issue state updated at all times.

## [Confirmed issues - state::confirmed](issue-handling.md#id7)

In case of kind::bug issues the **confirmed** state means that there is
a real problem with the functionality and there is (seemingly) enough
information to figure out where the problem is and fix it.

kind::enhancement issues should be marked as **confirmed** as long as the
general idea of the required functionality makes sense and would be in line
of the project strategy.

**Note:** Unless the issue is assigned to a specific person, the **confirmed**
state does not necessarily mean that anybody is actively looking to implement
the functionality or fix the problem. See the [disclaimer](issue-handling.md#disclaimer).

## [Unconfirmed issues - state::unconfirmed](issue-handling.md#id8)

kind::bug issues are considered **unconfirmed** when there is seemingly
enough information describing the problem, but the triager is not sure whether
the problem would be considered a bug.

In case of kind::enhancement issues the **unconfirmed** state is similarly
used for feature requests which might not make sense.

In general use of the **unconfirmed** state should be avoided if possible,
although if the initial triager requests all necessary information from the
reporter, but is not sure about the issue itself it's okay to defer it to
somebody else by setting the state::unconfirmed label and thus deferring it
to somebody with more knowledge about the code.

## [Issues needing additional information from reporter - state::needinfo](issue-handling.md#id9)

If additional information is requested from the reporter of the issue the
state:needinfo label should be added, so that the issues can be easily
filtered.

If the reporter doesn't respond to the request in a timely manner (~2 weeks)
the issue should be closed prompting the reporter to reopen once they provide
the required information.

# [Triage process](issue-handling.md#id10)

The following steps should be applied to any new issue reported.

> - Set the labels categorrizing the area of the issue, e.g. driver-qemu,
>   virsh, xml etc. If an appropriate label is not available, add it.
> - Check whether the reporter described the issue sufficiently.
>   If something is missing or unclear, ask for additional data and set
>   state::needinfo.
> - Once all requested information is provided set the appropriate state:
>   :   - state::confirmed if you are certain where the bug is or that the
>         feature request makes sense
>       - state::unconfirmed to defer the investigation to somebody else

# [Issues needing attention](issue-handling.md#id11)

The following gitlab search queries provide lists of issues which require
attention from the upstream community.

> [Untriaged issues](https://gitlab.com/libvirt/libvirt/-/issues/?sort=created_date&state=opened&not%5Blabel_name%5D%5B%5D=state%3A%3Aunconfirmed&not%5Blabel_name%5D%5B%5D=state%3A%3Aneedinfo&not%5Blabel_name%5D%5B%5D=state%3A%3Aconfirmed&first_page_size=100)
> :   Issues which haven't undergone the [Triage process](issue-handling.md#triage-process) yet.
>
> [Unconfirmed bugs](https://gitlab.com/libvirt/libvirt/-/issues/?sort=created_date&state=opened&label_name%5B%5D=kind%3A%3Abug&label_name%5B%5D=state%3A%3Aunconfirmed&first_page_size=100)
> :   Bugs which should have all the information needed but the initial triager
>     couldn't determine nor confirm the problem.
>
> [Unconfirmed features](https://gitlab.com/libvirt/libvirt/-/issues/?sort=created_date&state=opened&label_name%5B%5D=kind%3A%3Aenhancement&label_name%5B%5D=state%3A%3Aunconfirmed&first_page_size=100)
> :   Feature requests having the proper description of the request but it's not
>     yet clear whether the feature makes sense.

# [Assigning issues](issue-handling.md#id12)

When you plan to address an issue please assign it to yourself to indicate that
there's somebody working on it and thus prevent duplicated work.

# [Contribution possibility for non-members of the project](issue-handling.md#id13)

Anyone is very welcome to assist in handling and triage of issues.

Even though non-members don't have permissions to set the labels mentioned
above, you can always post a comment to the issue, describing your findings or
prompt the reporter to provide more information (obviously adhering to the
[code of conduct](https://libvirt.org/governance.html#code-of-conduct)) or even analyze where the problem lies followed by
submitting a patch to the mailing list.

Someone from the project members will then take care of applying the correct
label to the issue.

# [Disclaimer](issue-handling.md#id14)

Please note that libvirt, like most open source projects, relies on
contributors who have motivation, skills and available time to work on
implementing particular features or fixing bugs as well as assisting the
upstream community.

Reporting an issue can be helpful for determining demand and interest or
reporting a problem, but doing so is not a guarantee that a contributor will
volunteer to implement or fix it.

We even welcome and encourage draft patches implementing a feature to be sent
to the mailing list where they can be discussed and further improved by the
community.
