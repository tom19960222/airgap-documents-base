---
collection: gitlab
version: "17.9.8"
title: "Use Auto DevOps to deploy to EC2"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/topics/autodevops/cloud_deployments/auto_devops_with_ec2.md
fetched_at: 2025-05-07T10:05:15Z
---
To use [Auto DevOps](../_index.md) to deploy to EC2:

1. Define [your AWS credentials as CI/CD variables](../../../ci/cloud_deployment/_index.md#authenticate-gitlab-with-aws).
1. In your `.gitlab-ci.yml` file, reference the `Auto-Devops.gitlab-ci.yml` template.
1. Define a job for the `build` stage named `build_artifact`. For example:

   ```yaml
   # .gitlab-ci.yml

   include:
     - template: Auto-DevOps.gitlab-ci.yml

   variables:
     AUTO_DEVOPS_PLATFORM_TARGET: EC2

   build_artifact:
     stage: build
     script:
       - <your build script goes here>
     artifacts:
       paths:
         - <built artifact>
   ```

<i class="fa fa-youtube-play youtube" aria-hidden="true"></i>
For a video walkthrough of this process, view [Auto Deploy to EC2](https://www.youtube.com/watch?v=4B-qSwKnacA).
