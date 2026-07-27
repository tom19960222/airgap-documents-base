---
collection: ceph
version: "19.2.2"
title: "build on MacOS"
source_url: https://docs.ceph.com/en/squid/dev/macos/
fetched_at: 2026-07-27T16:41:24+00:00
---
# build on MacOS

Since we’ve switched to C++ 17, and the default clang shipped with Xcode 9 does not support all the C++ 17 language features, it’s suggested to install clang using brew:

```
brew install llvm
```

and install all the necessary bits:

```
brew install snappy ccache cmake pkg-config
pip install cython
```

install FUSE if you want to build the FUSE support:

```
brew cask install osxfuse
```

then, under the source directory of Ceph:

```
mkdir build
cd build
export PKG_CONFIG_PATH=/usr/local/Cellar/nss/3.48/lib/pkgconfig:/usr/local/Cellar/openssl/1.0.2t/lib/pkgconfig
cmake .. -DBOOST_J=4 \
  -DCMAKE_C_COMPILER=/usr/local/opt/llvm/bin/clang \
  -DCMAKE_CXX_COMPILER=/usr/local/opt/llvm/bin/clang++ \
  -DCMAKE_EXE_LINKER_FLAGS="-L/usr/local/opt/llvm/lib" \
  -DENABLE_GIT_VERSION=OFF \
  -DSNAPPY_ROOT_DIR=/usr/local/Cellar/snappy/1.1.7_1 \
  -DWITH_BABELTRACE=OFF \
  -DWITH_BLUESTORE=OFF \
  -DWITH_CCACHE=OFF \
  -DWITH_CEPHFS=OFF \
  -DWITH_KRBD=OFF \
  -DWITH_LIBCEPHFS=OFF \
  -DWITH_LTTNG=OFF \
  -DWITH_LZ4=OFF \
  -DWITH_MANPAGE=ON \
  -DWITH_MGR=OFF \
  -DWITH_MGR_DASHBOARD_FRONTEND=OFF \
  -DWITH_RADOSGW=OFF \
  -DWITH_RDMA=OFF \
  -DWITH_SPDK=OFF \
  -DWITH_SYSTEMD=OFF \
  -DWITH_TESTS=OFF \
  -DWITH_XFS=OFF
```

The paths to `nss` and `snappy` might vary if newer versions of the packages are installed.

Also, please consider using boost v1.69 to address the bug of <https://github.com/boostorg/atomic/issues/15>.

Currently, the most practical uses for Ceph on MacOS might be FUSE and some other librados based applications.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
