---
collection: libvirt
version: "12.7.0"
title: "Libvirt Logo README"
source_url: https://libvirt.org/logos/index.html
fetched_at: 2026-08-21T04:10:20+00:00
---
# Libvirt Logo README

The master SVG files were created in InkScape, using the Overpass font from Red
Hat:

> <https://overpassfont.org/>

Contents

- [Logo formats](index.md#logo-formats)

  - [logo-base.svg](index.md#logo-base-svg)
  - [logo-square.svg](index.md#logo-square-svg)
  - [logo-square-powered.svg](index.md#logo-square-powered-svg)
  - [logo-banner-light.svg](index.md#logo-banner-light-svg)
  - [logo-banner-dark.svg](index.md#logo-banner-dark-svg)
  - [logo-sticker-square.svg](index.md#logo-sticker-square-svg)
  - [logo-sticker-hexagon.svg](index.md#logo-sticker-hexagon-svg)
- [PNG file creation](index.md#png-file-creation)

# [Logo formats](index.md#id1)

The following SVG files are provided, along with standard bitmap sizes in PNG
format:

## [logo-base.svg](index.md#id2)

![logo-base.svg](logo-base.svg)

The basic "sardine tin" graphic used to create the other forms of the
libvirt logo.

The tin is rotated by 20 degrees, so its angle matches the angle of the left
side of the letter "v" in the Overpass font

Never use this logo file directly. It exists merely as a base for building
the other logos

## [logo-square.svg](index.md#id3)

![logo-square.svg](logo-square.svg)

The minimal square format logo for libvirt. Simply embeds the word "libvirt"
into the basic logo graphic.

This is intended for use where a compact, square format representation of
the logo is required.

Bitmap sizes: 96, 128, 192, 256 px square

- 96px:

![logo-square-96.png](logo-square-96.png)

- 128px:

![logo-square-128.png](logo-square-128.png)

- 192px:

![logo-square-192.png](logo-square-192.png)

- 256px:

![logo-square-256.png](logo-square-256.png)

## [logo-square-powered.svg](index.md#id4)

![logo-square-powered.svg](logo-square-powered.svg)

A variant of the square logo for use by 3rd party applications, to advertise
their use of libvirt.

Bitmap sizes: 96, 128, 192, 256 px square

- 96px:

![logo-square-powered-96.png](logo-square-powered-96.png)

- 128px:

![logo-square-powered-128.png](logo-square-powered-128.png)

- 192px:

![logo-square-powered-192.png](logo-square-powered-192.png)

- 256px:

![logo-square-powered-256.png](logo-square-powered-256.png)

## [logo-banner-light.svg](index.md#id5)

![logo-banner-light.svg](logo-banner-light.svg)

A wide banner format of the logo. Embeds the words "libvirt virtualization
API" into the basic logo graphic. The text is rendered in a light color, so
suitable for placement over a dark background.

Bitmap sizes: 256x92, 800x286 px

- 256x92px:

![logo-banner-light-256.png](logo-banner-light-256.png)

- 800x286px:

![logo-banner-light-800.png](logo-banner-light-800.png)

## [logo-banner-dark.svg](index.md#id6)

![logo-banner-dark.svg](logo-banner-dark.svg)

A wide banner format of the logo. Embeds the words "libvirt virtualization
API" into the basic logo graphic. The text is rendered in a dark color, so
suitable for placement over a light background.

Bitmap sizes: 256x92, 800x286 px

- 256x92px:

![logo-banner-dark-256.png](logo-banner-dark-256.png)

- 800x286px:

![logo-banner-dark-800.png](logo-banner-dark-800.png)

## [logo-sticker-square.svg](index.md#id7)

![logo-sticker-square.svg](logo-sticker-square.svg)

A logo formatted into a square shape with outline, suitable for printing
as a sticker. See <https://github.com/terinjokes/StickerConstructorSpec>

## [logo-sticker-hexagon.svg](index.md#id8)

![logo-sticker-hexagon.svg](logo-sticker-hexagon.svg)

A logo formatted into a hexagon shape with outline, suitable for printing
as a sticker. See <https://github.com/terinjokes/StickerConstructorSpec>

# [PNG file creation](index.md#id9)

The bitmap images should not be created in Inkscape, since its anti-aliasing of
the rendered bitmaps is too aggressive, resulting in fuzzy images. Instead the
GIMP is used to create bitmaps as follows:

> - File -> Open, select the SVG file
>
>   When prompted for the image size, enter 1024 as the width and allow height
>   to be auto-set based on aspect ratio
> - Image -> Scale Image
>
>   Enter desired final bitmap size and use "Cubic" as scaling method.
> - File -> Export As

It is important to let GIMP render initially at 1024 and then scale down, rather
than rendering directly at the target size, since this the manual scaling step
produces better quality
