---
collection: ceph
version: "19.2.2"
title: "Cloning the Ceph Source Code Repository"
source_url: https://docs.ceph.com/en/squid/install/clone-source/
fetched_at: 2026-07-27T16:41:46+00:00
---
# Cloning the Ceph Source Code Repository

To clone a Ceph branch of the Ceph source code, go to [github Ceph
Repository](https://github.com/ceph/ceph), select a branch (`main` by default), and click the **Download
ZIP** button.

To clone the entire git repository, [install](index.md#install-git) and configure
`git`.

## Install Git

To install `git` on Debian/Ubuntu, run the following command:

```
sudo apt-get install git
```

To install `git` on CentOS/RHEL, run the following command:

```
sudo yum install git
```

You must have a `github` account. If you do not have a `github`
account, go to [github.com](https://github.com) and register. Follow the directions for setting
up git at [Set Up Git](https://help.github.com/linux-set-up-git).

## Add SSH Keys (Optional)

To commit code to Ceph or to clone the respository by using SSH
(`git@github.com:ceph/ceph.git`), you must generate SSH keys for github.

> **Tip:**
>
> If you want only to clone the repository, you can
> use `git clone --recursive https://github.com/ceph/ceph.git`
> without generating SSH keys.

To generate SSH keys for `github`, run the following command:

```
ssh-keygen
```

To print the SSH key that you just generated and that you will add to your
`github` account, use the `cat` command. (The following example assumes you
used the default file path.):

```
cat .ssh/id_rsa.pub
```

Copy the public key.

Go to your `github` account, click “Account Settings” (represented by the
‘tools’ icon), and click “SSH Keys” on the left side navbar.

Click “Add SSH key” in the “SSH Keys” list, enter a name for the key, paste the
key you generated, and press the “Add key” button.

## Clone the Source

To clone the Ceph source code repository, run the following command:

```
git clone --recursive https://github.com/ceph/ceph.git
```

After `git clone` has run, you should have a full copy of the Ceph
repository.

> **Tip:**
>
> Make sure you maintain the latest copies of the submodules included in
> the repository. Running `git status` will tell you whether the submodules
> are out of date. See [Updating Submodules](index.md#update-submodules) for more information.

```
cd ceph
git status
```

### Updating Submodules

If your submodules are out of date, run the following commands:

> ```
> git submodule update --force --init --recursive --progress
> git clean -fdx
> git submodule foreach git clean -fdx
> ```

If you still have problems with a submodule directory, use `rm -rf [directory
name]` to remove the directory. Then run `git submodule update --init
--recursive --progress` again.

## Choose a Branch

Once you clone the source code and submodules, your Ceph repository
will be on the `main` branch by default, which is the unstable
development branch. You may choose other branches too.

- `main`: The unstable development branch.
- `stable-release-name`: The name of the stable, [Active Releases](https://docs.ceph.com/en/latest/releases/#active-releases). e.g. `Pacific`
- `next`: The release candidate branch.

```
git checkout main
```

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
