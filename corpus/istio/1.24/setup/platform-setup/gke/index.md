---
collection: istio
version: "1.24"
title: "Google Kubernetes Engine"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/platform-setup/gke/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Instructions to set up a Google Kubernetes Engine cluster for Istio."
---
Follow these instructions to prepare a GKE cluster for Istio.

1. Create a new cluster.

```bash
$ export PROJECT_ID=`gcloud config get-value project` && \
  export M_TYPE=n1-standard-2 && \
  export ZONE=us-west2-a && \
  export CLUSTER_NAME=${PROJECT_ID}-${RANDOM} && \
  gcloud services enable container.googleapis.com && \
  gcloud container clusters create $CLUSTER_NAME \
  --cluster-version latest \
  --machine-type=$M_TYPE \
  --num-nodes 4 \
  --zone $ZONE \
  --project $PROJECT_ID
```

> **Tip:**
>
> The default installation of Istio requires nodes with >1 vCPU. If you are
>     installing with the
>     [demo configuration profile](../../additional-setup/config-profiles/index.md),
>     you can remove the `--machine-type` argument to use the smaller `n1-standard-1` machine size instead.

> **Warning:**
>
> To use the Istio CNI feature on GKE, please check the [CNI installation guide](../../additional-setup/cni/index.md#prerequisites)
>     for prerequisite cluster configuration steps.

> **Warning:**
>
> **For private GKE clusters**
>
>     An automatically created firewall rule does not open port 15017. This is needed by the istiod discovery validation webhook.
>
>     To review this firewall rule for master access:
>
>
>
> ```bash
> $ gcloud compute firewall-rules list --filter="name~gke-${CLUSTER_NAME}-[0-9a-z]*-master"
> ```
>
>
>
>     To replace the existing rule and allow master access:
>
>
>
> ```bash
> $ gcloud compute firewall-rules update <firewall-rule-name> --allow tcp:10250,tcp:443,tcp:15017
> ```

1. Retrieve your credentials for `kubectl`.

```bash
$ gcloud container clusters get-credentials $CLUSTER_NAME \
    --zone $ZONE \
    --project $PROJECT_ID
```

1. Grant cluster administrator (admin) permissions to the current user. To
   create the necessary RBAC rules for Istio, the current user requires admin
   permissions.

```bash
$ kubectl create clusterrolebinding cluster-admin-binding \
    --clusterrole=cluster-admin \
    --user=$(gcloud config get-value core/account)
```

## Multi-cluster communication

In some cases, a firewall rule must be explicitly created to allow cross-cluster traffic.

> **Warning:**
>
> The following instructions will allow communication between *all* clusters in your project. Adjust the commands as needed.

1. Gather information about your clusters' network.

```bash
$ function join_by { local IFS="$1"; shift; echo "$*"; }
$ ALL_CLUSTER_CIDRS=$(gcloud --project $PROJECT_ID container clusters list --format='value(clusterIpv4Cidr)' | sort | uniq)
$ ALL_CLUSTER_CIDRS=$(join_by , $(echo "${ALL_CLUSTER_CIDRS}"))
$ ALL_CLUSTER_NETTAGS=$(gcloud --project $PROJECT_ID compute instances list --format='value(tags.items.[0])' | sort | uniq)
$ ALL_CLUSTER_NETTAGS=$(join_by , $(echo "${ALL_CLUSTER_NETTAGS}"))
```

1. Create the firewall rule.

```bash
$ gcloud compute firewall-rules create istio-multicluster-pods \
    --allow=tcp,udp,icmp,esp,ah,sctp \
    --direction=INGRESS \
    --priority=900 \
    --source-ranges="${ALL_CLUSTER_CIDRS}" \
    --target-tags="${ALL_CLUSTER_NETTAGS}" --quiet
```
