---
collection: gitlab
version: "17.9.8"
title: "Service Desk email Rake tasks"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/administration/raketasks/service_desk_email.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab Self-Managed

**History:**

- [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/108279) in GitLab 15.9.

The following are Service Desk email-related Rake tasks.

## Secrets

GitLab can use [Service Desk email](../../user/project/service_desk/configure.md#configure-service-desk-alias-email) secrets read from an encrypted file instead of storing them in plaintext in the file system. The following Rake tasks are provided for updating the contents of the encrypted file.

### Show secret

Show the contents of the current Service Desk email secrets.

**Tab: Linux package (Omnibus)**

```shell
sudo gitlab-rake gitlab:service_desk_email:secret:show
```

**Tab: Helm chart (Kubernetes)**

Use a Kubernetes secret to store the Service Desk email password. For more information,
read about [Helm IMAP secrets](https://docs.gitlab.com/charts/installation/secrets.html#imap-password-for-service-desk-emails).

**Tab: Docker**

```shell
sudo docker exec -t <container name> gitlab:service_desk_email:secret:show
```

**Tab: Self-compiled (source)**

```shell
bundle exec rake gitlab:service_desk_email:secret:show RAILS_ENV=production
```

#### Example output

```plaintext
password: 'examplepassword'
user: 'service-desk-email@mail.example.com'
```

### Edit secret

Opens the secret contents in your editor, and writes the resulting content to the encrypted secret file when you exit.

**Tab: Linux package (Omnibus)**

```shell
sudo gitlab-rake gitlab:service_desk_email:secret:edit EDITOR=vim
```

**Tab: Helm chart (Kubernetes)**

Use a Kubernetes secret to store the Service Desk email password. For more information,
read about [Helm IMAP secrets](https://docs.gitlab.com/charts/installation/secrets.html#imap-password-for-service-desk-emails).

**Tab: Docker**

```shell
sudo docker exec -t <container name> gitlab:service_desk_email:secret:edit EDITOR=editor
```

**Tab: Self-compiled (source)**

```shell
bundle exec rake gitlab:service_desk_email:secret:edit RAILS_ENV=production EDITOR=vim
```

### Write raw secret

Write new secret content by providing it on `STDIN`.

**Tab: Linux package (Omnibus)**

```shell
echo -e "password: 'examplepassword'" | sudo gitlab-rake gitlab:service_desk_email:secret:write
```

**Tab: Helm chart (Kubernetes)**

Use a Kubernetes secret to store the Service Desk email password. For more information,
read about [Helm IMAP secrets](https://docs.gitlab.com/charts/installation/secrets.html#imap-password-for-service-desk-emails).

**Tab: Docker**

```shell
sudo docker exec -t <container name> /bin/bash
echo -e "password: 'examplepassword'" | gitlab-rake gitlab:service_desk_email:secret:write
```

**Tab: Self-compiled (source)**

```shell
echo -e "password: 'examplepassword'" | bundle exec rake gitlab:service_desk_email:secret:write RAILS_ENV=production
```

### Secrets examples

**Editor example**

The write task can be used in cases where the edit command does not work with your editor:

```shell
# Write the existing secret to a plaintext file
sudo gitlab-rake gitlab:service_desk_email:secret:show > service_desk_email.yaml
# Edit the service_desk_email file in your editor
...
# Re-encrypt the file
cat service_desk_email.yaml | sudo gitlab-rake gitlab:service_desk_email:secret:write
# Remove the plaintext file
rm service_desk_email.yaml
```

**KMS integration example**

It can also be used as a receiving application for content encrypted with a KMS:

```shell
gcloud kms decrypt --key my-key --keyring my-test-kms --plaintext-file=- --ciphertext-file=my-file --location=us-west1 | sudo gitlab-rake gitlab:service_desk_email:secret:write
```

**Google Cloud secret integration example**

It can also be used as a receiving application for secrets out of Google Cloud:

```shell
gcloud secrets versions access latest --secret="my-test-secret" > $1 | sudo gitlab-rake gitlab:service_desk_email:secret:write
```
