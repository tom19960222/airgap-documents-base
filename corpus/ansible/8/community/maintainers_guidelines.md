---
collection: ansible
version: "8"
title: "Maintainer responsibilities"
source_url: https://docs.ansible.com/projects/ansible/8/community/maintainers_guidelines.html
fetched_at: 2026-07-28T01:00:28+00:00
---
# Maintainer responsibilities

- [How to become a maintainer](maintainers_guidelines.md#how-to-become-a-maintainer)
- [Communicating as a collection maintainer](maintainers_guidelines.md#communicating-as-a-collection-maintainer)
- [Establishing working group communication](maintainers_guidelines.md#establishing-working-group-communication)
- [Community Topics](maintainers_guidelines.md#community-topics)
- [Contributor Summits](maintainers_guidelines.md#contributor-summits)
- [Weekly community Matrix/IRC meetings](maintainers_guidelines.md#weekly-community-matrix-irc-meetings)

An Ansible collection maintainer is a contributor trusted by the community who makes significant and regular contributions to the project and who has shown themselves as a specialist in the related area.
Collection maintainers have [extended permissions](maintainers_workflow.md#collection-maintainers) in the collection scope.

Ansible collection maintainers provide feedback, responses, or actions on pull requests or issues to the collection(s) they maintain in a reasonably timely manner. They can also update the contributor guidelines for that collection, in collaboration with the Ansible community team and the other maintainers of that collection.

In general, collection maintainers:

- Act in accordance with the [Community Code of Conduct](code_of_conduct.md#code-of-conduct).
- Subscribe to the collection repository they maintain (click Watch > All activity in GitHub).
- Keep README, development guidelines, and other general collections [Maintaining good collection documentation](maintainers_guidelines.md#maintainer-documentation) relevant.
- Review and commit changes made by other contributors.
- [Backport](maintainers_workflow.md#backporting) changes to stable branches.
- Address or assign issues to appropriate contributors.
- [Release collections](collection_contributors/collection_releasing.md#releasing).
- Ensure that collections adhere to the [Ansible community package collections requirements](collection_contributors/collection_requirements.md#collections-requirements).
- Track changes announced in [News for collection contributors and maintainers](https://github.com/ansible-collections/news-for-maintainers) and update a collection in accordance with these changes.
- Subscribe and submit news to the [Bullhorn newsletter](https://github.com/ansible/community/wiki/News#the-bullhorn).
- [Build a healthy community](maintainers_guidelines.md#expanding-community) to increase the number of active contributors and maintainers around collections.
- Revise these guidelines to improve the maintainer experience for yourself and others.

Multiple maintainers can divide responsibilities among each other.

## [How to become a maintainer](maintainers_guidelines.md#id5)

A person interested in becoming a maintainer and satisfying the [requirements](maintainers_guidelines.md#maintainer-requirements) may either self-nominate or be nominated by another maintainer.

To nominate a candidate, create a GitHub issue in the relevant collection repository. If there is no response, the repository is not actively maintained, or the current maintainers do not have permissions to add the candidate, please create the issue in the [ansible/community](https://github.com/ansible/community) repository.

## [Communicating as a collection maintainer](maintainers_guidelines.md#id6)

> Maintainers are highly encouraged to subscribe to the [“Changes impacting collection contributors and maintainers” GitHub repo](https://github.com/ansible-collections/news-for-maintainers) and the [Bullhorn newsletter](https://github.com/ansible/community/wiki/News#the-bullhorn). If you have something important to announce through the newsletter (for example, recent releases), see the [Bullhorn’s wiki page](https://github.com/ansible/community/wiki/News#the-bullhorn) to learn how.

Collection contributors and maintainers can also communicate through:

- Real-time chats and forum topics appropriate to their collection, or if none exists, the general community and developer chat channels.
- Collection project boards, issues, and GitHub discussions in corresponding repositories.
- Contributor Summits and Ansible community days.
- Ansiblefest and local meetups.

See [Communicating with the Ansible community](communication.md#communication) for more details on these communication channels.

## [Establishing working group communication](maintainers_guidelines.md#id7)

Working groups depend on efficient communication.
Project maintainers can use the following techniques to establish communication for working groups:

- Find an existing [forum group](https://forum.ansible.com/g) or [working group](communication.md#working-group-list) that is similar to your project and join the conversation.
- [Request](https://github.com/ansible/community/blob/main/WORKING-GROUPS.md) a new working group for your project.
- [Create](https://hackmd.io/@ansible-community/community-matrix-faq#How-do-I-create-a-public-community-room) a public chat for your working group or [ask](https://github.com/ansible/community/issues/new) the community team.
- Provide working group details and links to chat rooms in the contributor section of your project `README.md`.
- Encourage contributors to join the forum group and chat.

See the [Communication guide](communication.md#communication-irc) to learn more about real-time chat.

## [Community Topics](maintainers_guidelines.md#id8)

The Community and the [Steering Committee](https://docs.ansible.com/ansible/devel/community/steering/community_steering_committee.html) asynchronously discuss and vote on the [Community Topics](https://github.com/ansible-community/community-topics/issues) which impact the whole project or its parts including collections and packaging.

Share your opinion and vote on the topics to help the community make the best decisions.

## [Contributor Summits](maintainers_guidelines.md#id9)

The quarterly Ansible Contributor Summit is a global event that provides our contributors a great opportunity to meet each other, communicate, share ideas, and see that there are other real people behind the messages on Matrix or Libera Chat IRC, or GitHub. This gives a sense of community. Watch the [Bullhorn newsletter](https://github.com/ansible/community/wiki/News#the-bullhorn) for information when the next contributor summit, invite contributors you know, and take part in the event together.

## [Weekly community Matrix/IRC meetings](maintainers_guidelines.md#id10)

The Community and the Steering Committee come together at weekly meetings in the `#ansible-community` [Libera.Chat IRC](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-irc) channel or in the bridged [#community:ansible.com](https://matrix.to/#/#community:ansible.com) room on [Matrix](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-matrix) to discuss important project questions. Join us! Here is our [schedule](https://github.com/ansible/community/blob/main/meetings/README.md#schedule).

# Expanding the collection community

> **Note:**
>
> If you discover good ways to expand a community or make it more robust, edit this section with your ideas to share with other collection maintainers.

Here are some ways you can expand the community around your collection:

> - Give [newcomers a positive first experience](maintainers_guidelines.md#collection-new-contributors).
> - Invite contributors to join forum groups and [real-time chats](maintainers_guidelines.md#wg-and-real-time-chat) related to your project.
> - Have [good documentation](maintainers_guidelines.md#maintainer-documentation) with guidelines for new contributors.
> - Make people feel welcome personally and individually.
> - Use labels to show easy fixes and leave non-critical easy fixes to newcomers and offer to mentor them.
> - Be responsive in issues, PRs and other communication.
> - Conduct PR days regularly.
> - Maintain a zero-tolerance policy towards behavior violating the [Community Code of Conduct](code_of_conduct.md#code-of-conduct).
> - Put information about how people can register code of conduct violations in your `README` and `CONTRIBUTING` files.
> - Include quick ways contributors can help and other documentation in your `README`.
> - Add and keep updated the `CONTRIBUTORS` and `MAINTAINERS` files.
> - Create a pinned issue to announce that the collection welcomes new maintainers and contributors.
> - Look for new maintainers among active contributors.
> - Announce that your collection welcomes new maintainers.
> - Take part and congratulate new maintainers in Contributor Summits.

## Encouraging new contributors

Easy-fix items are the best way to attract and mentor new contributors. You should triage incoming issues to mark them with labels such as `easyfix`, `waiting_on_contributor`, and `docs`. where appropriate. Do not fix these trivial non-critical bugs yourself. Instead, mentor a person who wants to contribute.

For some easy-fix issues, you could ask the issue reporter whether they want to fix the issue themselves providing the link to a quick start guide for creating PRs.

Conduct pull request days regularly. You could plan PR days, for example, on the last Friday of every month when you and other maintainers go through all open issues and pull requests focusing on old ones, asking people if you can help, and so on. If there are pull requests that look abandoned (for example, there is no response on your help offers since the previous PR day), announce that anyone else interested can complete the pull request.

Promote active contributors satisfying [requirements](maintainers_guidelines.md#maintainer-requirements) to maintainers. Revise contributors’ activity regularly.

If your collection found new maintainers, announce that fact in the [Bullhorn newsletter](https://github.com/ansible/community/wiki/News#the-bullhorn) and during the next Contributor Summit congratulating and thanking them for the work done. You can mention all the people promoted since the previous summit. Remember to invite the other maintainers to the Summit in advance.

Some other general guidelines to encourage contributors:

- Welcome the author and thank them for the issue or pull request.
- If there is a non-crucial easy-fix bug reported, politely ask the author to fix it themselves providing a link to [Creating your first collection pull request](create_pr_quick_start.md#collection-quickstart).
- When suggesting changes, try to use questions, not statements.
- When suggesting mandatory changes, do it as politely as possible providing documentation references.
- If your suggestion is optional or a matter of personal preference, please say it explicitly.
- When asking for adding tests or for complex code refactoring, say that the author is welcome to ask for clarifications and help if they need it.
- If somebody suggests a good idea, mention it or put a thumbs up.
- After merging, thank the author and reviewers for their time and effort.

See the [Review checklist for collection PRs](collection_contributors/collection_reviewing.md#review-checklist) for a list of items to check before you merge a PR.

# Maintaining good collection documentation

Maintainers look after the collection documentation to ensure it matches the [Ansible documentation style guide](../dev_guide/style_guide/index.md#style-guide). This includes keeping the following documents accurate and updated regularly:

- Collection module and plugin documentation that adheres to the [Ansible documentation format](../dev_guide/developing_modules_documenting.md#module-documenting).
- Collection user guides that follow the [Collection documentation format](../dev_guide/developing_collections_structure.md#collections-doc-dir).
- Repository files that includes at least a `README` and `CONTRIBUTING` file.

A good `README` includes a description of the collection, a link to the [Community Code of Conduct](code_of_conduct.md#code-of-conduct), and details on how to contribute or a pointer to the `CONTRIBUTING` file. If your collection is a part of Ansible (is shipped with Ansible package), highlight that fact at the top of the collection’s `README`.

> The `CONTRIBUTING` file includes all the details or links to the details on how a new or continuing contributor can contribute to this collection. The `CONTRIBUTING` file should include:

- Information or links to new contributor guidelines, such as a quick start on opening PRs.
- Information or links to contributor requirements, such as unit and integration test requirements.

You can optionally include a `CONTRIBUTORS` and `MAINTAINERS` file to list the collection contributors and maintainers.
