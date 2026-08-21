---
collection: qemu
version: "11.1.0"
title: "Submitting a Patch"
source_url: https://www.qemu.org/docs/master/devel/submitting-a-patch.html
fetched_at: 2026-08-21T03:23:42+00:00
---
# [Submitting a Patch](submitting-a-patch.md#id32)

QEMU welcomes contributions to fix bugs, add functionality or improve
the documentation. However, we get a lot of patches, and so we have
some guidelines about submitting them. If you follow these, you’ll
help make our task of contribution review easier and your change is
likely to be accepted and committed faster.

This page seems very long, so if you are only trying to post a quick
one-shot fix, the bare minimum we ask is that:

Minimal Checklist for Patches

| Check | Reason |
| --- | --- |
| Patches contain `Signed-off-by: Your Name <author@email>` | States you are legally able to contribute the code. See [Patch emails must include a Signed-off-by: line](submitting-a-patch.md#patch-emails-must-include-a-signed-off-by-line) |
| Sent as patch emails to `qemu-devel@nongnu.org` | The project uses an email list based workflow. See [Submitting your Patches](submitting-a-patch.md#submitting-your-patches) |
| Be prepared to respond to review comments | Code that doesn’t pass review will not get merged. See [Retrieve an existing series](submitting-a-patch.md#participating-in-code-review) |

You do not have to subscribe to post (list policy is to reply-to-all to
preserve CCs and keep non-subscribers in the loop on the threads they
start), although you may find it easier as a subscriber to pick up good
ideas from other posts. If you do subscribe, be prepared for a high
volume of email, often over one thousand messages in a week. The list is
moderated; first-time posts from an email address (whether or not you
subscribed) may be subject to some delay while waiting for a moderator
to allow your address.

The larger your contribution is, or if you plan on becoming a long-term
contributor, then the more important the rest of this page becomes.
Reading the table of contents below should already give you an idea of
the basic requirements. Use the table of contents as a reference, and
read the parts that you have doubts about.

Table of Contents

- [Submitting a Patch](submitting-a-patch.md#submitting-a-patch)

  - [Writing your Patches](submitting-a-patch.md#writing-your-patches)

    - [Use the QEMU coding style](submitting-a-patch.md#use-the-qemu-coding-style)
    - [Base patches against current git master](submitting-a-patch.md#base-patches-against-current-git-master)
    - [Split up long patches](submitting-a-patch.md#split-up-long-patches)
    - [Make code motion patches easy to review](submitting-a-patch.md#make-code-motion-patches-easy-to-review)
    - [Don’t include irrelevant changes](submitting-a-patch.md#don-t-include-irrelevant-changes)
    - [Write a meaningful commit message](submitting-a-patch.md#write-a-meaningful-commit-message)
    - [Test your patches](submitting-a-patch.md#test-your-patches)
  - [Submitting your Patches](submitting-a-patch.md#submitting-your-patches)

    - [Use B4](submitting-a-patch.md#use-b4)
    - [Use git-publish](submitting-a-patch.md#use-git-publish)
    - [If you cannot send patch emails](submitting-a-patch.md#if-you-cannot-send-patch-emails)
    - [CC the relevant maintainer](submitting-a-patch.md#cc-the-relevant-maintainer)
    - [Do not send as an attachment](submitting-a-patch.md#do-not-send-as-an-attachment)
    - [Use `git format-patch`](submitting-a-patch.md#use-git-format-patch)
    - [Avoid posting large binary blob](submitting-a-patch.md#avoid-posting-large-binary-blob)
    - [Patch emails must include a `Signed-off-by:` line](submitting-a-patch.md#patch-emails-must-include-a-signed-off-by-line)
    - [Include a meaningful cover letter](submitting-a-patch.md#include-a-meaningful-cover-letter)
    - [Use the RFC tag if needed](submitting-a-patch.md#use-the-rfc-tag-if-needed)
    - [Consider whether your patch is applicable for stable](submitting-a-patch.md#consider-whether-your-patch-is-applicable-for-stable)
  - [Retrieve an existing series](submitting-a-patch.md#retrieve-an-existing-series)
  - [Participating in Code Review](submitting-a-patch.md#id21)

    - [Stay around to fix problems raised in code review](submitting-a-patch.md#stay-around-to-fix-problems-raised-in-code-review)
    - [Pay attention to review comments](submitting-a-patch.md#pay-attention-to-review-comments)
    - [When resending patches add a version tag](submitting-a-patch.md#when-resending-patches-add-a-version-tag)
    - [Include version history in patchset revisions](submitting-a-patch.md#include-version-history-in-patchset-revisions)
  - [Tips and Tricks](submitting-a-patch.md#tips-and-tricks)

    - [Proper use of Reviewed-by: tags can aid review](submitting-a-patch.md#proper-use-of-reviewed-by-tags-can-aid-review)
    - [If your patch seems to have been ignored](submitting-a-patch.md#if-your-patch-seems-to-have-been-ignored)
    - [Is my patch in?](submitting-a-patch.md#is-my-patch-in)
    - [Return the favor](submitting-a-patch.md#return-the-favor)

## [Writing your Patches](submitting-a-patch.md#id33)

### [Use the QEMU coding style](submitting-a-patch.md#id34)

You can run run *scripts/checkpatch.pl <patchfile>* before submitting to
check that you are in compliance with our coding standards. Be aware
that `checkpatch.pl` is not infallible, though, especially where C
preprocessor macros are involved; use some common sense too. See also:

- [QEMU Coding Style](style.md#coding-style)
- [Automate a checkpatch run on
  commit](https://blog.vmsplice.net/2011/03/how-to-automatically-run-checkpatchpl.html)

### [Base patches against current git master](submitting-a-patch.md#id35)

There’s no point submitting a patch which is based on a released version
of QEMU because development will have moved on from then and it probably
won’t even apply to master. We only apply selected bugfixes to release
branches and then only as backports once the code has gone into master.

It is also okay to base patches on top of other on-going work that is
not yet part of the git master branch. To aid continuous integration
tools, such as [patchew](http://patchew.org/QEMU/), you should [add a
tag](https://lists.gnu.org/archive/html/qemu-devel/2017-08/msg01288.html)
line `Based-on: $MESSAGE_ID` to your cover letter to make the series
dependency obvious.

### [Split up long patches](submitting-a-patch.md#id36)

Split up longer patches into a patch series of logical code changes.
Each change should compile and execute successfully. For instance, don’t
add a file to the makefile in patch one and then add the file itself in
patch two. (This rule is here so that people can later use tools like
[git bisect](http://git-scm.com/docs/git-bisect) without hitting
points in the commit history where QEMU doesn’t work for reasons
unrelated to the bug they’re chasing.) Put documentation first, not
last, so that someone reading the series can do a clean-room evaluation
of the documentation, then validate that the code matched the
documentation. A commit message that mentions “Also, …” is often a
good candidate for splitting into multiple patches. For more thoughts on
properly splitting patches and writing good commit messages, see [this
advice from
OpenStack](https://wiki.openstack.org/wiki/GitCommitMessages).

### [Make code motion patches easy to review](submitting-a-patch.md#id37)

If a series requires large blocks of code motion, there are tricks for
making the refactoring easier to review. Split up the series so that
semantic changes (or even function renames) are done in a separate patch
from the raw code motion. Use a one-time setup of `git config
diff.renames true;` `git config diff.algorithm patience` (refer to
[git-config](http://git-scm.com/docs/git-config)). The ‘diff.renames’
property ensures file rename patches will be given in a more compact
representation that focuses only on the differences across the file
rename, instead of showing the entire old file as a deletion and the new
file as an insertion. Meanwhile, the ‘diff.algorithm’ property ensures
that extracting a non-contiguous subset of one file into a new file, but
where all extracted parts occur in the same order both before and after
the patch, will reduce churn in trying to treat unrelated `}` lines in
the original file as separating hunks of changes.

Ideally, a code motion patch can be reviewed by doing:

```
git format-patch --stdout -1 > patch;
diff -u <(sed -n 's/^-//p' patch) <(sed -n 's/^\+//p' patch)
```

to focus on the few changes that weren’t wholesale code motion.

### [Don’t include irrelevant changes](submitting-a-patch.md#id38)

In particular, don’t include formatting, coding style or whitespace
changes to bits of code that would otherwise not be touched by the
patch. (It’s OK to fix coding style issues in the immediate area (few
lines) of the lines you’re changing.) If you think a section of code
really does need a reindent or other large-scale style fix, submit this
as a separate patch which makes no semantic changes; don’t put it in the
same patch as your bug fix.

For smaller patches in less frequently changed areas of QEMU, consider
using the [Trivial Patches](trivial-patches.md#trivial-patches) process.

### [Write a meaningful commit message](submitting-a-patch.md#id39)

Commit messages should be meaningful and should stand on their own as a
historical record of why the changes you applied were necessary or
useful.

QEMU follows the usual standard for git commit messages: the first line
(which becomes the email subject line) is “subsystem: single line
summary of change”. Whether the “single line summary of change” starts
with a capital is a matter of taste, but we prefer that the summary does
not end in a dot. Look at `git shortlog -30` for an idea of sample
subject lines. Then there is a blank line and a more detailed
description of the patch, another blank and your Signed-off-by: line.
Please do not use lines that are longer than 76 characters in your
commit message (so that the text still shows up nicely with “git show”
in a 80-columns terminal window).

The body of the commit message is a good place to document why your
change is important. Don’t include comments like “This is a suggestion
for fixing this bug” (they can go below the `---` line in the email so
they don’t go into the final commit message). Make sure the body of the
commit message can be read in isolation even if the reader’s mailer
displays the subject line some distance apart (that is, a body that
starts with “… so that” as a continuation of the subject line is
harder to follow).

If your patch fixes a commit that is already in the repository, please
add an additional line with “Fixes: <at-least-12-digits-of-SHA-commit-id>
(“Fixed commit subject”)” below the patch description / before your
“Signed-off-by:” line in the commit message.

If your patch fixes a bug in the gitlab bug tracker, please add a line
with “Resolves: <URL-of-the-bug>” to the commit message, too. Gitlab can
close bugs automatically once commits with the “Resolves:” keyword get
merged into the master branch of the project. And if your patch addresses
a bug in another public bug tracker, you can also use a line with
“Buglink: <URL-of-the-bug>” for reference here, too.

Example:

```
Fixes: 14055ce53c2d ("s390x/tcg: avoid overflows in time2tod/tod2time")
Resolves: https://gitlab.com/qemu-project/qemu/-/issues/42
Buglink: https://bugs.launchpad.net/qemu/+bug/1804323``
```

Some other tags that are used in commit messages include “Message-Id:”
“Tested-by:”, “Acked-by:”, “Reported-by:”, “Suggested-by:”. See `git
log` for these keywords for example usage.

### [Test your patches](submitting-a-patch.md#id40)

Although QEMU uses various [Continuous Integration (CI)](testing/ci.md#ci) services that attempt to test
patches submitted to the list, it still saves everyone time if you
have already tested that your patch compiles and works. Because QEMU
is such a large project the default configuration won’t create a
testing pipeline on GitLab when a branch is pushed. See the [CI
variable documentation](testing/ci.md#ci-var) for details on how to control the
running of tests; but it is still wise to also check that your patches
work with a full build before submitting a series, especially if your
changes might have an unintended effect on other areas of the code you
don’t normally experiment with. See [Testing in QEMU](testing/main.md#testing) for more details on
what tests are available.

Also, it is a wise idea to include a testsuite addition as part of
your patches - either to ensure that future changes won’t regress your
new feature, or to add a test which exposes the bug that the rest of
your series fixes. Keeping separate commits for the test and the fix
allows reviewers to rebase the test to occur first to prove it catches
the problem, then again to place it last in the series so that
bisection doesn’t land on a known-broken state.

## [Submitting your Patches](submitting-a-patch.md#id41)

The QEMU project uses a public email based workflow for reviewing and
merging patches. As a result all contributions to QEMU must be **sent
as patches** to the qemu-devel [mailing list](https://wiki.qemu.org/Contribute/MailingLists). Patch
contributions should not be posted on the bug tracker, posted on
forums, or externally hosted and linked to. (We have other mailing
lists too, but all patches must go to qemu-devel, possibly with a Cc:
to another list.) `git send-email` ([step-by-step setup guide](https://git-send-email.io/) and [hints and tips](https://elixir.bootlin.com/linux/latest/source/Documentation/process/email-clients.rst))
works best for delivering the patch without mangling it, but
attachments can be used as a last resort on a first-time submission.

### [Use B4](submitting-a-patch.md#id42)

The [b4](https://github.com/mricon/b4/) tool, used for Linux kernel development, can also be used for QEMU
development. It is packaged in most distros and PyPi. The QEMU source tree
includes a `b4` project configuration file at the root: `.b4-config`.

Example workflow to prepare a patch series:

1. Start with a clean checkout of the `master` branch.
2. Create a new series with a topical branch name using `b4 prep -n descriptive-name`.
   `b4` will create a `b4/descriptive-name` branch and switch to it.
3. Commit your changes, following this page’s guidelines about proper commit messages etc.
4. Write a descriptive cover letter with `b4 prep --edit-cover`.
5. Add maintainer and reviewer CCs with `b4 prep --auto-to-cc`. You can make
   changes to Cc: and To: recipients by editing the cover letter.
6. Run patch checks with `b4 prep --check`.
7. Optionally review the patches with `b4 send --dry-run` which will print the
   raw patches in standard output.

To send the patches, you can:

- Setup `git-send-email` and use `b4 send`, or
- Export the patches to files using `b4 send -o OUTPUT_DIR` and send them manually.

For more details, consult the [b4 documentation](https://b4.docs.kernel.org/).

### [Use git-publish](submitting-a-patch.md#id43)

If you already configured git send-email, you can simply use [git-publish](https://github.com/stefanha/git-publish) to send series.

```
$ git checkout master -b my-feature
$ # work on new commits, add your 'Signed-off-by' lines to each
$ git publish
$ ... more work, rebase on master, ...
$ git publish # will send a v2
```

Each time you post a series, git-publish will create a local tag with the format
`<branchname>-v<version>` to record the patch series.

When sending patch emails, ‘git publish’ will consult the output of
‘scripts/get_maintainers.pl’ and automatically CC anyone listed as maintainers
of the affected code. Generally you should accept the suggested CC list, but
there may sometimes be scenarios where it is appropriate to cut it down (eg on
certain large tree-wide cleanups), or augment it with other interested people.

### [If you cannot send patch emails](submitting-a-patch.md#id44)

In rare cases it may not be possible to send properly formatted patch
emails. You can use [sourcehut](https://sourcehut.org/) to send your
patches to the QEMU mailing list by following these steps:

1. Register or sign in to your account
2. Add your SSH public key in [meta |
   keys](https://meta.sr.ht/keys).
3. Publish your git branch using **git push git@git.sr.ht:~USERNAME/qemu
   HEAD**
4. Send your patches to the QEMU mailing list using the web-based
   `git-send-email` UI at <https://git.sr.ht/~USERNAME/qemu/send-email>

Documentation for sourcehut is available [here](https://man.sr.ht/git.sr.ht/#sending-patches-upstream).

### [CC the relevant maintainer](submitting-a-patch.md#id45)

Send patches both to the mailing list and CC the maintainer(s) of the
files you are modifying. look in the MAINTAINERS file to find out who
that is. Also try using scripts/get_maintainer.pl from the repository
for learning the most common committers for the files you touched.

Example:

```
~/src/qemu/scripts/get_maintainer.pl -f hw/ide/core.c
```

In fact, you can automate this, via a one-time setup of `git config
sendemail.cccmd 'scripts/get_maintainer.pl --nogit-fallback'` (Refer to
[git-config](http://git-scm.com/docs/git-config).)

### [Do not send as an attachment](submitting-a-patch.md#id46)

Send patches inline so they are easy to reply to with review comments.
Do not put patches in attachments.

### [Use `git format-patch`](submitting-a-patch.md#id47)

Use the right diff format.
[git format-patch](http://git-scm.com/docs/git-format-patch) will
produce patch emails in the right format (check the documentation to
find out how to drive it). You can then edit the cover letter before
using `git send-email` to mail the files to the mailing list. (We
recommend [git send-email](http://git-scm.com/docs/git-send-email)
because mail clients often mangle patches by wrapping long lines or
messing up whitespace. Some distributions do not include send-email in a
default install of git; you may need to download additional packages,
such as ‘git-email’ on Fedora-based systems.) Patch series need a cover
letter, with shallow threading (all patches in the series are
in-reply-to the cover letter, but not to each other); single unrelated
patches do not need a cover letter (but if you do send a cover letter,
use `--numbered` so the cover and the patch have distinct subject lines).
Patches are easier to find if they start a new top-level thread, rather
than being buried in-reply-to another existing thread.

### [Avoid posting large binary blob](submitting-a-patch.md#id48)

If you added binaries to the repository, consider producing the patch
emails using `git format-patch --no-binary` and include a link to a
git repository to fetch the original commit.

### [Patch emails must include a `Signed-off-by:` line](submitting-a-patch.md#id49)

Your patches **must** include a Signed-off-by: line. This is a hard
requirement because it’s how you say “I’m legally okay to contribute
this and happy for it to go into QEMU”. For full guidance, read the
[Code provenance](code-provenance.md#code-provenance) documentation.

### [Include a meaningful cover letter](submitting-a-patch.md#id50)

This is a requirement for any series with multiple patches (as it aids
continuous integration), but optional for an isolated patch. The cover
letter explains the overall goal of such a series, and also provides a
convenient 0/N email for others to reply to the series as a whole. A
one-time setup of `git config format.coverletter auto` (refer to
[git-config](http://git-scm.com/docs/git-config)) will generate the
cover letter as needed.

When reviewers don’t know your goal at the start of their review, they
may object to early changes that don’t make sense until the end of the
series, because they do not have enough context yet at that point of
their review. A series where the goal is unclear also risks a higher
number of review-fix cycles because the reviewers haven’t bought into
the idea yet. If the cover letter can explain these points to the
reviewer, the process will be smoother patches will get merged faster.
Make sure your cover letter includes a diffstat of changes made over the
entire series; potential reviewers know what files they are interested
in, and they need an easy way determine if your series touches them.

### [Use the RFC tag if needed](submitting-a-patch.md#id51)

For example, “[PATCH RFC v2]”. `git format-patch --subject-prefix=RFC`
can help.

“RFC” means “Request For Comments” and is a statement that you don’t
intend for your patchset to be applied to master, but would like some
review on it anyway. Reasons for doing this include:

- the patch depends on some pending kernel changes which haven’t yet
  been accepted, so the QEMU patch series is blocked until that
  dependency has been dealt with, but is worth reviewing anyway
- the patch set is not finished yet (perhaps it doesn’t cover all use
  cases or work with all targets) but you want early review of a major
  API change or design structure before continuing

In general, since it’s asking other people to do review work on a
patchset that the submitter themselves is saying shouldn’t be applied,
it’s best to:

- use it sparingly
- in the cover letter, be clear about why a patch is an RFC, what areas
  of the patchset you’re looking for review on, and why reviewers
  should care

### [Consider whether your patch is applicable for stable](submitting-a-patch.md#id52)

If your patch fixes a severe issue or a regression, it may be applicable
for stable. In that case, consider adding `Cc: qemu-stable@nongnu.org`
to your patch to notify the stable maintainers.

For more details on how QEMU’s stable process works, refer to the
[QEMU and the stable process](stable-process.md#stable-process) page.

## [Retrieve an existing series](submitting-a-patch.md#id53)

If you want to apply an existing series on top of your tree, you can simply use
[b4](https://github.com/mricon/b4/).

```
b4 shazam $msg-id
```

The message id is related to the patch series that has been sent to the mailing
list. You need to retrieve the “Message-Id:” header from one of the patches. Any
of them can be used and b4 will apply the whole series.

## [Participating in Code Review](submitting-a-patch.md#id54)

All patches submitted to the QEMU project go through a code review
process before they are accepted. This will often mean a series will
go through a number of iterations before being picked up by
[maintainers](maintainers.md#maintainers). You therefore should be prepared to
read replies to your messages and be willing to act on them.

Maintainers are often willing to manually fix up first-time
contributions, since there is a learning curve involved in making an
ideal patch submission. However for the best results you should
proactively respond to suggestions with changes or justifications for
your current approach.

Some areas of code that are well maintained may review patches
quickly, lesser-loved areas of code may have a longer delay.

### [Stay around to fix problems raised in code review](submitting-a-patch.md#id55)

Not many patches get into QEMU straight away – it is quite common that
developers will identify bugs, or suggest a cleaner approach, or even
just point out code style issues or commit message typos. You’ll need to
respond to these, and then send a second version of your patches with
the issues fixed. This takes a little time and effort on your part, but
if you don’t do it then your changes will never get into QEMU.

Remember that a maintainer is under no obligation to take your
patches. If someone has spent the time reviewing your code and
suggesting improvements and you simply re-post without either
addressing the comment directly or providing additional justification
for the change then it becomes wasted effort. You cannot demand others
merge and then fix up your code after the fact.

When replying to comments on your patches **reply to all and not just
the sender** – keeping discussion on the mailing list means everybody
can follow it. Remember the spirit of the [Code of Conduct](code-of-conduct.md#code-of-conduct) and
keep discussions respectful and collaborative and avoid making
personal comments.

### [Pay attention to review comments](submitting-a-patch.md#id56)

Someone took their time to review your work, and it pays to respect that
effort; repeatedly submitting a series without addressing all comments
from the previous round tends to alienate reviewers and stall your
patch. Reviewers aren’t always perfect, so it is okay if you want to
argue that your code was correct in the first place instead of blindly
doing everything the reviewer asked. On the other hand, if someone
pointed out a potential issue during review, then even if your code
turns out to be correct, it’s probably a sign that you should improve
your commit message and/or comments in the code explaining why the code
is correct.

If you fix issues that are raised during review **resend the entire
patch series** not just the one patch that was changed. This allows
maintainers to easily apply the fixed series without having to manually
identify which patches are relevant. Send the new version as a complete
fresh email or series of emails – don’t try to make it a followup to
version 1. (This helps automatic patch email handling tools distinguish
between v1 and v2 emails.)

### [When resending patches add a version tag](submitting-a-patch.md#id57)

All patches beyond the first version should include a version tag – for
example, “[PATCH v2]”. This means people can easily identify whether
they’re looking at the most recent version. (The first version of a
patch need not say “v1”, just [PATCH] is sufficient.) For patch series,
the version applies to the whole series – even if you only change one
patch, you resend the entire series and mark it as “v2”. Don’t try to
track versions of different patches in the series separately. [git
format-patch](http://git-scm.com/docs/git-format-patch) and [git
send-email](http://git-scm.com/docs/git-send-email) both understand
the `-v2` option to make this easier. Send each new revision as a new
top-level thread, rather than burying it in-reply-to an earlier
revision, as many reviewers are not looking inside deep threads for new
patches.

### [Include version history in patchset revisions](submitting-a-patch.md#id58)

For later versions of patches, include a summary of changes from
previous versions, but not in the commit message itself. In an email
formatted as a git patch, the commit message is the part above the `---`
line, and this will go into the git changelog when the patch is
committed. This part should be a self-contained description of what this
version of the patch does, written to make sense to anybody who comes
back to look at this commit in git in six months’ time. The part below
the `---` line and above the patch proper (git format-patch puts the
diffstat here) is a good place to put remarks for people reading the
patch email, and this is where the “changes since previous version”
summary belongs. The [git-publish](https://github.com/stefanha/git-publish) script can help with
tracking a good summary across versions. Also, the [git-backport-diff](https://github.com/codyprime/git-scripts) script can help focus
reviewers on what changed between revisions. The `b4` tool automatically
generates a version history section in the cover letter, including links to the
previous versions on [Lore](https://lore.kernel.org/).

## [Tips and Tricks](submitting-a-patch.md#id59)

### [Proper use of Reviewed-by: tags can aid review](submitting-a-patch.md#id60)

When reviewing a large series, a reviewer can reply to some of the
patches with a Reviewed-by tag, stating that they are happy with that
patch in isolation (sometimes conditional on minor cleanup, like fixing
whitespace, that doesn’t affect code content). You should then update
those commit messages by hand to include the Reviewed-by tag, so that in
the next revision, reviewers can spot which patches were already clean
from the previous round. Conversely, if you significantly modify a patch
that was previously reviewed, remove the reviewed-by tag out of the
commit message, as well as listing the changes from the previous
version, to make it easier to focus a reviewer’s attention to your
changes.

### [If your patch seems to have been ignored](submitting-a-patch.md#id61)

If your patchset has received no replies you should “ping” it after a
week or two, by sending an email as a reply-to-all to the patch mail,
including the word “ping” and ideally also a link to the page for the
patch on [patchew](https://patchew.org/QEMU/) or
[lore.kernel.org](https://lore.kernel.org/qemu-devel/). It’s worth
double-checking for reasons why your patch might have been ignored
(forgot to CC the maintainer? annoyed people by failing to respond to
review comments on an earlier version?), but often for less-maintained
areas of QEMU patches do just slip through the cracks. If your ping is
also ignored, ping again after another week or so. As the submitter, you
are the person with the most motivation to get your patch applied, so
you have to be persistent.

### [Is my patch in?](submitting-a-patch.md#id62)

QEMU has some Continuous Integration machines that try to catch patch
submission problems as soon as possible. [patchew](http://patchew.org/QEMU/) includes a web interface for tracking the
status of various threads that have been posted to the list, and may
send you an automated mail if it detected a problem with your patch.

Once your patch has had enough review on list, the maintainer for that
area of code will send notification to the list that they are including
your patch in a particular staging branch. Periodically, the maintainer
then takes care of [Submitting a Pull Request](submitting-a-pull-request.md#submitting-a-pull-request)
for aggregating topic branches into mainline QEMU. Generally, you do not
need to send a pull request unless you have contributed enough patches
to become a maintainer over a particular section of code. Maintainers
may further modify your commit, by resolving simple merge conflicts or
fixing minor typos pointed out during review, but will always add a
Signed-off-by line in addition to yours, indicating that it went through
their tree. Occasionally, the maintainer’s pull request may hit more
difficult merge conflicts, where you may be requested to help rebase and
resolve the problems. It may take a couple of weeks between when your
patch first had a positive review to when it finally lands in qemu.git;
release cycle freezes may extend that time even longer.

### [Return the favor](submitting-a-patch.md#id63)

Peer review only works if everyone chips in a bit of review time. If
everyone submitted more patches than they reviewed, we would have a
patch backlog. A good goal is to try to review at least as many patches
from others as what you submit. Don’t worry if you don’t know the code
base as well as a maintainer; it’s perfectly fine to admit when your
review is weak because you are unfamiliar with the code.
