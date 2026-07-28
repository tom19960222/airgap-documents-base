---
collection: ansible
version: "6"
title: "Steering Committee mission and responsibilities"
source_url: https://docs.ansible.com/projects/ansible/6/community/steering/community_steering_committee.html
fetched_at: 2026-07-27T16:40:50+00:00
---
# Steering Committee mission and responsibilities

The Steering Committee mission is to provide continuity, guidance, and suggestions to the Ansible community to ensure the delivery and high quality of the Ansible package. In addition, the committee helps decide the technical direction of the Ansible project. It is responsible for approving new proposals and policies in the community, package, and community collections world, new community collection-inclusion requests, and other technical aspects regarding inclusion and packaging.
The Committee should reflect the scope and breadth of the Ansible community.

## Steering Committee responsibilities

The Committee:

- Designs policies and procedures for the community collections world.
- Votes on approval changes to established policies and procedures.
- Reviews community collections for compliance with the policies.
- Helps create and define roadmaps for our deliverables such as the `ansible` package, major community collections, and documentation.
- Reviews community collections submitted for inclusion in the Ansible package and decides whether to include them or not.
- Review other proposals of importance that need the Committee’s attention and provide feedback.

## Current Steering Committee members

The following table lists the current Steering Committee members. See [Steering Committee past members](steering_committee_past_members.md#steering-past-members) for a list of past members.

Current Steering committee members

| Name | GitHub | Start year |
| --- | --- | --- |
| Alexei Znamensky | russoz | 2022 |
| Alicia Cozine | acozine | 2021 |
| Andrew Klychkov | Andersson007 | 2021 |
| Brad Thornton | cidrblock | 2021 |
| Brian Scholer | briantist | 2022 |
| Dylan Silva | thaumos | 2021 |
| Felix Fontein | felixfontein | 2021 |
| James Cassell | jamescassell | 2021 |
| John Barker | gundalow | 2021 |
| Mario Lenz | mariolenz | 2022 |
| Markus Bergholz | markuman | 2022 |
| Sorin Sbarnea | ssbarnea | 2021 |

John Barker ([gundalow](https://github.com/gundalow)) has been elected by the Committee as its [Chairperson](steering_committee_membership.md#chairperson).

Committee members are selected based on their active contribution to the Ansible Project and its community. See [Steering Committee membership guidelines](steering_committee_membership.md#community-steering-guidelines) to learn details.

## Creating new policy proposals & inclusion requests

The Committee uses the [community-topics repository](https://github.com/ansible-community/community-topics/issues) to asynchronously discuss with the Community and vote on Community topics in corresponding issues.

You can create a new issue in the [community-topics repository](https://github.com/ansible-community/community-topics/issues) as a discussion topic if you want to discuss an idea that impacts any of the following:

> - Ansible Community
> - Community collection best practices and requirements
> - Community collection inclusion policy
> - The Community governance
> - Other proposals of importance that need the Committee’s or overall Ansible community attention

To request changes to the inclusion policy and collection requirements:

1. Submit a new pull request to the [ansible-collections/overview](https://github.com/ansible-collections/overview) repository.
2. Create a corresponding issue containing the rationale behind these changes in the [community-topics repository](https://github.com/ansible-community/community-topics/issues) repository.

To submit new collections for inclusion into the Ansible package:

- Submit the new collection inclusion requests through a new discussion in the [ansible-inclusion](https://github.com/ansible-collections/ansible-inclusion/discussions/new) repository.

Depending on a topic you want to discuss with the Community and the Committee, as you prepare your proposal, please consider the requirements established by:

- [Community Code of Conduct](../code_of_conduct.md#code-of-conduct).
- [Ansible Collection Requirements](https://github.com/ansible-collections/overview/blob/main/collection_requirements.rst).
- [Ansible Collection Inclusion Checklist](https://github.com/ansible-collections/overview/blob/main/collection_checklist.md).

### Community topics workflow

The Committee uses the [Community-topics workflow](https://github.com/ansible-community/community-topics/blob/main/community_topics_workflow.md) to asynchronously discuss and vote on the [community-topics](https://github.com/ansible-community/community-topics/issues).

The quorum, the minimum number of Committee members who must vote on a topic in order for a decision to be officially made, is half of the whole number of the Committee members. If the quorum number contains a fractional part, it is rounded up to the next whole number. For example, if there are thirteen members currently in the committee, the quorum will be seven.

Votes must always have “no change” as an option.

In case of equal numbers of votes for and against a topic, the chairperson’s vote will break the tie. For example, if there are six votes for and six votes against a topic, and the chairperson’s vote is among those six which are for the topic, the final decision will be positive. If the chairperson has not voted yet, other members ask them to vote.

For votes with more than two options, one choice must have at least half of the votes. If two choices happen to both have half of the votes, the chairperson’s vote will break the tie. If no choice has at least half of the votes, the vote choices have to be adjusted so that a majority can be found for a choice in a new vote.

### Collection inclusion requests workflow

When reviewing community collection [inclusion requests](https://github.com/ansible-collections/ansible-inclusion/discussions), the Committee members check if a collection adheres to the [Community collection requirements](https://github.com/ansible-collections/overview/blob/main/collection_requirements.rst).

1. A Committee member who conducts the inclusion review copies the [Ansible community collection checklist](https://github.com/ansible-collections/overview/blob/main/collection_checklist.md) into a corresponding [discussion](https://github.com/ansible-collections/ansible-inclusion/discussions).
2. In the course of the review, the Committee member marks items as completed or leaves a comment saying whether the reviewer expects an issue to be addressed or whether it is optional (for example, it could be **MUST FIX:** <what> or **SHOULD FIX:** <what> under an item).
3. For a collection to be included in the Ansible community package, the collection:

> - MUST be reviewed and approved by at least two persons, where at least one person is a Steering Committee member.
> - For a Non-Steering Committee review to be counted for inclusion, it MUST be checked and approved by *another* Steering Committee member.
> - Reviewers must not be involved significantly in development of the collection. They must declare any potential conflict of interest (for example, being friends/relatives/coworkers of the maintainers/authors, being users of the collection, or having contributed to that collection recently or in the past).

1. After the collection gets two or more Committee member approvals, a Committee member creates a [community topic](https://github.com/ansible-community/community-topics/issues) linked to the corresponding inclusion request. The issue’s description says that the collection has been approved by two or more Committee members and establishes a date (a week by default) when the inclusion decision will be considered made. This time period can be used to raise concerns.
2. If no objections are raised up to the established date, the inclusion request is considered successfully resolved. In this case, a Committee member:

> 1. Declares the decision in the topic and in the inclusion request.
> 2. Moves the request to the `Resolved reviews` category.
> 3. Adds the collection to the `ansible.in` file in a corresponding directory of the [ansible-build-data repository](https://github.com/ansible-community/ansible-build-data).
> 4. Announces the inclusion through the [Bullhorn newsletter](https://github.com/ansible/community/wiki/News#the-bullhorn).
> 5. Closes the topic.

## Community Working Group meetings

See the Community Working Group meeting [schedule](https://github.com/ansible/community/blob/main/meetings/README.md#wednesdays). Meeting summaries are posted in the [Community Working Group Meeting Agenda](https://github.com/ansible/community/issues?q=is%3Aopen+label%3Ameeting_agenda+label%3Acommunity+) issue.

> **Note:**
>
> Participation in the Community Working Group meetings is optional for Committee members. Decisions on community topics are made asynchronously in the [community-topics](https://github.com/ansible-community/community-topics/issues) repository.

The meeting minutes can be found at the [fedora meetbot site](https://meetbot.fedoraproject.org/sresults/?group_id=ansible-community&type=channel) and the same is posted to [Ansible Devel Mailing List](https://groups.google.com/g/ansible-devel) after every meeting.
