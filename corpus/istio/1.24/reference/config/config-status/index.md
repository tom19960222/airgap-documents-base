---
collection: istio
version: "1.24"
title: "Configuration Status Field"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/config-status/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Describes the role of the `status` field in configuration workflow."
---
> **Warning:**
>
> This feature is in the Alpha stage, see
> [Istio Feature Status](../../../releases/feature-stages/index.md). Your feedback is welcome in the
> [Istio User Experience discussion](https://discuss.istio.io/c/UX/23). Currently,
> this feature is tested only for single, low volume clusters with a single
> control plane revision.

Istio 1.6 and later provides information about the propagation of configuration
changes through the mesh, using the `status` field of the resource.
Status is disabled by default, and can be enabled during install with
(you must also enable `config_distribution_tracking`):

```bash
$ istioctl install --set values.pilot.env.PILOT_ENABLE_STATUS=true --set values.global.istiod.enableAnalysis=true
```

The `status` field contains the state of a resource's configuration with various
informational messages, including:

* The resource's readiness.
* How many data plane instances are associated with it.
* Information for the output of tools, such as `istioctl analyze`.

## View the `status` field

You can view the contents of the `status` field of a resource using
`kubectl get`. For example, to view the status of a virtual service, use the following
command:

```bash
$ kubectl get virtualservice <service-name> -o yaml
```

In the output, the `status` field contains several nested fields with details
about the process of propagating configuration changes through the mesh.

```yaml
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2019-12-26T22:06:56Z"
    message: "1 Error and 1 Warning found. See validationMessages field for details"
    reason: "errorsFound"
    status: "False"
    type: PassedAnalysis
  validationMessages:
  - code: IST0101
    level: Error
    message: 'Referenced gateway not found: "bogus-gateway"'
  - code: IST0102
    level: Warn
    message: 'mTLS not enabled for virtual service'
```

## The `conditions` field

Conditions represent possible states of the resource. The `type` field of a
condition can have the following values:

* `PassedAnalysis`

When you apply a configuration, a condition of each of these types is added to the
`conditions` field.

The `status` field of the `PassedAnalysis` type condition will have a value of
`True` or `False` depending on whether or not Istio's background analyzers have
detected a problem with your config. If `False`, the problem(s) will be detailed in the
`validationMessages` field.

The `PassedAnalysis` condition is an informational field only. It does not
block the application of an invalid configuration. It is possible for the status to
indicate that validation failed, but applying the configuration was successful.
This means Istio was able to set the new configuration, but the configuration was
invalid, likely due to a syntax error or similar problem.

## The `validationMessages` field

In case of a validation failure, check the `validationMessages` field for
more information. The `validationMessages` field has details about the validation
process, such as error messages indicating that Istio cannot apply the
configuration, and warning or informational messages that did not result in an
error.

If the condition of type `PassedValidation` has a status of `False`, there will
be `validationMessages` explaining the problem. There might be messages present
when `PassedValidation` status is `True`, because those are informational
messages.

For validation message examples, see
[Configuration Analysis Messages](../analysis/_index.md).
