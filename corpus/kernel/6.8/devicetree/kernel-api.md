---
collection: kernel
version: "6.8"
title: "DeviceTree Kernel API"
source_url: https://www.kernel.org/doc/html/v6.8/devicetree/kernel-api.html
fetched_at: 2026-08-21T03:35:47+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/devicetree/kernel-api.md)

# DeviceTree Kernel API

## Core functions

struct device_node \*of_find_all_nodes(struct device_node \*prev)
:   Get next node in global list

**Parameters**

`struct device_node *prev`
:   Previous node or NULL to start iteration
    [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") will be called on it

**Return**

A node pointer with refcount incremented, use
[`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on it when done.

int of_machine_is_compatible(const char \*compat)
:   Test root of device tree for a given compatible value

**Parameters**

`const char *compat`
:   compatible string to look for in root node's compatible property.

**Return**

A positive integer if the root node has the given value in its
compatible property.

bool of_device_is_available(const struct device_node \*device)
:   check if a device is available for use

**Parameters**

`const struct device_node *device`
:   Node to check for availability

**Return**

True if the status property is absent or set to "okay" or "ok",
:   false otherwise

bool of_device_is_big_endian(const struct device_node \*device)
:   check if a device has BE registers

**Parameters**

`const struct device_node *device`
:   Node to check for endianness

**Return**

True if the device has a "big-endian" property, or if the kernel
:   was compiled for BE *and* the device has a "native-endian" property.
    Returns false otherwise.

    Callers would nominally use ioread32be/iowrite32be if
    [`of_device_is_big_endian()`](kernel-api.md#c.of_device_is_big_endian "of_device_is_big_endian") == true, or readl/writel otherwise.

struct device_node \*of_get_parent(const struct device_node \*node)
:   Get a node's parent if any

**Parameters**

`const struct device_node *node`
:   Node to get parent

**Return**

A node pointer with refcount incremented, use
[`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on it when done.

struct device_node \*of_get_next_parent(struct device_node \*node)
:   Iterate to a node's parent

**Parameters**

`struct device_node *node`
:   Node to get parent of

**Description**

This is like [`of_get_parent()`](kernel-api.md#c.of_get_parent "of_get_parent") except that it drops the
refcount on the passed node, making it suitable for iterating
through a node's parents.

**Return**

A node pointer with refcount incremented, use
[`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on it when done.

struct device_node \*of_get_next_child(const struct device_node \*node, struct device_node \*prev)
:   Iterate a node childs

**Parameters**

`const struct device_node *node`
:   parent node

`struct device_node *prev`
:   previous child of the parent node, or NULL to get first

**Return**

A node pointer with refcount incremented, use [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on
it when done. Returns NULL when prev is the last child. Decrements the
refcount of prev.

struct device_node \*of_get_next_available_child(const struct device_node \*node, struct device_node \*prev)
:   Find the next available child node

**Parameters**

`const struct device_node *node`
:   parent node

`struct device_node *prev`
:   previous child of the parent node, or NULL to get first

**Description**

This function is like [`of_get_next_child()`](kernel-api.md#c.of_get_next_child "of_get_next_child"), except that it
automatically skips any disabled nodes (i.e. status = "disabled").

struct device_node \*of_get_next_cpu_node(struct device_node \*prev)
:   Iterate on cpu nodes

**Parameters**

`struct device_node *prev`
:   previous child of the /cpus node, or NULL to get first

**Description**

Unusable CPUs (those with the status property set to "fail" or "fail-...")
will be skipped.

**Return**

A cpu node pointer with refcount incremented, use [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put")
on it when done. Returns NULL when prev is the last child. Decrements
the refcount of prev.

struct device_node \*of_get_compatible_child(const struct device_node \*parent, const char \*compatible)
:   Find compatible child node

**Parameters**

`const struct device_node *parent`
:   parent node

`const char *compatible`
:   compatible string

**Description**

Lookup child node whose compatible property contains the given compatible
string.

**Return**

a node pointer with refcount incremented, use [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on it
when done; or NULL if not found.

struct device_node \*of_get_child_by_name(const struct device_node \*node, const char \*name)
:   Find the child node by name for a given parent

**Parameters**

`const struct device_node *node`
:   parent node

`const char *name`
:   child name to look for.

**Description**

This function looks for child node for given matching name

**Return**

A node pointer if found, with refcount incremented, use
[`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on it when done.
Returns NULL if node is not found.

struct device_node \*of_find_node_opts_by_path(const char \*path, const char \*\*opts)
:   Find a node matching a full OF path

**Parameters**

`const char *path`
:   Either the full path to match, or if the path does not
    start with '/', the name of a property of the /aliases
    node (an alias). In the case of an alias, the node
    matching the alias' value will be returned.

`const char **opts`
:   Address of a pointer into which to store the start of
    an options string appended to the end of the path with
    a ':' separator.

**Description**

Valid paths:
:   - /foo/bar Full path
    - foo Valid alias
    - foo/bar Valid alias + relative path

**Return**

A node pointer with refcount incremented, use
[`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on it when done.

struct device_node \*of_find_node_by_name(struct device_node \*from, const char \*name)
:   Find a node by its "name" property

**Parameters**

`struct device_node *from`
:   The node to start searching from or NULL; the node
    you pass will not be searched, only the next one
    will. Typically, you pass what the previous call
    returned. [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") will be called on **from**.

`const char *name`
:   The name string to match against

**Return**

A node pointer with refcount incremented, use
[`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on it when done.

struct device_node \*of_find_node_by_type(struct device_node \*from, const char \*type)
:   Find a node by its "device_type" property

**Parameters**

`struct device_node *from`
:   The node to start searching from, or NULL to start searching
    the entire device tree. The node you pass will not be
    searched, only the next one will; typically, you pass
    what the previous call returned. [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") will be
    called on from for you.

`const char *type`
:   The type string to match against

**Return**

A node pointer with refcount incremented, use
[`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on it when done.

struct device_node \*of_find_compatible_node(struct device_node \*from, const char \*type, const char \*compatible)
:   Find a node based on type and one of the tokens in its "compatible" property

**Parameters**

`struct device_node *from`
:   The node to start searching from or NULL, the node
    you pass will not be searched, only the next one
    will; typically, you pass what the previous call
    returned. [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") will be called on it

`const char *type`
:   The type string to match "device_type" or NULL to ignore

`const char *compatible`
:   The string to match to one of the tokens in the device
    "compatible" list.

**Return**

A node pointer with refcount incremented, use
[`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on it when done.

struct device_node \*of_find_node_with_property(struct device_node \*from, const char \*prop_name)
:   Find a node which has a property with the given name.

**Parameters**

`struct device_node *from`
:   The node to start searching from or NULL, the node
    you pass will not be searched, only the next one
    will; typically, you pass what the previous call
    returned. [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") will be called on it

`const char *prop_name`
:   The name of the property to look for.

**Return**

A node pointer with refcount incremented, use
[`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on it when done.

const struct of_device_id \*of_match_node(const struct of_device_id \*matches, const struct device_node \*node)
:   Tell if a device_node has a matching of_match structure

**Parameters**

`const struct of_device_id *matches`
:   array of of device match structures to search in

`const struct device_node *node`
:   the of device structure to match against

**Description**

Low level utility function used by device matching.

struct device_node \*of_find_matching_node_and_match(struct device_node \*from, const struct of_device_id \*matches, const struct of_device_id \*\*match)
:   Find a node based on an of_device_id match table.

**Parameters**

`struct device_node *from`
:   The node to start searching from or NULL, the node
    you pass will not be searched, only the next one
    will; typically, you pass what the previous call
    returned. [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") will be called on it

`const struct of_device_id *matches`
:   array of of device match structures to search in

`const struct of_device_id **match`
:   Updated to point at the matches entry which matched

**Return**

A node pointer with refcount incremented, use
[`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on it when done.

int of_alias_from_compatible(const struct device_node \*node, char \*alias, int len)
:   Lookup appropriate alias for a device node depending on compatible

**Parameters**

`const struct device_node *node`
:   pointer to a device tree node

`char *alias`
:   Pointer to buffer that alias value will be copied into

`int len`
:   Length of alias value

**Description**

Based on the value of the compatible property, this routine will attempt
to choose an appropriate alias value for a particular device tree node.
It does this by stripping the manufacturer prefix (as delimited by a ',')
from the first entry in the compatible list property.

**Note**

The matching on just the "product" side of the compatible is a relic
from I2C and SPI. Please do not add any new user.

**Return**

This routine returns 0 on success, <0 on failure.

struct device_node \*of_find_node_by_phandle(phandle handle)
:   Find a node given a phandle

**Parameters**

`phandle handle`
:   phandle of the node to find

**Return**

A node pointer with refcount incremented, use
[`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on it when done.

int of_parse_phandle_with_args_map(const struct device_node \*np, const char \*list_name, const char \*stem_name, int index, struct of_phandle_args \*out_args)
:   Find a node pointed by phandle in a list and remap it

**Parameters**

`const struct device_node *np`
:   pointer to a device tree node containing a list

`const char *list_name`
:   property name that contains a list

`const char *stem_name`
:   stem of property names that specify phandles' arguments count

`int index`
:   index of a phandle to parse out

`struct of_phandle_args *out_args`
:   optional pointer to output arguments structure (will be filled)

**Description**

This function is useful to parse lists of phandles and their arguments.
Returns 0 on success and fills out_args, on error returns appropriate errno
value. The difference between this function and [`of_parse_phandle_with_args()`](kernel-api.md#c.of_parse_phandle_with_args "of_parse_phandle_with_args")
is that this API remaps a phandle if the node the phandle points to has
a <**stem_name**>-map property.

Caller is responsible to call [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on the returned out_args->np
pointer.

Example:

```
phandle1: node1 {
    #list-cells = <2>;
};

phandle2: node2 {
    #list-cells = <1>;
};

phandle3: node3 {
    #list-cells = <1>;
    list-map = <0 &phandle2 3>,
               <1 &phandle2 2>,
               <2 &phandle1 5 1>;
    list-map-mask = <0x3>;
};

node4 {
    list = <&phandle1 1 2 &phandle3 0>;
};
```

To get a device_node of the `node2` node you may call this:
of_parse_phandle_with_args(node4, "list", "list", 1, `args`);

int of_count_phandle_with_args(const struct device_node \*np, const char \*list_name, const char \*cells_name)
:   Find the number of phandles references in a property

**Parameters**

`const struct device_node *np`
:   pointer to a device tree node containing a list

`const char *list_name`
:   property name that contains a list

`const char *cells_name`
:   property name that specifies phandles' arguments count

**Return**

The number of phandle + argument tuples within a property. It
is a typical pattern to encode a list of phandle and variable
arguments into a single property. The number of arguments is encoded
by a property in the phandle-target node. For example, a gpios
property would contain a list of GPIO specifies consisting of a
phandle and 1 or more arguments. The number of arguments are
determined by the #gpio-cells property in the node pointed to by the
phandle.

int of_add_property(struct device_node \*np, struct property \*prop)
:   Add a property to a node

**Parameters**

`struct device_node *np`
:   Caller's Device Node

`struct property *prop`
:   Property to add

int of_remove_property(struct device_node \*np, struct property \*prop)
:   Remove a property from a node.

**Parameters**

`struct device_node *np`
:   Caller's Device Node

`struct property *prop`
:   Property to remove

**Description**

Note that we don't actually remove it, since we have given out
who-knows-how-many pointers to the data using get-property.
Instead we just move the property to the "dead properties"
list, so it won't be found any more.

int of_alias_get_id(struct device_node \*np, const char \*stem)
:   Get alias id for the given device_node

**Parameters**

`struct device_node *np`
:   Pointer to the given device_node

`const char *stem`
:   Alias stem of the given device_node

**Description**

The function travels the lookup table to get the alias id for the given
device_node and alias stem.

**Return**

The alias id if found.

int of_alias_get_highest_id(const char \*stem)
:   Get highest alias id for the given stem

**Parameters**

`const char *stem`
:   Alias stem to be examined

**Description**

The function travels the lookup table to get the highest alias id for the
given alias stem. It returns the alias id if found.

bool of_console_check(struct device_node \*dn, char \*name, int index)
:   Test and setup console for DT setup

**Parameters**

`struct device_node *dn`
:   Pointer to device node

`char *name`
:   Name to use for preferred console without index. ex. "ttyS"

`int index`
:   Index to use for preferred console.

**Description**

Check if the given device node matches the stdout-path property in the
/chosen node. If it does then register it as the preferred console.

**Return**

TRUE if console successfully setup. Otherwise return FALSE.

int of_map_id(struct device_node \*np, u32 id, const char \*map_name, const char \*map_mask_name, struct device_node \*\*target, u32 \*id_out)
:   Translate an ID through a downstream mapping.

**Parameters**

`struct device_node *np`
:   root complex device node.

`u32 id`
:   device ID to map.

`const char *map_name`
:   property name of the map to use.

`const char *map_mask_name`
:   optional property name of the mask to use.

`struct device_node **target`
:   optional pointer to a target device node.

`u32 *id_out`
:   optional pointer to receive the translated ID.

**Description**

Given a device ID, look up the appropriate implementation-defined
platform ID and/or the target device which receives transactions on that
ID, as per the "iommu-map" and "msi-map" bindings. Either of **target** or
**id_out** may be NULL if only the other is required. If **target** points to
a non-NULL device node pointer, only entries targeting that node will be
matched; if it points to a NULL value, it will receive the device node of
the first matching target phandle, with a reference held.

**Return**

0 on success or a standard error code on failure.

void of_node_init(struct device_node \*node)
:   initialize a devicetree node

**Parameters**

`struct device_node *node`
:   Pointer to device node that has been created by [`kzalloc()`](../core-api/mm-api.md#c.kzalloc "kzalloc")

**Description**

On return the device_node refcount is set to one. Use [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put")
on **node** when done to free the memory allocated for it. If the node
is NOT a dynamic node the memory will not be freed. The decision of
whether to free the memory will be done by node->release(), which is
of_node_release().

struct device_node \*of_parse_phandle(const struct device_node \*np, const char \*phandle_name, int index)
:   Resolve a phandle property to a device_node pointer

**Parameters**

`const struct device_node *np`
:   Pointer to device node holding phandle property

`const char *phandle_name`
:   Name of property holding a phandle value

`int index`
:   For properties holding a table of phandles, this is the index into
    the table

**Return**

The device_node pointer with refcount incremented. Use
[`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on it when done.

int of_parse_phandle_with_args(const struct device_node \*np, const char \*list_name, const char \*cells_name, int index, struct of_phandle_args \*out_args)
:   Find a node pointed by phandle in a list

**Parameters**

`const struct device_node *np`
:   pointer to a device tree node containing a list

`const char *list_name`
:   property name that contains a list

`const char *cells_name`
:   property name that specifies phandles' arguments count

`int index`
:   index of a phandle to parse out

`struct of_phandle_args *out_args`
:   optional pointer to output arguments structure (will be filled)

**Description**

This function is useful to parse lists of phandles and their arguments.
Returns 0 on success and fills out_args, on error returns appropriate
errno value.

Caller is responsible to call [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on the returned out_args->np
pointer.

Example:

```
phandle1: node1 {
    #list-cells = <2>;
};

phandle2: node2 {
    #list-cells = <1>;
};

node3 {
    list = <&phandle1 1 2 &phandle2 3>;
};
```

To get a device_node of the `node2` node you may call this:
of_parse_phandle_with_args(node3, "list", "#list-cells", 1, `args`);

int of_parse_phandle_with_fixed_args(const struct device_node \*np, const char \*list_name, int cell_count, int index, struct of_phandle_args \*out_args)
:   Find a node pointed by phandle in a list

**Parameters**

`const struct device_node *np`
:   pointer to a device tree node containing a list

`const char *list_name`
:   property name that contains a list

`int cell_count`
:   number of argument cells following the phandle

`int index`
:   index of a phandle to parse out

`struct of_phandle_args *out_args`
:   optional pointer to output arguments structure (will be filled)

**Description**

This function is useful to parse lists of phandles and their arguments.
Returns 0 on success and fills out_args, on error returns appropriate
errno value.

Caller is responsible to call [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on the returned out_args->np
pointer.

Example:

```
phandle1: node1 {
};

phandle2: node2 {
};

node3 {
    list = <&phandle1 0 2 &phandle2 2 3>;
};
```

To get a device_node of the `node2` node you may call this:
of_parse_phandle_with_fixed_args(node3, "list", 2, 1, `args`);

int of_parse_phandle_with_optional_args(const struct device_node \*np, const char \*list_name, const char \*cells_name, int index, struct of_phandle_args \*out_args)
:   Find a node pointed by phandle in a list

**Parameters**

`const struct device_node *np`
:   pointer to a device tree node containing a list

`const char *list_name`
:   property name that contains a list

`const char *cells_name`
:   property name that specifies phandles' arguments count

`int index`
:   index of a phandle to parse out

`struct of_phandle_args *out_args`
:   optional pointer to output arguments structure (will be filled)

**Description**

Same as [`of_parse_phandle_with_args()`](kernel-api.md#c.of_parse_phandle_with_args "of_parse_phandle_with_args") except that if the cells_name property
is not found, cell_count of 0 is assumed.

This is used to useful, if you have a phandle which didn't have arguments
before and thus doesn't have a '#\*-cells' property but is now migrated to
having arguments while retaining backwards compatibility.

int of_property_count_u8_elems(const struct device_node \*np, const char \*propname)
:   Count the number of u8 elements in a property

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

**Description**

Search for a property in a device node and count the number of u8 elements
in it.

**Return**

The number of elements on sucess, -EINVAL if the property does
not exist or its length does not match a multiple of u8 and -ENODATA if the
property does not have a value.

int of_property_count_u16_elems(const struct device_node \*np, const char \*propname)
:   Count the number of u16 elements in a property

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

**Description**

Search for a property in a device node and count the number of u16 elements
in it.

**Return**

The number of elements on sucess, -EINVAL if the property does
not exist or its length does not match a multiple of u16 and -ENODATA if the
property does not have a value.

int of_property_count_u32_elems(const struct device_node \*np, const char \*propname)
:   Count the number of u32 elements in a property

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

**Description**

Search for a property in a device node and count the number of u32 elements
in it.

**Return**

The number of elements on sucess, -EINVAL if the property does
not exist or its length does not match a multiple of u32 and -ENODATA if the
property does not have a value.

int of_property_count_u64_elems(const struct device_node \*np, const char \*propname)
:   Count the number of u64 elements in a property

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

**Description**

Search for a property in a device node and count the number of u64 elements
in it.

**Return**

The number of elements on sucess, -EINVAL if the property does
not exist or its length does not match a multiple of u64 and -ENODATA if the
property does not have a value.

int of_property_read_string_array(const struct device_node \*np, const char \*propname, const char \*\*out_strs, size_t sz)
:   Read an array of strings from a multiple strings property.

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

`const char **out_strs`
:   output array of string pointers.

`size_t sz`
:   number of array elements to read.

**Description**

Search for a property in a device tree node and retrieve a list of
terminated string values (pointer to data, not a copy) in that property.

**Return**

If **out_strs** is NULL, the number of strings in the property is returned.

int of_property_count_strings(const struct device_node \*np, const char \*propname)
:   Find and return the number of strings from a multiple strings property.

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

**Description**

Search for a property in a device tree node and retrieve the number of null
terminated string contain in it.

**Return**

The number of strings on success, -EINVAL if the property does not
exist, -ENODATA if property does not have a value, and -EILSEQ if the string
is not null-terminated within the length of the property data.

int of_property_read_string_index(const struct device_node \*np, const char \*propname, int index, const char \*\*output)
:   Find and read a string from a multiple strings property.

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

`int index`
:   index of the string in the list of strings

`const char **output`
:   pointer to null terminated return string, modified only if
    return value is 0.

**Description**

Search for a property in a device tree node and retrieve a null
terminated string value (pointer to data, not a copy) in the list of strings
contained in that property.

The out_string pointer is modified only if a valid string can be decoded.

**Return**

0 on success, -EINVAL if the property does not exist, -ENODATA if
property does not have a value, and -EILSEQ if the string is not
null-terminated within the length of the property data.

bool of_property_read_bool(const struct device_node \*np, const char \*propname)
:   Find a property

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

**Description**

Search for a boolean property in a device node. Usage on non-boolean
property types is deprecated.

**Return**

true if the property exists false otherwise.

bool of_property_present(const struct device_node \*np, const char \*propname)
:   Test if a property is present in a node

**Parameters**

`const struct device_node *np`
:   device node to search for the property.

`const char *propname`
:   name of the property to be searched.

**Description**

Test for a property present in a device node.

**Return**

true if the property exists false otherwise.

int of_property_read_u8_array(const struct device_node \*np, const char \*propname, u8 \*out_values, size_t sz)
:   Find and read an array of u8 from a property.

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

`u8 *out_values`
:   pointer to return value, modified only if return value is 0.

`size_t sz`
:   number of array elements to read

**Description**

Search for a property in a device node and read 8-bit value(s) from
it.

dts entry of array should be like:
:   `property = /bits/ 8 <0x50 0x60 0x70>;`

The out_values is modified only if a valid u8 value can be decoded.

**Return**

0 on success, -EINVAL if the property does not exist,
-ENODATA if property does not have a value, and -EOVERFLOW if the
property data isn't large enough.

int of_property_read_u16_array(const struct device_node \*np, const char \*propname, u16 \*out_values, size_t sz)
:   Find and read an array of u16 from a property.

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

`u16 *out_values`
:   pointer to return value, modified only if return value is 0.

`size_t sz`
:   number of array elements to read

**Description**

Search for a property in a device node and read 16-bit value(s) from
it.

dts entry of array should be like:
:   `property = /bits/ 16 <0x5000 0x6000 0x7000>;`

The out_values is modified only if a valid u16 value can be decoded.

**Return**

0 on success, -EINVAL if the property does not exist,
-ENODATA if property does not have a value, and -EOVERFLOW if the
property data isn't large enough.

int of_property_read_u32_array(const struct device_node \*np, const char \*propname, u32 \*out_values, size_t sz)
:   Find and read an array of 32 bit integers from a property.

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

`u32 *out_values`
:   pointer to return value, modified only if return value is 0.

`size_t sz`
:   number of array elements to read

**Description**

Search for a property in a device node and read 32-bit value(s) from
it.

The out_values is modified only if a valid u32 value can be decoded.

**Return**

0 on success, -EINVAL if the property does not exist,
-ENODATA if property does not have a value, and -EOVERFLOW if the
property data isn't large enough.

int of_property_read_u64_array(const struct device_node \*np, const char \*propname, u64 \*out_values, size_t sz)
:   Find and read an array of 64 bit integers from a property.

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

`u64 *out_values`
:   pointer to return value, modified only if return value is 0.

`size_t sz`
:   number of array elements to read

**Description**

Search for a property in a device node and read 64-bit value(s) from
it.

The out_values is modified only if a valid u64 value can be decoded.

**Return**

0 on success, -EINVAL if the property does not exist,
-ENODATA if property does not have a value, and -EOVERFLOW if the
property data isn't large enough.

struct of_changeset_entry
:   Holds a changeset entry

**Definition**:

```
struct of_changeset_entry {
    struct list_head node;
    unsigned long action;
    struct device_node *np;
    struct property *prop;
    struct property *old_prop;
};
```

**Members**

`node`
:   list_head for the log list

`action`
:   notifier action

`np`
:   pointer to the device node affected

`prop`
:   pointer to the property affected

`old_prop`
:   hold a pointer to the original property

**Description**

Every modification of the device tree during a changeset
is held in a list of of_changeset_entry structures.
That way we can recover from a partial application, or we can
revert the changeset

struct of_changeset
:   changeset tracker structure

**Definition**:

```
struct of_changeset {
    struct list_head entries;
};
```

**Members**

`entries`
:   list_head for the changeset entries

**Description**

changesets are a convenient way to apply bulk changes to the
live tree. In case of an error, changes are rolled-back.
changesets live on after initial application, and if not
destroyed after use, they can be reverted in one single call.

bool of_device_is_system_power_controller(const struct device_node \*np)
:   Tells if system-power-controller is found for device_node

**Parameters**

`const struct device_node *np`
:   Pointer to the given device_node

**Return**

true if present false otherwise

bool of_graph_is_present(const struct device_node \*node)
:   check graph's presence

**Parameters**

`const struct device_node *node`
:   pointer to device_node containing graph port

**Return**

True if **node** has a port or ports (with a port) sub-node,
false otherwise.

int of_property_count_elems_of_size(const struct device_node \*np, const char \*propname, int elem_size)
:   Count the number of elements in a property

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

`int elem_size`
:   size of the individual element

**Description**

Search for a property in a device node and count the number of elements of
size elem_size in it.

**Return**

The number of elements on sucess, -EINVAL if the property does not
exist or its length does not match a multiple of elem_size and -ENODATA if
the property does not have a value.

int of_property_read_u32_index(const struct device_node \*np, const char \*propname, u32 index, u32 \*out_value)
:   Find and read a u32 from a multi-value property.

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

`u32 index`
:   index of the u32 in the list of values

`u32 *out_value`
:   pointer to return value, modified only if no error.

**Description**

Search for a property in a device node and read nth 32-bit value from
it.

The out_value is modified only if a valid u32 value can be decoded.

**Return**

0 on success, -EINVAL if the property does not exist,
-ENODATA if property does not have a value, and -EOVERFLOW if the
property data isn't large enough.

int of_property_read_u64_index(const struct device_node \*np, const char \*propname, u32 index, u64 \*out_value)
:   Find and read a u64 from a multi-value property.

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

`u32 index`
:   index of the u64 in the list of values

`u64 *out_value`
:   pointer to return value, modified only if no error.

**Description**

Search for a property in a device node and read nth 64-bit value from
it.

The out_value is modified only if a valid u64 value can be decoded.

**Return**

0 on success, -EINVAL if the property does not exist,
-ENODATA if property does not have a value, and -EOVERFLOW if the
property data isn't large enough.

int of_property_read_variable_u8_array(const struct device_node \*np, const char \*propname, u8 \*out_values, size_t sz_min, size_t sz_max)
:   Find and read an array of u8 from a property, with bounds on the minimum and maximum array size.

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

`u8 *out_values`
:   pointer to found values.

`size_t sz_min`
:   minimum number of array elements to read

`size_t sz_max`
:   maximum number of array elements to read, if zero there is no
    upper limit on the number of elements in the dts entry but only
    sz_min will be read.

**Description**

Search for a property in a device node and read 8-bit value(s) from
it.

dts entry of array should be like:
:   `property = /bits/ 8 <0x50 0x60 0x70>;`

The out_values is modified only if a valid u8 value can be decoded.

**Return**

The number of elements read on success, -EINVAL if the property
does not exist, -ENODATA if property does not have a value, and -EOVERFLOW
if the property data is smaller than sz_min or longer than sz_max.

int of_property_read_variable_u16_array(const struct device_node \*np, const char \*propname, u16 \*out_values, size_t sz_min, size_t sz_max)
:   Find and read an array of u16 from a property, with bounds on the minimum and maximum array size.

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

`u16 *out_values`
:   pointer to found values.

`size_t sz_min`
:   minimum number of array elements to read

`size_t sz_max`
:   maximum number of array elements to read, if zero there is no
    upper limit on the number of elements in the dts entry but only
    sz_min will be read.

**Description**

Search for a property in a device node and read 16-bit value(s) from
it.

dts entry of array should be like:
:   `property = /bits/ 16 <0x5000 0x6000 0x7000>;`

The out_values is modified only if a valid u16 value can be decoded.

**Return**

The number of elements read on success, -EINVAL if the property
does not exist, -ENODATA if property does not have a value, and -EOVERFLOW
if the property data is smaller than sz_min or longer than sz_max.

int of_property_read_variable_u32_array(const struct device_node \*np, const char \*propname, u32 \*out_values, size_t sz_min, size_t sz_max)
:   Find and read an array of 32 bit integers from a property, with bounds on the minimum and maximum array size.

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

`u32 *out_values`
:   pointer to return found values.

`size_t sz_min`
:   minimum number of array elements to read

`size_t sz_max`
:   maximum number of array elements to read, if zero there is no
    upper limit on the number of elements in the dts entry but only
    sz_min will be read.

**Description**

Search for a property in a device node and read 32-bit value(s) from
it.

The out_values is modified only if a valid u32 value can be decoded.

**Return**

The number of elements read on success, -EINVAL if the property
does not exist, -ENODATA if property does not have a value, and -EOVERFLOW
if the property data is smaller than sz_min or longer than sz_max.

int of_property_read_u64(const struct device_node \*np, const char \*propname, u64 \*out_value)
:   Find and read a 64 bit integer from a property

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

`u64 *out_value`
:   pointer to return value, modified only if return value is 0.

**Description**

Search for a property in a device node and read a 64-bit value from
it.

The out_value is modified only if a valid u64 value can be decoded.

**Return**

0 on success, -EINVAL if the property does not exist,
-ENODATA if property does not have a value, and -EOVERFLOW if the
property data isn't large enough.

int of_property_read_variable_u64_array(const struct device_node \*np, const char \*propname, u64 \*out_values, size_t sz_min, size_t sz_max)
:   Find and read an array of 64 bit integers from a property, with bounds on the minimum and maximum array size.

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

`u64 *out_values`
:   pointer to found values.

`size_t sz_min`
:   minimum number of array elements to read

`size_t sz_max`
:   maximum number of array elements to read, if zero there is no
    upper limit on the number of elements in the dts entry but only
    sz_min will be read.

**Description**

Search for a property in a device node and read 64-bit value(s) from
it.

The out_values is modified only if a valid u64 value can be decoded.

**Return**

The number of elements read on success, -EINVAL if the property
does not exist, -ENODATA if property does not have a value, and -EOVERFLOW
if the property data is smaller than sz_min or longer than sz_max.

int of_property_read_string(const struct device_node \*np, const char \*propname, const char \*\*out_string)
:   Find and read a string from a property

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

`const char **out_string`
:   pointer to null terminated return string, modified only if
    return value is 0.

**Description**

Search for a property in a device tree node and retrieve a null
terminated string value (pointer to data, not a copy).

Note that the empty string "" has length of 1, thus -ENODATA cannot
be interpreted as an empty string.

The out_string pointer is modified only if a valid string can be decoded.

**Return**

0 on success, -EINVAL if the property does not exist, -ENODATA if
property does not have a value, and -EILSEQ if the string is not
null-terminated within the length of the property data.

int of_property_match_string(const struct device_node \*np, const char \*propname, const char \*string)
:   Find string in a list and return index

**Parameters**

`const struct device_node *np`
:   pointer to node containing string list property

`const char *propname`
:   string list property name

`const char *string`
:   pointer to string to search for in string list

**Description**

This function searches a string list property and returns the index
of a specific string value.

int of_property_read_string_helper(const struct device_node \*np, const char \*propname, const char \*\*out_strs, size_t sz, int skip)
:   Utility helper for parsing string properties

**Parameters**

`const struct device_node *np`
:   device node from which the property value is to be read.

`const char *propname`
:   name of the property to be searched.

`const char **out_strs`
:   output array of string pointers.

`size_t sz`
:   number of array elements to read.

`int skip`
:   Number of strings to skip over at beginning of list.

**Description**

Don't call this function directly. It is a utility helper for the
of_property_read_string\*() family of functions.

int of_graph_parse_endpoint(const struct device_node \*node, struct [of_endpoint](kernel-api.md#c.of_endpoint "of_endpoint") \*endpoint)
:   parse common endpoint node properties

**Parameters**

`const struct device_node *node`
:   pointer to endpoint device_node

`struct of_endpoint *endpoint`
:   pointer to the OF endpoint data structure

**Description**

The caller should hold a reference to **node**.

struct device_node \*of_graph_get_port_by_id(struct device_node \*parent, u32 id)
:   get the port matching a given id

**Parameters**

`struct device_node *parent`
:   pointer to the parent device node

`u32 id`
:   id of the port

**Return**

A 'port' node pointer with refcount incremented. The caller
has to use [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on it when done.

struct device_node \*of_graph_get_next_endpoint(const struct device_node \*parent, struct device_node \*prev)
:   get next endpoint node

**Parameters**

`const struct device_node *parent`
:   pointer to the parent device node

`struct device_node *prev`
:   previous endpoint node, or NULL to get first

**Return**

An 'endpoint' node pointer with refcount incremented. Refcount
of the passed **prev** node is decremented.

struct device_node \*of_graph_get_endpoint_by_regs(const struct device_node \*parent, int port_reg, int reg)
:   get endpoint node of specific identifiers

**Parameters**

`const struct device_node *parent`
:   pointer to the parent device node

`int port_reg`
:   identifier (value of reg property) of the parent port node

`int reg`
:   identifier (value of reg property) of the endpoint node

**Return**

An 'endpoint' node pointer which is identified by reg and at the same
is the child of a port node identified by port_reg. reg and port_reg are
ignored when they are -1. Use [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on the pointer when done.

struct device_node \*of_graph_get_remote_endpoint(const struct device_node \*node)
:   get remote endpoint node

**Parameters**

`const struct device_node *node`
:   pointer to a local endpoint device_node

**Return**

Remote endpoint node associated with remote endpoint node linked
:   to **node**. Use [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on it when done.

struct device_node \*of_graph_get_port_parent(struct device_node \*node)
:   get port's parent node

**Parameters**

`struct device_node *node`
:   pointer to a local endpoint device_node

**Return**

device node associated with endpoint node linked
:   to **node**. Use [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on it when done.

struct device_node \*of_graph_get_remote_port_parent(const struct device_node \*node)
:   get remote port's parent node

**Parameters**

`const struct device_node *node`
:   pointer to a local endpoint device_node

**Return**

Remote device node associated with remote endpoint node linked
:   to **node**. Use [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on it when done.

struct device_node \*of_graph_get_remote_port(const struct device_node \*node)
:   get remote port node

**Parameters**

`const struct device_node *node`
:   pointer to a local endpoint device_node

**Return**

Remote port node associated with remote endpoint node linked
to **node**. Use [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on it when done.

struct device_node \*of_graph_get_remote_node(const struct device_node \*node, u32 port, u32 endpoint)
:   get remote parent device_node for given port/endpoint

**Parameters**

`const struct device_node *node`
:   pointer to parent device_node containing graph port/endpoint

`u32 port`
:   identifier (value of reg property) of the parent port node

`u32 endpoint`
:   identifier (value of reg property) of the endpoint node

**Return**

Remote device node associated with remote endpoint node linked
to **node**. Use [`of_node_put()`](kernel-api.md#c.of_node_put "of_node_put") on it when done.

struct of_endpoint
:   the OF graph endpoint data structure

**Definition**:

```
struct of_endpoint {
    unsigned int port;
    unsigned int id;
    const struct device_node *local_node;
};
```

**Members**

`port`
:   identifier (value of reg property) of a port this endpoint belongs to

`id`
:   identifier (value of reg property) of this endpoint

`local_node`
:   pointer to device_node of this endpoint

for_each_endpoint_of_node

`for_each_endpoint_of_node (parent, child)`

> iterate over every endpoint in a device node

**Parameters**

`parent`
:   parent device node containing ports and endpoints

`child`
:   loop variable pointing to the current endpoint node

**Description**

When breaking out of the loop, of_node_put(child) has to be called manually.

const __be32 \*of_translate_dma_region(struct device_node \*dev, const __be32 \*prop, phys_addr_t \*start, size_t \*length)
:   Translate device tree address and size tuple

**Parameters**

`struct device_node *dev`
:   device tree node for which to translate

`const __be32 *prop`
:   pointer into array of cells

`phys_addr_t *start`
:   return value for the start of the DMA range

`size_t *length`
:   return value for the length of the DMA range

**Description**

Returns a pointer to the cell immediately following the translated DMA region.

int of_property_read_reg(struct device_node \*np, int idx, u64 \*addr, u64 \*size)
:   Retrieve the specified "reg" entry index without translating

**Parameters**

`struct device_node *np`
:   device tree node for which to retrieve "reg" from

`int idx`
:   "reg" entry index to read

`u64 *addr`
:   return value for the untranslated address

`u64 *size`
:   return value for the entry size

**Description**

Returns -EINVAL if "reg" is not found. Returns 0 on success with addr and
size values filled in.

bool of_dma_is_coherent(struct device_node \*np)
:   Check if device is coherent

**Parameters**

`struct device_node *np`
:   device node

**Description**

It returns true if "dma-coherent" property was found
for this device in the DT, or if DMA is coherent by
default for OF devices on the current platform and no
"dma-noncoherent" property was found for this device.

int of_address_to_resource(struct device_node \*dev, int index, struct resource \*r)
:   Translate device tree address and return as resource

**Parameters**

`struct device_node *dev`
:   Caller's Device Node

`int index`
:   Index into the array

`struct resource *r`
:   Pointer to resource array

**Description**

Returns -EINVAL if the range cannot be converted to resource.

Note that if your address is a PIO address, the conversion will fail if
the physical address can't be internally converted to an IO token with
pci_address_to_pio(), that is because it's either called too early or it
can't be matched to any host bridge IO space

void __iomem \*of_iomap(struct device_node \*np, int index)
:   Maps the memory mapped IO for a given device_node

**Parameters**

`struct device_node *np`
:   the device whose io range will be mapped

`int index`
:   index of the io range

**Description**

Returns a pointer to the mapped memory

unsigned int irq_of_parse_and_map(struct device_node \*dev, int index)
:   Parse and map an interrupt into linux virq space

**Parameters**

`struct device_node *dev`
:   Device node of the device whose interrupt is to be mapped

`int index`
:   Index of the interrupt to map

**Description**

This function is a wrapper that chains [`of_irq_parse_one()`](kernel-api.md#c.of_irq_parse_one "of_irq_parse_one") and
irq_create_of_mapping() to make things easier to callers

struct device_node \*of_irq_find_parent(struct device_node \*child)
:   Given a device node, find its interrupt parent node

**Parameters**

`struct device_node *child`
:   pointer to device node

**Return**

A pointer to the interrupt parent node, or NULL if the interrupt
parent could not be determined.

int of_irq_parse_raw(const __be32 \*addr, struct of_phandle_args \*out_irq)
:   Low level interrupt tree parsing

**Parameters**

`const __be32 *addr`
:   address specifier (start of "reg" property of the device) in be32 format

`struct of_phandle_args *out_irq`
:   structure of_phandle_args updated by this function

**Description**

This function is a low-level interrupt tree walking function. It
can be used to do a partial walk with synthetized reg and interrupts
properties, for example when resolving PCI interrupts when no device
node exist for the parent. It takes an interrupt specifier structure as
input, walks the tree looking for any interrupt-map properties, translates
the specifier for each map, and then returns the translated map.

**Return**

0 on success and a negative number on error

int of_irq_parse_one(struct device_node \*device, int index, struct of_phandle_args \*out_irq)
:   Resolve an interrupt for a device

**Parameters**

`struct device_node *device`
:   the device whose interrupt is to be resolved

`int index`
:   index of the interrupt to resolve

`struct of_phandle_args *out_irq`
:   structure of_phandle_args filled by this function

**Description**

This function resolves an interrupt for a node by walking the interrupt tree,
finding which interrupt controller node it is attached to, and returning the
interrupt specifier that can be used to retrieve a Linux IRQ number.

int of_irq_to_resource(struct device_node \*dev, int index, struct resource \*r)
:   Decode a node's IRQ and return it as a resource

**Parameters**

`struct device_node *dev`
:   pointer to device tree node

`int index`
:   zero-based index of the irq

`struct resource *r`
:   pointer to resource structure to return result into.

int of_irq_get(struct device_node \*dev, int index)
:   Decode a node's IRQ and return it as a Linux IRQ number

**Parameters**

`struct device_node *dev`
:   pointer to device tree node

`int index`
:   zero-based index of the IRQ

**Return**

Linux IRQ number on success, or 0 on the IRQ mapping failure, or
-EPROBE_DEFER if the IRQ domain is not yet created, or error code in case
of any other failure.

int of_irq_get_byname(struct device_node \*dev, const char \*name)
:   Decode a node's IRQ and return it as a Linux IRQ number

**Parameters**

`struct device_node *dev`
:   pointer to device tree node

`const char *name`
:   IRQ name

**Return**

Linux IRQ number on success, or 0 on the IRQ mapping failure, or
-EPROBE_DEFER if the IRQ domain is not yet created, or error code in case
of any other failure.

int of_irq_to_resource_table(struct device_node \*dev, struct resource \*res, int nr_irqs)
:   Fill in resource table with node's IRQ info

**Parameters**

`struct device_node *dev`
:   pointer to device tree node

`struct resource *res`
:   array of resources to fill in

`int nr_irqs`
:   the number of IRQs (and upper bound for num of **res** elements)

**Return**

The size of the filled in table (up to **nr_irqs**).

struct irq_domain \*of_msi_get_domain(struct [device](../driver-api/infrastructure.md#c.device "device") \*dev, struct device_node \*np, enum irq_domain_bus_token token)
:   Use msi-parent to find the relevant MSI domain

**Parameters**

`struct device *dev`
:   device for which the domain is requested

`struct device_node *np`
:   device node for **dev**

`enum irq_domain_bus_token token`
:   bus type for this domain

**Description**

Parse the msi-parent property (both the simple and the complex
versions), and returns the corresponding MSI domain.

**Return**

the MSI domain for this device (or NULL on failure).

void of_msi_configure(struct [device](../driver-api/infrastructure.md#c.device "device") \*dev, struct device_node \*np)
:   Set the msi_domain field of a device

**Parameters**

`struct device *dev`
:   device structure to associate with an MSI irq domain

`struct device_node *np`
:   device node for that device

void \*of_fdt_unflatten_tree(const unsigned long \*blob, struct device_node \*dad, struct device_node \*\*mynodes)
:   create tree of device_nodes from flat blob

**Parameters**

`const unsigned long *blob`
:   Flat device tree blob

`struct device_node *dad`
:   Parent device node

`struct device_node **mynodes`
:   The device tree created by the call

**Description**

unflattens the device-tree passed by the firmware, creating the
tree of struct device_node. It also fills the "name" and "type"
pointers of the nodes so the normal device-tree walking functions
can be used.

**Return**

NULL on failure or the memory chunk containing the unflattened
device tree on success.

## Driver model functions

int of_driver_match_device(struct [device](../driver-api/infrastructure.md#c.device "device") \*dev, const struct [device_driver](../driver-api/infrastructure.md#c.device_driver "device_driver") \*drv)
:   Tell if a driver's of_match_table matches a device.

**Parameters**

`struct device *dev`
:   the device structure to match against

`const struct device_driver *drv`
:   the device_driver structure to test

const struct of_device_id \*of_match_device(const struct of_device_id \*matches, const struct [device](../driver-api/infrastructure.md#c.device "device") \*dev)
:   Tell if a [`struct device`](../driver-api/infrastructure.md#c.device "device") matches an of_device_id list

**Parameters**

`const struct of_device_id *matches`
:   array of of device match structures to search in

`const struct device *dev`
:   the of device structure to match against

**Description**

Used by a driver to check whether an platform_device present in the
system is in its list of supported devices.

int of_dma_configure_id(struct [device](../driver-api/infrastructure.md#c.device "device") \*dev, struct device_node \*np, bool force_dma, const u32 \*id)
:   Setup DMA configuration

**Parameters**

`struct device *dev`
:   Device to apply DMA configuration

`struct device_node *np`
:   Pointer to OF node having DMA configuration

`bool force_dma`
:   Whether device is to be set up by of_dma_configure() even if
    DMA capability is not explicitly described by firmware.

`const u32 *id`
:   Optional const pointer value input id

**Description**

Try to get devices's DMA configuration from DT and update it
accordingly.

If platform code needs to use its own special DMA configuration, it
can use a platform bus notifier and handle BUS_NOTIFY_ADD_DEVICE events
to fix up DMA configuration.

ssize_t of_device_modalias(struct [device](../driver-api/infrastructure.md#c.device "device") \*dev, char \*str, ssize_t len)
:   Fill buffer with newline terminated modalias string

**Parameters**

`struct device *dev`
:   Calling device

`char *str`
:   Modalias string

`ssize_t len`
:   Size of **str**

void of_device_uevent(const struct [device](../driver-api/infrastructure.md#c.device "device") \*dev, struct kobj_uevent_env \*env)
:   Display OF related uevent information

**Parameters**

`const struct device *dev`
:   Device to display the uevent information for

`struct kobj_uevent_env *env`
:   Kernel object's userspace event reference to fill up

void of_device_make_bus_id(struct [device](../driver-api/infrastructure.md#c.device "device") \*dev)
:   Use the device node data to assign a unique name

**Parameters**

`struct device *dev`
:   pointer to device structure that is linked to a device tree node

**Description**

This routine will first try using the translated bus address to
derive a unique name. If it cannot, then it will prepend names from
parent nodes until a unique name can be derived.

struct of_dev_auxdata
:   lookup table entry for device names & platform_data

**Definition**:

```
struct of_dev_auxdata {
    char *compatible;
    resource_size_t phys_addr;
    char *name;
    void *platform_data;
};
```

**Members**

`compatible`
:   compatible value of node to match against node

`phys_addr`
:   Start address of registers to match against node

`name`
:   Name to assign for matching nodes

`platform_data`
:   platform_data to assign for matching nodes

**Description**

This lookup table allows the caller of [`of_platform_populate()`](kernel-api.md#c.of_platform_populate "of_platform_populate") to override
the names of devices when creating devices from the device tree. The table
should be terminated with an empty entry. It also allows the platform_data
pointer to be set.

The reason for this functionality is that some Linux infrastructure uses
the device name to look up a specific device, but the Linux-specific names
are not encoded into the device tree, so the kernel needs to provide specific
values.

**Note**

Using an auxdata lookup table should be considered a last resort when
converting a platform to use the DT. Normally the automatically generated
device name will not matter, and drivers should obtain data from the device
node instead of from an anonymous platform_data pointer.

struct platform_device \*of_find_device_by_node(struct device_node \*np)
:   Find the platform_device associated with a node

**Parameters**

`struct device_node *np`
:   Pointer to device tree node

**Description**

Takes a reference to the embedded [`struct device`](../driver-api/infrastructure.md#c.device "device") which needs to be dropped
after use.

**Return**

platform_device pointer, or NULL if not found

struct platform_device \*of_device_alloc(struct device_node \*np, const char \*bus_id, struct [device](../driver-api/infrastructure.md#c.device "device") \*parent)
:   Allocate and initialize an of_device

**Parameters**

`struct device_node *np`
:   device node to assign to device

`const char *bus_id`
:   Name to assign to the device. May be null to use default name.

`struct device *parent`
:   Parent device.

struct platform_device \*of_platform_device_create(struct device_node \*np, const char \*bus_id, struct [device](../driver-api/infrastructure.md#c.device "device") \*parent)
:   Alloc, initialize and register an of_device

**Parameters**

`struct device_node *np`
:   pointer to node to create device for

`const char *bus_id`
:   name to assign device

`struct device *parent`
:   Linux device model parent device.

**Return**

Pointer to created platform device, or NULL if a device was not
registered. Unavailable devices will not get registered.

int of_platform_bus_probe(struct device_node \*root, const struct of_device_id \*matches, struct [device](../driver-api/infrastructure.md#c.device "device") \*parent)
:   Probe the device-tree for platform buses

**Parameters**

`struct device_node *root`
:   parent of the first level to probe or NULL for the root of the tree

`const struct of_device_id *matches`
:   match table for bus nodes

`struct device *parent`
:   parent to hook devices from, NULL for toplevel

**Description**

Note that children of the provided root are not instantiated as devices
unless the specified root itself matches the bus list and is not NULL.

int of_platform_populate(struct device_node \*root, const struct of_device_id \*matches, const struct [of_dev_auxdata](kernel-api.md#c.of_dev_auxdata "of_dev_auxdata") \*lookup, struct [device](../driver-api/infrastructure.md#c.device "device") \*parent)
:   Populate platform_devices from device tree data

**Parameters**

`struct device_node *root`
:   parent of the first level to probe or NULL for the root of the tree

`const struct of_device_id *matches`
:   match table, NULL to use the default

`const struct of_dev_auxdata *lookup`
:   auxdata table for matching id and platform_data with device nodes

`struct device *parent`
:   parent to hook devices from, NULL for toplevel

**Description**

Similar to [`of_platform_bus_probe()`](kernel-api.md#c.of_platform_bus_probe "of_platform_bus_probe"), this function walks the device tree
and creates devices from nodes. It differs in that it follows the modern
convention of requiring all device nodes to have a 'compatible' property,
and it is suitable for creating devices which are children of the root
node (of_platform_bus_probe will only create children of the root which
are selected by the **matches** argument).

New board support should be using this function instead of
[`of_platform_bus_probe()`](kernel-api.md#c.of_platform_bus_probe "of_platform_bus_probe").

**Return**

0 on success, < 0 on failure.

void of_platform_depopulate(struct [device](../driver-api/infrastructure.md#c.device "device") \*parent)
:   Remove devices populated from device tree

**Parameters**

`struct device *parent`
:   device which children will be removed

**Description**

Complementary to [`of_platform_populate()`](kernel-api.md#c.of_platform_populate "of_platform_populate"), this function removes children
of the given device (and, recursively, their children) that have been
created from their respective device tree nodes (and only those,
leaving others - eg. manually created - unharmed).

int devm_of_platform_populate(struct [device](../driver-api/infrastructure.md#c.device "device") \*dev)
:   Populate platform_devices from device tree data

**Parameters**

`struct device *dev`
:   device that requested to populate from device tree data

**Description**

Similar to [`of_platform_populate()`](kernel-api.md#c.of_platform_populate "of_platform_populate"), but will automatically call
[`of_platform_depopulate()`](kernel-api.md#c.of_platform_depopulate "of_platform_depopulate") when the device is unbound from the bus.

**Return**

0 on success, < 0 on failure.

void devm_of_platform_depopulate(struct [device](../driver-api/infrastructure.md#c.device "device") \*dev)
:   Remove devices populated from device tree

**Parameters**

`struct device *dev`
:   device that requested to depopulate from device tree data

**Description**

Complementary to [`devm_of_platform_populate()`](kernel-api.md#c.devm_of_platform_populate "devm_of_platform_populate"), this function removes children
of the given device (and, recursively, their children) that have been
created from their respective device tree nodes (and only those,
leaving others - eg. manually created - unharmed).

## Overlay and Dynamic DT functions

int of_resolve_phandles(struct device_node \*overlay)
:   Relocate and resolve overlay against live tree

**Parameters**

`struct device_node *overlay`
:   Pointer to devicetree overlay to relocate and resolve

**Description**

Modify (relocate) values of local phandles in **overlay** to a range that
does not conflict with the live expanded devicetree. Update references
to the local phandles in **overlay**. Update (resolve) phandle references
in **overlay** that refer to the live expanded devicetree.

Phandle values in the live tree are in the range of
1 .. live_tree_max_phandle(). The range of phandle values in the overlay
also begin with at 1. Adjust the phandle values in the overlay to begin
at live_tree_max_phandle() + 1. Update references to the phandles to
the adjusted phandle values.

The name of each property in the "__fixups__" node in the overlay matches
the name of a symbol (a label) in the live tree. The values of each
property in the "__fixups__" node is a list of the property values in the
overlay that need to be updated to contain the phandle reference
corresponding to that symbol in the live tree. Update the references in
the overlay with the phandle values in the live tree.

**overlay** must be detached.

Resolving and applying **overlay** to the live expanded devicetree must be
protected by a mechanism to ensure that multiple overlays are processed
in a single threaded manner so that multiple overlays will not relocate
phandles to overlapping ranges. The mechanism to enforce this is not
yet implemented.

**Return**

`0` on success or a negative error value on error.

struct device_node \*of_node_get(struct device_node \*node)
:   Increment refcount of a node

**Parameters**

`struct device_node *node`
:   Node to inc refcount, NULL is supported to simplify writing of
    callers

**Return**

The node with refcount incremented.

void of_node_put(struct device_node \*node)
:   Decrement refcount of a node

**Parameters**

`struct device_node *node`
:   Node to dec refcount, NULL is supported to simplify writing of
    callers

int of_detach_node(struct device_node \*np)
:   "Unplug" a node from the device tree.

**Parameters**

`struct device_node *np`
:   Pointer to the caller's Device Node

struct device_node \*of_changeset_create_node(struct [of_changeset](kernel-api.md#c.of_changeset "of_changeset") \*ocs, struct device_node \*parent, const char \*full_name)
:   Dynamically create a device node and attach to a given changeset.

**Parameters**

`struct of_changeset *ocs`
:   Pointer to changeset

`struct device_node *parent`
:   Pointer to parent device node

`const char *full_name`
:   Node full name

**Return**

Pointer to the created device node or NULL in case of an error.

void of_changeset_init(struct [of_changeset](kernel-api.md#c.of_changeset "of_changeset") \*ocs)
:   Initialize a changeset for use

**Parameters**

`struct of_changeset *ocs`
:   changeset pointer

**Description**

Initialize a changeset structure

void of_changeset_destroy(struct [of_changeset](kernel-api.md#c.of_changeset "of_changeset") \*ocs)
:   Destroy a changeset

**Parameters**

`struct of_changeset *ocs`
:   changeset pointer

**Description**

Destroys a changeset. Note that if a changeset is applied,
its changes to the tree cannot be reverted.

int of_changeset_apply(struct [of_changeset](kernel-api.md#c.of_changeset "of_changeset") \*ocs)
:   Applies a changeset

**Parameters**

`struct of_changeset *ocs`
:   changeset pointer

**Description**

Applies a changeset to the live tree.
Any side-effects of live tree state changes are applied here on
success, like creation/destruction of devices and side-effects
like creation of sysfs properties and directories.

**Return**

0 on success, a negative error value in case of an error.
On error the partially applied effects are reverted.

int of_changeset_revert(struct [of_changeset](kernel-api.md#c.of_changeset "of_changeset") \*ocs)
:   Reverts an applied changeset

**Parameters**

`struct of_changeset *ocs`
:   changeset pointer

**Description**

Reverts a changeset returning the state of the tree to what it
was before the application.
Any side-effects like creation/destruction of devices and
removal of sysfs properties and directories are applied.

**Return**

0 on success, a negative error value in case of an error.

int of_changeset_action(struct [of_changeset](kernel-api.md#c.of_changeset "of_changeset") \*ocs, unsigned long action, struct device_node \*np, struct property \*prop)
:   Add an action to the tail of the changeset list

**Parameters**

`struct of_changeset *ocs`
:   changeset pointer

`unsigned long action`
:   action to perform

`struct device_node *np`
:   Pointer to device node

`struct property *prop`
:   Pointer to property

**Description**

On action being one of:
+ OF_RECONFIG_ATTACH_NODE
+ OF_RECONFIG_DETACH_NODE,
+ OF_RECONFIG_ADD_PROPERTY
+ OF_RECONFIG_REMOVE_PROPERTY,
+ OF_RECONFIG_UPDATE_PROPERTY

**Return**

0 on success, a negative error value in case of an error.

int of_changeset_add_prop_string(struct [of_changeset](kernel-api.md#c.of_changeset "of_changeset") \*ocs, struct device_node \*np, const char \*prop_name, const char \*str)
:   Add a string property to a changeset

**Parameters**

`struct of_changeset *ocs`
:   changeset pointer

`struct device_node *np`
:   device node pointer

`const char *prop_name`
:   name of the property to be added

`const char *str`
:   pointer to null terminated string

**Description**

Create a string property and add it to a changeset.

**Return**

0 on success, a negative error value in case of an error.

int of_changeset_add_prop_string_array(struct [of_changeset](kernel-api.md#c.of_changeset "of_changeset") \*ocs, struct device_node \*np, const char \*prop_name, const char \*\*str_array, size_t sz)
:   Add a string list property to a changeset

**Parameters**

`struct of_changeset *ocs`
:   changeset pointer

`struct device_node *np`
:   device node pointer

`const char *prop_name`
:   name of the property to be added

`const char **str_array`
:   pointer to an array of null terminated strings

`size_t sz`
:   number of string array elements

**Description**

Create a string list property and add it to a changeset.

**Return**

0 on success, a negative error value in case of an error.

int of_changeset_add_prop_u32_array(struct [of_changeset](kernel-api.md#c.of_changeset "of_changeset") \*ocs, struct device_node \*np, const char \*prop_name, const u32 \*array, size_t sz)
:   Add a property of 32 bit integers property to a changeset

**Parameters**

`struct of_changeset *ocs`
:   changeset pointer

`struct device_node *np`
:   device node pointer

`const char *prop_name`
:   name of the property to be added

`const u32 *array`
:   pointer to an array of 32 bit integers

`size_t sz`
:   number of array elements

**Description**

Create a property of 32 bit integers and add it to a changeset.

**Return**

0 on success, a negative error value in case of an error.

int of_overlay_notifier_register(struct notifier_block \*nb)
:   Register notifier for overlay operations

**Parameters**

`struct notifier_block *nb`
:   Notifier block to register

**Description**

Register for notification on overlay operations on device tree nodes. The
reported actions definied by **of_reconfig_change**. The notifier callback
furthermore receives a pointer to the affected device tree node.

Note that a notifier callback is not supposed to store pointers to a device
tree node or its content beyond **OF_OVERLAY_POST_REMOVE** corresponding to the
respective node it received.

int of_overlay_notifier_unregister(struct notifier_block \*nb)
:   Unregister notifier for overlay operations

**Parameters**

`struct notifier_block *nb`
:   Notifier block to unregister

int of_overlay_fdt_apply(const void \*overlay_fdt, u32 overlay_fdt_size, int \*ret_ovcs_id, struct device_node \*base)
:   Create and apply an overlay changeset

**Parameters**

`const void *overlay_fdt`
:   pointer to overlay FDT

`u32 overlay_fdt_size`
:   number of bytes in **overlay_fdt**

`int *ret_ovcs_id`
:   pointer for returning created changeset id

`struct device_node *base`
:   pointer for the target node to apply overlay

**Description**

Creates and applies an overlay changeset.

See of_overlay_apply() for important behavior information.

On error return, the changeset may be partially applied. This is especially
likely if an OF_OVERLAY_POST_APPLY notifier returns an error. In this case
the caller should call [`of_overlay_remove()`](kernel-api.md#c.of_overlay_remove "of_overlay_remove") with the value in **\*ret_ovcs_id**.

**Return**

0 on success, or a negative error number. **\*ret_ovcs_id** is set to
the value of overlay changeset id, which can be passed to [`of_overlay_remove()`](kernel-api.md#c.of_overlay_remove "of_overlay_remove")
to remove the overlay.

int of_overlay_remove(int \*ovcs_id)
:   Revert and free an overlay changeset

**Parameters**

`int *ovcs_id`
:   Pointer to overlay changeset id

**Description**

Removes an overlay if it is permissible. **ovcs_id** was previously returned
by [`of_overlay_fdt_apply()`](kernel-api.md#c.of_overlay_fdt_apply "of_overlay_fdt_apply").

If an error occurred while attempting to revert the overlay changeset,
then an attempt is made to re-apply any changeset entry that was
reverted. If an error occurs on re-apply then the state of the device
tree can not be determined, and any following attempt to apply or remove
an overlay changeset will be refused.

A non-zero return value will not revert the changeset if error is from:
:   - parameter checks
    - overlay changeset pre-remove notifier
    - overlay changeset entry revert

If an error is returned by an overlay changeset pre-remove notifier
then no further overlay changeset pre-remove notifier will be called.

If more than one notifier returns an error, then the last notifier
error to occur is returned.

A non-zero return value will revert the changeset if error is from:
:   - overlay changeset entry notifier
    - overlay changeset post-remove notifier

If an error is returned by an overlay changeset post-remove notifier
then no further overlay changeset post-remove notifier will be called.

**Return**

0 on success, or a negative error number. **\*ovcs_id** is set to
zero after reverting the changeset, even if a subsequent error occurs.

int of_overlay_remove_all(void)
:   Reverts and frees all overlay changesets

**Parameters**

`void`
:   no arguments

**Description**

Removes all overlays from the system in the correct order.

**Return**

0 on success, or a negative error number
