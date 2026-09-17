---
collection: cilium
version: "1.16.7"
title: "Pull requests review process for committers"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/contributing/development/reviewers_committers/review_process.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="review_process"></a>

# Pull requests review process for committers

## Review process

> **Note:**
> These instructions assume that reviewers are members of the Cilium GitHub
> organization. This is required to obtain the privileges to modify GitHub
> labels on the pull request. See [Cilium's Contributor Ladder](https://github.com/cilium/community/blob/main/CONTRIBUTOR-LADDER.md) for details.

1. Find Pull Requests (PRs) needing a review [from you]([user_review_filter](https://github.com/cilium/cilium/pulls?q=is%3Apr+is%3Aopen+draft%3Afalse+user-review-requested%3A%40me+sort%3Aupdated-asc)) <!-- unresolved-source-link: target=[user_review_filter](https://github.com/cilium/cilium/pulls?q=is%3Apr+is%3Aopen+draft%3Afalse+user-review-requested%3A%40me+sort%3Aupdated-asc) -->,
   or [from one of your teams]([team_review_filter](https://github.com/cilium/cilium/pulls?q=is%3Apr+is%3Aopen+draft%3Afalse+review-requested%3A%40me+sort%3Aupdated-asc)) <!-- unresolved-source-link: target=[team_review_filter](https://github.com/cilium/cilium/pulls?q=is%3Apr+is%3Aopen+draft%3Afalse+review-requested%3A%40me+sort%3Aupdated-asc) -->.

1. If this PR was opened by a contributor who is not part of the Cilium
   organization, please assign yourself to that PR and keep track of the PR to
   ensure it gets reviewed and merged.

   If the contributor is a Cilium committer, then they are responsible for
   getting the PR in a ready to be merged state by adding the
   ``ready-to-merge`` label, once all reviews have been addressed and CI checks
   are successful, so that they (or another committer) can merge the PR.

   If this PR is a backport PR (typically with the label ``kind/backport``) and
   no-one else has reviewed the PR, review the changes as a sanity check. If
   any individual commits deviate from the original patch, request review from
   the original author to validate that the backport was correctly applied.

1. Review overall correctness of the PR according to the rules specified in the
   section [submit_pr](../contributing_guide.md#submit_pr).

1. Set the labels accordingly. A bot called maintainer's little helper might
   automatically help you with this.

| Labels | When to set |
| --- | --- |
| ``dont-merge/needs-sign-off`` | Some commits are not signed off |
| ``needs-rebase`` | PR is outdated and needs to be rebased |

1. Validate that bugfixes are marked with ``kind/bug`` and validate whether the
   assessment of backport requirements as requested by the submitter conforms
   to the [backport_criteria](../../release/backports.md#backport_criteria).

| Labels | When to set |
| --- | --- |
| ``needs-backport/X.Y`` | PR needs to be backported to these stable releases |

1. If the PR is subject to backport, validate that the PR does not mix bugfix
   and refactoring of code as it will heavily complicate the backport process.
   Demand for the PR to be split.

1. Validate the ``release-note/*`` label and check the release note
   suitability. Release notes are passed through the dedicated ``release-note``
   block (see [submit_pr](../contributing_guide.md#submit_pr)), or through the PR title if this block is
   missing. To check if the notes are suitable, put yourself into the
   perspective of a future release notes reader with lack of context and ensure
   the title is precise but brief.

| Labels | When to set |
| --- | --- |
| ``dont-merge/needs-release-note`` | Do NOT merge PR, needs a release note |
| ``release-note/bug`` | This is a non-trivial bugfix and is a user-facing bug |
| ``release-note/major`` | This is a major feature addition, e.g. Add MongoDB support |
| ``release-note/minor`` | This is a minor feature addition, e.g. Add support for a Kubernetes version |
| ``release-note/misc`` | This is a not user-facing change , e.g. Refactor endpoint package, a bug fix of a non-released feature |
| ``release-note/ci`` | This is a CI feature or bug fix. |

1. Check for upgrade compatibility impact and if in doubt, set the label
   ``upgrade-impact`` and discuss in Cilium Slack <!-- unresolved-rst-link: kind=named target=Cilium Slack -->'s ``#development`` channel
   or in the weekly meeting.

| Labels | When to set |
| --- | --- |
| ``upgrade-impact`` | The code changes have a potential upgrade impact |

1. When submitting a review, provide explicit approval or request specific
   changes whenever possible. Clear feedback indicates whether contributors
   must take action before a PR can merge.

   If you need more information before you can approve or request changes, you
   can leave comments seeking clarity. If you do not explicitly approve or
   request changes, it's best practice to raise awareness about the discussion
   so that others can participate. Here are some ways you can raise awareness:

   - Re-request review from codeowners in the PR
   - Raise the topic for discussion in Slack or during community meetings

   When requesting changes, summarize your feedback for the PR, including
   overall issues for a contributor to consider and/or encouragement for what a
   contributor is already doing well.

1. When all review objectives for all ``CODEOWNERS`` are met, all CI tests have
   passed, and all reviewers have approved the requested changes, you can merge
   the PR by clicking on the "Rebase and merge" button.

## Reviewer Teams

Every reviewer, including committers in the [committers team](https://github.com/orgs/cilium/teams/committers/members), belongs to [one
or more teams in the Cilium organization]([cilium_teams](https://github.com/orgs/cilium/teams/team/teams)) <!-- unresolved-source-link: target=[cilium_teams](https://github.com/orgs/cilium/teams/team/teams) -->. If you would like
to add or remove yourself from any team, please submit a PR against the
[community repository](https://github.com/cilium/community).

Once a contributor opens a PR, GitHub automatically picks which [teams]([cilium_teams](https://github.com/orgs/cilium/teams/team/teams)) <!-- unresolved-source-link: target=[cilium_teams](https://github.com/orgs/cilium/teams/team/teams) --> should review the PR using the ``CODEOWNERS`` file. Each
reviewer can see the PRs they need to review by filtering by reviews
requested. A good filter is provided in this [link]([user_review_filter](https://github.com/cilium/cilium/pulls?q=is%3Apr+is%3Aopen+draft%3Afalse+user-review-requested%3A%40me+sort%3Aupdated-asc)) <!-- unresolved-source-link: target=[user_review_filter](https://github.com/cilium/cilium/pulls?q=is%3Apr+is%3Aopen+draft%3Afalse+user-review-requested%3A%40me+sort%3Aupdated-asc) --> so
make sure to bookmark it.

Reviewers are expected to focus their review on the areas of the code where
GitHub requested their review. For small PRs, it may make sense to simply
review the entire PR. However, if the PR is quite large then it can help to
narrow the area of focus to one particular aspect of the code. When leaving a
review, share which areas you focused on and which areas you think that other
reviewers should look into. This helps others to focus on aspects of review
that have not been covered as deeply.

Belonging to a team does not mean that a reviewer needs to know every single
line of code the team is maintaining. Once you have reviewed a PR, if you feel
that another pair of eyes is needed, re-request a review from the appropriate
team. In the following example, the reviewer belonging to the CI team is
re-requesting a review for other team members to review the PR. This allows
other team members belonging to the CI team to see the PR as part of the PRs
that require review in the [filter]([team_review_filter](https://github.com/cilium/cilium/pulls?q=is%3Apr+is%3Aopen+draft%3Afalse+review-requested%3A%40me+sort%3Aupdated-asc)) <!-- unresolved-source-link: target=[team_review_filter](https://github.com/cilium/cilium/pulls?q=is%3Apr+is%3Aopen+draft%3Afalse+review-requested%3A%40me+sort%3Aupdated-asc) -->.

![](https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/images/re-request-review.png)

When all review objectives for all ``CODEOWNERS`` are met, all required CI
tests have passed and a proper release label is set, you may set the
``ready-to-merge`` label to indicate that all criteria have been met.
Maintainer's little helper might set this label automatically if the previous
requirements were met.

| Labels | When to set |
| --- | --- |
| ``ready-to-merge`` | PR is ready to be merged |

## Code owners

Included file `Documentation/codeowners.rst`:

..
    This file was autogenerated via Documentation/update-codeowners.sh, do not edit manually

Code owners are used by the Cilium community to consolidate common knowledge
into teams that can provide consistent and actionable feedback to
contributors. This section will describe groups of teams and suggestions
about the focus areas for review.

The primary motivation for these teams is to provide structure around review
processes to ensure that contributors know how to reach out to community
members to conduct discussions, ensure contributions meet the expectations of
the community, and align on the direction of proposed changes. Furthermore,
while these teams are primarily drawn upon to provide review on specific pull
requests, they are also encouraged to self-organize around how to make
improvements to their areas of the Cilium project over time.

Any committer may self-nominate to code owner teams. Reach out to the core
team on the #committers channel in Slack to coordinate. Committers do not
require expert knowledge in an area in order to join a code owner team,
only a willingness to engage in discussions and learn about the area.

### Project-wide

These code owners may provide feedback for Pull Requests submitted to any
repository in the Cilium project:

- [@cilium/api](https://github.com/orgs/cilium/teams/api):
  Ensure the backwards-compatibility of Cilium REST and gRPC APIs, excluding
  Hubble which is owned by [@cilium/sig-hubble-api](https://github.com/orgs/cilium/teams/sig-hubble-api).
- [@cilium/build](https://github.com/orgs/cilium/teams/build):
  Provide feedback on languages and scripting used for build and packaging
  system: Make, Shell, Docker.
- [@cilium/cli](https://github.com/orgs/cilium/teams/cli):
  Provide user experience feedback on changes to Command-Line Interfaces.
  These owners are a stand-in for the user community to bring a user
  perspective to the review process. Consider how information is presented,
  consistency of flags and options.
- [@cilium/ci-structure](https://github.com/orgs/cilium/teams/ci-structure):
  Provide guidance around the best use of Cilium project continuous
  integration and testing infrastructure, including GitHub actions, VM
  helpers, testing frameworks, etc.
- [@cilium/community](https://github.com/orgs/cilium/teams/community):
  Maintain files that refer to Cilium community users such as USERS.md.
- [@cilium/contributing](https://github.com/orgs/cilium/teams/contributing):
  Encourage practices that ensure an inclusive contributor community. Review
  tooling and scripts used by contributors.
- [@cilium/docs-structure](https://github.com/orgs/cilium/teams/docs-structure):
  Ensure the consistency and layout of documentation. General feedback on the
  use of Sphinx, how to communicate content clearly to the community. This
  code owner is not expected to validate the technical correctness of
  submissions. Correctness is typically handled by another code owner group
  which is also assigned to any given piece of documentation.
- [@cilium/sig-foundations](https://github.com/orgs/cilium/teams/sig-foundations):
  Review changes to the core libraries and provide guidance to overall
  software architecture.
- [@cilium/github-sec](https://github.com/orgs/cilium/teams/github-sec):
  Responsible for maintaining the security of repositories in the Cilium
  project by maintaining best practices for workflow usage, for instance
  preventing malicious use of GitHub actions.
- [@cilium/helm](https://github.com/orgs/cilium/teams/helm):
  Provide input on the way that Helm can be used to configure features. These
  owners are a stand-in for the user community to bring a user perspective to
  the review process. Ensure that Helm changes are defined in manners that
  will be forward-compatible for upgrade and follow best practices for
  deployment (for example, being GitOps-friendly).
- [@cilium/sig-hubble-api](https://github.com/orgs/cilium/teams/sig-hubble-api):
  Review all Hubble API related changes. The Hubble API covers gRPC and
  metrics endpoints. The team ensures that API changes are backward
  compatible or that a new API version is created for backward incompatible
  changes.
- [@cilium/metrics](https://github.com/orgs/cilium/teams/metrics):
  Provide recommendations about the types, names and labels for metrics to
  follow best practices. This includes considering the cardinality impact of
  metrics being added or extended.
- [@cilium/release-managers](https://github.com/orgs/cilium/teams/release-managers):
  Review files related to releases like AUTHORS and VERSION.
- [@cilium/security](https://github.com/orgs/cilium/teams/security):
  Provide feedback on changes that could have security implications for Cilium,
  and maintain security-related documentation.
- [@cilium/tophat](https://github.com/orgs/cilium/teams/tophat):
  Top Hat duties rotate between the committer group from week to week, and
  they may assist in maintenance, triage and backporting duties across
  different Cilium repositories. Catch-all for code not otherwise owned by a
  team.
- [@cilium/vendor](https://github.com/orgs/cilium/teams/vendor):
  Review vendor updates for software dependencies to check for any potential
  upstream breakages / incompatibilities. Discourage the use of unofficial
  forks of upstream libraries if they are actively maintained.

### Repository Owners

The following code owners are responsible for a range of general feedback for
contributions to specific repositories:

- [@cilium/sig-hubble](https://github.com/orgs/cilium/teams/sig-hubble):
  Review all Cilium and Hubble code related to observing system events,
  exporting those via gRPC protocols outside the node and outside the
  cluster. those event channels, for example via TLS.
- [@cilium/hubble-ui](https://github.com/orgs/cilium/teams/hubble-ui):
  Maintain the Hubble UI graphical interface.
- [@cilium/tetragon](https://github.com/orgs/cilium/teams/tetragon):
  Review of all Tetragon code, both for Go and C (for eBPF).

The teams above are responsible for reviewing the majority of contributions
to the corresponding repositories. Additionally, there are "maintainer" teams
listed below which may not be responsible for overall code review for a
repository, but they have administrator access to the repositories and so
they can assist with configuring GitHub repository settings, secrets, and
related processes. For the full codeowners for individual repositories, see
the CODEOWNERS file in the corresponding repository.

- [@cilium/cilium-cli-maintainers](https://github.com/orgs/cilium/teams/cilium-cli-maintainers)
- [@cilium/cilium-maintainers](https://github.com/orgs/cilium/teams/cilium-maintainers)
- [@cilium/cilium-packer-ci-build-maintainers](https://github.com/orgs/cilium/teams/cilium-packer-ci-build-maintainers)
- [@cilium/ebpf-lib-maintainers](https://github.com/orgs/cilium/teams/ebpf-lib-maintainers)
- [@cilium/hubble-maintainers](https://github.com/orgs/cilium/teams/hubble-maintainers)
- [@cilium/image-tools-maintainers](https://github.com/orgs/cilium/teams/image-tools-maintainers)
- [@cilium/metallb-maintainers](https://github.com/orgs/cilium/teams/metallb-maintainers)
- [@cilium/openshift-terraform-maintainers](https://github.com/orgs/cilium/teams/openshift-terraform-maintainers)
- [@cilium/proxy-maintainers](https://github.com/orgs/cilium/teams/proxy-maintainers)
- [@cilium/tetragon-maintainers](https://github.com/orgs/cilium/teams/tetragon-maintainers)

### Cloud Integrations

The following codeowner groups provide insight into the integrations with
specific cloud providers:

- [@cilium/alibabacloud](https://github.com/orgs/cilium/teams/alibabacloud)
- [@cilium/aws](https://github.com/orgs/cilium/teams/aws)
- [@cilium/azure](https://github.com/orgs/cilium/teams/azure)

### Cilium Internals

The following codeowner groups cover more specific knowledge about Cilium
Agent internals or the way that particular Cilium features interact with
external software and protocols:

- [@cilium/docker](https://github.com/orgs/cilium/teams/docker):
  Maintain the deprecated docker-plugin.
- [@cilium/endpoint](https://github.com/orgs/cilium/teams/endpoint):
  Provide background on how the Cilium Endpoint package fits into the overall
  agent architecture, relationship with generation of policy / datapath
  constructs, serialization and restore from disk.
- [@cilium/envoy](https://github.com/orgs/cilium/teams/envoy):
  Maintain the L7 proxy integration with Envoy. This includes the
  configurations for Envoy via xDS protocols as well as the extensible
  proxylib framework for Go-based layer 7 filters.
- [@cilium/egress-gateway](https://github.com/orgs/cilium/teams/egress-gateway):
  Maintain the egress gateway control plane and datapath logic.
- [@cilium/fqdn](https://github.com/orgs/cilium/teams/fqdn):
  Maintain the L7 DNS proxy integration.
- [@cilium/ipcache](https://github.com/orgs/cilium/teams/ipcache):
  Provide background on how the userspace IPCache structure fits into the
  overall agent architecture, ordering constraints with respect to network
  policies and encryption. Handle the relationship between Kubernetes state
  and datapath state as it pertains to remote peers.
- [@cilium/ipsec](https://github.com/orgs/cilium/teams/ipsec):
  Maintain the kernel IPsec configuration and related eBPF logic to ensure
  traffic is correctly encrypted.
- [@cilium/kvstore](https://github.com/orgs/cilium/teams/kvstore):
  Review Cilium interactions with key-value stores, particularly etcd.
  Understand the client libraries used by Cilium for sharing state between
  nodes and clusters.
- [@cilium/loader](https://github.com/orgs/cilium/teams/loader):
  Maintain the tooling that allows eBPF programs to be loaded into the
  kernel: LLVM, bpftool, use of cilium/ebpf for loading programs in the
  agent, ELF templating, etc.
- [@cilium/operator](https://github.com/orgs/cilium/teams/operator):
  Review operations that occur once per cluster via the Cilium Operator
  component. Take care of the corresponding garbage collection and leader
  election logic.
- [@cilium/proxy](https://github.com/orgs/cilium/teams/proxy):
  Review low-level implementations used to redirect L7 traffic to the actual
  proxy implementations (FQDN, Envoy, ...).
- [@cilium/sig-agent](https://github.com/orgs/cilium/teams/sig-agent):
  Provide Cilium (agent) general Go review. Internal architecture, core data
  structures and daemon startup.
- [@cilium/sig-bgp](https://github.com/orgs/cilium/teams/sig-bgp):
  Review changes to our BGP integration.
- [@cilium/sig-clustermesh](https://github.com/orgs/cilium/teams/sig-clustermesh):
  Ensure the reliability of state sharing between clusters to ensure that
  each cluster maintains a separate fault domain.
- [@cilium/sig-datapath](https://github.com/orgs/cilium/teams/sig-datapath):
  Provide feedback on all eBPF code changes, use of the kernel APIs for
  configuring the networking and socket layers. Coordination of kernel
  subsystems such as xfrm (IPsec), iptables / nftables, tc. Maintain the
  control plane layers that populate most eBPF maps; account for endianness
  and system architecture impacts on the datapath code.
- [@cilium/sig-hubble](https://github.com/orgs/cilium/teams/sig-hubble):
  Review all Cilium and Hubble code related to observing system events,
  exporting those via gRPC protocols outside the node and outside the
  cluster. Ensure the security of those event channels, for example via TLS.
- [@cilium/sig-ipam](https://github.com/orgs/cilium/teams/sig-ipam):
  Coordinate the implementation between all of the IP Address Management
  modes, provide awareness/insight into IP resource exhaustion and garbage
  collection concerns.
- [@cilium/sig-k8s](https://github.com/orgs/cilium/teams/sig-k8s):
  Provide input on all interactions with Kubernetes, both for standard
  resources and CRDs. Ensure best practices are followed for the coordination
  of clusterwide state in order to minimize memory usage.
- [@cilium/sig-lb](https://github.com/orgs/cilium/teams/sig-lb):
  Maintain the layers necessary to coordinate all load balancing
  configurations within the agent control plane, including Services,
  ClusterIP, NodePorts, Maglev, local redirect policies, and
  NAT46/NAT64.
- [@cilium/sig-policy](https://github.com/orgs/cilium/teams/sig-policy):
  Ensure consistency of semantics for all network policy representations.
  Responsible for all policy logic from Kubernetes down to eBPF policymap
  entries, including all intermediate layers such as the Policy Repository,
  SelectorCache, PolicyCache, CachedSelectorPolicy, EndpointPolicy, etc.
- [@cilium/sig-scalability](https://github.com/orgs/cilium/teams/sig-scalability):
  Maintain scalability and performance tests. Provide input on scalability
  and performance related changes.
- [@cilium/sig-servicemesh](https://github.com/orgs/cilium/teams/sig-servicemesh):
  Provide input on the way that Service Mesh constructs such as Gateway API
  are converted into lower-level constructs backed by eBPF or Envoy
  configurations. Maintain the CRDs necessary for Service Mesh functionality.
- [@cilium/wireguard](https://github.com/orgs/cilium/teams/wireguard):
  Maintain the kernel WireGuard configuration and datapath impacts related to
  ensuring traffic is encrypted correctly when WireGuard mode is enabled.
