---
collection: qemu
version: "11.1.0"
title: "Continuous Integration (CI)"
source_url: https://www.qemu.org/docs/master/devel/testing/ci.html
fetched_at: 2026-08-21T03:25:44+00:00
---
# Continuous Integration (CI)

Continuous integration (CI) requires the builds of the entire application and
the execution of a comprehensive set of automated tests every time there is a
need to commit any set of changes [[1]](ci.md#id3). The automated tests are composed
of unit, functional and other tests.

Most of QEMU’s CI is run on GitLab’s infrastructure although a number
of other CI services are used for specialised purposes. The most up to
date information about them and their status can be found on the
[project wiki testing page](https://wiki.qemu.org/Testing/CI).

These tests are also used as gating tests before merging pull requests.
A gating test restricts the move of code from one stage to another on a
test/deployment pipeline. The step move is granted with approval. The approval
can be a manual intervention or a set of tests succeeding [[2]](ci.md#id4).

On QEMU, the gating process happens during the pull request. The approval is
done by the project leader running its own set of tests. The pull request gets
merged when the tests succeed.

# Custom CI/CD variables

QEMU CI pipelines can be tuned by setting some CI environment variables.

## Set variable globally in the user’s CI namespace

Variables can be set globally in the user’s CI namespace setting.

For further information about how to set these variables, please refer to:

```
https://docs.gitlab.com/ee/ci/variables/#add-a-cicd-variable-to-a-project
```

## Set variable manually when pushing a branch or tag to the user’s repository

Variables can be set manually when pushing a branch or tag, using
git-push command line arguments.

Example setting the QEMU_CI_EXAMPLE_VAR variable:

```
git push -o ci.variable="QEMU_CI_EXAMPLE_VAR=value" myrepo mybranch
```

For further information about how to set these variables, please refer to:

```
https://docs.gitlab.com/ee/user/project/push_options.html#push-options-for-gitlab-cicd
```

## Setting aliases in your git config

You can use aliases to make it easier to push branches with different
CI configurations. For example define an alias for triggering CI:

```
git config --local alias.push-ci "push -o ci.variable=QEMU_CI=1"
git config --local alias.push-ci-now "push -o ci.variable=QEMU_CI=2"
```

Which lets you run:

```
git push-ci
```

to create the pipeline, or:

```
git push-ci-now
```

to create and run the pipeline

## Variable naming and grouping

The variables used by QEMU’s CI configuration are grouped together
in a handful of namespaces

> - QEMU_JOB_nnnn - variables to be defined in individual jobs
>   or templates, to influence the shared rules defined in the
>   .base_job_template.
> - QEMU_CI_nnn - variables to be set by contributors in their
>   repository CI settings, or as git push variables, to influence
>   which jobs get run in a pipeline
> - QEMU_CI_CONTAINER_TAG - the tag used to publish containers
>   in stage 1, for use by build jobs in stage 2. Defaults to
>   ‘latest’, but if running pipelines for different branches
>   concurrently, it should be overridden per pipeline.
> - QEMU_CI_UPSTREAM - gitlab namespace that is considered to be
>   the ‘upstream’. This defaults to ‘qemu-project’. Contributors
>   may choose to override this if they are modifying rules in
>   base.yml and need to validate how they will operate when in
>   an upstream context, as opposed to their fork context.
> - nnn - other misc variables not falling into the above
>   categories, or using different names for historical reasons
>   and not yet converted.

## Maintainer controlled job variables

The following variables may be set when defining a job in the
CI configuration file.

### QEMU_JOB_OPTIONAL

The job is expected to be successful in general, but is not run
by default due to need to conserve limited CI resources. It is
available to be started manually by the contributor in the CI
pipelines UI.

### QEMU_JOB_ONLY_FORKS

The job results are only of interest to contributors prior to
submitting code. They are not required as part of the gating
CI pipeline.

### QEMU_JOB_SKIPPED

The job is not reliably successful in general, so is not
currently suitable to be run by default. Ideally this should
be a temporary marker until the problems can be addressed, or
the job permanently removed.

### QEMU_JOB_PUBLISH

The job is for publishing content after a branch has been
merged into the upstream default branch.

### QEMU_JOB_FUNCTIONAL

The job runs the functional test suite

### QEMU_JOB_MACOS

The job requires access to the macOS shared runners, which are
only available to Premium/Ultimate tiers. This includes OSS project
members, but not forks.

## Contributor controlled runtime variables

The following variables may be set by contributors to control
job execution

### QEMU_CI

By default, no pipelines will be created on contributor forks
in order to preserve CI credits

Set this variable to 1 to create the pipelines, but leave all
the jobs to be manually started from the UI

Set this variable to 2 to create the pipelines and run all
the jobs immediately, as was the historical behaviour

### QEMU_CI_FUNCTIONAL

By default, tests using the functional framework are not run automatically
in the pipelines (because multiple artifacts have to be downloaded, which
might cause a lot of network traffic). Set this variable to have the tests
using the functional framework run automatically.

## Other misc variables

These variables are primarily to control execution of jobs on
private runners

### AARCH64_RUNNER_AVAILABLE

If you’ve got access to an aarch64 host that can be used as a gitlab-CI
runner, you can set this variable to enable the tests that require this
kind of host. The runner should be tagged with “aarch64”.

### S390X_RUNNER_AVAILABLE

If you’ve got access to an IBM Z host that can be used as a gitlab-CI
runner, you can set this variable to enable the tests that require this
kind of host. The runner should be tagged with “s390x”.

### PPC64LE_RUNNER_AVAILABLE

If you’ve got access to an PPC64LE host that can be used as a gitlab-CI
runner, you can set this variable to enable the tests that require this
kind of host. The runner should be tagged with “ppc64le”.

### CCACHE_DISABLE

The jobs are configured to use “ccache” by default since this typically
reduces compilation time, at the cost of increased storage. If the
use of “ccache” is suspected to be hurting the overall job execution
time, setting the “CCACHE_DISABLE=1” env variable to disable it.

# Jobs on Custom Runners

Besides the jobs run under the various CI systems listed before, there
are a number additional jobs that will run before an actual merge.
These use the same GitLab CI’s service/framework already used for all
other GitLab based CI jobs, but rely on additional systems, not the
ones provided by GitLab as “shared runners”.

The architecture of GitLab’s CI service allows different machines to
be set up with GitLab’s “agent”, called gitlab-runner, which will take
care of running jobs created by events such as a push to a branch.
Here, the combination of a machine, properly configured with GitLab’s
gitlab-runner, is called a “custom runner”.

The GitLab CI jobs definition for the custom runners are located under:

```
.gitlab-ci.d/custom-runners.yml
```

Custom runners entail custom machines. To see a list of the machines
currently deployed in the QEMU GitLab CI and their maintainers, please
refer to the QEMU [wiki](https://wiki.qemu.org/AdminContacts).

## Machine Setup Howto

For all Linux based systems, the setup can be mostly automated by the
execution of two Ansible playbooks. Create an `inventory` file
under `scripts/ci/setup`, such as this:

```
fully.qualified.domain
other.machine.hostname
```

You may need to set some variables in the inventory file itself. One
very common need is to tell Ansible to use a Python 3 interpreter on
those hosts. This would look like:

```
fully.qualified.domain ansible_python_interpreter=/usr/bin/python3
other.machine.hostname ansible_python_interpreter=/usr/bin/python3
```

### Build environment

The `scripts/ci/setup/$DISTRO/build-environment.yml` Ansible
playbook will set up machines with the environment needed to perform
builds and run QEMU tests. This playbook consists on the installation
of various required packages (and a general package update while at
it).

The minimum required version of Ansible successfully tested in this
playbook is 2.8.0 (a version check is embedded within the playbook
itself). To run the playbook, execute:

```
cd scripts/ci/setup
ansible-playbook -i inventory $DISTRO/build-environment.yml
```

Please note that most of the tasks in the playbook require superuser
privileges, such as those from the `root` account or those obtained
by `sudo`. If necessary, please refer to `ansible-playbook`
options such as `--become`, `--become-method`, `--become-user`
and `--ask-become-pass`.

### gitlab-runner setup and registration

The gitlab-runner agent needs to be installed on each machine that
will run jobs. The association between a machine and a GitLab project
happens with a registration token. To find the registration token for
your repository/project, navigate on GitLab’s web UI to:

> - Settings (the gears-like icon at the bottom of the left hand side
>   vertical toolbar), then
> - CI/CD, then
> - Runners, and click on the “Expand” button, then
> - Under “Set up a specific Runner manually”, look for the value under
>   “And this registration token:”

Copy the `scripts/ci/setup/vars.yml.template` file to
`scripts/ci/setup/vars.yml`. Then, set the
`gitlab_runner_registration_token` variable to the value obtained
earlier.

To run the playbook, execute:

```
cd scripts/ci/setup
ansible-playbook -i inventory gitlab-runner.yml
```

Following the registration, it’s necessary to configure the runner tags,
and optionally other configurations on the GitLab UI. Navigate to:

> - Settings (the gears like icon), then
> - CI/CD, then
> - Runners, and click on the “Expand” button, then
> - “Runners activated for this project”, then
> - Click on the “Edit” icon (next to the “Lock” Icon)

Tags are very important as they are used to route specific jobs to
specific types of runners, so it’s a good idea to double check that
the automatically created tags are consistent with the OS and
architecture. For instance, an Ubuntu 20.04 aarch64 system should
have tags set as:

```
ubuntu_20.04,aarch64
```

Because the job definition at `.gitlab-ci.d/custom-runners.yml`
would contain:

```
ubuntu-20.04-aarch64-all:
 tags:
 - ubuntu_20.04
 - aarch64
```

It’s also recommended to:

> - increase the “Maximum job timeout” to something like `2h`
> - give it a better Description

## References

[[1](ci.md#id1)]

Humble, Jez & Farley, David (2010). Continuous Delivery:
Reliable Software Releases Through Build, Test, and Deployment, p. 55.

[[2](ci.md#id2)]

Humble, Jez & Farley, David (2010). Continuous Delivery:
Reliable Software Releases Through Build, Test, and Deployment, p. 122.
