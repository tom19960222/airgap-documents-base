---
collection: qemu
version: "11.1.0"
title: "QEMU Object Model (QOM) API Reference"
source_url: https://www.qemu.org/docs/master/devel/qom-api.html
fetched_at: 2026-08-21T03:25:56+00:00
---
# QEMU Object Model (QOM) API Reference

This is the complete API documentation for [The QEMU Object Model (QOM)](qom.md#qom).

ObjectPropertyAccessor
:   **Typedef**:

**Syntax**

> `void ObjectPropertyAccessor (Object *obj, Visitor *v, const char *name, void *opaque, Error **errp)`

**Parameters**

`Object *obj`
:   the object that owns the property

`Visitor *v`
:   the visitor that contains the property data

`const char *name`
:   the name of the property

`void *opaque`
:   the object property opaque

`Error **errp`
:   a pointer to an Error that is filled if getting/setting fails.

**Description**

Called when trying to get/set a property.

ObjectPropertyResolve
:   **Typedef**:

**Syntax**

> `Object * ObjectPropertyResolve (Object *obj, void *opaque, const char *part)`

**Parameters**

`Object *obj`
:   the object that owns the property

`void *opaque`
:   the opaque registered with the property

`const char *part`
:   the name of the property

**Description**

Resolves the [`Object`](qom-api.md#c.Object "Object") corresponding to property **part**.

The returned object can also be used as a starting point
to resolve a relative path starting with “**part**”.

**Return**

If **path** is the path that led to **obj**, the function
returns the [`Object`](qom-api.md#c.Object "Object") corresponding to “**path**/**part**”.
If “**path**/**part**” is not a valid object path, it returns `NULL`.

ObjectPropertyRelease
:   **Typedef**:

**Syntax**

> `void ObjectPropertyRelease (Object *obj, const char *name, void *opaque)`

**Parameters**

`Object *obj`
:   the object that owns the property

`const char *name`
:   the name of the property

`void *opaque`
:   the opaque registered with the property

**Description**

Called when a property is removed from a object.

ObjectPropertyInit
:   **Typedef**:

**Syntax**

> `void ObjectPropertyInit (Object *obj, ObjectProperty *prop)`

**Parameters**

`Object *obj`
:   the object that owns the property

`ObjectProperty *prop`
:   the property to set

**Description**

Called when a property is initialized.

ObjectUnparent
:   **Typedef**:

**Syntax**

> `void ObjectUnparent (Object *obj)`

**Parameters**

`Object *obj`
:   the object that is being removed from the composition tree

**Description**

Called when an object is being removed from the QOM composition tree.
The function should remove any backlinks from children objects to **obj**.

ObjectFree
:   **Typedef**:

**Syntax**

> `void ObjectFree (void *obj)`

**Parameters**

`void *obj`
:   the object being freed

**Description**

Called when an object’s last reference is removed.

struct ObjectClass

**Definition**:

```
struct ObjectClass {
};
```

**Members**

**Description**

The base for all classes. The only thing that [`ObjectClass`](qom-api.md#c.ObjectClass "ObjectClass") contains is an
integer type handle.

struct Object

**Definition**:

```
struct Object {
};
```

**Members**

**Description**

The base for all objects. The first member of this object is a pointer to
a [`ObjectClass`](qom-api.md#c.ObjectClass "ObjectClass"). Since C guarantees that the first member of a structure
always begins at byte 0 of that structure, as long as any sub-object places
its parent as the first member, we can cast directly to a [`Object`](qom-api.md#c.Object "Object").

As a result, [`Object`](qom-api.md#c.Object "Object") contains a reference to the objects type as its
first member. This allows identification of the real type of the object at
run time.

DECLARE_INSTANCE_CHECKER

`DECLARE_INSTANCE_CHECKER (InstanceType, OBJ_NAME, TYPENAME)`

**Parameters**

`InstanceType`
:   instance struct name

`OBJ_NAME`
:   the object name in uppercase with underscore separators

`TYPENAME`
:   type name

**Description**

Direct usage of this macro should be avoided, and the complete
OBJECT_DECLARE_TYPE macro is recommended instead.

This macro will provide the instance type cast functions for a
QOM type.

DECLARE_CLASS_CHECKERS

`DECLARE_CLASS_CHECKERS (ClassType, OBJ_NAME, TYPENAME)`

**Parameters**

`ClassType`
:   class struct name

`OBJ_NAME`
:   the object name in uppercase with underscore separators

`TYPENAME`
:   type name

**Description**

Direct usage of this macro should be avoided, and the complete
OBJECT_DECLARE_TYPE macro is recommended instead.

This macro will provide the class type cast functions for a
QOM type.

DECLARE_OBJ_CHECKERS

`DECLARE_OBJ_CHECKERS (InstanceType, ClassType, OBJ_NAME, TYPENAME)`

**Parameters**

`InstanceType`
:   instance struct name

`ClassType`
:   class struct name

`OBJ_NAME`
:   the object name in uppercase with underscore separators

`TYPENAME`
:   type name

**Description**

Direct usage of this macro should be avoided, and the complete
OBJECT_DECLARE_TYPE macro is recommended instead.

This macro will provide the three standard type cast functions for a
QOM type.

OBJECT_DECLARE_TYPE

`OBJECT_DECLARE_TYPE (InstanceType, ClassType, MODULE_OBJ_NAME)`

**Parameters**

`InstanceType`
:   instance struct name

`ClassType`
:   class struct name

`MODULE_OBJ_NAME`
:   the object name in uppercase with underscore separators

**Description**

This macro is typically used in a header file, and will:

> - create the typedefs for the object and class structs
> - register the type for use with g_autoptr
> - provide three standard type cast functions

The object struct and class struct need to be declared manually.

OBJECT_DECLARE_SIMPLE_TYPE

`OBJECT_DECLARE_SIMPLE_TYPE (InstanceType, MODULE_OBJ_NAME)`

**Parameters**

`InstanceType`
:   instance struct name

`MODULE_OBJ_NAME`
:   the object name in uppercase with underscore separators

**Description**

This does the same as OBJECT_DECLARE_TYPE(), but with no class struct
declared.

This macro should be used unless the class struct needs to have
virtual methods declared.

DO_OBJECT_DEFINE_TYPE_EXTENDED

`DO_OBJECT_DEFINE_TYPE_EXTENDED (ModuleObjName, module_obj_name, MODULE_OBJ_NAME, PARENT_MODULE_OBJ_NAME, ABSTRACT, CLASS_SIZE, ...)`

**Parameters**

`ModuleObjName`
:   the object name with initial caps

`module_obj_name`
:   the object name in lowercase with underscore separators

`MODULE_OBJ_NAME`
:   the object name in uppercase with underscore separators

`PARENT_MODULE_OBJ_NAME`
:   the parent object name in uppercase with underscore
    separators

`ABSTRACT`
:   boolean flag to indicate whether the object can be instantiated

`CLASS_SIZE`
:   size of the type’s class

`...`
:   list of initializers for “InterfaceInfo” to declare implemented interfaces

**Description**

This is the base macro used to implement all the OBJECT_DEFINE_\*
macros. It should never be used directly in a source file.

OBJECT_DEFINE_TYPE_EXTENDED

`OBJECT_DEFINE_TYPE_EXTENDED (ModuleObjName, module_obj_name, MODULE_OBJ_NAME, PARENT_MODULE_OBJ_NAME, ABSTRACT, ...)`

**Parameters**

`ModuleObjName`
:   the object name with initial caps

`module_obj_name`
:   the object name in lowercase with underscore separators

`MODULE_OBJ_NAME`
:   the object name in uppercase with underscore separators

`PARENT_MODULE_OBJ_NAME`
:   the parent object name in uppercase with underscore
    separators

`ABSTRACT`
:   boolean flag to indicate whether the object can be instantiated

`...`
:   list of initializers for “InterfaceInfo” to declare implemented interfaces

**Description**

This macro is typically used in a source file, and will:

> - declare prototypes for _finalize, _class_init and _init methods
> - declare the TypeInfo struct instance
> - provide the constructor to register the type

After using this macro, implementations of the _finalize, _class_init,
and _init methods need to be written. Any of these can be zero-line
no-op impls if no special logic is required for a given type.

This macro should rarely be used, instead one of the more specialized
macros is usually a better choice.

OBJECT_DEFINE_TYPE

`OBJECT_DEFINE_TYPE (ModuleObjName, module_obj_name, MODULE_OBJ_NAME, PARENT_MODULE_OBJ_NAME)`

**Parameters**

`ModuleObjName`
:   the object name with initial caps

`module_obj_name`
:   the object name in lowercase with underscore separators

`MODULE_OBJ_NAME`
:   the object name in uppercase with underscore separators

`PARENT_MODULE_OBJ_NAME`
:   the parent object name in uppercase with underscore
    separators

**Description**

This is a specialization of OBJECT_DEFINE_TYPE_EXTENDED, which is suitable
for the common case of a non-abstract type, without any interfaces.

OBJECT_DEFINE_TYPE_WITH_INTERFACES

`OBJECT_DEFINE_TYPE_WITH_INTERFACES (ModuleObjName, module_obj_name, MODULE_OBJ_NAME, PARENT_MODULE_OBJ_NAME, ...)`

**Parameters**

`ModuleObjName`
:   the object name with initial caps

`module_obj_name`
:   the object name in lowercase with underscore separators

`MODULE_OBJ_NAME`
:   the object name in uppercase with underscore separators

`PARENT_MODULE_OBJ_NAME`
:   the parent object name in uppercase with underscore
    separators

`...`
:   list of initializers for “InterfaceInfo” to declare implemented interfaces

**Description**

This is a specialization of OBJECT_DEFINE_TYPE_EXTENDED, which is suitable
for the common case of a non-abstract type, with one or more implemented
interfaces.

Note when passing the list of interfaces, be sure to include the final
NULL entry, e.g. { TYPE_USER_CREATABLE }, { NULL }

OBJECT_DEFINE_ABSTRACT_TYPE

`OBJECT_DEFINE_ABSTRACT_TYPE (ModuleObjName, module_obj_name, MODULE_OBJ_NAME, PARENT_MODULE_OBJ_NAME)`

**Parameters**

`ModuleObjName`
:   the object name with initial caps

`module_obj_name`
:   the object name in lowercase with underscore separators

`MODULE_OBJ_NAME`
:   the object name in uppercase with underscore separators

`PARENT_MODULE_OBJ_NAME`
:   the parent object name in uppercase with underscore
    separators

**Description**

This is a specialization of OBJECT_DEFINE_TYPE_EXTENDED, which is suitable
for defining an abstract type, without any interfaces.

OBJECT_DEFINE_SIMPLE_TYPE_WITH_INTERFACES

`OBJECT_DEFINE_SIMPLE_TYPE_WITH_INTERFACES (ModuleObjName, module_obj_name, MODULE_OBJ_NAME, PARENT_MODULE_OBJ_NAME, ...)`

**Parameters**

`ModuleObjName`
:   the object name with initial caps

`module_obj_name`
:   the object name in lowercase with underscore separators

`MODULE_OBJ_NAME`
:   the object name in uppercase with underscore separators

`PARENT_MODULE_OBJ_NAME`
:   the parent object name in uppercase with underscore
    separators

`...`
:   variable arguments

**Description**

This is a variant of OBJECT_DEFINE_TYPE_EXTENDED, which is suitable for
the case of a non-abstract type, with interfaces, and with no requirement
for a class struct.

OBJECT_DEFINE_SIMPLE_TYPE

`OBJECT_DEFINE_SIMPLE_TYPE (ModuleObjName, module_obj_name, MODULE_OBJ_NAME, PARENT_MODULE_OBJ_NAME)`

**Parameters**

`ModuleObjName`
:   the object name with initial caps

`module_obj_name`
:   the object name in lowercase with underscore separators

`MODULE_OBJ_NAME`
:   the object name in uppercase with underscore separators

`PARENT_MODULE_OBJ_NAME`
:   the parent object name in uppercase with underscore
    separators

**Description**

This is a variant of OBJECT_DEFINE_TYPE_EXTENDED, which is suitable for
the common case of a non-abstract type, without any interfaces, and with
no requirement for a class struct. If you declared your type with
OBJECT_DECLARE_SIMPLE_TYPE then this is probably the right choice for
defining it.

struct TypeInfo

**Definition**:

```
struct TypeInfo {
    const char *name;
    const char *parent;
    size_t instance_size;
    size_t instance_align;
    void (*instance_init)(Object *obj);
    void (*instance_post_init)(Object *obj);
    void (*instance_finalize)(Object *obj);
    bool abstract;
    size_t class_size;
    void (*class_init)(ObjectClass *klass, const void *data);
    void (*class_base_init)(ObjectClass *klass, const void *data);
    const void *class_data;
    const InterfaceInfo *interfaces;
};
```

**Members**

`name`
:   The name of the type.

`parent`
:   The name of the parent type.

`instance_size`
:   The size of the object (derivative of [`Object`](qom-api.md#c.Object "Object")). If
    **instance_size** is 0, then the size of the object will be the size of the
    parent object.

`instance_align`
:   The required alignment of the object. If **instance_align**
    is 0, then normal malloc alignment is sufficient; if non-zero, then we
    must use qemu_memalign for allocation.

`instance_init`
:   This function is called to initialize an object. The parent
    class will have already been initialized so the type is only responsible
    for initializing its own members.

`instance_post_init`
:   This function is called to finish initialization of
    an object, after all **instance_init** functions were called, as well as
    **instance_post_init** functions for the parent classes.

`instance_finalize`
:   This function is called during object destruction. This
    is called before the parent **instance_finalize** function has been called.
    An object should only free the members that are unique to its type in this
    function.

`abstract`
:   If this field is true, then the class is considered abstract and
    cannot be directly instantiated.

`class_size`
:   The size of the class object (derivative of [`ObjectClass`](qom-api.md#c.ObjectClass "ObjectClass"))
    for this object. If **class_size** is 0, then the size of the class will be
    assumed to be the size of the parent class. This allows a type to avoid
    implementing an explicit class type if they are not adding additional
    virtual functions.

`class_init`
:   This function is called after all parent class initialization
    has occurred to allow a class to set its default virtual method pointers.
    This is also the function to use to override virtual methods from a parent
    class.

`class_base_init`
:   This function is called for all base classes after all
    parent class initialization has occurred, but before the class itself
    is initialized. This is the function to use to undo the effects of
    memcpy from the parent class to the descendants.

`class_data`
:   Data to pass to the **class_init**,
    **class_base_init**. This can be useful when building dynamic
    classes.

`interfaces`
:   The list of interfaces associated with this type. This
    should point to a static array that’s terminated with a zero filled
    element.

OBJECT

`OBJECT (obj)`

**Parameters**

`obj`
:   A derivative of [`Object`](qom-api.md#c.Object "Object")

**Description**

Converts an object to a [`Object`](qom-api.md#c.Object "Object"). Since all objects are `Objects`,
this function will always succeed.

OBJECT_CLASS

`OBJECT_CLASS (class)`

**Parameters**

`class`
:   A derivative of [`ObjectClass`](qom-api.md#c.ObjectClass "ObjectClass").

**Description**

Converts a class to an [`ObjectClass`](qom-api.md#c.ObjectClass "ObjectClass"). Since all objects are `Objects`,
this function will always succeed.

OBJECT_CHECK

`OBJECT_CHECK (type, obj, name)`

**Parameters**

`type`
:   The C type to use for the return value.

`obj`
:   A derivative of **type** to cast.

`name`
:   The QOM typename of **type**

**Description**

A type safe version of **object_dynamic_cast_assert**. Typically each class
will define a macro based on this type to perform type safe dynamic_casts to
this object type.

If an invalid object is passed to this function, a run time assert will be
generated.

OBJECT_CLASS_CHECK

`OBJECT_CLASS_CHECK (class_type, class, name)`

**Parameters**

`class_type`
:   The C type to use for the return value.

`class`
:   A derivative class of **class_type** to cast.

`name`
:   the QOM typename of **class_type**.

**Description**

A type safe version of **object_class_dynamic_cast_assert**. This macro is
typically wrapped by each type to perform type safe casts of a class to a
specific class type.

OBJECT_GET_CLASS

`OBJECT_GET_CLASS (class, obj, name)`

**Parameters**

`class`
:   The C type to use for the return value.

`obj`
:   The object to obtain the class for.

`name`
:   The QOM typename of **obj**.

**Description**

This function will return a specific class for a given object. Its generally
used by each type to provide a type safe macro to get a specific class type
from an object.

struct InterfaceInfo

**Definition**:

```
struct InterfaceInfo {
    const char *type;
};
```

**Members**

`type`
:   The name of the interface.

**Description**

The information associated with an interface.

struct InterfaceClass

**Definition**:

```
struct InterfaceClass {
    ObjectClass parent_class;
};
```

**Members**

`parent_class`
:   the base class

**Description**

The class for all interfaces. Subclasses of this class should only add
virtual methods.

Note that most of the fields of ObjectClass are unused (all except
“type”, in fact). They are only present in InterfaceClass to allow
**object_class_dynamic_cast** to work with both regular classes and interfaces.

INTERFACE_CLASS

`INTERFACE_CLASS (klass)`

**Parameters**

`klass`
:   class to cast from

**Return**

An [`InterfaceClass`](qom-api.md#c.InterfaceClass "InterfaceClass") or raise an error if cast is invalid

INTERFACE_CHECK

`INTERFACE_CHECK (interface, obj, name)`

**Parameters**

`interface`
:   the type to return

`obj`
:   the object to convert to an interface

`name`
:   the interface type name

**Return**

**obj** casted to **interface** if cast is valid, otherwise raise error.

[Object](qom-api.md#c.Object "Object") \*object_new_with_class([ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*klass)

**Parameters**

`ObjectClass *klass`
:   The class to instantiate.

**Description**

This function will initialize a new object using heap allocated memory.
The returned object has a reference count of 1, and will be freed when
the last reference is dropped.

**Return**

The newly allocated and instantiated object.

[Object](qom-api.md#c.Object "Object") \*object_new(const char \*typename)

**Parameters**

`const char *typename`
:   The name of the type of the object to instantiate.

**Description**

This function will initialize a new object using heap allocated memory.
The returned object has a reference count of 1, and will be freed when
the last reference is dropped.

**Return**

The newly allocated and instantiated object.

[Object](qom-api.md#c.Object "Object") \*object_new_with_props(const char \*typename, [Object](qom-api.md#c.Object "Object") \*parent, const char \*id, Error \*\*errp, ...)

**Parameters**

`const char *typename`
:   The name of the type of the object to instantiate.

`Object *parent`
:   the parent object

`const char *id`
:   The unique ID of the object

`Error **errp`
:   pointer to error object

`...`
:   list of property names and values

**Description**

This function will initialize a new object using heap allocated memory.
The returned object has a reference count of 1, and will be freed when
the last reference is dropped.

The **id** parameter will be used when registering the object as a
child of **parent** in the composition tree.

The variadic parameters are a list of pairs of (propname, propvalue)
strings. The propname of `NULL` indicates the end of the property
list. If the object implements the user creatable interface, the
object will be marked complete once all the properties have been
processed.

Creating an object with properties

```c
  Error *err = NULL;
  Object *obj;

  obj = object_new_with_props(TYPE_MEMORY_BACKEND_FILE,
                              object_get_objects_root(),
                              "hostmem0",
                              &err,
                              "share", "yes",
                              "mem-path", "/dev/shm/somefile",
                              "prealloc", "yes",
                              "size", "1048576",
                              NULL);

  if (!obj) {
    error_reportf_err(err, "Cannot create memory backend: ");
  }
```

The returned object will have one stable reference maintained
for as long as it is present in the object hierarchy.

**Return**

The newly allocated, instantiated & initialized object.

[Object](qom-api.md#c.Object "Object") \*object_new_with_propv(const char \*typename, [Object](qom-api.md#c.Object "Object") \*parent, const char \*id, va_list vargs, Error \*\*errp)

**Parameters**

`const char *typename`
:   The name of the type of the object to instantiate.

`Object *parent`
:   the parent object

`const char *id`
:   The unique ID of the object

`va_list vargs`
:   list of property names and values

`Error **errp`
:   pointer to error object

**Description**

See object_new_with_props() for documentation.

[Object](qom-api.md#c.Object "Object") \*object_new_with_props_from_qdict(const char \*typename, [Object](qom-api.md#c.Object "Object") \*parent, const char \*id, const QDict \*props, Visitor \*v, Error \*\*errp)

**Parameters**

`const char *typename`
:   The name of the type of the object to instantiate.

`Object *parent`
:   the parent object

`const char *id`
:   The unique ID of the object

`const QDict *props`
:   dictionary of property names and values

`Visitor *v`
:   visitor to iterate over **props**

`Error **errp`
:   pointer to error object

**Description**

A variant of object_new_with_props() which accepts the
properties in a QDict.

[Object](qom-api.md#c.Object "Object") \*object_new_with_props_parentless(const char \*typename, Error \*\*errp, ...)

**Parameters**

`const char *typename`
:   The name of the type of the object to instantiate.

`Error **errp`
:   pointer to error object

`...`
:   list of property names and values

**Description**

Behaviour as object_new_with_props(), except the object
will not be added to any parent and thus the caller will
own the returned instance. The caller must call
object_unref when it is no longer required.

[Object](qom-api.md#c.Object "Object") \*object_new_with_propv_parentless(const char \*typename, va_list vargs, Error \*\*errp)

**Parameters**

`const char *typename`
:   The name of the type of the object to instantiate.

`va_list vargs`
:   list of property names and values

`Error **errp`
:   pointer to error object

**Description**

Behaviour as object_new_with_propv(), except the object
will not be added to any parent and thus the caller will
own the returned instance. The caller must call
object_unref when it is no longer required.

[Object](qom-api.md#c.Object "Object") \*object_new_with_props_from_qdict_parentless(const char \*typename, const QDict \*props, Visitor \*v, Error \*\*errp)

**Parameters**

`const char *typename`
:   The name of the type of the object to instantiate.

`const QDict *props`
:   dictionary of property names and values

`Visitor *v`
:   visitor to iterate over **props**

`Error **errp`
:   pointer to error object

**Description**

Behaviour as object_new_with_props_from_qdict(), except the
object will not be added to any parent and thus the caller
will own the returned instance. The caller must call
object_unref when it is no longer required.

bool object_set_props([Object](qom-api.md#c.Object "Object") \*obj, Error \*\*errp, ...)

**Parameters**

`Object *obj`
:   the object instance to set properties on

`Error **errp`
:   pointer to error object

`...`
:   list of property names and values

**Description**

This function will set a list of properties on an existing object
instance.

The variadic parameters are a list of pairs of (propname, propvalue)
strings. The propname of `NULL` indicates the end of the property
list.

Update an object’s properties

```c
  Error *err = NULL;
  Object *obj = ...get / create object...;

  if (!object_set_props(obj,
                        &err,
                        "share", "yes",
                        "mem-path", "/dev/shm/somefile",
                        "prealloc", "yes",
                        "size", "1048576",
                        NULL)) {
    error_reportf_err(err, "Cannot set properties: ");
  }
```

The returned object will have one stable reference maintained
for as long as it is present in the object hierarchy.

**Return**

`true` on success, `false` on error.

bool object_set_propv([Object](qom-api.md#c.Object "Object") \*obj, va_list vargs, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object instance to set properties on

`va_list vargs`
:   list of property names and values

`Error **errp`
:   pointer to error object

**Description**

See object_set_props() for documentation.

**Return**

`true` on success, `false` on error.

bool object_set_props_from_qdict([Object](qom-api.md#c.Object "Object") \*obj, const QDict \*qdict, Visitor \*v, Error \*\*errp)

**Parameters**

`Object *obj`
:   a QOM object

`const QDict *qdict`
:   a dictionary with the properties to be set

`Visitor *v`
:   a visitor to iterate over **dict**

`Error **errp`
:   pointer to error object

**Description**

For each key in the dictionary, set the corresponding
property in **obj**.

**Return**

`true` on success, `false` on error.

bool object_set_props_from_keyval([Object](qom-api.md#c.Object "Object") \*obj, const QDict \*qdict, bool from_json, Error \*\*errp)

**Parameters**

`Object *obj`
:   a QOM object

`const QDict *qdict`
:   a dictionary with the properties to be set

`bool from_json`
:   true if leaf values of **qdict** are typed, false if they
    are strings

`Error **errp`
:   pointer to error object

**Description**

For each key in the dictionary, parse the value string if needed,
then set the corresponding property in **obj**.

**Return**

`true` on success, `false` on error.

void object_initialize(void \*obj, size_t size, const char \*typename)

**Parameters**

`void *obj`
:   A pointer to the memory to be used for the object.

`size_t size`
:   The maximum size available at **obj** for the object.

`const char *typename`
:   The name of the type of the object to instantiate.

**Description**

This function will initialize an object. The memory for the object should
have already been allocated. The returned object has a reference count of 1,
and will be finalized when the last reference is dropped.

bool object_initialize_child_with_props([Object](qom-api.md#c.Object "Object") \*parentobj, const char \*propname, void \*childobj, size_t size, const char \*type, Error \*\*errp, ...)

**Parameters**

`Object *parentobj`
:   The parent object to add a property to

`const char *propname`
:   The name of the property

`void *childobj`
:   A pointer to the memory to be used for the object.

`size_t size`
:   The maximum size available at **childobj** for the object.

`const char *type`
:   The name of the type of the object to instantiate.

`Error **errp`
:   If an error occurs, a pointer to an area to store the error

`...`
:   list of property names and values

**Description**

This function will initialize an object. The memory for the object should
have already been allocated. The object will then be added as child property
to a parent with object_property_add_child() function. The returned object
has a reference count of 1 (for the “child<…>” property from the parent),
so the object will be finalized automatically when the parent gets removed.

The variadic parameters are a list of pairs of (propname, propvalue)
strings. The propname of `NULL` indicates the end of the property list.
If the object implements the user creatable interface, the object will
be marked complete once all the properties have been processed.

**Return**

`true` on success, `false` on failure.

bool object_initialize_child_with_propsv([Object](qom-api.md#c.Object "Object") \*parentobj, const char \*propname, void \*childobj, size_t size, const char \*type, Error \*\*errp, va_list vargs)

**Parameters**

`Object *parentobj`
:   The parent object to add a property to

`const char *propname`
:   The name of the property

`void *childobj`
:   A pointer to the memory to be used for the object.

`size_t size`
:   The maximum size available at **childobj** for the object.

`const char *type`
:   The name of the type of the object to instantiate.

`Error **errp`
:   If an error occurs, a pointer to an area to store the error

`va_list vargs`
:   list of property names and values

**Description**

See object_initialize_child() for documentation.

**Return**

`true` on success, `false` on failure.

object_initialize_child

`object_initialize_child (parent, propname, child, type)`

**Parameters**

`parent`
:   The parent object to add a property to

`propname`
:   The name of the property

`child`
:   A precisely typed pointer to the memory to be used for the
    object.

`type`
:   The name of the type of the object to instantiate.

**Description**

This is like:

```
object_initialize_child_with_props(parent, propname,
                                   child, sizeof(*child), type,
                                   &error_abort, NULL)
```

[Object](qom-api.md#c.Object "Object") \*object_dynamic_cast([Object](qom-api.md#c.Object "Object") \*obj, const char \*typename)

**Parameters**

`Object *obj`
:   The object to cast.

`const char *typename`
:   The **typename** to cast to.

**Description**

This function will determine if **obj** is-a **typename**. **obj** can refer to an
object or an interface associated with an object.

**Return**

This function returns **obj** on success or `NULL` on failure.

[Object](qom-api.md#c.Object "Object") \*object_dynamic_cast_assert([Object](qom-api.md#c.Object "Object") \*obj, const char \*typename, const char \*file, int line, const char \*func)

**Parameters**

`Object *obj`
:   The object to cast.

`const char *typename`
:   The **typename** to cast to.

`const char *file`
:   Source code file where function was called

`int line`
:   Source code line where function was called

`const char *func`
:   Name of function where this function was called

**Description**

See object_dynamic_cast() for a description of the parameters of this
function. The only difference in behavior is that this function asserts
instead of returning `NULL` on failure if QOM cast debugging is enabled.
This function is not meant to be called directly, but only through
the wrapper macro OBJECT_CHECK.

[ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*object_get_class([Object](qom-api.md#c.Object "Object") \*obj)

**Parameters**

`Object *obj`
:   A derivative of [`Object`](qom-api.md#c.Object "Object")

**Return**

The [`ObjectClass`](qom-api.md#c.ObjectClass "ObjectClass") of the type associated with **obj**.

const char \*object_get_typename(const [Object](qom-api.md#c.Object "Object") \*obj)

**Parameters**

`const Object *obj`
:   A derivative of [`Object`](qom-api.md#c.Object "Object").

**Return**

The QOM typename of **obj**.

Type type_register_static(const [TypeInfo](qom-api.md#c.TypeInfo "TypeInfo") \*info)

**Parameters**

`const TypeInfo *info`
:   The [`TypeInfo`](qom-api.md#c.TypeInfo "TypeInfo") of the new type.

**Return**

the new `Type`.

void type_register_static_array(const [TypeInfo](qom-api.md#c.TypeInfo "TypeInfo") \*infos, int nr_infos)

**Parameters**

`const TypeInfo *infos`
:   The array of the new type [`TypeInfo`](qom-api.md#c.TypeInfo "TypeInfo") structures.

`int nr_infos`
:   number of entries in **infos**

**Description**

**infos** and all of the strings it points to should exist for the life time
that the type is registered.

DEFINE_TYPES

`DEFINE_TYPES (type_array)`

**Parameters**

`type_array`
:   The array containing [`TypeInfo`](qom-api.md#c.TypeInfo "TypeInfo") structures to register

**Description**

**type_array** should be static constant that exists for the life time
that the type is registered.

bool type_print_class_properties(const char \*type)

**Parameters**

`const char *type`
:   a QOM class name

**Description**

Print the object’s class properties to stdout or the monitor.
Return whether an object was found.

[ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*object_class_dynamic_cast_assert([ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*klass, const char \*typename, const char \*file, int line, const char \*func)

**Parameters**

`ObjectClass *klass`
:   The [`ObjectClass`](qom-api.md#c.ObjectClass "ObjectClass") to attempt to cast.

`const char *typename`
:   The QOM typename of the class to cast to.

`const char *file`
:   Source code file where function was called

`int line`
:   Source code line where function was called

`const char *func`
:   Name of function where this function was called

**Description**

See object_class_dynamic_cast() for a description of the parameters
of this function. The only difference in behavior is that this function
asserts instead of returning `NULL` on failure if QOM cast debugging is
enabled. This function is not meant to be called directly, but only through
the wrapper macro OBJECT_CLASS_CHECK.

[ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*object_class_dynamic_cast([ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*klass, const char \*typename)

**Parameters**

`ObjectClass *klass`
:   The [`ObjectClass`](qom-api.md#c.ObjectClass "ObjectClass") to attempt to cast.

`const char *typename`
:   The QOM typename of the class to cast to.

**Return**

If **typename** is a class, this function returns **klass** if
**typename** is a subtype of **klass**, else returns `NULL`.

**Description**

If **typename** is an interface, this function returns the interface
definition for **klass** if **klass** implements it unambiguously; `NULL`
is returned if **klass** does not implement the interface or if multiple
classes or interfaces on the hierarchy leading to **klass** implement
it. (FIXME: perhaps this can be detected at type definition time?)

[ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*object_class_get_parent([ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*klass)

**Parameters**

`ObjectClass *klass`
:   The class to obtain the parent for.

**Return**

The parent for **klass** or `NULL` if none.

const char \*object_class_get_name([ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*klass)

**Parameters**

`ObjectClass *klass`
:   The class to obtain the QOM typename for.

**Return**

The QOM typename for **klass**.

bool object_class_is_abstract([ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*klass)

**Parameters**

`ObjectClass *klass`
:   The class to obtain the abstractness for.

**Return**

`true` if **klass** is abstract, `false` otherwise.

[ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*object_class_by_name(const char \*typename)

**Parameters**

`const char *typename`
:   The QOM typename to obtain the class for.

**Return**

The class for **typename** or `NULL` if not found.

[ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*module_object_class_by_name(const char \*typename)

**Parameters**

`const char *typename`
:   The QOM typename to obtain the class for.

**Description**

For objects which might be provided by a module. Behaves like
object_class_by_name, but additionally tries to load the module
needed in case the class is not available.

**Return**

The class for **typename** or `NULL` if not found.

GSList \*object_class_get_list(const char \*implements_type, bool include_abstract)

**Parameters**

`const char *implements_type`
:   The type to filter for, including its derivatives.

`bool include_abstract`
:   Whether to include abstract classes.

**Return**

A singly-linked list of the classes in reverse hashtable order.

GSList \*object_class_get_list_sorted(const char \*implements_type, bool include_abstract)

**Parameters**

`const char *implements_type`
:   The type to filter for, including its derivatives.

`bool include_abstract`
:   Whether to include abstract classes.

**Return**

A singly-linked list of the classes in alphabetical
case-insensitive order.

[Object](qom-api.md#c.Object "Object") \*object_ref(void \*obj)

**Parameters**

`void *obj`
:   the object

**Description**

Increase the reference count of a object. A object cannot be freed as long
as its reference count is greater than zero.

**Return**

**obj**

void object_unref(void \*obj)

**Parameters**

`void *obj`
:   the object

**Description**

Decrease the reference count of a object. A object cannot be freed as long
as its reference count is greater than zero.

ObjectProperty \*object_property_try_add([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, const char \*type, [ObjectPropertyAccessor](qom-api.md#c.ObjectPropertyAccessor "ObjectPropertyAccessor") \*get, [ObjectPropertyAccessor](qom-api.md#c.ObjectPropertyAccessor "ObjectPropertyAccessor") \*set, [ObjectPropertyRelease](qom-api.md#c.ObjectPropertyRelease "ObjectPropertyRelease") \*release, void \*opaque, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object to add a property to

`const char *name`
:   the name of the property. This can contain any character except for
    a forward slash. In general, you should use hyphens ‘-’ instead of
    underscores ‘_’ when naming properties.

`const char *type`
:   the type name of the property. This namespace is pretty loosely
    defined. Sub namespaces are constructed by using a prefix and then
    to angle brackets. For instance, the type ‘virtio-net-pci’ in the
    ‘link’ namespace would be ‘link<virtio-net-pci>’.

`ObjectPropertyAccessor *get`
:   The getter to be called to read a property. If this is NULL, then
    the property cannot be read.

`ObjectPropertyAccessor *set`
:   the setter to be called to write a property. If this is NULL,
    then the property cannot be written.

`ObjectPropertyRelease *release`
:   called when the property is removed from the object. This is
    meant to allow a property to free its opaque upon object
    destruction. This may be NULL.

`void *opaque`
:   an opaque pointer to pass to the callbacks for the property

`Error **errp`
:   pointer to error object

**Return**

The `ObjectProperty`; this can be used to set the **resolve**
callback for child and link properties.

ObjectProperty \*object_property_add([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, const char \*type, [ObjectPropertyAccessor](qom-api.md#c.ObjectPropertyAccessor "ObjectPropertyAccessor") \*get, [ObjectPropertyAccessor](qom-api.md#c.ObjectPropertyAccessor "ObjectPropertyAccessor") \*set, [ObjectPropertyRelease](qom-api.md#c.ObjectPropertyRelease "ObjectPropertyRelease") \*release, void \*opaque)
:   Same as object_property_try_add() with **errp** hardcoded to &error_abort.

**Parameters**

`Object *obj`
:   the object to add a property to

`const char *name`
:   the name of the property. This can contain any character except for
    a forward slash. In general, you should use hyphens ‘-’ instead of
    underscores ‘_’ when naming properties.

`const char *type`
:   the type name of the property. This namespace is pretty loosely
    defined. Sub namespaces are constructed by using a prefix and then
    to angle brackets. For instance, the type ‘virtio-net-pci’ in the
    ‘link’ namespace would be ‘link<virtio-net-pci>’.

`ObjectPropertyAccessor *get`
:   The getter to be called to read a property. If this is NULL, then
    the property cannot be read.

`ObjectPropertyAccessor *set`
:   the setter to be called to write a property. If this is NULL,
    then the property cannot be written.

`ObjectPropertyRelease *release`
:   called when the property is removed from the object. This is
    meant to allow a property to free its opaque upon object
    destruction. This may be NULL.

`void *opaque`
:   an opaque pointer to pass to the callbacks for the property

void object_property_set_default_bool(ObjectProperty \*prop, bool value)

**Parameters**

`ObjectProperty *prop`
:   the property to set

`bool value`
:   the value to be written to the property

**Description**

Set the property default value.

void object_property_set_default_str(ObjectProperty \*prop, const char \*value)

**Parameters**

`ObjectProperty *prop`
:   the property to set

`const char *value`
:   the value to be written to the property

**Description**

Set the property default value.

void object_property_set_default_list(ObjectProperty \*prop)

**Parameters**

`ObjectProperty *prop`
:   the property to set

**Description**

Set the property default value to be an empty list.

void object_property_set_default_int(ObjectProperty \*prop, int64_t value)

**Parameters**

`ObjectProperty *prop`
:   the property to set

`int64_t value`
:   the value to be written to the property

**Description**

Set the property default value.

void object_property_set_default_uint(ObjectProperty \*prop, uint64_t value)

**Parameters**

`ObjectProperty *prop`
:   the property to set

`uint64_t value`
:   the value to be written to the property

**Description**

Set the property default value.

ObjectProperty \*object_property_find([Object](qom-api.md#c.Object "Object") \*obj, const char \*name)

**Parameters**

`Object *obj`
:   the object

`const char *name`
:   the name of the property

**Description**

Look up a property for an object.

Return its `ObjectProperty` if found, or NULL.

ObjectProperty \*object_property_find_err([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object

`const char *name`
:   the name of the property

`Error **errp`
:   returns an error if this function fails

**Description**

Look up a property for an object.

Return its `ObjectProperty` if found, or NULL.

ObjectProperty \*object_class_property_find([ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*klass, const char \*name)

**Parameters**

`ObjectClass *klass`
:   the object class

`const char *name`
:   the name of the property

**Description**

Look up a property for an object class.

Return its `ObjectProperty` if found, or NULL.

ObjectProperty \*object_class_property_find_err([ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*klass, const char \*name, Error \*\*errp)

**Parameters**

`ObjectClass *klass`
:   the object class

`const char *name`
:   the name of the property

`Error **errp`
:   returns an error if this function fails

**Description**

Look up a property for an object class.

Return its `ObjectProperty` if found, or NULL.

void object_property_iter_init(ObjectPropertyIterator \*iter, [Object](qom-api.md#c.Object "Object") \*obj)

**Parameters**

`ObjectPropertyIterator *iter`
:   the iterator instance

`Object *obj`
:   the object

**Description**

Initializes an iterator for traversing all properties
registered against an object instance, its class and all parent classes.

It is forbidden to modify the property list while iterating,
whether removing or adding properties.

Typical usage pattern would be

Using object property iterators

```c
  ObjectProperty *prop;
  ObjectPropertyIterator iter;

  object_property_iter_init(&iter, obj);
  while ((prop = object_property_iter_next(&iter))) {
    ... do something with prop ...
  }
```

void object_class_property_iter_init(ObjectPropertyIterator \*iter, [ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*klass)

**Parameters**

`ObjectPropertyIterator *iter`
:   the iterator instance

`ObjectClass *klass`
:   the class

**Description**

Initializes an iterator for traversing all properties
registered against an object class and all parent classes.

It is forbidden to modify the property list while iterating,
whether removing or adding properties.

This can be used on abstract classes as it does not create a temporary
instance.

ObjectProperty \*object_property_iter_next(ObjectPropertyIterator \*iter)

**Parameters**

`ObjectPropertyIterator *iter`
:   the iterator instance

**Description**

Return the next available property. If no further properties
are available, a `NULL` value will be returned and the **iter**
pointer should not be used again after this point without
re-initializing it.

**Return**

the next property, or `NULL` when all properties
have been traversed.

bool object_property_get([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, Visitor \*v, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object

`const char *name`
:   the name of the property

`Visitor *v`
:   the visitor that will receive the property value. This should be an
    Output visitor and the data will be written with **name** as the name.

`Error **errp`
:   returns an error if this function fails

**Description**

Reads a property from a object.

**Return**

`true` on success, `false` on failure.

bool object_property_set_str([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, const char \*value, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object

`const char *name`
:   the name of the property

`const char *value`
:   the value to be written to the property

`Error **errp`
:   returns an error if this function fails

**Description**

Writes a string value to a property.

**Return**

`true` on success, `false` on failure.

char \*object_property_get_str([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object

`const char *name`
:   the name of the property

`Error **errp`
:   returns an error if this function fails

**Return**

the value of the property, converted to a C string, or NULL if
an error occurs (including when the property value is not a string).
The caller should free the string.

bool object_property_set_link([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, [Object](qom-api.md#c.Object "Object") \*value, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object

`const char *name`
:   the name of the property

`Object *value`
:   the value to be written to the property

`Error **errp`
:   returns an error if this function fails

**Description**

Writes an object’s canonical path to a property.

If the link property was created with
`OBJ_PROP_LINK_STRONG` bit, the old target object is
unreferenced, and a reference is added to the new target object.

**Return**

`true` on success, `false` on failure.

[Object](qom-api.md#c.Object "Object") \*object_property_get_link([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object

`const char *name`
:   the name of the property

`Error **errp`
:   returns an error if this function fails

**Return**

the value of the property, resolved from a path to an Object,
or NULL if an error occurs (including when the property value is not a
string or not a valid object path).

bool object_property_set_bool([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, bool value, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object

`const char *name`
:   the name of the property

`bool value`
:   the value to be written to the property

`Error **errp`
:   returns an error if this function fails

**Description**

Writes a bool value to a property.

**Return**

`true` on success, `false` on failure.

bool object_property_get_bool([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object

`const char *name`
:   the name of the property

`Error **errp`
:   returns an error if this function fails

**Return**

the value of the property, converted to a boolean, or false if
an error occurs (including when the property value is not a bool).

bool object_property_set_int([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, int64_t value, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object

`const char *name`
:   the name of the property

`int64_t value`
:   the value to be written to the property

`Error **errp`
:   returns an error if this function fails

**Description**

Writes an integer value to a property.

**Return**

`true` on success, `false` on failure.

int64_t object_property_get_int([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object

`const char *name`
:   the name of the property

`Error **errp`
:   returns an error if this function fails

**Return**

the value of the property, converted to an integer, or -1 if
an error occurs (including when the property value is not an integer).

bool object_property_set_uint([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, uint64_t value, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object

`const char *name`
:   the name of the property

`uint64_t value`
:   the value to be written to the property

`Error **errp`
:   returns an error if this function fails

**Description**

Writes an unsigned integer value to a property.

**Return**

`true` on success, `false` on failure.

uint64_t object_property_get_uint([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object

`const char *name`
:   the name of the property

`Error **errp`
:   returns an error if this function fails

**Return**

the value of the property, converted to an unsigned integer, or 0
an error occurs (including when the property value is not an integer).

int object_property_get_enum([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, const char \*typename, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object

`const char *name`
:   the name of the property

`const char *typename`
:   the name of the enum data type

`Error **errp`
:   returns an error if this function fails

**Return**

the value of the property, converted to an integer (which
can’t be negative), or -1 on error (including when the property
value is not an enum).

bool object_property_set([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, Visitor \*v, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object

`const char *name`
:   the name of the property

`Visitor *v`
:   the visitor that will be used to write the property value. This should
    be an Input visitor and the data will be first read with **name** as the
    name and then written as the property value.

`Error **errp`
:   returns an error if this function fails

**Description**

Writes a property to a object.

**Return**

`true` on success, `false` on failure.

bool object_property_parse([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, const char \*string, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object

`const char *name`
:   the name of the property

`const char *string`
:   the string that will be used to parse the property value.

`Error **errp`
:   returns an error if this function fails

**Description**

Parses a string and writes the result into a property of an object.

**Return**

`true` on success, `false` on failure.

char \*object_property_print([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, bool human, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object

`const char *name`
:   the name of the property

`bool human`
:   if true, print for human consumption

`Error **errp`
:   returns an error if this function fails

**Description**

Returns a string representation of the value of the property. The
caller shall free the string.

const char \*object_property_get_type([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object

`const char *name`
:   the name of the property

`Error **errp`
:   returns an error if this function fails

**Return**

The type name of the property.

[Object](qom-api.md#c.Object "Object") \*object_get_root(void)

**Parameters**

`void`
:   no arguments

**Return**

the root object of the composition tree

[Object](qom-api.md#c.Object "Object") \*object_get_container(const char \*name)

**Parameters**

`const char *name`
:   the name of container to lookup

**Description**

Lookup a root level container.

**Return**

the container with **name**.

[Object](qom-api.md#c.Object "Object") \*object_get_objects_root(void)

**Parameters**

`void`
:   no arguments

**Description**

Get the container object that holds user created
object instances. This is the object at path
“/objects”

**Return**

the user object container

[Object](qom-api.md#c.Object "Object") \*object_get_internal_root(void)

**Parameters**

`void`
:   no arguments

**Description**

Get the container object that holds internally used object
instances. Any object which is put into this container must not be
user visible, and it will not be exposed in the QOM tree.

**Return**

the internal object container

const char \*object_get_canonical_path_component(const [Object](qom-api.md#c.Object "Object") \*obj)

**Parameters**

`const Object *obj`
:   the object

**Return**

The final component in the object’s canonical path. The canonical
path is the path within the composition tree starting from the root.
`NULL` if the object doesn’t have a parent (and thus a canonical path).

char \*object_get_canonical_path(const [Object](qom-api.md#c.Object "Object") \*obj)

**Parameters**

`const Object *obj`
:   the object

**Return**

The canonical path for a object, newly allocated. This is
the path within the composition tree starting from the root. Use
g_free() to free it.

[Object](qom-api.md#c.Object "Object") \*object_resolve_path(const char \*path, bool \*ambiguous)

**Parameters**

`const char *path`
:   the path to resolve

`bool *ambiguous`
:   (out) (optional): location to store whether the lookup failed
    because it was ambiguous, or `NULL`. Set to `false` on success.

**Description**

There are two types of supported paths–absolute paths and partial paths.

Absolute paths are derived from the root object and can follow child<> or
link<> properties. Since they can follow link<> properties, they can be
arbitrarily long. Absolute paths look like absolute filenames and are
prefixed with a leading slash.

Partial paths look like relative filenames. They do not begin with a
prefix. The matching rules for partial paths are subtle but designed to make
specifying objects easy. At each level of the composition tree, the partial
path is matched as an absolute path. The first match is not returned. At
least two matches are searched for. A successful result is only returned if
only one match is found. If more than one match is found, a flag is
returned to indicate that the match was ambiguous.

**Return**

The matched object or `NULL` on path lookup failure.

[Object](qom-api.md#c.Object "Object") \*object_resolve_path_type(const char \*path, const char \*typename, bool \*ambiguous)

**Parameters**

`const char *path`
:   the path to resolve

`const char *typename`
:   the type to look for.

`bool *ambiguous`
:   (out) (optional): location to store whether the lookup failed
    because it was ambiguous, or `NULL`. Set to `false` on success.

**Description**

This is similar to object_resolve_path(). However, when looking for a
partial path only matches that implement the given type are considered.
This restricts the search and avoids spuriously flagging matches as
ambiguous.

For both partial and absolute paths, the return value goes through
a dynamic cast to **typename**. This is important if either the link,
or the typename itself are of interface types.

**Return**

The matched object or NULL on path lookup failure.

[Object](qom-api.md#c.Object "Object") \*object_resolve_type_unambiguous(const char \*typename, Error \*\*errp)

**Parameters**

`const char *typename`
:   the type to look for

`Error **errp`
:   pointer to error object

**Description**

Return the only object in the QOM tree of type **typename**.
If no match or more than one match is found, an error is
returned.

**Return**

The matched object or NULL on path lookup failure.

[Object](qom-api.md#c.Object "Object") \*object_resolve_path_at([Object](qom-api.md#c.Object "Object") \*parent, const char \*path)

**Parameters**

`Object *parent`
:   the object in which to resolve the path

`const char *path`
:   the path to resolve

**Description**

This is like object_resolve_path(), except paths not starting with
a slash are relative to **parent**.

**Return**

The resolved object or NULL on path lookup failure.

[Object](qom-api.md#c.Object "Object") \*object_resolve_path_component([Object](qom-api.md#c.Object "Object") \*parent, const char \*part)

**Parameters**

`Object *parent`
:   the object in which to resolve the path

`const char *part`
:   the component to resolve.

**Description**

This is similar to object_resolve_path with an absolute path, but it
only resolves one element (**part**) and takes the others from **parent**.

**Return**

The resolved object or NULL on path lookup failure.

ObjectProperty \*object_property_try_add_child([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, [Object](qom-api.md#c.Object "Object") \*child, Error \*\*errp)

**Parameters**

`Object *obj`
:   the object to add a property to

`const char *name`
:   the name of the property

`Object *child`
:   the child object

`Error **errp`
:   pointer to error object

**Description**

Child properties form the composition tree. All objects need to be a child
of another object. Objects can only be a child of one object.

There is no way for a child to determine what its parent is. It is not
a bidirectional relationship. This is by design.

The value of a child property as a C string will be the child object’s
canonical path. It can be retrieved using object_property_get_str().
The child object itself can be retrieved using object_property_get_link().

**Return**

The newly added property on success, or `NULL` on failure.

ObjectProperty \*object_property_add_child([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, [Object](qom-api.md#c.Object "Object") \*child)

**Parameters**

`Object *obj`
:   the object to add a property to

`const char *name`
:   the name of the property

`Object *child`
:   the child object

**Description**

Same as object_property_try_add_child() with **errp** hardcoded to
&error_abort

void object_property_allow_set_link(const [Object](qom-api.md#c.Object "Object") \*obj, const char \*name, [Object](qom-api.md#c.Object "Object") \*child, Error \*\*errp)

**Parameters**

`const Object *obj`
:   the object to add a property to

`const char *name`
:   the name of the property

`Object *child`
:   the child object

`Error **errp`
:   pointer to error object

**Description**

The default implementation of the object_property_add_link() check()
callback function. It allows the link property to be set and never returns
an error.

ObjectProperty \*object_property_add_link([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, const char \*type, [Object](qom-api.md#c.Object "Object") \*\*targetp, void (\*check)(const [Object](qom-api.md#c.Object "Object") \*obj, const char \*name, [Object](qom-api.md#c.Object "Object") \*val, Error \*\*errp), ObjectPropertyLinkFlags flags)

**Parameters**

`Object *obj`
:   the object to add a property to

`const char *name`
:   the name of the property

`const char *type`
:   the qobj type of the link

`Object **targetp`
:   a pointer to where the link object reference is stored

`void (*check)(const Object *obj, const char *name, Object *val, Error **errp)`
:   callback to veto setting or NULL if the property is read-only

`ObjectPropertyLinkFlags flags`
:   additional options for the link

**Description**

Links establish relationships between objects. Links are unidirectional
although two links can be combined to form a bidirectional relationship
between objects.

Links form the graph in the object model.

The **check()** callback is invoked when object_property_set_link() is called
and can raise an error to prevent the link being set. If **check** is NULL, the
property is read-only and cannot be set. Care must be taken to handle NULL
values for **val**.

Ownership of the pointer that **targetp** points to is transferred to the
link property. The reference count for **\*targetp** is
managed by the property from after the function returns till the
property is deleted with object_property_del(). If the
**flags** `OBJ_PROP_LINK_STRONG` bit is set,
the reference count is decremented when the property is deleted or
modified.

**Return**

The newly added property on success, or `NULL` on failure.

ObjectProperty \*object_class_property_add_link([ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*oc, const char \*name, const char \*type, ptrdiff_t offset, void (\*check)(const [Object](qom-api.md#c.Object "Object") \*obj, const char \*name, [Object](qom-api.md#c.Object "Object") \*val, Error \*\*errp), ObjectPropertyLinkFlags flags)

**Parameters**

`ObjectClass *oc`
:   the object class to add a property to

`const char *name`
:   the name of the property

`const char *type`
:   the qobj type of the link

`ptrdiff_t offset`
:   the offset from the object instance where the link object reference
    is stored

`void (*check)(const Object *obj, const char *name, Object *val, Error **errp)`
:   callback to veto setting or NULL if the property is read-only

`ObjectPropertyLinkFlags flags`
:   additional options for the link

**Description**

Links establish relationships between objects. Links are unidirectional
although two links can be combined to form a bidirectional relationship
between objects.

Links form the graph in the object model.

The **check()** callback is invoked when object_property_set_link() is called
and can raise an error to prevent the link being set. If **check** is NULL, the
property is read-only and cannot be set. Care must be taken to handle NULL
values for **val**.

If the **flags** `OBJ_PROP_LINK_STRONG` bit is set, the reference count of the
linked object is incremented when the property is set, and decremented again
when the property is modified.

**Return**

The newly added property on success, or `NULL` on failure.

[Object](qom-api.md#c.Object "Object") \*object_resolve_and_typecheck(const char \*path, const char \*name, const char \*target_type, Error \*\*errp)

**Parameters**

`const char *path`
:   path to look up

`const char *name`
:   name of property we are resolving for (used only in error messages)

`const char *target_type`
:   QOM type we expect **path** to resolve to

`Error **errp`
:   error

**Description**

Look up the object at **path** and return it. If it does not have the
correct type **target_type**, return NULL and set **errp**.

This is similar to object_resolve_path_type(), but it insists on a
non-ambiguous path and it produces error messages that are
specialised to the use case of setting a link property on an object.

ObjectProperty \*object_property_add_str([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, char \*(\*get)([Object](qom-api.md#c.Object "Object")\*, Error\*\*), void (\*set)([Object](qom-api.md#c.Object "Object")\*, const char\*, Error\*\*))

**Parameters**

`Object *obj`
:   the object to add a property to

`const char *name`
:   the name of the property

`char *(*get)(Object *, Error **)`
:   the getter or NULL if the property is write-only. This function must
    return a string to be freed by g_free().

`void (*set)(Object *, const char *, Error **)`
:   the setter or NULL if the property is read-only

**Description**

Add a string property using getters/setters. This function will add a
property of type ‘string’.

**Return**

The newly added property on success, or `NULL` on failure.

ObjectProperty \*object_class_property_add_str([ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*klass, const char \*name, char \*(\*get)([Object](qom-api.md#c.Object "Object")\*, Error\*\*), void (\*set)([Object](qom-api.md#c.Object "Object")\*, const char\*, Error\*\*))

**Parameters**

`ObjectClass *klass`
:   the object class to add a property to

`const char *name`
:   the name of the property

`char *(*get)(Object *, Error **)`
:   the getter or NULL if the property is write-only. This function must
    return a string to be freed by g_free().

`void (*set)(Object *, const char *, Error **)`
:   the setter or NULL if the property is read-only

**Description**

Add a string property using getters/setters. This function will add a
property of type ‘string’.

**Return**

The newly added property on success, or `NULL` on failure.

ObjectProperty \*object_property_add_bool([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, bool (\*get)([Object](qom-api.md#c.Object "Object")\*, Error\*\*), void (\*set)([Object](qom-api.md#c.Object "Object")\*, bool, Error\*\*))

**Parameters**

`Object *obj`
:   the object to add a property to

`const char *name`
:   the name of the property

`bool (*get)(Object *, Error **)`
:   the getter or NULL if the property is write-only.

`void (*set)(Object *, bool, Error **)`
:   the setter or NULL if the property is read-only

**Description**

Add a bool property using getters/setters. This function will add a
property of type ‘bool’.

**Return**

The newly added property on success, or `NULL` on failure.

ObjectProperty \*object_class_property_add_bool([ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*klass, const char \*name, bool (\*get)([Object](qom-api.md#c.Object "Object")\*, Error\*\*), void (\*set)([Object](qom-api.md#c.Object "Object")\*, bool, Error\*\*))

**Parameters**

`ObjectClass *klass`
:   the object class to add a property to

`const char *name`
:   the name of the property

`bool (*get)(Object *, Error **)`
:   the getter or NULL if the property is write-only.

`void (*set)(Object *, bool, Error **)`
:   the setter or NULL if the property is read-only

**Description**

Add a bool property using getters/setters. This function will add a
property of type ‘bool’.

**Return**

The newly added property on success, or `NULL` on failure.

ObjectProperty \*object_property_add_enum([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, const char \*typename, const QEnumLookup \*lookup, int (\*get)([Object](qom-api.md#c.Object "Object")\*, Error\*\*), void (\*set)([Object](qom-api.md#c.Object "Object")\*, int, Error\*\*))

**Parameters**

`Object *obj`
:   the object to add a property to

`const char *name`
:   the name of the property

`const char *typename`
:   the name of the enum data type

`const QEnumLookup *lookup`
:   enum value namelookup table

`int (*get)(Object *, Error **)`
:   the getter or `NULL` if the property is write-only.

`void (*set)(Object *, int, Error **)`
:   the setter or `NULL` if the property is read-only

**Description**

Add an enum property using getters/setters. This function will add a
property of type ‘**typename**’.

**Return**

The newly added property on success, or `NULL` on failure.

ObjectProperty \*object_class_property_add_enum([ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*klass, const char \*name, const char \*typename, const QEnumLookup \*lookup, int (\*get)([Object](qom-api.md#c.Object "Object")\*, Error\*\*), void (\*set)([Object](qom-api.md#c.Object "Object")\*, int, Error\*\*))

**Parameters**

`ObjectClass *klass`
:   the object class to add a property to

`const char *name`
:   the name of the property

`const char *typename`
:   the name of the enum data type

`const QEnumLookup *lookup`
:   enum value namelookup table

`int (*get)(Object *, Error **)`
:   the getter or `NULL` if the property is write-only.

`void (*set)(Object *, int, Error **)`
:   the setter or `NULL` if the property is read-only

**Description**

Add an enum property using getters/setters. This function will add a
property of type ‘**typename**’.

**Return**

The newly added property on success, or `NULL` on failure.

ObjectProperty \*object_property_add_tm([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, void (\*get)([Object](qom-api.md#c.Object "Object")\*, struct tm\*, Error\*\*))

**Parameters**

`Object *obj`
:   the object to add a property to

`const char *name`
:   the name of the property

`void (*get)(Object *, struct tm *, Error **)`
:   the getter or NULL if the property is write-only.

**Description**

Add a read-only struct tm valued property using a getter function.
This function will add a property of type ‘struct tm’.

**Return**

The newly added property on success, or `NULL` on failure.

ObjectProperty \*object_class_property_add_tm([ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*klass, const char \*name, void (\*get)([Object](qom-api.md#c.Object "Object")\*, struct tm\*, Error\*\*))

**Parameters**

`ObjectClass *klass`
:   the object class to add a property to

`const char *name`
:   the name of the property

`void (*get)(Object *, struct tm *, Error **)`
:   the getter or NULL if the property is write-only.

**Description**

Add a read-only struct tm valued property using a getter function.
This function will add a property of type ‘struct tm’.

**Return**

The newly added property on success, or `NULL` on failure.

ObjectProperty \*object_property_add_uint8_ptr([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, const uint8_t \*v, ObjectPropertyFlags flags)

**Parameters**

`Object *obj`
:   the object to add a property to

`const char *name`
:   the name of the property

`const uint8_t *v`
:   pointer to value

`ObjectPropertyFlags flags`
:   bitwise-or’d ObjectPropertyFlags

**Description**

Add an integer property in memory. This function will add a
property of type ‘uint8’.

**Return**

The newly added property on success, or `NULL` on failure.

ObjectProperty \*object_class_static_property_add_uint8_ptr([ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*klass, const char \*name, const uint8_t \*v, ObjectPropertyFlags flags)

**Parameters**

`ObjectClass *klass`
:   the object class to add a static property to

`const char *name`
:   the name of the property

`const uint8_t *v`
:   pointer to value

`ObjectPropertyFlags flags`
:   bitwise-or’d ObjectPropertyFlags

**Description**

Add a static integer property in memory. This function will add a
property of type ‘uint8’.

A static property is one which is stored outside of the object instance,
typically in global variables. It is only appropriate to use static
properties when the class is designed as a singleton. If there is a
possibility of multiple instances, then properties must be stored
per-instance.

**Return**

The newly added property on success, or `NULL` on failure.

ObjectProperty \*object_property_add_uint16_ptr([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, const uint16_t \*v, ObjectPropertyFlags flags)

**Parameters**

`Object *obj`
:   the object to add a property to

`const char *name`
:   the name of the property

`const uint16_t *v`
:   pointer to value

`ObjectPropertyFlags flags`
:   bitwise-or’d ObjectPropertyFlags

**Description**

Add an integer property in memory. This function will add a
property of type ‘uint16’.

**Return**

The newly added property on success, or `NULL` on failure.

ObjectProperty \*object_class_static_property_add_uint16_ptr([ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*klass, const char \*name, const uint16_t \*v, ObjectPropertyFlags flags)

**Parameters**

`ObjectClass *klass`
:   the object class to add a static property to

`const char *name`
:   the name of the property

`const uint16_t *v`
:   pointer to value

`ObjectPropertyFlags flags`
:   bitwise-or’d ObjectPropertyFlags

**Description**

Add a static integer property in memory. This function will add a
property of type ‘uint16’.

A static property is one which is stored outside of the object instance,
typically in global variables. It is only appropriate to use static
properties when the class is designed as a singleton. If there is a
possibility of multiple instances, then properties must be stored
per-instance.

**Return**

The newly added property on success, or `NULL` on failure.

ObjectProperty \*object_property_add_uint32_ptr([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, const uint32_t \*v, ObjectPropertyFlags flags)

**Parameters**

`Object *obj`
:   the object to add a property to

`const char *name`
:   the name of the property

`const uint32_t *v`
:   pointer to value

`ObjectPropertyFlags flags`
:   bitwise-or’d ObjectPropertyFlags

**Description**

Add an integer property in memory. This function will add a
property of type ‘uint32’.

**Return**

The newly added property on success, or `NULL` on failure.

ObjectProperty \*object_class_static_property_add_uint32_ptr([ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*klass, const char \*name, const uint32_t \*v, ObjectPropertyFlags flags)

**Parameters**

`ObjectClass *klass`
:   the object class to add a static property to

`const char *name`
:   the name of the property

`const uint32_t *v`
:   pointer to value

`ObjectPropertyFlags flags`
:   bitwise-or’d ObjectPropertyFlags

**Description**

Add a static integer property in memory. This function will add a
property of type ‘uint32’.

A static property is one which is stored outside of the object instance,
typically in global variables. It is only appropriate to use static
properties when the class is designed as a singleton. If there is a
possibility of multiple instances, then properties must be stored
per-instance.

**Return**

The newly added property on success, or `NULL` on failure.

ObjectProperty \*object_property_add_uint64_ptr([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, const uint64_t \*v, ObjectPropertyFlags flags)

**Parameters**

`Object *obj`
:   the object to add a property to

`const char *name`
:   the name of the property

`const uint64_t *v`
:   pointer to value

`ObjectPropertyFlags flags`
:   bitwise-or’d ObjectPropertyFlags

**Description**

Add an integer property in memory. This function will add a
property of type ‘uint64’.

**Return**

The newly added property on success, or `NULL` on failure.

ObjectProperty \*object_class_static_property_add_uint64_ptr([ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*klass, const char \*name, const uint64_t \*v, ObjectPropertyFlags flags)

**Parameters**

`ObjectClass *klass`
:   the object class to add a static property to

`const char *name`
:   the name of the property

`const uint64_t *v`
:   pointer to value

`ObjectPropertyFlags flags`
:   bitwise-or’d ObjectPropertyFlags

**Description**

Add a static integer property in memory. This function will add a
property of type ‘uint64’.

A static property is one which is stored outside of the object instance,
typically in global variables. It is only appropriate to use static
properties when the class is designed as a singleton. If there is a
possibility of multiple instances, then properties must be stored
per-instance.

**Return**

The newly added property on success, or `NULL` on failure.

ObjectProperty \*object_property_add_alias([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, [Object](qom-api.md#c.Object "Object") \*target_obj, const char \*target_name)

**Parameters**

`Object *obj`
:   the object to add a property to

`const char *name`
:   the name of the property

`Object *target_obj`
:   the object to forward property access to

`const char *target_name`
:   the name of the property on the forwarded object

**Description**

Add an alias for a property on an object. This function will add a property
of the same type as the forwarded property.

The caller must ensure that **target_obj** stays alive as long as
this property exists. In the case of a child object or an alias on the same
object this will be the case. For aliases to other objects the caller is
responsible for taking a reference.

**Return**

The newly added property on success, or `NULL` on failure.

ObjectProperty \*object_property_add_const_link([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, [Object](qom-api.md#c.Object "Object") \*target)

**Parameters**

`Object *obj`
:   the object to add a property to

`const char *name`
:   the name of the property

`Object *target`
:   the object to be referred by the link

**Description**

Add an unmodifiable link for a property on an object. This function will
add a property of type link<TYPE> where TYPE is the type of **target**.

The caller must ensure that **target** stays alive as long as
this property exists. In the case **target** is a child of **obj**,
this will be the case. Otherwise, the caller is responsible for
taking a reference.

**Return**

The newly added property on success, or `NULL` on failure.

void object_property_set_description([Object](qom-api.md#c.Object "Object") \*obj, const char \*name, const char \*description)

**Parameters**

`Object *obj`
:   the object owning the property

`const char *name`
:   the name of the property

`const char *description`
:   the description of the property on the object

**Description**

Set an object property’s description.

**Return**

`true` on success, `false` on failure.

void object_class_property_set_description([ObjectClass](qom-api.md#c.ObjectClass "ObjectClass") \*klass, const char \*name, const char \*description)

**Parameters**

`ObjectClass *klass`
:   the object class owning the property

`const char *name`
:   the name of the property

`const char *description`
:   the description of the property on the object

**Description**

Set an object property’s description.

**Return**

`true` on success, `false` on failure.

int object_child_foreach([Object](qom-api.md#c.Object "Object") \*obj, int (\*fn)([Object](qom-api.md#c.Object "Object") \*child, void \*opaque), void \*opaque)

**Parameters**

`Object *obj`
:   the object whose children will be navigated

`int (*fn)(Object *child, void *opaque)`
:   the iterator function to be called

`void *opaque`
:   an opaque value that will be passed to the iterator

**Description**

Call **fn** passing each child of **obj** and **opaque** to it, until **fn** returns
non-zero.

It is forbidden to add or remove children from **obj** from the **fn**
callback.

**Return**

The last value returned by **fn**, or 0 if there is no child.

int object_child_foreach_recursive([Object](qom-api.md#c.Object "Object") \*obj, int (\*fn)([Object](qom-api.md#c.Object "Object") \*child, void \*opaque), void \*opaque)

**Parameters**

`Object *obj`
:   the object whose children will be navigated

`int (*fn)(Object *child, void *opaque)`
:   the iterator function to be called

`void *opaque`
:   an opaque value that will be passed to the iterator

**Description**

Call **fn** passing each child of **obj** and **opaque** to it, until **fn** returns
non-zero. Calls recursively, all child nodes of **obj** will also be passed
all the way down to the leaf nodes of the tree. Depth first ordering.

It is forbidden to add or remove children from **obj** (or its
child nodes) from the **fn** callback.

**Return**

The last value returned by **fn**, or 0 if there is no child.

[Object](qom-api.md#c.Object "Object") \*object_property_add_new_container([Object](qom-api.md#c.Object "Object") \*obj, const char \*name)

**Parameters**

`Object *obj`
:   the parent object

`const char *name`
:   the name of the parent object’s property to add

**Description**

Add a newly created container object to a parent object.

**Return**

the newly created container object. Its reference count is 1,
and the reference is owned by the parent object.

char \*object_property_help(const char \*name, const char \*type, QObject \*defval, const char \*description)

**Parameters**

`const char *name`
:   the name of the property

`const char *type`
:   the type of the property

`QObject *defval`
:   the default value

`const char *description`
:   description of the property

**Return**

a user-friendly formatted string describing the property
for help purposes.
