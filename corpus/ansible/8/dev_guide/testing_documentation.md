---
collection: ansible
version: "8"
title: "Testing plugin documentation"
source_url: https://docs.ansible.com/projects/ansible/8/dev_guide/testing_documentation.html
fetched_at: 2026-07-28T01:04:21+00:00
---
# Testing plugin documentation

A quick test while developing is to use `ansible-doc -t <plugin_type> <name>` to see if it renders, you might need to add `-M /path/to/module` if the module is not somewhere Ansible expects to find it.

Before you submit a plugin for inclusion in Ansible, you must test your documentation for correct HTML rendering and for modules to ensure that the argspec matches the documentation in your Python file.
The community pages offer more information on [testing reStructuredText documentation](../community/documentation_contributions.md#testing-documentation-locally).

For example, to check the HTML output of your module documentation:

1. Ensure working [development environment](developing_modules_general.md#environment-setup).
2. Install required Python packages (drop ‘–user’ in venv/virtualenv):

   ```bash
   pip install --user -r requirements.txt
   pip install --user -r docs/docsite/requirements.txt
   ```
3. Ensure your module is in the correct directory: `lib/ansible/modules/mymodule.py` or in a configured path.
4. Build HTML from your module documentation: `MODULES=mymodule make webdocs`.
5. To build the HTML documentation for multiple modules, use a comma-separated list of module names: `MODULES=mymodule,mymodule2 make webdocs`.
6. View the HTML page at `file:///path/to/docs/docsite/_build/html/modules/mymodule_module.html`.

To ensure that your module documentation matches your `argument_spec`:

1. Install required Python packages (drop ‘–user’ in venv/virtualenv):

   ```bash
   pip install --user -r test/lib/ansible_test/_data/requirements/sanity.txt
   ```
2. run the `validate-modules` test:

   ```bash
   ansible-test sanity --test validate-modules mymodule
   ```

For other plugin types the steps are similar, just adjusting names and paths to the specific type.
