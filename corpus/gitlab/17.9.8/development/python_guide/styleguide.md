---
collection: gitlab
version: "17.9.8"
title: "Python style guide"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/development/python_guide/styleguide.md
fetched_at: 2025-05-07T10:05:15Z
---
## Testing

### Overview

Testing at GitLab, including in Python codebases is a core priority rather than an afterthought. It is therefore important to consider test design quality alongside feature design from the start.

Use [Pytest](https://docs.pytest.org/en/stable/) for Python testing.

### Recommended reading

- [Five Factor Testing](https://madeintandem.com/blog/five-factor-testing/): Why do we need tests?
- [Principles of Automated Testing](https://www.lihaoyi.com/post/PrinciplesofAutomatedTesting.html): Levels of testing. Prioritize tests. Cost of tests.

### Testing levels

Before writing tests, understand the different testing levels and determine the appropriate level for your changes.

[Learn more about the different testing levels](../testing_guide/testing_levels.md), and how to decide at what level your changes should be tested.

### Recommendation when mocking

- Use `unittest.mock` library.
- Mock at the right level, for example, at method call boundaries.
- Mock external services and APIs.

### Testing in Python vs. Ruby on Rails

- [Work item](https://gitlab.com/gitlab-org/gitlab/-/issues/516193)
