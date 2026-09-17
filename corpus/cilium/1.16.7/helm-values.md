---
collection: cilium
version: "1.16.7"
title: "helm-values"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/helm-values.rst
fetched_at: 2025-02-13T12:04:31Z
---
..
  AUTO-GENERATED. Please DO NOT edit manually.

.. role:: raw-html-m2r(raw)
   :format: html

.. list-table::
   :header-rows: 1

   * - :spellingKey
     - Description
     - Type
     - Default
   * - :spellingMTU
     - Configure the underlying network MTU to overwrite auto-detected MTU. This value doesn't change the host network interface MTU i.e. eth0 or ens0. It changes the MTU for cilium_net@cilium_host, cilium_host@cilium_net, cilium_vxlan and lxc_health interfaces.
     - int
     - ``0``
   * - :spellingaffinity
     - Affinity for cilium-agent.
     - object
     - ``{"podAntiAffinity":{"requiredDuringSchedulingIgnoredDuringExecution":[{"labelSelector":{"matchLabels":{"k8s-app":"cilium"}},"topologyKey":"kubernetes.io/hostname"}]}}``
   * - :spellingagent
     - Install the cilium agent resources.
     - bool
     - ``true``
   * - :spellingagentNotReadyTaintKey
     - Configure the key of the taint indicating that Cilium is not ready on the node. When set to a value starting with ``ignore-taint.cluster-autoscaler.kubernetes.io/``\ , the Cluster Autoscaler will ignore the taint on its decisions, allowing the cluster to scale up.
     - string
     - ``"node.cilium.io/agent-not-ready"``
   * - :spellingaksbyocni.enabled
     - Enable AKS BYOCNI integration. Note that this is incompatible with AKS clusters not created in BYOCNI mode: use Azure integration (\ ``azure.enabled``\ ) instead.
     - bool
     - ``false``
   * - :spellingalibabacloud.enabled
     - Enable AlibabaCloud ENI integration
     - bool
     - ``false``
   * - :spellingannotateK8sNode
     - Annotate k8s node upon initialization with Cilium's metadata.
     - bool
     - ``false``
   * - :spellingannotations
     - Annotations to be added to all top-level cilium-agent objects (resources under templates/cilium-agent)
     - object
     - ``{}``
   * - :spellingapiRateLimit
     - The api-rate-limit option can be used to overwrite individual settings of the default configuration for rate limiting calls to the Cilium Agent API
     - string
     - ``nil``
   * - :spellingauthentication.enabled
     - Enable authentication processing and garbage collection. Note that if disabled, policy enforcement will still block requests that require authentication. But the resulting authentication requests for these requests will not be processed, therefore the requests not be allowed.
     - bool
     - ``true``
   * - :spellingauthentication.gcInterval
     - Interval for garbage collection of auth map entries.
     - string
     - ``"5m0s"``
   * - :spellingauthentication.mutual.connectTimeout
     - Timeout for connecting to the remote node TCP socket
     - string
     - ``"5s"``
   * - :spellingauthentication.mutual.port
     - Port on the agent where mutual authentication handshakes between agents will be performed
     - int
     - ``4250``
   * - :spellingauthentication.mutual.spire.adminSocketPath
     - SPIRE socket path where the SPIRE delegated api agent is listening
     - string
     - ``"/run/spire/sockets/admin.sock"``
   * - :spellingauthentication.mutual.spire.agentSocketPath
     - SPIRE socket path where the SPIRE workload agent is listening. Applies to both the Cilium Agent and Operator
     - string
     - ``"/run/spire/sockets/agent/agent.sock"``
   * - :spellingauthentication.mutual.spire.annotations
     - Annotations to be added to all top-level spire objects (resources under templates/spire)
     - object
     - ``{}``
   * - :spellingauthentication.mutual.spire.connectionTimeout
     - SPIRE connection timeout
     - string
     - ``"30s"``
   * - :spellingauthentication.mutual.spire.enabled
     - Enable SPIRE integration (beta)
     - bool
     - ``false``
   * - :spellingauthentication.mutual.spire.install.agent.affinity
     - SPIRE agent affinity configuration
     - object
     - ``{}``
   * - :spellingauthentication.mutual.spire.install.agent.annotations
     - SPIRE agent annotations
     - object
     - ``{}``
   * - :spellingauthentication.mutual.spire.install.agent.image
     - SPIRE agent image
     - object
     - ``{"digest":"sha256:5106ac601272a88684db14daf7f54b9a45f31f77bb16a906bd5e87756ee7b97c","override":null,"pullPolicy":"IfNotPresent","repository":"ghcr.io/spiffe/spire-agent","tag":"1.9.6","useDigest":true}``
   * - :spellingauthentication.mutual.spire.install.agent.labels
     - SPIRE agent labels
     - object
     - ``{}``
   * - :spellingauthentication.mutual.spire.install.agent.nodeSelector
     - SPIRE agent nodeSelector configuration ref: ref: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector
     - object
     - ``{}``
   * - :spellingauthentication.mutual.spire.install.agent.podSecurityContext
     - Security context to be added to spire agent pods. SecurityContext holds pod-level security attributes and common container settings. ref: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-pod
     - object
     - ``{}``
   * - :spellingauthentication.mutual.spire.install.agent.securityContext
     - Security context to be added to spire agent containers. SecurityContext holds pod-level security attributes and common container settings. ref: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-container
     - object
     - ``{}``
   * - :spellingauthentication.mutual.spire.install.agent.serviceAccount
     - SPIRE agent service account
     - object
     - ``{"create":true,"name":"spire-agent"}``
   * - :spellingauthentication.mutual.spire.install.agent.skipKubeletVerification
     - SPIRE Workload Attestor kubelet verification.
     - bool
     - ``true``
   * - :spellingauthentication.mutual.spire.install.agent.tolerations
     - SPIRE agent tolerations configuration By default it follows the same tolerations as the agent itself to allow the Cilium agent on this node to connect to SPIRE. ref: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
     - list
     - ``[{"effect":"NoSchedule","key":"node.kubernetes.io/not-ready"},{"effect":"NoSchedule","key":"node-role.kubernetes.io/master"},{"effect":"NoSchedule","key":"node-role.kubernetes.io/control-plane"},{"effect":"NoSchedule","key":"node.cloudprovider.kubernetes.io/uninitialized","value":"true"},{"key":"CriticalAddonsOnly","operator":"Exists"}]``
   * - :spellingauthentication.mutual.spire.install.enabled
     - Enable SPIRE installation. This will only take effect only if authentication.mutual.spire.enabled is true
     - bool
     - ``true``
   * - :spellingauthentication.mutual.spire.install.existingNamespace
     - SPIRE namespace already exists. Set to true if Helm should not create, manage, and import the SPIRE namespace.
     - bool
     - ``false``
   * - :spellingauthentication.mutual.spire.install.initImage
     - init container image of SPIRE agent and server
     - object
     - ``{"digest":"sha256:71b79694b71639e633452f57fd9de40595d524de308349218d9a6a144b40be02","override":null,"pullPolicy":"IfNotPresent","repository":"docker.io/library/busybox","tag":"1.36.1","useDigest":true}``
   * - :spellingauthentication.mutual.spire.install.namespace
     - SPIRE namespace to install into
     - string
     - ``"cilium-spire"``
   * - :spellingauthentication.mutual.spire.install.server.affinity
     - SPIRE server affinity configuration
     - object
     - ``{}``
   * - :spellingauthentication.mutual.spire.install.server.annotations
     - SPIRE server annotations
     - object
     - ``{}``
   * - :spellingauthentication.mutual.spire.install.server.ca.keyType
     - SPIRE CA key type AWS requires the use of RSA. EC cryptography is not supported
     - string
     - ``"rsa-4096"``
   * - :spellingauthentication.mutual.spire.install.server.ca.subject
     - SPIRE CA Subject
     - object
     - ``{"commonName":"Cilium SPIRE CA","country":"US","organization":"SPIRE"}``
   * - :spellingauthentication.mutual.spire.install.server.dataStorage.accessMode
     - Access mode of the SPIRE server data storage
     - string
     - ``"ReadWriteOnce"``
   * - :spellingauthentication.mutual.spire.install.server.dataStorage.enabled
     - Enable SPIRE server data storage
     - bool
     - ``true``
   * - :spellingauthentication.mutual.spire.install.server.dataStorage.size
     - Size of the SPIRE server data storage
     - string
     - ``"1Gi"``
   * - :spellingauthentication.mutual.spire.install.server.dataStorage.storageClass
     - StorageClass of the SPIRE server data storage
     - string
     - ``nil``
   * - :spellingauthentication.mutual.spire.install.server.image
     - SPIRE server image
     - object
     - ``{"digest":"sha256:59a0b92b39773515e25e68a46c40d3b931b9c1860bc445a79ceb45a805cab8b4","override":null,"pullPolicy":"IfNotPresent","repository":"ghcr.io/spiffe/spire-server","tag":"1.9.6","useDigest":true}``
   * - :spellingauthentication.mutual.spire.install.server.initContainers
     - SPIRE server init containers
     - list
     - ``[]``
   * - :spellingauthentication.mutual.spire.install.server.labels
     - SPIRE server labels
     - object
     - ``{}``
   * - :spellingauthentication.mutual.spire.install.server.nodeSelector
     - SPIRE server nodeSelector configuration ref: ref: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector
     - object
     - ``{}``
   * - :spellingauthentication.mutual.spire.install.server.podSecurityContext
     - Security context to be added to spire server pods. SecurityContext holds pod-level security attributes and common container settings. ref: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-pod
     - object
     - ``{}``
   * - :spellingauthentication.mutual.spire.install.server.securityContext
     - Security context to be added to spire server containers. SecurityContext holds pod-level security attributes and common container settings. ref: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-container
     - object
     - ``{}``
   * - :spellingauthentication.mutual.spire.install.server.service.annotations
     - Annotations to be added to the SPIRE server service
     - object
     - ``{}``
   * - :spellingauthentication.mutual.spire.install.server.service.labels
     - Labels to be added to the SPIRE server service
     - object
     - ``{}``
   * - :spellingauthentication.mutual.spire.install.server.service.type
     - Service type for the SPIRE server service
     - string
     - ``"ClusterIP"``
   * - :spellingauthentication.mutual.spire.install.server.serviceAccount
     - SPIRE server service account
     - object
     - ``{"create":true,"name":"spire-server"}``
   * - :spellingauthentication.mutual.spire.install.server.tolerations
     - SPIRE server tolerations configuration ref: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
     - list
     - ``[]``
   * - :spellingauthentication.mutual.spire.serverAddress
     - SPIRE server address used by Cilium Operator  If k8s Service DNS along with port number is used (e.g. service-name.\ namespace.svc(.*):\ port-number format), Cilium Operator will resolve its address by looking up the clusterIP from Service resource.  Example values: 10.0.0.1:8081, spire-server.cilium-spire.svc:8081
     - string
     - ``nil``
   * - :spellingauthentication.mutual.spire.trustDomain
     - SPIFFE trust domain to use for fetching certificates
     - string
     - ``"spiffe.cilium"``
   * - :spellingauthentication.queueSize
     - Buffer size of the channel Cilium uses to receive authentication events from the signal map.
     - int
     - ``1024``
   * - :spellingauthentication.rotatedIdentitiesQueueSize
     - Buffer size of the channel Cilium uses to receive certificate expiration events from auth handlers.
     - int
     - ``1024``
   * - :spellingautoDirectNodeRoutes
     - Enable installation of PodCIDR routes between worker nodes if worker nodes share a common L2 network segment.
     - bool
     - ``false``
   * - :spellingazure.enabled
     - Enable Azure integration. Note that this is incompatible with AKS clusters created in BYOCNI mode: use AKS BYOCNI integration (\ ``aksbyocni.enabled``\ ) instead.
     - bool
     - ``false``
   * - :spellingbandwidthManager
     - Enable bandwidth manager to optimize TCP and UDP workloads and allow for rate-limiting traffic from individual Pods with EDT (Earliest Departure Time) through the "kubernetes.io/egress-bandwidth" Pod annotation.
     - object
     - ``{"bbr":false,"enabled":false}``
   * - :spellingbandwidthManager.bbr
     - Activate BBR TCP congestion control for Pods
     - bool
     - ``false``
   * - :spellingbandwidthManager.enabled
     - Enable bandwidth manager infrastructure (also prerequirement for BBR)
     - bool
     - ``false``
   * - :spellingbgp
     - Configure BGP
     - object
     - ``{"announce":{"loadbalancerIP":false,"podCIDR":false},"enabled":false}``
   * - :spellingbgp.announce.loadbalancerIP
     - Enable allocation and announcement of service LoadBalancer IPs
     - bool
     - ``false``
   * - :spellingbgp.announce.podCIDR
     - Enable announcement of node pod CIDR
     - bool
     - ``false``
   * - :spellingbgp.enabled
     - Enable BGP support inside Cilium; embeds a new ConfigMap for BGP inside cilium-agent and cilium-operator
     - bool
     - ``false``
   * - :spellingbgpControlPlane
     - This feature set enables virtual BGP routers to be created via CiliumBGPPeeringPolicy CRDs.
     - object
     - ``{"enabled":false,"secretsNamespace":{"create":false,"name":"kube-system"}}``
   * - :spellingbgpControlPlane.enabled
     - Enables the BGP control plane.
     - bool
     - ``false``
   * - :spellingbgpControlPlane.secretsNamespace
     - SecretsNamespace is the namespace which BGP support will retrieve secrets from.
     - object
     - ``{"create":false,"name":"kube-system"}``
   * - :spellingbgpControlPlane.secretsNamespace.create
     - Create secrets namespace for BGP secrets.
     - bool
     - ``false``
   * - :spellingbgpControlPlane.secretsNamespace.name
     - The name of the secret namespace to which Cilium agents are given read access
     - string
     - ``"kube-system"``
   * - :spellingbpf.authMapMax
     - Configure the maximum number of entries in auth map.
     - int
     - ``524288``
   * - :spellingbpf.autoMount.enabled
     - Enable automatic mount of BPF filesystem When ``autoMount`` is enabled, the BPF filesystem is mounted at ``bpf.root`` path on the underlying host and inside the cilium agent pod. If users disable ``autoMount``\ , it's expected that users have mounted bpffs filesystem at the specified ``bpf.root`` volume, and then the volume will be mounted inside the cilium agent pod at the same path.
     - bool
     - ``true``
   * - :spellingbpf.ctAnyMax
     - Configure the maximum number of entries for the non-TCP connection tracking table.
     - int
     - ``262144``
   * - :spellingbpf.ctTcpMax
     - Configure the maximum number of entries in the TCP connection tracking table.
     - int
     - ``524288``
   * - :spellingbpf.datapathMode
     - Mode for Pod devices for the core datapath (veth, netkit, netkit-l2, lb-only)
     - string
     - ``veth``
   * - :spellingbpf.disableExternalIPMitigation
     - Disable ExternalIP mitigation (CVE-2020-8554)
     - bool
     - ``false``
   * - :spellingbpf.enableTCX
     - Attach endpoint programs using tcx instead of legacy tc hooks on supported kernels.
     - bool
     - ``true``
   * - :spellingbpf.events
     - Control events generated by the Cilium datapath exposed to Cilium monitor and Hubble.
     - object
     - ``{"drop":{"enabled":true},"policyVerdict":{"enabled":true},"trace":{"enabled":true}}``
   * - :spellingbpf.events.drop.enabled
     - Enable drop events.
     - bool
     - ``true``
   * - :spellingbpf.events.policyVerdict.enabled
     - Enable policy verdict events.
     - bool
     - ``true``
   * - :spellingbpf.events.trace.enabled
     - Enable trace events.
     - bool
     - ``true``
   * - :spellingbpf.hostLegacyRouting
     - Configure whether direct routing mode should route traffic via host stack (true) or directly and more efficiently out of BPF (false) if the kernel supports it. The latter has the implication that it will also bypass netfilter in the host namespace.
     - bool
     - ``false``
   * - :spellingbpf.lbExternalClusterIP
     - Allow cluster external access to ClusterIP services.
     - bool
     - ``false``
   * - :spellingbpf.lbMapMax
     - Configure the maximum number of service entries in the load balancer maps.
     - int
     - ``65536``
   * - :spellingbpf.mapDynamicSizeRatio
     - Configure auto-sizing for all BPF maps based on available memory. ref: https://docs.cilium.io/en/stable/network/ebpf/maps/
     - float64
     - ``0.0025``
   * - :spellingbpf.masquerade
     - Enable native IP masquerade support in eBPF
     - bool
     - ``false``
   * - :spellingbpf.monitorAggregation
     - Configure the level of aggregation for monitor notifications. Valid options are none, low, medium, maximum.
     - string
     - ``"medium"``
   * - :spellingbpf.monitorFlags
     - Configure which TCP flags trigger notifications when seen for the first time in a connection.
     - string
     - ``"all"``
   * - :spellingbpf.monitorInterval
     - Configure the typical time between monitor notifications for active connections.
     - string
     - ``"5s"``
   * - :spellingbpf.natMax
     - Configure the maximum number of entries for the NAT table.
     - int
     - ``524288``
   * - :spellingbpf.neighMax
     - Configure the maximum number of entries for the neighbor table.
     - int
     - ``524288``
   * - :spellingbpf.nodeMapMax
     - Configures the maximum number of entries for the node table.
     - int
     - ``nil``
   * - :spellingbpf.policyMapMax
     - Configure the maximum number of entries in endpoint policy map (per endpoint). @schema type: [null, integer] @schema
     - int
     - ``16384``
   * - :spellingbpf.preallocateMaps
     - Enables pre-allocation of eBPF map values. This increases memory usage but can reduce latency.
     - bool
     - ``false``
   * - :spellingbpf.root
     - Configure the mount point for the BPF filesystem
     - string
     - ``"/sys/fs/bpf"``
   * - :spellingbpf.tproxy
     - Configure the eBPF-based TPROXY to reduce reliance on iptables rules for implementing Layer 7 policy.
     - bool
     - ``false``
   * - :spellingbpf.vlanBypass
     - Configure explicitly allowed VLAN id's for bpf logic bypass. [0] will allow all VLAN id's without any filtering.
     - list
     - ``[]``
   * - :spellingbpfClockProbe
     - Enable BPF clock source probing for more efficient tick retrieval.
     - bool
     - ``false``
   * - :spellingcertgen
     - Configure certificate generation for Hubble integration. If hubble.tls.auto.method=cronJob, these values are used for the Kubernetes CronJob which will be scheduled regularly to (re)generate any certificates not provided manually.
     - object
     - ``{"affinity":{},"annotations":{"cronJob":{},"job":{}},"extraVolumeMounts":[],"extraVolumes":[],"image":{"digest":"sha256:169d93fd8f2f9009db3b9d5ccd37c2b753d0989e1e7cd8fe79f9160c459eef4f","override":null,"pullPolicy":"IfNotPresent","repository":"quay.io/cilium/certgen","tag":"v0.2.0","useDigest":true},"podLabels":{},"tolerations":[],"ttlSecondsAfterFinished":1800}``
   * - :spellingcertgen.affinity
     - Affinity for certgen
     - object
     - ``{}``
   * - :spellingcertgen.annotations
     - Annotations to be added to the hubble-certgen initial Job and CronJob
     - object
     - ``{"cronJob":{},"job":{}}``
   * - :spellingcertgen.extraVolumeMounts
     - Additional certgen volumeMounts.
     - list
     - ``[]``
   * - :spellingcertgen.extraVolumes
     - Additional certgen volumes.
     - list
     - ``[]``
   * - :spellingcertgen.podLabels
     - Labels to be added to hubble-certgen pods
     - object
     - ``{}``
   * - :spellingcertgen.tolerations
     - Node tolerations for pod assignment on nodes with taints ref: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
     - list
     - ``[]``
   * - :spellingcertgen.ttlSecondsAfterFinished
     - Seconds after which the completed job pod will be deleted
     - int
     - ``1800``
   * - :spellingcgroup
     - Configure cgroup related configuration
     - object
     - ``{"autoMount":{"enabled":true,"resources":{}},"hostRoot":"/run/cilium/cgroupv2"}``
   * - :spellingcgroup.autoMount.enabled
     - Enable auto mount of cgroup2 filesystem. When ``autoMount`` is enabled, cgroup2 filesystem is mounted at ``cgroup.hostRoot`` path on the underlying host and inside the cilium agent pod. If users disable ``autoMount``\ , it's expected that users have mounted cgroup2 filesystem at the specified ``cgroup.hostRoot`` volume, and then the volume will be mounted inside the cilium agent pod at the same path.
     - bool
     - ``true``
   * - :spellingcgroup.autoMount.resources
     - Init Container Cgroup Automount resource limits & requests
     - object
     - ``{}``
   * - :spellingcgroup.hostRoot
     - Configure cgroup root where cgroup2 filesystem is mounted on the host (see also: ``cgroup.autoMount``\ )
     - string
     - ``"/run/cilium/cgroupv2"``
   * - :spellingciliumEndpointSlice.enabled
     - Enable Cilium EndpointSlice feature.
     - bool
     - ``false``
   * - :spellingciliumEndpointSlice.rateLimits
     - List of rate limit options to be used for the CiliumEndpointSlice controller. Each object in the list must have the following fields: nodes: Count of nodes at which to apply the rate limit. limit: The sustained request rate in requests per second. The maximum rate that can be configured is 50. burst: The burst request rate in requests per second. The maximum burst that can be configured is 100.
     - list
     - ``[{"burst":20,"limit":10,"nodes":0},{"burst":15,"limit":7,"nodes":100},{"burst":10,"limit":5,"nodes":500}]``
   * - :spellingcleanBpfState
     - Clean all eBPF datapath state from the initContainer of the cilium-agent DaemonSet.  WARNING: Use with care!
     - bool
     - ``false``
   * - :spellingcleanState
     - Clean all local Cilium state from the initContainer of the cilium-agent DaemonSet. Implies cleanBpfState: true.  WARNING: Use with care!
     - bool
     - ``false``
   * - :spellingcluster.id
     - Unique ID of the cluster. Must be unique across all connected clusters and in the range of 1 to 255. Only required for Cluster Mesh, may be 0 if Cluster Mesh is not used.
     - int
     - ``0``
   * - :spellingcluster.name
     - Name of the cluster. Only required for Cluster Mesh and mutual authentication with SPIRE. It must respect the following constraints: * It must contain at most 32 characters; * It must begin and end with a lower case alphanumeric character; * It may contain lower case alphanumeric characters and dashes between. The "default" name cannot be used if the Cluster ID is different from 0.
     - string
     - ``"default"``
   * - :spellingclustermesh.annotations
     - Annotations to be added to all top-level clustermesh objects (resources under templates/clustermesh-apiserver and templates/clustermesh-config)
     - object
     - ``{}``
   * - :spellingclustermesh.apiserver.affinity
     - Affinity for clustermesh.apiserver
     - object
     - ``{"podAntiAffinity":{"preferredDuringSchedulingIgnoredDuringExecution":[{"podAffinityTerm":{"labelSelector":{"matchLabels":{"k8s-app":"clustermesh-apiserver"}},"topologyKey":"kubernetes.io/hostname"},"weight":100}]}}``
   * - :spellingclustermesh.apiserver.etcd.init.extraArgs
     - Additional arguments to ``clustermesh-apiserver etcdinit``.
     - list
     - ``[]``
   * - :spellingclustermesh.apiserver.etcd.init.extraEnv
     - Additional environment variables to ``clustermesh-apiserver etcdinit``.
     - list
     - ``[]``
   * - :spellingclustermesh.apiserver.etcd.init.resources
     - Specifies the resources for etcd init container in the apiserver
     - object
     - ``{}``
   * - :spellingclustermesh.apiserver.etcd.lifecycle
     - lifecycle setting for the etcd container
     - object
     - ``{}``
   * - :spellingclustermesh.apiserver.etcd.resources
     - Specifies the resources for etcd container in the apiserver
     - object
     - ``{}``
   * - :spellingclustermesh.apiserver.etcd.securityContext
     - Security context to be added to clustermesh-apiserver etcd containers
     - object
     - ``{"allowPrivilegeEscalation":false,"capabilities":{"drop":["ALL"]}}``
   * - :spellingclustermesh.apiserver.etcd.storageMedium
     - Specifies whether etcd data is stored in a temporary volume backed by the node's default medium, such as disk, SSD or network storage (Disk), or RAM (Memory). The Memory option enables improved etcd read and write performance at the cost of additional memory usage, which counts against the memory limits of the container.
     - string
     - ``"Disk"``
   * - :spellingclustermesh.apiserver.extraArgs
     - Additional clustermesh-apiserver arguments.
     - list
     - ``[]``
   * - :spellingclustermesh.apiserver.extraEnv
     - Additional clustermesh-apiserver environment variables.
     - list
     - ``[]``
   * - :spellingclustermesh.apiserver.extraVolumeMounts
     - Additional clustermesh-apiserver volumeMounts.
     - list
     - ``[]``
   * - :spellingclustermesh.apiserver.extraVolumes
     - Additional clustermesh-apiserver volumes.
     - list
     - ``[]``
   * - :spellingclustermesh.apiserver.healthPort
     - TCP port for the clustermesh-apiserver health API.
     - int
     - ``9880``
   * - :spellingclustermesh.apiserver.image
     - Clustermesh API server image.
     - object
     - ``{"digest":"","override":null,"pullPolicy":"IfNotPresent","repository":"quay.io/cilium/clustermesh-apiserver","tag":"v1.16.7","useDigest":false}``
   * - :spellingclustermesh.apiserver.kvstoremesh.enabled
     - Enable KVStoreMesh. KVStoreMesh caches the information retrieved from the remote clusters in the local etcd instance.
     - bool
     - ``true``
   * - :spellingclustermesh.apiserver.kvstoremesh.extraArgs
     - Additional KVStoreMesh arguments.
     - list
     - ``[]``
   * - :spellingclustermesh.apiserver.kvstoremesh.extraEnv
     - Additional KVStoreMesh environment variables.
     - list
     - ``[]``
   * - :spellingclustermesh.apiserver.kvstoremesh.extraVolumeMounts
     - Additional KVStoreMesh volumeMounts.
     - list
     - ``[]``
   * - :spellingclustermesh.apiserver.kvstoremesh.healthPort
     - TCP port for the KVStoreMesh health API.
     - int
     - ``9881``
   * - :spellingclustermesh.apiserver.kvstoremesh.lifecycle
     - lifecycle setting for the KVStoreMesh container
     - object
     - ``{}``
   * - :spellingclustermesh.apiserver.kvstoremesh.readinessProbe
     - Configuration for the KVStoreMesh readiness probe.
     - object
     - ``{}``
   * - :spellingclustermesh.apiserver.kvstoremesh.resources
     - Resource requests and limits for the KVStoreMesh container
     - object
     - ``{}``
   * - :spellingclustermesh.apiserver.kvstoremesh.securityContext
     - KVStoreMesh Security context
     - object
     - ``{"allowPrivilegeEscalation":false,"capabilities":{"drop":["ALL"]}}``
   * - :spellingclustermesh.apiserver.lifecycle
     - lifecycle setting for the apiserver container
     - object
     - ``{}``
   * - :spellingclustermesh.apiserver.metrics.enabled
     - Enables exporting apiserver metrics in OpenMetrics format.
     - bool
     - ``true``
   * - :spellingclustermesh.apiserver.metrics.etcd.enabled
     - Enables exporting etcd metrics in OpenMetrics format.
     - bool
     - ``true``
   * - :spellingclustermesh.apiserver.metrics.etcd.mode
     - Set level of detail for etcd metrics; specify 'extensive' to include server side gRPC histogram metrics.
     - string
     - ``"basic"``
   * - :spellingclustermesh.apiserver.metrics.etcd.port
     - Configure the port the etcd metric server listens on.
     - int
     - ``9963``
   * - :spellingclustermesh.apiserver.metrics.kvstoremesh.enabled
     - Enables exporting KVStoreMesh metrics in OpenMetrics format.
     - bool
     - ``true``
   * - :spellingclustermesh.apiserver.metrics.kvstoremesh.port
     - Configure the port the KVStoreMesh metric server listens on.
     - int
     - ``9964``
   * - :spellingclustermesh.apiserver.metrics.port
     - Configure the port the apiserver metric server listens on.
     - int
     - ``9962``
   * - :spellingclustermesh.apiserver.metrics.serviceMonitor.annotations
     - Annotations to add to ServiceMonitor clustermesh-apiserver
     - object
     - ``{}``
   * - :spellingclustermesh.apiserver.metrics.serviceMonitor.enabled
     - Enable service monitor. This requires the prometheus CRDs to be available (see https://github.com/prometheus-operator/prometheus-operator/blob/main/example/prometheus-operator-crd/monitoring.coreos.com_servicemonitors.yaml)
     - bool
     - ``false``
   * - :spellingclustermesh.apiserver.metrics.serviceMonitor.etcd.interval
     - Interval for scrape metrics (etcd metrics)
     - string
     - ``"10s"``
   * - :spellingclustermesh.apiserver.metrics.serviceMonitor.etcd.metricRelabelings
     - Metrics relabeling configs for the ServiceMonitor clustermesh-apiserver (etcd metrics)
     - string
     - ``nil``
   * - :spellingclustermesh.apiserver.metrics.serviceMonitor.etcd.relabelings
     - Relabeling configs for the ServiceMonitor clustermesh-apiserver (etcd metrics)
     - string
     - ``nil``
   * - :spellingclustermesh.apiserver.metrics.serviceMonitor.interval
     - Interval for scrape metrics (apiserver metrics)
     - string
     - ``"10s"``
   * - :spellingclustermesh.apiserver.metrics.serviceMonitor.kvstoremesh.interval
     - Interval for scrape metrics (KVStoreMesh metrics)
     - string
     - ``"10s"``
   * - :spellingclustermesh.apiserver.metrics.serviceMonitor.kvstoremesh.metricRelabelings
     - Metrics relabeling configs for the ServiceMonitor clustermesh-apiserver (KVStoreMesh metrics)
     - string
     - ``nil``
   * - :spellingclustermesh.apiserver.metrics.serviceMonitor.kvstoremesh.relabelings
     - Relabeling configs for the ServiceMonitor clustermesh-apiserver (KVStoreMesh metrics)
     - string
     - ``nil``
   * - :spellingclustermesh.apiserver.metrics.serviceMonitor.labels
     - Labels to add to ServiceMonitor clustermesh-apiserver
     - object
     - ``{}``
   * - :spellingclustermesh.apiserver.metrics.serviceMonitor.metricRelabelings
     - Metrics relabeling configs for the ServiceMonitor clustermesh-apiserver (apiserver metrics)
     - string
     - ``nil``
   * - :spellingclustermesh.apiserver.metrics.serviceMonitor.relabelings
     - Relabeling configs for the ServiceMonitor clustermesh-apiserver (apiserver metrics)
     - string
     - ``nil``
   * - :spellingclustermesh.apiserver.nodeSelector
     - Node labels for pod assignment ref: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector
     - object
     - ``{"kubernetes.io/os":"linux"}``
   * - :spellingclustermesh.apiserver.podAnnotations
     - Annotations to be added to clustermesh-apiserver pods
     - object
     - ``{}``
   * - :spellingclustermesh.apiserver.podDisruptionBudget.enabled
     - enable PodDisruptionBudget ref: https://kubernetes.io/docs/concepts/workloads/pods/disruptions/
     - bool
     - ``false``
   * - :spellingclustermesh.apiserver.podDisruptionBudget.maxUnavailable
     - Maximum number/percentage of pods that may be made unavailable
     - int
     - ``1``
   * - :spellingclustermesh.apiserver.podDisruptionBudget.minAvailable
     - Minimum number/percentage of pods that should remain scheduled. When it's set, maxUnavailable must be disabled by ``maxUnavailable: null``
     - string
     - ``nil``
   * - :spellingclustermesh.apiserver.podLabels
     - Labels to be added to clustermesh-apiserver pods
     - object
     - ``{}``
   * - :spellingclustermesh.apiserver.podSecurityContext
     - Security context to be added to clustermesh-apiserver pods
     - object
     - ``{"fsGroup":65532,"runAsGroup":65532,"runAsNonRoot":true,"runAsUser":65532}``
   * - :spellingclustermesh.apiserver.priorityClassName
     - The priority class to use for clustermesh-apiserver
     - string
     - ``""``
   * - :spellingclustermesh.apiserver.readinessProbe
     - Configuration for the clustermesh-apiserver readiness probe.
     - object
     - ``{}``
   * - :spellingclustermesh.apiserver.replicas
     - Number of replicas run for the clustermesh-apiserver deployment.
     - int
     - ``1``
   * - :spellingclustermesh.apiserver.resources
     - Resource requests and limits for the clustermesh-apiserver
     - object
     - ``{}``
   * - :spellingclustermesh.apiserver.securityContext
     - Security context to be added to clustermesh-apiserver containers
     - object
     - ``{"allowPrivilegeEscalation":false,"capabilities":{"drop":["ALL"]}}``
   * - :spellingclustermesh.apiserver.service.annotations
     - Annotations for the clustermesh-apiserver For GKE LoadBalancer, use annotation cloud.google.com/load-balancer-type: "Internal" For EKS LoadBalancer, use annotation service.beta.kubernetes.io/aws-load-balancer-internal: "true"
     - object
     - ``{}``
   * - :spellingclustermesh.apiserver.service.enableSessionAffinity
     - Defines when to enable session affinity. Each replica in a clustermesh-apiserver deployment runs its own discrete etcd cluster. Remote clients connect to one of the replicas through a shared Kubernetes Service. A client reconnecting to a different backend will require a full resync to ensure data integrity. Session affinity can reduce the likelihood of this happening, but may not be supported by all cloud providers. Possible values:  - "HAOnly" (default) Only enable session affinity for deployments with more than 1 replica.  - "Always" Always enable session affinity.  - "Never" Never enable session affinity. Useful in environments where            session affinity is not supported, but may lead to slightly            degraded performance due to more frequent reconnections.
     - string
     - ``"HAOnly"``
   * - :spellingclustermesh.apiserver.service.externalTrafficPolicy
     - The externalTrafficPolicy of service used for apiserver access.
     - string
     - ``"Cluster"``
   * - :spellingclustermesh.apiserver.service.internalTrafficPolicy
     - The internalTrafficPolicy of service used for apiserver access.
     - string
     - ``"Cluster"``
   * - :spellingclustermesh.apiserver.service.loadBalancerClass
     - Configure a loadBalancerClass. Allows to configure the loadBalancerClass on the clustermesh-apiserver LB service in case the Service type is set to LoadBalancer (requires Kubernetes 1.24+).
     - string
     - ``nil``
   * - :spellingclustermesh.apiserver.service.loadBalancerIP
     - Configure a specific loadBalancerIP. Allows to configure a specific loadBalancerIP on the clustermesh-apiserver LB service in case the Service type is set to LoadBalancer.
     - string
     - ``nil``
   * - :spellingclustermesh.apiserver.service.nodePort
     - Optional port to use as the node port for apiserver access.  WARNING: make sure to configure a different NodePort in each cluster if kube-proxy replacement is enabled, as Cilium is currently affected by a known bug (#24692) when NodePorts are handled by the KPR implementation. If a service with the same NodePort exists both in the local and the remote cluster, all traffic originating from inside the cluster and targeting the corresponding NodePort will be redirected to a local backend, regardless of whether the destination node belongs to the local or the remote cluster.
     - int
     - ``32379``
   * - :spellingclustermesh.apiserver.service.type
     - The type of service used for apiserver access.
     - string
     - ``"NodePort"``
   * - :spellingclustermesh.apiserver.terminationGracePeriodSeconds
     - terminationGracePeriodSeconds for the clustermesh-apiserver deployment
     - int
     - ``30``
   * - :spellingclustermesh.apiserver.tls.admin
     - base64 encoded PEM values for the clustermesh-apiserver admin certificate and private key. Used if 'auto' is not enabled.
     - object
     - ``{"cert":"","key":""}``
   * - :spellingclustermesh.apiserver.tls.authMode
     - Configure the clustermesh authentication mode. Supported values: - legacy:     All clusters access remote clustermesh instances with the same               username (i.e., remote). The "remote" certificate must be               generated with CN=remote if provided manually. - migration:  Intermediate mode required to upgrade from legacy to cluster               (and vice versa) with no disruption. Specifically, it enables               the creation of the per-cluster usernames, while still using               the common one for authentication. The "remote" certificate must               be generated with CN=remote if provided manually (same as legacy). - cluster:    Each cluster accesses remote etcd instances with a username               depending on the local cluster name (i.e., remote-\ cluster-name\ ).               The "remote" certificate must be generated with CN=remote-\ cluster-name               if provided manually. Cluster mode is meaningful only when the same               CA is shared across all clusters part of the mesh.
     - string
     - ``"legacy"``
   * - :spellingclustermesh.apiserver.tls.auto
     - Configure automatic TLS certificates generation. A Kubernetes CronJob is used the generate any certificates not provided by the user at installation time.
     - object
     - ``{"certManagerIssuerRef":{},"certValidityDuration":1095,"enabled":true,"method":"helm"}``
   * - :spellingclustermesh.apiserver.tls.auto.certManagerIssuerRef
     - certmanager issuer used when clustermesh.apiserver.tls.auto.method=certmanager.
     - object
     - ``{}``
   * - :spellingclustermesh.apiserver.tls.auto.certValidityDuration
     - Generated certificates validity duration in days.
     - int
     - ``1095``
   * - :spellingclustermesh.apiserver.tls.auto.enabled
     - When set to true, automatically generate a CA and certificates to enable mTLS between clustermesh-apiserver and external workload instances. If set to false, the certs to be provided by setting appropriate values below.
     - bool
     - ``true``
   * - :spellingclustermesh.apiserver.tls.client
     - base64 encoded PEM values for the clustermesh-apiserver client certificate and private key. Used if 'auto' is not enabled.
     - object
     - ``{"cert":"","key":""}``
   * - :spellingclustermesh.apiserver.tls.enableSecrets
     - Allow users to provide their own certificates Users may need to provide their certificates using a mechanism that requires they provide their own secrets. This setting does not apply to any of the auto-generated mechanisms below, it only restricts the creation of secrets via the ``tls-provided`` templates.
     - bool
     - ``true``
   * - :spellingclustermesh.apiserver.tls.remote
     - base64 encoded PEM values for the clustermesh-apiserver remote cluster certificate and private key. Used if 'auto' is not enabled.
     - object
     - ``{"cert":"","key":""}``
   * - :spellingclustermesh.apiserver.tls.server
     - base64 encoded PEM values for the clustermesh-apiserver server certificate and private key. Used if 'auto' is not enabled.
     - object
     - ``{"cert":"","extraDnsNames":[],"extraIpAddresses":[],"key":""}``
   * - :spellingclustermesh.apiserver.tls.server.extraDnsNames
     - Extra DNS names added to certificate when it's auto generated
     - list
     - ``[]``
   * - :spellingclustermesh.apiserver.tls.server.extraIpAddresses
     - Extra IP addresses added to certificate when it's auto generated
     - list
     - ``[]``
   * - :spellingclustermesh.apiserver.tolerations
     - Node tolerations for pod assignment on nodes with taints ref: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
     - list
     - ``[]``
   * - :spellingclustermesh.apiserver.topologySpreadConstraints
     - Pod topology spread constraints for clustermesh-apiserver
     - list
     - ``[]``
   * - :spellingclustermesh.apiserver.updateStrategy
     - clustermesh-apiserver update strategy
     - object
     - ``{"rollingUpdate":{"maxSurge":1,"maxUnavailable":0},"type":"RollingUpdate"}``
   * - :spellingclustermesh.config
     - Clustermesh explicit configuration.
     - object
     - ``{"clusters":[],"domain":"mesh.cilium.io","enabled":false}``
   * - :spellingclustermesh.config.clusters
     - List of clusters to be peered in the mesh.
     - list
     - ``[]``
   * - :spellingclustermesh.config.domain
     - Default dns domain for the Clustermesh API servers This is used in the case cluster addresses are not provided and IPs are used.
     - string
     - ``"mesh.cilium.io"``
   * - :spellingclustermesh.config.enabled
     - Enable the Clustermesh explicit configuration.
     - bool
     - ``false``
   * - :spellingclustermesh.enableEndpointSliceSynchronization
     - Enable the synchronization of Kubernetes EndpointSlices corresponding to the remote endpoints of appropriately-annotated global services through ClusterMesh
     - bool
     - ``false``
   * - :spellingclustermesh.enableMCSAPISupport
     - Enable Multi-Cluster Services API support
     - bool
     - ``false``
   * - :spellingclustermesh.maxConnectedClusters
     - The maximum number of clusters to support in a ClusterMesh. This value cannot be changed on running clusters, and all clusters in a ClusterMesh must be configured with the same value. Values > 255 will decrease the maximum allocatable cluster-local identities. Supported values are 255 and 511.
     - int
     - ``255``
   * - :spellingclustermesh.useAPIServer
     - Deploy clustermesh-apiserver for clustermesh
     - bool
     - ``false``
   * - :spellingcni.binPath
     - Configure the path to the CNI binary directory on the host.
     - string
     - ``"/opt/cni/bin"``
   * - :spellingcni.chainingMode
     - Configure chaining on top of other CNI plugins. Possible values:  - none  - aws-cni  - flannel  - generic-veth  - portmap
     - string
     - ``nil``
   * - :spellingcni.chainingTarget
     - A CNI network name in to which the Cilium plugin should be added as a chained plugin. This will cause the agent to watch for a CNI network with this network name. When it is found, this will be used as the basis for Cilium's CNI configuration file. If this is set, it assumes a chaining mode of generic-veth. As a special case, a chaining mode of aws-cni implies a chainingTarget of aws-cni.
     - string
     - ``nil``
   * - :spellingcni.confFileMountPath
     - Configure the path to where to mount the ConfigMap inside the agent pod.
     - string
     - ``"/tmp/cni-configuration"``
   * - :spellingcni.confPath
     - Configure the path to the CNI configuration directory on the host.
     - string
     - ``"/etc/cni/net.d"``
   * - :spellingcni.configMapKey
     - Configure the key in the CNI ConfigMap to read the contents of the CNI configuration from.
     - string
     - ``"cni-config"``
   * - :spellingcni.customConf
     - Skip writing of the CNI configuration. This can be used if writing of the CNI configuration is performed by external automation.
     - bool
     - ``false``
   * - :spellingcni.enableRouteMTUForCNIChaining
     - Enable route MTU for pod netns when CNI chaining is used
     - bool
     - ``false``
   * - :spellingcni.exclusive
     - Make Cilium take ownership over the ``/etc/cni/net.d`` directory on the node, renaming all non-Cilium CNI configurations to ``*.cilium_bak``. This ensures no Pods can be scheduled using other CNI plugins during Cilium agent downtime.
     - bool
     - ``true``
   * - :spellingcni.hostConfDirMountPath
     - Configure the path to where the CNI configuration directory is mounted inside the agent pod.
     - string
     - ``"/host/etc/cni/net.d"``
   * - :spellingcni.install
     - Install the CNI configuration and binary files into the filesystem.
     - bool
     - ``true``
   * - :spellingcni.logFile
     - Configure the log file for CNI logging with retention policy of 7 days. Disable CNI file logging by setting this field to empty explicitly.
     - string
     - ``"/var/run/cilium/cilium-cni.log"``
   * - :spellingcni.resources
     - Specifies the resources for the cni initContainer
     - object
     - ``{"requests":{"cpu":"100m","memory":"10Mi"}}``
   * - :spellingcni.uninstall
     - Remove the CNI configuration and binary files on agent shutdown. Enable this if you're removing Cilium from the cluster. Disable this to prevent the CNI configuration file from being removed during agent upgrade, which can cause nodes to go unmanageable.
     - bool
     - ``false``
   * - :spellingconntrackGCInterval
     - Configure how frequently garbage collection should occur for the datapath connection tracking table.
     - string
     - ``"0s"``
   * - :spellingconntrackGCMaxInterval
     - Configure the maximum frequency for the garbage collection of the connection tracking table. Only affects the automatic computation for the frequency and has no effect when 'conntrackGCInterval' is set. This can be set to more frequently clean up unused identities created from ToFQDN policies.
     - string
     - ``""``
   * - :spellingcrdWaitTimeout
     - Configure timeout in which Cilium will exit if CRDs are not available
     - string
     - ``"5m"``
   * - :spellingcustomCalls
     - Tail call hooks for custom eBPF programs.
     - object
     - ``{"enabled":false}``
   * - :spellingcustomCalls.enabled
     - Enable tail call hooks for custom eBPF programs.
     - bool
     - ``false``
   * - :spellingdaemon.allowedConfigOverrides
     - allowedConfigOverrides is a list of config-map keys that can be overridden. That is to say, if this value is set, config sources (excepting the first one) can only override keys in this list.  This takes precedence over blockedConfigOverrides.  By default, all keys may be overridden. To disable overrides, set this to "none" or change the configSources variable.
     - string
     - ``nil``
   * - :spellingdaemon.blockedConfigOverrides
     - blockedConfigOverrides is a list of config-map keys that may not be overridden. In other words, if any of these keys appear in a configuration source excepting the first one, they will be ignored  This is ignored if allowedConfigOverrides is set.  By default, all keys may be overridden.
     - string
     - ``nil``
   * - :spellingdaemon.configSources
     - Configure a custom list of possible configuration override sources The default is "config-map:cilium-config,cilium-node-config". For supported values, see the help text for the build-config subcommand. Note that this value should be a comma-separated string.
     - string
     - ``nil``
   * - :spellingdaemon.runPath
     - Configure where Cilium runtime state should be stored.
     - string
     - ``"/var/run/cilium"``
   * - :spellingdashboards
     - Grafana dashboards for cilium-agent grafana can import dashboards based on the label and value ref: https://github.com/grafana/helm-charts/tree/main/charts/grafana#sidecar-for-dashboards
     - object
     - ``{"annotations":{},"enabled":false,"label":"grafana_dashboard","labelValue":"1","namespace":null}``
   * - :spellingdebug.enabled
     - Enable debug logging
     - bool
     - ``false``
   * - :spellingdebug.verbose
     - Configure verbosity levels for debug logging This option is used to enable debug messages for operations related to such sub-system such as (e.g. kvstore, envoy, datapath or policy), and flow is for enabling debug messages emitted per request, message and connection. Multiple values can be set via a space-separated string (e.g. "datapath envoy").  Applicable values: - flow - kvstore - envoy - datapath - policy
     - string
     - ``nil``
   * - :spellingdirectRoutingSkipUnreachable
     - Enable skipping of PodCIDR routes between worker nodes if the worker nodes are in a different L2 network segment.
     - bool
     - ``false``
   * - :spellingdisableEndpointCRD
     - Disable the usage of CiliumEndpoint CRD.
     - bool
     - ``false``
   * - :spellingdnsPolicy
     - DNS policy for Cilium agent pods. Ref: https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pod-s-dns-policy
     - string
     - ``""``
   * - :spellingdnsProxy.dnsRejectResponseCode
     - DNS response code for rejecting DNS requests, available options are '[nameError refused]'.
     - string
     - ``"refused"``
   * - :spellingdnsProxy.enableDnsCompression
     - Allow the DNS proxy to compress responses to endpoints that are larger than 512 Bytes or the EDNS0 option, if present.
     - bool
     - ``true``
   * - :spellingdnsProxy.endpointMaxIpPerHostname
     - Maximum number of IPs to maintain per FQDN name for each endpoint.
     - int
     - ``50``
   * - :spellingdnsProxy.idleConnectionGracePeriod
     - Time during which idle but previously active connections with expired DNS lookups are still considered alive.
     - string
     - ``"0s"``
   * - :spellingdnsProxy.maxDeferredConnectionDeletes
     - Maximum number of IPs to retain for expired DNS lookups with still-active connections.
     - int
     - ``10000``
   * - :spellingdnsProxy.minTtl
     - The minimum time, in seconds, to use DNS data for toFQDNs policies. If the upstream DNS server returns a DNS record with a shorter TTL, Cilium overwrites the TTL with this value. Setting this value to zero means that Cilium will honor the TTLs returned by the upstream DNS server.
     - int
     - ``0``
   * - :spellingdnsProxy.preCache
     - DNS cache data at this path is preloaded on agent startup.
     - string
     - ``""``
   * - :spellingdnsProxy.proxyPort
     - Global port on which the in-agent DNS proxy should listen. Default 0 is a OS-assigned port.
     - int
     - ``0``
   * - :spellingdnsProxy.proxyResponseMaxDelay
     - The maximum time the DNS proxy holds an allowed DNS response before sending it along. Responses are sent as soon as the datapath is updated with the new IP information.
     - string
     - ``"100ms"``
   * - :spellingdnsProxy.socketLingerTimeout
     - Timeout (in seconds) when closing the connection between the DNS proxy and the upstream server. If set to 0, the connection is closed immediately (with TCP RST). If set to -1, the connection is closed asynchronously in the background.
     - int
     - ``10``
   * - :spellingegressGateway.enabled
     - Enables egress gateway to redirect and SNAT the traffic that leaves the cluster.
     - bool
     - ``false``
   * - :spellingegressGateway.reconciliationTriggerInterval
     - Time between triggers of egress gateway state reconciliations
     - string
     - ``"1s"``
   * - :spellingenableCiliumEndpointSlice
     - Enable CiliumEndpointSlice feature (deprecated, please use ``ciliumEndpointSlice.enabled`` instead).
     - bool
     - ``false``
   * - :spellingenableCriticalPriorityClass
     - Explicitly enable or disable priority class. .Capabilities.KubeVersion is unsettable in ``helm template`` calls, it depends on k8s libraries version that Helm was compiled against. This option allows to explicitly disable setting the priority class, which is useful for rendering charts for gke clusters in advance.
     - bool
     - ``true``
   * - :spellingenableIPv4BIGTCP
     - Enables IPv4 BIG TCP support which increases maximum IPv4 GSO/GRO limits for nodes and pods
     - bool
     - ``false``
   * - :spellingenableIPv4Masquerade
     - Enables masquerading of IPv4 traffic leaving the node from endpoints.
     - bool
     - ``true``
   * - :spellingenableIPv6BIGTCP
     - Enables IPv6 BIG TCP support which increases maximum IPv6 GSO/GRO limits for nodes and pods
     - bool
     - ``false``
   * - :spellingenableIPv6Masquerade
     - Enables masquerading of IPv6 traffic leaving the node from endpoints.
     - bool
     - ``true``
   * - :spellingenableK8sTerminatingEndpoint
     - Configure whether to enable auto detect of terminating state for endpoints in order to support graceful termination.
     - bool
     - ``true``
   * - :spellingenableMasqueradeRouteSource
     - Enables masquerading to the source of the route for traffic leaving the node from endpoints.
     - bool
     - ``false``
   * - :spellingenableRuntimeDeviceDetection
     - Enables experimental support for the detection of new and removed datapath devices. When devices change the eBPF datapath is reloaded and services updated. If "devices" is set then only those devices, or devices matching a wildcard will be considered.  This option has been deprecated and is a no-op.
     - bool
     - ``true``
   * - :spellingenableXTSocketFallback
     - Enables the fallback compatibility solution for when the xt_socket kernel module is missing and it is needed for the datapath L7 redirection to work properly. See documentation for details on when this can be disabled: https://docs.cilium.io/en/stable/operations/system_requirements/#linux-kernel.
     - bool
     - ``true``
   * - :spellingencryption.enabled
     - Enable transparent network encryption.
     - bool
     - ``false``
   * - :spellingencryption.ipsec.encryptedOverlay
     - Enable IPsec encrypted overlay
     - bool
     - ``false``
   * - :spellingencryption.ipsec.interface
     - The interface to use for encrypted traffic.
     - string
     - ``""``
   * - :spellingencryption.ipsec.keyFile
     - Name of the key file inside the Kubernetes secret configured via secretName.
     - string
     - ``"keys"``
   * - :spellingencryption.ipsec.keyRotationDuration
     - Maximum duration of the IPsec key rotation. The previous key will be removed after that delay.
     - string
     - ``"5m"``
   * - :spellingencryption.ipsec.keyWatcher
     - Enable the key watcher. If disabled, a restart of the agent will be necessary on key rotations.
     - bool
     - ``true``
   * - :spellingencryption.ipsec.mountPath
     - Path to mount the secret inside the Cilium pod.
     - string
     - ``"/etc/ipsec"``
   * - :spellingencryption.ipsec.secretName
     - Name of the Kubernetes secret containing the encryption keys.
     - string
     - ``"cilium-ipsec-keys"``
   * - :spellingencryption.nodeEncryption
     - Enable encryption for pure node to node traffic. This option is only effective when encryption.type is set to "wireguard".
     - bool
     - ``false``
   * - :spellingencryption.strictMode
     - Configure the WireGuard Pod2Pod strict mode.
     - object
     - ``{"allowRemoteNodeIdentities":false,"cidr":"","enabled":false}``
   * - :spellingencryption.strictMode.allowRemoteNodeIdentities
     - Allow dynamic lookup of remote node identities. This is required when tunneling is used or direct routing is used and the node CIDR and pod CIDR overlap.
     - bool
     - ``false``
   * - :spellingencryption.strictMode.cidr
     - CIDR for the WireGuard Pod2Pod strict mode.
     - string
     - ``""``
   * - :spellingencryption.strictMode.enabled
     - Enable WireGuard Pod2Pod strict mode.
     - bool
     - ``false``
   * - :spellingencryption.type
     - Encryption method. Can be either ipsec or wireguard.
     - string
     - ``"ipsec"``
   * - :spellingencryption.wireguard.persistentKeepalive
     - Controls WireGuard PersistentKeepalive option. Set 0s to disable.
     - string
     - ``"0s"``
   * - :spellingencryption.wireguard.userspaceFallback
     - Enables the fallback to the user-space implementation (deprecated).
     - bool
     - ``false``
   * - :spellingendpointHealthChecking.enabled
     - Enable connectivity health checking between virtual endpoints.
     - bool
     - ``true``
   * - :spellingendpointRoutes.enabled
     - Enable use of per endpoint routes instead of routing via the cilium_host interface.
     - bool
     - ``false``
   * - :spellingeni.awsEnablePrefixDelegation
     - Enable ENI prefix delegation
     - bool
     - ``false``
   * - :spellingeni.awsReleaseExcessIPs
     - Release IPs not used from the ENI
     - bool
     - ``false``
   * - :spellingeni.ec2APIEndpoint
     - EC2 API endpoint to use
     - string
     - ``""``
   * - :spellingeni.enabled
     - Enable Elastic Network Interface (ENI) integration.
     - bool
     - ``false``
   * - :spellingeni.eniTags
     - Tags to apply to the newly created ENIs
     - object
     - ``{}``
   * - :spellingeni.gcInterval
     - Interval for garbage collection of unattached ENIs. Set to "0s" to disable.
     - string
     - ``"5m"``
   * - :spellingeni.gcTags
     - Additional tags attached to ENIs created by Cilium. Dangling ENIs with this tag will be garbage collected
     - object
     - ``{"io.cilium/cilium-managed":"true,"io.cilium/cluster-name":"<auto-detected>"}``
   * - :spellingeni.iamRole
     - If using IAM role for Service Accounts will not try to inject identity values from cilium-aws kubernetes secret. Adds annotation to service account if managed by Helm. See https://github.com/aws/amazon-eks-pod-identity-webhook
     - string
     - ``""``
   * - :spellingeni.instanceTagsFilter
     - Filter via AWS EC2 Instance tags (k=v) which will dictate which AWS EC2 Instances are going to be used to create new ENIs
     - list
     - ``[]``
   * - :spellingeni.subnetIDsFilter
     - Filter via subnet IDs which will dictate which subnets are going to be used to create new ENIs Important note: This requires that each instance has an ENI with a matching subnet attached when Cilium is deployed. If you only want to control subnets for ENIs attached by Cilium, use the CNI configuration file settings (cni.customConf) instead.
     - list
     - ``[]``
   * - :spellingeni.subnetTagsFilter
     - Filter via tags (k=v) which will dictate which subnets are going to be used to create new ENIs Important note: This requires that each instance has an ENI with a matching subnet attached when Cilium is deployed. If you only want to control subnets for ENIs attached by Cilium, use the CNI configuration file settings (cni.customConf) instead.
     - list
     - ``[]``
   * - :spellingeni.updateEC2AdapterLimitViaAPI
     - Update ENI Adapter limits from the EC2 API
     - bool
     - ``true``
   * - :spellingenvoy.affinity
     - Affinity for cilium-envoy.
     - object
     - ``{"nodeAffinity":{"requiredDuringSchedulingIgnoredDuringExecution":{"nodeSelectorTerms":[{"matchExpressions":[{"key":"cilium.io/no-schedule","operator":"NotIn","values":["true"]}]}]}},"podAffinity":{"requiredDuringSchedulingIgnoredDuringExecution":[{"labelSelector":{"matchLabels":{"k8s-app":"cilium"}},"topologyKey":"kubernetes.io/hostname"}]},"podAntiAffinity":{"requiredDuringSchedulingIgnoredDuringExecution":[{"labelSelector":{"matchLabels":{"k8s-app":"cilium-envoy"}},"topologyKey":"kubernetes.io/hostname"}]}}``
   * - :spellingenvoy.annotations
     - Annotations to be added to all top-level cilium-envoy objects (resources under templates/cilium-envoy)
     - object
     - ``{}``
   * - :spellingenvoy.baseID
     - Set Envoy'--base-id' to use when allocating shared memory regions. Only needs to be changed if multiple Envoy instances will run on the same node and may have conflicts. Supported values: 0 - 4294967295. Defaults to '0'
     - int
     - ``0``
   * - :spellingenvoy.connectTimeoutSeconds
     - Time in seconds after which a TCP connection attempt times out
     - int
     - ``2``
   * - :spellingenvoy.debug.admin.enabled
     - Enable admin interface for cilium-envoy. This is useful for debugging and should not be enabled in production.
     - bool
     - ``false``
   * - :spellingenvoy.debug.admin.port
     - Port number (bound to loopback interface). kubectl port-forward can be used to access the admin interface.
     - int
     - ``9901``
   * - :spellingenvoy.dnsPolicy
     - DNS policy for Cilium envoy pods. Ref: https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pod-s-dns-policy
     - string
     - ``nil``
   * - :spellingenvoy.enabled
     - Enable Envoy Proxy in standalone DaemonSet. This field is enabled by default for new installation.
     - string
     - ``true`` for new installation
   * - :spellingenvoy.extraArgs
     - Additional envoy container arguments.
     - list
     - ``[]``
   * - :spellingenvoy.extraContainers
     - Additional containers added to the cilium Envoy DaemonSet.
     - list
     - ``[]``
   * - :spellingenvoy.extraEnv
     - Additional envoy container environment variables.
     - list
     - ``[]``
   * - :spellingenvoy.extraHostPathMounts
     - Additional envoy hostPath mounts.
     - list
     - ``[]``
   * - :spellingenvoy.extraVolumeMounts
     - Additional envoy volumeMounts.
     - list
     - ``[]``
   * - :spellingenvoy.extraVolumes
     - Additional envoy volumes.
     - list
     - ``[]``
   * - :spellingenvoy.healthPort
     - TCP port for the health API.
     - int
     - ``9878``
   * - :spellingenvoy.idleTimeoutDurationSeconds
     - Set Envoy upstream HTTP idle connection timeout seconds. Does not apply to connections with pending requests. Default 60s
     - int
     - ``60``
   * - :spellingenvoy.image
     - Envoy container image.
     - object
     - ``{"digest":"sha256:fc708bd36973d306412b2e50c924cd8333de67e0167802c9b48506f9d772f521","override":null,"pullPolicy":"IfNotPresent","repository":"quay.io/cilium/cilium-envoy","tag":"v1.31.5-1739264036-958bef243c6c66fcfd73ca319f2eb49fff1eb2ae","useDigest":true}``
   * - :spellingenvoy.initialFetchTimeoutSeconds
     - Time in seconds after which the initial fetch on an xDS stream is considered timed out
     - int
     - ``30``
   * - :spellingenvoy.livenessProbe.failureThreshold
     - failure threshold of liveness probe
     - int
     - ``10``
   * - :spellingenvoy.livenessProbe.periodSeconds
     - interval between checks of the liveness probe
     - int
     - ``30``
   * - :spellingenvoy.log.accessLogBufferSize
     - Size of the Envoy access log buffer created within the agent in bytes. Tune this value up if you encounter "Envoy: Discarded truncated access log message" errors. Large request/response header sizes (e.g. 16KiB) will require a larger buffer size.
     - int
     - ``4096``
   * - :spellingenvoy.log.format
     - The format string to use for laying out the log message metadata of Envoy.
     - string
     - ``"[%Y-%m-%d %T.%e][%t][%l][%n] [%g:%#] %v"``
   * - :spellingenvoy.log.path
     - Path to a separate Envoy log file, if any. Defaults to /dev/stdout.
     - string
     - ``""``
   * - :spellingenvoy.maxConnectionDurationSeconds
     - Set Envoy HTTP option max_connection_duration seconds. Default 0 (disable)
     - int
     - ``0``
   * - :spellingenvoy.maxRequestsPerConnection
     - ProxyMaxRequestsPerConnection specifies the max_requests_per_connection setting for Envoy
     - int
     - ``0``
   * - :spellingenvoy.nodeSelector
     - Node selector for cilium-envoy.
     - object
     - ``{"kubernetes.io/os":"linux"}``
   * - :spellingenvoy.podAnnotations
     - Annotations to be added to envoy pods
     - object
     - ``{}``
   * - :spellingenvoy.podLabels
     - Labels to be added to envoy pods
     - object
     - ``{}``
   * - :spellingenvoy.podSecurityContext
     - Security Context for cilium-envoy pods.
     - object
     - ``{"appArmorProfile":{"type":"Unconfined"}}``
   * - :spellingenvoy.podSecurityContext.appArmorProfile
     - AppArmorProfile options for the ``cilium-agent`` and init containers
     - object
     - ``{"type":"Unconfined"}``
   * - :spellingenvoy.priorityClassName
     - The priority class to use for cilium-envoy.
     - string
     - ``nil``
   * - :spellingenvoy.prometheus
     - Configure Cilium Envoy Prometheus options. Note that some of these apply to either cilium-agent or cilium-envoy.
     - object
     - ``{"enabled":true,"port":"9964","serviceMonitor":{"annotations":{},"enabled":false,"interval":"10s","labels":{},"metricRelabelings":null,"relabelings":[{"replacement":"${1}","sourceLabels":["__meta_kubernetes_pod_node_name"],"targetLabel":"node"}]}}``
   * - :spellingenvoy.prometheus.enabled
     - Enable prometheus metrics for cilium-envoy
     - bool
     - ``true``
   * - :spellingenvoy.prometheus.port
     - Serve prometheus metrics for cilium-envoy on the configured port
     - string
     - ``"9964"``
   * - :spellingenvoy.prometheus.serviceMonitor.annotations
     - Annotations to add to ServiceMonitor cilium-envoy
     - object
     - ``{}``
   * - :spellingenvoy.prometheus.serviceMonitor.enabled
     - Enable service monitors. This requires the prometheus CRDs to be available (see https://github.com/prometheus-operator/prometheus-operator/blob/main/example/prometheus-operator-crd/monitoring.coreos.com_servicemonitors.yaml) Note that this setting applies to both cilium-envoy *and* cilium-agent with Envoy enabled.
     - bool
     - ``false``
   * - :spellingenvoy.prometheus.serviceMonitor.interval
     - Interval for scrape metrics.
     - string
     - ``"10s"``
   * - :spellingenvoy.prometheus.serviceMonitor.labels
     - Labels to add to ServiceMonitor cilium-envoy
     - object
     - ``{}``
   * - :spellingenvoy.prometheus.serviceMonitor.metricRelabelings
     - Metrics relabeling configs for the ServiceMonitor cilium-envoy or for cilium-agent with Envoy configured.
     - string
     - ``nil``
   * - :spellingenvoy.prometheus.serviceMonitor.relabelings
     - Relabeling configs for the ServiceMonitor cilium-envoy or for cilium-agent with Envoy configured.
     - list
     - ``[{"replacement":"${1}","sourceLabels":["__meta_kubernetes_pod_node_name"],"targetLabel":"node"}]``
   * - :spellingenvoy.readinessProbe.failureThreshold
     - failure threshold of readiness probe
     - int
     - ``3``
   * - :spellingenvoy.readinessProbe.periodSeconds
     - interval between checks of the readiness probe
     - int
     - ``30``
   * - :spellingenvoy.resources
     - Envoy resource limits & requests ref: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
     - object
     - ``{}``
   * - :spellingenvoy.rollOutPods
     - Roll out cilium envoy pods automatically when configmap is updated.
     - bool
     - ``false``
   * - :spellingenvoy.securityContext.capabilities.envoy
     - Capabilities for the ``cilium-envoy`` container. Even though granted to the container, the cilium-envoy-starter wrapper drops all capabilities after forking the actual Envoy process. ``NET_BIND_SERVICE`` is the only capability that can be passed to the Envoy process by setting ``envoy.securityContext.capabilities.keepNetBindService=true`` (in addition to granting the capability to the container). Note: In case of embedded envoy, the capability must  be granted to the cilium-agent container.
     - list
     - ``["NET_ADMIN","SYS_ADMIN"]``
   * - :spellingenvoy.securityContext.capabilities.keepCapNetBindService
     - Keep capability ``NET_BIND_SERVICE`` for Envoy process.
     - bool
     - ``false``
   * - :spellingenvoy.securityContext.privileged
     - Run the pod with elevated privileges
     - bool
     - ``false``
   * - :spellingenvoy.securityContext.seLinuxOptions
     - SELinux options for the ``cilium-envoy`` container
     - object
     - ``{"level":"s0","type":"spc_t"}``
   * - :spellingenvoy.startupProbe.failureThreshold
     - failure threshold of startup probe. 105 x 2s translates to the old behaviour of the readiness probe (120s delay + 30 x 3s)
     - int
     - ``105``
   * - :spellingenvoy.startupProbe.periodSeconds
     - interval between checks of the startup probe
     - int
     - ``2``
   * - :spellingenvoy.terminationGracePeriodSeconds
     - Configure termination grace period for cilium-envoy DaemonSet.
     - int
     - ``1``
   * - :spellingenvoy.tolerations
     - Node tolerations for envoy scheduling to nodes with taints ref: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
     - list
     - ``[{"operator":"Exists"}]``
   * - :spellingenvoy.updateStrategy
     - cilium-envoy update strategy ref: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/#updating-a-daemonset
     - object
     - ``{"rollingUpdate":{"maxUnavailable":2},"type":"RollingUpdate"}``
   * - :spellingenvoy.xffNumTrustedHopsL7PolicyEgress
     - Number of trusted hops regarding the x-forwarded-for and related HTTP headers for the egress L7 policy enforcement Envoy listeners.
     - int
     - ``0``
   * - :spellingenvoy.xffNumTrustedHopsL7PolicyIngress
     - Number of trusted hops regarding the x-forwarded-for and related HTTP headers for the ingress L7 policy enforcement Envoy listeners.
     - int
     - ``0``
   * - :spellingenvoyConfig.enabled
     - Enable CiliumEnvoyConfig CRD CiliumEnvoyConfig CRD can also be implicitly enabled by other options.
     - bool
     - ``false``
   * - :spellingenvoyConfig.retryInterval
     - Interval in which an attempt is made to reconcile failed EnvoyConfigs. If the duration is zero, the retry is deactivated.
     - string
     - ``"15s"``
   * - :spellingenvoyConfig.secretsNamespace
     - SecretsNamespace is the namespace in which envoy SDS will retrieve secrets from.
     - object
     - ``{"create":true,"name":"cilium-secrets"}``
   * - :spellingenvoyConfig.secretsNamespace.create
     - Create secrets namespace for CiliumEnvoyConfig CRDs.
     - bool
     - ``true``
   * - :spellingenvoyConfig.secretsNamespace.name
     - The name of the secret namespace to which Cilium agents are given read access.
     - string
     - ``"cilium-secrets"``
   * - :spellingetcd.enabled
     - Enable etcd mode for the agent.
     - bool
     - ``false``
   * - :spellingetcd.endpoints
     - List of etcd endpoints
     - list
     - ``["https://CHANGE-ME:2379"]``
   * - :spellingetcd.ssl
     - Enable use of TLS/SSL for connectivity to etcd.
     - bool
     - ``false``
   * - :spellingexternalIPs.enabled
     - Enable ExternalIPs service support.
     - bool
     - ``false``
   * - :spellingexternalWorkloads
     - Configure external workloads support
     - object
     - ``{"enabled":false}``
   * - :spellingexternalWorkloads.enabled
     - Enable support for external workloads, such as VMs (false by default).
     - bool
     - ``false``
   * - :spellingextraArgs
     - Additional agent container arguments.
     - list
     - ``[]``
   * - :spellingextraConfig
     - extraConfig allows you to specify additional configuration parameters to be included in the cilium-config configmap.
     - object
     - ``{}``
   * - :spellingextraContainers
     - Additional containers added to the cilium DaemonSet.
     - list
     - ``[]``
   * - :spellingextraEnv
     - Additional agent container environment variables.
     - list
     - ``[]``
   * - :spellingextraHostPathMounts
     - Additional agent hostPath mounts.
     - list
     - ``[]``
   * - :spellingextraInitContainers
     - Additional initContainers added to the cilium Daemonset.
     - list
     - ``[]``
   * - :spellingextraVolumeMounts
     - Additional agent volumeMounts.
     - list
     - ``[]``
   * - :spellingextraVolumes
     - Additional agent volumes.
     - list
     - ``[]``
   * - :spellingforceDeviceDetection
     - Forces the auto-detection of devices, even if specific devices are explicitly listed
     - bool
     - ``false``
   * - :spellinggatewayAPI.enableAlpn
     - Enable ALPN for all listeners configured with Gateway API. ALPN will attempt HTTP/2, then HTTP 1.1. Note that this will also enable ``appProtocol`` support, and services that wish to use HTTP/2 will need to indicate that via their ``appProtocol``.
     - bool
     - ``false``
   * - :spellinggatewayAPI.enableAppProtocol
     - Enable Backend Protocol selection support (GEP-1911) for Gateway API via appProtocol.
     - bool
     - ``false``
   * - :spellinggatewayAPI.enableProxyProtocol
     - Enable proxy protocol for all GatewayAPI listeners. Note that *only* Proxy protocol traffic will be accepted once this is enabled.
     - bool
     - ``false``
   * - :spellinggatewayAPI.enabled
     - Enable support for Gateway API in cilium This will automatically set enable-envoy-config as well.
     - bool
     - ``false``
   * - :spellinggatewayAPI.externalTrafficPolicy
     - Control how traffic from external sources is routed to the LoadBalancer Kubernetes Service for all Cilium GatewayAPI Gateway instances. Valid values are "Cluster" and "Local". Note that this value will be ignored when ``hostNetwork.enabled == true``. ref: https://kubernetes.io/docs/reference/networking/virtual-ips/#external-traffic-policy
     - string
     - ``"Cluster"``
   * - :spellinggatewayAPI.gatewayClass.create
     - Enable creation of GatewayClass resource The default value is 'auto' which decides according to presence of gateway.networking.k8s.io/v1/GatewayClass in the cluster. Other possible values are 'true' and 'false', which will either always or never create the GatewayClass, respectively.
     - string
     - ``"auto"``
   * - :spellinggatewayAPI.hostNetwork.enabled
     - Configure whether the Envoy listeners should be exposed on the host network.
     - bool
     - ``false``
   * - :spellinggatewayAPI.hostNetwork.nodes.matchLabels
     - Specify the labels of the nodes where the Ingress listeners should be exposed  matchLabels:   kubernetes.io/os: linux   kubernetes.io/hostname: kind-worker
     - object
     - ``{}``
   * - :spellinggatewayAPI.secretsNamespace
     - SecretsNamespace is the namespace in which envoy SDS will retrieve TLS secrets from.
     - object
     - ``{"create":true,"name":"cilium-secrets","sync":true}``
   * - :spellinggatewayAPI.secretsNamespace.create
     - Create secrets namespace for Gateway API.
     - bool
     - ``true``
   * - :spellinggatewayAPI.secretsNamespace.name
     - Name of Gateway API secret namespace.
     - string
     - ``"cilium-secrets"``
   * - :spellinggatewayAPI.secretsNamespace.sync
     - Enable secret sync, which will make sure all TLS secrets used by Ingress are synced to secretsNamespace.name. If disabled, TLS secrets must be maintained externally.
     - bool
     - ``true``
   * - :spellinggatewayAPI.xffNumTrustedHops
     - The number of additional GatewayAPI proxy hops from the right side of the HTTP header to trust when determining the origin client's IP address.
     - int
     - ``0``
   * - :spellinggke.enabled
     - Enable Google Kubernetes Engine integration
     - bool
     - ``false``
   * - :spellinghealthChecking
     - Enable connectivity health checking.
     - bool
     - ``true``
   * - :spellinghealthPort
     - TCP port for the agent health API. This is not the port for cilium-health.
     - int
     - ``9879``
   * - :spellinghighScaleIPcache
     - EnableHighScaleIPcache enables the special ipcache mode for high scale clusters. The ipcache content will be reduced to the strict minimum and traffic will be encapsulated to carry security identities.
     - object
     - ``{"enabled":false}``
   * - :spellinghighScaleIPcache.enabled
     - Enable the high scale mode for the ipcache.
     - bool
     - ``false``
   * - :spellinghostFirewall
     - Configure the host firewall.
     - object
     - ``{"enabled":false}``
   * - :spellinghostFirewall.enabled
     - Enables the enforcement of host policies in the eBPF datapath.
     - bool
     - ``false``
   * - :spellinghostPort.enabled
     - Enable hostPort service support.
     - bool
     - ``false``
   * - :spellinghubble.annotations
     - Annotations to be added to all top-level hubble objects (resources under templates/hubble)
     - object
     - ``{}``
   * - :spellinghubble.dropEventEmitter
     - Emit v1.Events related to pods on detection of packet drops.    This feature is alpha, please provide feedback at https://github.com/cilium/cilium/issues/33975.
     - object
     - ``{"enabled":false,"interval":"2m","reasons":["auth_required","policy_denied"]}``
   * - :spellinghubble.dropEventEmitter.interval
     - - Minimum time between emitting same events.
     - string
     - ``"2m"``
   * - :spellinghubble.dropEventEmitter.reasons
     - - Drop reasons to emit events for. ref: https://docs.cilium.io/en/stable/_api/v1/flow/README/#dropreason
     - list
     - ``["auth_required","policy_denied"]``
   * - :spellinghubble.enabled
     - Enable Hubble (true by default).
     - bool
     - ``true``
   * - :spellinghubble.export
     - Hubble flows export.
     - object
     - ``{"dynamic":{"config":{"configMapName":"cilium-flowlog-config","content":[{"excludeFilters":[],"fieldMask":[],"filePath":"/var/run/cilium/hubble/events.log","includeFilters":[],"name":"all"}],"createConfigMap":true},"enabled":false},"fileMaxBackups":5,"fileMaxSizeMb":10,"static":{"allowList":[],"denyList":[],"enabled":false,"fieldMask":[],"filePath":"/var/run/cilium/hubble/events.log"}}``
   * - :spellinghubble.export.dynamic
     - - Dynamic exporters configuration. Dynamic exporters may be reconfigured without a need of agent restarts.
     - object
     - ``{"config":{"configMapName":"cilium-flowlog-config","content":[{"excludeFilters":[],"fieldMask":[],"filePath":"/var/run/cilium/hubble/events.log","includeFilters":[],"name":"all"}],"createConfigMap":true},"enabled":false}``
   * - :spellinghubble.export.dynamic.config.configMapName
     - -- Name of configmap with configuration that may be altered to reconfigure exporters within a running agents.
     - string
     - ``"cilium-flowlog-config"``
   * - :spellinghubble.export.dynamic.config.content
     - -- Exporters configuration in YAML format.
     - list
     - ``[{"excludeFilters":[],"fieldMask":[],"filePath":"/var/run/cilium/hubble/events.log","includeFilters":[],"name":"all"}]``
   * - :spellinghubble.export.dynamic.config.createConfigMap
     - -- True if helm installer should create config map. Switch to false if you want to self maintain the file content.
     - bool
     - ``true``
   * - :spellinghubble.export.fileMaxBackups
     - - Defines max number of backup/rotated files.
     - int
     - ``5``
   * - :spellinghubble.export.fileMaxSizeMb
     - - Defines max file size of output file before it gets rotated.
     - int
     - ``10``
   * - :spellinghubble.export.static
     - - Static exporter configuration. Static exporter is bound to agent lifecycle.
     - object
     - ``{"allowList":[],"denyList":[],"enabled":false,"fieldMask":[],"filePath":"/var/run/cilium/hubble/events.log"}``
   * - :spellinghubble.listenAddress
     - An additional address for Hubble to listen to. Set this field ":4244" if you are enabling Hubble Relay, as it assumes that Hubble is listening on port 4244.
     - string
     - ``":4244"``
   * - :spellinghubble.metrics
     - Hubble metrics configuration. See https://docs.cilium.io/en/stable/observability/metrics/#hubble-metrics for more comprehensive documentation about Hubble metrics.
     - object
     - ``{"dashboards":{"annotations":{},"enabled":false,"label":"grafana_dashboard","labelValue":"1","namespace":null},"enableOpenMetrics":false,"enabled":null,"port":9965,"serviceAnnotations":{},"serviceMonitor":{"annotations":{},"enabled":false,"interval":"10s","jobLabel":"","labels":{},"metricRelabelings":null,"relabelings":[{"replacement":"${1}","sourceLabels":["__meta_kubernetes_pod_node_name"],"targetLabel":"node"}],"tlsConfig":{}},"tls":{"enabled":false,"server":{"cert":"","existingSecret":"","extraDnsNames":[],"extraIpAddresses":[],"key":"","mtls":{"enabled":false,"key":"ca.crt","name":null,"useSecret":false}}}}``
   * - :spellinghubble.metrics.dashboards
     - Grafana dashboards for hubble grafana can import dashboards based on the label and value ref: https://github.com/grafana/helm-charts/tree/main/charts/grafana#sidecar-for-dashboards
     - object
     - ``{"annotations":{},"enabled":false,"label":"grafana_dashboard","labelValue":"1","namespace":null}``
   * - :spellinghubble.metrics.enableOpenMetrics
     - Enables exporting hubble metrics in OpenMetrics format.
     - bool
     - ``false``
   * - :spellinghubble.metrics.enabled
     - Configures the list of metrics to collect. If empty or null, metrics are disabled. Example:    enabled:   - dns:query;ignoreAAAA   - drop   - tcp   - flow   - icmp   - http  You can specify the list of metrics from the helm CLI:    --set hubble.metrics.enabled="{dns:query;ignoreAAAA,drop,tcp,flow,icmp,http}"
     - string
     - ``nil``
   * - :spellinghubble.metrics.port
     - Configure the port the hubble metric server listens on.
     - int
     - ``9965``
   * - :spellinghubble.metrics.serviceAnnotations
     - Annotations to be added to hubble-metrics service.
     - object
     - ``{}``
   * - :spellinghubble.metrics.serviceMonitor.annotations
     - Annotations to add to ServiceMonitor hubble
     - object
     - ``{}``
   * - :spellinghubble.metrics.serviceMonitor.enabled
     - Create ServiceMonitor resources for Prometheus Operator. This requires the prometheus CRDs to be available. ref: https://github.com/prometheus-operator/prometheus-operator/blob/main/example/prometheus-operator-crd/monitoring.coreos.com_servicemonitors.yaml)
     - bool
     - ``false``
   * - :spellinghubble.metrics.serviceMonitor.interval
     - Interval for scrape metrics.
     - string
     - ``"10s"``
   * - :spellinghubble.metrics.serviceMonitor.jobLabel
     - jobLabel to add for ServiceMonitor hubble
     - string
     - ``""``
   * - :spellinghubble.metrics.serviceMonitor.labels
     - Labels to add to ServiceMonitor hubble
     - object
     - ``{}``
   * - :spellinghubble.metrics.serviceMonitor.metricRelabelings
     - Metrics relabeling configs for the ServiceMonitor hubble
     - string
     - ``nil``
   * - :spellinghubble.metrics.serviceMonitor.relabelings
     - Relabeling configs for the ServiceMonitor hubble
     - list
     - ``[{"replacement":"${1}","sourceLabels":["__meta_kubernetes_pod_node_name"],"targetLabel":"node"}]``
   * - :spellinghubble.metrics.tls.server.cert
     - base64 encoded PEM values for the Hubble metrics server certificate (deprecated). Use existingSecret instead.
     - string
     - ``""``
   * - :spellinghubble.metrics.tls.server.existingSecret
     - Name of the Secret containing the certificate and key for the Hubble metrics server. If specified, cert and key are ignored.
     - string
     - ``""``
   * - :spellinghubble.metrics.tls.server.extraDnsNames
     - Extra DNS names added to certificate when it's auto generated
     - list
     - ``[]``
   * - :spellinghubble.metrics.tls.server.extraIpAddresses
     - Extra IP addresses added to certificate when it's auto generated
     - list
     - ``[]``
   * - :spellinghubble.metrics.tls.server.key
     - base64 encoded PEM values for the Hubble metrics server key (deprecated). Use existingSecret instead.
     - string
     - ``""``
   * - :spellinghubble.metrics.tls.server.mtls
     - Configure mTLS for the Hubble metrics server.
     - object
     - ``{"enabled":false,"key":"ca.crt","name":null,"useSecret":false}``
   * - :spellinghubble.metrics.tls.server.mtls.key
     - Entry of the ConfigMap containing the CA.
     - string
     - ``"ca.crt"``
   * - :spellinghubble.metrics.tls.server.mtls.name
     - Name of the ConfigMap containing the CA to validate client certificates against. If mTLS is enabled and this is unspecified, it will default to the same CA used for Hubble metrics server certificates.
     - string
     - ``nil``
   * - :spellinghubble.peerService.clusterDomain
     - The cluster domain to use to query the Hubble Peer service. It should be the local cluster.
     - string
     - ``"cluster.local"``
   * - :spellinghubble.peerService.targetPort
     - Target Port for the Peer service, must match the hubble.listenAddress' port.
     - int
     - ``4244``
   * - :spellinghubble.preferIpv6
     - Whether Hubble should prefer to announce IPv6 or IPv4 addresses if both are available.
     - bool
     - ``false``
   * - :spellinghubble.redact
     - Enables redacting sensitive information present in Layer 7 flows.
     - object
     - ``{"enabled":false,"http":{"headers":{"allow":[],"deny":[]},"urlQuery":false,"userInfo":true},"kafka":{"apiKey":false}}``
   * - :spellinghubble.redact.http.headers.allow
     - List of HTTP headers to allow: headers not matching will be redacted. Note: ``allow`` and ``deny`` lists cannot be used both at the same time, only one can be present. Example:   redact:     enabled: true     http:       headers:         allow:           - traceparent           - tracestate           - Cache-Control  You can specify the options from the helm CLI:   --set hubble.redact.enabled="true"   --set hubble.redact.http.headers.allow="traceparent,tracestate,Cache-Control"
     - list
     - ``[]``
   * - :spellinghubble.redact.http.headers.deny
     - List of HTTP headers to deny: matching headers will be redacted. Note: ``allow`` and ``deny`` lists cannot be used both at the same time, only one can be present. Example:   redact:     enabled: true     http:       headers:         deny:           - Authorization           - Proxy-Authorization  You can specify the options from the helm CLI:   --set hubble.redact.enabled="true"   --set hubble.redact.http.headers.deny="Authorization,Proxy-Authorization"
     - list
     - ``[]``
   * - :spellinghubble.redact.http.urlQuery
     - Enables redacting URL query (GET) parameters. Example:    redact:     enabled: true     http:       urlQuery: true  You can specify the options from the helm CLI:    --set hubble.redact.enabled="true"   --set hubble.redact.http.urlQuery="true"
     - bool
     - ``false``
   * - :spellinghubble.redact.http.userInfo
     - Enables redacting user info, e.g., password when basic auth is used. Example:    redact:     enabled: true     http:       userInfo: true  You can specify the options from the helm CLI:    --set hubble.redact.enabled="true"   --set hubble.redact.http.userInfo="true"
     - bool
     - ``true``
   * - :spellinghubble.redact.kafka.apiKey
     - Enables redacting Kafka's API key. Example:    redact:     enabled: true     kafka:       apiKey: true  You can specify the options from the helm CLI:    --set hubble.redact.enabled="true"   --set hubble.redact.kafka.apiKey="true"
     - bool
     - ``false``
   * - :spellinghubble.relay.affinity
     - Affinity for hubble-replay
     - object
     - ``{"podAffinity":{"requiredDuringSchedulingIgnoredDuringExecution":[{"labelSelector":{"matchLabels":{"k8s-app":"cilium"}},"topologyKey":"kubernetes.io/hostname"}]}}``
   * - :spellinghubble.relay.annotations
     - Annotations to be added to all top-level hubble-relay objects (resources under templates/hubble-relay)
     - object
     - ``{}``
   * - :spellinghubble.relay.dialTimeout
     - Dial timeout to connect to the local hubble instance to receive peer information (e.g. "30s").
     - string
     - ``nil``
   * - :spellinghubble.relay.enabled
     - Enable Hubble Relay (requires hubble.enabled=true)
     - bool
     - ``false``
   * - :spellinghubble.relay.extraEnv
     - Additional hubble-relay environment variables.
     - list
     - ``[]``
   * - :spellinghubble.relay.extraVolumeMounts
     - Additional hubble-relay volumeMounts.
     - list
     - ``[]``
   * - :spellinghubble.relay.extraVolumes
     - Additional hubble-relay volumes.
     - list
     - ``[]``
   * - :spellinghubble.relay.gops.enabled
     - Enable gops for hubble-relay
     - bool
     - ``true``
   * - :spellinghubble.relay.gops.port
     - Configure gops listen port for hubble-relay
     - int
     - ``9893``
   * - :spellinghubble.relay.image
     - Hubble-relay container image.
     - object
     - ``{"digest":"","override":null,"pullPolicy":"IfNotPresent","repository":"quay.io/cilium/hubble-relay","tag":"v1.16.7","useDigest":false}``
   * - :spellinghubble.relay.listenHost
     - Host to listen to. Specify an empty string to bind to all the interfaces.
     - string
     - ``""``
   * - :spellinghubble.relay.listenPort
     - Port to listen to.
     - string
     - ``"4245"``
   * - :spellinghubble.relay.nodeSelector
     - Node labels for pod assignment ref: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector
     - object
     - ``{"kubernetes.io/os":"linux"}``
   * - :spellinghubble.relay.podAnnotations
     - Annotations to be added to hubble-relay pods
     - object
     - ``{}``
   * - :spellinghubble.relay.podDisruptionBudget.enabled
     - enable PodDisruptionBudget ref: https://kubernetes.io/docs/concepts/workloads/pods/disruptions/
     - bool
     - ``false``
   * - :spellinghubble.relay.podDisruptionBudget.maxUnavailable
     - Maximum number/percentage of pods that may be made unavailable
     - int
     - ``1``
   * - :spellinghubble.relay.podDisruptionBudget.minAvailable
     - Minimum number/percentage of pods that should remain scheduled. When it's set, maxUnavailable must be disabled by ``maxUnavailable: null``
     - string
     - ``nil``
   * - :spellinghubble.relay.podLabels
     - Labels to be added to hubble-relay pods
     - object
     - ``{}``
   * - :spellinghubble.relay.podSecurityContext
     - hubble-relay pod security context
     - object
     - ``{"fsGroup":65532}``
   * - :spellinghubble.relay.pprof.address
     - Configure pprof listen address for hubble-relay
     - string
     - ``"localhost"``
   * - :spellinghubble.relay.pprof.enabled
     - Enable pprof for hubble-relay
     - bool
     - ``false``
   * - :spellinghubble.relay.pprof.port
     - Configure pprof listen port for hubble-relay
     - int
     - ``6062``
   * - :spellinghubble.relay.priorityClassName
     - The priority class to use for hubble-relay
     - string
     - ``""``
   * - :spellinghubble.relay.prometheus
     - Enable prometheus metrics for hubble-relay on the configured port at /metrics
     - object
     - ``{"enabled":false,"port":9966,"serviceMonitor":{"annotations":{},"enabled":false,"interval":"10s","labels":{},"metricRelabelings":null,"relabelings":null}}``
   * - :spellinghubble.relay.prometheus.serviceMonitor.annotations
     - Annotations to add to ServiceMonitor hubble-relay
     - object
     - ``{}``
   * - :spellinghubble.relay.prometheus.serviceMonitor.enabled
     - Enable service monitors. This requires the prometheus CRDs to be available (see https://github.com/prometheus-operator/prometheus-operator/blob/main/example/prometheus-operator-crd/monitoring.coreos.com_servicemonitors.yaml)
     - bool
     - ``false``
   * - :spellinghubble.relay.prometheus.serviceMonitor.interval
     - Interval for scrape metrics.
     - string
     - ``"10s"``
   * - :spellinghubble.relay.prometheus.serviceMonitor.labels
     - Labels to add to ServiceMonitor hubble-relay
     - object
     - ``{}``
   * - :spellinghubble.relay.prometheus.serviceMonitor.metricRelabelings
     - Metrics relabeling configs for the ServiceMonitor hubble-relay
     - string
     - ``nil``
   * - :spellinghubble.relay.prometheus.serviceMonitor.relabelings
     - Relabeling configs for the ServiceMonitor hubble-relay
     - string
     - ``nil``
   * - :spellinghubble.relay.replicas
     - Number of replicas run for the hubble-relay deployment.
     - int
     - ``1``
   * - :spellinghubble.relay.resources
     - Specifies the resources for the hubble-relay pods
     - object
     - ``{}``
   * - :spellinghubble.relay.retryTimeout
     - Backoff duration to retry connecting to the local hubble instance in case of failure (e.g. "30s").
     - string
     - ``nil``
   * - :spellinghubble.relay.rollOutPods
     - Roll out Hubble Relay pods automatically when configmap is updated.
     - bool
     - ``false``
   * - :spellinghubble.relay.securityContext
     - hubble-relay container security context
     - object
     - ``{"capabilities":{"drop":["ALL"]},"runAsGroup":65532,"runAsNonRoot":true,"runAsUser":65532}``
   * - :spellinghubble.relay.service
     - hubble-relay service configuration.
     - object
     - ``{"nodePort":31234,"type":"ClusterIP"}``
   * - :spellinghubble.relay.service.nodePort
     - - The port to use when the service type is set to NodePort.
     - int
     - ``31234``
   * - :spellinghubble.relay.service.type
     - - The type of service used for Hubble Relay access, either ClusterIP or NodePort.
     - string
     - ``"ClusterIP"``
   * - :spellinghubble.relay.sortBufferDrainTimeout
     - When the per-request flows sort buffer is not full, a flow is drained every time this timeout is reached (only affects requests in follow-mode) (e.g. "1s").
     - string
     - ``nil``
   * - :spellinghubble.relay.sortBufferLenMax
     - Max number of flows that can be buffered for sorting before being sent to the client (per request) (e.g. 100).
     - int
     - ``nil``
   * - :spellinghubble.relay.terminationGracePeriodSeconds
     - Configure termination grace period for hubble relay Deployment.
     - int
     - ``1``
   * - :spellinghubble.relay.tls
     - TLS configuration for Hubble Relay
     - object
     - ``{"client":{"cert":"","existingSecret":"","key":""},"server":{"cert":"","enabled":false,"existingSecret":"","extraDnsNames":[],"extraIpAddresses":[],"key":"","mtls":false,"relayName":"ui.hubble-relay.cilium.io"}}``
   * - :spellinghubble.relay.tls.client
     - The hubble-relay client certificate and private key. This keypair is presented to Hubble server instances for mTLS authentication and is required when hubble.tls.enabled is true. These values need to be set manually if hubble.tls.auto.enabled is false.
     - object
     - ``{"cert":"","existingSecret":"","key":""}``
   * - :spellinghubble.relay.tls.client.cert
     - base64 encoded PEM values for the Hubble relay client certificate (deprecated). Use existingSecret instead.
     - string
     - ``""``
   * - :spellinghubble.relay.tls.client.existingSecret
     - Name of the Secret containing the certificate and key for the Hubble metrics server. If specified, cert and key are ignored.
     - string
     - ``""``
   * - :spellinghubble.relay.tls.client.key
     - base64 encoded PEM values for the Hubble relay client key (deprecated). Use existingSecret instead.
     - string
     - ``""``
   * - :spellinghubble.relay.tls.server
     - The hubble-relay server certificate and private key
     - object
     - ``{"cert":"","enabled":false,"existingSecret":"","extraDnsNames":[],"extraIpAddresses":[],"key":"","mtls":false,"relayName":"ui.hubble-relay.cilium.io"}``
   * - :spellinghubble.relay.tls.server.cert
     - base64 encoded PEM values for the Hubble relay server certificate (deprecated). Use existingSecret instead.
     - string
     - ``""``
   * - :spellinghubble.relay.tls.server.existingSecret
     - Name of the Secret containing the certificate and key for the Hubble relay server. If specified, cert and key are ignored.
     - string
     - ``""``
   * - :spellinghubble.relay.tls.server.extraDnsNames
     - extra DNS names added to certificate when its auto gen
     - list
     - ``[]``
   * - :spellinghubble.relay.tls.server.extraIpAddresses
     - extra IP addresses added to certificate when its auto gen
     - list
     - ``[]``
   * - :spellinghubble.relay.tls.server.key
     - base64 encoded PEM values for the Hubble relay server key (deprecated). Use existingSecret instead.
     - string
     - ``""``
   * - :spellinghubble.relay.tolerations
     - Node tolerations for pod assignment on nodes with taints ref: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
     - list
     - ``[]``
   * - :spellinghubble.relay.topologySpreadConstraints
     - Pod topology spread constraints for hubble-relay
     - list
     - ``[]``
   * - :spellinghubble.relay.updateStrategy
     - hubble-relay update strategy
     - object
     - ``{"rollingUpdate":{"maxUnavailable":1},"type":"RollingUpdate"}``
   * - :spellinghubble.skipUnknownCGroupIDs
     - Skip Hubble events with unknown cgroup ids
     - bool
     - ``true``
   * - :spellinghubble.socketPath
     - Unix domain socket path to listen to when Hubble is enabled.
     - string
     - ``"/var/run/cilium/hubble.sock"``
   * - :spellinghubble.tls
     - TLS configuration for Hubble
     - object
     - ``{"auto":{"certManagerIssuerRef":{},"certValidityDuration":365,"enabled":true,"method":"helm","schedule":"0 0 1 */4 *"},"enabled":true,"server":{"cert":"","existingSecret":"","extraDnsNames":[],"extraIpAddresses":[],"key":""}}``
   * - :spellinghubble.tls.auto
     - Configure automatic TLS certificates generation.
     - object
     - ``{"certManagerIssuerRef":{},"certValidityDuration":365,"enabled":true,"method":"helm","schedule":"0 0 1 */4 *"}``
   * - :spellinghubble.tls.auto.certManagerIssuerRef
     - certmanager issuer used when hubble.tls.auto.method=certmanager.
     - object
     - ``{}``
   * - :spellinghubble.tls.auto.certValidityDuration
     - Generated certificates validity duration in days.  Defaults to 365 days (1 year) because MacOS does not accept self-signed certificates with expirations > 825 days.
     - int
     - ``365``
   * - :spellinghubble.tls.auto.enabled
     - Auto-generate certificates. When set to true, automatically generate a CA and certificates to enable mTLS between Hubble server and Hubble Relay instances. If set to false, the certs for Hubble server need to be provided by setting appropriate values below.
     - bool
     - ``true``
   * - :spellinghubble.tls.auto.method
     - Set the method to auto-generate certificates. Supported values: - helm:         This method uses Helm to generate all certificates. - cronJob:      This method uses a Kubernetes CronJob the generate any                 certificates not provided by the user at installation                 time. - certmanager:  This method use cert-manager to generate & rotate certificates.
     - string
     - ``"helm"``
   * - :spellinghubble.tls.auto.schedule
     - Schedule for certificates regeneration (regardless of their expiration date). Only used if method is "cronJob". If nil, then no recurring job will be created. Instead, only the one-shot job is deployed to generate the certificates at installation time.  Defaults to midnight of the first day of every fourth month. For syntax, see https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#schedule-syntax
     - string
     - ``"0 0 1 */4 *"``
   * - :spellinghubble.tls.enabled
     - Enable mutual TLS for listenAddress. Setting this value to false is highly discouraged as the Hubble API provides access to potentially sensitive network flow metadata and is exposed on the host network.
     - bool
     - ``true``
   * - :spellinghubble.tls.server
     - The Hubble server certificate and private key
     - object
     - ``{"cert":"","existingSecret":"","extraDnsNames":[],"extraIpAddresses":[],"key":""}``
   * - :spellinghubble.tls.server.cert
     - base64 encoded PEM values for the Hubble server certificate (deprecated). Use existingSecret instead.
     - string
     - ``""``
   * - :spellinghubble.tls.server.existingSecret
     - Name of the Secret containing the certificate and key for the Hubble server. If specified, cert and key are ignored.
     - string
     - ``""``
   * - :spellinghubble.tls.server.extraDnsNames
     - Extra DNS names added to certificate when it's auto generated
     - list
     - ``[]``
   * - :spellinghubble.tls.server.extraIpAddresses
     - Extra IP addresses added to certificate when it's auto generated
     - list
     - ``[]``
   * - :spellinghubble.tls.server.key
     - base64 encoded PEM values for the Hubble server key (deprecated). Use existingSecret instead.
     - string
     - ``""``
   * - :spellinghubble.ui.affinity
     - Affinity for hubble-ui
     - object
     - ``{}``
   * - :spellinghubble.ui.annotations
     - Annotations to be added to all top-level hubble-ui objects (resources under templates/hubble-ui)
     - object
     - ``{}``
   * - :spellinghubble.ui.backend.extraEnv
     - Additional hubble-ui backend environment variables.
     - list
     - ``[]``
   * - :spellinghubble.ui.backend.extraVolumeMounts
     - Additional hubble-ui backend volumeMounts.
     - list
     - ``[]``
   * - :spellinghubble.ui.backend.extraVolumes
     - Additional hubble-ui backend volumes.
     - list
     - ``[]``
   * - :spellinghubble.ui.backend.image
     - Hubble-ui backend image.
     - object
     - ``{"digest":"sha256:0e0eed917653441fded4e7cdb096b7be6a3bddded5a2dd10812a27b1fc6ed95b","override":null,"pullPolicy":"IfNotPresent","repository":"quay.io/cilium/hubble-ui-backend","tag":"v0.13.1","useDigest":true}``
   * - :spellinghubble.ui.backend.livenessProbe.enabled
     - Enable liveness probe for Hubble-ui backend (requires Hubble-ui 0.12+)
     - bool
     - ``false``
   * - :spellinghubble.ui.backend.readinessProbe.enabled
     - Enable readiness probe for Hubble-ui backend (requires Hubble-ui 0.12+)
     - bool
     - ``false``
   * - :spellinghubble.ui.backend.resources
     - Resource requests and limits for the 'backend' container of the 'hubble-ui' deployment.
     - object
     - ``{}``
   * - :spellinghubble.ui.backend.securityContext
     - Hubble-ui backend security context.
     - object
     - ``{}``
   * - :spellinghubble.ui.baseUrl
     - Defines base url prefix for all hubble-ui http requests. It needs to be changed in case if ingress for hubble-ui is configured under some sub-path. Trailing ``/`` is required for custom path, ex. ``/service-map/``
     - string
     - ``"/"``
   * - :spellinghubble.ui.enabled
     - Whether to enable the Hubble UI.
     - bool
     - ``false``
   * - :spellinghubble.ui.frontend.extraEnv
     - Additional hubble-ui frontend environment variables.
     - list
     - ``[]``
   * - :spellinghubble.ui.frontend.extraVolumeMounts
     - Additional hubble-ui frontend volumeMounts.
     - list
     - ``[]``
   * - :spellinghubble.ui.frontend.extraVolumes
     - Additional hubble-ui frontend volumes.
     - list
     - ``[]``
   * - :spellinghubble.ui.frontend.image
     - Hubble-ui frontend image.
     - object
     - ``{"digest":"sha256:e2e9313eb7caf64b0061d9da0efbdad59c6c461f6ca1752768942bfeda0796c6","override":null,"pullPolicy":"IfNotPresent","repository":"quay.io/cilium/hubble-ui","tag":"v0.13.1","useDigest":true}``
   * - :spellinghubble.ui.frontend.resources
     - Resource requests and limits for the 'frontend' container of the 'hubble-ui' deployment.
     - object
     - ``{}``
   * - :spellinghubble.ui.frontend.securityContext
     - Hubble-ui frontend security context.
     - object
     - ``{}``
   * - :spellinghubble.ui.frontend.server.ipv6
     - Controls server listener for ipv6
     - object
     - ``{"enabled":true}``
   * - :spellinghubble.ui.ingress
     - hubble-ui ingress configuration.
     - object
     - ``{"annotations":{},"className":"","enabled":false,"hosts":["chart-example.local"],"labels":{},"tls":[]}``
   * - :spellinghubble.ui.nodeSelector
     - Node labels for pod assignment ref: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector
     - object
     - ``{"kubernetes.io/os":"linux"}``
   * - :spellinghubble.ui.podAnnotations
     - Annotations to be added to hubble-ui pods
     - object
     - ``{}``
   * - :spellinghubble.ui.podDisruptionBudget.enabled
     - enable PodDisruptionBudget ref: https://kubernetes.io/docs/concepts/workloads/pods/disruptions/
     - bool
     - ``false``
   * - :spellinghubble.ui.podDisruptionBudget.maxUnavailable
     - Maximum number/percentage of pods that may be made unavailable
     - int
     - ``1``
   * - :spellinghubble.ui.podDisruptionBudget.minAvailable
     - Minimum number/percentage of pods that should remain scheduled. When it's set, maxUnavailable must be disabled by ``maxUnavailable: null``
     - string
     - ``nil``
   * - :spellinghubble.ui.podLabels
     - Labels to be added to hubble-ui pods
     - object
     - ``{}``
   * - :spellinghubble.ui.priorityClassName
     - The priority class to use for hubble-ui
     - string
     - ``""``
   * - :spellinghubble.ui.replicas
     - The number of replicas of Hubble UI to deploy.
     - int
     - ``1``
   * - :spellinghubble.ui.rollOutPods
     - Roll out Hubble-ui pods automatically when configmap is updated.
     - bool
     - ``false``
   * - :spellinghubble.ui.securityContext
     - Security context to be added to Hubble UI pods
     - object
     - ``{"fsGroup":1001,"runAsGroup":1001,"runAsUser":1001}``
   * - :spellinghubble.ui.service
     - hubble-ui service configuration.
     - object
     - ``{"annotations":{},"nodePort":31235,"type":"ClusterIP"}``
   * - :spellinghubble.ui.service.annotations
     - Annotations to be added for the Hubble UI service
     - object
     - ``{}``
   * - :spellinghubble.ui.service.nodePort
     - - The port to use when the service type is set to NodePort.
     - int
     - ``31235``
   * - :spellinghubble.ui.service.type
     - - The type of service used for Hubble UI access, either ClusterIP or NodePort.
     - string
     - ``"ClusterIP"``
   * - :spellinghubble.ui.standalone.enabled
     - When true, it will allow installing the Hubble UI only, without checking dependencies. It is useful if a cluster already has cilium and Hubble relay installed and you just want Hubble UI to be deployed. When installed via helm, installing UI should be done via ``helm upgrade`` and when installed via the cilium cli, then ``cilium hubble enable --ui``
     - bool
     - ``false``
   * - :spellinghubble.ui.standalone.tls.certsVolume
     - When deploying Hubble UI in standalone, with tls enabled for Hubble relay, it is required to provide a volume for mounting the client certificates.
     - object
     - ``{}``
   * - :spellinghubble.ui.tls.client.cert
     - base64 encoded PEM values for the Hubble UI client certificate (deprecated). Use existingSecret instead.
     - string
     - ``""``
   * - :spellinghubble.ui.tls.client.existingSecret
     - Name of the Secret containing the client certificate and key for Hubble UI If specified, cert and key are ignored.
     - string
     - ``""``
   * - :spellinghubble.ui.tls.client.key
     - base64 encoded PEM values for the Hubble UI client key (deprecated). Use existingSecret instead.
     - string
     - ``""``
   * - :spellinghubble.ui.tolerations
     - Node tolerations for pod assignment on nodes with taints ref: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
     - list
     - ``[]``
   * - :spellinghubble.ui.topologySpreadConstraints
     - Pod topology spread constraints for hubble-ui
     - list
     - ``[]``
   * - :spellinghubble.ui.updateStrategy
     - hubble-ui update strategy.
     - object
     - ``{"rollingUpdate":{"maxUnavailable":1},"type":"RollingUpdate"}``
   * - :spellingidentityAllocationMode
     - Method to use for identity allocation (\ ``crd`` or ``kvstore``\ ).
     - string
     - ``"crd"``
   * - :spellingidentityChangeGracePeriod
     - Time to wait before using new identity on endpoint identity change.
     - string
     - ``"5s"``
   * - :spellingimage
     - Agent container image.
     - object
     - ``{"digest":"","override":null,"pullPolicy":"IfNotPresent","repository":"quay.io/cilium/cilium","tag":"v1.16.7","useDigest":false}``
   * - :spellingimagePullSecrets
     - Configure image pull secrets for pulling container images
     - list
     - ``[]``
   * - :spellingingressController.default
     - Set cilium ingress controller to be the default ingress controller This will let cilium ingress controller route entries without ingress class set
     - bool
     - ``false``
   * - :spellingingressController.defaultSecretName
     - Default secret name for ingresses without .spec.tls[].secretName set.
     - string
     - ``nil``
   * - :spellingingressController.defaultSecretNamespace
     - Default secret namespace for ingresses without .spec.tls[].secretName set.
     - string
     - ``nil``
   * - :spellingingressController.enableProxyProtocol
     - Enable proxy protocol for all Ingress listeners. Note that *only* Proxy protocol traffic will be accepted once this is enabled.
     - bool
     - ``false``
   * - :spellingingressController.enabled
     - Enable cilium ingress controller This will automatically set enable-envoy-config as well.
     - bool
     - ``false``
   * - :spellingingressController.enforceHttps
     - Enforce https for host having matching TLS host in Ingress. Incoming traffic to http listener will return 308 http error code with respective location in header.
     - bool
     - ``true``
   * - :spellingingressController.hostNetwork.enabled
     - Configure whether the Envoy listeners should be exposed on the host network.
     - bool
     - ``false``
   * - :spellingingressController.hostNetwork.nodes.matchLabels
     - Specify the labels of the nodes where the Ingress listeners should be exposed  matchLabels:   kubernetes.io/os: linux   kubernetes.io/hostname: kind-worker
     - object
     - ``{}``
   * - :spellingingressController.hostNetwork.sharedListenerPort
     - Configure a specific port on the host network that gets used for the shared listener.
     - int
     - ``8080``
   * - :spellingingressController.ingressLBAnnotationPrefixes
     - IngressLBAnnotations are the annotation and label prefixes, which are used to filter annotations and/or labels to propagate from Ingress to the Load Balancer service
     - list
     - ``["lbipam.cilium.io","nodeipam.cilium.io","service.beta.kubernetes.io","service.kubernetes.io","cloud.google.com"]``
   * - :spellingingressController.loadbalancerMode
     - Default ingress load balancer mode Supported values: shared, dedicated For granular control, use the following annotations on the ingress resource: "ingress.cilium.io/loadbalancer-mode: dedicated" (or "shared").
     - string
     - ``"dedicated"``
   * - :spellingingressController.secretsNamespace
     - SecretsNamespace is the namespace in which envoy SDS will retrieve TLS secrets from.
     - object
     - ``{"create":true,"name":"cilium-secrets","sync":true}``
   * - :spellingingressController.secretsNamespace.create
     - Create secrets namespace for Ingress.
     - bool
     - ``true``
   * - :spellingingressController.secretsNamespace.name
     - Name of Ingress secret namespace.
     - string
     - ``"cilium-secrets"``
   * - :spellingingressController.secretsNamespace.sync
     - Enable secret sync, which will make sure all TLS secrets used by Ingress are synced to secretsNamespace.name. If disabled, TLS secrets must be maintained externally.
     - bool
     - ``true``
   * - :spellingingressController.service
     - Load-balancer service in shared mode. This is a single load-balancer service for all Ingress resources.
     - object
     - ``{"allocateLoadBalancerNodePorts":null,"annotations":{},"externalTrafficPolicy":"Cluster","insecureNodePort":null,"labels":{},"loadBalancerClass":null,"loadBalancerIP":null,"name":"cilium-ingress","secureNodePort":null,"type":"LoadBalancer"}``
   * - :spellingingressController.service.allocateLoadBalancerNodePorts
     - Configure if node port allocation is required for LB service ref: https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-nodeport-allocation
     - string
     - ``nil``
   * - :spellingingressController.service.annotations
     - Annotations to be added for the shared LB service
     - object
     - ``{}``
   * - :spellingingressController.service.externalTrafficPolicy
     - Control how traffic from external sources is routed to the LoadBalancer Kubernetes Service for Cilium Ingress in shared mode. Valid values are "Cluster" and "Local". ref: https://kubernetes.io/docs/reference/networking/virtual-ips/#external-traffic-policy
     - string
     - ``"Cluster"``
   * - :spellingingressController.service.insecureNodePort
     - Configure a specific nodePort for insecure HTTP traffic on the shared LB service
     - string
     - ``nil``
   * - :spellingingressController.service.labels
     - Labels to be added for the shared LB service
     - object
     - ``{}``
   * - :spellingingressController.service.loadBalancerClass
     - Configure a specific loadBalancerClass on the shared LB service (requires Kubernetes 1.24+)
     - string
     - ``nil``
   * - :spellingingressController.service.loadBalancerIP
     - Configure a specific loadBalancerIP on the shared LB service
     - string
     - ``nil``
   * - :spellingingressController.service.name
     - Service name
     - string
     - ``"cilium-ingress"``
   * - :spellingingressController.service.secureNodePort
     - Configure a specific nodePort for secure HTTPS traffic on the shared LB service
     - string
     - ``nil``
   * - :spellingingressController.service.type
     - Service type for the shared LB service
     - string
     - ``"LoadBalancer"``
   * - :spellinginitResources
     - resources & limits for the agent init containers
     - object
     - ``{}``
   * - :spellinginstallNoConntrackIptablesRules
     - Install Iptables rules to skip netfilter connection tracking on all pod traffic. This option is only effective when Cilium is running in direct routing and full KPR mode. Moreover, this option cannot be enabled when Cilium is running in a managed Kubernetes environment or in a chained CNI setup.
     - bool
     - ``false``
   * - :spellingipMasqAgent
     - Configure the eBPF-based ip-masq-agent
     - object
     - ``{"enabled":false}``
   * - :spellingipam.ciliumNodeUpdateRate
     - Maximum rate at which the CiliumNode custom resource is updated.
     - string
     - ``"15s"``
   * - :spellingipam.mode
     - Configure IP Address Management mode. ref: https://docs.cilium.io/en/stable/network/concepts/ipam/
     - string
     - ``"cluster-pool"``
   * - :spellingipam.operator.autoCreateCiliumPodIPPools
     - IP pools to auto-create in multi-pool IPAM mode.
     - object
     - ``{}``
   * - :spellingipam.operator.clusterPoolIPv4MaskSize
     - IPv4 CIDR mask size to delegate to individual nodes for IPAM.
     - int
     - ``24``
   * - :spellingipam.operator.clusterPoolIPv4PodCIDRList
     - IPv4 CIDR list range to delegate to individual nodes for IPAM.
     - list
     - ``["10.0.0.0/8"]``
   * - :spellingipam.operator.clusterPoolIPv6MaskSize
     - IPv6 CIDR mask size to delegate to individual nodes for IPAM.
     - int
     - ``120``
   * - :spellingipam.operator.clusterPoolIPv6PodCIDRList
     - IPv6 CIDR list range to delegate to individual nodes for IPAM.
     - list
     - ``["fd00::/104"]``
   * - :spellingipam.operator.externalAPILimitBurstSize
     - The maximum burst size when rate limiting access to external APIs. Also known as the token bucket capacity.
     - int
     - ``20``
   * - :spellingipam.operator.externalAPILimitQPS
     - The maximum queries per second when rate limiting access to external APIs. Also known as the bucket refill rate, which is used to refill the bucket up to the burst size capacity.
     - float
     - ``4.0``
   * - :spellingipv4.enabled
     - Enable IPv4 support.
     - bool
     - ``true``
   * - :spellingipv4NativeRoutingCIDR
     - Allows to explicitly specify the IPv4 CIDR for native routing. When specified, Cilium assumes networking for this CIDR is preconfigured and hands traffic destined for that range to the Linux network stack without applying any SNAT. Generally speaking, specifying a native routing CIDR implies that Cilium can depend on the underlying networking stack to route packets to their destination. To offer a concrete example, if Cilium is configured to use direct routing and the Kubernetes CIDR is included in the native routing CIDR, the user must configure the routes to reach pods, either manually or by setting the auto-direct-node-routes flag.
     - string
     - ``""``
   * - :spellingipv6.enabled
     - Enable IPv6 support.
     - bool
     - ``false``
   * - :spellingipv6NativeRoutingCIDR
     - Allows to explicitly specify the IPv6 CIDR for native routing. When specified, Cilium assumes networking for this CIDR is preconfigured and hands traffic destined for that range to the Linux network stack without applying any SNAT. Generally speaking, specifying a native routing CIDR implies that Cilium can depend on the underlying networking stack to route packets to their destination. To offer a concrete example, if Cilium is configured to use direct routing and the Kubernetes CIDR is included in the native routing CIDR, the user must configure the routes to reach pods, either manually or by setting the auto-direct-node-routes flag.
     - string
     - ``""``
   * - :spellingk8s
     - Configure Kubernetes specific configuration
     - object
     - ``{"requireIPv4PodCIDR":false,"requireIPv6PodCIDR":false}``
   * - :spellingk8s.requireIPv4PodCIDR
     - requireIPv4PodCIDR enables waiting for Kubernetes to provide the PodCIDR range via the Kubernetes node resource
     - bool
     - ``false``
   * - :spellingk8s.requireIPv6PodCIDR
     - requireIPv6PodCIDR enables waiting for Kubernetes to provide the PodCIDR range via the Kubernetes node resource
     - bool
     - ``false``
   * - :spellingk8sClientRateLimit
     - Configure the client side rate limit for the agent and operator  If the amount of requests to the Kubernetes API server exceeds the configured rate limit, the agent and operator will start to throttle requests by delaying them until there is budget or the request times out.
     - object
     - ``{"burst":null,"qps":null}``
   * - :spellingk8sClientRateLimit.burst
     - The burst request rate in requests per second. The rate limiter will allow short bursts with a higher rate.
     - int
     - 10 for k8s up to 1.26. 20 for k8s version 1.27+
   * - :spellingk8sClientRateLimit.qps
     - The sustained request rate in requests per second.
     - int
     - 5 for k8s up to 1.26. 10 for k8s version 1.27+
   * - :spellingk8sNetworkPolicy.enabled
     - Enable support for K8s NetworkPolicy
     - bool
     - ``true``
   * - :spellingk8sServiceHost
     - Kubernetes service host - use "auto" for automatic lookup from the cluster-info ConfigMap (kubeadm-based clusters only)
     - string
     - ``""``
   * - :spellingk8sServicePort
     - Kubernetes service port
     - string
     - ``""``
   * - :spellingkeepDeprecatedLabels
     - Keep the deprecated selector labels when deploying Cilium DaemonSet.
     - bool
     - ``false``
   * - :spellingkeepDeprecatedProbes
     - Keep the deprecated probes when deploying Cilium DaemonSet
     - bool
     - ``false``
   * - :spellingkubeConfigPath
     - Kubernetes config path
     - string
     - ``"~/.kube/config"``
   * - :spellingkubeProxyReplacementHealthzBindAddr
     - healthz server bind address for the kube-proxy replacement. To enable set the value to '0.0.0.0:10256' for all ipv4 addresses and this '[::]:10256' for all ipv6 addresses. By default it is disabled.
     - string
     - ``""``
   * - :spellingl2NeighDiscovery.enabled
     - Enable L2 neighbor discovery in the agent
     - bool
     - ``true``
   * - :spellingl2NeighDiscovery.refreshPeriod
     - Override the agent's default neighbor resolution refresh period.
     - string
     - ``"30s"``
   * - :spellingl2announcements
     - Configure L2 announcements
     - object
     - ``{"enabled":false}``
   * - :spellingl2announcements.enabled
     - Enable L2 announcements
     - bool
     - ``false``
   * - :spellingl2podAnnouncements
     - Configure L2 pod announcements
     - object
     - ``{"enabled":false,"interface":"eth0"}``
   * - :spellingl2podAnnouncements.enabled
     - Enable L2 pod announcements
     - bool
     - ``false``
   * - :spellingl2podAnnouncements.interface
     - Interface used for sending Gratuitous ARP pod announcements
     - string
     - ``"eth0"``
   * - :spellingl7Proxy
     - Enable Layer 7 network policy.
     - bool
     - ``true``
   * - :spellinglivenessProbe.failureThreshold
     - failure threshold of liveness probe
     - int
     - ``10``
   * - :spellinglivenessProbe.periodSeconds
     - interval between checks of the liveness probe
     - int
     - ``30``
   * - :spellingloadBalancer
     - Configure service load balancing
     - object
     - ``{"acceleration":"disabled","l7":{"algorithm":"round_robin","backend":"disabled","ports":[]}}``
   * - :spellingloadBalancer.acceleration
     - acceleration is the option to accelerate service handling via XDP Applicable values can be: disabled (do not use XDP), native (XDP BPF program is run directly out of the networking driver's early receive path), or best-effort (use native mode XDP acceleration on devices that support it).
     - string
     - ``"disabled"``
   * - :spellingloadBalancer.l7
     - L7 LoadBalancer
     - object
     - ``{"algorithm":"round_robin","backend":"disabled","ports":[]}``
   * - :spellingloadBalancer.l7.algorithm
     - Default LB algorithm The default LB algorithm to be used for services, which can be overridden by the service annotation (e.g. service.cilium.io/lb-l7-algorithm) Applicable values: round_robin, least_request, random
     - string
     - ``"round_robin"``
   * - :spellingloadBalancer.l7.backend
     - Enable L7 service load balancing via envoy proxy. The request to a k8s service, which has specific annotation e.g. service.cilium.io/lb-l7, will be forwarded to the local backend proxy to be load balanced to the service endpoints. Please refer to docs for supported annotations for more configuration.  Applicable values:   - envoy: Enable L7 load balancing via envoy proxy. This will automatically set enable-envoy-config as well.   - disabled: Disable L7 load balancing by way of service annotation.
     - string
     - ``"disabled"``
   * - :spellingloadBalancer.l7.ports
     - List of ports from service to be automatically redirected to above backend. Any service exposing one of these ports will be automatically redirected. Fine-grained control can be achieved by using the service annotation.
     - list
     - ``[]``
   * - :spellinglocalRedirectPolicy
     - Enable Local Redirect Policy.
     - bool
     - ``false``
   * - :spellinglogSystemLoad
     - Enables periodic logging of system load
     - bool
     - ``false``
   * - :spellingmaglev
     - Configure maglev consistent hashing
     - object
     - ``{}``
   * - :spellingmonitor
     - cilium-monitor sidecar.
     - object
     - ``{"enabled":false}``
   * - :spellingmonitor.enabled
     - Enable the cilium-monitor sidecar.
     - bool
     - ``false``
   * - :spellingname
     - Agent container name.
     - string
     - ``"cilium"``
   * - :spellingnat.mapStatsEntries
     - Number of the top-k SNAT map connections to track in Cilium statedb.
     - int
     - ``32``
   * - :spellingnat.mapStatsInterval
     - Interval between how often SNAT map is counted for stats.
     - string
     - ``"30s"``
   * - :spellingnat46x64Gateway
     - Configure standalone NAT46/NAT64 gateway
     - object
     - ``{"enabled":false}``
   * - :spellingnat46x64Gateway.enabled
     - Enable RFC8215-prefixed translation
     - bool
     - ``false``
   * - :spellingnodeIPAM.enabled
     - Configure Node IPAM ref: https://docs.cilium.io/en/stable/network/node-ipam/
     - bool
     - ``false``
   * - :spellingnodePort
     - Configure N-S k8s service loadbalancing
     - object
     - ``{"addresses":null,"autoProtectPortRange":true,"bindProtection":true,"enableHealthCheck":true,"enableHealthCheckLoadBalancerIP":false,"enabled":false}``
   * - :spellingnodePort.addresses
     - List of CIDRs for choosing which IP addresses assigned to native devices are used for NodePort load-balancing. By default this is empty and the first suitable, preferably private, IPv4 and IPv6 address assigned to each device is used.  Example:    addresses: ["192.168.1.0/24", "2001::/64"]
     - string
     - ``nil``
   * - :spellingnodePort.autoProtectPortRange
     - Append NodePort range to ip_local_reserved_ports if clash with ephemeral ports is detected.
     - bool
     - ``true``
   * - :spellingnodePort.bindProtection
     - Set to true to prevent applications binding to service ports.
     - bool
     - ``true``
   * - :spellingnodePort.enableHealthCheck
     - Enable healthcheck nodePort server for NodePort services
     - bool
     - ``true``
   * - :spellingnodePort.enableHealthCheckLoadBalancerIP
     - Enable access of the healthcheck nodePort on the LoadBalancerIP. Needs EnableHealthCheck to be enabled
     - bool
     - ``false``
   * - :spellingnodePort.enabled
     - Enable the Cilium NodePort service implementation.
     - bool
     - ``false``
   * - :spellingnodeSelector
     - Node selector for cilium-agent.
     - object
     - ``{"kubernetes.io/os":"linux"}``
   * - :spellingnodeSelectorLabels
     - Enable/Disable use of node label based identity
     - bool
     - ``false``
   * - :spellingnodeinit.affinity
     - Affinity for cilium-nodeinit
     - object
     - ``{}``
   * - :spellingnodeinit.annotations
     - Annotations to be added to all top-level nodeinit objects (resources under templates/cilium-nodeinit)
     - object
     - ``{}``
   * - :spellingnodeinit.bootstrapFile
     - bootstrapFile is the location of the file where the bootstrap timestamp is written by the node-init DaemonSet
     - string
     - ``"/tmp/cilium-bootstrap.d/cilium-bootstrap-time"``
   * - :spellingnodeinit.enabled
     - Enable the node initialization DaemonSet
     - bool
     - ``false``
   * - :spellingnodeinit.extraEnv
     - Additional nodeinit environment variables.
     - list
     - ``[]``
   * - :spellingnodeinit.extraVolumeMounts
     - Additional nodeinit volumeMounts.
     - list
     - ``[]``
   * - :spellingnodeinit.extraVolumes
     - Additional nodeinit volumes.
     - list
     - ``[]``
   * - :spellingnodeinit.image
     - node-init image.
     - object
     - ``{"digest":"sha256:8d7b41c4ca45860254b3c19e20210462ef89479bb6331d6760c4e609d651b29c","override":null,"pullPolicy":"IfNotPresent","repository":"quay.io/cilium/startup-script","tag":"c54c7edeab7fde4da68e59acd319ab24af242c3f","useDigest":true}``
   * - :spellingnodeinit.nodeSelector
     - Node labels for nodeinit pod assignment ref: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector
     - object
     - ``{"kubernetes.io/os":"linux"}``
   * - :spellingnodeinit.podAnnotations
     - Annotations to be added to node-init pods.
     - object
     - ``{}``
   * - :spellingnodeinit.podLabels
     - Labels to be added to node-init pods.
     - object
     - ``{}``
   * - :spellingnodeinit.podSecurityContext
     - Security Context for cilium-node-init pods.
     - object
     - ``{"appArmorProfile":{"type":"Unconfined"}}``
   * - :spellingnodeinit.podSecurityContext.appArmorProfile
     - AppArmorProfile options for the ``cilium-node-init`` and init containers
     - object
     - ``{"type":"Unconfined"}``
   * - :spellingnodeinit.prestop
     - prestop offers way to customize prestop nodeinit script (pre and post position)
     - object
     - ``{"postScript":"","preScript":""}``
   * - :spellingnodeinit.priorityClassName
     - The priority class to use for the nodeinit pod.
     - string
     - ``""``
   * - :spellingnodeinit.resources
     - nodeinit resource limits & requests ref: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
     - object
     - ``{"requests":{"cpu":"100m","memory":"100Mi"}}``
   * - :spellingnodeinit.securityContext
     - Security context to be added to nodeinit pods.
     - object
     - ``{"capabilities":{"add":["SYS_MODULE","NET_ADMIN","SYS_ADMIN","SYS_CHROOT","SYS_PTRACE"]},"privileged":false,"seLinuxOptions":{"level":"s0","type":"spc_t"}}``
   * - :spellingnodeinit.startup
     - startup offers way to customize startup nodeinit script (pre and post position)
     - object
     - ``{"postScript":"","preScript":""}``
   * - :spellingnodeinit.tolerations
     - Node tolerations for nodeinit scheduling to nodes with taints ref: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
     - list
     - ``[{"operator":"Exists"}]``
   * - :spellingnodeinit.updateStrategy
     - node-init update strategy
     - object
     - ``{"type":"RollingUpdate"}``
   * - :spellingoperator.affinity
     - Affinity for cilium-operator
     - object
     - ``{"podAntiAffinity":{"requiredDuringSchedulingIgnoredDuringExecution":[{"labelSelector":{"matchLabels":{"io.cilium/app":"operator"}},"topologyKey":"kubernetes.io/hostname"}]}}``
   * - :spellingoperator.annotations
     - Annotations to be added to all top-level cilium-operator objects (resources under templates/cilium-operator)
     - object
     - ``{}``
   * - :spellingoperator.dashboards
     - Grafana dashboards for cilium-operator grafana can import dashboards based on the label and value ref: https://github.com/grafana/helm-charts/tree/main/charts/grafana#sidecar-for-dashboards
     - object
     - ``{"annotations":{},"enabled":false,"label":"grafana_dashboard","labelValue":"1","namespace":null}``
   * - :spellingoperator.dnsPolicy
     - DNS policy for Cilium operator pods. Ref: https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pod-s-dns-policy
     - string
     - ``""``
   * - :spellingoperator.enabled
     - Enable the cilium-operator component (required).
     - bool
     - ``true``
   * - :spellingoperator.endpointGCInterval
     - Interval for endpoint garbage collection.
     - string
     - ``"5m0s"``
   * - :spellingoperator.extraArgs
     - Additional cilium-operator container arguments.
     - list
     - ``[]``
   * - :spellingoperator.extraEnv
     - Additional cilium-operator environment variables.
     - list
     - ``[]``
   * - :spellingoperator.extraHostPathMounts
     - Additional cilium-operator hostPath mounts.
     - list
     - ``[]``
   * - :spellingoperator.extraVolumeMounts
     - Additional cilium-operator volumeMounts.
     - list
     - ``[]``
   * - :spellingoperator.extraVolumes
     - Additional cilium-operator volumes.
     - list
     - ``[]``
   * - :spellingoperator.hostNetwork
     - HostNetwork setting
     - bool
     - ``true``
   * - :spellingoperator.identityGCInterval
     - Interval for identity garbage collection.
     - string
     - ``"15m0s"``
   * - :spellingoperator.identityHeartbeatTimeout
     - Timeout for identity heartbeats.
     - string
     - ``"30m0s"``
   * - :spellingoperator.image
     - cilium-operator image.
     - object
     - ``{"alibabacloudDigest":"","awsDigest":"","azureDigest":"","genericDigest":"","override":null,"pullPolicy":"IfNotPresent","repository":"quay.io/cilium/operator","suffix":"","tag":"v1.16.7","useDigest":false}``
   * - :spellingoperator.nodeGCInterval
     - Interval for cilium node garbage collection.
     - string
     - ``"5m0s"``
   * - :spellingoperator.nodeSelector
     - Node labels for cilium-operator pod assignment ref: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector
     - object
     - ``{"kubernetes.io/os":"linux"}``
   * - :spellingoperator.podAnnotations
     - Annotations to be added to cilium-operator pods
     - object
     - ``{}``
   * - :spellingoperator.podDisruptionBudget.enabled
     - enable PodDisruptionBudget ref: https://kubernetes.io/docs/concepts/workloads/pods/disruptions/
     - bool
     - ``false``
   * - :spellingoperator.podDisruptionBudget.maxUnavailable
     - Maximum number/percentage of pods that may be made unavailable
     - int
     - ``1``
   * - :spellingoperator.podDisruptionBudget.minAvailable
     - Minimum number/percentage of pods that should remain scheduled. When it's set, maxUnavailable must be disabled by ``maxUnavailable: null``
     - string
     - ``nil``
   * - :spellingoperator.podLabels
     - Labels to be added to cilium-operator pods
     - object
     - ``{}``
   * - :spellingoperator.podSecurityContext
     - Security context to be added to cilium-operator pods
     - object
     - ``{}``
   * - :spellingoperator.pprof.address
     - Configure pprof listen address for cilium-operator
     - string
     - ``"localhost"``
   * - :spellingoperator.pprof.enabled
     - Enable pprof for cilium-operator
     - bool
     - ``false``
   * - :spellingoperator.pprof.port
     - Configure pprof listen port for cilium-operator
     - int
     - ``6061``
   * - :spellingoperator.priorityClassName
     - The priority class to use for cilium-operator
     - string
     - ``""``
   * - :spellingoperator.prometheus
     - Enable prometheus metrics for cilium-operator on the configured port at /metrics
     - object
     - ``{"enabled":true,"port":9963,"serviceMonitor":{"annotations":{},"enabled":false,"interval":"10s","jobLabel":"","labels":{},"metricRelabelings":null,"relabelings":null}}``
   * - :spellingoperator.prometheus.serviceMonitor.annotations
     - Annotations to add to ServiceMonitor cilium-operator
     - object
     - ``{}``
   * - :spellingoperator.prometheus.serviceMonitor.enabled
     - Enable service monitors. This requires the prometheus CRDs to be available (see https://github.com/prometheus-operator/prometheus-operator/blob/main/example/prometheus-operator-crd/monitoring.coreos.com_servicemonitors.yaml)
     - bool
     - ``false``
   * - :spellingoperator.prometheus.serviceMonitor.interval
     - Interval for scrape metrics.
     - string
     - ``"10s"``
   * - :spellingoperator.prometheus.serviceMonitor.jobLabel
     - jobLabel to add for ServiceMonitor cilium-operator
     - string
     - ``""``
   * - :spellingoperator.prometheus.serviceMonitor.labels
     - Labels to add to ServiceMonitor cilium-operator
     - object
     - ``{}``
   * - :spellingoperator.prometheus.serviceMonitor.metricRelabelings
     - Metrics relabeling configs for the ServiceMonitor cilium-operator
     - string
     - ``nil``
   * - :spellingoperator.prometheus.serviceMonitor.relabelings
     - Relabeling configs for the ServiceMonitor cilium-operator
     - string
     - ``nil``
   * - :spellingoperator.removeNodeTaints
     - Remove Cilium node taint from Kubernetes nodes that have a healthy Cilium pod running.
     - bool
     - ``true``
   * - :spellingoperator.replicas
     - Number of replicas to run for the cilium-operator deployment
     - int
     - ``2``
   * - :spellingoperator.resources
     - cilium-operator resource limits & requests ref: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
     - object
     - ``{}``
   * - :spellingoperator.rollOutPods
     - Roll out cilium-operator pods automatically when configmap is updated.
     - bool
     - ``false``
   * - :spellingoperator.securityContext
     - Security context to be added to cilium-operator pods
     - object
     - ``{}``
   * - :spellingoperator.setNodeNetworkStatus
     - Set Node condition NetworkUnavailable to 'false' with the reason 'CiliumIsUp' for nodes that have a healthy Cilium pod.
     - bool
     - ``true``
   * - :spellingoperator.setNodeTaints
     - Taint nodes where Cilium is scheduled but not running. This prevents pods from being scheduled to nodes where Cilium is not the default CNI provider.
     - string
     - same as removeNodeTaints
   * - :spellingoperator.skipCRDCreation
     - Skip CRDs creation for cilium-operator
     - bool
     - ``false``
   * - :spellingoperator.tolerations
     - Node tolerations for cilium-operator scheduling to nodes with taints ref: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
     - list
     - ``[{"operator":"Exists"}]``
   * - :spellingoperator.topologySpreadConstraints
     - Pod topology spread constraints for cilium-operator
     - list
     - ``[]``
   * - :spellingoperator.unmanagedPodWatcher.intervalSeconds
     - Interval, in seconds, to check if there are any pods that are not managed by Cilium.
     - int
     - ``15``
   * - :spellingoperator.unmanagedPodWatcher.restart
     - Restart any pod that are not managed by Cilium.
     - bool
     - ``true``
   * - :spellingoperator.updateStrategy
     - cilium-operator update strategy
     - object
     - ``{"rollingUpdate":{"maxSurge":"25%","maxUnavailable":"50%"},"type":"RollingUpdate"}``
   * - :spellingpmtuDiscovery.enabled
     - Enable path MTU discovery to send ICMP fragmentation-needed replies to the client.
     - bool
     - ``false``
   * - :spellingpodAnnotations
     - Annotations to be added to agent pods
     - object
     - ``{}``
   * - :spellingpodLabels
     - Labels to be added to agent pods
     - object
     - ``{}``
   * - :spellingpodSecurityContext
     - Security Context for cilium-agent pods.
     - object
     - ``{"appArmorProfile":{"type":"Unconfined"}}``
   * - :spellingpodSecurityContext.appArmorProfile
     - AppArmorProfile options for the ``cilium-agent`` and init containers
     - object
     - ``{"type":"Unconfined"}``
   * - :spellingpolicyCIDRMatchMode
     - policyCIDRMatchMode is a list of entities that may be selected by CIDR selector. The possible value is "nodes".
     - string
     - ``nil``
   * - :spellingpolicyEnforcementMode
     - The agent can be put into one of the three policy enforcement modes: default, always and never. ref: https://docs.cilium.io/en/stable/security/policy/intro/#policy-enforcement-modes
     - string
     - ``"default"``
   * - :spellingpprof.address
     - Configure pprof listen address for cilium-agent
     - string
     - ``"localhost"``
   * - :spellingpprof.enabled
     - Enable pprof for cilium-agent
     - bool
     - ``false``
   * - :spellingpprof.port
     - Configure pprof listen port for cilium-agent
     - int
     - ``6060``
   * - :spellingpreflight.affinity
     - Affinity for cilium-preflight
     - object
     - ``{"podAffinity":{"requiredDuringSchedulingIgnoredDuringExecution":[{"labelSelector":{"matchLabels":{"k8s-app":"cilium"}},"topologyKey":"kubernetes.io/hostname"}]}}``
   * - :spellingpreflight.annotations
     - Annotations to be added to all top-level preflight objects (resources under templates/cilium-preflight)
     - object
     - ``{}``
   * - :spellingpreflight.enabled
     - Enable Cilium pre-flight resources (required for upgrade)
     - bool
     - ``false``
   * - :spellingpreflight.extraEnv
     - Additional preflight environment variables.
     - list
     - ``[]``
   * - :spellingpreflight.extraVolumeMounts
     - Additional preflight volumeMounts.
     - list
     - ``[]``
   * - :spellingpreflight.extraVolumes
     - Additional preflight volumes.
     - list
     - ``[]``
   * - :spellingpreflight.image
     - Cilium pre-flight image.
     - object
     - ``{"digest":"","override":null,"pullPolicy":"IfNotPresent","repository":"quay.io/cilium/cilium","tag":"v1.16.7","useDigest":false}``
   * - :spellingpreflight.nodeSelector
     - Node labels for preflight pod assignment ref: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector
     - object
     - ``{"kubernetes.io/os":"linux"}``
   * - :spellingpreflight.podAnnotations
     - Annotations to be added to preflight pods
     - object
     - ``{}``
   * - :spellingpreflight.podDisruptionBudget.enabled
     - enable PodDisruptionBudget ref: https://kubernetes.io/docs/concepts/workloads/pods/disruptions/
     - bool
     - ``false``
   * - :spellingpreflight.podDisruptionBudget.maxUnavailable
     - Maximum number/percentage of pods that may be made unavailable
     - int
     - ``1``
   * - :spellingpreflight.podDisruptionBudget.minAvailable
     - Minimum number/percentage of pods that should remain scheduled. When it's set, maxUnavailable must be disabled by ``maxUnavailable: null``
     - string
     - ``nil``
   * - :spellingpreflight.podLabels
     - Labels to be added to the preflight pod.
     - object
     - ``{}``
   * - :spellingpreflight.podSecurityContext
     - Security context to be added to preflight pods.
     - object
     - ``{}``
   * - :spellingpreflight.priorityClassName
     - The priority class to use for the preflight pod.
     - string
     - ``""``
   * - :spellingpreflight.readinessProbe.initialDelaySeconds
     - For how long kubelet should wait before performing the first probe
     - int
     - ``5``
   * - :spellingpreflight.readinessProbe.periodSeconds
     - interval between checks of the readiness probe
     - int
     - ``5``
   * - :spellingpreflight.resources
     - preflight resource limits & requests ref: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
     - object
     - ``{}``
   * - :spellingpreflight.securityContext
     - Security context to be added to preflight pods
     - object
     - ``{}``
   * - :spellingpreflight.terminationGracePeriodSeconds
     - Configure termination grace period for preflight Deployment and DaemonSet.
     - int
     - ``1``
   * - :spellingpreflight.tofqdnsPreCache
     - Path to write the ``--tofqdns-pre-cache`` file to.
     - string
     - ``""``
   * - :spellingpreflight.tolerations
     - Node tolerations for preflight scheduling to nodes with taints ref: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
     - list
     - ``[{"operator":"Exists"}]``
   * - :spellingpreflight.updateStrategy
     - preflight update strategy
     - object
     - ``{"type":"RollingUpdate"}``
   * - :spellingpreflight.validateCNPs
     - By default we should always validate the installed CNPs before upgrading Cilium. This will make sure the user will have the policies deployed in the cluster with the right schema.
     - bool
     - ``true``
   * - :spellingpriorityClassName
     - The priority class to use for cilium-agent.
     - string
     - ``""``
   * - :spellingprometheus
     - Configure prometheus metrics on the configured port at /metrics
     - object
     - ``{"controllerGroupMetrics":["write-cni-file","sync-host-ips","sync-lb-maps-with-k8s-services"],"enabled":false,"metrics":null,"port":9962,"serviceMonitor":{"annotations":{},"enabled":false,"interval":"10s","jobLabel":"","labels":{},"metricRelabelings":null,"relabelings":[{"replacement":"${1}","sourceLabels":["__meta_kubernetes_pod_node_name"],"targetLabel":"node"}],"trustCRDsExist":false}}``
   * - :spellingprometheus.controllerGroupMetrics
     - - Enable controller group metrics for monitoring specific Cilium subsystems. The list is a list of controller group names. The special values of "all" and "none" are supported. The set of controller group names is not guaranteed to be stable between Cilium versions.
     - list
     - ``["write-cni-file","sync-host-ips","sync-lb-maps-with-k8s-services"]``
   * - :spellingprometheus.metrics
     - Metrics that should be enabled or disabled from the default metric list. The list is expected to be separated by a space. (+metric_foo to enable metric_foo , -metric_bar to disable metric_bar). ref: https://docs.cilium.io/en/stable/observability/metrics/
     - string
     - ``nil``
   * - :spellingprometheus.serviceMonitor.annotations
     - Annotations to add to ServiceMonitor cilium-agent
     - object
     - ``{}``
   * - :spellingprometheus.serviceMonitor.enabled
     - Enable service monitors. This requires the prometheus CRDs to be available (see https://github.com/prometheus-operator/prometheus-operator/blob/main/example/prometheus-operator-crd/monitoring.coreos.com_servicemonitors.yaml)
     - bool
     - ``false``
   * - :spellingprometheus.serviceMonitor.interval
     - Interval for scrape metrics.
     - string
     - ``"10s"``
   * - :spellingprometheus.serviceMonitor.jobLabel
     - jobLabel to add for ServiceMonitor cilium-agent
     - string
     - ``""``
   * - :spellingprometheus.serviceMonitor.labels
     - Labels to add to ServiceMonitor cilium-agent
     - object
     - ``{}``
   * - :spellingprometheus.serviceMonitor.metricRelabelings
     - Metrics relabeling configs for the ServiceMonitor cilium-agent
     - string
     - ``nil``
   * - :spellingprometheus.serviceMonitor.relabelings
     - Relabeling configs for the ServiceMonitor cilium-agent
     - list
     - ``[{"replacement":"${1}","sourceLabels":["__meta_kubernetes_pod_node_name"],"targetLabel":"node"}]``
   * - :spellingprometheus.serviceMonitor.trustCRDsExist
     - Set to ``true`` and helm will not check for monitoring.coreos.com/v1 CRDs before deploying
     - bool
     - ``false``
   * - :spellingrbac.create
     - Enable creation of Resource-Based Access Control configuration.
     - bool
     - ``true``
   * - :spellingreadinessProbe.failureThreshold
     - failure threshold of readiness probe
     - int
     - ``3``
   * - :spellingreadinessProbe.periodSeconds
     - interval between checks of the readiness probe
     - int
     - ``30``
   * - :spellingresourceQuotas
     - Enable resource quotas for priority classes used in the cluster.
     - object
     - ``{"cilium":{"hard":{"pods":"10k"}},"enabled":false,"operator":{"hard":{"pods":"15"}}}``
   * - :spellingresources
     - Agent resource limits & requests ref: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
     - object
     - ``{}``
   * - :spellingrollOutCiliumPods
     - Roll out cilium agent pods automatically when configmap is updated.
     - bool
     - ``false``
   * - :spellingroutingMode
     - Enable native-routing mode or tunneling mode. Possible values:   - ""   - native   - tunnel
     - string
     - ``"tunnel"``
   * - :spellingsctp
     - SCTP Configuration Values
     - object
     - ``{"enabled":false}``
   * - :spellingsctp.enabled
     - Enable SCTP support. NOTE: Currently, SCTP support does not support rewriting ports or multihoming.
     - bool
     - ``false``
   * - :spellingsecurityContext.capabilities.applySysctlOverwrites
     - capabilities for the ``apply-sysctl-overwrites`` init container
     - list
     - ``["SYS_ADMIN","SYS_CHROOT","SYS_PTRACE"]``
   * - :spellingsecurityContext.capabilities.ciliumAgent
     - Capabilities for the ``cilium-agent`` container
     - list
     - ``["CHOWN","KILL","NET_ADMIN","NET_RAW","IPC_LOCK","SYS_MODULE","SYS_ADMIN","SYS_RESOURCE","DAC_OVERRIDE","FOWNER","SETGID","SETUID"]``
   * - :spellingsecurityContext.capabilities.cleanCiliumState
     - Capabilities for the ``clean-cilium-state`` init container
     - list
     - ``["NET_ADMIN","SYS_MODULE","SYS_ADMIN","SYS_RESOURCE"]``
   * - :spellingsecurityContext.capabilities.mountCgroup
     - Capabilities for the ``mount-cgroup`` init container
     - list
     - ``["SYS_ADMIN","SYS_CHROOT","SYS_PTRACE"]``
   * - :spellingsecurityContext.privileged
     - Run the pod with elevated privileges
     - bool
     - ``false``
   * - :spellingsecurityContext.seLinuxOptions
     - SELinux options for the ``cilium-agent`` and init containers
     - object
     - ``{"level":"s0","type":"spc_t"}``
   * - :spellingserviceAccounts
     - Define serviceAccount names for components.
     - object
     - Component's fully qualified name.
   * - :spellingserviceAccounts.clustermeshcertgen
     - Clustermeshcertgen is used if clustermesh.apiserver.tls.auto.method=cronJob
     - object
     - ``{"annotations":{},"automount":true,"create":true,"name":"clustermesh-apiserver-generate-certs"}``
   * - :spellingserviceAccounts.hubblecertgen
     - Hubblecertgen is used if hubble.tls.auto.method=cronJob
     - object
     - ``{"annotations":{},"automount":true,"create":true,"name":"hubble-generate-certs"}``
   * - :spellingserviceAccounts.nodeinit.enabled
     - Enabled is temporary until https://github.com/cilium/cilium-cli/issues/1396 is implemented. Cilium CLI doesn't create the SAs for node-init, thus the workaround. Helm is not affected by this issue. Name and automount can be configured, if enabled is set to true. Otherwise, they are ignored. Enabled can be removed once the issue is fixed. Cilium-nodeinit DS must also be fixed.
     - bool
     - ``false``
   * - :spellingserviceNoBackendResponse
     - Configure what the response should be to traffic for a service without backends. Possible values:  - reject (default)  - drop
     - string
     - ``"reject"``
   * - :spellingsleepAfterInit
     - Do not run Cilium agent when running with clean mode. Useful to completely uninstall Cilium as it will stop Cilium from starting and create artifacts in the node.
     - bool
     - ``false``
   * - :spellingsocketLB
     - Configure socket LB
     - object
     - ``{"enabled":false}``
   * - :spellingsocketLB.enabled
     - Enable socket LB
     - bool
     - ``false``
   * - :spellingstartupProbe.failureThreshold
     - failure threshold of startup probe. 105 x 2s translates to the old behaviour of the readiness probe (120s delay + 30 x 3s)
     - int
     - ``105``
   * - :spellingstartupProbe.periodSeconds
     - interval between checks of the startup probe
     - int
     - ``2``
   * - :spellingsvcSourceRangeCheck
     - Enable check of service source ranges (currently, only for LoadBalancer).
     - bool
     - ``true``
   * - :spellingsynchronizeK8sNodes
     - Synchronize Kubernetes nodes to kvstore and perform CNP GC.
     - bool
     - ``true``
   * - :spellingsysctlfix
     - Configure sysctl override described in #20072.
     - object
     - ``{"enabled":true}``
   * - :spellingsysctlfix.enabled
     - Enable the sysctl override. When enabled, the init container will mount the /proc of the host so that the ``sysctlfix`` utility can execute.
     - bool
     - ``true``
   * - :spellingterminationGracePeriodSeconds
     - Configure termination grace period for cilium-agent DaemonSet.
     - int
     - ``1``
   * - :spellingtls
     - Configure TLS configuration in the agent.
     - object
     - ``{"ca":{"cert":"","certValidityDuration":1095,"key":""},"caBundle":{"enabled":false,"key":"ca.crt","name":"cilium-root-ca.crt","useSecret":false},"secretsBackend":"local"}``
   * - :spellingtls.ca
     - Base64 encoded PEM values for the CA certificate and private key. This can be used as common CA to generate certificates used by hubble and clustermesh components. It is neither required nor used when cert-manager is used to generate the certificates.
     - object
     - ``{"cert":"","certValidityDuration":1095,"key":""}``
   * - :spellingtls.ca.cert
     - Optional CA cert. If it is provided, it will be used by cilium to generate all other certificates. Otherwise, an ephemeral CA is generated.
     - string
     - ``""``
   * - :spellingtls.ca.certValidityDuration
     - Generated certificates validity duration in days. This will be used for auto generated CA.
     - int
     - ``1095``
   * - :spellingtls.ca.key
     - Optional CA private key. If it is provided, it will be used by cilium to generate all other certificates. Otherwise, an ephemeral CA is generated.
     - string
     - ``""``
   * - :spellingtls.caBundle
     - Configure the CA trust bundle used for the validation of the certificates leveraged by hubble and clustermesh. When enabled, it overrides the content of the 'ca.crt' field of the respective certificates, allowing for CA rotation with no down-time.
     - object
     - ``{"enabled":false,"key":"ca.crt","name":"cilium-root-ca.crt","useSecret":false}``
   * - :spellingtls.caBundle.enabled
     - Enable the use of the CA trust bundle.
     - bool
     - ``false``
   * - :spellingtls.caBundle.key
     - Entry of the ConfigMap containing the CA trust bundle.
     - string
     - ``"ca.crt"``
   * - :spellingtls.caBundle.name
     - Name of the ConfigMap containing the CA trust bundle.
     - string
     - ``"cilium-root-ca.crt"``
   * - :spellingtls.caBundle.useSecret
     - Use a Secret instead of a ConfigMap.
     - bool
     - ``false``
   * - :spellingtls.secretsBackend
     - This configures how the Cilium agent loads the secrets used TLS-aware CiliumNetworkPolicies (namely the secrets referenced by terminatingTLS and originatingTLS). Possible values:   - local   - k8s
     - string
     - ``"local"``
   * - :spellingtolerations
     - Node tolerations for agent scheduling to nodes with taints ref: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
     - list
     - ``[{"operator":"Exists"}]``
   * - :spellingtunnelPort
     - Configure VXLAN and Geneve tunnel port.
     - int
     - Port 8472 for VXLAN, Port 6081 for Geneve
   * - :spellingtunnelProtocol
     - Tunneling protocol to use in tunneling mode and for ad-hoc tunnels. Possible values:   - ""   - vxlan   - geneve
     - string
     - ``"vxlan"``
   * - :spellingupdateStrategy
     - Cilium agent update strategy
     - object
     - ``{"rollingUpdate":{"maxUnavailable":2},"type":"RollingUpdate"}``
   * - :spellingupgradeCompatibility
     - upgradeCompatibility helps users upgrading to ensure that the configMap for Cilium will not change critical values to ensure continued operation This flag is not required for new installations. For example: '1.7', '1.8', '1.9'
     - string
     - ``nil``
   * - :spellingvtep.cidr
     - A space separated list of VTEP device CIDRs, for example "1.1.1.0/24 1.1.2.0/24"
     - string
     - ``""``
   * - :spellingvtep.enabled
     - Enables VXLAN Tunnel Endpoint (VTEP) Integration (beta) to allow Cilium-managed pods to talk to third party VTEP devices over Cilium tunnel.
     - bool
     - ``false``
   * - :spellingvtep.endpoint
     - A space separated list of VTEP device endpoint IPs, for example "1.1.1.1  1.1.2.1"
     - string
     - ``""``
   * - :spellingvtep.mac
     - A space separated list of VTEP device MAC addresses (VTEP MAC), for example "x:x:x:x:x:x  y:y:y:y:y:y:y"
     - string
     - ``""``
   * - :spellingvtep.mask
     - VTEP CIDRs Mask that applies to all VTEP CIDRs, for example "255.255.255.0"
     - string
     - ``""``
   * - :spellingwaitForKubeProxy
     - Wait for KUBE-PROXY-CANARY iptables rule to appear in "wait-for-kube-proxy" init container before launching cilium-agent. More context can be found in the commit message of below PR https://github.com/cilium/cilium/pull/20123
     - bool
     - ``false``
   * - :spellingwellKnownIdentities.enabled
     - Enable the use of well-known identities.
     - bool
     - ``false``
