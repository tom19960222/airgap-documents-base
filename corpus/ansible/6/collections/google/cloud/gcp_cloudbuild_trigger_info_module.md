---
collection: ansible
version: "6"
title: "google.cloud.gcp_cloudbuild_trigger_info module – Gather info for GCP Trigger"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_cloudbuild_trigger_info_module.html
fetched_at: 2026-07-27T17:47:40+00:00
---
# google.cloud.gcp_cloudbuild_trigger_info module – Gather info for GCP Trigger

> **Note:**
>
> This module is part of the [google.cloud collection](https://galaxy.ansible.com/google/cloud) (version 1.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install google.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](gcp_cloudbuild_trigger_info_module.md#ansible-collections-google-cloud-gcp-cloudbuild-trigger-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_cloudbuild_trigger_info`.

- [Synopsis](gcp_cloudbuild_trigger_info_module.md#synopsis)
- [Requirements](gcp_cloudbuild_trigger_info_module.md#requirements)
- [Parameters](gcp_cloudbuild_trigger_info_module.md#parameters)
- [Notes](gcp_cloudbuild_trigger_info_module.md#notes)
- [Examples](gcp_cloudbuild_trigger_info_module.md#examples)
- [Return Values](gcp_cloudbuild_trigger_info_module.md#return-values)

## [Synopsis](gcp_cloudbuild_trigger_info_module.md#id1)

- Gather info for GCP Trigger

## [Requirements](gcp_cloudbuild_trigger_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_cloudbuild_trigger_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |

## [Notes](gcp_cloudbuild_trigger_info_module.md#id4)

> **Note:**
>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_cloudbuild_trigger_info_module.md#id5)

```yaml+jinja
- name: get info on a trigger
  gcp_cloudbuild_trigger_info:
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_cloudbuild_trigger_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  Returned: always |
| **build**  complex | Contents of the build template. Either a filename or build template must be provided.  Returned: success |
| **artifacts**  complex | Artifacts produced by the build that should be uploaded upon successful completion of all build steps.  Returned: success |
| **images**  list / elements=string | A list of images to be pushed upon the successful completion of all build steps.  The images will be pushed using the builder service account’s credentials.  The digests of the pushed images will be stored in the Build resource’s results field.  If any of the images fail to be pushed, the build is marked FAILURE.  Returned: success |
| **objects**  complex | A list of objects to be uploaded to Cloud Storage upon successful completion of all build steps.  Files in the workspace matching specified paths globs will be uploaded to the Cloud Storage location using the builder service account’s credentials.  The location and generation of the uploaded objects will be stored in the Build resource’s results field.  If any objects fail to be pushed, the build is marked FAILURE.  Returned: success |
| **location**  string | Cloud Storage bucket and optional object path, in the form “gs://bucket/path/to/somewhere/”.  Files in the workspace matching any path pattern will be uploaded to Cloud Storage with this location as a prefix.  Returned: success |
| **paths**  list / elements=string | Path globs used to match files in the build’s workspace.  Returned: success |
| **timing**  complex | Output only. Stores timing information for pushing all artifact objects.  Returned: success |
| **endTime**  string | End of time span.  A timestamp in RFC3339 UTC “Zulu” format, with nanosecond resolution and up to nine fractional digits. Examples: “2014-10-02T15:01:23Z” and “2014-10-02T15:01:23.045123456Z”.  Returned: success |
| **startTime**  string | Start of time span.  A timestamp in RFC3339 UTC “Zulu” format, with nanosecond resolution and up to nine fractional digits. Examples: “2014-10-02T15:01:23Z” and “2014-10-02T15:01:23.045123456Z”.  Returned: success |
| **images**  list / elements=string | A list of images to be pushed upon the successful completion of all build steps.  The images are pushed using the builder service account’s credentials.  The digests of the pushed images will be stored in the Build resource’s results field.  If any of the images fail to be pushed, the build status is marked FAILURE.  Returned: success |
| **logsBucket**  string | Google Cloud Storage bucket where logs should be written. Logs file names will be of the format ${logsBucket}/log-${build_id}.txt.  Returned: success |
| **options**  complex | Special options for this build.  Returned: success |
| **diskSizeGb**  integer | Requested disk size for the VM that runs the build. Note that this is NOT “disk free”; some of the space will be used by the operating system and build utilities.  Also note that this is the minimum disk size that will be allocated for the build – the build may run with a larger disk than requested. At present, the maximum disk size is 1000GB; builds that request more than the maximum are rejected with an error.  Returned: success |
| **dynamicSubstitutions**  boolean | Option to specify whether or not to apply bash style string operations to the substitutions.  NOTE this is always enabled for triggered builds and cannot be overridden in the build configuration file.  Returned: success |
| **env**  list / elements=string | A list of global environment variable definitions that will exist for all build steps in this build. If a variable is defined in both globally and in a build step, the variable will use the build step value.  The elements are of the form “KEY=VALUE” for the environment variable “KEY” being given the value “VALUE”.  Returned: success |
| **logging**  string | Option to specify the logging mode, which determines if and where build logs are stored.  Returned: success |
| **logStreamingOption**  string | Option to define build log streaming behavior to Google Cloud Storage.  Returned: success |
| **machineType**  string | Compute Engine machine type on which to run the build.  Returned: success |
| **requestedVerifyOption**  string | Requested verifiability options.  Returned: success |
| **secretEnv**  list / elements=string | A list of global environment variables, which are encrypted using a Cloud Key Management Service crypto key. These values must be specified in the build’s Secret. These variables will be available to all build steps in this build.  Returned: success |
| **sourceProvenanceHash**  list / elements=string | Requested hash for SourceProvenance.  Returned: success |
| **substitutionOption**  string | Option to specify behavior when there is an error in the substitution checks.  NOTE this is always set to ALLOW_LOOSE for triggered builds and cannot be overridden in the build configuration file.  Returned: success |
| **volumes**  complex | Global list of volumes to mount for ALL build steps Each volume is created as an empty volume prior to starting the build process.  Upon completion of the build, volumes and their contents are discarded. Global volume names and paths cannot conflict with the volumes defined a build step.  Using a global volume in a build with only one step is not valid as it is indicative of a build request with an incorrect configuration.  Returned: success |
| **name**  string | Name of the volume to mount.  Volume names must be unique per build step and must be valid names for Docker volumes.  Each named volume must be used by at least two build steps.  Returned: success |
| **path**  string | Path at which to mount the volume.  Paths must be absolute and cannot conflict with other volume paths on the same build step or with certain reserved volume paths.  Returned: success |
| **workerPool**  string | Option to specify a WorkerPool for the build. Format projects/{project}/workerPools/{workerPool} This field is experimental.  Returned: success |
| **queueTtl**  string | TTL in queue for this build. If provided and the build is enqueued longer than this value, the build will expire and the build status will be EXPIRED.  The TTL starts ticking from createTime.  A duration in seconds with up to nine fractional digits, terminated by ‘s’. Example: “3.5s”.  Returned: success |
| **secrets**  complex | Secrets to decrypt using Cloud Key Management Service.  Returned: success |
| **kmsKeyName**  string | Cloud KMS key name to use to decrypt these envs.  Returned: success |
| **secretEnv**  dictionary | Map of environment variable name to its encrypted value.  Secret environment variables must be unique across all of a build’s secrets, and must be used by at least one build step. Values can be at most 64 KB in size. There can be at most 100 secret values across all of a build’s secrets.  Returned: success |
| **source**  complex | The location of the source files to build.  Returned: success |
| **repoSource**  complex | Location of the source in a Google Cloud Source Repository.  Returned: success |
| **branchName**  string | Regex matching branches to build. Exactly one a of branch name, tag, or commit SHA must be provided.  The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at <https://github.com/google/re2/wiki/Syntax> .  Returned: success |
| **commitSha**  string | Explicit commit SHA to build. Exactly one a of branch name, tag, or commit SHA must be provided.  Returned: success |
| **dir**  string | Directory, relative to the source root, in which to run the build.  This must be a relative path. If a step’s dir is specified and is an absolute path, this value is ignored for that step’s execution.  Returned: success |
| **invertRegex**  boolean | Only trigger a build if the revision regex does NOT match the revision regex.  Returned: success |
| **projectId**  string | ID of the project that owns the Cloud Source Repository. If omitted, the project ID requesting the build is assumed.  Returned: success |
| **repoName**  string | Name of the Cloud Source Repository.  Returned: success |
| **substitutions**  dictionary | Substitutions to use in a triggered build. Should only be used with triggers.run .  Returned: success |
| **tagName**  string | Regex matching tags to build. Exactly one a of branch name, tag, or commit SHA must be provided.  The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at <https://github.com/google/re2/wiki/Syntax> .  Returned: success |
| **storageSource**  complex | Location of the source in an archive file in Google Cloud Storage.  Returned: success |
| **bucket**  string | Google Cloud Storage bucket containing the source.  Returned: success |
| **generation**  string | Google Cloud Storage generation for the object. If the generation is omitted, the latest generation will be used .  Returned: success |
| **object**  string | Google Cloud Storage object containing the source.  This object must be a gzipped archive file (.tar.gz) containing source to build.  Returned: success |
| **steps**  complex | The operations to be performed on the workspace.  Returned: success |
| **args**  list / elements=string | A list of arguments that will be presented to the step when it is started.  If the image used to run the step’s container has an entrypoint, the args are used as arguments to that entrypoint. If the image does not define an entrypoint, the first element in args is used as the entrypoint, and the remainder will be used as arguments.  Returned: success |
| **dir**  string | Working directory to use when running this step’s container.  If this value is a relative path, it is relative to the build’s working directory. If this value is absolute, it may be outside the build’s working directory, in which case the contents of the path may not be persisted across build step executions, unless a `volume` for that path is specified.  If the build specifies a `RepoSource` with `dir` and a step with a `dir`, which specifies an absolute path, the `RepoSource` `dir` is ignored for the step’s execution.  Returned: success |
| **entrypoint**  string | Entrypoint to be used instead of the build step image’s default entrypoint.  If unset, the image’s default entrypoint is used .  Returned: success |
| **env**  list / elements=string | A list of environment variable definitions to be used when running a step.  The elements are of the form “KEY=VALUE” for the environment variable “KEY” being given the value “VALUE”.  Returned: success |
| **id**  string | Unique identifier for this build step, used in `wait_for` to reference this build step as a dependency.  Returned: success |
| **name**  string | The name of the container image that will run this particular build step.  If the image is available in the host’s Docker daemon’s cache, it will be run directly. If not, the host will attempt to pull the image first, using the builder service account’s credentials if necessary.  The Docker daemon’s cache will already have the latest versions of all of the officially supported build steps (see <https://github.com/GoogleCloudPlatform/cloud-builders> for images and examples).  The Docker daemon will also have cached many of the layers for some popular images, like “ubuntu”, “debian”, but they will be refreshed at the time you attempt to use them.  If you built an image in a previous build step, it will be stored in the host’s Docker daemon’s cache and is available to use as the name for a later build step.  Returned: success |
| **secretEnv**  list / elements=string | A list of environment variables which are encrypted using a Cloud Key Management Service crypto key. These values must be specified in the build’s `Secret`.  Returned: success |
| **timeout**  string | Time limit for executing this build step. If not defined, the step has no time limit and will be allowed to continue to run until either it completes or the build itself times out.  Returned: success |
| **timing**  string | Output only. Stores timing information for executing this build step.  Returned: success |
| **volumes**  complex | List of volumes to mount into the build step.  Each volume is created as an empty volume prior to execution of the build step. Upon completion of the build, volumes and their contents are discarded.  Using a named volume in only one step is not valid as it is indicative of a build request with an incorrect configuration.  Returned: success |
| **name**  string | Name of the volume to mount.  Volume names must be unique per build step and must be valid names for Docker volumes. Each named volume must be used by at least two build steps.  Returned: success |
| **path**  string | Path at which to mount the volume.  Paths must be absolute and cannot conflict with other volume paths on the same build step or with certain reserved volume paths.  Returned: success |
| **waitFor**  list / elements=string | The ID(s) of the step(s) that this build step depends on.  This build step will not start until all the build steps in `wait_for` have completed successfully. If `wait_for` is empty, this build step will start when all previous build steps in the `Build.Steps` list have completed successfully.  Returned: success |
| **substitutions**  dictionary | Substitutions data for Build resource.  Returned: success |
| **tags**  list / elements=string | Tags for annotation of a Build. These are not docker tags.  Returned: success |
| **timeout**  string | Amount of time that this build should be allowed to run, to second granularity.  If this amount of time elapses, work on the build will cease and the build status will be TIMEOUT.  This timeout must be equal to or greater than the sum of the timeouts for build steps within the build.  The expected format is the number of seconds followed by s.  Default time is ten minutes (600s).  Returned: success |
| **createTime**  string | Time when the trigger was created.  Returned: success |
| **description**  string | Human-readable description of the trigger.  Returned: success |
| **disabled**  boolean | Whether the trigger is disabled or not. If true, the trigger will never result in a build.  Returned: success |
| **filename**  string | Path, from the source root, to a file whose contents is used for the template. Either a filename or build template must be provided.  Returned: success |
| **github**  complex | Describes the configuration of a trigger that creates a build whenever a GitHub event is received.  Returned: success |
| **name**  string | Name of the repository. For example: The name for <https://github.com/googlecloudplatform/cloud-builders> is “cloud-builders”.  Returned: success |
| **owner**  string | Owner of the repository. For example: The owner for <https://github.com/googlecloudplatform/cloud-builders> is “googlecloudplatform”.  Returned: success |
| **pullRequest**  complex | filter to match changes in pull requests. Specify only one of pullRequest or push.  Returned: success |
| **branch**  string | Regex of branches to match.  Returned: success |
| **commentControl**  string | Whether to block builds on a “/gcbrun” comment from a repository owner or collaborator.  Returned: success |
| **invertRegex**  boolean | If true, branches that do NOT match the git_ref will trigger a build.  Returned: success |
| **push**  complex | filter to match changes in refs, like branches or tags. Specify only one of pullRequest or push.  Returned: success |
| **branch**  string | Regex of branches to match. Specify only one of branch or tag.  Returned: success |
| **invertRegex**  boolean | When true, only trigger a build if the revision regex does NOT match the git_ref regex.  Returned: success |
| **tag**  string | Regex of tags to match. Specify only one of branch or tag.  Returned: success |
| **id**  string | The unique identifier for the trigger.  Returned: success |
| **ignoredFiles**  list / elements=string | ignoredFiles and includedFiles are file glob matches using <https://golang.org/pkg/path/filepath/#Match> extended with support for `\*\*`.  If ignoredFiles and changed files are both empty, then they are not used to determine whether or not to trigger a build.  If ignoredFiles is not empty, then we ignore any files that match any of the ignored_file globs. If the change has no files that are outside of the ignoredFiles globs, then we do not trigger a build.  Returned: success |
| **includedFiles**  list / elements=string | ignoredFiles and includedFiles are file glob matches using <https://golang.org/pkg/path/filepath/#Match> extended with support for `\*\*`.  If any of the files altered in the commit pass the ignoredFiles filter and includedFiles is empty, then as far as this filter is concerned, we should trigger the build.  If any of the files altered in the commit pass the ignoredFiles filter and includedFiles is not empty, then we make sure that at least one of those files matches a includedFiles glob. If not, then we do not trigger a build.  Returned: success |
| **name**  string | Name of the trigger. Must be unique within the project.  Returned: success |
| **substitutions**  dictionary | Substitutions data for Build resource.  Returned: success |
| **tags**  list / elements=string | Tags for annotation of a BuildTrigger .  Returned: success |
| **triggerTemplate**  complex | Template describing the types of source changes to trigger a build.  Branch and tag names in trigger templates are interpreted as regular expressions. Any branch or tag change that matches that regular expression will trigger a build.  Returned: success |
| **branchName**  string | Name of the branch to build. Exactly one a of branch name, tag, or commit SHA must be provided.  This field is a regular expression.  Returned: success |
| **commitSha**  string | Explicit commit SHA to build. Exactly one of a branch name, tag, or commit SHA must be provided.  Returned: success |
| **dir**  string | Directory, relative to the source root, in which to run the build.  This must be a relative path. If a step’s dir is specified and is an absolute path, this value is ignored for that step’s execution.  Returned: success |
| **invertRegex**  boolean | Only trigger a build if the revision regex does NOT match the revision regex.  Returned: success |
| **projectId**  string | ID of the project that owns the Cloud Source Repository. If omitted, the project ID requesting the build is assumed.  Returned: success |
| **repoName**  string | Name of the Cloud Source Repository. If omitted, the name “default” is assumed.  Returned: success |
| **tagName**  string | Name of the tag to build. Exactly one of a branch name, tag, or commit SHA must be provided.  This field is a regular expression.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
