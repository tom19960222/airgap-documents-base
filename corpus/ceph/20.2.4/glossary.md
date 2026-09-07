---
collection: ceph
version: "20.2.4"
title: "Ceph Glossary"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/glossary.rst
fetched_at: 2026-08-18T01:32:45Z
---
# Ceph Glossary

.. glossary::

   Application
           More properly called a client, an application is any program
           external to Ceph that uses a Ceph Cluster to store and
           replicate data.

   [BlueStore](rados/configuration/storage-devices.md#rados-config-storage-devices-bluestore)
           OSD BlueStore is a storage back end used by OSD daemons, and
           was designed specifically for use with Ceph. BlueStore was
           introduced in the Ceph Kraken release. The Luminous release of
           Ceph promoted BlueStore to the default OSD back end,
           supplanting FileStore. As of the Reef release, FileStore is no
           longer available as a storage back end.

           BlueStore stores objects directly on raw block devices or
           partitions, and does not interact with mounted file systems.
           BlueStore uses RocksDB's key/value database to map object names
           to block locations on disk.

   Bucket
           In the context of RGW, a bucket is a group of objects.
           In a filesystem-based analogy in which objects are the
           counterpart of files, buckets are the counterpart of
           directories. [Multisite sync policies](radosgw/multisite-sync-policy.md#radosgw-multisite-sync-policy) can be set on buckets,
           to provide fine-grained control of data movement from one zone
           to another zone.

           The concept of the bucket has been taken from AWS S3. See also
           [the AWS S3 page on creating buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html)
           and [the AWS S3 'Buckets Overview' page](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html).

           OpenStack Swift uses the term "containers" for what RGW and AWS call "buckets".
           See [the OpenStack Storage API overview page](https://docs.openstack.org/swift/latest/api/object_api_v1_overview.html).

   Ceph
           Ceph is a distributed network storage and file system with
           distributed metadata management and POSIX semantics.

   [ceph-ansible](https://docs.ceph.com/projects/ceph-ansible/en/latest/index.html)
           A GitHub repository, supported from the Jewel release to the
           Quincy release, that facilitates the installation of a Ceph
           cluster.

   Ceph Block Device
           Also called "RADOS Block Device" and RBD. A software
           instrument that orchestrates the storage of block-based data in
           Ceph. Ceph Block Device splits block-based application data
           into "chunks". RADOS stores these chunks as objects. Ceph Block
           Device orchestrates the storage of those objects across the
           storage cluster.

   Ceph Block Storage
           One of the three kinds of storage supported by Ceph (the other
           two are object storage and file storage). Ceph Block Storage is
           the block storage "product", which refers to block-storage
           related services and capabilities when used in conjunction with
           the collection of (1) ``librbd`` (a python module that provides
           file-like access to RBD images), (2) a hypervisor such
           as QEMU or Xen, and (3) a hypervisor abstraction layer such as
           ``libvirt``.

   [Ceph Client](architecture.md#architecture-ceph-clients)
           Any of the Ceph components that can access a Ceph Storage
           Cluster. This includes the Ceph Object Gateway, the Ceph Block
           Device, the Ceph File System, and their corresponding
           libraries. It also includes kernel modules, and FUSEs
           (Filesystems in USERspace).

   Ceph Client Libraries
           The collection of libraries that can be used to interact with
           components of the Ceph Cluster.

   Ceph Cluster Map
           See Cluster Map

   Ceph Dashboard
           [The Ceph Dashboard](mgr/dashboard.md#mgr-dashboard) is a built-in
           web-based Ceph management and monitoring application through
           which you can inspect and administer various resources within
           the cluster. It is implemented as a [ceph-manager-daemon](mgr/index.md#ceph-manager-daemon)
           module.

   Ceph File System
           See CephFS

   [CephFS](cephfs/index.md#ceph-file-system)
           The **Ceph F**\ile **S**\ystem, or CephFS, is a
           POSIX-compliant file system built on top of Ceph’s distributed
           object store, RADOS.  See [CephFS Architecture](architecture.md#arch-cephfs) for more details.

   [ceph-fuse](man/8/ceph-fuse.md#man-ceph-fuse)
           [ceph-fuse](man/8/ceph-fuse.md#man-ceph-fuse) is a FUSE ("**F**\ilesystem in
           **USE**\rspace") client for CephFS. ceph-fuse mounts a Ceph FS
           ata  specified mount point.

   Ceph Interim Release
           See Releases.

   Ceph Kernel Modules
           The collection of kernel modules that can be used to interact
           with the Ceph Cluster (for example: ``ceph.ko``, ``rbd.ko``).

   [Ceph Manager](mgr/index.md#ceph-manager-daemon)
           The Ceph manager daemon (ceph-mgr) is a daemon that runs
           alongside monitor daemons to provide monitoring and interfacing
           to external monitoring and management systems. Since the
           Luminous release (12.x), no Ceph cluster functions properly
           unless it contains a running ceph-mgr daemon.

   Ceph Manager Dashboard
           See Ceph Dashboard.

   Ceph Metadata Server
           See MDS.

   Ceph Monitor
           A daemon that maintains a map of the state of the cluster. This
           "cluster state" includes the monitor map, the manager map, the
           OSD map, and the CRUSH map. A Ceph cluster must contain a
           minimum of three running monitors in order to be both redundant
           and highly-available. Ceph monitors and the nodes on which they
           run are often referred to as "mon"s. See [Monitor Config Reference](rados/configuration/mon-config-ref.md#monitor-config-reference).

   Ceph Node
          A Ceph node is a unit of the Ceph Cluster that communicates with
          other nodes in the Ceph Cluster in order to replicate and
          redistribute data. All of the nodes together are called the
          Ceph Storage Cluster. Ceph nodes include OSD\s,
          Ceph Monitor\s, Ceph Manager\s, and
          MDS\es. The term "node" is usually equivalent to "host"
          in the Ceph documentation. If you have a running Ceph Cluster,
          you can list all of the nodes in it by running the command
          ``ceph node ls all``.

   [Ceph Object Gateway](radosgw/index.md#object-gateway)
           An object storage interface built on top of librados. Ceph
           Object Gateway provides a RESTful gateway between applications
           and Ceph storage clusters.

   Ceph Object Storage
           See Ceph Object Store.

   Ceph Object Store
           A Ceph Object Store consists of a Ceph Storage Cluster
           and a Ceph Object Gateway (RGW).

   [Ceph OSD](rados/configuration/storage-devices.md#rados-configuration-storage-devices-ceph-osd)
           Ceph **O**\bject **S**\torage **D**\aemon. The Ceph OSD
           software, which interacts with logical disks (OSD).
           Around 2013, there was an attempt by "research and industry"
           (Sage's own words) to insist on using the term "OSD" to mean
           only "Object Storage Device", but the Ceph community has always
           persisted in using the term to mean "Object Storage Daemon" and
           no less an authority than Sage Weil himself confirms in
           November of 2022 that "Daemon is more accurate for how Ceph is
           built" (private correspondence between Zac Dover and Sage Weil,
           07 Nov 2022).

   Ceph OSD Daemon
           See Ceph OSD.

   Ceph OSD Daemons
           See Ceph OSD.

   Ceph Platform
           All Ceph software, which includes any piece of code hosted at
           [https://github.com/ceph](https://github.com/ceph).

   Ceph Point Release
           See Releases.

   Ceph Project
           The aggregate term for the people, software, mission and
           infrastructure of Ceph.

   Ceph Release
           See Releases.

   Ceph Release Candidate
           See Releases.

   Ceph Stable Release
           See Releases.

   Ceph Stack
           A collection of two or more components of Ceph.

   [Ceph Storage Cluster](architecture.md#arch-ceph-storage-cluster)
           The collection of Ceph Monitor\s, Ceph
           Manager\s, Ceph Metadata Server\s, and OSD\s
           that work together to store and replicate data for use by
           applications, Ceph Users, and Ceph Client\s. Ceph
           Storage Clusters receive data from Ceph Client\s.

   CephX
           The Ceph authentication protocol. CephX authenticates users and
           daemons. CephX operates like Kerberos, but it has no single
           point of failure and allows authentication to a class of
           services. See the [High-availability Authentication section](architecture.md#arch-high-availability-authentication) of the
           Architecture document and the [CephX Configuration Reference](rados/configuration/auth-config-ref.md#rados-cephx-config-ref).

   Client
           A client is any program external to Ceph that uses a Ceph
           Cluster to store and replicate data.

   Cloud Platforms
   Cloud Stacks
           Third party cloud provisioning platforms such as OpenStack,
           CloudStack, OpenNebula, and Proxmox VE.

   Cluster Map
           The set of maps consisting of the monitor map, OSD map, PG map,
           MDS map, and CRUSH map, which together report the state of the
           Ceph cluster. See [the "Cluster Map" section of the Architecture document](architecture.md#architecture-cluster-map) for details.

   Crimson
           A next-generation OSD architecture whose aim is the
           reduction of latency costs incurred due to cross-core
           communications. A re-design of the OSD reduces lock
           contention by reducing communication between shards in the data
           path. Crimson improves upon the performance of classic Ceph
           OSDs by eliminating reliance on thread pools. See [Crimson:
           Next-generation Ceph OSD for Multi-core Scalability](https://ceph.io/en/news/blog/2023/crimson-multi-core-scalability/).
           See the [Crimson developer documentation](dev/crimson/index.md#crimson-dev-doc).

   CRUSH
           **C**\ontrolled **R**\eplication **U**\nder **S**\calable
           **H**\ashing. The algorithm that Ceph uses to compute object
           storage locations. See [CRUSH: Controlled, Scalable,
           Decentralized Placement of Replicated Data](https://ceph.com/assets/pdfs/weil-crush-sc06.pdf).

   CRUSH rule
           The CRUSH data placement rule that applies to a particular
           pool or pools.

   DAS
           **D**\irect-\ **A**\ttached **S**\torage. Storage that is
           attached directly to the computer accessing it, without passing
           through a network.  Contrast with NAS and SAN.

   [Dashboard](mgr/dashboard.md#mgr-dashboard)
           A built-in web-based Ceph management and monitoring application
           to administer various aspects and objects of the cluster. The
           dashboard is implemented as a Ceph Manager module. See
           [mgr-dashboard](mgr/dashboard.md#mgr-dashboard) for more details.

   Dashboard Module
           Another name for Dashboard.

   Dashboard Plugin
           The dashboard plugin was a Mimic-era web application that
           visualized information and statistics about the Ceph cluster
           using a web server hosted by the [Ceph Manager](mgr/index.md#ceph-manager-daemon).

           See [the Mimic-era Dashboard Plugin documentation](https://docs.ceph.com/en/mimic/mgr/dashboard/).

   DC
           **D**\ata **C**\enter.

   Flapping OSD
           An OSD that is repeatedly marked ``up`` and then ``down`` in
           rapid succession. See [rados_tshooting_flapping_osd](rados/troubleshooting/troubleshooting-osd.md#rados-tshooting-flapping-osd).

   FQDN
           **F**\ully **Q**\ualified **D**\omain **N**\ame. A domain name
           that is applied to a node in a network and that specifies the
           node's exact location in the tree hierarchy of the DNS.

           In the context of Ceph cluster administration, FQDNs are often
           applied to hosts. In this documentation, the term "FQDN" is
           used mostly to distinguish between FQDNs and relatively simpler
           hostnames, which do not specify the exact location of the host
           in the tree hierarchy of the DNS but merely name the host.

   Host
           Any single machine or server in a Ceph Cluster. See Ceph
           Node.

   Hybrid OSD
           Refers to an OSD that has both HDD and SSD drives.

   librados
           An API that can be used to create a custom interface to a Ceph
           storage cluster. ``librados`` makes it possible to interact
           with Ceph Monitors and with OSDs. See [Introduction to librados](rados/api/librados-intro.md#librados-intro). See [librados (Python)](rados/api/python.md#librados-python).

   LVM tags
           **L**\ogical **V**\olume **M**\anager tags. Extensible metadata
           for LVM volumes and groups. They are used to store
           Ceph-specific information about devices and its relationship
           with OSDs.

   MDS
           The Ceph **M**\eta\ **D**\ata **S**\erver daemon. Also referred
           to as "ceph-mds". The Ceph metadata server daemon must be
           running in any Ceph cluster that runs the CephFS file system.
           The MDS stores all filesystem metadata. Client\s work
           together with either a single MDS or a group of MDSes to
           maintain a distributed metadata cache that is required by
           CephFS.

           See [Deploying Metadata Servers](cephfs/add-remove-mds.md#cephfs-add-remote-mds).

           See the [ceph-mds man page](man/8/ceph-mds.md#ceph-mds-man).

   MGR
           The Ceph manager software, which collects all the state from
           the whole cluster in one place.

   [MON](architecture.md#arch-monitor)
           The Ceph monitor software.

   Monitor Store
           The persistent storage that is used by the Monitor. This
           includes the Monitor's RocksDB and all related files in
           ``/var/lib/ceph``.

   Node
           See Ceph Node.

   Object Storage
           Object storage is one of three kinds of storage relevant to
           Ceph. The other two kinds of storage relevant to Ceph are file
           storage and block storage. Object storage is the category of
           storage most fundamental to Ceph.

   Object Storage Device
           See OSD.

   omap
           "object map". A key-value store (a database) that is used to
           reduce the time it takes to read data from and to write to the
           Ceph cluster. RGW bucket indexes are stored as omaps.
           Erasure-coded pools cannot store RADOS omap data structures.

           Run the command ``ceph osd df`` to see your omap.

           See Eleanor Cawthon's 2012 paper [A Distributed Key-Value Store
           using Ceph](https://ceph.io/assets/pdfs/CawthonKeyValueStore.pdf) (17
           pages).

   OpenStack Swift
           In the context of Ceph, OpenStack Swift is one of the two APIs
           supported by the Ceph Object Store. The other API supported by
           the Ceph Object Store is S3.

           See [the OpenStack Storage API overview page](https://docs.openstack.org/swift/latest/api/object_api_v1_overview.html).

   OSD
           Probably Ceph OSD, but not necessarily. Sometimes
           (especially in older correspondence, and especially in
           documentation that is not written specifically for Ceph), "OSD"
           means "**O**\bject **S**\torage **D**\evice", which refers to a
           physical or logical storage unit (for example: LUN). The Ceph
           community has always used the term "OSD" to refer to
           Ceph OSD Daemon despite an industry push in the
           mid-2010s to insist that "OSD" should refer to "Object Storage
           Device", so it is important to know which meaning is intended.

   OSD, flapping
           See Flapping OSD.

   OSD FSID
           The OSD fsid is a unique identifier that is used to identify an
           OSD. It is found in the OSD path in a file called ``osd_fsid``.
           The term ``FSID`` is used interchangeably with ``UUID``.

   OSD ID
           The OSD id an integer unique to each OSD (each OSD has a unique
           OSD ID). Each OSD id is generated by the monitors during the
           creation of its associated OSD.

   OSD UUID
           The OSD UUID is the unique identifier of an OSD. This term is
           used interchangeably with ``FSID``.

   Period
           In the context of RGW, a period is the configuration
           state of the Realm. The period stores the configuration
           state of a multi-site configuration. When the period is updated,
           the "epoch" is said thereby to have been changed.

   Placement Groups (PGs)
           Placement groups (PGs) are subsets of each logical Ceph pool.
           Placement groups perform the function of placing objects (as a
           group) into OSDs. Ceph manages data internally at
           placement-group granularity: this scales better than would
           managing individual (and therefore more numerous) RADOS
           objects. A cluster that has a larger number of placement groups
           (for example, 100 per OSD) is better balanced than an otherwise
           identical cluster with a smaller number of placement groups.

           Ceph's internal RADOS objects are each mapped to a specific
           placement group, and each placement group belongs to exactly
           one Ceph pool.

   PLP
           **P**\ower **L**\oss **P**\rotection. A technology that
           protects the data of solid-state drives by using capacitors to
           extend the amount of time available for transferring data from
           the DRAM cache to the SSD's permanent memory. Consumer-grade
           SSDs are rarely equipped with PLP.

   [Pool](rados/operations/pools.md#rados-pools)

           A pool is a logical partition used to store objects.

   Pools
           See pool.

   [Primary Affinity](rados/operations/crush-map.md#rados-ops-primary-affinity)
           The characteristic of an OSD that governs the likelihood that
           a given OSD will be selected as the primary OSD (or "lead
           OSD") in an acting set. Primary affinity was introduced in
           Firefly (v. 0.80). See [Primary Affinity](rados/operations/crush-map.md#rados-ops-primary-affinity).

   [Prometheus](mgr/prometheus.md#mgr-prometheus)
           An open-source monitoring and alerting toolkit. Ceph offers a
           ["Prometheus module"](mgr/prometheus.md#mgr-prometheus), which provides a
           Prometheus exporter that passes performance counters from a
           collection point in ``ceph-mgr`` to Prometheus.

   Quorum
           Quorum is the state that exists when a majority of the
           [Monitors](architecture.md#arch-monitor) in the cluster are ``up``. A
           minimum of three [Monitors](architecture.md#arch-monitor) must exist in
           the cluster in order for Quorum to be possible.

   RADOS
           **R**\eliable **A**\utonomic **D**\istributed **O**\bject
           **S**\tore. RADOS is the object store that provides a scalable
           service for variably-sized objects. The RADOS object store is
           the core component of a Ceph cluster.  [This blog post from
           2009](https://ceph.io/en/news/blog/2009/the-rados-distributed-object-store/)
           provides a beginner's introduction to RADOS. Readers interested
           in a deeper understanding of RADOS are directed to [RADOS: A
           Scalable, Reliable Storage Service for Petabyte-scale Storage
           Clusters](https://ceph.io/assets/pdfs/weil-rados-pdsw07.pdf).

   RADOS Cluster
           A proper subset of the Ceph Cluster consisting of
           OSD\s, Ceph Monitor\s, and Ceph
           Manager\s.

   RADOS Gateway
           See RGW.

   RBD
           **R**\ADOS **B**\lock **D**\evice. See Ceph Block
           Device.

   [Realm](radosgw/multisite.md#rgw-realms)
           In the context of RADOS Gateway (RGW), a realm is a globally
           unique namespace that consists of one or more zonegroups.

   Releases

           Ceph Interim Release
                   A version of Ceph that has not yet been put through
                   quality assurance testing. May contain new features.

           Ceph Point Release
                   Any ad hoc release that includes only bug fixes and
                   security fixes.

           Ceph Release
                   Any distinct numbered version of Ceph.

           Ceph Release Candidate
                   A major version of Ceph that has undergone initial
                   quality assurance testing and is ready for beta
                   testers.

           Ceph Stable Release
                   A major version of Ceph where all features from the
                   preceding interim releases have been put through
                   quality assurance testing successfully.

   Reliable Autonomic Distributed Object Store
           The core set of storage software which stores the user's data
           (MON+OSD). See also RADOS.

   [RGW](radosgw/index.md#object-gateway)
           **R**\ADOS **G**\ate\ **w**\ay.

           Also called "Ceph Object Gateway". The component of Ceph that
           provides a gateway to both the Amazon S3 RESTful API and the
           OpenStack Swift API.

   S3
           In the context of Ceph, S3 is one of the two APIs supported by
           the Ceph Object Store. The other API supported by the Ceph
           Object Store is OpenStack Swift.

           See [the Amazon S3 overview page](https://aws.amazon.com/s3/).

   scrubs

           The processes by which Ceph ensures data integrity. During the
           process of scrubbing, Ceph generates a catalog of all objects
           in a placement group, then ensures that none of the objects are
           missing or mismatched by comparing each primary object against
           its replicas, which are stored across other OSDs. Any PG
           is determined to have a copy of an object that is different
           than the other copies or is missing entirely is marked
           "inconsistent" (that is, the PG is marked "inconsistent").

           There are two kinds of scrubbing: light scrubbing and deep
           scrubbing (also called "shallow scrubbing" and "deep scrubbing",
           respectively). Light scrubbing is performed daily and does
           nothing more than confirm that a given object exists and that
           its metadata is correct. Deep scrubbing is performed weekly and
           reads the data and uses checksums to ensure data integrity.

           See [Scrubbing](rados/configuration/osd-config-ref.md#rados-config-scrubbing) in the RADOS OSD
           Configuration Reference Guide and page 141 of *Mastering Ceph,
           second edition* (Fisk, Nick. 2019).

   secrets
           Secrets are credentials used to perform digital authentication
           whenever privileged users must access systems that require
           authentication. Secrets can be passwords, API keys, tokens, SSH
           keys, private certificates, or encryption keys.

   SDS
           **S**\oftware-**d**\efined **S**\torage.

   systemd oneshot
           A systemd ``type`` where a command is defined in ``ExecStart``
           which will exit upon completion (it is not intended to
           daemonize)

   Swift
           See OpenStack Swift.

   Teuthology
           The collection of software that performs scripted tests on Ceph.

   User
           An individual or a system actor (for example, an application)
           that uses Ceph clients to interact with the Ceph Storage
           Cluster. See [User](rados/operations/user-management.md#rados-ops-user) and [User Management](rados/operations/user-management.md#user-management).

   Zone
           In the context of RGW, a zone is a logical group that
           consists of one or more RGW instances.  A zone's
           configuration state is stored in the period. See
           [Zones](radosgw/multisite.md#radosgw-zones).
