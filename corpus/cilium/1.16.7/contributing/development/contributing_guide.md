---
collection: cilium
version: "1.16.7"
title: "How To Contribute"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/contributing/development/contributing_guide.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="howto_contribute"></a>

# How To Contribute

This document shows how to contribute as a community contributor.
[Guidance for reviewers and committers](reviewers_committers/index.md#reviewer_committer) is also
available.

## Cilium Feature Proposals

Before you start working on a significant code change, it's a good idea to make sure
that your approach is likely to be accepted. The best way to do this is to
create a [Cilium issue of type "Feature Request" in
GitHub](https://github.com/cilium/cilium/issues/new?assignees=&labels=kind%2Ffeature&template=feature_template.md&title=CFP%3A+)
where you describe your plans.

For longer proposals, you might like to include a link to an external doc (e.g.
a Google doc) where it's easier for reviewers to make comments and suggestions
in-line. The GitHub feature request template includes a link to the [Cilium
Feature Proposal template](https://docs.google.com/document/d/1vtE82JExQHw8_-pX2Uhq5acN1BMPxNlS6cMQUezRTWg/edit) which you are welcome to use to help structure your
proposal. Please make a copy of that template, fill it in with your ideas, and
ensure it's publicly visible, before adding the link into the GitHub issue.

<a id="provision_environment"></a>

## Clone and Provision Environment

1. Make sure you have a [GitHub account](https://github.com/join)
1. Fork the Cilium repository to your GitHub user or organization.
1. Turn off GitHub actions for your fork as described in the [GitHub Docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#managing-github-actions-permissions-for-your-repository).
   This is recommended to avoid unnecessary CI notification failures on the fork.
1. Clone your ``${YOUR_GITHUB_USERNAME_OR_ORG}/cilium`` fork and setup the base repository as ``upstream`` remote:

```shell-session
git clone https://github.com/${YOUR_GITHUB_USERNAME_OR_ORG}/cilium.git
cd cilium
git remote add upstream https://github.com/cilium/cilium.git
```

1. Set up your [dev_env](dev_setup.md#dev_env).
1. Check the GitHub issues for [good tasks to get started](https://github.com/cilium/cilium/issues?q=is%3Aopen+is%3Aissue+label%3Agood-first-issue).
1. Follow the steps in [making_changes](dev_setup.md#making_changes) to start contributing :)

<a id="submit_pr"></a>

## Submitting a pull request

Contributions must be submitted in the form of pull requests against the
upstream GitHub repository at https://github.com/cilium/cilium.

1. Fork the Cilium repository.
1. Push your changes to the topic branch in your fork of the repository.
1. Submit a pull request on https://github.com/cilium/cilium.

Before hitting the submit button, please make sure that the following
requirements have been met:

1. Take some time to describe your change in the PR description! A well-written
   description about the motivation of the change and choices you made during
   the implementation can go a long way to help the reviewers understand why
   you've made the change and why it's a good way to solve your problem. If
   it helps you to explain something, use pictures or
   [Mermaid diagrams](https://mermaid-js.github.io/).
1. Each commit must compile and be functional on its own to allow for
   bisecting of commits in the event of a bug affecting the tree.
1. All code is covered by unit and/or runtime tests where feasible.
1. All changes have been tested and checked for regressions by running the
   existing testsuite against your changes. See the [testsuite-legacy](../testing/e2e_legacy.md#testsuite-legacy) section
   for additional details.
1. All commits contain a well written commit description including a title,
   description and a ``Fixes: #XXX`` line if the commit addresses a particular
   GitHub issue. Note that the GitHub issue will be automatically closed when
   the commit is merged.

   :

```
apipanic: Log stack at debug level

Previously, it was difficult to debug issues when the API panicked
because only a single line like the following was printed:

level=warning msg="Cilium API handler panicked" client=@ method=GET
panic_message="write unix /var/run/cilium/cilium.sock->@: write: broken
pipe"

This patch logs the stack at this point at debug level so that it can at
least be determined in developer environments.

Fixes: #4191

Signed-off-by: Joe Stringer <joe@cilium.io>
```

> **Note:**
> Make sure to include a blank line in between commit title and commit
> description.

1. If any of the commits fixes a particular commit already in the tree, that
   commit is referenced in the commit message of the bugfix. This ensures that
   whoever performs a backport will pull in all required fixes:

   :

```
daemon: use endpoint RLock in HandleEndpoint

Fixes: a804c7c7dd9a ("daemon: wait for endpoint to be in ready state if specified via EndpointChangeRequest")

Signed-off-by: André Martins <andre@cilium.io>
```

> **Note:**
> The proper format for the ``Fixes:`` tag referring to commits is to use
> the first 12 characters of the git SHA followed by the full commit title
> as seen above without breaking the line.

1. If you change CLI arguments of any binaries in this repo, the CI will reject your PR if you don't
   also update the command reference docs. To do so, make sure to run the ``postcheck`` make target.

```shell-session
$ make postcheck
$ git add Documentation/cmdref
$ git commit
```

1. All commits are signed off. See the section [dev_coo](contributing_guide.md#dev_coo).

> **Note:**
> Passing the ``-s`` option to ``git commit`` will add the
> ``Signed-off-by:`` line to your commit message automatically.

1. Document any user-facing or breaking changes in ``Documentation/operations/upgrade.rst``.

1. (optional) Pick the appropriate milestone for which this PR is being
   targeted, e.g. ``1.6``, ``1.7``. This is in particular important in the time
   frame between the feature freeze and final release date.

1. If you have permissions to do so, pick the right release-note label. These
   labels will be used to generate the release notes which will primarily be
   read by users.

| Labels | When to set |
| --- | --- |
| ``release-note/bug`` | This is a non-trivial bugfix and is a user-facing bug |
| ``release-note/major`` | This is a major feature addition, e.g. Add MongoDB support |
| ``release-note/minor`` | This is a minor feature addition, e.g. Add support for a Kubernetes version |
| ``release-note/misc`` | This is a not user-facing change , e.g. Refactor endpoint package, a bug fix of a non-released feature |
| ``release-note/ci`` | This is a CI feature or bug fix. |

1. Verify the release note text. If not explicitly changed, the title of the PR
   will be used for the release notes. If you want to change this, you can add
   a special section to the description of the PR.
   These release notes are primarily going to be read by users so it is
   important that release notes for bugs, major and minor features do not
   contain internal details of Cilium functionality which sometimes are
   irrelevant for users.

   Example of a bad release note
   :

```
```release-note
Fix concurrent access in k8s watchers structures
```
```

   Example of a good release note
   :

```
```release-note
Fix panic when Cilium received an invalid Cilium Network Policy from Kubernetes
```
```

> **Note:**
> If multiple lines are provided, then the first line serves as the high
> level bullet point item and any additional line will be added as a sub
> item to the first line.

1. If you have permissions, pick the right labels for your PR:

| Labels | When to set |
| --- | --- |
| ``kind/bug`` | This is a bugfix worth mentioning in the release notes |
| ``kind/enhancement`` | This enhances existing functionality in Cilium |
| ``kind/feature`` | This is a feature |
| ``release-blocker/X.Y`` | This PR should block the next X.Y release |
| ``needs-backport/X.Y`` | PR needs to be backported to these stable releases |
| ``backport/X.Y`` | This is backport PR, may only be set as part of [backport_process](../release/backports.md#backport_process) |
| ``upgrade-impact`` | The code changes have a potential upgrade impact |
| ``area/*`` (Optional) | Code area this PR covers |

> **Note:**
> If you do not have permissions to set labels on your pull request. Leave
> a comment and a core team member will add the labels for you. Most
> reviewers will do this automatically without prior request.

1. Open a draft pull request. GitHub provides the ability to create a Pull
   Request in "draft" mode. On the "New Pull Request" page, below the pull
   request description box there is a button for creating the pull request.
   Click the arrow and choose "Create draft pull request". If your PR is still a
   work in progress, please select this mode. You will still be able to run the
   CI against it.

![](https://i1.wp.com/user-images.githubusercontent.com/3477155/52671177-5d0e0100-2ee8-11e9-8645-bdd923b7d93b.gif)

1. To notify reviewers that the PR is ready for review, click **Ready for
   review** at the bottom of the page.

1. Engage in any discussions raised by reviewers and address any changes
   requested. Set the PR to draft PR mode while you address changes, then click
   **Ready for review** to re-request review.

![](/images/cilium_request_review.png)

## Getting a pull request merged

1. As you submit the pull request as described in the section [submit_pr](contributing_guide.md#submit_pr).
   One of the reviewers will start a CI run by replying with a comment
   ``/test`` as described in [trigger_phrases](../testing/ci.md#trigger_phrases). If you are an
   [organization member](https://github.com/cilium/community/blob/main/CONTRIBUTOR-LADDER.md#organization-member), you can trigger the CI run yourself. CI consists of:

   1. Static code analysis by Github Actions and Travis CI. Golang linter
      suggestions are added in-line on PRs. For other failed jobs, please refer
      to build log for required action (e.g. Please run ``go mod tidy && go mod
      vendor`` and submit your changes, etc).

   1. [ci_gha](../testing/ci.md#ci_gha): Will run a series of tests:

      1. Unit tests
      1. Single node runtime tests
      1. Multi node Kubernetes tests

      If a CI test fails which seems unrelated to your PR, it may be a flaky
      test. Follow the process described in [ci_failure_triage](../testing/ci.md#ci_failure_triage).

1. As part of the submission, GitHub will have requested a review from the
   respective code owners according to the ``CODEOWNERS`` file in the
   repository.

   1. Address any feedback received from the reviewers
   1. You can push individual commits to address feedback and then rebase your
      branch at the end before merging.
   1. Once you have addressed the feedback, re-request a review from the
      reviewers that provided feedback by clicking on the button next to their
      name in the list of reviewers. This ensures that the reviewers are
      notified again that your PR is ready for subsequent review.

1. Owners of the repository will automatically adjust the labels on the pull
   request to track its state and progress towards merging.

1. Once the PR has been reviewed and the CI tests have passed, the PR will be
   merged by one of the repository owners. In case this does not happen, ping
   us on Cilium Slack <!-- unresolved-rst-link: kind=named target=Cilium Slack --> in the ``#development`` channel.

### Handling large pull requests

If the PR is considerably large (e.g. with more than 200 lines changed and/or
more than 6 commits), consider whether there is a good way to split the PR into
smaller PRs that can be merged more incrementally. Reviewers are often more
hesitant to review large PRs due to the level of complexity involved in
understanding the changes and the amount of time required to provide
constructive review comments. By making smaller logical PRs, this makes it
easier for the reviewer to provide comments and to engage in dialogue on the
PR, and also means there should be fewer overall pieces of feedback that you
need to address as a contributor. Tighter feedback cycles like this then make
it easier to get your contributions into the tree, which also helps with
reducing conflicts with other contributions. Good candidates for smaller PRs
may be individual bugfixes, or self-contained refactoring that adjusts the code
in order to make it easier to build subsequent functionality on top.

While handling review on larger PRs, consider creating a new commit to address
feedback from each review that you receive on your PR. This will make the
review process smoother as GitHub has limitations that prevents reviewers from
only seeing the new changes added since the last time they have reviewed a PR.
Once all reviews are addressed those commits should be squashed against the
commit that introduced those changes. This can be accomplished by the usage of
``git rebase -i upstream/main`` and in that windows, move these new commits
below the commit that introduced the changes and replace the work ``pick`` with
``fixup``. In the following example, commit ``d2cb02265`` will be combined into
``9c62e62d8`` and commit ``146829b59`` will be combined into ``9400fed20``.

    :

```
pick 9c62e62d8 docs: updating contribution guide process
fixup d2cb02265 joe + paul + chris changes
pick 9400fed20 docs: fixing typo
fixup 146829b59 Quentin and Maciej reviews
```

Once this is done you can perform push force into your branch and request for
your PR to be merged.

Reviewers should apply the documented [review_process](reviewers_committers/review_process.md#review_process) when providing
feedback to a PR.

<a id="dev_coo"></a>

## Developer's Certificate of Origin

To improve tracking of who did what, we've introduced a "sign-off"
procedure.

The sign-off is a simple line at the end of the explanation for the
commit, which certifies that you wrote it or otherwise have the right to
pass it on as open-source work. The rules are pretty simple: if you can
certify the below:

:

```
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.
1 Letterman Drive
Suite D4700
San Francisco, CA, 94129

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.

Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```

then you just add a line saying:

:

```
Signed-off-by: Random J Developer <random@developer.example.org>
```

If you need to add your sign off to a commit you have already made, please see [this article](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/managing-commits/amending-a-commit).

Cilium follows the real names policy described in the CNCF [DCO Guidelines v1.0](https://github.com/cncf/foundation/blob/main/dco-guidelines.md):

:

```
The DCO requires the use of a real name that can be used to identify
someone in case there is an issue about a contribution they made.

A real name does not require a legal name, nor a birth name, nor any name
that appears on an official ID (e.g. a passport). Your real name is the
name you convey to people in the community for them to use to identify you
as you. The key concern is that your identification is sufficient enough to
contact you if an issue were to arise in the future about your
contribution.

Your real name should not be an anonymous id or false name that
misrepresents who you are.
```

<a id="contributor_ladder"></a>

## Contributor Ladder

To help contributors grow in both privileges and responsibilities for the
project, Cilium also has a [contributor ladder](https://github.com/cilium/community/blob/main/CONTRIBUTOR-LADDER.md).
The ladder lays out how contributors can go from community contributor
to a committer and what is expected for each level. Community members
generally start at the first levels of the "ladder" and advance up it as
their involvement in the project grows. Our contributors are happy to
help you advance along the contributor ladder.
