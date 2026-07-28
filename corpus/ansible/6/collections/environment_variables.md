---
collection: ansible
version: "6"
title: "Index of all Collection Environment Variables"
source_url: https://docs.ansible.com/projects/ansible/6/collections/environment_variables.html
fetched_at: 2026-07-28T00:24:25+00:00
---
# Index of all Collection Environment Variables

The following index documents all environment variables declared by plugins in collections.
Environment variables used by the ansible-core configuration are documented in [Ansible Configuration Settings](../reference_appendices/config.md#ansible-configuration-settings).

AIM_CLIPASSWORDSDK_CMD
:   Cyberark CLI utility.

    *Used by:*
    [community.general.cyberarkpassword lookup plugin](community/general/cyberarkpassword_lookup.md#ansible-collections-community-general-cyberarkpassword-lookup)

ANSIBLE_ADMIN_USERS
:   list of users to be expected to have admin privileges. This is used by the controller to determine how to share temporary files between the remote user and the become user.

    *Used by:*
    [ansible.builtin.sh shell plugin](ansible/builtin/sh_shell.md#ansible-collections-ansible-builtin-sh-shell),
    [ansible.posix.csh shell plugin](ansible/posix/csh_shell.md#ansible-collections-ansible-posix-csh-shell),
    [ansible.posix.fish shell plugin](ansible/posix/fish_shell.md#ansible-collections-ansible-posix-fish-shell)

ANSIBLE_ASYNC_DIR
:   Directory in which ansible will keep async job information

    *Used by:*
    [ansible.builtin.sh shell plugin](ansible/builtin/sh_shell.md#ansible-collections-ansible-builtin-sh-shell),
    [ansible.posix.csh shell plugin](ansible/posix/csh_shell.md#ansible-collections-ansible-posix-csh-shell),
    [ansible.posix.fish shell plugin](ansible/posix/fish_shell.md#ansible-collections-ansible-posix-fish-shell)

ANSIBLE_BECOME_PASS
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [ansible.builtin.runas become plugin](ansible/builtin/runas_become.md#ansible-collections-ansible-builtin-runas-become),
    [ansible.builtin.su become plugin](ansible/builtin/su_become.md#ansible-collections-ansible-builtin-su-become),
    [ansible.builtin.sudo become plugin](ansible/builtin/sudo_become.md#ansible-collections-ansible-builtin-sudo-become),
    [ansible.netcommon.enable become plugin](ansible/netcommon/enable_become.md#ansible-collections-ansible-netcommon-enable-become),
    [community.general.doas become plugin](community/general/doas_become.md#ansible-collections-community-general-doas-become),
    [community.general.dzdo become plugin](community/general/dzdo_become.md#ansible-collections-community-general-dzdo-become),
    [community.general.ksu become plugin](community/general/ksu_become.md#ansible-collections-community-general-ksu-become),
    [community.general.machinectl become plugin](community/general/machinectl_become.md#ansible-collections-community-general-machinectl-become),
    [community.general.pbrun become plugin](community/general/pbrun_become.md#ansible-collections-community-general-pbrun-become),
    [community.general.pfexec become plugin](community/general/pfexec_become.md#ansible-collections-community-general-pfexec-become),
    [community.general.pmrun become plugin](community/general/pmrun_become.md#ansible-collections-community-general-pmrun-become),
    [community.general.sesu become plugin](community/general/sesu_become.md#ansible-collections-community-general-sesu-become),
    [community.general.sudosu become plugin](community/general/sudosu_become.md#ansible-collections-community-general-sudosu-become),
    [containers.podman.podman_unshare become plugin](containers/podman/podman_unshare_become.md#ansible-collections-containers-podman-podman-unshare-become)

ANSIBLE_CACHE_REDIS_KEYSET_NAME
:   User defined name for cache keyset name.

    *Used by:*
    [community.general.redis cache plugin](community/general/redis_cache.md#ansible-collections-community-general-redis-cache)

ANSIBLE_CACHE_REDIS_SENTINEL
:   The redis sentinel service name (or referenced as cluster name).

    *Used by:*
    [community.general.redis cache plugin](community/general/redis_cache.md#ansible-collections-community-general-redis-cache)

ANSIBLE_CALLBACK_DIY_ON_ANY_MSG
:   Output to be used for callback on_any.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_ON_ANY_MSG_COLOR
:   Output color to be used for *on_any_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_ON_FILE_DIFF_MSG
:   Output to be used for callback on_file_diff.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_ON_FILE_DIFF_MSG_COLOR
:   Output color to be used for *on_file_diff_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_HANDLER_TASK_START_MSG
:   Output to be used for callback playbook_on_handler_task_start.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_HANDLER_TASK_START_MSG_COLOR
:   Output color to be used for *playbook_on_handler_task_start_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_INCLUDE_MSG
:   Output to be used for callback playbook_on_include.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_INCLUDE_MSG_COLOR
:   Output color to be used for *playbook_on_include_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_NO_HOSTS_MATCHED_MSG
:   Output to be used for callback playbook_on_no_hosts_matched.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_NO_HOSTS_MATCHED_MSG_COLOR
:   Output color to be used for *playbook_on_no_hosts_matched_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_NO_HOSTS_REMAINING_MSG
:   Output to be used for callback playbook_on_no_hosts_remaining.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_NO_HOSTS_REMAINING_MSG_COLOR
:   Output color to be used for *playbook_on_no_hosts_remaining_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_NOTIFY_MSG
:   Output to be used for callback playbook_on_notify.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_NOTIFY_MSG_COLOR
:   Output color to be used for *playbook_on_notify_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_PLAY_START_MSG
:   Output to be used for callback playbook_on_play_start.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_PLAY_START_MSG_COLOR
:   Output color to be used for *playbook_on_play_start_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_SETUP_MSG
:   Output to be used for callback playbook_on_setup.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_SETUP_MSG_COLOR
:   Output color to be used for *playbook_on_setup_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_START_MSG
:   Output to be used for callback playbook_on_start.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_START_MSG_COLOR
:   Output color to be used for *playbook_on_start_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_STATS_MSG
:   Output to be used for callback playbook_on_stats.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_STATS_MSG_COLOR
:   Output color to be used for *playbook_on_stats_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_TASK_START_MSG
:   Output to be used for callback playbook_on_task_start.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_TASK_START_MSG_COLOR
:   Output color to be used for *playbook_on_task_start_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_VARS_PROMPT_MSG
:   Output to be used for callback playbook_on_vars_prompt.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_VARS_PROMPT_MSG_COLOR
:   Output color to be used for *playbook_on_vars_prompt_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_ITEM_ON_FAILED_MSG
:   Output to be used for callback runner_item_on_failed.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_ITEM_ON_FAILED_MSG_COLOR
:   Output color to be used for *runner_item_on_failed_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_ITEM_ON_OK_MSG
:   Output to be used for callback runner_item_on_ok.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_ITEM_ON_OK_MSG_COLOR
:   Output color to be used for *runner_item_on_ok_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_ITEM_ON_SKIPPED_MSG
:   Output to be used for callback runner_item_on_skipped.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_ITEM_ON_SKIPPED_MSG_COLOR
:   Output color to be used for *runner_item_on_skipped_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_ON_FAILED_MSG
:   Output to be used for callback runner_on_failed.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_ON_FAILED_MSG_COLOR
:   Output color to be used for *runner_on_failed_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_ON_NO_HOSTS_MSG
:   Output to be used for callback runner_on_no_hosts.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_ON_NO_HOSTS_MSG_COLOR
:   Output color to be used for *runner_on_no_hosts_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_ON_OK_MSG
:   Output to be used for callback runner_on_ok.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_ON_OK_MSG_COLOR
:   Output color to be used for *runner_on_ok_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_ON_SKIPPED_MSG
:   Output to be used for callback runner_on_skipped.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_ON_SKIPPED_MSG_COLOR
:   Output color to be used for *runner_on_skipped_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_ON_START_MSG
:   Output to be used for callback runner_on_start.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_ON_START_MSG_COLOR
:   Output color to be used for *runner_on_start_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_ON_UNREACHABLE_MSG
:   Output to be used for callback runner_on_unreachable.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_ON_UNREACHABLE_MSG_COLOR
:   Output color to be used for *runner_on_unreachable_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_RETRY_MSG
:   Output to be used for callback runner_retry.

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_DIY_RUNNER_RETRY_MSG_COLOR
:   Output color to be used for *runner_retry_msg*.

    Template should render a [valid color value](environment_variables.md#notes).

    *Used by:*
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback)

ANSIBLE_CALLBACK_FORMAT_PRETTY
:   Configure the result format to be more readable

    When the result format is set to `yaml` this option defaults to `True`, and defaults to `False` when configured to `json`.

    Setting this option to `True` will force `json` and `yaml` results to always be pretty printed regardless of verbosity.

    When set to `True` and used with the `yaml` result format, this option will modify module responses in an attempt to produce a more human friendly output at the expense of correctness, and should not be relied upon to aid in writing variable manipulations or conditionals. For correctness, set this option to `False` or set the result format to `json`.

    *Used by:*
    [ansible.builtin.default callback plugin](ansible/builtin/default_callback.md#ansible-collections-ansible-builtin-default-callback),
    [ansible.builtin.minimal callback plugin](ansible/builtin/minimal_callback.md#ansible-collections-ansible-builtin-minimal-callback)

ANSIBLE_CALLBACK_RESULT_FORMAT
:   Define the task result format used in the callback output.

    These formats do not cause the callback to emit valid JSON or YAML formats.

    The output contains these formats interspersed with other non-machine parsable data.

    *Used by:*
    [ansible.builtin.default callback plugin](ansible/builtin/default_callback.md#ansible-collections-ansible-builtin-default-callback),
    [ansible.builtin.minimal callback plugin](ansible/builtin/minimal_callback.md#ansible-collections-ansible-builtin-minimal-callback)

ANSIBLE_CALLBACK_TREE_DIR
:   directory that will contain the per host JSON files. Also set by the `--tree` option when using adhoc.

    *Used by:*
    [ansible.builtin.tree callback plugin](ansible/builtin/tree_callback.md#ansible-collections-ansible-builtin-tree-callback)

ANSIBLE_CERTIFICATE_CHAIN_FILE
:   The PEM encoded certificate chain file used to create a SSL-enabled channel. If the value is None, no certificate chain is used.

    *Used by:*
    [ansible.netcommon.grpc connection plugin](ansible/netcommon/grpc_connection.md#ansible-collections-ansible-netcommon-grpc-connection)

ANSIBLE_CHECK_MODE_MARKERS
:   Toggle to control displaying markers when running in check mode.

    The markers are `DRY RUN` at the beginning and ending of playbook execution (when calling `ansible-playbook --check`) and `CHECK MODE` as a suffix at every play and task that is run in check mode.

    *Used by:*
    [ansible.builtin.default callback plugin](ansible/builtin/default_callback.md#ansible-collections-ansible-builtin-default-callback),
    [ansible.posix.debug callback plugin](ansible/posix/debug_callback.md#ansible-collections-ansible-posix-debug-callback),
    [ansible.posix.skippy callback plugin](ansible/posix/skippy_callback.md#ansible-collections-ansible-posix-skippy-callback),
    [community.general.counter_enabled callback plugin](community/general/counter_enabled_callback.md#ansible-collections-community-general-counter-enabled-callback),
    [community.general.dense callback plugin](community/general/dense_callback.md#ansible-collections-community-general-dense-callback),
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback),
    [community.general.unixy callback plugin](community/general/unixy_callback.md#ansible-collections-community-general-unixy-callback),
    [community.general.yaml callback plugin](community/general/yaml_callback.md#ansible-collections-community-general-yaml-callback)

ANSIBLE_CHROOT_EXE
:   User specified chroot binary

    *Used by:*
    [community.general.chroot connection plugin](community/general/chroot_connection.md#ansible-collections-community-general-chroot-connection)

ANSIBLE_COMMON_REMOTE_GROUP
:   Checked when Ansible needs to execute a module as a different user.

    If setfacl and chown both fail and do not let the different user access the module’s files, they will be chgrp’d to this group.

    In order for this to work, the remote_user and become_user must share a common group and this setting must be set to that group.

    *Used by:*
    [ansible.builtin.sh shell plugin](ansible/builtin/sh_shell.md#ansible-collections-ansible-builtin-sh-shell),
    [ansible.posix.csh shell plugin](ansible/posix/csh_shell.md#ansible-collections-ansible-posix-csh-shell),
    [ansible.posix.fish shell plugin](ansible/posix/fish_shell.md#ansible-collections-ansible-posix-fish-shell)

ANSIBLE_CONSUL_CLIENT_CERT
:   The client cert to verify the ssl connection.

    *Used by:*
    [community.general.consul_kv lookup plugin](community/general/consul_kv_lookup.md#ansible-collections-community-general-consul-kv-lookup)

ANSIBLE_CONSUL_URL
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [community.general.consul_kv lookup plugin](community/general/consul_kv_lookup.md#ansible-collections-community-general-consul-kv-lookup)

ANSIBLE_CONSUL_VALIDATE_CERTS
:   Whether to verify the ssl connection or not.

    *Used by:*
    [community.general.consul_kv lookup plugin](community/general/consul_kv_lookup.md#ansible-collections-community-general-consul-kv-lookup)

ANSIBLE_DISPLAY_FAILED_STDERR
:   Toggle to control whether failed and unreachable tasks are displayed to STDERR (vs. STDOUT)

    *Used by:*
    [ansible.builtin.default callback plugin](ansible/builtin/default_callback.md#ansible-collections-ansible-builtin-default-callback),
    [ansible.posix.debug callback plugin](ansible/posix/debug_callback.md#ansible-collections-ansible-posix-debug-callback),
    [ansible.posix.skippy callback plugin](ansible/posix/skippy_callback.md#ansible-collections-ansible-posix-skippy-callback),
    [community.general.counter_enabled callback plugin](community/general/counter_enabled_callback.md#ansible-collections-community-general-counter-enabled-callback),
    [community.general.dense callback plugin](community/general/dense_callback.md#ansible-collections-community-general-dense-callback),
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback),
    [community.general.unixy callback plugin](community/general/unixy_callback.md#ansible-collections-community-general-unixy-callback),
    [community.general.yaml callback plugin](community/general/yaml_callback.md#ansible-collections-community-general-yaml-callback)

ANSIBLE_DISPLAY_OK_HOSTS
:   Toggle to control displaying ‘ok’ task/host results in a task

    *Used by:*
    [ansible.builtin.default callback plugin](ansible/builtin/default_callback.md#ansible-collections-ansible-builtin-default-callback),
    [ansible.posix.debug callback plugin](ansible/posix/debug_callback.md#ansible-collections-ansible-posix-debug-callback),
    [ansible.posix.skippy callback plugin](ansible/posix/skippy_callback.md#ansible-collections-ansible-posix-skippy-callback),
    [community.general.counter_enabled callback plugin](community/general/counter_enabled_callback.md#ansible-collections-community-general-counter-enabled-callback),
    [community.general.dense callback plugin](community/general/dense_callback.md#ansible-collections-community-general-dense-callback),
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback),
    [community.general.unixy callback plugin](community/general/unixy_callback.md#ansible-collections-community-general-unixy-callback),
    [community.general.yaml callback plugin](community/general/yaml_callback.md#ansible-collections-community-general-yaml-callback)

ANSIBLE_DOAS_EXE
:   Doas executable

    *Used by:*
    [community.general.doas become plugin](community/general/doas_become.md#ansible-collections-community-general-doas-become)

ANSIBLE_DOAS_FLAGS
:   Options to pass to doas

    *Used by:*
    [community.general.doas become plugin](community/general/doas_become.md#ansible-collections-community-general-doas-become)

ANSIBLE_DOAS_PASS
:   password for doas prompt

    *Used by:*
    [community.general.doas become plugin](community/general/doas_become.md#ansible-collections-community-general-doas-become)

ANSIBLE_DOAS_PROMPT_L10N
:   List of localized strings to match for prompt detection

    If empty we’ll use the built in one

    *Used by:*
    [community.general.doas become plugin](community/general/doas_become.md#ansible-collections-community-general-doas-become)

ANSIBLE_DOAS_USER
:   User you ‘become’ to execute the task

    *Used by:*
    [community.general.doas become plugin](community/general/doas_become.md#ansible-collections-community-general-doas-become)

ANSIBLE_DOCKER_TIMEOUT
:   Controls how long we can wait to access reading output from the container once execution started.

    *Used by:*
    [community.docker.docker connection plugin](community/docker/docker_connection.md#ansible-collections-community-docker-docker-connection),
    [community.docker.docker_api connection plugin](community/docker/docker_api_connection.md#ansible-collections-community-docker-docker-api-connection)

ANSIBLE_DZDO_EXE
:   Dzdo executable

    *Used by:*
    [community.general.dzdo become plugin](community/general/dzdo_become.md#ansible-collections-community-general-dzdo-become)

ANSIBLE_DZDO_FLAGS
:   Options to pass to dzdo

    *Used by:*
    [community.general.dzdo become plugin](community/general/dzdo_become.md#ansible-collections-community-general-dzdo-become)

ANSIBLE_DZDO_PASS
:   Options to pass to dzdo

    *Used by:*
    [community.general.dzdo become plugin](community/general/dzdo_become.md#ansible-collections-community-general-dzdo-become)

ANSIBLE_DZDO_USER
:   User you ‘become’ to execute the task

    *Used by:*
    [community.general.dzdo become plugin](community/general/dzdo_become.md#ansible-collections-community-general-dzdo-become)

ANSIBLE_ENABLE_PASS
:   password

    *Used by:*
    [ansible.netcommon.enable become plugin](ansible/netcommon/enable_become.md#ansible-collections-ansible-netcommon-enable-become)

ANSIBLE_EOS_USE_SESSIONS
:   Specifies if sessions should be used on remote host or not

    *Used by:*
    [arista.eos.eos cliconf plugin](arista/eos/eos_cliconf.md#ansible-collections-arista-eos-eos-cliconf),
    [arista.eos.eos httpapi plugin](arista/eos/eos_httpapi.md#ansible-collections-arista-eos-eos-httpapi)

ANSIBLE_ETCD_URL
:   Environment variable with the url for the etcd server

    *Used by:*
    [community.general.etcd lookup plugin](community/general/etcd_lookup.md#ansible-collections-community-general-etcd-lookup)

ANSIBLE_ETCD_VERSION
:   Environment variable with the etcd protocol version

    *Used by:*
    [community.general.etcd lookup plugin](community/general/etcd_lookup.md#ansible-collections-community-general-etcd-lookup)

ANSIBLE_GPRC_SSL_TARGET_NAME_OVERRIDE
:   The option overrides SSL target name used for SSL host name checking. The name used for SSL host name checking will be the target parameter (assuming that the secure channel is an SSL channel). If this parameter is specified and the underlying is not an SSL channel, it will just be ignored.

    *Used by:*
    [ansible.netcommon.grpc connection plugin](ansible/netcommon/grpc_connection.md#ansible-collections-ansible-netcommon-grpc-connection)

ANSIBLE_GRPC_CONNECTION_TYPE
:   This option indicates the grpc type and it can be used in place of network_os. (example cisco.iosxr.iosxr)

    *Used by:*
    [ansible.netcommon.grpc connection plugin](ansible/netcommon/grpc_connection.md#ansible-collections-ansible-netcommon-grpc-connection)

ANSIBLE_HASHI_VAULT_ADDR
:   URL to the Vault service.

    If not specified by any other means, the value of the `VAULT_ADDR` environment variable will be used.

    If `VAULT_ADDR` is also not defined then an error will be raised.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_AUTH_METHOD
:   Authentication method to be used.

    `none` auth method was added in collection version `1.2.0`.

    `cert` auth method was added in collection version `1.4.0`.

    `aws_iam_login` was renamed `aws_iam` in collection version `2.1.0` and was removed in `3.0.0`.

    `azure` auth method was added in collection version `3.2.0`.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_AWS_IAM_SERVER_ID
:   If specified, sets the value to use for the `X-Vault-AWS-IAM-Server-ID` header as part of `GetCallerIdentity` request.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_AZURE_CLIENT_ID
:   The client ID (also known as application ID) of the Azure AD service principal or managed identity. Should be a UUID.

    If not specified, will use the system assigned managed identity.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_AZURE_CLIENT_SECRET
:   The client secret of the Azure AD service principal.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_AZURE_RESOURCE
:   The resource URL for the application registered in Azure Active Directory. Usually should not be changed from the default.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_AZURE_TENANT_ID
:   The Azure Active Directory Tenant ID (also known as the Directory ID) of the service principal. Should be a UUID.

    Required when using a service principal to authenticate to Vault, e.g. required when both *azure_client_id* and *azure_client_secret* are specified.

    Optional when using managed identity to authenticate to Vault.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_CA_CERT
:   Path to certificate to use for authentication.

    If not specified by any other means, the `VAULT_CACERT` environment variable will be used.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_CERT_AUTH_PRIVATE_KEY
:   For `cert` auth, path to the private key file to authenticate with, in PEM format.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_CERT_AUTH_PUBLIC_KEY
:   For `cert` auth, path to the certificate file to authenticate with, in PEM format.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_JWT
:   The JSON Web Token (JWT) to use for JWT authentication to Vault.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_MOUNT_POINT
:   Vault mount point.

    If not specified, the default mount point for a given auth method is used.

    Does not apply to token authentication.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_NAMESPACE
:   Vault namespace where secrets reside. This option requires HVAC 0.7.0+ and Vault 0.11+.

    Optionally, this may be achieved by prefixing the authentication mount point and/or secret path with the namespace (e.g `mynamespace/secret/mysecret`).

    If environment variable `VAULT_NAMESPACE` is set, its value will be used last among all ways to specify *namespace*.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_PASSWORD
:   Authentication password.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_PROXIES
:   URL(s) to the proxies used to access the Vault service.

    It can be a string or a dict.

    If it’s a dict, provide the scheme (eg. `http` or `https`) as the key, and the URL as the value.

    If it’s a string, provide a single URL that will be used as the proxy for both `http` and `https` schemes.

    A string that can be interpreted as a dictionary will be converted to one (see examples).

    You can specify a different proxy for HTTP and HTTPS resources.

    If not specified, [environment variables from the Requests library](https://requests.readthedocs.io/en/master/user/advanced/#proxies) are used.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_RETRIES
:   Allows for retrying on errors, based on the [Retry class in the urllib3 library](https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html#urllib3.util.Retry).

    This collection defines recommended defaults for retrying connections to Vault.

    This option can be specified as a positive number (integer) or dictionary.

    If this option is not specified or the number is `0`, then retries are disabled.

    A number sets the total number of retries, and uses collection defaults for the other settings.

    A dictionary value is used directly to initialize the `Retry` class, so it can be used to fully customize retries.

    For detailed information on retries, see the collection User Guide.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_RETRY_ACTION
:   Controls whether and how to show messages on *retries*.

    This has no effect if a request is not retried.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_ROLE_ID
:   Vault Role ID or name. Used in `approle`, `aws_iam`, `azure` and `cert` auth methods.

    For `cert` auth, if no *role_id* is supplied, the default behavior is to try all certificate roles and return any one that matches.

    For `azure` auth, *role_id* is required.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_SECRET_ID
:   Secret ID to be used for Vault AppRole authentication.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_TIMEOUT
:   Sets the connection timeout in seconds.

    If not set, then the `hvac` library’s default is used.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_TOKEN
:   Vault token. Token may be specified explicitly, through the listed [env] vars, and also through the `VAULT_TOKEN` env var.

    If no token is supplied, explicitly or through env, then the plugin will check for a token file, as determined by *token_path* and *token_file*.

    The order of token loading (first found wins) is `token param -> ansible var -> ANSIBLE_HASHI_VAULT_TOKEN -> VAULT_TOKEN -> token file`.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_TOKEN_FILE
:   If no token is specified, will try to read the token from this file in *token_path*.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_TOKEN_PATH
:   If no token is specified, will try to read the *token_file* from this path.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_TOKEN_VALIDATE
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HASHI_VAULT_USERNAME
:   Authentication user name.

    *Used by:*
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ANSIBLE_HIERA_BIN
:   Binary file to execute Hiera

    *Used by:*
    [community.general.hiera lookup plugin](community/general/hiera_lookup.md#ansible-collections-community-general-hiera-lookup)

ANSIBLE_HIERA_CFG
:   File that describes the hierarchy of Hiera

    *Used by:*
    [community.general.hiera lookup plugin](community/general/hiera_lookup.md#ansible-collections-community-general-hiera-lookup)

ANSIBLE_HOST_KEY_AUTO_ADD
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [ansible.netcommon.napalm connection plugin](ansible/netcommon/napalm_connection.md#ansible-collections-ansible-netcommon-napalm-connection),
    [ansible.netcommon.network_cli connection plugin](ansible/netcommon/network_cli_connection.md#ansible-collections-ansible-netcommon-network-cli-connection)

ANSIBLE_IGNORE_ERRORS
:   Whether to ignore errors on failing or not

    *Used by:*
    [community.general.logdna callback plugin](community/general/logdna_callback.md#ansible-collections-community-general-logdna-callback)

ANSIBLE_INVENTORY_PLUGIN_EXTS
:   list of ‘valid’ extensions for files containing YAML

    *Used by:*
    [ansible.builtin.yaml inventory plugin](ansible/builtin/yaml_inventory.md#ansible-collections-ansible-builtin-yaml-inventory)

ANSIBLE_INVENTORY_PLUGIN_SCRIPT_STDERR
:   Toggle display of stderr even when script was successful

    *Used by:*
    [ansible.builtin.script inventory plugin](ansible/builtin/script_inventory.md#ansible-collections-ansible-builtin-script-inventory)

ANSIBLE_INVENTORY_USE_EXTRA_VARS
:   Merge extra vars into the available variables for composition (highest precedence).

    *Used by:*
    [amazon.aws.aws_ec2 inventory plugin](amazon/aws/aws_ec2_inventory.md#ansible-collections-amazon-aws-aws-ec2-inventory),
    [amazon.aws.aws_rds inventory plugin](amazon/aws/aws_rds_inventory.md#ansible-collections-amazon-aws-aws-rds-inventory),
    [ansible.builtin.constructed inventory plugin](ansible/builtin/constructed_inventory.md#ansible-collections-ansible-builtin-constructed-inventory),
    [azure.azcollection.azure_rm inventory plugin](azure/azcollection/azure_rm_inventory.md#ansible-collections-azure-azcollection-azure-rm-inventory),
    [cloudscale_ch.cloud.inventory inventory plugin](cloudscale_ch/cloud/inventory_inventory.md#ansible-collections-cloudscale-ch-cloud-inventory-inventory),
    [community.digitalocean.digitalocean inventory plugin](community/digitalocean/digitalocean_inventory.md#ansible-collections-community-digitalocean-digitalocean-inventory),
    [community.docker.docker_containers inventory plugin](community/docker/docker_containers_inventory.md#ansible-collections-community-docker-docker-containers-inventory),
    [community.docker.docker_machine inventory plugin](community/docker/docker_machine_inventory.md#ansible-collections-community-docker-docker-machine-inventory),
    [community.docker.docker_swarm inventory plugin](community/docker/docker_swarm_inventory.md#ansible-collections-community-docker-docker-swarm-inventory),
    [community.general.gitlab_runners inventory plugin](community/general/gitlab_runners_inventory.md#ansible-collections-community-general-gitlab-runners-inventory),
    [community.general.icinga2 inventory plugin](community/general/icinga2_inventory.md#ansible-collections-community-general-icinga2-inventory),
    [community.general.linode inventory plugin](community/general/linode_inventory.md#ansible-collections-community-general-linode-inventory),
    [community.general.nmap inventory plugin](community/general/nmap_inventory.md#ansible-collections-community-general-nmap-inventory),
    [community.general.opennebula inventory plugin](community/general/opennebula_inventory.md#ansible-collections-community-general-opennebula-inventory),
    [community.general.proxmox inventory plugin](community/general/proxmox_inventory.md#ansible-collections-community-general-proxmox-inventory),
    [community.general.stackpath_compute inventory plugin](community/general/stackpath_compute_inventory.md#ansible-collections-community-general-stackpath-compute-inventory),
    [community.general.virtualbox inventory plugin](community/general/virtualbox_inventory.md#ansible-collections-community-general-virtualbox-inventory),
    [community.general.xen_orchestra inventory plugin](community/general/xen_orchestra_inventory.md#ansible-collections-community-general-xen-orchestra-inventory),
    [community.hrobot.robot inventory plugin](community/hrobot/robot_inventory.md#ansible-collections-community-hrobot-robot-inventory),
    [community.libvirt.libvirt inventory plugin](community/libvirt/libvirt_inventory.md#ansible-collections-community-libvirt-libvirt-inventory),
    [community.vmware.vmware_host_inventory inventory plugin](community/vmware/vmware_host_inventory_inventory.md#ansible-collections-community-vmware-vmware-host-inventory-inventory),
    [community.vmware.vmware_vm_inventory inventory plugin](community/vmware/vmware_vm_inventory_inventory.md#ansible-collections-community-vmware-vmware-vm-inventory-inventory),
    [community.zabbix.zabbix_inventory inventory plugin](community/zabbix/zabbix_inventory_inventory.md#ansible-collections-community-zabbix-zabbix-inventory-inventory),
    [google.cloud.gcp_compute inventory plugin](google/cloud/gcp_compute_inventory.md#ansible-collections-google-cloud-gcp-compute-inventory),
    [hetzner.hcloud.hcloud inventory plugin](hetzner/hcloud/hcloud_inventory.md#ansible-collections-hetzner-hcloud-hcloud-inventory),
    [netbox.netbox.nb_inventory inventory plugin](netbox/netbox/nb_inventory_inventory.md#ansible-collections-netbox-netbox-nb-inventory-inventory),
    [ngine_io.cloudstack.instance inventory plugin](ngine_io/cloudstack/instance_inventory.md#ansible-collections-ngine-io-cloudstack-instance-inventory),
    [ngine_io.vultr.vultr inventory plugin](ngine_io/vultr/vultr_inventory.md#ansible-collections-ngine-io-vultr-vultr-inventory),
    [openstack.cloud.openstack inventory plugin](openstack/cloud/openstack_inventory.md#ansible-collections-openstack-cloud-openstack-inventory),
    [ovirt.ovirt.ovirt inventory plugin](ovirt/ovirt/ovirt_inventory.md#ansible-collections-ovirt-ovirt-ovirt-inventory),
    [servicenow.servicenow.now inventory plugin](servicenow/servicenow/now_inventory.md#ansible-collections-servicenow-servicenow-now-inventory),
    [t_systems_mms.icinga_director.icinga_director_inventory inventory plugin](t_systems_mms/icinga_director/icinga_director_inventory_inventory.md#ansible-collections-t-systems-mms-icinga-director-icinga-director-inventory-inventory),
    [theforeman.foreman.foreman inventory plugin](theforeman/foreman/foreman_inventory.md#ansible-collections-theforeman-foreman-foreman-inventory)

ANSIBLE_IOSXR_COMMIT_COMMENT
:   Adds comment to commit confirmed..

    *Used by:*
    [cisco.iosxr.iosxr cliconf plugin](cisco/iosxr/iosxr_cliconf.md#ansible-collections-cisco-iosxr-iosxr-cliconf)

ANSIBLE_IOSXR_COMMIT_CONFIRMED
:   enable or disable commit confirmed mode

    *Used by:*
    [cisco.iosxr.iosxr cliconf plugin](cisco/iosxr/iosxr_cliconf.md#ansible-collections-cisco-iosxr-iosxr-cliconf)

ANSIBLE_IOSXR_COMMIT_CONFIRMED_TIMEOUT
:   Commits the configuration on a trial basis for the time specified in seconds or minutes.

    *Used by:*
    [cisco.iosxr.iosxr cliconf plugin](cisco/iosxr/iosxr_cliconf.md#ansible-collections-cisco-iosxr-iosxr-cliconf)

ANSIBLE_IOSXR_COMMIT_LABEL
:   Adds label to commit confirmed.

    *Used by:*
    [cisco.iosxr.iosxr cliconf plugin](cisco/iosxr/iosxr_cliconf.md#ansible-collections-cisco-iosxr-iosxr-cliconf)

ANSIBLE_IOSXR_CONFIG_MODE_EXCLUSIVE
:   enable or disable config mode exclusive

    *Used by:*
    [cisco.iosxr.iosxr cliconf plugin](cisco/iosxr/iosxr_cliconf.md#ansible-collections-cisco-iosxr-iosxr-cliconf)

ANSIBLE_KSU_EXE
:   Su executable

    *Used by:*
    [community.general.ksu become plugin](community/general/ksu_become.md#ansible-collections-community-general-ksu-become)

ANSIBLE_KSU_FLAGS
:   Options to pass to ksu

    *Used by:*
    [community.general.ksu become plugin](community/general/ksu_become.md#ansible-collections-community-general-ksu-become)

ANSIBLE_KSU_PASS
:   ksu password

    *Used by:*
    [community.general.ksu become plugin](community/general/ksu_become.md#ansible-collections-community-general-ksu-become)

ANSIBLE_KSU_PROMPT_L10N
:   List of localized strings to match for prompt detection

    If empty we’ll use the built in one

    *Used by:*
    [community.general.ksu become plugin](community/general/ksu_become.md#ansible-collections-community-general-ksu-become)

ANSIBLE_KSU_USER
:   User you ‘become’ to execute the task

    *Used by:*
    [community.general.ksu become plugin](community/general/ksu_become.md#ansible-collections-community-general-ksu-become)

ANSIBLE_LIBSSH_HOST_KEY_AUTO_ADD
:   TODO: write it

    *Used by:*
    [ansible.netcommon.libssh connection plugin](ansible/netcommon/libssh_connection.md#ansible-collections-ansible-netcommon-libssh-connection)

ANSIBLE_LIBSSH_HOST_KEY_CHECKING
:   Set this to “False” if you want to avoid host key checking by the underlying tools Ansible uses to connect to the host

    *Used by:*
    [ansible.netcommon.libssh connection plugin](ansible/netcommon/libssh_connection.md#ansible-collections-ansible-netcommon-libssh-connection)

ANSIBLE_LIBSSH_LOOK_FOR_KEYS
:   TODO: write it

    *Used by:*
    [ansible.netcommon.libssh connection plugin](ansible/netcommon/libssh_connection.md#ansible-collections-ansible-netcommon-libssh-connection)

ANSIBLE_LIBSSH_PROXY_COMMAND
:   Proxy information for running the connection via a jumphost.

    Also this plugin will scan ‘ssh_args’, ‘ssh_extra_args’ and ‘ssh_common_args’ from the ‘ssh’ plugin settings for proxy information if set.

    *Used by:*
    [ansible.netcommon.libssh connection plugin](ansible/netcommon/libssh_connection.md#ansible-collections-ansible-netcommon-libssh-connection)

ANSIBLE_LIBSSH_PTY
:   TODO: write it

    *Used by:*
    [ansible.netcommon.libssh connection plugin](ansible/netcommon/libssh_connection.md#ansible-collections-ansible-netcommon-libssh-connection)

ANSIBLE_LIBSSH_REMOTE_USER
:   User to login/authenticate as

    Can be set from the CLI via the `--user` or `-u` options.

    *Used by:*
    [ansible.netcommon.libssh connection plugin](ansible/netcommon/libssh_connection.md#ansible-collections-ansible-netcommon-libssh-connection)

ANSIBLE_LOG_FOLDER
:   The folder where log files will be created.

    *Used by:*
    [community.general.log_plays callback plugin](community/general/log_plays_callback.md#ansible-collections-community-general-log-plays-callback)

ANSIBLE_LOOKUP_URL_AGENT
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [ansible.builtin.url lookup plugin](ansible/builtin/url_lookup.md#ansible-collections-ansible-builtin-url-lookup)

ANSIBLE_LOOKUP_URL_CA_PATH
:   String of file system path to CA cert bundle to use

    *Used by:*
    [ansible.builtin.url lookup plugin](ansible/builtin/url_lookup.md#ansible-collections-ansible-builtin-url-lookup)

ANSIBLE_LOOKUP_URL_FOLLOW_REDIRECTS
:   String of urllib2, all/yes, safe, none to determine how redirects are followed, see RedirectHandlerFactory for more information

    *Used by:*
    [ansible.builtin.url lookup plugin](ansible/builtin/url_lookup.md#ansible-collections-ansible-builtin-url-lookup)

ANSIBLE_LOOKUP_URL_FORCE
:   Whether or not to set “cache-control” header with value “no-cache”

    *Used by:*
    [ansible.builtin.url lookup plugin](ansible/builtin/url_lookup.md#ansible-collections-ansible-builtin-url-lookup)

ANSIBLE_LOOKUP_URL_TIMEOUT
:   How long to wait for the server to send data before giving up

    *Used by:*
    [ansible.builtin.url lookup plugin](ansible/builtin/url_lookup.md#ansible-collections-ansible-builtin-url-lookup)

ANSIBLE_LOOKUP_URL_UNIX_SOCKET
:   String of file system path to unix socket file to use when establishing connection to the provided url

    *Used by:*
    [ansible.builtin.url lookup plugin](ansible/builtin/url_lookup.md#ansible-collections-ansible-builtin-url-lookup)

ANSIBLE_LOOKUP_URL_UNREDIR_HEADERS
:   A list of headers to not attach on a redirected request

    *Used by:*
    [ansible.builtin.url lookup plugin](ansible/builtin/url_lookup.md#ansible-collections-ansible-builtin-url-lookup)

ANSIBLE_LOOKUP_URL_USE_GSSAPI
:   Use GSSAPI handler of requests

    As of Ansible 2.11, GSSAPI credentials can be specified with *username* and *password*.

    *Used by:*
    [ansible.builtin.url lookup plugin](ansible/builtin/url_lookup.md#ansible-collections-ansible-builtin-url-lookup)

ANSIBLE_MACHINECTL_EXE
:   Machinectl executable

    *Used by:*
    [community.general.machinectl become plugin](community/general/machinectl_become.md#ansible-collections-community-general-machinectl-become)

ANSIBLE_MACHINECTL_FLAGS
:   Options to pass to machinectl

    *Used by:*
    [community.general.machinectl become plugin](community/general/machinectl_become.md#ansible-collections-community-general-machinectl-become)

ANSIBLE_MACHINECTL_PASS
:   Password for machinectl

    *Used by:*
    [community.general.machinectl become plugin](community/general/machinectl_become.md#ansible-collections-community-general-machinectl-become)

ANSIBLE_MACHINECTL_USER
:   User you ‘become’ to execute the task

    *Used by:*
    [community.general.machinectl become plugin](community/general/machinectl_become.md#ansible-collections-community-general-machinectl-become)

ANSIBLE_NETCONF_HOST_KEY_CHECKING
:   Set this to “False” if you want to avoid host key checking by the underlying tools Ansible uses to connect to the host

    *Used by:*
    [ansible.netcommon.netconf connection plugin](ansible/netcommon/netconf_connection.md#ansible-collections-ansible-netcommon-netconf-connection)

ANSIBLE_NETCONF_PROXY_COMMAND
:   Proxy information for running the connection via a jumphost.

    This requires ncclient >= 0.6.10 to be installed on the controller.

    *Used by:*
    [ansible.netcommon.netconf connection plugin](ansible/netcommon/netconf_connection.md#ansible-collections-ansible-netcommon-netconf-connection)

ANSIBLE_NETWORK_CLI_RETRIES
:   Number of attempts to connect to remote host. The delay time between the retires increases after every attempt by power of 2 in seconds till either the maximum attempts are exhausted or any of the `persistent_command_timeout` or `persistent_connect_timeout` timers are triggered.

    *Used by:*
    [ansible.netcommon.network_cli connection plugin](ansible/netcommon/network_cli_connection.md#ansible-collections-ansible-netcommon-network-cli-connection)

ANSIBLE_NETWORK_CLI_SSH_TYPE
:   The python package that will be used by the `network_cli` connection plugin to create a SSH connection to remote host.

    *libssh* will use the ansible-pylibssh package, which needs to be installed in order to work.

    *paramiko* will instead use the paramiko package to manage the SSH connection.

    *auto* will use ansible-pylibssh if that package is installed, otherwise will fallback to paramiko.

    *Used by:*
    [ansible.netcommon.network_cli connection plugin](ansible/netcommon/network_cli_connection.md#ansible-collections-ansible-netcommon-network-cli-connection)

ANSIBLE_NETWORK_IMPORT_MODULES
:   Reduce CPU usage and network module execution time by enabling direct execution. Instead of the module being packaged and executed by the shell, it will be directly executed by the Ansible control node using the same python interpreter as the Ansible process. Note- Incompatible with `asynchronous mode`. Note- Python 3 and Ansible 2.9.16 or greater required. Note- With Ansible 2.9.x fully qualified modules names are required in tasks.

    *Used by:*
    [ansible.netcommon.grpc connection plugin](ansible/netcommon/grpc_connection.md#ansible-collections-ansible-netcommon-grpc-connection),
    [ansible.netcommon.httpapi connection plugin](ansible/netcommon/httpapi_connection.md#ansible-collections-ansible-netcommon-httpapi-connection),
    [ansible.netcommon.napalm connection plugin](ansible/netcommon/napalm_connection.md#ansible-collections-ansible-netcommon-napalm-connection),
    [ansible.netcommon.netconf connection plugin](ansible/netcommon/netconf_connection.md#ansible-collections-ansible-netcommon-netconf-connection),
    [ansible.netcommon.network_cli connection plugin](ansible/netcommon/network_cli_connection.md#ansible-collections-ansible-netcommon-network-cli-connection),
    [ansible.netcommon.persistent connection plugin](ansible/netcommon/persistent_connection.md#ansible-collections-ansible-netcommon-persistent-connection)

ANSIBLE_NETWORK_SINGLE_USER_MODE
:   This option enables caching of data fetched from the target for re-use. The cache is invalidated when the target device enters configuration mode.

    Applicable only for platforms where this has been implemented.

    *Used by:*
    [ansible.netcommon.network_cli connection plugin](ansible/netcommon/network_cli_connection.md#ansible-collections-ansible-netcommon-network-cli-connection)

ANSIBLE_NSENTER_PID
:   PID to attach with using nsenter.

    The default should be fine unless you are attaching as a non-root user.

    *Used by:*
    [community.docker.nsenter connection plugin](community/docker/nsenter_connection.md#ansible-collections-community-docker-nsenter-connection)

ANSIBLE_OPENTELEMETRY_DISABLE_LOGS
:   Disable sending logs.

    *Used by:*
    [community.general.opentelemetry callback plugin](community/general/opentelemetry_callback.md#ansible-collections-community-general-opentelemetry-callback)

ANSIBLE_OPENTELEMETRY_ENABLE_FROM_ENVIRONMENT
:   Whether to enable this callback only if the given environment variable exists and it is set to `true`.

    This is handy when you use Configuration as Code and want to send distributed traces if running in the CI rather when running Ansible locally.

    For such, it evaluates the given *enable_from_environment* value as environment variable and if set to true this plugin will be enabled.

    *Used by:*
    [community.general.opentelemetry callback plugin](community/general/opentelemetry_callback.md#ansible-collections-community-general-opentelemetry-callback)

ANSIBLE_OPENTELEMETRY_HIDE_TASK_ARGUMENTS
:   Hide the arguments for a task.

    *Used by:*
    [community.general.elastic callback plugin](community/general/elastic_callback.md#ansible-collections-community-general-elastic-callback),
    [community.general.opentelemetry callback plugin](community/general/opentelemetry_callback.md#ansible-collections-community-general-opentelemetry-callback)

ANSIBLE_PARAMIKO_HOST_KEY_CHECKING
:   Set this to “False” if you want to avoid host key checking by the underlying tools Ansible uses to connect to the host

    *Used by:*
    [ansible.builtin.paramiko_ssh connection plugin](ansible/builtin/paramiko_ssh_connection.md#ansible-collections-ansible-builtin-paramiko-ssh-connection)

ANSIBLE_PARAMIKO_PROXY_COMMAND
:   Proxy information for running the connection via a jumphost

    Also this plugin will scan ‘ssh_args’, ‘ssh_extra_args’ and ‘ssh_common_args’ from the ‘ssh’ plugin settings for proxy information if set.

    *Used by:*
    [ansible.builtin.paramiko_ssh connection plugin](ansible/builtin/paramiko_ssh_connection.md#ansible-collections-ansible-builtin-paramiko-ssh-connection)

ANSIBLE_PARAMIKO_PTY
:   SUDO usually requires a PTY, True to give a PTY and False to not give a PTY.

    *Used by:*
    [ansible.builtin.paramiko_ssh connection plugin](ansible/builtin/paramiko_ssh_connection.md#ansible-collections-ansible-builtin-paramiko-ssh-connection)

ANSIBLE_PARAMIKO_RECORD_HOST_KEYS
:   Save the host keys to a file

    *Used by:*
    [ansible.builtin.paramiko_ssh connection plugin](ansible/builtin/paramiko_ssh_connection.md#ansible-collections-ansible-builtin-paramiko-ssh-connection)

ANSIBLE_PARAMIKO_REMOTE_USER
:   User to login/authenticate as

    Can be set from the CLI via the `--user` or `-u` options.

    *Used by:*
    [ansible.builtin.paramiko_ssh connection plugin](ansible/builtin/paramiko_ssh_connection.md#ansible-collections-ansible-builtin-paramiko-ssh-connection)

ANSIBLE_PBRUN_EXE
:   Sudo executable

    *Used by:*
    [community.general.pbrun become plugin](community/general/pbrun_become.md#ansible-collections-community-general-pbrun-become)

ANSIBLE_PBRUN_FLAGS
:   Options to pass to pbrun

    *Used by:*
    [community.general.pbrun become plugin](community/general/pbrun_become.md#ansible-collections-community-general-pbrun-become)

ANSIBLE_PBRUN_PASS
:   Password for pbrun

    *Used by:*
    [community.general.pbrun become plugin](community/general/pbrun_become.md#ansible-collections-community-general-pbrun-become)

ANSIBLE_PBRUN_USER
:   User you ‘become’ to execute the task

    *Used by:*
    [community.general.pbrun become plugin](community/general/pbrun_become.md#ansible-collections-community-general-pbrun-become)

ANSIBLE_PBRUN_WRAP_EXECUTION
:   Toggle to wrap the command pbrun calls in ‘shell -c’ or not

    *Used by:*
    [community.general.pbrun become plugin](community/general/pbrun_become.md#ansible-collections-community-general-pbrun-become)

ANSIBLE_PERSISTENT_BUFFER_READ_TIMEOUT
:   Configures, in seconds, the amount of time to wait for the data to be read from Paramiko channel after the command prompt is matched. This timeout value ensures that command prompt matched is correct and there is no more data left to be received from remote host.

    *Used by:*
    [ansible.netcommon.network_cli connection plugin](ansible/netcommon/network_cli_connection.md#ansible-collections-ansible-netcommon-network-cli-connection)

ANSIBLE_PERSISTENT_LOG_MESSAGES
:   This flag will enable logging the command executed and response received from target device in the ansible log file. For this option to work ‘log_path’ ansible configuration option is required to be set to a file path with write access.

    Be sure to fully understand the security implications of enabling this option as it could create a security vulnerability by logging sensitive information in log file.

    *Used by:*
    [ansible.netcommon.grpc connection plugin](ansible/netcommon/grpc_connection.md#ansible-collections-ansible-netcommon-grpc-connection),
    [ansible.netcommon.httpapi connection plugin](ansible/netcommon/httpapi_connection.md#ansible-collections-ansible-netcommon-httpapi-connection),
    [ansible.netcommon.napalm connection plugin](ansible/netcommon/napalm_connection.md#ansible-collections-ansible-netcommon-napalm-connection),
    [ansible.netcommon.netconf connection plugin](ansible/netcommon/netconf_connection.md#ansible-collections-ansible-netcommon-netconf-connection),
    [ansible.netcommon.network_cli connection plugin](ansible/netcommon/network_cli_connection.md#ansible-collections-ansible-netcommon-network-cli-connection),
    [ansible.netcommon.persistent connection plugin](ansible/netcommon/persistent_connection.md#ansible-collections-ansible-netcommon-persistent-connection)

ANSIBLE_PFEXEC_EXE
:   Sudo executable

    *Used by:*
    [community.general.pfexec become plugin](community/general/pfexec_become.md#ansible-collections-community-general-pfexec-become)

ANSIBLE_PFEXEC_FLAGS
:   Options to pass to pfexec

    *Used by:*
    [community.general.pfexec become plugin](community/general/pfexec_become.md#ansible-collections-community-general-pfexec-become)

ANSIBLE_PFEXEC_PASS
:   pfexec password

    *Used by:*
    [community.general.pfexec become plugin](community/general/pfexec_become.md#ansible-collections-community-general-pfexec-become)

ANSIBLE_PFEXEC_USER
:   User you ‘become’ to execute the task

    This plugin ignores this setting as pfexec uses it’s own `exec_attr` to figure this out, but it is supplied here for Ansible to make decisions needed for the task execution, like file permissions.

    *Used by:*
    [community.general.pfexec become plugin](community/general/pfexec_become.md#ansible-collections-community-general-pfexec-become)

ANSIBLE_PFEXEC_WRAP_EXECUTION
:   Toggle to wrap the command pfexec calls in ‘shell -c’ or not

    *Used by:*
    [community.general.pfexec become plugin](community/general/pfexec_become.md#ansible-collections-community-general-pfexec-become)

ANSIBLE_PKCS11_PROVIDER
:   PKCS11 SmartCard provider such as opensc, example: /usr/local/lib/opensc-pkcs11.so

    Requires sshpass version 1.06+, sshpass must support the -P option.

    *Used by:*
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection)

ANSIBLE_PLATFORM_TYPE
:   Set type of platform.

    *Used by:*
    [ansible.netcommon.httpapi connection plugin](ansible/netcommon/httpapi_connection.md#ansible-collections-ansible-netcommon-httpapi-connection)

ANSIBLE_PMRUN_EXE
:   Sudo executable

    *Used by:*
    [community.general.pmrun become plugin](community/general/pmrun_become.md#ansible-collections-community-general-pmrun-become)

ANSIBLE_PMRUN_FLAGS
:   Options to pass to pmrun

    *Used by:*
    [community.general.pmrun become plugin](community/general/pmrun_become.md#ansible-collections-community-general-pmrun-become)

ANSIBLE_PMRUN_PASS
:   pmrun password

    *Used by:*
    [community.general.pmrun become plugin](community/general/pmrun_become.md#ansible-collections-community-general-pmrun-become)

ANSIBLE_PODMAN_EXECUTABLE
:   Executable for podman command.

    *Used by:*
    [containers.podman.podman connection plugin](containers/podman/podman_connection.md#ansible-collections-containers-podman-podman-connection)

ANSIBLE_PODMAN_EXTRA_ARGS
:   Extra arguments to pass to the podman command line.

    *Used by:*
    [containers.podman.podman connection plugin](containers/podman/podman_connection.md#ansible-collections-containers-podman-podman-connection)

ANSIBLE_REDIS_HOST
:   location of Redis host

    *Used by:*
    [community.general.redis lookup plugin](community/general/redis_lookup.md#ansible-collections-community-general-redis-lookup)

ANSIBLE_REDIS_PORT
:   port on which Redis is listening on

    *Used by:*
    [community.general.redis lookup plugin](community/general/redis_lookup.md#ansible-collections-community-general-redis-lookup)

ANSIBLE_REDIS_SOCKET
:   path to socket on which to query Redis, this option overrides host and port options when set.

    *Used by:*
    [community.general.redis lookup plugin](community/general/redis_lookup.md#ansible-collections-community-general-redis-lookup)

ANSIBLE_REMOTE_TEMP
:   Temporary directory to use on targets when executing tasks.

    *Used by:*
    [ansible.builtin.sh shell plugin](ansible/builtin/sh_shell.md#ansible-collections-ansible-builtin-sh-shell),
    [ansible.posix.csh shell plugin](ansible/posix/csh_shell.md#ansible-collections-ansible-posix-csh-shell),
    [ansible.posix.fish shell plugin](ansible/posix/fish_shell.md#ansible-collections-ansible-posix-fish-shell)

ANSIBLE_REMOTE_TMP
:   Temporary directory to use on targets when executing tasks.

    *Used by:*
    [ansible.builtin.sh shell plugin](ansible/builtin/sh_shell.md#ansible-collections-ansible-builtin-sh-shell),
    [ansible.posix.csh shell plugin](ansible/posix/csh_shell.md#ansible-collections-ansible-posix-csh-shell),
    [ansible.posix.fish shell plugin](ansible/posix/fish_shell.md#ansible-collections-ansible-posix-fish-shell)

ANSIBLE_ROOT_CERTIFICATES_FILE
:   The PEM encoded root certificate file used to create a SSL-enabled channel, if the value is None it reads the root certificates from a default location chosen by gRPC at runtime.

    *Used by:*
    [ansible.netcommon.grpc connection plugin](ansible/netcommon/grpc_connection.md#ansible-collections-ansible-netcommon-grpc-connection)

ANSIBLE_RUNAS_FLAGS
:   Options to pass to runas, a space delimited list of k=v pairs

    *Used by:*
    [ansible.builtin.runas become plugin](ansible/builtin/runas_become.md#ansible-collections-ansible-builtin-runas-become)

ANSIBLE_RUNAS_PASS
:   password

    *Used by:*
    [ansible.builtin.runas become plugin](ansible/builtin/runas_become.md#ansible-collections-ansible-builtin-runas-become)

ANSIBLE_RUNAS_USER
:   User you ‘become’ to execute the task

    *Used by:*
    [ansible.builtin.runas become plugin](ansible/builtin/runas_become.md#ansible-collections-ansible-builtin-runas-become)

ANSIBLE_SCP_EXECUTABLE
:   This defines the location of the scp binary. It defaults to `scp` which will use the first binary available in $PATH.

    *Used by:*
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection)

ANSIBLE_SCP_EXTRA_ARGS
:   Extra exclusive to the `scp` CLI

    *Used by:*
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection)

ANSIBLE_SCP_IF_SSH
:   Preferred method to use when transferring files over SSH.

    When set to *smart*, Ansible will try them until one succeeds or they all fail.

    If set to *True*, it will force ‘scp’, if *False* it will use ‘sftp’.

    For OpenSSH >=9.0 you must add an additional option to enable scp (scp_extra_args=”-O”)

    This setting will overridden by ssh_transfer_method if set.

    *Used by:*
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection)

ANSIBLE_SELECTIVE_DONT_COLORIZE
:   This setting allows suppressing colorizing output

    *Used by:*
    [community.general.selective callback plugin](community/general/selective_callback.md#ansible-collections-community-general-selective-callback)

ANSIBLE_SESU_EXE
:   sesu executable

    *Used by:*
    [community.general.sesu become plugin](community/general/sesu_become.md#ansible-collections-community-general-sesu-become)

ANSIBLE_SESU_FLAGS
:   Options to pass to sesu

    *Used by:*
    [community.general.sesu become plugin](community/general/sesu_become.md#ansible-collections-community-general-sesu-become)

ANSIBLE_SESU_PASS
:   Password to pass to sesu

    *Used by:*
    [community.general.sesu become plugin](community/general/sesu_become.md#ansible-collections-community-general-sesu-become)

ANSIBLE_SESU_USER
:   User you ‘become’ to execute the task

    *Used by:*
    [community.general.sesu become plugin](community/general/sesu_become.md#ansible-collections-community-general-sesu-become)

ANSIBLE_SFTP_BATCH_MODE
:   TODO: write it

    *Used by:*
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection)

ANSIBLE_SFTP_EXECUTABLE
:   This defines the location of the sftp binary. It defaults to `sftp` which will use the first binary available in $PATH.

    *Used by:*
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection)

ANSIBLE_SFTP_EXTRA_ARGS
:   Extra exclusive to the `sftp` CLI

    *Used by:*
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection)

ANSIBLE_SHELL_ALLOW_WORLD_READABLE_TEMP
:   This makes the temporary files created on the machine world-readable and will issue a warning instead of failing the task.

    It is useful when becoming an unprivileged user.

    *Used by:*
    [ansible.builtin.sh shell plugin](ansible/builtin/sh_shell.md#ansible-collections-ansible-builtin-sh-shell),
    [ansible.posix.csh shell plugin](ansible/posix/csh_shell.md#ansible-collections-ansible-posix-csh-shell),
    [ansible.posix.fish shell plugin](ansible/posix/fish_shell.md#ansible-collections-ansible-posix-fish-shell)

ANSIBLE_SHOW_PER_HOST_START
:   This adds output that shows when a task is started to execute for each host

    *Used by:*
    [ansible.builtin.default callback plugin](ansible/builtin/default_callback.md#ansible-collections-ansible-builtin-default-callback),
    [ansible.posix.debug callback plugin](ansible/posix/debug_callback.md#ansible-collections-ansible-posix-debug-callback),
    [ansible.posix.skippy callback plugin](ansible/posix/skippy_callback.md#ansible-collections-ansible-posix-skippy-callback),
    [community.general.counter_enabled callback plugin](community/general/counter_enabled_callback.md#ansible-collections-community-general-counter-enabled-callback),
    [community.general.dense callback plugin](community/general/dense_callback.md#ansible-collections-community-general-dense-callback),
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback),
    [community.general.unixy callback plugin](community/general/unixy_callback.md#ansible-collections-community-general-unixy-callback),
    [community.general.yaml callback plugin](community/general/yaml_callback.md#ansible-collections-community-general-yaml-callback)

ANSIBLE_SHOW_TASK_PATH_ON_FAILURE
:   When a task fails, display the path to the file containing the failed task and the line number. This information is displayed automatically for every task when running with `-vv` or greater verbosity.

    *Used by:*
    [ansible.builtin.default callback plugin](ansible/builtin/default_callback.md#ansible-collections-ansible-builtin-default-callback),
    [ansible.posix.debug callback plugin](ansible/posix/debug_callback.md#ansible-collections-ansible-posix-debug-callback),
    [ansible.posix.skippy callback plugin](ansible/posix/skippy_callback.md#ansible-collections-ansible-posix-skippy-callback),
    [community.general.counter_enabled callback plugin](community/general/counter_enabled_callback.md#ansible-collections-community-general-counter-enabled-callback),
    [community.general.dense callback plugin](community/general/dense_callback.md#ansible-collections-community-general-dense-callback),
    [community.general.diy callback plugin](community/general/diy_callback.md#ansible-collections-community-general-diy-callback),
    [community.general.unixy callback plugin](community/general/unixy_callback.md#ansible-collections-community-general-unixy-callback),
    [community.general.yaml callback plugin](community/general/yaml_callback.md#ansible-collections-community-general-yaml-callback)

ANSIBLE_SOPS_AGE_KEY
:   One or more age private keys that can be used to decrypt encrypted files.

    Will be set as the `SOPS_AGE_KEY` environment variable when calling sops.

    *Used by:*
    [community.sops.sops lookup plugin](community/sops/sops_lookup.md#ansible-collections-community-sops-sops-lookup),
    [community.sops.sops vars plugin](community/sops/sops_vars.md#ansible-collections-community-sops-sops-vars)

ANSIBLE_SOPS_AGE_KEYFILE
:   The file containing the age private keys that sops can use to decrypt encrypted files.

    Will be set as the `SOPS_AGE_KEY_FILE` environment variable when calling sops.

    By default, sops looks for `sops/age/keys.txt` inside your user configuration directory.

    *Used by:*
    [community.sops.sops lookup plugin](community/sops/sops_lookup.md#ansible-collections-community-sops-sops-lookup),
    [community.sops.sops vars plugin](community/sops/sops_vars.md#ansible-collections-community-sops-sops-vars)

ANSIBLE_SOPS_AWS_ACCESS_KEY_ID
:   The AWS access key ID to use for requests to AWS.

    Sets the environment variable `AWS_ACCESS_KEY_ID` for the sops call.

    *Used by:*
    [community.sops.sops lookup plugin](community/sops/sops_lookup.md#ansible-collections-community-sops-sops-lookup),
    [community.sops.sops vars plugin](community/sops/sops_vars.md#ansible-collections-community-sops-sops-vars)

ANSIBLE_SOPS_AWS_PROFILE
:   The AWS profile to use for requests to AWS.

    This corresponds to the sops `--aws-profile` option.

    *Used by:*
    [community.sops.sops lookup plugin](community/sops/sops_lookup.md#ansible-collections-community-sops-sops-lookup),
    [community.sops.sops vars plugin](community/sops/sops_vars.md#ansible-collections-community-sops-sops-vars)

ANSIBLE_SOPS_AWS_SECRET_ACCESS_KEY
:   The AWS secret access key to use for requests to AWS.

    Sets the environment variable `AWS_SECRET_ACCESS_KEY` for the sops call.

    *Used by:*
    [community.sops.sops lookup plugin](community/sops/sops_lookup.md#ansible-collections-community-sops-sops-lookup),
    [community.sops.sops vars plugin](community/sops/sops_vars.md#ansible-collections-community-sops-sops-vars)

ANSIBLE_SOPS_AWS_SESSION_TOKEN
:   The AWS session token to use for requests to AWS.

    Sets the environment variable `AWS_SESSION_TOKEN` for the sops call.

    *Used by:*
    [community.sops.sops lookup plugin](community/sops/sops_lookup.md#ansible-collections-community-sops-sops-lookup),
    [community.sops.sops vars plugin](community/sops/sops_vars.md#ansible-collections-community-sops-sops-vars)

ANSIBLE_SOPS_BINARY
:   Path to the sops binary.

    By default uses `sops`.

    *Used by:*
    [community.sops.sops lookup plugin](community/sops/sops_lookup.md#ansible-collections-community-sops-sops-lookup),
    [community.sops.sops vars plugin](community/sops/sops_vars.md#ansible-collections-community-sops-sops-vars)

ANSIBLE_SOPS_CONFIG_PATH
:   Path to the sops configuration file.

    If not set, sops will recursively search for the config file starting at the file that is encrypted or decrypted.

    This corresponds to the sops `--config` option.

    *Used by:*
    [community.sops.sops lookup plugin](community/sops/sops_lookup.md#ansible-collections-community-sops-sops-lookup),
    [community.sops.sops vars plugin](community/sops/sops_vars.md#ansible-collections-community-sops-sops-vars)

ANSIBLE_SOPS_ENABLE_LOCAL_KEYSERVICE
:   Tell sops to use local key service.

    This corresponds to the sops `--enable-local-keyservice` option.

    *Used by:*
    [community.sops.sops lookup plugin](community/sops/sops_lookup.md#ansible-collections-community-sops-sops-lookup),
    [community.sops.sops vars plugin](community/sops/sops_vars.md#ansible-collections-community-sops-sops-vars)

ANSIBLE_SOPS_KEYSERVICE
:   Specify key services to use next to the local one.

    A key service must be specified in the form `protocol://address`, for example `tcp://myserver.com:5000`.

    This corresponds to the sops `--keyservice` option.

    *Used by:*
    [community.sops.sops lookup plugin](community/sops/sops_lookup.md#ansible-collections-community-sops-sops-lookup),
    [community.sops.sops vars plugin](community/sops/sops_vars.md#ansible-collections-community-sops-sops-vars)

ANSIBLE_SSH_ARGS
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [ansible.builtin.paramiko_ssh connection plugin](ansible/builtin/paramiko_ssh_connection.md#ansible-collections-ansible-builtin-paramiko-ssh-connection),
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection),
    [ansible.netcommon.libssh connection plugin](ansible/netcommon/libssh_connection.md#ansible-collections-ansible-netcommon-libssh-connection)

ANSIBLE_SSH_COMMON_ARGS
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [ansible.builtin.paramiko_ssh connection plugin](ansible/builtin/paramiko_ssh_connection.md#ansible-collections-ansible-builtin-paramiko-ssh-connection),
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection),
    [ansible.netcommon.libssh connection plugin](ansible/netcommon/libssh_connection.md#ansible-collections-ansible-netcommon-libssh-connection)

ANSIBLE_SSH_CONTROL_PATH
:   This is the location to save SSH’s ControlPath sockets, it uses SSH’s variable substitution.

    Since 2.3, if null (default), ansible will generate a unique hash. Use ``%(directory)s`` to indicate where to use the control dir path setting.

    Before 2.3 it defaulted to ``control_path=%(directory)s/ansible-ssh-%%h-%%p-%%r``.

    Be aware that this setting is ignored if `-o ControlPath` is set in ssh args.

    *Used by:*
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection)

ANSIBLE_SSH_CONTROL_PATH_DIR
:   This sets the directory to use for ssh control path if the control path setting is null.

    Also, provides the ``%(directory)s`` variable for the control path setting.

    *Used by:*
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection)

ANSIBLE_SSH_EXECUTABLE
:   This defines the location of the SSH binary. It defaults to `ssh` which will use the first SSH binary available in $PATH.

    This option is usually not required, it might be useful when access to system SSH is restricted, or when using SSH wrappers to connect to remote hosts.

    *Used by:*
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection)

ANSIBLE_SSH_EXTRA_ARGS
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [ansible.builtin.paramiko_ssh connection plugin](ansible/builtin/paramiko_ssh_connection.md#ansible-collections-ansible-builtin-paramiko-ssh-connection),
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection),
    [ansible.netcommon.libssh connection plugin](ansible/netcommon/libssh_connection.md#ansible-collections-ansible-netcommon-libssh-connection)

ANSIBLE_SSH_HOST_KEY_CHECKING
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [ansible.builtin.paramiko_ssh connection plugin](ansible/builtin/paramiko_ssh_connection.md#ansible-collections-ansible-builtin-paramiko-ssh-connection),
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection),
    [ansible.netcommon.libssh connection plugin](ansible/netcommon/libssh_connection.md#ansible-collections-ansible-netcommon-libssh-connection),
    [ansible.netcommon.netconf connection plugin](ansible/netcommon/netconf_connection.md#ansible-collections-ansible-netcommon-netconf-connection),
    [ansible.netcommon.network_cli connection plugin](ansible/netcommon/network_cli_connection.md#ansible-collections-ansible-netcommon-network-cli-connection)

ANSIBLE_SSH_PIPELINING
:   Pipelining reduces the number of connection operations required to execute a module on the remote server, by executing many Ansible modules without actual file transfers.

    This can result in a very significant performance improvement when enabled.

    However this can conflict with privilege escalation (become). For example, when using sudo operations you must first disable ‘requiretty’ in the sudoers file for the target hosts, which is why this feature is disabled by default.

    *Used by:*
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection)

ANSIBLE_SSH_RETRIES
:   Number of attempts to connect.

    Ansible retries connections only if it gets an SSH error with a return code of 255.

    Any errors with return codes other than 255 indicate an issue with program execution.

    *Used by:*
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection)

ANSIBLE_SSH_TIMEOUT
:   This is the default amount of time we will wait while establishing an SSH connection.

    It also controls how long we can wait to access reading the connection once established (select on the socket).

    *Used by:*
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection)

ANSIBLE_SSH_TRANSFER_METHOD
:   Preferred method to use when transferring files over ssh

    Setting to ‘smart’ (default) will try them in order, until one succeeds or they all fail

    For OpenSSH >=9.0 you must add an additional option to enable scp (scp_extra_args=”-O”)

    Using ‘piped’ creates an ssh pipe with `dd` on either side to copy the data

    *Used by:*
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection)

ANSIBLE_SSH_USETTY
:   add -tt to ssh commands to force tty allocation.

    *Used by:*
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection)

ANSIBLE_SSHPASS_PROMPT
:   Password prompt that sshpass should search for. Supported by sshpass 1.06 and up.

    Defaults to `Enter PIN for` when pkcs11_provider is set.

    *Used by:*
    [ansible.builtin.ssh connection plugin](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection)

ANSIBLE_SU_EXE
:   Su executable

    *Used by:*
    [ansible.builtin.su become plugin](ansible/builtin/su_become.md#ansible-collections-ansible-builtin-su-become)

ANSIBLE_SU_FLAGS
:   Options to pass to su

    *Used by:*
    [ansible.builtin.su become plugin](ansible/builtin/su_become.md#ansible-collections-ansible-builtin-su-become)

ANSIBLE_SU_PASS
:   Password to pass to su

    *Used by:*
    [ansible.builtin.su become plugin](ansible/builtin/su_become.md#ansible-collections-ansible-builtin-su-become)

ANSIBLE_SU_PROMPT_L10N
:   List of localized strings to match for prompt detection

    If empty we’ll use the built in one

    Do NOT add a colon (:) to your custom entries. Ansible adds a colon at the end of each prompt; if you add another one in your string, your prompt will fail with a “Timeout” error.

    *Used by:*
    [ansible.builtin.su become plugin](ansible/builtin/su_become.md#ansible-collections-ansible-builtin-su-become)

ANSIBLE_SU_USER
:   User you ‘become’ to execute the task

    *Used by:*
    [ansible.builtin.su become plugin](ansible/builtin/su_become.md#ansible-collections-ansible-builtin-su-become)

ANSIBLE_SUDO_EXE
:   Sudo executable

    *Used by:*
    [ansible.builtin.sudo become plugin](ansible/builtin/sudo_become.md#ansible-collections-ansible-builtin-sudo-become),
    [containers.podman.podman_unshare become plugin](containers/podman/podman_unshare_become.md#ansible-collections-containers-podman-podman-unshare-become)

ANSIBLE_SUDO_FLAGS
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [ansible.builtin.sudo become plugin](ansible/builtin/sudo_become.md#ansible-collections-ansible-builtin-sudo-become),
    [community.general.sudosu become plugin](community/general/sudosu_become.md#ansible-collections-community-general-sudosu-become)

ANSIBLE_SUDO_PASS
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [ansible.builtin.sudo become plugin](ansible/builtin/sudo_become.md#ansible-collections-ansible-builtin-sudo-become),
    [community.general.sudosu become plugin](community/general/sudosu_become.md#ansible-collections-community-general-sudosu-become),
    [containers.podman.podman_unshare become plugin](containers/podman/podman_unshare_become.md#ansible-collections-containers-podman-podman-unshare-become)

ANSIBLE_SUDO_USER
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [ansible.builtin.sudo become plugin](ansible/builtin/sudo_become.md#ansible-collections-ansible-builtin-sudo-become),
    [community.general.sudosu become plugin](community/general/sudosu_become.md#ansible-collections-community-general-sudosu-become),
    [containers.podman.podman_unshare become plugin](containers/podman/podman_unshare_become.md#ansible-collections-containers-podman-podman-unshare-become)

ANSIBLE_SYSLOG_SETUP
:   Log setup tasks.

    *Used by:*
    [community.general.syslog_json callback plugin](community/general/syslog_json_callback.md#ansible-collections-community-general-syslog-json-callback)

ANSIBLE_SYSTEM_TMPDIRS
:   List of valid system temporary directories on the managed machine for Ansible to validate `remote_tmp` against, when specific permissions are needed. These must be world readable, writable, and executable. This list should only contain directories which the system administrator has pre-created with the proper ownership and permissions otherwise security issues can arise.

    When `remote_tmp` is required to be a system temp dir and it does not match any in the list, the first one from the list will be used instead.

    *Used by:*
    [ansible.builtin.sh shell plugin](ansible/builtin/sh_shell.md#ansible-collections-ansible-builtin-sh-shell),
    [ansible.posix.csh shell plugin](ansible/posix/csh_shell.md#ansible-collections-ansible-posix-csh-shell),
    [ansible.posix.fish shell plugin](ansible/posix/fish_shell.md#ansible-collections-ansible-posix-fish-shell)

ANSIBLE_VARS_PLUGIN_STAGE
:   Control when this vars plugin may be executed.

    Setting this option to `all` will run the vars plugin after importing inventory and whenever it is demanded by a task.

    Setting this option to `task` will only run the vars plugin whenever it is demanded by a task.

    Setting this option to `inventory` will only run the vars plugin after parsing inventory.

    If this option is omitted, the global *RUN_VARS_PLUGINS* configuration is used to determine when to execute the vars plugin.

    *Used by:*
    [ansible.builtin.host_group_vars vars plugin](ansible/builtin/host_group_vars_vars.md#ansible-collections-ansible-builtin-host-group-vars-vars)

ANSIBLE_VARS_SOPS_PLUGIN_CACHE
:   Whether to cache decrypted files or not.

    If the cache is disabled, the files will be decrypted for almost every task. This is very slow!

    Only disable caching if you modify the variable files during a playbook run and want the updated result to be available from the next task on.

    Note that setting *stage* to `inventory` has the same effect as setting *cache* to `true`: the variables will be loaded only once (during inventory loading) and the vars plugin will not be called for every task.

    *Used by:*
    [community.sops.sops vars plugin](community/sops/sops_vars.md#ansible-collections-community-sops-sops-vars)

ANSIBLE_VARS_SOPS_PLUGIN_STAGE
:   Control when this vars plugin may be executed.

    Setting this option to `all` will run the vars plugin after importing inventory and whenever it is demanded by a task.

    Setting this option to `task` will only run the vars plugin whenever it is demanded by a task.

    Setting this option to `inventory` will only run the vars plugin after parsing inventory.

    If this option is omitted, the global *RUN_VARS_PLUGINS* configuration is used to determine when to execute the vars plugin.

    *Used by:*
    [community.sops.sops vars plugin](community/sops/sops_vars.md#ansible-collections-community-sops-sops-vars)

ANSIBLE_XO_HOST
:   API host to XOA API.

    If the value is not specified in the inventory configuration, the value of environment variable `ANSIBLE_XO_HOST` will be used instead.

    *Used by:*
    [community.general.xen_orchestra inventory plugin](community/general/xen_orchestra_inventory.md#ansible-collections-community-general-xen-orchestra-inventory)

ANSIBLE_XO_PASSWORD
:   Xen Orchestra password.

    If the value is not specified in the inventory configuration, the value of environment variable `ANSIBLE_XO_PASSWORD` will be used instead.

    *Used by:*
    [community.general.xen_orchestra inventory plugin](community/general/xen_orchestra_inventory.md#ansible-collections-community-general-xen-orchestra-inventory)

ANSIBLE_XO_USER
:   Xen Orchestra user.

    If the value is not specified in the inventory configuration, the value of environment variable `ANSIBLE_XO_USER` will be used instead.

    *Used by:*
    [community.general.xen_orchestra inventory plugin](community/general/xen_orchestra_inventory.md#ansible-collections-community-general-xen-orchestra-inventory)

ANSIBLE_ZABBIX_AUTH_KEY
:   Specifies API authentication key

    *Used by:*
    [community.zabbix.zabbix httpapi plugin](community/zabbix/zabbix_httpapi.md#ansible-collections-community-zabbix-zabbix-httpapi)

ANSIBLE_ZABBIX_URL_PATH
:   Specifies path portion in Zabbix WebUI URL, e.g. for <https://myzabbixfarm.com/zabbixeu> zabbix_url_path=zabbixeu

    *Used by:*
    [community.zabbix.zabbix httpapi plugin](community/zabbix/zabbix_httpapi.md#ansible-collections-community-zabbix-zabbix-httpapi)

AWS_ACCESS_KEY
:   The AWS access key to use.

    *Used by:*
    [amazon.aws.aws_account_attribute lookup plugin](amazon/aws/aws_account_attribute_lookup.md#ansible-collections-amazon-aws-aws-account-attribute-lookup),
    [amazon.aws.aws_ec2 inventory plugin](amazon/aws/aws_ec2_inventory.md#ansible-collections-amazon-aws-aws-ec2-inventory),
    [amazon.aws.aws_rds inventory plugin](amazon/aws/aws_rds_inventory.md#ansible-collections-amazon-aws-aws-rds-inventory),
    [amazon.aws.aws_secret lookup plugin](amazon/aws/aws_secret_lookup.md#ansible-collections-amazon-aws-aws-secret-lookup),
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

AWS_ACCESS_KEY_ID
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [amazon.aws.aws_account_attribute lookup plugin](amazon/aws/aws_account_attribute_lookup.md#ansible-collections-amazon-aws-aws-account-attribute-lookup),
    [amazon.aws.aws_ec2 inventory plugin](amazon/aws/aws_ec2_inventory.md#ansible-collections-amazon-aws-aws-ec2-inventory),
    [amazon.aws.aws_rds inventory plugin](amazon/aws/aws_rds_inventory.md#ansible-collections-amazon-aws-aws-rds-inventory),
    [amazon.aws.aws_secret lookup plugin](amazon/aws/aws_secret_lookup.md#ansible-collections-amazon-aws-aws-secret-lookup),
    [community.general.credstash lookup plugin](community/general/credstash_lookup.md#ansible-collections-community-general-credstash-lookup),
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

AWS_DEFAULT_PROFILE
:   The AWS profile

    *Used by:*
    [amazon.aws.aws_account_attribute lookup plugin](amazon/aws/aws_account_attribute_lookup.md#ansible-collections-amazon-aws-aws-account-attribute-lookup),
    [amazon.aws.aws_ec2 inventory plugin](amazon/aws/aws_ec2_inventory.md#ansible-collections-amazon-aws-aws-ec2-inventory),
    [amazon.aws.aws_rds inventory plugin](amazon/aws/aws_rds_inventory.md#ansible-collections-amazon-aws-aws-rds-inventory),
    [amazon.aws.aws_secret lookup plugin](amazon/aws/aws_secret_lookup.md#ansible-collections-amazon-aws-aws-secret-lookup),
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

AWS_PROFILE
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [amazon.aws.aws_account_attribute lookup plugin](amazon/aws/aws_account_attribute_lookup.md#ansible-collections-amazon-aws-aws-account-attribute-lookup),
    [amazon.aws.aws_ec2 inventory plugin](amazon/aws/aws_ec2_inventory.md#ansible-collections-amazon-aws-aws-ec2-inventory),
    [amazon.aws.aws_rds inventory plugin](amazon/aws/aws_rds_inventory.md#ansible-collections-amazon-aws-aws-rds-inventory),
    [amazon.aws.aws_secret lookup plugin](amazon/aws/aws_secret_lookup.md#ansible-collections-amazon-aws-aws-secret-lookup),
    [community.general.credstash lookup plugin](community/general/credstash_lookup.md#ansible-collections-community-general-credstash-lookup),
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

AWS_REGION
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [amazon.aws.aws_account_attribute lookup plugin](amazon/aws/aws_account_attribute_lookup.md#ansible-collections-amazon-aws-aws-account-attribute-lookup),
    [amazon.aws.aws_secret lookup plugin](amazon/aws/aws_secret_lookup.md#ansible-collections-amazon-aws-aws-secret-lookup),
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

AWS_SECRET_ACCESS_KEY
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [amazon.aws.aws_account_attribute lookup plugin](amazon/aws/aws_account_attribute_lookup.md#ansible-collections-amazon-aws-aws-account-attribute-lookup),
    [amazon.aws.aws_ec2 inventory plugin](amazon/aws/aws_ec2_inventory.md#ansible-collections-amazon-aws-aws-ec2-inventory),
    [amazon.aws.aws_rds inventory plugin](amazon/aws/aws_rds_inventory.md#ansible-collections-amazon-aws-aws-rds-inventory),
    [amazon.aws.aws_secret lookup plugin](amazon/aws/aws_secret_lookup.md#ansible-collections-amazon-aws-aws-secret-lookup),
    [community.general.credstash lookup plugin](community/general/credstash_lookup.md#ansible-collections-community-general-credstash-lookup),
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

AWS_SECRET_KEY
:   The AWS secret key that corresponds to the access key.

    *Used by:*
    [amazon.aws.aws_account_attribute lookup plugin](amazon/aws/aws_account_attribute_lookup.md#ansible-collections-amazon-aws-aws-account-attribute-lookup),
    [amazon.aws.aws_ec2 inventory plugin](amazon/aws/aws_ec2_inventory.md#ansible-collections-amazon-aws-aws-ec2-inventory),
    [amazon.aws.aws_rds inventory plugin](amazon/aws/aws_rds_inventory.md#ansible-collections-amazon-aws-aws-rds-inventory),
    [amazon.aws.aws_secret lookup plugin](amazon/aws/aws_secret_lookup.md#ansible-collections-amazon-aws-aws-secret-lookup),
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

AWS_SECURITY_TOKEN
:   The AWS security token if using temporary access and secret keys.

    *Used by:*
    [amazon.aws.aws_account_attribute lookup plugin](amazon/aws/aws_account_attribute_lookup.md#ansible-collections-amazon-aws-aws-account-attribute-lookup),
    [amazon.aws.aws_ec2 inventory plugin](amazon/aws/aws_ec2_inventory.md#ansible-collections-amazon-aws-aws-ec2-inventory),
    [amazon.aws.aws_rds inventory plugin](amazon/aws/aws_rds_inventory.md#ansible-collections-amazon-aws-aws-rds-inventory),
    [amazon.aws.aws_secret lookup plugin](amazon/aws/aws_secret_lookup.md#ansible-collections-amazon-aws-aws-secret-lookup),
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

AWS_SESSION_TOKEN
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [amazon.aws.aws_account_attribute lookup plugin](amazon/aws/aws_account_attribute_lookup.md#ansible-collections-amazon-aws-aws-account-attribute-lookup),
    [amazon.aws.aws_ec2 inventory plugin](amazon/aws/aws_ec2_inventory.md#ansible-collections-amazon-aws-aws-ec2-inventory),
    [amazon.aws.aws_rds inventory plugin](amazon/aws/aws_rds_inventory.md#ansible-collections-amazon-aws-aws-rds-inventory),
    [amazon.aws.aws_secret lookup plugin](amazon/aws/aws_secret_lookup.md#ansible-collections-amazon-aws-aws-secret-lookup),
    [community.general.credstash lookup plugin](community/general/credstash_lookup.md#ansible-collections-community-general-credstash-lookup),
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

CGROUP_CONTROL_GROUP
:   Name of cgroups control group

    *Used by:*
    [ansible.posix.cgroup_perf_recap callback plugin](ansible/posix/cgroup_perf_recap_callback.md#ansible-collections-ansible-posix-cgroup-perf-recap-callback)

CGROUP_CPU_POLL_INTERVAL
:   Interval between CPU polling for determining CPU usage. A lower value may produce inaccurate results, a higher value may not be short enough to collect results for short tasks.

    *Used by:*
    [ansible.posix.cgroup_perf_recap callback plugin](ansible/posix/cgroup_perf_recap_callback.md#ansible-collections-ansible-posix-cgroup-perf-recap-callback)

CGROUP_CUR_MEM_FILE
:   Path to `memory.usage_in_bytes` file. Example `/sys/fs/cgroup/memory/ansible_profile/memory.usage_in_bytes`

    *Used by:*
    [community.general.cgroup_memory_recap callback plugin](community/general/cgroup_memory_recap_callback.md#ansible-collections-community-general-cgroup-memory-recap-callback)

CGROUP_DISPLAY_RECAP
:   Controls whether the recap is printed at the end, useful if you will automatically process the output files

    *Used by:*
    [ansible.posix.cgroup_perf_recap callback plugin](ansible/posix/cgroup_perf_recap_callback.md#ansible-collections-ansible-posix-cgroup-perf-recap-callback)

CGROUP_FILE_NAME_FORMAT
:   Format of filename. Accepts `%(counter`s), `%(task_uuid`s), `%(feature`s), `%(ext`s). Defaults to `%(feature`s.%(ext)s) when `file_per_task` is `False` and `%(counter`s-%(task_uuid)s-%(feature)s.%(ext)s) when `True`

    *Used by:*
    [ansible.posix.cgroup_perf_recap callback plugin](ansible/posix/cgroup_perf_recap_callback.md#ansible-collections-ansible-posix-cgroup-perf-recap-callback)

CGROUP_FILE_PER_TASK
:   When set as `True` along with `write_files`, this callback will write 1 file per task instead of 1 file for the entire playbook run

    *Used by:*
    [ansible.posix.cgroup_perf_recap callback plugin](ansible/posix/cgroup_perf_recap_callback.md#ansible-collections-ansible-posix-cgroup-perf-recap-callback)

CGROUP_MAX_MEM_FILE
:   Path to cgroups `memory.max_usage_in_bytes` file. Example `/sys/fs/cgroup/memory/ansible_profile/memory.max_usage_in_bytes`

    *Used by:*
    [community.general.cgroup_memory_recap callback plugin](community/general/cgroup_memory_recap_callback.md#ansible-collections-community-general-cgroup-memory-recap-callback)

CGROUP_MEMORY_POLL_INTERVAL
:   Interval between memory polling for determining memory usage. A lower value may produce inaccurate results, a higher value may not be short enough to collect results for short tasks.

    *Used by:*
    [ansible.posix.cgroup_perf_recap callback plugin](ansible/posix/cgroup_perf_recap_callback.md#ansible-collections-ansible-posix-cgroup-perf-recap-callback)

CGROUP_OUTPUT_DIR
:   Output directory for files containing recorded performance readings. If the value contains a single %s, the start time of the playbook run will be inserted in that space. Only the deepest level directory will be created if it does not exist, parent directories will not be created.

    *Used by:*
    [ansible.posix.cgroup_perf_recap callback plugin](ansible/posix/cgroup_perf_recap_callback.md#ansible-collections-ansible-posix-cgroup-perf-recap-callback)

CGROUP_OUTPUT_FORMAT
:   Output format, either CSV or JSON-seq

    *Used by:*
    [ansible.posix.cgroup_perf_recap callback plugin](ansible/posix/cgroup_perf_recap_callback.md#ansible-collections-ansible-posix-cgroup-perf-recap-callback)

CGROUP_PID_POLL_INTERVAL
:   Interval between PID polling for determining PID count. A lower value may produce inaccurate results, a higher value may not be short enough to collect results for short tasks.

    *Used by:*
    [ansible.posix.cgroup_perf_recap callback plugin](ansible/posix/cgroup_perf_recap_callback.md#ansible-collections-ansible-posix-cgroup-perf-recap-callback)

CGROUP_WRITE_FILES
:   Dictates whether files will be written containing performance readings

    *Used by:*
    [ansible.posix.cgroup_perf_recap callback plugin](ansible/posix/cgroup_perf_recap_callback.md#ansible-collections-ansible-posix-cgroup-perf-recap-callback)

CLOUDSTACK_ENDPOINT
:   URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.

    If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered.

    *Used by:*
    [ngine_io.cloudstack.instance inventory plugin](ngine_io/cloudstack/instance_inventory.md#ansible-collections-ngine-io-cloudstack-instance-inventory)

CLOUDSTACK_KEY
:   API key of the CloudStack API.

    If not given, the `CLOUDSTACK_KEY` env variable is considered.

    *Used by:*
    [ngine_io.cloudstack.instance inventory plugin](ngine_io/cloudstack/instance_inventory.md#ansible-collections-ngine-io-cloudstack-instance-inventory)

CLOUDSTACK_METHOD
:   HTTP method used to query the API endpoint.

    If not given, the `CLOUDSTACK_METHOD` env variable is considered.

    *Used by:*
    [ngine_io.cloudstack.instance inventory plugin](ngine_io/cloudstack/instance_inventory.md#ansible-collections-ngine-io-cloudstack-instance-inventory)

CLOUDSTACK_SECRET
:   Secret key of the CloudStack API.

    If not set, the `CLOUDSTACK_SECRET` env variable is considered.

    *Used by:*
    [ngine_io.cloudstack.instance inventory plugin](ngine_io/cloudstack/instance_inventory.md#ansible-collections-ngine-io-cloudstack-instance-inventory)

CLOUDSTACK_TIMEOUT
:   HTTP timeout in seconds.

    If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.

    *Used by:*
    [ngine_io.cloudstack.instance inventory plugin](ngine_io/cloudstack/instance_inventory.md#ansible-collections-ngine-io-cloudstack-instance-inventory)

CLOUDSTACK_VERIFY
:   Verify CA authority cert file.

    If not given, the `CLOUDSTACK_VERIFY` env variable is considered.

    *Used by:*
    [ngine_io.cloudstack.instance inventory plugin](ngine_io/cloudstack/instance_inventory.md#ansible-collections-ngine-io-cloudstack-instance-inventory)

COBBLER_PASSWORD
:   Cobbler authentication password

    *Used by:*
    [community.general.cobbler inventory plugin](community/general/cobbler_inventory.md#ansible-collections-community-general-cobbler-inventory)

COBBLER_SERVER
:   URL to cobbler.

    *Used by:*
    [community.general.cobbler inventory plugin](community/general/cobbler_inventory.md#ansible-collections-community-general-cobbler-inventory)

COBBLER_USER
:   Cobbler authentication user.

    *Used by:*
    [community.general.cobbler inventory plugin](community/general/cobbler_inventory.md#ansible-collections-community-general-cobbler-inventory)

CONJUR_AUTHN_TOKEN_FILE
:   Path to the access token file.

    *Used by:*
    [cyberark.conjur.conjur_variable lookup plugin](cyberark/conjur/conjur_variable_lookup.md#ansible-collections-cyberark-conjur-conjur-variable-lookup)

CONJUR_CONFIG_FILE
:   Path to the Conjur configuration file. The configuration file is a YAML file.

    *Used by:*
    [cyberark.conjur.conjur_variable lookup plugin](cyberark/conjur/conjur_variable_lookup.md#ansible-collections-cyberark-conjur-conjur-variable-lookup)

CONJUR_IDENTITY_FILE
:   Path to the Conjur identity file. The identity file follows the netrc file format convention.

    *Used by:*
    [cyberark.conjur.conjur_variable lookup plugin](cyberark/conjur/conjur_variable_lookup.md#ansible-collections-cyberark-conjur-conjur-variable-lookup)

CONTROLLER_HOST
:   The network address of your Automation Platform Controller host.

    *Used by:*
    [awx.awx.controller inventory plugin](awx/awx/controller_inventory.md#ansible-collections-awx-awx-controller-inventory),
    [awx.awx.controller_api lookup plugin](awx/awx/controller_api_lookup.md#ansible-collections-awx-awx-controller-api-lookup)

CONTROLLER_INVENTORY
:   The ID of the inventory that you wish to import.

    This is allowed to be either the inventory primary key or its named URL slug.

    Primary key values will be accepted as strings or integers, and URL slugs must be strings.

    Named URL slugs follow the syntax of “inventory_name++organization_name”.

    *Used by:*
    [awx.awx.controller inventory plugin](awx/awx/controller_inventory.md#ansible-collections-awx-awx-controller-inventory)

CONTROLLER_OAUTH_TOKEN
:   The OAuth token to use.

    *Used by:*
    [awx.awx.controller inventory plugin](awx/awx/controller_inventory.md#ansible-collections-awx-awx-controller-inventory),
    [awx.awx.controller_api lookup plugin](awx/awx/controller_api_lookup.md#ansible-collections-awx-awx-controller-api-lookup)

CONTROLLER_PASSWORD
:   The password for your controller user.

    *Used by:*
    [awx.awx.controller inventory plugin](awx/awx/controller_inventory.md#ansible-collections-awx-awx-controller-inventory),
    [awx.awx.controller_api lookup plugin](awx/awx/controller_api_lookup.md#ansible-collections-awx-awx-controller-api-lookup)

CONTROLLER_USERNAME
:   The user that you plan to use to access inventories on the controller.

    *Used by:*
    [awx.awx.controller inventory plugin](awx/awx/controller_inventory.md#ansible-collections-awx-awx-controller-inventory),
    [awx.awx.controller_api lookup plugin](awx/awx/controller_api_lookup.md#ansible-collections-awx-awx-controller-api-lookup)

CONTROLLER_VERIFY_SSL
:   Specify whether Ansible should verify the SSL certificate of the controller host.

    Defaults to True, but this is handled by the shared module_utils code

    *Used by:*
    [awx.awx.controller inventory plugin](awx/awx/controller_inventory.md#ansible-collections-awx-awx-controller-inventory),
    [awx.awx.controller_api lookup plugin](awx/awx/controller_api_lookup.md#ansible-collections-awx-awx-controller-api-lookup)

DO_API_TOKEN
:   DigitalOcean OAuth token.

    Template expressions can be used in this field.

    *Used by:*
    [community.digitalocean.digitalocean inventory plugin](community/digitalocean/digitalocean_inventory.md#ansible-collections-community-digitalocean-digitalocean-inventory)

DSV_CLIENT_ID
:   The client_id with which to request the Access Grant.

    *Used by:*
    [community.general.dsv lookup plugin](community/general/dsv_lookup.md#ansible-collections-community-general-dsv-lookup)

DSV_CLIENT_SECRET
:   The client secret associated with the specific *client_id*.

    *Used by:*
    [community.general.dsv lookup plugin](community/general/dsv_lookup.md#ansible-collections-community-general-dsv-lookup)

DSV_TENANT
:   The first format parameter in the default *url_template*.

    *Used by:*
    [community.general.dsv lookup plugin](community/general/dsv_lookup.md#ansible-collections-community-general-dsv-lookup)

DSV_TLD
:   The top-level domain of the tenant; the second format parameter in the default *url_template*.

    *Used by:*
    [community.general.dsv lookup plugin](community/general/dsv_lookup.md#ansible-collections-community-general-dsv-lookup)

DSV_URL_TEMPLATE
:   The path to prepend to the base URL to form a valid REST API request.

    *Used by:*
    [community.general.dsv lookup plugin](community/general/dsv_lookup.md#ansible-collections-community-general-dsv-lookup)

EC2_ACCESS_KEY
:   The AWS access key to use.

    *Used by:*
    [amazon.aws.aws_account_attribute lookup plugin](amazon/aws/aws_account_attribute_lookup.md#ansible-collections-amazon-aws-aws-account-attribute-lookup),
    [amazon.aws.aws_ec2 inventory plugin](amazon/aws/aws_ec2_inventory.md#ansible-collections-amazon-aws-aws-ec2-inventory),
    [amazon.aws.aws_rds inventory plugin](amazon/aws/aws_rds_inventory.md#ansible-collections-amazon-aws-aws-rds-inventory),
    [amazon.aws.aws_secret lookup plugin](amazon/aws/aws_secret_lookup.md#ansible-collections-amazon-aws-aws-secret-lookup),
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

EC2_REGION
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [amazon.aws.aws_account_attribute lookup plugin](amazon/aws/aws_account_attribute_lookup.md#ansible-collections-amazon-aws-aws-account-attribute-lookup),
    [amazon.aws.aws_secret lookup plugin](amazon/aws/aws_secret_lookup.md#ansible-collections-amazon-aws-aws-secret-lookup),
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

EC2_SECRET_KEY
:   The AWS secret key that corresponds to the access key.

    *Used by:*
    [amazon.aws.aws_account_attribute lookup plugin](amazon/aws/aws_account_attribute_lookup.md#ansible-collections-amazon-aws-aws-account-attribute-lookup),
    [amazon.aws.aws_ec2 inventory plugin](amazon/aws/aws_ec2_inventory.md#ansible-collections-amazon-aws-aws-ec2-inventory),
    [amazon.aws.aws_rds inventory plugin](amazon/aws/aws_rds_inventory.md#ansible-collections-amazon-aws-aws-rds-inventory),
    [amazon.aws.aws_secret lookup plugin](amazon/aws/aws_secret_lookup.md#ansible-collections-amazon-aws-aws-secret-lookup),
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

EC2_SECURITY_TOKEN
:   The AWS security token if using temporary access and secret keys.

    *Used by:*
    [amazon.aws.aws_account_attribute lookup plugin](amazon/aws/aws_account_attribute_lookup.md#ansible-collections-amazon-aws-aws-account-attribute-lookup),
    [amazon.aws.aws_ec2 inventory plugin](amazon/aws/aws_ec2_inventory.md#ansible-collections-amazon-aws-aws-ec2-inventory),
    [amazon.aws.aws_rds inventory plugin](amazon/aws/aws_rds_inventory.md#ansible-collections-amazon-aws-aws-rds-inventory),
    [amazon.aws.aws_secret lookup plugin](amazon/aws/aws_secret_lookup.md#ansible-collections-amazon-aws-aws-secret-lookup),
    [community.hashi_vault.hashi_vault lookup plugin](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup),
    [community.hashi_vault.vault_kv1_get lookup plugin](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup),
    [community.hashi_vault.vault_kv2_get lookup plugin](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup),
    [community.hashi_vault.vault_login lookup plugin](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup),
    [community.hashi_vault.vault_read lookup plugin](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup),
    [community.hashi_vault.vault_token_create lookup plugin](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup),
    [community.hashi_vault.vault_write lookup plugin](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup)

ELASTIC_APM_API_KEY
:   Use the APM API key

    *Used by:*
    [community.general.elastic callback plugin](community/general/elastic_callback.md#ansible-collections-community-general-elastic-callback)

ELASTIC_APM_SECRET_TOKEN
:   Use the APM server token

    *Used by:*
    [community.general.elastic callback plugin](community/general/elastic_callback.md#ansible-collections-community-general-elastic-callback)

ELASTIC_APM_SERVER_URL
:   Use the APM server and its environment variables.

    *Used by:*
    [community.general.elastic callback plugin](community/general/elastic_callback.md#ansible-collections-community-general-elastic-callback)

ELASTIC_APM_SERVICE_NAME
:   The service name resource attribute.

    *Used by:*
    [community.general.elastic callback plugin](community/general/elastic_callback.md#ansible-collections-community-general-elastic-callback)

ELASTIC_APM_VERIFY_SERVER_CERT
:   Verifies the SSL certificate if an HTTPS connection.

    *Used by:*
    [community.general.elastic callback plugin](community/general/elastic_callback.md#ansible-collections-community-general-elastic-callback)

ETCDCTL_CACERT
:   etcd3 CA authority.

    *Used by:*
    [community.general.etcd3 lookup plugin](community/general/etcd3_lookup.md#ansible-collections-community-general-etcd3-lookup)

ETCDCTL_CERT
:   etcd3 client certificate.

    *Used by:*
    [community.general.etcd3 lookup plugin](community/general/etcd3_lookup.md#ansible-collections-community-general-etcd3-lookup)

ETCDCTL_DIAL_TIMEOUT
:   Client timeout.

    *Used by:*
    [community.general.etcd3 lookup plugin](community/general/etcd3_lookup.md#ansible-collections-community-general-etcd3-lookup)

ETCDCTL_ENDPOINTS
:   Counterpart of `ETCDCTL_ENDPOINTS` environment variable. Specify the etcd3 connection with and URL form eg. `https://hostname:2379` or `<host>:<port>` form.

    The `host` part is overwritten by *host* option, if defined.

    The `port` part is overwritten by *port* option, if defined.

    *Used by:*
    [community.general.etcd3 lookup plugin](community/general/etcd3_lookup.md#ansible-collections-community-general-etcd3-lookup)

ETCDCTL_KEY
:   etcd3 client private key.

    *Used by:*
    [community.general.etcd3 lookup plugin](community/general/etcd3_lookup.md#ansible-collections-community-general-etcd3-lookup)

ETCDCTL_PASSWORD
:   Authenticated user password.

    *Used by:*
    [community.general.etcd3 lookup plugin](community/general/etcd3_lookup.md#ansible-collections-community-general-etcd3-lookup)

ETCDCTL_USER
:   Authenticated user name.

    *Used by:*
    [community.general.etcd3 lookup plugin](community/general/etcd3_lookup.md#ansible-collections-community-general-etcd3-lookup)

FOREMAN_CALLBACK_DISABLE
:   Toggle to make the callback plugin disable itself even if it is loaded.

    It can be set to ‘1’ to prevent the plugin from being used even if it gets loaded.

    *Used by:*
    [theforeman.foreman.foreman callback plugin](theforeman/foreman/foreman_callback.md#ansible-collections-theforeman-foreman-foreman-callback)

FOREMAN_DIR_STORE
:   When set, callback does not perform HTTP calls but stores results in a given directory.

    For each report, new file in the form of SEQ_NO-hostname.json is created.

    For each facts, new file in the form of SEQ_NO-hostname.json is created.

    The value must be a valid directory.

    This is meant for debugging and testing purposes.

    When set to blank (default) this functionality is turned off.

    *Used by:*
    [theforeman.foreman.foreman callback plugin](theforeman/foreman/foreman_callback.md#ansible-collections-theforeman-foreman-foreman-callback)

FOREMAN_PASSWORD
:   Password of the user accessing the Foreman server.

    *Used by:*
    [theforeman.foreman.foreman inventory plugin](theforeman/foreman/foreman_inventory.md#ansible-collections-theforeman-foreman-foreman-inventory)

FOREMAN_PROXY_URL
:   URL of the Foreman Smart Proxy server.

    *Used by:*
    [theforeman.foreman.foreman callback plugin](theforeman/foreman/foreman_callback.md#ansible-collections-theforeman-foreman-foreman-callback)

FOREMAN_REPORT_TYPE
:   endpoint type for reports: foreman or proxy

    *Used by:*
    [theforeman.foreman.foreman callback plugin](theforeman/foreman/foreman_callback.md#ansible-collections-theforeman-foreman-foreman-callback)

FOREMAN_SERVER
:   URL of the Foreman server.

    *Used by:*
    [theforeman.foreman.foreman callback plugin](theforeman/foreman/foreman_callback.md#ansible-collections-theforeman-foreman-foreman-callback),
    [theforeman.foreman.foreman inventory plugin](theforeman/foreman/foreman_inventory.md#ansible-collections-theforeman-foreman-foreman-inventory)

FOREMAN_SERVER_URL
:   URL of the Foreman server.

    *Used by:*
    [theforeman.foreman.foreman callback plugin](theforeman/foreman/foreman_callback.md#ansible-collections-theforeman-foreman-foreman-callback),
    [theforeman.foreman.foreman inventory plugin](theforeman/foreman/foreman_inventory.md#ansible-collections-theforeman-foreman-foreman-inventory)

FOREMAN_SSL_CERT
:   X509 certificate to authenticate to Foreman if https is used

    *Used by:*
    [theforeman.foreman.foreman callback plugin](theforeman/foreman/foreman_callback.md#ansible-collections-theforeman-foreman-foreman-callback)

FOREMAN_SSL_KEY
:   the corresponding private key

    *Used by:*
    [theforeman.foreman.foreman callback plugin](theforeman/foreman/foreman_callback.md#ansible-collections-theforeman-foreman-foreman-callback)

FOREMAN_SSL_VERIFY
:   Toggle to decide whether to verify the Foreman certificate.

    It can be set to ‘1’ to verify SSL certificates using the installed CAs or to a path pointing to a CA bundle.

    Set to ‘0’ to disable certificate checking.

    *Used by:*
    [theforeman.foreman.foreman callback plugin](theforeman/foreman/foreman_callback.md#ansible-collections-theforeman-foreman-foreman-callback)

FOREMAN_URL
:   URL of the Foreman server.

    *Used by:*
    [theforeman.foreman.foreman callback plugin](theforeman/foreman/foreman_callback.md#ansible-collections-theforeman-foreman-foreman-callback),
    [theforeman.foreman.foreman inventory plugin](theforeman/foreman/foreman_inventory.md#ansible-collections-theforeman-foreman-foreman-inventory)

FOREMAN_USER
:   Username accessing the Foreman server.

    *Used by:*
    [theforeman.foreman.foreman inventory plugin](theforeman/foreman/foreman_inventory.md#ansible-collections-theforeman-foreman-foreman-inventory)

FOREMAN_USERNAME
:   Username accessing the Foreman server.

    *Used by:*
    [theforeman.foreman.foreman inventory plugin](theforeman/foreman/foreman_inventory.md#ansible-collections-theforeman-foreman-foreman-inventory)

FOREMAN_VALIDATE_CERTS
:   Whether or not to verify the TLS certificates of the Foreman server.

    *Used by:*
    [theforeman.foreman.foreman inventory plugin](theforeman/foreman/foreman_inventory.md#ansible-collections-theforeman-foreman-foreman-inventory)

GCE_CREDENTIALS_FILE_PATH
:   The path of a Service Account JSON file if serviceaccount is selected as type.

    *Used by:*
    [google.cloud.gcp_compute inventory plugin](google/cloud/gcp_compute_inventory.md#ansible-collections-google-cloud-gcp-compute-inventory)

GCP_AUTH_KIND
:   The type of credential used.

    *Used by:*
    [google.cloud.gcp_compute inventory plugin](google/cloud/gcp_compute_inventory.md#ansible-collections-google-cloud-gcp-compute-inventory)

GCP_SCOPES
:   list of authentication scopes

    *Used by:*
    [google.cloud.gcp_compute inventory plugin](google/cloud/gcp_compute_inventory.md#ansible-collections-google-cloud-gcp-compute-inventory)

GCP_SERVICE_ACCOUNT_CONTENTS
:   A string representing the contents of a Service Account JSON file. This should not be passed in as a dictionary, but a string that has the exact contents of a service account json file (valid JSON).

    *Used by:*
    [google.cloud.gcp_compute inventory plugin](google/cloud/gcp_compute_inventory.md#ansible-collections-google-cloud-gcp-compute-inventory)

GCP_SERVICE_ACCOUNT_EMAIL
:   An optional service account email address if machineaccount is selected and the user does not wish to use the default email.

    *Used by:*
    [google.cloud.gcp_compute inventory plugin](google/cloud/gcp_compute_inventory.md#ansible-collections-google-cloud-gcp-compute-inventory)

GCP_SERVICE_ACCOUNT_FILE
:   The path of a Service Account JSON file if serviceaccount is selected as type.

    *Used by:*
    [google.cloud.gcp_compute inventory plugin](google/cloud/gcp_compute_inventory.md#ansible-collections-google-cloud-gcp-compute-inventory)

GITLAB_API_TOKEN
:   GitLab token for logging in.

    *Used by:*
    [community.general.gitlab_runners inventory plugin](community/general/gitlab_runners_inventory.md#ansible-collections-community-general-gitlab-runners-inventory)

GITLAB_FILTER
:   filter runners from GitLab API

    *Used by:*
    [community.general.gitlab_runners inventory plugin](community/general/gitlab_runners_inventory.md#ansible-collections-community-general-gitlab-runners-inventory)

GITLAB_SERVER_URL
:   The URL of the GitLab server, with protocol (i.e. http or https).

    *Used by:*
    [community.general.gitlab_runners inventory plugin](community/general/gitlab_runners_inventory.md#ansible-collections-community-general-gitlab-runners-inventory)

GRAFANA_API_KEY
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [community.grafana.grafana_annotations callback plugin](community/grafana/grafana_annotations_callback.md#ansible-collections-community-grafana-grafana-annotations-callback),
    [community.grafana.grafana_dashboard lookup plugin](community/grafana/grafana_dashboard_lookup.md#ansible-collections-community-grafana-grafana-dashboard-lookup)

GRAFANA_DASHBOARD_ID
:   The grafana dashboard id where the annotation shall be created.

    *Used by:*
    [community.grafana.grafana_annotations callback plugin](community/grafana/grafana_annotations_callback.md#ansible-collections-community-grafana-grafana-annotations-callback)

GRAFANA_DASHBOARD_SEARCH
:   optional filter for dashboard search.

    *Used by:*
    [community.grafana.grafana_dashboard lookup plugin](community/grafana/grafana_dashboard_lookup.md#ansible-collections-community-grafana-grafana-dashboard-lookup)

GRAFANA_ORG_ID
:   grafana organisation id.

    *Used by:*
    [community.grafana.grafana_dashboard lookup plugin](community/grafana/grafana_dashboard_lookup.md#ansible-collections-community-grafana-grafana-dashboard-lookup)

GRAFANA_PANEL_IDS
:   The grafana panel ids where the annotation shall be created. Give a single integer or a comma-separated list of integers.

    *Used by:*
    [community.grafana.grafana_annotations callback plugin](community/grafana/grafana_annotations_callback.md#ansible-collections-community-grafana-grafana-annotations-callback)

GRAFANA_PASSWORD
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [community.grafana.grafana_annotations callback plugin](community/grafana/grafana_annotations_callback.md#ansible-collections-community-grafana-grafana-annotations-callback),
    [community.grafana.grafana_dashboard lookup plugin](community/grafana/grafana_dashboard_lookup.md#ansible-collections-community-grafana-grafana-dashboard-lookup)

GRAFANA_URL
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [community.grafana.grafana_annotations callback plugin](community/grafana/grafana_annotations_callback.md#ansible-collections-community-grafana-grafana-annotations-callback),
    [community.grafana.grafana_dashboard lookup plugin](community/grafana/grafana_dashboard_lookup.md#ansible-collections-community-grafana-grafana-dashboard-lookup)

GRAFANA_USER
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [community.grafana.grafana_annotations callback plugin](community/grafana/grafana_annotations_callback.md#ansible-collections-community-grafana-grafana-annotations-callback),
    [community.grafana.grafana_dashboard lookup plugin](community/grafana/grafana_dashboard_lookup.md#ansible-collections-community-grafana-grafana-dashboard-lookup)

GRAFANA_VALIDATE_CERT
:   validate the SSL certificate of the Grafana server. (For HTTPS url)

    *Used by:*
    [community.grafana.grafana_annotations callback plugin](community/grafana/grafana_annotations_callback.md#ansible-collections-community-grafana-grafana-annotations-callback)

HETZNER_DNS_TOKEN
:   The token for the Hetzner API.

    If not provided, will be read from the environment variable `HETZNER_DNS_TOKEN`.

    *Used by:*
    [community.dns.hetzner_dns_records inventory plugin](community/dns/hetzner_dns_records_inventory.md#ansible-collections-community-dns-hetzner-dns-records-inventory)

HIPCHAT_API_VERSION
:   HipChat API version, v1 or v2.

    *Used by:*
    [community.general.hipchat callback plugin](community/general/hipchat_callback.md#ansible-collections-community-general-hipchat-callback)

HIPCHAT_FROM
:   Name to post as

    *Used by:*
    [community.general.hipchat callback plugin](community/general/hipchat_callback.md#ansible-collections-community-general-hipchat-callback)

HIPCHAT_NOTIFY
:   Add notify flag to important messages

    *Used by:*
    [community.general.hipchat callback plugin](community/general/hipchat_callback.md#ansible-collections-community-general-hipchat-callback)

HIPCHAT_ROOM
:   HipChat room to post in.

    *Used by:*
    [community.general.hipchat callback plugin](community/general/hipchat_callback.md#ansible-collections-community-general-hipchat-callback)

HIPCHAT_TOKEN
:   HipChat API token for v1 or v2 API.

    *Used by:*
    [community.general.hipchat callback plugin](community/general/hipchat_callback.md#ansible-collections-community-general-hipchat-callback)

HROBOT_API_PASSWORD
:   The password for the Robot webservice user.

    *Used by:*
    [community.hrobot.robot inventory plugin](community/hrobot/robot_inventory.md#ansible-collections-community-hrobot-robot-inventory)

HROBOT_API_USER
:   The username for the Robot webservice user.

    *Used by:*
    [community.hrobot.robot inventory plugin](community/hrobot/robot_inventory.md#ansible-collections-community-hrobot-robot-inventory)

HTTP_AGENT
:   The HTTP ‘User-agent’ value to set in HTTP requets.

    *Used by:*
    [community.grafana.grafana_annotations callback plugin](community/grafana/grafana_annotations_callback.md#ansible-collections-community-grafana-grafana-annotations-callback)

INFOBLOX_HOST
:   Specifies the DNS host name or address for connecting to the remote instance of NIOS WAPI over REST.

    Value can also be specified using `INFOBLOX_HOST` environment variable.

    *Used by:*
    [infoblox.nios_modules.nios_inventory inventory plugin](infoblox/nios_modules/nios_inventory_inventory.md#ansible-collections-infoblox-nios-modules-nios-inventory-inventory)

INFOBLOX_PASSWORD
:   Specifies the password to use to authenticate the connection to the remote instance of NIOS.

    Value can also be specified using `INFOBLOX_PASSWORD` environment variable.

    *Used by:*
    [infoblox.nios_modules.nios_inventory inventory plugin](infoblox/nios_modules/nios_inventory_inventory.md#ansible-collections-infoblox-nios-modules-nios-inventory-inventory)

INFOBLOX_USERNAME
:   Configures the username to use to authenticate the connection to the remote instance of NIOS.

    Value can also be specified using `INFOBLOX_USERNAME` environment variable.

    *Used by:*
    [infoblox.nios_modules.nios_inventory inventory plugin](infoblox/nios_modules/nios_inventory_inventory.md#ansible-collections-infoblox-nios-modules-nios-inventory-inventory)

JABBER_PASS
:   Password for the user to the jabber server

    *Used by:*
    [community.general.jabber callback plugin](community/general/jabber_callback.md#ansible-collections-community-general-jabber-callback)

JABBER_SERV
:   connection info to jabber server

    *Used by:*
    [community.general.jabber callback plugin](community/general/jabber_callback.md#ansible-collections-community-general-jabber-callback)

JABBER_TO
:   chat identifier that will receive the message

    *Used by:*
    [community.general.jabber callback plugin](community/general/jabber_callback.md#ansible-collections-community-general-jabber-callback)

JABBER_USER
:   Jabber user to authenticate as

    *Used by:*
    [community.general.jabber callback plugin](community/general/jabber_callback.md#ansible-collections-community-general-jabber-callback)

JUNIT_FAIL_ON_CHANGE
:   Consider any tasks reporting “changed” as a junit test failure

    *Used by:*
    [ansible.builtin.junit callback plugin](ansible/builtin/junit_callback.md#ansible-collections-ansible-builtin-junit-callback)

JUNIT_FAIL_ON_IGNORE
:   Consider failed tasks as a junit test failure even if ignore_on_error is set

    *Used by:*
    [ansible.builtin.junit callback plugin](ansible/builtin/junit_callback.md#ansible-collections-ansible-builtin-junit-callback)

JUNIT_HIDE_TASK_ARGUMENTS
:   Hide the arguments for a task

    *Used by:*
    [ansible.builtin.junit callback plugin](ansible/builtin/junit_callback.md#ansible-collections-ansible-builtin-junit-callback)

JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT
:   Should the setup tasks be included in the final report

    *Used by:*
    [ansible.builtin.junit callback plugin](ansible/builtin/junit_callback.md#ansible-collections-ansible-builtin-junit-callback)

JUNIT_OUTPUT_DIR
:   Directory to write XML files to.

    *Used by:*
    [ansible.builtin.junit callback plugin](ansible/builtin/junit_callback.md#ansible-collections-ansible-builtin-junit-callback)

JUNIT_REPLACE_OUT_OF_TREE_PATH
:   Replace the directory portion of an out-of-tree relative task path with the given placeholder

    *Used by:*
    [ansible.builtin.junit callback plugin](ansible/builtin/junit_callback.md#ansible-collections-ansible-builtin-junit-callback)

JUNIT_TASK_CLASS
:   Configure the output to be one class per yaml file

    *Used by:*
    [ansible.builtin.junit callback plugin](ansible/builtin/junit_callback.md#ansible-collections-ansible-builtin-junit-callback)

JUNIT_TASK_RELATIVE_PATH
:   Configure the output to use relative paths to given directory

    *Used by:*
    [ansible.builtin.junit callback plugin](ansible/builtin/junit_callback.md#ansible-collections-ansible-builtin-junit-callback)

JUNIT_TEST_CASE_PREFIX
:   Consider a task only as test case if it has this value as prefix. Additionally failing tasks are recorded as failed test cases.

    *Used by:*
    [ansible.builtin.junit callback plugin](ansible/builtin/junit_callback.md#ansible-collections-ansible-builtin-junit-callback)

K8S_AUTH_API_KEY
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [community.okd.oc connection plugin](community/okd/oc_connection.md#ansible-collections-community-okd-oc-connection),
    [kubernetes.core.kubectl connection plugin](kubernetes/core/kubectl_connection.md#ansible-collections-kubernetes-core-kubectl-connection)

K8S_AUTH_CERT_FILE
:   Path to a certificate used to authenticate with the API.

    *Used by:*
    [community.okd.oc connection plugin](community/okd/oc_connection.md#ansible-collections-community-okd-oc-connection),
    [kubernetes.core.kubectl connection plugin](kubernetes/core/kubectl_connection.md#ansible-collections-kubernetes-core-kubectl-connection)

K8S_AUTH_CONTAINER
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [community.okd.oc connection plugin](community/okd/oc_connection.md#ansible-collections-community-okd-oc-connection),
    [kubernetes.core.kubectl connection plugin](kubernetes/core/kubectl_connection.md#ansible-collections-kubernetes-core-kubectl-connection)

K8S_AUTH_CONTEXT
:   The name of a context found in the K8s config file.

    *Used by:*
    [community.okd.oc connection plugin](community/okd/oc_connection.md#ansible-collections-community-okd-oc-connection),
    [kubernetes.core.kubectl connection plugin](kubernetes/core/kubectl_connection.md#ansible-collections-kubernetes-core-kubectl-connection)

K8S_AUTH_EXTRA_ARGS
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [community.okd.oc connection plugin](community/okd/oc_connection.md#ansible-collections-community-okd-oc-connection),
    [kubernetes.core.kubectl connection plugin](kubernetes/core/kubectl_connection.md#ansible-collections-kubernetes-core-kubectl-connection)

K8S_AUTH_HOST
:   URL for accessing the API.

    *Used by:*
    [community.okd.oc connection plugin](community/okd/oc_connection.md#ansible-collections-community-okd-oc-connection),
    [kubernetes.core.kubectl connection plugin](kubernetes/core/kubectl_connection.md#ansible-collections-kubernetes-core-kubectl-connection)

K8S_AUTH_KEY_FILE
:   Path to a key file used to authenticate with the API.

    *Used by:*
    [community.okd.oc connection plugin](community/okd/oc_connection.md#ansible-collections-community-okd-oc-connection),
    [kubernetes.core.kubectl connection plugin](kubernetes/core/kubectl_connection.md#ansible-collections-kubernetes-core-kubectl-connection)

K8S_AUTH_KUBECONFIG
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [community.okd.oc connection plugin](community/okd/oc_connection.md#ansible-collections-community-okd-oc-connection),
    [kubernetes.core.kubectl connection plugin](kubernetes/core/kubectl_connection.md#ansible-collections-kubernetes-core-kubectl-connection)

K8S_AUTH_NAMESPACE
:   The namespace of the pod

    *Used by:*
    [community.okd.oc connection plugin](community/okd/oc_connection.md#ansible-collections-community-okd-oc-connection),
    [kubernetes.core.kubectl connection plugin](kubernetes/core/kubectl_connection.md#ansible-collections-kubernetes-core-kubectl-connection)

K8S_AUTH_PASSWORD
:   Provide a password for authenticating with the API.

    Please be aware that this passes information directly on the command line and it could expose sensitive data. We recommend using the file based authentication options instead.

    *Used by:*
    [kubernetes.core.kubectl connection plugin](kubernetes/core/kubectl_connection.md#ansible-collections-kubernetes-core-kubectl-connection)

K8S_AUTH_POD
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [community.okd.oc connection plugin](community/okd/oc_connection.md#ansible-collections-community-okd-oc-connection),
    [kubernetes.core.kubectl connection plugin](kubernetes/core/kubectl_connection.md#ansible-collections-kubernetes-core-kubectl-connection)

K8S_AUTH_SERVER
:   URL for accessing the API.

    *Used by:*
    [community.okd.oc connection plugin](community/okd/oc_connection.md#ansible-collections-community-okd-oc-connection),
    [kubernetes.core.kubectl connection plugin](kubernetes/core/kubectl_connection.md#ansible-collections-kubernetes-core-kubectl-connection)

K8S_AUTH_SSL_CA_CERT
:   Path to a CA certificate used to authenticate with the API.

    *Used by:*
    [community.okd.oc connection plugin](community/okd/oc_connection.md#ansible-collections-community-okd-oc-connection),
    [kubernetes.core.kubectl connection plugin](kubernetes/core/kubectl_connection.md#ansible-collections-kubernetes-core-kubectl-connection)

K8S_AUTH_TOKEN
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [community.okd.oc connection plugin](community/okd/oc_connection.md#ansible-collections-community-okd-oc-connection),
    [kubernetes.core.kubectl connection plugin](kubernetes/core/kubectl_connection.md#ansible-collections-kubernetes-core-kubectl-connection)

K8S_AUTH_USERNAME
:   Provide a username for authenticating with the API.

    *Used by:*
    [kubernetes.core.kubectl connection plugin](kubernetes/core/kubectl_connection.md#ansible-collections-kubernetes-core-kubectl-connection)

K8S_AUTH_VERIFY_SSL
:   Whether or not to verify the API server’s SSL certificate. Defaults to *true*.

    *Used by:*
    [community.okd.oc connection plugin](community/okd/oc_connection.md#ansible-collections-community-okd-oc-connection),
    [kubernetes.core.kubectl connection plugin](kubernetes/core/kubectl_connection.md#ansible-collections-kubernetes-core-kubectl-connection)

LINODE_ACCESS_TOKEN
:   The Linode account personal access token.

    *Used by:*
    [community.general.linode inventory plugin](community/general/linode_inventory.md#ansible-collections-community-general-linode-inventory)

LOGDNA_HOSTNAME
:   Alternative Host Name; the current host name by default

    *Used by:*
    [community.general.logdna callback plugin](community/general/logdna_callback.md#ansible-collections-community-general-logdna-callback)

LOGDNA_INGESTION_KEY
:   LogDNA Ingestion Key

    *Used by:*
    [community.general.logdna callback plugin](community/general/logdna_callback.md#ansible-collections-community-general-logdna-callback)

LOGDNA_TAGS
:   Tags

    *Used by:*
    [community.general.logdna callback plugin](community/general/logdna_callback.md#ansible-collections-community-general-logdna-callback)

LOGENTRIES_ANSIBLE_TOKEN
:   The logentries “TCP token”

    *Used by:*
    [community.general.logentries callback plugin](community/general/logentries_callback.md#ansible-collections-community-general-logentries-callback)

LOGENTRIES_API
:   URI to the Logentries API

    *Used by:*
    [community.general.logentries callback plugin](community/general/logentries_callback.md#ansible-collections-community-general-logentries-callback)

LOGENTRIES_FLATTEN
:   flatten complex data structures into a single dictionary with complex keys

    *Used by:*
    [community.general.logentries callback plugin](community/general/logentries_callback.md#ansible-collections-community-general-logentries-callback)

LOGENTRIES_PORT
:   HTTP port to use when connecting to the API

    *Used by:*
    [community.general.logentries callback plugin](community/general/logentries_callback.md#ansible-collections-community-general-logentries-callback)

LOGENTRIES_TLS_PORT
:   Port to use when connecting to the API when TLS is enabled

    *Used by:*
    [community.general.logentries callback plugin](community/general/logentries_callback.md#ansible-collections-community-general-logentries-callback)

LOGENTRIES_USE_TLS
:   Toggle to decide whether to use TLS to encrypt the communications with the API server

    *Used by:*
    [community.general.logentries callback plugin](community/general/logentries_callback.md#ansible-collections-community-general-logentries-callback)

LOGSTASH_FORMAT_VERSION
:   Logging format

    *Used by:*
    [community.general.logstash callback plugin](community/general/logstash_callback.md#ansible-collections-community-general-logstash-callback)

LOGSTASH_PORT
:   Port on which logstash is listening

    *Used by:*
    [community.general.logstash callback plugin](community/general/logstash_callback.md#ansible-collections-community-general-logstash-callback)

LOGSTASH_PRE_COMMAND
:   Executes command before run and its result is added to the `ansible_pre_command_output` logstash field.

    *Used by:*
    [community.general.logstash callback plugin](community/general/logstash_callback.md#ansible-collections-community-general-logstash-callback)

LOGSTASH_SERVER
:   Address of the Logstash server

    *Used by:*
    [community.general.logstash callback plugin](community/general/logstash_callback.md#ansible-collections-community-general-logstash-callback)

LOGSTASH_TYPE
:   Message type

    *Used by:*
    [community.general.logstash callback plugin](community/general/logstash_callback.md#ansible-collections-community-general-logstash-callback)

MANIFOLD_API_TOKEN
:   manifold API token

    *Used by:*
    [community.general.manifold lookup plugin](community/general/manifold_lookup.md#ansible-collections-community-general-manifold-lookup)

NETBOX_API
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [netbox.netbox.nb_inventory inventory plugin](netbox/netbox/nb_inventory_inventory.md#ansible-collections-netbox-netbox-nb-inventory-inventory),
    [netbox.netbox.nb_lookup lookup plugin](netbox/netbox/nb_lookup_lookup.md#ansible-collections-netbox-netbox-nb-lookup-lookup)

NETBOX_API_KEY
:   NetBox API token to be able to read against NetBox.

    This may not be required depending on the NetBox setup.

    *Used by:*
    [netbox.netbox.nb_inventory inventory plugin](netbox/netbox/nb_inventory_inventory.md#ansible-collections-netbox-netbox-nb-inventory-inventory)

NETBOX_API_TOKEN
:   The API token created through NetBox

    This may not be required depending on the NetBox setup.

    *Used by:*
    [netbox.netbox.nb_lookup lookup plugin](netbox/netbox/nb_lookup_lookup.md#ansible-collections-netbox-netbox-nb-lookup-lookup)

NETBOX_TOKEN
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [netbox.netbox.nb_inventory inventory plugin](netbox/netbox/nb_inventory_inventory.md#ansible-collections-netbox-netbox-nb-inventory-inventory),
    [netbox.netbox.nb_lookup lookup plugin](netbox/netbox/nb_lookup_lookup.md#ansible-collections-netbox-netbox-nb-lookup-lookup)

NETBOX_URL
:   The URL to the NetBox instance to query

    *Used by:*
    [netbox.netbox.nb_lookup lookup plugin](netbox/netbox/nb_lookup_lookup.md#ansible-collections-netbox-netbox-nb-lookup-lookup)

NRDP_HOSTNAME
:   Hostname where the passive check is linked to.

    *Used by:*
    [community.general.nrdp callback plugin](community/general/nrdp_callback.md#ansible-collections-community-general-nrdp-callback)

NRDP_SERVICENAME
:   Service where the passive check is linked to.

    *Used by:*
    [community.general.nrdp callback plugin](community/general/nrdp_callback.md#ansible-collections-community-general-nrdp-callback)

NRDP_TOKEN
:   Token to be allowed to push nrdp events.

    *Used by:*
    [community.general.nrdp callback plugin](community/general/nrdp_callback.md#ansible-collections-community-general-nrdp-callback)

NRDP_URL
:   URL of the nrdp server.

    *Used by:*
    [community.general.nrdp callback plugin](community/general/nrdp_callback.md#ansible-collections-community-general-nrdp-callback)

NRDP_VALIDATE_CERTS
:   Validate the SSL certificate of the nrdp server. (Used for HTTPS URLs.)

    *Used by:*
    [community.general.nrdp callback plugin](community/general/nrdp_callback.md#ansible-collections-community-general-nrdp-callback)

ONE_AUTH
:   If both *api_username* or *api_password* are not set, then it will try authenticate with ONE auth file. Default path is `~/.one/one_auth`.

    Set environment variable `ONE_AUTH` to override this path.

    *Used by:*
    [community.general.opennebula inventory plugin](community/general/opennebula_inventory.md#ansible-collections-community-general-opennebula-inventory)

ONE_PASSWORD
:   Password or a token of the user to login into OpenNebula RPC server.

    If not set, the value of the `ONE_PASSWORD` environment variable is used.

    *Used by:*
    [community.general.opennebula inventory plugin](community/general/opennebula_inventory.md#ansible-collections-community-general-opennebula-inventory)

ONE_URL
:   URL of the OpenNebula RPC server.

    It is recommended to use HTTPS so that the username/password are not transferred over the network unencrypted.

    If not set then the value of the `ONE_URL` environment variable is used.

    *Used by:*
    [community.general.opennebula inventory plugin](community/general/opennebula_inventory.md#ansible-collections-community-general-opennebula-inventory)

ONE_USERNAME
:   Name of the user to login into the OpenNebula RPC server. If not set then the value of the `ONE_USERNAME` environment variable is used.

    *Used by:*
    [community.general.opennebula inventory plugin](community/general/opennebula_inventory.md#ansible-collections-community-general-opennebula-inventory)

ONLINE_API_KEY
:   Online OAuth token.

    *Used by:*
    [community.general.online inventory plugin](community/general/online_inventory.md#ansible-collections-community-general-online-inventory)

ONLINE_OAUTH_TOKEN
:   Online OAuth token.

    *Used by:*
    [community.general.online inventory plugin](community/general/online_inventory.md#ansible-collections-community-general-online-inventory)

ONLINE_TOKEN
:   Online OAuth token.

    *Used by:*
    [community.general.online inventory plugin](community/general/online_inventory.md#ansible-collections-community-general-online-inventory)

OS_CLIENT_CONFIG_FILE
:   Override path to clouds.yaml file. If this value is given it
    :   will be searched first. The default path for the
        ansible inventory adds /etc/ansible/openstack.yaml and
        /etc/ansible/openstack.yml to the regular locations documented
        at <https://docs.openstack.org/os-client-config/latest/user/configuration.html#config-files>

    *Used by:*
    [openstack.cloud.openstack inventory plugin](openstack/cloud/openstack_inventory.md#ansible-collections-openstack-cloud-openstack-inventory)

OTEL_SERVICE_NAME
:   The service name resource attribute.

    *Used by:*
    [community.general.opentelemetry callback plugin](community/general/opentelemetry_callback.md#ansible-collections-community-general-opentelemetry-callback)

OVIRT_PASSWORD
:   ovirt authentication password.

    *Used by:*
    [ovirt.ovirt.ovirt inventory plugin](ovirt/ovirt/ovirt_inventory.md#ansible-collections-ovirt-ovirt-ovirt-inventory)

OVIRT_URL
:   URL to ovirt-engine API.

    *Used by:*
    [ovirt.ovirt.ovirt inventory plugin](ovirt/ovirt/ovirt_inventory.md#ansible-collections-ovirt-ovirt-ovirt-inventory)

OVIRT_USERNAME
:   ovirt authentication user.

    *Used by:*
    [ovirt.ovirt.ovirt inventory plugin](ovirt/ovirt/ovirt_inventory.md#ansible-collections-ovirt-ovirt-ovirt-inventory)

PASSWORD_STORE_DIR
:   The directory of the password store.

    *Used by:*
    [community.general.passwordstore lookup plugin](community/general/passwordstore_lookup.md#ansible-collections-community-general-passwordstore-lookup)

PASSWORD_STORE_UMASK
:   Sets the umask for the created .gpg files. The first octed must be greater than 3 (user readable).

    Note pass’ default value is `'077'`.

    *Used by:*
    [community.general.passwordstore lookup plugin](community/general/passwordstore_lookup.md#ansible-collections-community-general-passwordstore-lookup)

PROFILE_TASKS_SORT_ORDER
:   Adjust the sorting output of summary tasks

    *Used by:*
    [ansible.posix.profile_tasks callback plugin](ansible/posix/profile_tasks_callback.md#ansible-collections-ansible-posix-profile-tasks-callback)

PROFILE_TASKS_TASK_OUTPUT_LIMIT
:   Number of tasks to display in the summary

    *Used by:*
    [ansible.posix.profile_tasks callback plugin](ansible/posix/profile_tasks_callback.md#ansible-collections-ansible-posix-profile-tasks-callback)

PROXMOX_PASSWORD
:   Proxmox authentication password.

    If the value is not specified in the inventory configuration, the value of environment variable `PROXMOX_PASSWORD` will be used instead.

    Since community.general 4.7.0 you can also use templating to specify the value of the *password*.

    If you do not specify a password, you must set *token_id* and *token_secret* instead.

    *Used by:*
    [community.general.proxmox inventory plugin](community/general/proxmox_inventory.md#ansible-collections-community-general-proxmox-inventory)

PROXMOX_TOKEN_ID
:   Proxmox authentication token ID.

    If the value is not specified in the inventory configuration, the value of environment variable `PROXMOX_TOKEN_ID` will be used instead.

    To use token authentication, you must also specify *token_secret*. If you do not specify *token_id* and *token_secret*, you must set a password instead.

    Make sure to grant explicit pve permissions to the token or disable ‘privilege separation’ to use the users’ privileges instead.

    *Used by:*
    [community.general.proxmox inventory plugin](community/general/proxmox_inventory.md#ansible-collections-community-general-proxmox-inventory)

PROXMOX_TOKEN_SECRET
:   Proxmox authentication token secret.

    If the value is not specified in the inventory configuration, the value of environment variable `PROXMOX_TOKEN_SECRET` will be used instead.

    To use token authentication, you must also specify *token_id*. If you do not specify *token_id* and *token_secret*, you must set a password instead.

    *Used by:*
    [community.general.proxmox inventory plugin](community/general/proxmox_inventory.md#ansible-collections-community-general-proxmox-inventory)

PROXMOX_URL
:   URL to Proxmox cluster.

    If the value is not specified in the inventory configuration, the value of environment variable `PROXMOX_URL` will be used instead.

    Since community.general 4.7.0 you can also use templating to specify the value of the *url*.

    *Used by:*
    [community.general.proxmox inventory plugin](community/general/proxmox_inventory.md#ansible-collections-community-general-proxmox-inventory)

PROXMOX_USER
:   Proxmox authentication user.

    If the value is not specified in the inventory configuration, the value of environment variable `PROXMOX_USER` will be used instead.

    Since community.general 4.7.0 you can also use templating to specify the value of the *user*.

    *Used by:*
    [community.general.proxmox inventory plugin](community/general/proxmox_inventory.md#ansible-collections-community-general-proxmox-inventory)

SCW_API_KEY
:   Scaleway OAuth token.

    If not explicitly defined or in environment variables, it will try to lookup in the scaleway-cli configuration file (`$SCW_CONFIG_PATH`, `$XDG_CONFIG_HOME/scw/config.yaml`, or `~/.config/scw/config.yaml`).

    More details on [how to generate token](https://www.scaleway.com/en/docs/generate-api-keys/).

    *Used by:*
    [community.general.scaleway inventory plugin](community/general/scaleway_inventory.md#ansible-collections-community-general-scaleway-inventory)

SCW_OAUTH_TOKEN
:   Scaleway OAuth token.

    If not explicitly defined or in environment variables, it will try to lookup in the scaleway-cli configuration file (`$SCW_CONFIG_PATH`, `$XDG_CONFIG_HOME/scw/config.yaml`, or `~/.config/scw/config.yaml`).

    More details on [how to generate token](https://www.scaleway.com/en/docs/generate-api-keys/).

    *Used by:*
    [community.general.scaleway inventory plugin](community/general/scaleway_inventory.md#ansible-collections-community-general-scaleway-inventory)

SCW_TOKEN
:   Scaleway OAuth token.

    If not explicitly defined or in environment variables, it will try to lookup in the scaleway-cli configuration file (`$SCW_CONFIG_PATH`, `$XDG_CONFIG_HOME/scw/config.yaml`, or `~/.config/scw/config.yaml`).

    More details on [how to generate token](https://www.scaleway.com/en/docs/generate-api-keys/).

    *Used by:*
    [community.general.scaleway inventory plugin](community/general/scaleway_inventory.md#ansible-collections-community-general-scaleway-inventory)

SLACK_CHANNEL
:   Slack room to post in.

    *Used by:*
    [community.general.slack callback plugin](community/general/slack_callback.md#ansible-collections-community-general-slack-callback)

SLACK_USERNAME
:   Username to post as.

    *Used by:*
    [community.general.slack callback plugin](community/general/slack_callback.md#ansible-collections-community-general-slack-callback)

SLACK_VALIDATE_CERTS
:   validate the SSL certificate of the Slack server. (For HTTPS URLs)

    *Used by:*
    [community.general.slack callback plugin](community/general/slack_callback.md#ansible-collections-community-general-slack-callback)

SLACK_WEBHOOK_URL
:   Slack Webhook URL

    *Used by:*
    [community.general.slack callback plugin](community/general/slack_callback.md#ansible-collections-community-general-slack-callback)

SMTPHOST
:   Mail Transfer Agent, server that accepts SMTP.

    *Used by:*
    [community.general.mail callback plugin](community/general/mail_callback.md#ansible-collections-community-general-mail-callback)

SN_HOST
:   The ServiceNow hostname.

    This value is FQDN for ServiceNow host.

    If the value is not specified in the task, the value of environment variable `SN_HOST` will be used instead.

    Mutually exclusive with `instance`.

    *Used by:*
    [servicenow.servicenow.now inventory plugin](servicenow/servicenow/now_inventory.md#ansible-collections-servicenow-servicenow-now-inventory)

SN_INSTANCE
:   The ServiceNow instance name, without the domain, service-now.com.

    If the value is not specified in the task, the value of environment variable `SN_INSTANCE` will be used instead.

    *Used by:*
    [servicenow.servicenow.now inventory plugin](servicenow/servicenow/now_inventory.md#ansible-collections-servicenow-servicenow-now-inventory)

SN_PASSWORD
:   Password for username.

    If the value is not specified, the value of environment variable `SN_PASSWORD` will be used instead.

    *Used by:*
    [servicenow.servicenow.now inventory plugin](servicenow/servicenow/now_inventory.md#ansible-collections-servicenow-servicenow-now-inventory)

SN_USERNAME
:   Name of user for connection to ServiceNow.

    If the value is not specified, the value of environment variable `SN_USERNAME` will be used instead.

    *Used by:*
    [servicenow.servicenow.now inventory plugin](servicenow/servicenow/now_inventory.md#ansible-collections-servicenow-servicenow-now-inventory)

SOPS_ANSIBLE_AWX_DISABLE_VARS_PLUGIN_TEMPORARILY
:   Temporarily disable this plugin.

    Useful if ansible-inventory is supposed to be run without decrypting secrets (in AWX for instance).

    *Used by:*
    [community.sops.sops vars plugin](community/sops/sops_vars.md#ansible-collections-community-sops-sops-vars)

SPLUNK_AUTHTOKEN
:   Token to authenticate the connection to the Splunk HTTP collector

    *Used by:*
    [community.general.splunk callback plugin](community/general/splunk_callback.md#ansible-collections-community-general-splunk-callback)

SPLUNK_BATCH
:   Correlation ID which can be set across multiple playbook executions.

    *Used by:*
    [community.general.splunk callback plugin](community/general/splunk_callback.md#ansible-collections-community-general-splunk-callback)

SPLUNK_INCLUDE_MILLISECONDS
:   Whether to include milliseconds as part of the generated timestamp field in the event sent to the Splunk HTTP collector

    *Used by:*
    [community.general.splunk callback plugin](community/general/splunk_callback.md#ansible-collections-community-general-splunk-callback)

SPLUNK_URL
:   URL to the Splunk HTTP collector source

    *Used by:*
    [community.general.splunk callback plugin](community/general/splunk_callback.md#ansible-collections-community-general-splunk-callback)

SPLUNK_VALIDATE_CERTS
:   Whether to validate certificates for connections to HEC. It is not recommended to set to `false` except when you are sure that nobody can intercept the connection between this plugin and HEC, as setting it to `false` allows man-in-the-middle attacks!

    *Used by:*
    [community.general.splunk callback plugin](community/general/splunk_callback.md#ansible-collections-community-general-splunk-callback)

SUMOLOGIC_URL
:   URL to the Sumologic HTTP collector source

    *Used by:*
    [community.general.sumologic callback plugin](community/general/sumologic_callback.md#ansible-collections-community-general-sumologic-callback)

SYSLOG_FACILITY
:   syslog facility to log as

    *Used by:*
    [community.general.syslog_json callback plugin](community/general/syslog_json_callback.md#ansible-collections-community-general-syslog-json-callback)

SYSLOG_PORT
:   port on which the syslog server is listening

    *Used by:*
    [community.general.syslog_json callback plugin](community/general/syslog_json_callback.md#ansible-collections-community-general-syslog-json-callback)

SYSLOG_SERVER
:   syslog server that will receive the event

    *Used by:*
    [community.general.syslog_json callback plugin](community/general/syslog_json_callback.md#ansible-collections-community-general-syslog-json-callback)

TOWER_HOST
:   The network address of your Automation Platform Controller host.

    *Used by:*
    [awx.awx.controller inventory plugin](awx/awx/controller_inventory.md#ansible-collections-awx-awx-controller-inventory),
    [awx.awx.controller_api lookup plugin](awx/awx/controller_api_lookup.md#ansible-collections-awx-awx-controller-api-lookup)

TOWER_OAUTH_TOKEN
:   The OAuth token to use.

    *Used by:*
    [awx.awx.controller inventory plugin](awx/awx/controller_inventory.md#ansible-collections-awx-awx-controller-inventory),
    [awx.awx.controller_api lookup plugin](awx/awx/controller_api_lookup.md#ansible-collections-awx-awx-controller-api-lookup)

TOWER_PASSWORD
:   The password for your controller user.

    *Used by:*
    [awx.awx.controller inventory plugin](awx/awx/controller_inventory.md#ansible-collections-awx-awx-controller-inventory),
    [awx.awx.controller_api lookup plugin](awx/awx/controller_api_lookup.md#ansible-collections-awx-awx-controller-api-lookup)

TOWER_USERNAME
:   The user that you plan to use to access inventories on the controller.

    *Used by:*
    [awx.awx.controller inventory plugin](awx/awx/controller_inventory.md#ansible-collections-awx-awx-controller-inventory),
    [awx.awx.controller_api lookup plugin](awx/awx/controller_api_lookup.md#ansible-collections-awx-awx-controller-api-lookup)

TOWER_VERIFY_SSL
:   Specify whether Ansible should verify the SSL certificate of the controller host.

    Defaults to True, but this is handled by the shared module_utils code

    *Used by:*
    [awx.awx.controller inventory plugin](awx/awx/controller_inventory.md#ansible-collections-awx-awx-controller-inventory),
    [awx.awx.controller_api lookup plugin](awx/awx/controller_api_lookup.md#ansible-collections-awx-awx-controller-api-lookup)

TRACEPARENT
:   The [W3C Trace Context header traceparent](https://www.w3.org/TR/trace-context-1/#traceparent-header).

    *Used by:*
    [community.general.elastic callback plugin](community/general/elastic_callback.md#ansible-collections-community-general-elastic-callback),
    [community.general.opentelemetry callback plugin](community/general/opentelemetry_callback.md#ansible-collections-community-general-opentelemetry-callback)

TSS_API_PATH_URI
:   The path to append to the base URL to form a valid REST API request.

    *Used by:*
    [community.general.tss lookup plugin](community/general/tss_lookup.md#ansible-collections-community-general-tss-lookup)

TSS_BASE_URL
:   The base URL of the server, e.g. `https://localhost/SecretServer`.

    *Used by:*
    [community.general.tss lookup plugin](community/general/tss_lookup.md#ansible-collections-community-general-tss-lookup)

TSS_DOMAIN
:   The domain with which to request the OAuth2 Access Grant.

    Optional when *token* is not provided.

    Requires `python-tss-sdk` version 1.0.0 or greater.

    *Used by:*
    [community.general.tss lookup plugin](community/general/tss_lookup.md#ansible-collections-community-general-tss-lookup)

TSS_PASSWORD
:   The password associated with the supplied username.

    Required when *token* is not provided.

    *Used by:*
    [community.general.tss lookup plugin](community/general/tss_lookup.md#ansible-collections-community-general-tss-lookup)

TSS_TOKEN
:   Existing token for Thycotic authorizer.

    If provided, *username* and *password* are not needed.

    Requires `python-tss-sdk` version 1.0.0 or greater.

    *Used by:*
    [community.general.tss lookup plugin](community/general/tss_lookup.md#ansible-collections-community-general-tss-lookup)

TSS_TOKEN_PATH_URI
:   The path to append to the base URL to form a valid OAuth2 Access Grant request.

    *Used by:*
    [community.general.tss lookup plugin](community/general/tss_lookup.md#ansible-collections-community-general-tss-lookup)

TSS_USERNAME
:   The username with which to request the OAuth2 Access Grant.

    *Used by:*
    [community.general.tss lookup plugin](community/general/tss_lookup.md#ansible-collections-community-general-tss-lookup)

VI_PASSWORD
:   Password for the connection.

    *Used by:*
    [community.vmware.vmware_tools connection plugin](community/vmware/vmware_tools_connection.md#ansible-collections-community-vmware-vmware-tools-connection)

VI_PORTNUMBER
:   Port for the connection.

    *Used by:*
    [community.vmware.vmware_tools connection plugin](community/vmware/vmware_tools_connection.md#ansible-collections-community-vmware-vmware-tools-connection)

VI_SERVER
:   FQDN or IP Address for the connection (vCenter or ESXi Host).

    *Used by:*
    [community.vmware.vmware_tools connection plugin](community/vmware/vmware_tools_connection.md#ansible-collections-community-vmware-vmware-tools-connection)

VI_USERNAME
:   Username for the connection.

    Requires the following permissions on the VM: - VirtualMachine.GuestOperations.Execute - VirtualMachine.GuestOperations.Modify - VirtualMachine.GuestOperations.Query

    *Used by:*
    [community.vmware.vmware_tools connection plugin](community/vmware/vmware_tools_connection.md#ansible-collections-community-vmware-vmware-tools-connection)

VMWARE_HOST
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [community.vmware.vmware_host_inventory inventory plugin](community/vmware/vmware_host_inventory_inventory.md#ansible-collections-community-vmware-vmware-host-inventory-inventory),
    [community.vmware.vmware_tools connection plugin](community/vmware/vmware_tools_connection.md#ansible-collections-community-vmware-vmware-tools-connection),
    [community.vmware.vmware_vm_inventory inventory plugin](community/vmware/vmware_vm_inventory_inventory.md#ansible-collections-community-vmware-vmware-vm-inventory-inventory)

VMWARE_PASSWORD
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [community.vmware.vmware_host_inventory inventory plugin](community/vmware/vmware_host_inventory_inventory.md#ansible-collections-community-vmware-vmware-host-inventory-inventory),
    [community.vmware.vmware_tools connection plugin](community/vmware/vmware_tools_connection.md#ansible-collections-community-vmware-vmware-tools-connection),
    [community.vmware.vmware_vm_inventory inventory plugin](community/vmware/vmware_vm_inventory_inventory.md#ansible-collections-community-vmware-vmware-vm-inventory-inventory)

VMWARE_PORT
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [community.vmware.vmware_host_inventory inventory plugin](community/vmware/vmware_host_inventory_inventory.md#ansible-collections-community-vmware-vmware-host-inventory-inventory),
    [community.vmware.vmware_tools connection plugin](community/vmware/vmware_tools_connection.md#ansible-collections-community-vmware-vmware-tools-connection),
    [community.vmware.vmware_vm_inventory inventory plugin](community/vmware/vmware_vm_inventory_inventory.md#ansible-collections-community-vmware-vmware-vm-inventory-inventory)

VMWARE_PROXY_HOST
:   Address of a proxy that will receive all HTTPS requests and relay them.

    The format is a hostname or a IP.

    This feature depends on a version of pyvmomi>=v6.7.1.2018.12.

    *Used by:*
    [community.vmware.vmware_host_inventory inventory plugin](community/vmware/vmware_host_inventory_inventory.md#ansible-collections-community-vmware-vmware-host-inventory-inventory),
    [community.vmware.vmware_vm_inventory inventory plugin](community/vmware/vmware_vm_inventory_inventory.md#ansible-collections-community-vmware-vmware-vm-inventory-inventory)

VMWARE_PROXY_PORT
:   Port of the HTTP proxy that will receive all HTTPS requests and relay them.

    *Used by:*
    [community.vmware.vmware_host_inventory inventory plugin](community/vmware/vmware_host_inventory_inventory.md#ansible-collections-community-vmware-vmware-host-inventory-inventory),
    [community.vmware.vmware_vm_inventory inventory plugin](community/vmware/vmware_vm_inventory_inventory.md#ansible-collections-community-vmware-vmware-vm-inventory-inventory)

VMWARE_SERVER
:   Name of vCenter or ESXi server.

    *Used by:*
    [community.vmware.vmware_host_inventory inventory plugin](community/vmware/vmware_host_inventory_inventory.md#ansible-collections-community-vmware-vmware-host-inventory-inventory),
    [community.vmware.vmware_vm_inventory inventory plugin](community/vmware/vmware_vm_inventory_inventory.md#ansible-collections-community-vmware-vmware-vm-inventory-inventory)

VMWARE_USER
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [community.vmware.vmware_host_inventory inventory plugin](community/vmware/vmware_host_inventory_inventory.md#ansible-collections-community-vmware-vmware-host-inventory-inventory),
    [community.vmware.vmware_tools connection plugin](community/vmware/vmware_tools_connection.md#ansible-collections-community-vmware-vmware-tools-connection),
    [community.vmware.vmware_vm_inventory inventory plugin](community/vmware/vmware_vm_inventory_inventory.md#ansible-collections-community-vmware-vmware-vm-inventory-inventory)

VMWARE_USERNAME
:   Name of vSphere user.

    Accepts vault encrypted variable.

    *Used by:*
    [community.vmware.vmware_host_inventory inventory plugin](community/vmware/vmware_host_inventory_inventory.md#ansible-collections-community-vmware-vmware-host-inventory-inventory),
    [community.vmware.vmware_vm_inventory inventory plugin](community/vmware/vmware_vm_inventory_inventory.md#ansible-collections-community-vmware-vmware-vm-inventory-inventory)

VMWARE_VALIDATE_CERTS
:   See the documentations for the options where this environment variable is used.

    *Used by:*
    [community.vmware.vmware_host_inventory inventory plugin](community/vmware/vmware_host_inventory_inventory.md#ansible-collections-community-vmware-vmware-host-inventory-inventory),
    [community.vmware.vmware_tools connection plugin](community/vmware/vmware_tools_connection.md#ansible-collections-community-vmware-vmware-tools-connection),
    [community.vmware.vmware_vm_inventory inventory plugin](community/vmware/vmware_vm_inventory_inventory.md#ansible-collections-community-vmware-vmware-vm-inventory-inventory)

VULTR_API_CONFIG
:   Path to the vultr configuration file. If not specified will be taken from regular Vultr configuration.

    *Used by:*
    [ngine_io.vultr.vultr inventory plugin](ngine_io/vultr/vultr_inventory.md#ansible-collections-ngine-io-vultr-vultr-inventory)

VULTR_API_KEY
:   Vultr API key. If not specified will be taken from regular Vultr configuration.

    *Used by:*
    [ngine_io.vultr.vultr inventory plugin](ngine_io/vultr/vultr_inventory.md#ansible-collections-ngine-io-vultr-vultr-inventory)

WORKSPACE_ID
:   Workspace ID of the Azure log analytics workspace.

    *Used by:*
    [community.general.loganalytics callback plugin](community/general/loganalytics_callback.md#ansible-collections-community-general-loganalytics-callback)

WORKSPACE_SHARED_KEY
:   Shared key to connect to Azure log analytics workspace.

    *Used by:*
    [community.general.loganalytics callback plugin](community/general/loganalytics_callback.md#ansible-collections-community-general-loganalytics-callback)

ZABBIX_PASSWORD
:   Zabbix user password.

    *Used by:*
    [community.zabbix.zabbix_inventory inventory plugin](community/zabbix/zabbix_inventory_inventory.md#ansible-collections-community-zabbix-zabbix-inventory-inventory)

ZABBIX_SERVER
:   URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.

    *Used by:*
    [community.zabbix.zabbix_inventory inventory plugin](community/zabbix/zabbix_inventory_inventory.md#ansible-collections-community-zabbix-zabbix-inventory-inventory)

ZABBIX_USERNAME
:   Zabbix user name.

    *Used by:*
    [community.zabbix.zabbix_inventory inventory plugin](community/zabbix/zabbix_inventory_inventory.md#ansible-collections-community-zabbix-zabbix-inventory-inventory)

ZABBIX_VALIDATE_CERTS
:   If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.

    *Used by:*
    [community.zabbix.zabbix_inventory inventory plugin](community/zabbix/zabbix_inventory_inventory.md#ansible-collections-community-zabbix-zabbix-inventory-inventory)
