---
collection: ansible
version: "6"
title: "Running integration tests"
source_url: https://docs.ansible.com/projects/ansible/6/community/collection_contributors/collection_integration_running.html
fetched_at: 2026-07-27T16:43:13+00:00
---
# Running integration tests

In the following examples, we will use `Docker` to run integration tests locally. Ensure you have [Prepare your environment](collection_test_pr_locally.md#collection-prepare-environment) first.

We assume that you are in the `~/ansible_collections/NAMESPACE/COLLECTION` directory.

After you change the tests, you can run them with the following command:

```
ansible-test integration <target_name> --docker <distro>
```

The `target_name` is a test role directory containing the tests. For example, if the test files you changed are stored in the `tests/integration/targets/postgresql_info/` directory and you want to use the `fedora34` container image, then the command will be:

```bash
ansible-test integration postgresql_info --docker fedora34
```

You can use the `-vv` or `-vvv` argument if you need more detailed output.

In the examples above, the `fedora34` test image will be automatically downloaded and used to create and run a test container.

See the [list of supported container images](../../dev_guide/testing_integration.md#test-container-images).

In some cases, for example, for platform independent tests, the `default` test image is required. Use the `--docker default` or just `--docker` option without specifying a distribution in this case.

> **Note:**
>
> If you have any difficulties with writing or running integration tests or you are not sure if the case can be covered, submit your pull request without the tests. Other contributors can help you with them later if needed.
