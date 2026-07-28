---
collection: ansible
version: "6"
title: "community.okd.openshift_route module – Expose a Service as an OpenShift Route."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/okd/openshift_route_module.html
fetched_at: 2026-07-27T17:20:14+00:00
---
# community.okd.openshift_route module – Expose a Service as an OpenShift Route.

> **Note:**
>
> This module is part of the [community.okd collection](https://galaxy.ansible.com/community/okd) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.okd`.
> You need further requirements to be able to use this module,
> see [Requirements](openshift_route_module.md#ansible-collections-community-okd-openshift-route-module-requirements) for details.
>
> To use it in a playbook, specify: `community.okd.openshift_route`.

New in community.okd 0.3.0

- [Synopsis](openshift_route_module.md#synopsis)
- [Requirements](openshift_route_module.md#requirements)
- [Parameters](openshift_route_module.md#parameters)
- [Notes](openshift_route_module.md#notes)
- [Examples](openshift_route_module.md#examples)
- [Return Values](openshift_route_module.md#return-values)

## [Synopsis](openshift_route_module.md#id1)

- Looks up a Service and creates a new Route based on it.
- Analogous to `oc expose` and `oc create route` for creating Routes, but does not support creating Services.
- For creating Services from other resources, see kubernetes.core.k8s.

## [Requirements](openshift_route_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- kubernetes >= 12.0.0
- PyYAML >= 3.11

## [Parameters](openshift_route_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **annotations**  dictionary  added in community.okd 2.1.0 | Specify the Route Annotations.  A set of key: value pairs. |
| **api_key**  string | Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable. |
| **ca_cert**  aliases: ssl_ca_cert  path | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable. |
| **client_cert**  aliases: cert_file  path | Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable. |
| **client_key**  aliases: key_file  path | Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment variable. |
| **context**  string | The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable. |
| **force**  boolean | If set to `yes`, and *state* is `present`, an existing object will be replaced.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable. |
| **hostname**  string | The hostname for the Route. |
| **impersonate_groups**  list / elements=string  added in kubernetes.core 2.3.0 | Group(s) to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_GROUPS environment. Example: Group1,Group2 |
| **impersonate_user**  string  added in kubernetes.core 2.3.0 | Username to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_USER environment. |
| **kubeconfig**  any | Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the Kubernetes client will attempt to load the default configuration file from *~/.kube/config*. Can also be specified via K8S_AUTH_KUBECONFIG environment variable.  The kubernetes configuration can be provided as dictionary. This feature requires a python kubernetes client version >= 17.17.0. Added in version 2.2.0. |
| **labels**  dictionary | Specify the labels to apply to the created Route.  A set of key: value pairs. |
| **name**  string | The desired name of the Route to be created.  Defaults to the value of *service* |
| **namespace**  string / required | The namespace of the resource being targeted.  The Route will be created in this namespace as well. |
| **no_proxy**  string  added in kubernetes.core 2.3.0 | The comma separated list of hosts/domains/IP/CIDR that shouldn’t go through proxy. Can also be specified via K8S_AUTH_NO_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. NO_PROXY).  This feature requires kubernetes>=19.15.0. When kubernetes library is less than 19.15.0, it fails even no_proxy set in correct.  example value is “localhost,.local,.example.com,127.0.0.1,127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16” |
| **password**  string | Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.  Please read the description of the `username` option for a discussion of when this option is applicable. |
| **path**  string | The path for the Route |
| **persist_config**  boolean | Whether or not to save the kube config refresh tokens. Can also be specified via K8S_AUTH_PERSIST_CONFIG environment variable.  When the k8s context is using a user credentials with refresh tokens (like oidc or gke/gcloud auth), the token is refreshed by the k8s python client library but not saved by default. So the old refresh token can expire and the next auth might fail. Setting this flag to true will tell the k8s python client to save the new refresh token to the kube config file.  Default to false.  Please note that the current version of the k8s python client library does not support setting this flag to True yet.  The fix for this k8s python library is here: <https://github.com/kubernetes-client/python-base/pull/169>  Choices:   - `false` - `true` |
| **port**  string | Name or number of the port the Route will route traffic to. |
| **proxy**  string | The URL of an HTTP proxy to use for the connection. Can also be specified via K8S_AUTH_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. HTTP_PROXY). |
| **proxy_headers**  dictionary  added in kubernetes.core 2.0.0 | The Header used for the HTTP proxy.  Documentation can be found here <https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html?highlight%3Dproxy_headers#urllib3.util.make_headers>. |
| **basic_auth**  string | Colon-separated username:password for basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_BASIC_AUTH environment. |
| **proxy_basic_auth**  string | Colon-separated username:password for proxy basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_PROXY_BASIC_AUTH environment. |
| **user_agent**  string | String representing the user-agent you want, such as foo/1.0.  Can also be specified via K8S_AUTH_PROXY_HEADERS_USER_AGENT environment. |
| **service**  aliases: svc  string | The name of the service to expose.  Required when *state* is not absent. |
| **state**  string | Determines if an object should be created, patched, or deleted. When set to `present`, an object will be created, if it does not already exist. If set to `absent`, an existing object will be deleted. If set to `present`, an existing object will be patched, if its attributes differ from those specified using *resource_definition* or *src*.  Choices:   - `"absent"` - `"present"` ← (default) |
| **termination**  string | The termination type of the Route.  If left empty no termination type will be set, and the route will be insecure.  When set to insecure *tls* will be ignored.  Choices:   - `"edge"` - `"passthrough"` - `"reencrypt"` - `"insecure"` ← (default) |
| **tls**  dictionary | TLS configuration for the newly created route.  Only used when *termination* is set. |
| **ca_certificate**  string | Path to a CA certificate file on the target host.  Not supported when *termination* is set to passthrough. |
| **certificate**  string | Path to a certificate file on the target host.  Not supported when *termination* is set to passthrough. |
| **destination_ca_certificate**  string | Path to a CA certificate file used for securing the connection.  Only used when *termination* is set to reencrypt.  Defaults to the Service CA. |
| **insecure_policy**  string | Sets the InsecureEdgeTerminationPolicy for the Route.  Not supported when *termination* is set to reencrypt.  When *termination* is set to passthrough, only redirect is supported.  If not provided, insecure traffic will be disallowed.  Choices:   - `"allow"` - `"redirect"` - `"disallow"` ← (default) |
| **key**  string | Path to a key file on the target host.  Not supported when *termination* is set to passthrough. |
| **username**  string | Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.  Please note that this only works with clusters configured to use HTTP Basic Auth. If your cluster has a different form of authentication (e.g. OAuth2 in OpenShift), this option will not work as expected and you should look into the [community.okd.k8s_auth](k8s_auth_module.md#ansible-collections-community-okd-k8s-auth-module) module, as that might do what you need. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  Choices:   - `false` - `true` |
| **wait**  boolean | Whether to wait for certain resource kinds to end up in the desired state.  By default the module exits once Kubernetes has received the request.  Implemented for `state=present` for `Deployment`, `DaemonSet` and `Pod`, and for `state=absent` for all resource kinds.  For resource kinds without an implementation, `wait` returns immediately unless `wait_condition` is set.  Choices:   - `false` ← (default) - `true` |
| **wait_condition**  dictionary | Specifies a custom condition on the status to wait for.  Ignored if `wait` is not set or is set to False. |
| **reason**  string | The value of the reason field in your desired condition  For example, if a `Deployment` is paused, The `Progressing` `type` will have the `DeploymentPaused` reason.  The possible reasons in a condition are specific to each resource type in Kubernetes.  See the API documentation of the status field for a given resource to see possible choices. |
| **status**  string | The value of the status field in your desired condition.  For example, if a `Deployment` is paused, the `Progressing` `type` will have the `Unknown` status.  Choices:   - `"True"` ← (default) - `"False"` - `"Unknown"` |
| **type**  string | The type of condition to wait for.  For example, the `Pod` resource will set the `Ready` condition (among others).  Required if you are specifying a `wait_condition`.  If left empty, the `wait_condition` field will be ignored.  The possible types for a condition are specific to each resource type in Kubernetes.  See the API documentation of the status field for a given resource to see possible choices. |
| **wait_sleep**  integer | Number of seconds to sleep between checks.  Default: `5` |
| **wait_timeout**  integer | How long in seconds to wait for the resource to end up in the desired state.  Ignored if `wait` is not set.  Default: `120` |
| **wildcard_policy**  string | The wildcard policy for the hostname.  Currently only Subdomain is supported.  If not provided, the default of None will be used.  Choices:   - `"Subdomain"` |

## [Notes](openshift_route_module.md#id4)

> **Note:**
>
> - To avoid SSL certificate validation errors when `validate_certs` is *True*, the full certificate chain for the API server must be provided via `ca_cert` or in the kubeconfig file.

## [Examples](openshift_route_module.md#id5)

```yaml+jinja
- name: Create hello-world deployment
  community.okd.k8s:
    definition:
      apiVersion: apps/v1
      kind: Deployment
      metadata:
        name: hello-kubernetes
        namespace: default
      spec:
        replicas: 3
        selector:
          matchLabels:
            app: hello-kubernetes
        template:
          metadata:
            labels:
              app: hello-kubernetes
          spec:
            containers:
            - name: hello-kubernetes
              image: paulbouwer/hello-kubernetes:1.8
              ports:
              - containerPort: 8080

- name: Create Service for the hello-world deployment
  community.okd.k8s:
    definition:
      apiVersion: v1
      kind: Service
      metadata:
        name: hello-kubernetes
        namespace: default
      spec:
        ports:
        - port: 80
          targetPort: 8080
        selector:
          app: hello-kubernetes

- name: Expose the insecure hello-world service externally
  community.okd.openshift_route:
    service: hello-kubernetes
    namespace: default
    insecure_policy: allow
    annotations:
      haproxy.router.openshift.io/balance: roundrobin
  register: route
```

## [Return Values](openshift_route_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **duration**  integer | elapsed time of task in seconds  Returned: when `wait` is true  Sample: `48` |
| **result**  complex | The Route object that was created or updated. Will be empty in the case of deletion.  Returned: success |
| **apiVersion**  string | The versioned schema of this representation of an object.  Returned: success |
| **kind**  string | Represents the REST resource this object represents.  Returned: success |
| **metadata**  complex | Standard object metadata. Includes name, namespace, annotations, labels, etc.  Returned: success |
| **name**  string | The name of the created Route  Returned: success |
| **namespace**  string | The namespace of the create Route  Returned: success |
| **spec**  complex | Specification for the Route  Returned: success |
| **host**  string | Host is an alias/DNS that points to the service.  Returned: success |
| **path**  string | Path that the router watches for, to route traffic for to the service.  Returned: success |
| **port**  complex | Defines a port mapping from a router to an endpoint in the service endpoints.  Returned: success |
| **targetPort**  string | The target port on pods selected by the service this route points to.  Returned: success |
| **tls**  complex | Defines config used to secure a route and provide termination.  Returned: success |
| **caCertificate**  string | Provides the cert authority certificate contents.  Returned: success |
| **certificate**  string | Provides certificate contents.  Returned: success |
| **destinationCACertificate**  string | Provides the contents of the ca certificate of the final destination.  Returned: success |
| **insecureEdgeTerminationPolicy**  string | Indicates the desired behavior for insecure connections to a route.  Returned: success |
| **key**  string | Provides key file contents.  Returned: success |
| **termination**  string | Indicates termination type.  Returned: success |
| **to**  complex | Specifies the target that resolve into endpoints.  Returned: success |
| **kind**  string | The kind of target that the route is referring to. Currently, only ‘Service’ is allowed.  Returned: success |
| **name**  string | Name of the service/target that is being referred to. e.g. name of the service.  Returned: success |
| **weight**  integer | Specifies the target’s relative weight against other target reference objects.  Returned: success |
| **wildcardPolicy**  string | Wildcard policy if any for the route.  Returned: success |
| **status**  complex | Current status details for the Route  Returned: success |
| **ingress**  complex | List of places where the route may be exposed.  Returned: success |
| **conditions**  complex | Array of status conditions for the Route ingress.  Returned: success |
| **status**  string | The status of the condition. Can be True, False, Unknown.  Returned: success |
| **type**  string | The type of the condition. Currently only ‘Ready’.  Returned: success |
| **host**  string | The host string under which the route is exposed.  Returned: success |
| **routerCanonicalHostname**  string | The external host name for the router that can be used as a CNAME for the host requested for this route. May not be set.  Returned: success |
| **routerName**  string | A name chosen by the router to identify itself.  Returned: success |
| **wildcardPolicy**  string | The wildcard policy that was allowed where this route is exposed.  Returned: success |

### Authors

- Fabian von Feilitzsch (@fabianvf)

### Collection links

[Issue Tracker](https://github.com/openshift/community.okd/issues)
[Repository (Sources)](https://github.com/openshift/community.okd)
