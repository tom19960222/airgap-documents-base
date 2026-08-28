---
collection: netbox
version: "4.2.9"
title: "Image Attachments"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/extras/imageattachment.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Image Attachments

Certain objects in NetBox support the attachment of uploaded images. These will be saved to the NetBox server and made available whenever the object is viewed.

## Fields

### Name

The name of the image being attached. If not defined, this will be inferred from the name of the uploaded file.

### Image

The image file to upload. Note that the uploaded file **must** be a supported image type, or validation will fail.
