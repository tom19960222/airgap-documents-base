---
collection: kernel
version: "6.8"
title: "Writing Devicetree Bindings in json-schema"
source_url: https://www.kernel.org/doc/html/v6.8/devicetree/bindings/writing-schema.html
fetched_at: 2026-08-21T03:35:52+00:00
---
# Writing Devicetree Bindings in json-schema

Devicetree bindings are written using json-schema vocabulary. Schema files are
written in a JSON-compatible subset of YAML. YAML is used instead of JSON as it
is considered more human readable and has some advantages such as allowing
comments (Prefixed with '#').

Also see [Annotated Example Schema](writing-schema.md#example-schema).

## Schema Contents

Each schema doc is a structured json-schema which is defined by a set of
top-level properties. Generally, there is one binding defined per file. The
top-level json-schema properties used are:

$id
:   A json-schema unique identifier string. The string must be a valid
    URI typically containing the binding's filename and path. For DT schema, it must
    begin with "<http://devicetree.org/schemas/>". The URL is used in constructing
    references to other files specified in schema "$ref" properties. A $ref value
    with a leading '/' will have the hostname prepended. A $ref value with only a
    relative path or filename will be prepended with the hostname and path
    components of the current schema file's '$id' value. A URL is used even for
    local files, but there may not actually be files present at those locations.

$schema
:   Indicates the meta-schema the schema file adheres to.

title
:   A one-line description on the contents of the binding schema.

maintainers
:   A DT specific property. Contains a list of email address(es)
    for maintainers of this binding.

description
:   Optional. A multi-line text block containing any detailed
    information about this binding. It should contain things such as what the block
    or device does, standards the device conforms to, and links to datasheets for
    more information.

select
:   Optional. A json-schema used to match nodes for applying the
    schema. By default, without 'select', nodes are matched against their possible
    compatible-string values or node name. Most bindings should not need select.

allOf
:   Optional. A list of other schemas to include. This is used to
    include other schemas the binding conforms to. This may be schemas for a
    particular class of devices such as I2C or SPI controllers.

properties
:   A set of sub-schema defining all the DT properties for the
    binding. The exact schema syntax depends on whether properties are known,
    common properties (e.g. 'interrupts') or are binding/vendor-specific
    properties.

A property can also define a child DT node with child properties defined
under it.

For more details on properties sections, see 'Property Schema' section.

patternProperties
:   Optional. Similar to 'properties', but names are regex.

required
:   A list of DT properties from the 'properties' section that
    must always be present.

examples
:   Optional. A list of one or more DTS hunks implementing the
    binding. Note: YAML doesn't allow leading tabs, so spaces must be used instead.

Unless noted otherwise, all properties are required.

## Property Schema

The 'properties' section of the schema contains all the DT properties for a
binding. Each property contains a set of constraints using json-schema
vocabulary for that property. The properties schemas are what are used for
validation of DT files.

For common properties, only additional constraints not covered by the common,
binding schema need to be defined such as how many values are valid or what
possible values are valid.

Vendor-specific properties will typically need more detailed schema. With the
exception of boolean properties, they should have a reference to a type in
schemas/types.yaml. A "description" property is always required.

The Devicetree schemas don't exactly match the YAML-encoded DT data produced by
dtc. They are simplified to make them more compact and avoid a bunch of
boilerplate. The tools process the schema files to produce the final schema for
validation. There are currently 2 transformations the tools perform.

The default for arrays in json-schema is they are variable-sized and allow more
entries than explicitly defined. This can be restricted by defining 'minItems',
'maxItems', and 'additionalItems'. However, for DeviceTree Schemas, a fixed
size is desired in most cases, so these properties are added based on the
number of entries in an 'items' list.

The YAML Devicetree format also makes all string values an array and scalar
values a matrix (in order to define groupings) even when only a single value
is present. Single entries in schemas are fixed up to match this encoding.

## Coding style

Use YAML coding style (two-space indentation). For DTS examples in the schema,
preferred is four-space indentation.

## Testing

### Dependencies

The DT schema project must be installed in order to validate the DT schema
binding documents and validate DTS files using the DT schema. The DT schema
project can be installed with pip:

```
pip3 install dtschema
```

Note that 'dtschema' installation requires 'swig' and Python development files
installed first. On Debian/Ubuntu systems:

```
apt install swig python3-dev
```

Several executables (dt-doc-validate, dt-mk-schema, dt-validate) will be
installed. Ensure they are in your PATH (~/.local/bin by default).

Recommended is also to install yamllint (used by dtschema when present).

### Running checks

The DT schema binding documents must be validated using the meta-schema (the
schema for the schema) to ensure they are both valid json-schema and valid
binding schema. All of the DT binding documents can be validated using the
`dt_binding_check` target:

```
make dt_binding_check
```

In order to perform validation of DT source files, use the `dtbs_check` target:

```
make dtbs_check
```

Note that `dtbs_check` will skip any binding schema files with errors. It is
necessary to use `dt_binding_check` to get all the validation errors in the
binding schema files.

It is possible to run both in a single command:

```
make dt_binding_check dtbs_check
```

It is also possible to run checks with a subset of matching schema files by
setting the `DT_SCHEMA_FILES` variable to 1 or more specific schema files or
patterns (partial match of a fixed string). Each file or pattern should be
separated by ':'.

```
make dt_binding_check DT_SCHEMA_FILES=trivial-devices.yaml
make dt_binding_check DT_SCHEMA_FILES=trivial-devices.yaml:rtc.yaml
make dt_binding_check DT_SCHEMA_FILES=/gpio/
make dtbs_check DT_SCHEMA_FILES=trivial-devices.yaml
```

## json-schema Resources

[JSON-Schema Specifications](http://json-schema.org/)

[Using JSON Schema Book](http://usingjsonschema.com/)

## Annotated Example Schema

Also available as a separate file: [`example-schema.yaml`](../../_downloads/bf29fbb4b15af5f11533d4e2b6a0e85b/example-schema.yaml.md)

```
# SPDX-License-Identifier: (GPL-2.0-only OR BSD-2-Clause)
# Copyright 2018 Linaro Ltd.
%YAML 1.2
---
# All the top-level keys are standard json-schema keywords except for
# 'maintainers' and 'select'

# $id is a unique identifier based on the filename. There may or may not be a
# file present at the URL.
$id: http://devicetree.org/schemas/example-schema.yaml#
# $schema is the meta-schema this schema should be validated with.
$schema: http://devicetree.org/meta-schemas/core.yaml#

title: An Example Device

maintainers:
  - Rob Herring <robh@kernel.org>

description: |
  A more detailed multi-line description of the binding.

  Details about the hardware device and any links to datasheets can go here.

  Literal blocks are marked with the '|' at the beginning. The end is marked by
  indentation less than the first line of the literal block. Lines also cannot
  begin with a tab character.

select: false
  # 'select' is a schema applied to a DT node to determine if this binding
  # schema should be applied to the node. It is optional and by default the
  # possible compatible strings are extracted and used to match.

  # In this case, a 'false' schema will never match.

properties:
  # A dictionary of DT properties for this binding schema
  compatible:
    # More complicated schema can use oneOf (XOR), anyOf (OR), or allOf (AND)
    # to handle different conditions.
    # In this case, it's needed to handle a variable number of values as there
    # isn't another way to express a constraint of the last string value.
    # The boolean schema must be a list of schemas.
    oneOf:
      - items:
          # items is a list of possible values for the property. The number of
          # values is determined by the number of elements in the list.
          # Order in lists is significant, order in dicts is not
          # Must be one of the 1st enums followed by the 2nd enum
          #
          # Each element in items should be 'enum' or 'const'
          - enum:
              - vendor,soc4-ip
              - vendor,soc3-ip
              - vendor,soc2-ip
          - const: vendor,soc1-ip
        # additionalItems being false is implied
        # minItems/maxItems equal to 2 is implied
      - items:
          # 'const' is just a special case of an enum with a single possible value
          - const: vendor,soc1-ip

  reg:
    # The core schema already checks that reg values are numbers, so device
    # specific schema don't need to do those checks.
    # The description of each element defines the order and implicitly defines
    # the number of reg entries.
    items:
      - description: core registers
      - description: aux registers
    # minItems/maxItems equal to 2 is implied

  reg-names:
    # The core schema enforces this (*-names) is a string array
    items:
      - const: core
      - const: aux

  clocks:
    # Cases that have only a single entry just need to express that with maxItems
    maxItems: 1
    description: bus clock. A description is only needed for a single item if
      there's something unique to add.
      The items should have a fixed order, so pattern matching names are
      discouraged.

  clock-names:
    # For single-entry lists in clocks, resets etc., the xxx-names often do not
    # bring any value, especially if they copy the IP block name.  In such case
    # just skip the xxx-names.
    items:
      - const: bus

  interrupts:
    # Either 1 or 2 interrupts can be present
    minItems: 1
    items:
      - description: tx or combined interrupt
      - description: rx interrupt
    description:
      A variable number of interrupts warrants a description of what conditions
      affect the number of interrupts. Otherwise, descriptions on standard
      properties are not necessary.
      The items should have a fixed order, so pattern matching names are
      discouraged.

  interrupt-names:
    # minItems must be specified here because the default would be 2
    minItems: 1
    items:
      - const: tx irq
      - const: rx irq

  # Property names starting with '#' must be quoted
  '#interrupt-cells':
    # A simple case where the value must always be '2'.
    # The core schema handles that this must be a single integer.
    const: 2

  interrupt-controller: true
    # The core checks this is a boolean, so just have to list it here to be
    # valid for this binding.

  clock-frequency:
    # The type is set in the core schema. Per-device schema only need to set
    # constraints on the possible values.
    minimum: 100
    maximum: 400000
    # The value that should be used if the property is not present
    default: 200

  foo-gpios:
    maxItems: 1
    description: A connection of the 'foo' gpio line.

  # *-supply is always a single phandle, so nothing more to define.
  foo-supply: true

  # Vendor-specific properties
  #
  # Vendor-specific properties have slightly different schema requirements than
  # common properties. They must have at least a type definition and
  # 'description'.
  vendor,int-property:
    description: Vendor-specific properties must have a description
    $ref: /schemas/types.yaml#/definitions/uint32
    enum: [2, 4, 6, 8, 10]

  vendor,bool-property:
    description: Vendor-specific properties must have a description. Boolean
      properties are one case where the json-schema 'type' keyword can be used
      directly.
    type: boolean

  vendor,string-array-property:
    description: Vendor-specific properties should reference a type in the
      core schema.
    $ref: /schemas/types.yaml#/definitions/string-array
    items:
      - enum: [foo, bar]
      - enum: [baz, boo]

  vendor,property-in-standard-units-microvolt:
    description: Vendor-specific properties having a standard unit suffix
      don't need a type.
    enum: [ 100, 200, 300 ]

  vendor,int-array-variable-length-and-constrained-values:
    description: Array might define what type of elements might be used (e.g.
      their range).
    $ref: /schemas/types.yaml#/definitions/uint32-array
    minItems: 2
    maxItems: 3
    items:
      minimum: 0
      maximum: 8

  child-node:
    description: Child nodes are just another property from a json-schema
      perspective.
    type: object  # DT nodes are json objects
    # Child nodes also need additionalProperties or unevaluatedProperties
    additionalProperties: false
    properties:
      vendor,a-child-node-property:
        description: Child node properties have all the same schema
          requirements.
        type: boolean

    required:
      - vendor,a-child-node-property

# Describe the relationship between different properties
dependencies:
  # 'vendor,bool-property' is only allowed when 'vendor,string-array-property'
  # is present
  vendor,bool-property: [ 'vendor,string-array-property' ]
  # Expressing 2 properties in both orders means all of the set of properties
  # must be present or none of them.
  vendor,string-array-property: [ 'vendor,bool-property' ]

required:
  - compatible
  - reg
  - interrupts
  - interrupt-controller

# if/then schema can be used to handle conditions on a property affecting
# another property. A typical case is a specific 'compatible' value changes the
# constraints on other properties.
#
# For multiple 'if' schema, group them under an 'allOf'.
#
# If the conditionals become too unweldy, then it may be better to just split
# the binding into separate schema documents.
allOf:
  - if:
      properties:
        compatible:
          contains:
            const: vendor,soc2-ip
    then:
      required:
        - foo-supply
    else:
      # If otherwise the property is not allowed:
      properties:
        foo-supply: false
  # Altering schema depending on presence of properties is usually done by
  # dependencies (see above), however some adjustments might require if:
  - if:
      required:
        - vendor,bool-property
    then:
      properties:
        vendor,int-property:
          enum: [2, 4, 6]

# Ideally, the schema should have this line otherwise any other properties
# present are allowed. There's a few common properties such as 'status' and
# 'pinctrl-*' which are added automatically by the tooling.
#
# This can't be used in cases where another schema is referenced
# (i.e. allOf: [{$ref: ...}]).
# If and only if another schema is referenced and arbitrary children nodes can
# appear, "unevaluatedProperties: false" could be used.  A typical example is
# an I2C controller where no name pattern matching for children can be added.
additionalProperties: false

examples:
  # Examples are now compiled with dtc and validated against the schemas
  #
  # Examples have a default #address-cells and #size-cells value of 1. This can
  # be overridden or an appropriate parent bus node should be shown (such as on
  # i2c buses).
  #
  # Any includes used have to be explicitly included. Use 4-space indentation.
  - |
    node@1000 {
        compatible = "vendor,soc4-ip", "vendor,soc1-ip";
        reg = <0x1000 0x80>,
              <0x3000 0x80>;
        reg-names = "core", "aux";
        interrupts = <10>;
        interrupt-controller;
    };
```
