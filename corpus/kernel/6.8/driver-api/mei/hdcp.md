---
collection: kernel
version: "6.8"
title: "HDCP:"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/mei/hdcp.html
fetched_at: 2026-08-21T03:40:01+00:00
---
# HDCP:

ME FW as a security engine provides the capability for setting up
HDCP2.2 protocol negotiation between the Intel graphics device and
an HDC2.2 sink.

ME FW prepares HDCP2.2 negotiation parameters, signs and encrypts them
according the HDCP 2.2 spec. The Intel graphics sends the created blob
to the HDCP2.2 sink.

Similarly, the HDCP2.2 sink's response is transferred to ME FW
for decryption and verification.

Once all the steps of HDCP2.2 negotiation are completed,
upon request ME FW will configure the port as authenticated and supply
the HDCP encryption keys to Intel graphics hardware.

## mei_hdcp driver

The mei_hdcp driver acts as a translation layer between HDCP 2.2
protocol implementer (I915) and ME FW by translating HDCP2.2
negotiation messages to ME FW command payloads and vice versa.

## mei_hdcp api

int mei_hdcp_initiate_session(struct [device](../infrastructure.md#c.device "device") \*dev, struct hdcp_port_data \*data, struct hdcp2_ake_init \*ake_data)
:   Initiate a Wired HDCP2.2 Tx Session in ME FW

**Parameters**

`struct device *dev`
:   device corresponding to the mei_cl_device

`struct hdcp_port_data *data`
:   Intel HW specific hdcp data

`struct hdcp2_ake_init *ake_data`
:   AKE_Init msg output.

**Return**

0 on Success, <0 on Failure.

int mei_hdcp_verify_receiver_cert_prepare_km(struct [device](../infrastructure.md#c.device "device") \*dev, struct hdcp_port_data \*data, struct hdcp2_ake_send_cert \*rx_cert, bool \*km_stored, struct hdcp2_ake_no_stored_km \*ek_pub_km, size_t \*msg_sz)
:   Verify the Receiver Certificate AKE_Send_Cert and prepare AKE_Stored_Km/AKE_No_Stored_Km

**Parameters**

`struct device *dev`
:   device corresponding to the mei_cl_device

`struct hdcp_port_data *data`
:   Intel HW specific hdcp data

`struct hdcp2_ake_send_cert *rx_cert`
:   AKE_Send_Cert for verification

`bool *km_stored`
:   Pairing status flag output

`struct hdcp2_ake_no_stored_km *ek_pub_km`
:   AKE_Stored_Km/AKE_No_Stored_Km output msg

`size_t *msg_sz`
:   size of AKE_XXXXX_Km output msg

**Return**

0 on Success, <0 on Failure

int mei_hdcp_verify_hprime(struct [device](../infrastructure.md#c.device "device") \*dev, struct hdcp_port_data \*data, struct hdcp2_ake_send_hprime \*rx_hprime)
:   Verify AKE_Send_H_prime at ME FW.

**Parameters**

`struct device *dev`
:   device corresponding to the mei_cl_device

`struct hdcp_port_data *data`
:   Intel HW specific hdcp data

`struct hdcp2_ake_send_hprime *rx_hprime`
:   AKE_Send_H_prime msg for ME FW verification

**Return**

0 on Success, <0 on Failure

int mei_hdcp_store_pairing_info(struct [device](../infrastructure.md#c.device "device") \*dev, struct hdcp_port_data \*data, struct hdcp2_ake_send_pairing_info \*pairing_info)
:   Store pairing info received at ME FW

**Parameters**

`struct device *dev`
:   device corresponding to the mei_cl_device

`struct hdcp_port_data *data`
:   Intel HW specific hdcp data

`struct hdcp2_ake_send_pairing_info *pairing_info`
:   AKE_Send_Pairing_Info msg input to ME FW

**Return**

0 on Success, <0 on Failure

int mei_hdcp_initiate_locality_check(struct [device](../infrastructure.md#c.device "device") \*dev, struct hdcp_port_data \*data, struct hdcp2_lc_init \*lc_init_data)
:   Prepare LC_Init

**Parameters**

`struct device *dev`
:   device corresponding to the mei_cl_device

`struct hdcp_port_data *data`
:   Intel HW specific hdcp data

`struct hdcp2_lc_init *lc_init_data`
:   LC_Init msg output

**Return**

0 on Success, <0 on Failure

int mei_hdcp_verify_lprime(struct [device](../infrastructure.md#c.device "device") \*dev, struct hdcp_port_data \*data, struct hdcp2_lc_send_lprime \*rx_lprime)
:   Verify lprime.

**Parameters**

`struct device *dev`
:   device corresponding to the mei_cl_device

`struct hdcp_port_data *data`
:   Intel HW specific hdcp data

`struct hdcp2_lc_send_lprime *rx_lprime`
:   LC_Send_L_prime msg for ME FW verification

**Return**

0 on Success, <0 on Failure

int mei_hdcp_get_session_key(struct [device](../infrastructure.md#c.device "device") \*dev, struct hdcp_port_data \*data, struct hdcp2_ske_send_eks \*ske_data)
:   Prepare SKE_Send_Eks.

**Parameters**

`struct device *dev`
:   device corresponding to the mei_cl_device

`struct hdcp_port_data *data`
:   Intel HW specific hdcp data

`struct hdcp2_ske_send_eks *ske_data`
:   SKE_Send_Eks msg output from ME FW.

**Return**

0 on Success, <0 on Failure

int mei_hdcp_repeater_check_flow_prepare_ack(struct [device](../infrastructure.md#c.device "device") \*dev, struct hdcp_port_data \*data, struct hdcp2_rep_send_receiverid_list \*rep_topology, struct hdcp2_rep_send_ack \*rep_send_ack)
:   Validate the Downstream topology and prepare rep_ack.

**Parameters**

`struct device *dev`
:   device corresponding to the mei_cl_device

`struct hdcp_port_data *data`
:   Intel HW specific hdcp data

`struct hdcp2_rep_send_receiverid_list *rep_topology`
:   Receiver ID List to be validated

`struct hdcp2_rep_send_ack *rep_send_ack`
:   repeater ack from ME FW.

**Return**

0 on Success, <0 on Failure

int mei_hdcp_verify_mprime(struct [device](../infrastructure.md#c.device "device") \*dev, struct hdcp_port_data \*data, struct hdcp2_rep_stream_ready \*stream_ready)
:   Verify mprime.

**Parameters**

`struct device *dev`
:   device corresponding to the mei_cl_device

`struct hdcp_port_data *data`
:   Intel HW specific hdcp data

`struct hdcp2_rep_stream_ready *stream_ready`
:   RepeaterAuth_Stream_Ready msg for ME FW verification.

**Return**

0 on Success, <0 on Failure

int mei_hdcp_enable_authentication(struct [device](../infrastructure.md#c.device "device") \*dev, struct hdcp_port_data \*data)
:   Mark a port as authenticated through ME FW

**Parameters**

`struct device *dev`
:   device corresponding to the mei_cl_device

`struct hdcp_port_data *data`
:   Intel HW specific hdcp data

**Return**

0 on Success, <0 on Failure

int mei_hdcp_close_session(struct [device](../infrastructure.md#c.device "device") \*dev, struct hdcp_port_data \*data)
:   Close the Wired HDCP Tx session of ME FW per port. This also disables the authenticated state of the port.

**Parameters**

`struct device *dev`
:   device corresponding to the mei_cl_device

`struct hdcp_port_data *data`
:   Intel HW specific hdcp data

**Return**

0 on Success, <0 on Failure

int mei_hdcp_component_match(struct [device](../infrastructure.md#c.device "device") \*dev, int subcomponent, void \*data)
:   compare function for matching mei hdcp.

**Parameters**

`struct device *dev`
:   master device

`int subcomponent`
:   subcomponent to match (I915_COMPONENT_HDCP)

`void *data`
:   compare data (mei hdcp device)

**Description**

> The function checks if the driver is i915, the subcomponent is HDCP
> and the grand parent of hdcp and the parent of i915 are the same
> PCH device.

**Return**

- 1 - if components match
- 0 - otherwise
