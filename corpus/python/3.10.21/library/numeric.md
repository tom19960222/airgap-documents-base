---
collection: python
version: "3.10.21"
title: "Numeric and Mathematical Modules"
source_url: https://docs.python.org/3.10/library/numeric.html
fetched_at: 2026-09-17T15:13:38+00:00
---
# Numeric and Mathematical Modules

The modules described in this chapter provide numeric and math-related functions
and data types. The [`numbers`](numbers.md#module-numbers "numbers: Numeric abstract base classes (Complex, Real, Integral, etc.).") module defines an abstract hierarchy of
numeric types. The [`math`](math.md#module-math "math: Mathematical functions (sin() etc.).") and [`cmath`](cmath.md#module-cmath "cmath: Mathematical functions for complex numbers.") modules contain various
mathematical functions for floating-point and complex numbers. The [`decimal`](decimal.md#module-decimal "decimal: Implementation of the General Decimal Arithmetic  Specification.")
module supports exact representations of decimal numbers, using arbitrary precision
arithmetic.

The following modules are documented in this chapter:

- [`numbers` — Numeric abstract base classes](numbers.md)
  - [The numeric tower](numbers.md#the-numeric-tower)
  - [Notes for type implementors](numbers.md#notes-for-type-implementors)
    - [Adding More Numeric ABCs](numbers.md#adding-more-numeric-abcs)
    - [Implementing the arithmetic operations](numbers.md#implementing-the-arithmetic-operations)
- [`math` — Mathematical functions](math.md)
  - [Number-theoretic and representation functions](math.md#number-theoretic-and-representation-functions)
  - [Power and logarithmic functions](math.md#power-and-logarithmic-functions)
  - [Trigonometric functions](math.md#trigonometric-functions)
  - [Angular conversion](math.md#angular-conversion)
  - [Hyperbolic functions](math.md#hyperbolic-functions)
  - [Special functions](math.md#special-functions)
  - [Constants](math.md#constants)
- [`cmath` — Mathematical functions for complex numbers](cmath.md)
  - [Conversions to and from polar coordinates](cmath.md#conversions-to-and-from-polar-coordinates)
  - [Power and logarithmic functions](cmath.md#power-and-logarithmic-functions)
  - [Trigonometric functions](cmath.md#trigonometric-functions)
  - [Hyperbolic functions](cmath.md#hyperbolic-functions)
  - [Classification functions](cmath.md#classification-functions)
  - [Constants](cmath.md#constants)
- [`decimal` — Decimal fixed point and floating point arithmetic](decimal.md)
  - [Quick-start Tutorial](decimal.md#quick-start-tutorial)
  - [Decimal objects](decimal.md#decimal-objects)
    - [Logical operands](decimal.md#logical-operands)
  - [Context objects](decimal.md#context-objects)
  - [Constants](decimal.md#constants)
  - [Rounding modes](decimal.md#rounding-modes)
  - [Signals](decimal.md#signals)
  - [Floating Point Notes](decimal.md#floating-point-notes)
    - [Mitigating round-off error with increased precision](decimal.md#mitigating-round-off-error-with-increased-precision)
    - [Special values](decimal.md#special-values)
  - [Working with threads](decimal.md#working-with-threads)
  - [Recipes](decimal.md#recipes)
  - [Decimal FAQ](decimal.md#decimal-faq)
- [`fractions` — Rational numbers](fractions.md)
- [`random` — Generate pseudo-random numbers](random.md)
  - [Bookkeeping functions](random.md#bookkeeping-functions)
  - [Functions for bytes](random.md#functions-for-bytes)
  - [Functions for integers](random.md#functions-for-integers)
  - [Functions for sequences](random.md#functions-for-sequences)
  - [Real-valued distributions](random.md#real-valued-distributions)
  - [Alternative Generator](random.md#alternative-generator)
  - [Notes on Reproducibility](random.md#notes-on-reproducibility)
  - [Examples](random.md#examples)
  - [Recipes](random.md#recipes)
- [`statistics` — Mathematical statistics functions](statistics.md)
  - [Averages and measures of central location](statistics.md#averages-and-measures-of-central-location)
  - [Measures of spread](statistics.md#measures-of-spread)
  - [Statistics for relations between two inputs](statistics.md#statistics-for-relations-between-two-inputs)
  - [Function details](statistics.md#function-details)
  - [Exceptions](statistics.md#exceptions)
  - [`NormalDist` objects](statistics.md#normaldist-objects)
    - [`NormalDist` Examples and Recipes](statistics.md#normaldist-examples-and-recipes)
