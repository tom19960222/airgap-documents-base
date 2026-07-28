---
collection: ansible
version: "6"
title: "ansible.builtin.git module – Deploy software (or files) from git checkouts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/git_module.html
fetched_at: 2026-07-27T16:44:02+00:00
---
# ansible.builtin.git module – Deploy software (or files) from git checkouts

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `git` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](git_module.md#synopsis)
- [Requirements](git_module.md#requirements)
- [Parameters](git_module.md#parameters)
- [Attributes](git_module.md#attributes)
- [Notes](git_module.md#notes)
- [Examples](git_module.md#examples)
- [Return Values](git_module.md#return-values)

## [Synopsis](git_module.md#id1)

- Manage *git* checkouts of repositories to deploy files or software.

## [Requirements](git_module.md#id2)

The below requirements are needed on the host that executes this module.

- git>=1.7.1 (the command line tool)

## [Parameters](git_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **accept_hostkey**  boolean | Will ensure or not that “-o StrictHostKeyChecking=no” is present as an ssh option.  Be aware that this disables a protection against MITM attacks.  Those using OpenSSH >= 7.5 might want to set *ssh_opt* to ‘StrictHostKeyChecking=accept-new’ instead, it does not remove the MITM issue but it does restrict it to the first attempt.  Choices:   - `false` ← (default) - `true` |
| **accept_newhostkey**  boolean  added in ansible-core 2.12 | As of OpenSSH 7.5, “-o StrictHostKeyChecking=accept-new” can be used which is safer and will only accepts host keys which are not present or are the same. if `yes`, ensure that “-o StrictHostKeyChecking=accept-new” is present as an ssh option.  Choices:   - `false` ← (default) - `true` |
| **archive**  path | Specify archive file path with extension. If specified, creates an archive file of the specified format containing the tree structure for the source tree. Allowed archive formats [“zip”, “tar.gz”, “tar”, “tgz”].  This will clone and perform git archive from local directory as not all git servers support git archive. |
| **archive_prefix**  string  added in ansible-base 2.10 | Specify a prefix to add to each file path in archive. Requires *archive* to be specified. |
| **bare**  boolean | If `yes`, repository will be created as a bare repo, otherwise it will be a standard repo with a workspace.  Choices:   - `false` ← (default) - `true` |
| **clone**  boolean | If `no`, do not clone the repository even if it does not exist locally.  Choices:   - `false` - `true` ← (default) |
| **depth**  integer | Create a shallow clone with a history truncated to the specified number or revisions. The minimum possible value is `1`, otherwise ignored. Needs *git>=1.9.1* to work correctly. |
| **dest**  path / required | The path of where the repository should be checked out. This is equivalent to `git clone [repo_url] [directory]`. The repository named in *repo* is not appended to this path and the destination directory must be empty. This parameter is required, unless *clone* is set to `no`. |
| **executable**  path | Path to git executable to use. If not supplied, the normal mechanism for resolving binary paths will be used. |
| **force**  boolean | If `yes`, any modified files in the working repository will be discarded. Prior to 0.7, this was always `yes` and could not be disabled. Prior to 1.9, the default was `yes`.  Choices:   - `false` ← (default) - `true` |
| **gpg_whitelist**  list / elements=string  added in Ansible 2.9 | A list of trusted GPG fingerprints to compare to the fingerprint of the GPG-signed commit.  Only used when *verify_commit=yes*.  Use of this feature requires Git 2.6+ due to its reliance on git’s `--raw` flag to `verify-commit` and `verify-tag`.  Default: `[]` |
| **key_file**  path | Specify an optional private key file path, on the target host, to use for the checkout.  This ensures ‘IdentitiesOnly=yes’ is present in ssh_opts. |
| **recursive**  boolean | If `no`, repository will be cloned without the –recursive option, skipping sub-modules.  Choices:   - `false` - `true` ← (default) |
| **reference**  string | Reference repository (see “git clone –reference …”). |
| **refspec**  string | Add an additional refspec to be fetched. If version is set to a *SHA-1* not reachable from any branch or tag, this option may be necessary to specify the ref containing the *SHA-1*. Uses the same syntax as the `git fetch` command. An example value could be “refs/meta/config”. |
| **remote**  string | Name of the remote.  Default: `"origin"` |
| **repo**  aliases: name  string / required | git, SSH, or HTTP(S) protocol address of the git repository. |
| **separate_git_dir**  path  added in Ansible 2.7 | The path to place the cloned repository. If specified, Git repository can be separated from working tree. |
| **single_branch**  boolean  added in ansible-core 2.11 | Clone only the history leading to the tip of the specified revision.  Choices:   - `false` ← (default) - `true` |
| **ssh_opts**  string | Options git will pass to ssh when used as protocol, it works via `git`‘s GIT_SSH/GIT_SSH_COMMAND environment variables.  For older versions it appends GIT_SSH_OPTS (specific to this module) to the variables above or via a wrapper script.  Other options can add to this list, like *key_file* and *accept_hostkey*.  An example value could be “-o StrictHostKeyChecking=no” (although this particular option is better set by *accept_hostkey*).  The module ensures that ‘BatchMode=yes’ is always present to avoid prompts. |
| **track_submodules**  boolean | If `yes`, submodules will track the latest commit on their master branch (or other branch specified in .gitmodules). If `no`, submodules will be kept at the revision specified by the main project. This is equivalent to specifying the –remote flag to git submodule update.  Choices:   - `false` ← (default) - `true` |
| **umask**  any | The umask to set before doing any checkouts, or any other repository maintenance. |
| **update**  boolean | If `no`, do not retrieve new revisions from the origin repository.  Operations like archive will work on the existing (old) repository and might not respond to changes to the options version or remote.  Choices:   - `false` - `true` ← (default) |
| **verify_commit**  boolean | If `yes`, when cloning or checking out a *version* verify the signature of a GPG signed commit. This requires git version>=2.1.0 to be installed. The commit MUST be signed and the public key MUST be present in the GPG keyring.  Choices:   - `false` ← (default) - `true` |
| **version**  string | What version of the repository to check out. This can be the literal string `HEAD`, a branch name, a tag name. It can also be a *SHA-1* hash, in which case *refspec* needs to be specified if the given revision is not already available.  Default: `"HEAD"` |

## [Attributes](git_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | Support: full | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | Platform: posix | Target OS/families that can be operated against |

## [Notes](git_module.md#id5)

> **Note:**
>
> - If the task seems to be hanging, first verify remote host is in `known_hosts`. SSH will prompt user to authorize the first contact with a remote host. To avoid this prompt, one solution is to use the option accept_hostkey. Another solution is to add the remote host public key in `/etc/ssh/ssh_known_hosts` before calling the git module, with the following command: ssh-keyscan -H remote_host.com >> /etc/ssh/ssh_known_hosts.

## [Examples](git_module.md#id6)

```yaml+jinja
- name: Git checkout
  ansible.builtin.git:
    repo: 'https://foosball.example.org/path/to/repo.git'
    dest: /srv/checkout
    version: release-0.22

- name: Read-write git checkout from github
  ansible.builtin.git:
    repo: git@github.com:mylogin/hello.git
    dest: /home/mylogin/hello

- name: Just ensuring the repo checkout exists
  ansible.builtin.git:
    repo: 'https://foosball.example.org/path/to/repo.git'
    dest: /srv/checkout
    update: no

- name: Just get information about the repository whether or not it has already been cloned locally
  ansible.builtin.git:
    repo: 'https://foosball.example.org/path/to/repo.git'
    dest: /srv/checkout
    clone: no
    update: no

- name: Checkout a github repo and use refspec to fetch all pull requests
  ansible.builtin.git:
    repo: https://github.com/ansible/ansible-examples.git
    dest: /src/ansible-examples
    refspec: '+refs/pull/*:refs/heads/*'

- name: Create git archive from repo
  ansible.builtin.git:
    repo: https://github.com/ansible/ansible-examples.git
    dest: /src/ansible-examples
    archive: /tmp/ansible-examples.zip

- name: Clone a repo with separate git directory
  ansible.builtin.git:
    repo: https://github.com/ansible/ansible-examples.git
    dest: /src/ansible-examples
    separate_git_dir: /src/ansible-examples.git

- name: Example clone of a single branch
  ansible.builtin.git:
    repo: https://github.com/ansible/ansible-examples.git
    dest: /src/ansible-examples
    single_branch: yes
    version: master

- name: Avoid hanging when http(s) password is missing
  ansible.builtin.git:
    repo: https://github.com/ansible/could-be-a-private-repo
    dest: /src/from-private-repo
  environment:
    GIT_TERMINAL_PROMPT: 0 # reports "terminal prompts disabled" on missing password
    # or GIT_ASKPASS: /bin/true # for git before version 2.3.0, reports "Authentication failed" on missing password
```

## [Return Values](git_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  string | Last commit revision of the repository retrieved during the update.  Returned: success  Sample: `"4c020102a9cd6fe908c9a4a326a38f972f63a903"` |
| **before**  string | Commit revision before the repository was updated, “null” for new repository.  Returned: success  Sample: `"67c04ebe40a003bda0efb34eacfb93b0cafdf628"` |
| **git_dir_before**  string | Contains the original path of .git directory if it is changed.  Returned: success  Sample: `"/path/to/old/git/dir"` |
| **git_dir_now**  string | Contains the new path of .git directory if it is changed.  Returned: success  Sample: `"/path/to/new/git/dir"` |
| **remote_url_changed**  boolean | Contains True or False whether or not the remote URL was changed.  Returned: success  Sample: `true` |
| **warnings**  string | List of warnings if requested features were not available due to a too old git version.  Returned: error  Sample: `"git version is too old to fully support the depth argument. Falling back to full checkouts."` |

### Authors

- Ansible Core Team
- Michael DeHaan

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
