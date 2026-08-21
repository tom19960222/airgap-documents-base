---
collection: k8s
version: "1.31.6"
title: "WebhookAdmission Configuration (v1)"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/config-api/apiserver-webhookadmission.v1.md
fetched_at: 2026-01-16T10:18:07+05:30
---
<p>Package v1 is the v1 version of the API.</p>

## Resource Types 

- [WebhookAdmission](#apiserver-config-k8s-io-v1-WebhookAdmission)
  

## `WebhookAdmission`     {#apiserver-config-k8s-io-v1-WebhookAdmission}
    

<p>WebhookAdmission provides configuration for the webhook admission controller.</p>

<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>apiserver.config.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>WebhookAdmission</code></td></tr>
    
  
<tr><td><code>kubeConfigFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>KubeConfigFile is the path to the kubeconfig file.</p>
</td>
</tr>
</tbody>
</table>
