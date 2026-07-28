---
collection: ansible
version: "6"
title: "Ansible Reference: Module Utilities"
source_url: https://docs.ansible.com/projects/ansible/6/reference_appendices/module_utils.html
fetched_at: 2026-07-27T16:39:35+00:00
---
# Ansible Reference: Module Utilities

This page documents utilities intended to be helpful when writing
Ansible modules in Python.

## AnsibleModule

To use this functionality, include `from ansible.module_utils.basic import AnsibleModule` in your module.

*class* ansible.module_utils.basic.AnsibleModule(*argument_spec*, *bypass_checks=False*, *no_log=False*, *mutually_exclusive=None*, *required_together=None*, *required_one_of=None*, *add_file_common_args=False*, *supports_check_mode=False*, *required_if=None*, *required_by=None*)
:   Common code for quickly building an ansible module in Python
    (although you can write modules with anything that can return JSON).

    See [Developing modules](../dev_guide/developing_modules_general.md#developing-modules-general) for a general introduction
    and [Ansible module architecture](../dev_guide/developing_program_flow_modules.md#developing-program-flow-modules) for more detailed explanation.

    add_path_info(*kwargs*)
    :   for results that are files, supplement the info about the file
        in the return path with stats about the file path.

    atomic_move(*src*, *dest*, *unsafe_writes=False*)
    :   atomically move src to dest, copying attributes from dest, returns true on success
        it uses os.rename to ensure this as it is an atomic operation, rest of the function is
        to work around limitations, corner cases and ensure selinux context is saved if possible

    backup_local(*fn*)
    :   make a date-marked backup of the specified file, return True or False on success or failure

    boolean(*arg*)
    :   Convert the argument to a boolean

    digest_from_file(*filename*, *algorithm*)
    :   Return hex digest of local file for a digest_method specified by name, or None if file is not present.

    exit_json(*\*\*kwargs*)
    :   return from the module, without error

    fail_json(*msg*, *\*\*kwargs*)
    :   return from the module, with an error message

    find_mount_point(*path*)
    :   > Takes a path and returns it’s mount point

        Parameters:
        :   **path** – a string type with a filesystem path

        Returns:
        :   the path to the mount point as a text type

    get_bin_path(*arg*, *required=False*, *opt_dirs=None*)
    :   Find system executable in PATH.

        Parameters:
        :   - **arg** – The executable to find.
            - **required** – if executable is not found and required is `True`, fail_json
            - **opt_dirs** – optional list of directories to search in addition to `PATH`

        Returns:
        :   if found return full path; otherwise return None

    is_executable(*path*)
    :   is the given path executable?

        Parameters:
        :   **path** – The path of the file to check.

        Limitations:

        - Does not account for FSACLs.
        - Most times we really want to know “Can the current user execute this
          file”. This function does not tell us that, only if any execute bit is set.

    is_special_selinux_path(*path*)
    :   Returns a tuple containing (True, selinux_context) if the given path is on a
        NFS or other ‘special’ fs mount point, otherwise the return will be (False, None).

    load_file_common_arguments(*params*, *path=None*)
    :   many modules deal with files, this encapsulates common
        options that the file module accepts such that it is directly
        available to all modules and they can share code.

        Allows to overwrite the path/dest module argument by providing path.

    md5(*filename*)
    :   Return MD5 hex digest of local file using digest_from_file().

        Do not use this function unless you have no other choice for:
        :   1. Optional backwards compatibility
            2. Compatibility with a third party protocol

        This function will not work on systems complying with FIPS-140-2.

        Most uses of this function can use the module.sha1 function instead.

    preserved_copy(*src*, *dest*)
    :   Copy a file with preserved ownership, permissions and context

    run_command(*args*, *check_rc=False*, *close_fds=True*, *executable=None*, *data=None*, *binary_data=False*, *path_prefix=None*, *cwd=None*, *use_unsafe_shell=False*, *prompt_regex=None*, *environ_update=None*, *umask=None*, *encoding='utf-8'*, *errors='surrogate_or_strict'*, *expand_user_and_vars=True*, *pass_fds=None*, *before_communicate_callback=None*, *ignore_invalid_cwd=True*, *handle_exceptions=True*)
    :   Execute a command, returns rc, stdout, and stderr.

        Parameters:
        :   **args** – is the command to run
            \* If args is a list, the command will be run with shell=False.
            \* If args is a string and use_unsafe_shell=False it will split args to a list and run with shell=False
            \* If args is a string and use_unsafe_shell=True it runs with shell=True.

        Kw check_rc:
        :   Whether to call fail_json in case of non zero RC.
            Default False

        Kw close_fds:
        :   See documentation for subprocess.Popen(). Default True

        Kw executable:
        :   See documentation for subprocess.Popen(). Default None

        Kw data:
        :   If given, information to write to the stdin of the command

        Kw binary_data:
        :   If False, append a newline to the data. Default False

        Kw path_prefix:
        :   If given, additional path to find the command in.
            This adds to the PATH environment variable so helper commands in
            the same directory can also be found

        Kw cwd:
        :   If given, working directory to run the command inside

        Kw use_unsafe_shell:
        :   See args parameter. Default False

        Kw prompt_regex:
        :   Regex string (not a compiled regex) which can be
            used to detect prompts in the stdout which would otherwise cause
            the execution to hang (especially if no input data is specified)

        Kw environ_update:
        :   dictionary to *update* environ variables with

        Kw umask:
        :   Umask to be used when running the command. Default None

        Kw encoding:
        :   Since we return native strings, on python3 we need to
            know the encoding to use to transform from bytes to text. If you
            want to always get bytes back, use encoding=None. The default is
            “utf-8”. This does not affect transformation of strings given as
            args.

        Kw errors:
        :   Since we return native strings, on python3 we need to
            transform stdout and stderr from bytes to text. If the bytes are
            undecodable in the `encoding` specified, then use this error
            handler to deal with them. The default is `surrogate_or_strict`
            which means that the bytes will be decoded using the
            surrogateescape error handler if available (available on all
            python3 versions we support) otherwise a UnicodeError traceback
            will be raised. This does not affect transformations of strings
            given as args.

        Kw expand_user_and_vars:
        :   When `use_unsafe_shell=False` this argument
            dictates whether `~` is expanded in paths and environment variables
            are expanded before running the command. When `True` a string such as
            `$SHELL` will be expanded regardless of escaping. When `False` and
            `use_unsafe_shell=False` no path or variable expansion will be done.

        Kw pass_fds:
        :   When running on Python 3 this argument
            dictates which file descriptors should be passed
            to an underlying `Popen` constructor. On Python 2, this will
            set `close_fds` to False.

        Kw before_communicate_callback:
        :   This function will be called
            after `Popen` object will be created
            but before communicating to the process.
            (`Popen` object will be passed to callback as a first argument)

        Kw ignore_invalid_cwd:
        :   This flag indicates whether an invalid `cwd`
            (non-existent or not a directory) should be ignored or should raise
            an exception.

        Kw handle_exceptions:
        :   This flag indicates whether an exception will
            be handled inline and issue a failed_json or if the caller should
            handle it.

        Returns:
        :   A 3-tuple of return code (integer), stdout (native string),
            and stderr (native string). On python2, stdout and stderr are both
            byte strings. On python3, stdout and stderr are text strings converted
            according to the encoding and errors parameters. If you want byte
            strings on python3, use encoding=None to turn decoding to text off.

    sha1(*filename*)
    :   Return SHA1 hex digest of local file using digest_from_file().

    sha256(*filename*)
    :   Return SHA-256 hex digest of local file using digest_from_file().

## Basic

To use this functionality, include `import ansible.module_utils.basic` in your module.

ansible.module_utils.basic.get_all_subclasses(*cls*)
:   **Deprecated**: Use ansible.module_utils.common._utils.get_all_subclasses instead

ansible.module_utils.basic.get_platform()
:   **Deprecated** Use [`platform.system()`](https://docs.python.org/3/library/platform.html#platform.system "(in Python v3.11)") directly.

    Returns:
    :   Name of the platform the module is running on in a native string

    Returns a native string that labels the platform (“Linux”, “Solaris”, etc). Currently, this is
    the result of calling [`platform.system()`](https://docs.python.org/3/library/platform.html#platform.system "(in Python v3.11)").

ansible.module_utils.basic.heuristic_log_sanitize(*data*, *no_log_values=None*)
:   Remove strings that look like passwords from log messages

ansible.module_utils.basic.load_platform_subclass(*cls*, *\*args*, *\*\*kwargs*)
:   **Deprecated**: Use ansible.module_utils.common.sys_info.get_platform_subclass instead

## Argument Spec

Classes and functions for validating parameters against an argument spec.

### ArgumentSpecValidator

*class* ansible.module_utils.common.arg_spec.ArgumentSpecValidator(*argument_spec*, *mutually_exclusive=None*, *required_together=None*, *required_one_of=None*, *required_if=None*, *required_by=None*)
:   Argument spec validation class

    Creates a validator based on the `argument_spec` that can be used to
    validate a number of parameters using the [`validate()`](module_utils.md#ansible.module_utils.common.arg_spec.ArgumentSpecValidator.validate "ansible.module_utils.common.arg_spec.ArgumentSpecValidator.validate") method.

    Parameters:
    :   - **argument_spec** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.11)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")*,* [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.11)")*]*) – Specification of valid parameters and their type. May
          include nested argument specs.
        - **mutually_exclusive** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.11)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")*] or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.11)")*[*[*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.11)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")*]**]*) – List or list of lists of terms that should not
          be provided together.
        - **required_together** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.11)")*[*[*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.11)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")*]**]*) – List of lists of terms that are required together.
        - **required_one_of** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.11)")*[*[*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.11)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")*]**]*) – List of lists of terms, one of which in each list
          is required.
        - **required_if** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.11)")) – List of lists of `[parameter, value, [parameters]]` where
          one of `[parameters]` is required if `parameter == value`.
        - **required_by** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.11)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")*,* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.11)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")*]**]*) – Dictionary of parameter names that contain a list of
          parameters required by each key in the dictionary.

    validate(*parameters*, *\*args*, *\*\*kwargs*)
    :   Validate `parameters` against argument spec.

        Error messages in the [`ValidationResult`](module_utils.md#ansible.module_utils.common.arg_spec.ValidationResult "ansible.module_utils.common.arg_spec.ValidationResult") may contain no_log values and should be
        sanitized with [`sanitize_keys()`](module_utils.md#ansible.module_utils.common.parameters.sanitize_keys "ansible.module_utils.common.parameters.sanitize_keys") before logging or displaying.

        Parameters:
        :   **parameters** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.11)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")*,* [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.11)")*]*) – Parameters to validate against the argument spec

        Returns:
        :   [`ValidationResult`](module_utils.md#ansible.module_utils.common.arg_spec.ValidationResult "ansible.module_utils.common.arg_spec.ValidationResult") containing validated parameters.

        Simple Example:
        :   ```
            argument_spec = {
                'name': {'type': 'str'},
                'age': {'type': 'int'},
            }

            parameters = {
                'name': 'bo',
                'age': '42',
            }

            validator = ArgumentSpecValidator(argument_spec)
            result = validator.validate(parameters)

            if result.error_messages:
                sys.exit("Validation failed: {0}".format(", ".join(result.error_messages))

            valid_params = result.validated_parameters
            ```

### ValidationResult

*class* ansible.module_utils.common.arg_spec.ValidationResult(*parameters*)
:   Result of argument spec validation.

    This is the object returned by [`ArgumentSpecValidator.validate()`](module_utils.md#ansible.module_utils.common.arg_spec.ArgumentSpecValidator.validate "ansible.module_utils.common.arg_spec.ArgumentSpecValidator.validate")
    containing the validated parameters and any errors.

    Parameters:
    :   **parameters** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.11)")) – Terms to be validated and coerced to the correct type.

    errors
    :   [`AnsibleValidationErrorMultiple`](module_utils.md#ansible.module_utils.errors.AnsibleValidationErrorMultiple "ansible.module_utils.errors.AnsibleValidationErrorMultiple") containing all
        [`AnsibleValidationError`](module_utils.md#ansible.module_utils.errors.AnsibleValidationError "ansible.module_utils.errors.AnsibleValidationError") objects if there were
        any failures during validation.

    *property* validated_parameters
    :   Validated and coerced parameters.

    *property* unsupported_parameters
    :   [`set`](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.11)") of unsupported parameter names.

    *property* error_messages
    :   [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.11)") of all error messages from each exception in [`errors`](module_utils.md#ansible.module_utils.common.arg_spec.ValidationResult.errors "ansible.module_utils.common.arg_spec.ValidationResult.errors").

### Parameters

ansible.module_utils.common.parameters.DEFAULT_TYPE_VALIDATORS
:   [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.11)") of type names, such as `'str'`, and the default function
    used to check that type, [`check_type_str()`](module_utils.md#ansible.module_utils.common.validation.check_type_str "ansible.module_utils.common.validation.check_type_str") in this case.

ansible.module_utils.common.parameters.env_fallback(*\*args*, *\*\*kwargs*)
:   Load value from environment variable

ansible.module_utils.common.parameters.remove_values(*value*, *no_log_strings*)
:   Remove strings in `no_log_strings` from value.

    If value is a container type, then remove a lot more.

    Use of `deferred_removals` exists, rather than a pure recursive solution,
    because of the potential to hit the maximum recursion depth when dealing with
    large amounts of data (see [issue #24560](https://github.com/ansible/ansible/issues/24560)).

ansible.module_utils.common.parameters.sanitize_keys(*obj*, *no_log_strings*, *ignore_keys=frozenset({})*)
:   Sanitize the keys in a container object by removing `no_log` values from key names.

    This is a companion function to the [`remove_values()`](module_utils.md#ansible.module_utils.common.parameters.remove_values "ansible.module_utils.common.parameters.remove_values") function. Similar to that function,
    we make use of `deferred_removals` to avoid hitting maximum recursion depth in cases of
    large data structures.

    Parameters:
    :   - **obj** – The container object to sanitize. Non-container objects are returned unmodified.
        - **no_log_strings** – A set of string values we do not want logged.
        - **ignore_keys** – A set of string values of keys to not sanitize.

    Returns:
    :   An object with sanitized keys.

### Validation

Standalone functions for validating various parameter types.

ansible.module_utils.common.validation.check_missing_parameters(*parameters*, *required_parameters=None*)
:   This is for checking for required params when we can not check via
    argspec because we need more information than is simply given in the argspec.

    Raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.11)") if any required parameters are missing

    Parameters:
    :   - **parameters** – Dictionary of parameters
        - **required_parameters** – List of parameters to look for in the given parameters.

    Returns:
    :   Empty list or raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.11)") if the check fails.

ansible.module_utils.common.validation.check_mutually_exclusive(*terms*, *parameters*, *options_context=None*)
:   Check mutually exclusive terms against argument parameters

    Accepts a single list or list of lists that are groups of terms that should be
    mutually exclusive with one another

    Parameters:
    :   - **terms** – List of mutually exclusive parameters
        - **parameters** – Dictionary of parameters
        - **options_context** – List of strings of parent key names if `terms` are
          in a sub spec.

    Returns:
    :   Empty list or raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.11)") if the check fails.

ansible.module_utils.common.validation.check_required_arguments(*argument_spec*, *parameters*, *options_context=None*)
:   Check all parameters in argument_spec and return a list of parameters
    that are required but not present in parameters.

    Raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.11)") if the check fails

    Parameters:
    :   - **argument_spec** – Argument spec dictionary containing all parameters
          and their specification
        - **parameters** – Dictionary of parameters
        - **options_context** – List of strings of parent key names if `argument_spec` are
          in a sub spec.

    Returns:
    :   Empty list or raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.11)") if the check fails.

ansible.module_utils.common.validation.check_required_by(*requirements*, *parameters*, *options_context=None*)
:   For each key in requirements, check the corresponding list to see if they
    exist in parameters.

    Accepts a single string or list of values for each key.

    Parameters:
    :   - **requirements** – Dictionary of requirements
        - **parameters** – Dictionary of parameters
        - **options_context** – List of strings of parent key names if `requirements` are
          in a sub spec.

    Returns:
    :   Empty dictionary or raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.11)") if the

ansible.module_utils.common.validation.check_required_if(*requirements*, *parameters*, *options_context=None*)
:   Check parameters that are conditionally required

    Raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.11)") if the check fails

    Parameters:
    :   **requirements** – List of lists specifying a parameter, value, parameters
        required when the given parameter is the specified value, and optionally
        a boolean indicating any or all parameters are required.

    Example:

    ```python
    required_if=[
        ['state', 'present', ('path',), True],
        ['someint', 99, ('bool_param', 'string_param')],
    ]
    ```

    Parameters:
    :   - **parameters** – Dictionary of parameters
        - **options_context** – List of strings of parent key names if `requirements` are
          in a sub spec.

    Returns:
    :   Empty list or raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.11)") if the check fails.
        The results attribute of the exception contains a list of dictionaries.
        Each dictionary is the result of evaluating each item in requirements.
        Each return dictionary contains the following keys:

        > key missing:
        > :   List of parameters that are required but missing
        >
        > key requires:
        > :   ’any’ or ‘all’
        >
        > key parameter:
        > :   Parameter name that has the requirement
        >
        > key value:
        > :   Original value of the parameter
        >
        > key requirements:
        > :   Original required parameters

        Example:

        ```python
        [
            {
                'parameter': 'someint',
                'value': 99
                'requirements': ('bool_param', 'string_param'),
                'missing': ['string_param'],
                'requires': 'all',
            }
        ]
        ```

ansible.module_utils.common.validation.check_required_one_of(*terms*, *parameters*, *options_context=None*)
:   Check each list of terms to ensure at least one exists in the given module
    parameters

    Accepts a list of lists or tuples

    Parameters:
    :   - **terms** – List of lists of terms to check. For each list of terms, at
          least one is required.
        - **parameters** – Dictionary of parameters
        - **options_context** – List of strings of parent key names if `terms` are
          in a sub spec.

    Returns:
    :   Empty list or raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.11)") if the check fails.

ansible.module_utils.common.validation.check_required_together(*terms*, *parameters*, *options_context=None*)
:   Check each list of terms to ensure every parameter in each list exists
    in the given parameters.

    Accepts a list of lists or tuples.

    Parameters:
    :   - **terms** – List of lists of terms to check. Each list should include
          parameters that are all required when at least one is specified
          in the parameters.
        - **parameters** – Dictionary of parameters
        - **options_context** – List of strings of parent key names if `terms` are
          in a sub spec.

    Returns:
    :   Empty list or raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.11)") if the check fails.

ansible.module_utils.common.validation.check_type_bits(*value*)
:   Convert a human-readable string bits value to bits in integer.

    Example: `check_type_bits('1Mb')` returns integer 1048576.

    Raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.11)") if unable to covert the value.

ansible.module_utils.common.validation.check_type_bool(*value*)
:   Verify that the value is a bool or convert it to a bool and return it.

    Raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.11)") if unable to convert to a bool

    Parameters:
    :   **value** – String, int, or float to convert to bool. Valid booleans include:
        ‘1’, ‘on’, 1, ‘0’, 0, ‘n’, ‘f’, ‘false’, ‘true’, ‘y’, ‘t’, ‘yes’, ‘no’, ‘off’

    Returns:
    :   Boolean True or False

ansible.module_utils.common.validation.check_type_bytes(*value*)
:   Convert a human-readable string value to bytes

    Raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.11)") if unable to covert the value

ansible.module_utils.common.validation.check_type_dict(*value*)
:   Verify that value is a dict or convert it to a dict and return it.

    Raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.11)") if unable to convert to a dict

    Parameters:
    :   **value** – Dict or string to convert to a dict. Accepts `k1=v2, k2=v2`.

    Returns:
    :   value converted to a dictionary

ansible.module_utils.common.validation.check_type_float(*value*)
:   Verify that value is a float or convert it to a float and return it

    Raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.11)") if unable to convert to a float

    Parameters:
    :   **value** – float, int, str, or bytes to verify or convert and return.

    Returns:
    :   float of given value.

ansible.module_utils.common.validation.check_type_int(*value*)
:   Verify that the value is an integer and return it or convert the value
    to an integer and return it

    Raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.11)") if unable to convert to an int

    Parameters:
    :   **value** – String or int to convert of verify

    Returns:
    :   int of given value

ansible.module_utils.common.validation.check_type_jsonarg(*value*)
:   Return a jsonified string. Sometimes the controller turns a json string
    into a dict/list so transform it back into json here

    Raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.11)") if unable to covert the value

ansible.module_utils.common.validation.check_type_list(*value*)
:   Verify that the value is a list or convert to a list

    A comma separated string will be split into a list. Raises a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.11)")
    if unable to convert to a list.

    Parameters:
    :   **value** – Value to validate or convert to a list

    Returns:
    :   Original value if it is already a list, single item list if a
        float, int, or string without commas, or a multi-item list if a
        comma-delimited string.

ansible.module_utils.common.validation.check_type_path(*value*)
:   Verify the provided value is a string or convert it to a string,
    then return the expanded path

ansible.module_utils.common.validation.check_type_raw(*value*)
:   Returns the raw value

ansible.module_utils.common.validation.check_type_str(*value*, *allow_conversion=True*, *param=None*, *prefix=''*)
:   Verify that the value is a string or convert to a string.

    Since unexpected changes can sometimes happen when converting to a string,
    `allow_conversion` controls whether or not the value will be converted or a
    TypeError will be raised if the value is not a string and would be converted

    Parameters:
    :   - **value** – Value to validate or convert to a string
        - **allow_conversion** – Whether to convert the string and return it or raise
          a TypeError

    Returns:
    :   Original value if it is a string, the value converted to a string
        if allow_conversion=True, or raises a TypeError if allow_conversion=False.

ansible.module_utils.common.validation.count_terms(*terms*, *parameters*)
:   Count the number of occurrences of a key in a given dictionary

    Parameters:
    :   - **terms** – String or iterable of values to check
        - **parameters** – Dictionary of parameters

    Returns:
    :   An integer that is the number of occurrences of the terms values
        in the provided dictionary.

## Errors

*exception* ansible.module_utils.errors.AnsibleFallbackNotFound
:   Fallback validator was not found

*exception* ansible.module_utils.errors.AnsibleValidationError(*message*)
:   Single argument spec validation error

    error_message
    :   The error message passed in when the exception was raised.

    *property* msg
    :   The error message passed in when the exception was raised.

*exception* ansible.module_utils.errors.AnsibleValidationErrorMultiple(*errors=None*)
:   Multiple argument spec validation errors

    errors
    :   [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.11)") of [`AnsibleValidationError`](module_utils.md#ansible.module_utils.errors.AnsibleValidationError "ansible.module_utils.errors.AnsibleValidationError") objects

    *property* msg
    :   The first message from the first error in `errors`.

    *property* messages
    :   [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.11)") of each error message in `errors`.

    append(*error*)
    :   Append a new error to `self.errors`.

        Only [`AnsibleValidationError`](module_utils.md#ansible.module_utils.errors.AnsibleValidationError "ansible.module_utils.errors.AnsibleValidationError") should be added.

    extend(*errors*)
    :   Append each item in `errors` to `self.errors`. Only [`AnsibleValidationError`](module_utils.md#ansible.module_utils.errors.AnsibleValidationError "ansible.module_utils.errors.AnsibleValidationError") should be added.

*exception* ansible.module_utils.errors.AliasError(*message*)
:   Error handling aliases

*exception* ansible.module_utils.errors.ArgumentTypeError(*message*)
:   Error with parameter type

*exception* ansible.module_utils.errors.ArgumentValueError(*message*)
:   Error with parameter value

*exception* ansible.module_utils.errors.ElementError(*message*)
:   Error when validating elements

*exception* ansible.module_utils.errors.MutuallyExclusiveError(*message*)
:   Mutually exclusive parameters were supplied

*exception* ansible.module_utils.errors.NoLogError(*message*)
:   Error converting no_log values

*exception* ansible.module_utils.errors.RequiredByError(*message*)
:   Error with parameters that are required by other parameters

*exception* ansible.module_utils.errors.RequiredDefaultError(*message*)
:   A required parameter was assigned a default value

*exception* ansible.module_utils.errors.RequiredError(*message*)
:   Missing a required parameter

*exception* ansible.module_utils.errors.RequiredIfError(*message*)
:   Error with conditionally required parameters

*exception* ansible.module_utils.errors.RequiredOneOfError(*message*)
:   Error with parameters where at least one is required

*exception* ansible.module_utils.errors.RequiredTogetherError(*message*)
:   Error with parameters that are required together

*exception* ansible.module_utils.errors.SubParameterTypeError(*message*)
:   Incorrect type for subparameter

*exception* ansible.module_utils.errors.UnsupportedError(*message*)
:   Unsupported parameters were supplied
