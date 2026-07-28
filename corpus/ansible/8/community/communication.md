---
collection: ansible
version: "8"
title: "Communicating with the Ansible community"
source_url: https://docs.ansible.com/projects/ansible/8/community/communication.html
fetched_at: 2026-07-28T01:00:25+00:00
---
# Communicating with the Ansible community

- [Code of Conduct](communication.md#code-of-conduct)
- [Forum](communication.md#forum)
- [Real-time chat](communication.md#real-time-chat)

  - [Ansible community on Matrix](communication.md#ansible-community-on-matrix)
  - [Ansible community on IRC](communication.md#ansible-community-on-irc)
  - [General channels](communication.md#general-channels)
  - [Working group-specific channels](communication.md#working-group-specific-channels)
  - [Regional and Language-specific channels](communication.md#regional-and-language-specific-channels)
  - [Meetings on chat](communication.md#meetings-on-chat)
- [Working groups](communication.md#working-groups)
- [Ansible Community Topics](communication.md#ansible-community-topics)
- [Ansible Automation Platform support questions](communication.md#ansible-automation-platform-support-questions)
- [The Bullhorn](communication.md#the-bullhorn)
- [Asking questions over email](communication.md#asking-questions-over-email)

## [Code of Conduct](communication.md#id7)

All communication and interactions in the Ansible Community are governed by our [Community Code of Conduct](code_of_conduct.md#code-of-conduct). Please read and understand it!

## [Forum](communication.md#id8)

The [Ansible Community Forum](https://forum.ansible.com) is a single starting point for questions and help, development discussions, events, and much more. [Register](https://forum.ansible.com/signup?) to join the community. Search by categories and tags to find interesting topics or start a new one; subscribe only to topics you need!

Take a look at the [forum groups](https://forum.ansible.com/g) and join ones that match your interests.
In most cases, joining a forum group automatically subscribes you to related posts.

Want to create a group?
Request it in the [forum topic](https://forum.ansible.com/t/requesting-a-forum-group/503).

## [Real-time chat](communication.md#id9)

For real-time interactions, conversations in the Ansible community happen over two chat protocols: Matrix and IRC. We maintain a bridge between Matrix and IRC, so you can choose whichever protocol you prefer. All channels exist in both places. Join a channel any time to ask questions, participate in a Working Group meeting, or just say hello.

### [Ansible community on Matrix](communication.md#id10)

To join the community using Matrix, you need two things:

- a Matrix account (from [Matrix.org](https://app.element.io/#/register) or any other Matrix homeserver)
- a [Matrix client](https://matrix.org/clients/) (we recommend [Element Webchat](https://app.element.io))

The Ansible community maintains its own Matrix homeserver at `ansible.im`, however public registration is currently unavailable.

Matrix chat supports:

- persistence (when you log on, you see all messages since you last logged off)
- edits (Lets you fix typos and so on. **NOTE** Each edit you make on Matrix re-sends the message to IRC. Please try to avoid multiple edits!)
- replies to individual users
- reactions/emojis
- bridging to IRC
- no line limits
- images

The room links in the [General channels](communication.md#general-channels) or in the [Working groups](communication.md#working-group-list) list will take you directly to the relevant rooms.

If there is no appropriate room for your community, please create it.

For more information, see the community-hosted [Matrix FAQ](https://hackmd.io/@ansible-community/community-matrix-faq).

You can add Matrix shields to your repository’s `README.md` using the shield in the [community-topics](https://github.com/ansible-community/community-topics#community-topics) repository as a template.

### [Ansible community on IRC](communication.md#id11)

The Ansible community maintains several IRC channels on [irc.libera.chat](https://libera.chat/). To join the community using IRC, you need one thing:

- an IRC client

IRC chat supports:

- no persistence (you only see messages when you are logged on unless you add a bouncer)
- simple text interface
- bridging from Matrix

Our IRC channels may require you to register your IRC nickname. If you receive an error when you connect or when posting a message, see [libera.chat’s Nickname Registration guide](https://libera.chat/guides/registration) for instructions. To find all `ansible` specific channels on the libera.chat network, use the following command in your IRC client:

```
/msg alias LIST #ansible* -min 5
```

as described in the [libera.chat docs](https://libera.chat/guides/findingchannels).

Our channels record history on the Matrix side. The channel history can be viewed in a browser - all channels will report an appropriate link to `chat.ansible.im` in their Chanserv entrymsg upon joining the room. Alternatively, a URL of the form `https://chat.ansible.im/#/room/# {IRC channel name}:libera.chat` will also work, for example - for the #ansible-docs channel it would be https://app.element.io/#/room/#ansible-docs:libera.chat.

### [General channels](communication.md#id12)

The clickable links will take you directly to the relevant Matrix room in your browser; room/channel information is also given for use in other clients:

- [Community social room and posting news for the Bullhorn newsletter](https://matrix.to:/#/#social:ansible.com) - `Matrix: #social:ansible.com | IRC: #ansible-social`
- [General usage and support questions](https://matrix.to:/#/#users:ansible.com) - `Matrix: #users:ansible.com | IRC: #ansible`
- [Discussions on developer topics and code related to features or bugs](https://matrix.to/#/#devel:ansible.com) - `Matrix: #devel:ansible.com | IRC: #ansible-devel`
- [Discussions on community and collections related topics](https://matrix.to:/#/#community:ansible.com) - `Matrix: #community:ansible.com | IRC: #ansible-community`
- [For public community meetings](https://matrix.to/#/#meeting:ansible.im) - `Matrix: #meeting:ansible.im | IRC: #ansible-meeting`
  :   - We will generally announce these on one or more of the above mailing lists. See the [meeting schedule and agenda page](https://github.com/ansible/community/blob/main/meetings/README.md)

### [Working group-specific channels](communication.md#id13)

Many of the working groups have dedicated chat channels. See the [Working groups](communication.md#working-group-list) for more information.

### [Regional and Language-specific channels](communication.md#id14)

- Comunidad Ansible en español - Matrix: [#espanol:ansible.im](https://matrix.to:/#/#espanol:ansible.im) | IRC: `#ansible-es`
- Communauté française d’Ansible - Matrix: [#francais:ansible.im](https://matrix.to:/#/#francais:ansible.im) | IRC: `#ansible-fr`
- Communauté suisse d’Ansible - Matrix: [#suisse:ansible.im](https://matrix.to:/#/#suisse:ansible.im) | IRC: `#ansible-zh`
- European Ansible Community - Matrix: [#europe:ansible.im](https://matrix.to:/#/#europe:ansible.im) | IRC: `#ansible-eu`

### [Meetings on chat](communication.md#id15)

The Ansible community holds regular meetings on various topics on Matrix/IRC, and anyone who is interested is invited to participate. For more information about Ansible meetings, consult the [meeting schedule and agenda page](https://github.com/ansible/community/blob/main/meetings/README.md).

## [Working groups](communication.md#id16)

Our community working groups are represented in forms of [Forum groups](https://forum.ansible.com/g) (new style) or [wiki pages](https://github.com/ansible/community/wiki#working-groups) (deprecated).

Many of them meet in chat. If you want to get involved in a working group, join the Matrix room or IRC channel where it meets or comment on the agenda.

- [AAP Configuration as Code](https://github.com/redhat-cop/controller_configuration/wiki/AAP-Configuration-as-Code) - Matrix: [#aap_config_as_code:ansible.com](https://matrix.to/#/#aap_config_as_code:ansible.com)
- [Amazon (AWS) Working Group](https://github.com/ansible/community/wiki/AWS) - Matrix: [#aws:ansible.com](https://matrix.to:/#/#aws:ansible.com) | IRC: `#ansible-aws`
- [AWX Working Group](https://github.com/ansible/awx) - Matrix: [#awx:ansible.com](https://matrix.to:/#/#awx:ansible.com) | IRC: `#ansible-awx`
- [Azure Working Group](https://github.com/ansible/community/wiki/Azure) - Matrix: [#azure:ansible.com](https://matrix.to:/#/#azure:ansible.com) | IRC: `#ansible-azure`
- [Community Working Group](https://github.com/ansible/community/wiki/Community) (including Meetups) - Matrix: [#community:ansible.com](https://matrix.to:/#/#community:ansible.com) | IRC: `#ansible-community`
- [Container Working Group](https://github.com/ansible/community/wiki/Container) - Matrix: [#container:ansible.com](https://matrix.to:/#/#container:ansible.com) | IRC: `#ansible-container`
- [Contributor Experience Working Group](https://github.com/ansible/community/wiki/Contributor-Experience) - Matrix: [#community:ansible.com](https://matrix.to:/#/#community:ansible.com) | IRC: `#ansible-community`
- [DigitalOcean Working Group](https://github.com/ansible/community/wiki/Digital-Ocean) - Matrix: [#digitalocean:ansible.im](https://matrix.to:/#/#digitalocean:ansible.im) | IRC: `#ansible-digitalocean`
- [Diversity Working Group](https://github.com/ansible/community/wiki/Diversity) - Matrix: [#diversity:ansible.com](https://matrix.to:/#/#diversity:ansible.com) | IRC: `#ansible-diversity`
- [Docker Working Group](https://github.com/ansible/community/wiki/Docker) - Matrix: [#devel:ansible.com](https://matrix.to:/#/#devel:ansible.com) | IRC: `#ansible-devel`
- [Documentation Working Group](https://forum.ansible.com/g/Docs) - Matrix: [#docs:ansible.com](https://matrix.to:/#/#docs:ansible.com) | IRC: `#ansible-docs`
- [Galaxy Working Group](https://github.com/ansible/community/wiki/Galaxy) - Matrix: [#galaxy:ansible.com](https://matrix.to:/#/#galaxy:ansible.com) | IRC: `#ansible-galaxy`
- [JBoss Working Group](https://github.com/ansible/community/wiki/JBoss) - Matrix: [#jboss:ansible.com](https://matrix.to:/#/#jboss:ansible.com) | IRC: `#ansible-jboss`
- [Kubernetes Working Group](https://github.com/ansible/community/wiki/Kubernetes) - Matrix: [#kubernetes:ansible.com](https://matrix.to:/#/#kubernetes:ansible.com) | IRC: `#ansible-kubernetes`
- [Linode Working Group](https://github.com/ansible/community/wiki/Linode) - Matrix: [#linode:ansible.com](https://matrix.to:/#/#linode:ansible.com) | IRC: `#ansible-linode`
- [Molecule Working Group](https://github.com/ansible/community/wiki/Molecule) ([testing platform for Ansible playbooks and roles](https://ansible.readthedocs.io/projects/molecule/)) - Matrix: [#molecule:ansible.im](https://matrix.to:/#/#molecule:ansible.im) | IRC: `#ansible-molecule`
- [MySQL Working Group](https://forum.ansible.com/g/MySQLTeam) - Matrix: [#mysql:ansible.com](https://matrix.to:/#/#mysql:ansible.com)
- [Network Working Group](https://github.com/ansible/community/wiki/Network) - Matrix: [#network:ansible.com](https://matrix.to:/#/#network:ansible.com) | IRC: `#ansible-network`
- [PostgreSQL Working Group](https://forum.ansible.com/g/PostgreSQLTeam/) - Matrix: [#postgresql:ansible.com](https://matrix.to:/#/#postgresql:ansible.com)
- [Release Management Working Group](https://forum.ansible.com/g/release-managers) - Matrix: [#release-management:ansible.com](https://matrix.to/#/#release-management:ansible.com)
- [Remote Management Working Group](https://github.com/ansible/community/issues/409) - Matrix: [#devel:ansible.com](https://matrix.to:/#/#devel:ansible.com) | IRC: `#ansible-devel`
- [Storage Working Group](https://github.com/ansible/community/wiki/Storage) - Matrix: [#storage:ansible.com](https://matrix.to/#/#storage:ansible.com) | IRC: `#ansible-storage`
- [VMware Working Group](https://github.com/ansible/community/wiki/VMware) - Matrix: [#vmware:ansible.com](https://matrix.to:/#/#vmware:ansible.com) | IRC: `#ansible-vmware`
- [Windows Working Group](https://github.com/ansible/community/wiki/Windows) - Matrix: [#windows:ansible.com](https://matrix.to:/#/#windows:ansible.com) | IRC: `#ansible-windows`
- [Ansible developer tools Group](https://github.com/ansible/community/wiki/Ansible-developer-tools) - Matrix: [#devtools:ansible.com](https://matrix.to/#/#devtools:ansible.com) | IRC: `#ansible-devtools`

Want to [form a new Working Group](https://github.com/ansible/community/blob/main/WORKING-GROUPS.md)?

## [Ansible Community Topics](communication.md#id17)

The [Ansible Community Steering Committee](https://docs.ansible.com/ansible/devel/community/steering/community_steering_committee.html) uses the [community-topics repository](https://github.com/ansible-community/community-topics/issues) to asynchronously discuss with the Community and vote on Community topics in corresponding issues.

Create a new issue in the [repository](https://github.com/ansible-community/community-topics/issues) if you want to discuss an idea that impacts any of the following:

- Ansible Community
- Community collection best practices and [requirements](https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_requirements.html)
- [Community collection inclusion policy](https://github.com/ansible-collections/ansible-inclusion/blob/main/README.md)
- [The Community governance](https://docs.ansible.com/ansible/devel/community/steering/community_steering_committee.html)
- Other proposals of importance that need the Committee or overall Ansible community attention

## [Ansible Automation Platform support questions](communication.md#id18)

Red Hat Ansible [Automation Platform](https://www.ansible.com/products/automation-platform) is a subscription that contains support, certified content, and tooling for Ansible including content management, a controller, UI and REST API.

If you have a question about Ansible Automation Platform, visit [Red Hat support](https://access.redhat.com/products/red-hat-ansible-automation-platform/) rather than using a chat channel or the general project mailing list.

## [The Bullhorn](communication.md#id19)

**The Bullhorn** is our newsletter for the Ansible contributor community. Please [subscribe](https://eepurl.com/gZmiEP) to receive it.

If you have any content you would like to share, please [contribute/suggest it](https://github.com/ansible/community/wiki/News#the-bullhorn) for upcoming releases.

If you have any questions, please reach out to us at `the-bullhorn@redhat.com`.

Read past issues on the official Bullhorn’s [wiki page](https://github.com/ansible/community/wiki/News#the-bullhorn).

## [Asking questions over email](communication.md#id20)

> **Note:**
>
> This form of communication is deprecated. Consider using the [Forum](communication.md#forum) instead.

Your first post to the mailing list will be moderated (to reduce spam), so please allow up to a day or so for your first post to appear.

- [Ansible Announce list](https://groups.google.com/forum/#!forum/ansible-announce) is a read-only list that shares information about new releases of Ansible, and also rare infrequent event information, such as announcements about an upcoming AnsibleFest, which is our official conference series. Worth subscribing to!
- [Ansible AWX List](https://forum.ansible.com/tag/awx) is for [Ansible AWX](https://github.com/ansible/awx)
- [Ansible Development List](https://groups.google.com/forum/#!forum/ansible-devel) is for questions about developing Ansible modules (mostly in Python), fixing bugs in the Ansible Core code, asking about prospective feature design, or discussions about extending Ansible or features in progress.
- [Ansible Outreach List](https://groups.google.com/forum/#!forum/ansible-outreach) help with promoting Ansible and [Ansible Meetups](https://www.meetup.com/topics/ansible/)
- [Ansible Project List](https://groups.google.com/forum/#!forum/ansible-project) is for sharing Ansible tips, answering questions about playbooks and roles, and general user discussion.
- [Molecule Discussions](https://github.com/ansible-community/molecule/discussions) is designed to aid with the development and testing of Ansible roles with Molecule.

The Ansible mailing lists are hosted on Google, but you do not need a Google account to subscribe. To subscribe to a group from a non-Google account, send an email to the subscription address requesting the subscription. For example: `ansible-devel+subscribe@googlegroups.com`.
