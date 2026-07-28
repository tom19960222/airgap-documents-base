---
collection: ansible
version: "8"
title: "Contributing to the Ansible Documentation"
source_url: https://docs.ansible.com/projects/ansible/8/community/documentation_contributions.html
fetched_at: 2026-07-28T00:58:59+00:00
---
# Contributing to the Ansible Documentation

Ansible has a lot of documentation and a small team of writers. Community support helps us keep up with new features, fixes, and changes.

Improving the documentation is an easy way to make your first contribution to the Ansible project. You do not have to be a programmer, since most of our documentation is written in YAML (module documentation) or [reStructuredText](https://docutils.sourceforge.io/rst.html) (rST). Some collection-level documentation is written in a subset of [Markdown](https://github.com/ansible/ansible/issues/68119#issuecomment-596723053). If you are using Ansible, you already use YAML in your playbooks. rST and Markdown are mostly just text. You do not even need git experience, if you use the `Edit on GitHub` option.

If you find a typo, a broken example, a missing topic, or any other error or omission on this documentation website, let us know. Here are some ways to support Ansible documentation:

- [Editing docs directly on GitHub](documentation_contributions.md#editing-docs-directly-on-github)
- [Reviewing or solving open issues](documentation_contributions.md#reviewing-or-solving-open-issues)
- [Reviewing open PRs](documentation_contributions.md#reviewing-open-prs)
- [Opening a new issue and/or PR](documentation_contributions.md#opening-a-new-issue-and-or-pr)
- [Verifying your documentation PR](documentation_contributions.md#verifying-your-documentation-pr)

  - [Setting up your environment to build documentation locally](documentation_contributions.md#setting-up-your-environment-to-build-documentation-locally)
  - [Testing the documentation locally](documentation_contributions.md#testing-the-documentation-locally)
  - [Building the documentation locally](documentation_contributions.md#building-the-documentation-locally)

    - [Periodically cloning Ansible Core](documentation_contributions.md#periodically-cloning-ansible-core)
    - [Building a single rST page](documentation_contributions.md#building-a-single-rst-page)
    - [Building all the rST pages](documentation_contributions.md#building-all-the-rst-pages)
    - [Building module docs and rST pages](documentation_contributions.md#building-module-docs-and-rst-pages)
    - [Building rST files with `sphinx-build`](documentation_contributions.md#building-rst-files-with-sphinx-build)
    - [Running the final tests](documentation_contributions.md#running-the-final-tests)
- [Joining the documentation working group](documentation_contributions.md#joining-the-documentation-working-group)

## [Editing docs directly on GitHub](documentation_contributions.md#id2)

For typos and other quick fixes, you can edit most of the documentation right from the site. Look at the top right corner of this page. That `Edit on GitHub` link is available on all the guide pages in the documentation. If you have a GitHub account, you can submit a quick and easy pull request this way.

> **Note:**
>
> The source files for individual collection plugins exist in their respective repositories. Follow the link to the collection on Galaxy to find where the repository is located and any guidelines on how to contribute to that collection.

To submit a documentation PR from docs.ansible.com with `Edit on GitHub`:

1. Click on `Edit on GitHub`.
2. If you don’t already have a fork of the ansible repo on your GitHub account, you’ll be prompted to create one.
3. Fix the typo, update the example, or make whatever other change you have in mind.
4. Enter a commit message in the first rectangle under the heading `Propose file change` at the bottom of the GitHub page. The more specific, the better. For example, “fixes typo in my_module description”. You can put more detail in the second rectangle if you like. Leave the `+label: docsite_pr` there.
5. Submit the suggested change by clicking on the green “Propose file change” button. GitHub will handle branching and committing for you, and open a page with the heading “Comparing Changes”.
6. Click on `Create pull request` to open the PR template.
7. Fill out the PR template, including as much detail as appropriate for your change. You can change the title of your PR if you like (by default it is the same as your commit message). In the `Issue Type` section, delete all lines except the `Docs Pull Request` line.
8. Submit your change by clicking on `Create pull request` button.
9. Be patient while Ansibot, our automated script, adds labels, pings the docs maintainers, and kicks off a CI testing run.
10. Keep an eye on your PR - the docs team may ask you for changes.

## [Reviewing or solving open issues](documentation_contributions.md#id3)

Review or solve open documentation issues for:

- [Ansible projects](https://github.com/search?q=user%3Aansible+user%3Aansible-community+label%3Adocs+state%3Aopen+type%3Aissue&type=Issues)
- [Ansible collections](https://github.com/search?q=user%3Aansible-collections+label%3Adocs+state%3Aopen+type%3Aissue&type=Issues)

## [Reviewing open PRs](documentation_contributions.md#id4)

Review open documentation pull requests for:

- Ansible [documentation](https://github.com/ansible/ansible-documentation/pulls)
- Ansible [projects](https://github.com/search?q=user%3Aansible+user%3Aansible-community+label%3Adocs+state%3Aopen+type%3Apr)
- Ansible [collections](https://github.com/search?q=user%3Aansible-collections+label%3Adocs+state%3Aopen+type%3Apr)

To add a helpful review, please:

- Test the change if applicable.
- Think if it can be made better (including wording, structure, fixing typos and so on).
- Suggest improvements.
- Approve the change with the `looks good to me` comment.

## [Opening a new issue and/or PR](documentation_contributions.md#id5)

If the problem you have noticed is too complex to fix with the `Edit on GitHub` option, and no open issue or PR already documents the problem, please open an issue and/or a PR on the correct underlying repo - `ansible/ansible-documentation` for most pages that are not plugin or module documentation. If the documentation page has no `Edit on GitHub` option, check if the page is for a module within a collection. If so, follow the link to the collection on Galaxy and select the `repo` button in the upper right corner to find the source repository for that collection and module. The Collection README file should contain information on how to contribute to that collection, or report issues.

A great documentation GitHub issue or PR includes:

- a specific title
- a detailed description of the problem (even for a PR - it is hard to evaluate a suggested change unless we know what problem it is meant to solve)
- links to other information (related issues/PRs, external documentation, pages on docs.ansible.com, and so on)

## [Verifying your documentation PR](documentation_contributions.md#id6)

If you make multiple changes to the documentation, or add more than a line to it, before you open a pull request, please:

1. Check that your text follows our [Ansible documentation style guide](../dev_guide/style_guide/index.md#style-guide).
2. Test your changes for rST errors.
3. Build the page, and preferably the entire documentation site, locally.

> **Note:**
>
> The following sections apply to documentation sourced from the `ansible/ansible-documentation` repo and does not apply to documentation from an individual collection. See the collection README file for details on how to contribute to that collection.

### [Setting up your environment to build documentation locally](documentation_contributions.md#id7)

To build documentation locally, ensure you have a working [development environment](../dev_guide/developing_modules_general.md#environment-setup).

To work with documentation on your local machine, you should use a version of Python that meets the minimum requirement for `ansible-core`.
For more information on minimum Python versions, see the [support matrix](../reference_appendices/release_and_maintenance.md#support-life).

1. Set up a virtual environment in which to install dependencies.

   ```bash
   python3 -m venv ./venv
   source ./venv/bin/activate
   ```
2. Clone required parts of Ansible Core for the docs build.

   ```bash
   python3 docs/bin/clone-core.py
   ```
3. Install either the unpinned or tested documentation dependencies.

   ```bash
   pip install -r tests/requirements.in -c tests/requirements.txt # Installs tested dependency versions.
   pip install -r tests/requirements.in # Installs the unpinned dependency versions.
   pip install -r tests/requirements-relaxed.in # Installs the unpinned dependency versions including untested antsibull-docs.
   ```

### [Testing the documentation locally](documentation_contributions.md#id8)

To test an individual file for rST errors:

```bash
rstcheck changed_file.rst
```

### [Building the documentation locally](documentation_contributions.md#id9)

Building the documentation is the best way to check for errors and review your changes. Once rstcheck runs with no errors, navigate to `ansible-documentation/docs/docsite` and then build the page(s) you want to review.

> > **Note:**
> >
> > If building on macOS with Python 3.8 or later, you must use Sphinx >= 2.2.2. See [#6803](https://github.com/sphinx-doc/sphinx/pull/6879) for details.

#### [Periodically cloning Ansible Core](documentation_contributions.md#id10)

Documentation in the `ansible/ansible-documentation` repository builds “on top of” the `ansible/ansible` repository.
When you set up your local build environment, you clone the relevant parts Ansible Core.

To ensure that you use the latest source from Ansible Core, you should periodically run the following script before you build documentation:

> ```bash
> python3 docs/bin/clone-core.py
> ```

#### [Building a single rST page](documentation_contributions.md#id11)

To build a single rST file with the make utility:

```bash
make htmlsingle rst=path/to/your_file.rst
```

For example:

```bash
make htmlsingle rst=community/documentation_contributions.rst
```

This process compiles all the links but provides minimal log output. If you’re writing a new page or want more detailed log output, refer to the instructions on [Building rST files with sphinx-build](documentation_contributions.md#build-with-sphinx-build)

> **Note:**
>
> `make htmlsingle` adds `rst/` to the beginning of the path you provide in `rst=`, so you can’t type the filename with autocomplete. Here are the error messages you will see if you get this wrong:
>
> > - If you run `make htmlsingle` from the `docs/docsite/rst/` directory: `` make: *** No rule to make target `htmlsingle'.  Stop. ``
> > - If you run `make htmlsingle` from the `docs/docsite/` directory with the full path to your rST document: `sphinx-build: error: cannot find files ['rst/rst/community/documentation_contributions.rst']`.

#### [Building all the rST pages](documentation_contributions.md#id12)

To build all the rST files without any module documentation:

```bash
MODULES=none make webdocs
```

#### [Building module docs and rST pages](documentation_contributions.md#id13)

To build documentation for a few modules included in `ansible/ansible` plus all the rST files, use a comma-separated list:

```bash
MODULES=one_module,another_module make webdocs
```

To build all the module documentation plus all the rST files:

```bash
make webdocs
```

#### [Building rST files with `sphinx-build`](documentation_contributions.md#id14)

Advanced users can build one or more rST files with the sphinx utility directly. `sphinx-build` returns misleading `undefined label` warnings if you only build a single page, because it does not create internal links. However, `sphinx-build` returns more extensive syntax feedback, including warnings about indentation errors and `x-string without end-string` warnings. This can be useful, especially if you’re creating a new page from scratch. To build a page or pages with `sphinx-build`:

```bash
sphinx-build [options] sourcedir outdir [filenames...]
```

You can specify filenames, or `–a` for all files, or omit both to compile only new/changed files.

For example:

```bash
sphinx-build -b html -c rst/ rst/dev_guide/ _build/html/dev_guide/ rst/dev_guide/developing_modules_documenting.rst
```

#### [Running the final tests](documentation_contributions.md#id15)

When you submit a documentation pull request, automated tests are run. Those same tests can be run locally. To do so, navigate to the repository’s top directory and run:

```bash
make clean -C docs/docsite
python tests/checkers.py docs-build
python tests/checkers.py rstcheck
```

It is recommended to run tests on a clean copy of the repository, which is the purpose of the `make clean` command.

## [Joining the documentation working group](documentation_contributions.md#id16)

The Documentation Working Group (DaWGs) meets weekly on Tuesdays in the Docs chat (using [Matrix](https://matrix.to/#/#docs:ansible.im) or using IRC at [irc.libera.chat](https://libera.chat/)). For more information, including links to our agenda and a calendar invite, please visit the [working group page in the community repo](https://github.com/ansible/community/wiki/Docs).

> **See also:**
>
> [More about testing module documentation](../dev_guide/testing_documentation.md#testing-module-documentation)
>
> [More about documenting modules](../dev_guide/developing_modules_documenting.md#module-documenting)
