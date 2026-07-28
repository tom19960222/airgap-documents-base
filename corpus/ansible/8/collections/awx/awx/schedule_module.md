---
collection: ansible
version: "8"
title: "awx.awx.schedule module – create, update, or destroy Automation Platform Controller schedules."
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/schedule_module.html
fetched_at: 2026-07-28T01:11:43+00:00
---
# awx.awx.schedule module – create, update, or destroy Automation Platform Controller schedules.

> **Note:**
>
> This module is part of the [awx.awx collection](https://galaxy.ansible.com/ui/repo/published/awx/awx/) (version 22.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install awx.awx`.
>
> To use it in a playbook, specify: `awx.awx.schedule`.

- [Synopsis](schedule_module.md#synopsis)
- [Parameters](schedule_module.md#parameters)
- [Notes](schedule_module.md#notes)
- [Examples](schedule_module.md#examples)

## [Synopsis](schedule_module.md#id1)

- Create, update, or destroy Automation Platform Controller schedules. See <https://www.ansible.com/tower> for an overview.

Aliases: tower_schedule

## [Parameters](schedule_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  *added in awx.awx 3.7.0* | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **credentials**  list / elements=string | List of credential names, IDs, or named URLs applied as a prompt, assuming job template prompts for credentials |
| **description**  string | Optional description of this schedule. |
| **diff_mode**  boolean | Enable diff mode for the job template.  **Choices:**   - `false` - `true` |
| **enabled**  boolean | Enables processing of this schedule.  **Choices:**   - `false` - `true` |
| **execution_environment**  string | Execution Environment name, ID, or named URL applied as a prompt, assuming job template prompts for execution environment |
| **extra_data**  dictionary | Specify `extra_vars` for the template. |
| **forks**  integer | Forks applied as a prompt, assuming job template prompts for forks |
| **instance_groups**  list / elements=string | List of Instance Group names, IDs, or named URLs applied as a prompt, assuming job template prompts for instance groups |
| **inventory**  string | Inventory name, ID, or named URL applied as a prompt, assuming job template prompts for inventory |
| **job_slice_count**  integer | Job Slice Count applied as a prompt, assuming job template prompts for job slice count |
| **job_tags**  string | Comma separated list of the tags to use for the job template. |
| **job_type**  string | The job type to use for the job template.  **Choices:**   - `"run"` - `"check"` |
| **labels**  list / elements=string | List of labels applied as a prompt, assuming job template prompts for labels |
| **limit**  string | A host pattern to further constrain the list of hosts managed or affected by the playbook |
| **name**  string / required | Name of this schedule. |
| **new_name**  string | Setting this option will change the existing name (looked up via the name field. |
| **organization**  string | The organization name, ID, or named URL the unified job template exists in.  Used for looking up the unified job template, not a direct model field. |
| **request_timeout**  float | Specify the timeout Ansible should use in requests to the controller host.  Defaults to 10s, but this is handled by the shared module_utils code |
| **rrule**  string | A value representing the schedules iCal recurrence rule.  See rrule plugin for help constructing this value |
| **scm_branch**  string | Branch to use in job run. Project default used if blank. Only allowed if project allow_override field is set to true. |
| **skip_tags**  string | Comma separated list of the tags to skip for the job template. |
| **state**  string | Desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"exists"` |
| **timeout**  integer | Timeout applied as a prompt, assuming job template prompts for timeout |
| **unified_job_template**  string | Name, ID, or named URL of unified job template to schedule. Used to look up an already existing schedule. |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  **Choices:**   - `false` - `true` |
| **verbosity**  integer | Control the output level Ansible produces as the playbook runs. 0 - Normal, 1 - Verbose, 2 - More Verbose, 3 - Debug, 4 - Connection Debug.  **Choices:**   - `0` - `1` - `2` - `3` - `4` - `5` |

## [Notes](schedule_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](schedule_module.md#id4)

```yaml+jinja
- name: Build a schedule for Demo Job Template
  schedule:
    name: "{{ sched1 }}"
    state: present
    unified_job_template: "Demo Job Template"
    rrule: "DTSTART:20191219T130551Z RRULE:FREQ=WEEKLY;INTERVAL=1;COUNT=1"
  register: result

- name: Build the same schedule using the rrule plugin
  schedule:
    name: "{{ sched1 }}"
    state: present
    unified_job_template: "Demo Job Template"
    rrule: "{{ query('awx.awx.schedule_rrule', 'week', start_date='2019-12-19 13:05:51') }}"
  register: result

- name: Build a complex schedule for every day except sunday using the rruleset plugin
  schedule:
    name: "{{ sched1 }}"
    state: present
    unified_job_template: "Demo Job Template"
    rrule: "{{ query(awx.awx.schedule_rruleset, '2022-04-30 10:30:45', rules=rrules, timezone='UTC' ) }}"
  vars:
    rrules:
      - frequency: 'day'
        every: 1
      - frequency: 'day'
        every: 1
        on_days: 'sunday'
        include: False

- name: Delete 'my_schedule' schedule for my_workflow
  schedule:
    name: "my_schedule"
    state: absent
    unified_job_template: my_workflow
```

### Authors

- John Westcott IV (@john-westcott-iv)

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
