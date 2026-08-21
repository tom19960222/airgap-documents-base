---
collection: libvirt
version: "12.7.0"
title: "libvirt Installation"
source_url: https://libvirt.org/compiling.html
fetched_at: 2026-08-21T04:09:40+00:00
---
# libvirt Installation

Contents

- [Installing from distribution repositories](compiling.md#installing-from-distribution-repositories)
- [Preparing sources](compiling.md#preparing-sources)

  - [Unpacking a source tarball](compiling.md#unpacking-a-source-tarball)
  - [Git checkout](compiling.md#git-checkout)
- [Configuring the project](compiling.md#configuring-the-project)

  - [Explicitly enabling required functionality](compiling.md#explicitly-enabling-required-functionality)
  - [Notes:](compiling.md#notes)
- [Compiling the sources](compiling.md#compiling-the-sources)
- [Running compiled binaries from build directory](compiling.md#running-compiled-binaries-from-build-directory)
- [Installing compiled binaries](compiling.md#installing-compiled-binaries)

# [Installing from distribution repositories](compiling.md#id1)

This is the recommended option to install libvirt. Libvirt is present in the
package repositories of all major distributions. Installing a package from the
package manager ensures that it's properly compiled, installed, started, and
updated during the lifecycle of the distribution.

For users who wish to use the most recent version, certain distributions also
allow installing the most recent versions of virtualization packages:

> **Fedora**
>
> > Refer to <https://fedoraproject.org/wiki/Virtualization_Preview_Repository>
>
> **Gentoo**
>
> > The app-emulation/libvirt is regularly updated, but newest versions are
> > usually marked as testing by the ~\* keyword.
>
> **openSUSE**
>
> > Refer to <https://build.opensuse.org/package/show/Virtualization/libvirt>

# [Preparing sources](compiling.md#id2)

Libvirt can be built both from release tarballs and from a git checkout using
the same steps once the source code is prepared. Note that the build system
requires that the build directory is separate from the top level source
directory.

By default further steps will build libvirt inside a subdirectory of the source
tree named build.

Refer to the [downloads page](https://libvirt.org/downloads.html) for official tarballs and the
git repository.

## [Unpacking a source tarball](compiling.md#id3)

Download a source tarball of the version you want to compile and unpack it
using the following commands:

```
$ xz -dc libvirt-x.x.x.tar.xz | tar xvf -
$ cd libvirt-x.x.x
```

## [Git checkout](compiling.md#id4)

A git checkout/clone is already in correct state for next steps. Just change
your working directory to the checkout.

# [Configuring the project](compiling.md#id5)

The libvirt build process uses the **Meson** build system. To configure for a
build use the following command. Note that the build argument is the name
of the build directory which will be created.

```
$ meson setup build [options]
```

To get the complete list of the options run the following command:

```
$ meson configure
```

Be aware that by default the build is configured with a local prefix path
which will not interoperate with OS vendor provided binaries, since the UNIX
socket paths will all be different. To produce a build that is compatible with
normal OS vendor prefixes, use

```
$ meson setup build -Dsystem=true
```

## [Explicitly enabling required functionality](compiling.md#id6)

By default each module of functionality of libvirtd is optionally enabled,
meaning it will be enabled if the build environment contains the required
dependencies.

To ensure that your build contains the required functionality it's recommended
to explicitly enable given modules, in which case the configure step will end
with an error if dependencies are not present. **Example:** to build the
libvirt project with support for the **qemu** driver use the following options:

```
$ meson setup build -Dsystem=true -Ddriver_qemu=enabled
```

## [Notes:](compiling.md#id7)

By default when the meson is run from within a GIT checkout, it will turn
on -Werror for builds. This can be disabled with
-Dwerror=false -Dgit_werror=disabled, but this is not recommended.

Please ensure that you have the appropriate minimal meson version installed
in your build environment. The minimal version for a specific package can be
checked in the top level meson.build file in the meson_version field.

**DO NOT** use the CFLAGS environment variable to set optimizations
(e.g. CFLAGS=-O0), but rather use Meson's --optimization=0 option.
Certain internal build options are based on the configured optimization value
and Meson does not interpret CFLAGS.

# [Compiling the sources](compiling.md#id8)

Compilation can be carried out by ninja:

```
$ ninja -C build
```

"build" is the path to a directory which must match a path previously given
to meson setup.

Binaries and other resulting files can be found within the build directory.

Additionally you can also run the test suite:

```
$ ninja -C build test
```

# [Running compiled binaries from build directory](compiling.md#id9)

For testing or development purposes it's usually not necessary to install the
built binaries into your system. Instead simply run libvirt directly from the
source tree. For example to run a privileged libvirtd instance

```
$ su -
# service libvirtd stop  (or systemctl stop libvirtd.service)
# /home/to/your/checkout/build/src/libvirtd
```

It is also possible to run virsh directly from the build tree using the
./run script (which sets some environment variables):

```
$ pwd
/home/to/your/checkout/build
$ ./run ./tools/virsh ....
```

**Note:** The libvirt project provides [multiple daemons](daemons.md) and
the above steps may replace only some of them with the custom compiled instances.
In most cases this should work but keep that fact in mind.

# [Installing compiled binaries](compiling.md#id10)

**Important:** Manual installation of libvirt is generally not recommended and
you should prefer installation from your operating system's package repository
or from manually built packages which are then installed using the package
manager. Overwriting an installation of libvirt from the package manager by a
manually compiled installation may not work properly.

Installing the compiled binaries into the appropriate location (based on
how the build was configured) is done by the following command:

```
$ sudo ninja -C build install
```

Note the use of **sudo** with the *ninja install* command. Using
sudo is only required when installing to a location your user does not
have write access to. Installing to a system location is a good example
of this.

If you are installing to a location that your user *does* have write
access to, then you can instead run the *ninja install* command without
putting **sudo** before it.

After installation you you **may** have to run ldconfig or a similar
utility to update your list of installed shared libs, or adjust the paths where
the system looks for binaries and shared libraries.

The libvirt project provides [multiple daemons](daemons.md) based on your
configuration. You have to ensure that you start the appropriate processes for
the freshly installed libvirt to be usable (e.g. even monolithic libvirtd
requires in most configurations that virtlogd is started).
