---
collection: ansible
version: "8"
title: "How to test a collection PR"
source_url: https://docs.ansible.com/projects/ansible/8/community/collection_contributors/collection_test_pr_locally.html
fetched_at: 2026-07-28T01:00:26+00:00
---
# How to test a collection PR

Reviewers and issue authors can verify a PR fixes the reported bug by testing the PR locally.

- [Prepare your environment](collection_test_pr_locally.md#prepare-your-environment)
- [Test the Pull Request](collection_test_pr_locally.md#test-the-pull-request)

## [Prepare your environment](collection_test_pr_locally.md#id1)

We assume that you use Linux as a work environment (you can use a virtual machine as well) and have `git` installed.

1. [Install Ansible](../../installation_guide/intro_installation.md#installation-guide) or ansible-core.
2. Create the following directories in your home directory:

> ```bash
> mkdir -p ~/ansible_collections/NAMESPACE/COLLECTION_NAME
> ```
>
> For example, if the collection is `community.general`:
>
> ```bash
> mkdir -p ~/ansible_collections/community/general
> ```
>
> If the collection is `ansible.posix`:
>
> ```bash
> mkdir -p ~/ansible_collections/ansible/posix
> ```

3. Clone the forked repository from the author profile to the created path:

> ```bash
> git clone https://github.com/AUTHOR_ACC/COLLECTION_REPO.git ~/ansible_collections/NAMESPACE/COLLECTION_NAME
> ```

4. Go to the cloned repository.

> ```bash
> cd ~/ansible_collections/NAMESPACE/COLLECTION_NAME
> ```

5. Checkout the PR branch (it can be retrieved from the PR’s page):

> ```bash
> git checkout pr_branch
> ```

## [Test the Pull Request](collection_test_pr_locally.md#id2)

1. Include ~/ansible_collections in COLLECTIONS_PATHS. See [COLLECTIONS_PATHS](../../reference_appendices/config.md#collections-paths) for details.
2. Run your playbook using the PR branch and verify the PR fixed the bug.
3. Give feedback on the pull request or the linked issue(s).
