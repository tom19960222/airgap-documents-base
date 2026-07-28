---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_deployment module – Create or destroy Azure Resource Manager template deployments"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_deployment_module.html
fetched_at: 2026-07-28T01:12:58+00:00
---
# azure.azcollection.azure_rm_deployment module – Create or destroy Azure Resource Manager template deployments

> **Note:**
>
> This module is part of the [azure.azcollection collection](https://galaxy.ansible.com/ui/repo/published/azure/azcollection/) (version 1.19.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install azure.azcollection`.
> You need further requirements to be able to use this module,
> see [Requirements](azure_rm_deployment_module.md#ansible-collections-azure-azcollection-azure-rm-deployment-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_deployment`.

New in azure.azcollection 0.1.0

- [Synopsis](azure_rm_deployment_module.md#synopsis)
- [Requirements](azure_rm_deployment_module.md#requirements)
- [Parameters](azure_rm_deployment_module.md#parameters)
- [Notes](azure_rm_deployment_module.md#notes)
- [See Also](azure_rm_deployment_module.md#see-also)
- [Examples](azure_rm_deployment_module.md#examples)
- [Return Values](azure_rm_deployment_module.md#return-values)

## [Synopsis](azure_rm_deployment_module.md#id1)

- Create or destroy Azure Resource Manager template deployments via the Azure SDK for Python.
- You can find some quick start templates in GitHub here <https://github.com/azure/azure-quickstart-templates>.
- For more information on Azure Resource Manager templates see <https://azure.microsoft.com/en-us/documentation/articles/resource-group-template-deploy/>.

## [Requirements](azure_rm_deployment_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_deployment_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **deployment_mode**  string | In incremental mode, resources are deployed without deleting existing resources that are not included in the template.  In complete mode resources are deployed and existing resources in the resource group not included in the template are deleted.  **Choices:**   - `"complete"` - `"incremental"` ← (default) |
| **location**  string | The geo-locations in which the resource group will be located.  **Default:** `"westus"` |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  aliases: deployment_name  string | The name of the deployment to be tracked in the resource group deployment history.  Re-using a deployment name will overwrite the previous value in the resource group’s deployment history.  **Default:** `"ansible-arm"` |
| **parameters**  dictionary | A hash of all the required template variables for the deployment template. This parameter is mutually exclusive with *parameters_link*.  Either *parameters_link* or *parameters* is required if *state=present*. |
| **parameters_link**  string | Uri of file containing the parameters body. This parameter is mutually exclusive with *parameters*.  Either *parameters_link* or *parameters* is required if *state=present*. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  aliases: resource_group_name  string / required | The resource group name to use or create to host the deployed template. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | If *state=present*, template will be created.  If *state=present* and deployment exists, it will be updated.  If *state=absent*, the resource group will be removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **template**  dictionary | A hash containing the templates inline. This parameter is mutually exclusive with *template_link*.  Either *template* or *template_link* is required if *state=present*. |
| **template_link**  string | Uri of file containing the template body. This parameter is mutually exclusive with *template*.  Either *template* or *template_link* is required if *state=present*. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **wait_for_deployment_completion**  boolean | Whether or not to block until the deployment has completed.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_deployment_polling_period**  integer | Time (in seconds) to wait between polls when waiting for deployment completion.  **Default:** `10` |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_deployment_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_deployment_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_deployment_module.md#id6)

```yaml+jinja
# Destroy a template deployment
- name: Destroy Azure Deploy
  azure_rm_deployment:
    resource_group: myResourceGroup
    name: myDeployment
    state: absent

# Create or update a template deployment based on uris using parameter and template links
- name: Create Azure Deploy
  azure_rm_deployment:
    resource_group: myResourceGroup
    name: myDeployment
    template_link: 'https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-vm-simple-linux/azuredeploy.json'
    parameters_link: 'https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-vm-simple-linux/azuredeploy.parameters.json'

# Create or update a template deployment based on a uri to the template and parameters specified inline.
# This deploys a VM with SSH support for a given public key, then stores the result in 'azure_vms'. The result is then
# used to create a new host group. This host group is then used to wait for each instance to respond to the public IP SSH.

- name: Create Azure Deploy
  azure_rm_deployment:
    resource_group: myResourceGroup
    name: myDeployment
    parameters:
      newStorageAccountName:
        value: devopsclestorage1
      adminUsername:
        value: devopscle
      dnsNameForPublicIP:
        value: devopscleazure
      location:
        value: West US
      vmSize:
        value: Standard_A2
      vmName:
        value: ansibleSshVm
      sshKeyData:
        value: YOUR_SSH_PUBLIC_KEY
    template_link: 'https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-vm-sshkey/azuredeploy.json'
  register: azure
- name: Add new instance to host group
  add_host:
    hostname: "{{ item['ips'][0].public_ip }}"
    groupname: azure_vms
  loop: "{{ azure.deployment.instances }}"

# Deploy an Azure WebApp running a hello world'ish node app
- name: Create Azure WebApp Deployment at http://devopscleweb.azurewebsites.net/hello.js
  azure_rm_deployment:
    resource_group: myResourceGroup
    name: myDeployment
    parameters:
      repoURL:
        value: 'https://github.com/devigned/az-roadshow-oss.git'
      siteName:
        value: devopscleweb
      hostingPlanName:
        value: someplan
      siteLocation:
        value: westus
      sku:
        value: Standard
    template_link: 'https://raw.githubusercontent.com/azure/azure-quickstart-templates/master/201-web-app-github-deploy/azuredeploy.json'

# Create or update a template deployment based on an inline template and parameters
- name: Create Azure Deploy
  azure_rm_deployment:
    resource_group: myResourceGroup
    name: myDeployment
    template:
      $schema: "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#"
      contentVersion: "1.0.0.0"
      parameters:
        newStorageAccountName:
          type: "string"
          metadata:
            description: "Unique DNS Name for the Storage Account where the Virtual Machine's disks will be placed."
        adminUsername:
          type: "string"
          metadata:
            description: "User name for the Virtual Machine."
        adminPassword:
          type: "securestring"
          metadata:
            description: "Password for the Virtual Machine."
        dnsNameForPublicIP:
          type: "string"
          metadata:
            description: "Unique DNS Name for the Public IP used to access the Virtual Machine."
        ubuntuOSVersion:
          type: "string"
          defaultValue: "14.04.2-LTS"
          allowedValues:
            - "12.04.5-LTS"
            - "14.04.2-LTS"
            - "15.04"
          metadata:
            description: >
                         The Ubuntu version for the VM. This will pick a fully patched image of this given Ubuntu version.
                         Allowed values: 12.04.5-LTS, 14.04.2-LTS, 15.04."
      variables:
        location: "West US"
        imagePublisher: "Canonical"
        imageOffer: "UbuntuServer"
        OSDiskName: "osdiskforlinuxsimple"
        nicName: "myVMNic"
        addressPrefix: "192.0.2.0/24"
        subnetName: "Subnet"
        subnetPrefix: "10.0.0.0/24"
        storageAccountType: "Standard_LRS"
        publicIPAddressName: "myPublicIP"
        publicIPAddressType: "Dynamic"
        vmStorageAccountContainerName: "vhds"
        vmName: "MyUbuntuVM"
        vmSize: "Standard_D1"
        virtualNetworkName: "MyVNET"
        vnetID: "[resourceId('Microsoft.Network/virtualNetworks',variables('virtualNetworkName'))]"
        subnetRef: "[concat(variables('vnetID'),'/subnets/',variables('subnetName'))]"
      resources:
        - type: "Microsoft.Storage/storageAccounts"
          name: "[parameters('newStorageAccountName')]"
          apiVersion: "2015-05-01-preview"
          location: "[variables('location')]"
          properties:
            accountType: "[variables('storageAccountType')]"
        - apiVersion: "2015-05-01-preview"
          type: "Microsoft.Network/publicIPAddresses"
          name: "[variables('publicIPAddressName')]"
          location: "[variables('location')]"
          properties:
            publicIPAllocationMethod: "[variables('publicIPAddressType')]"
            dnsSettings:
              domainNameLabel: "[parameters('dnsNameForPublicIP')]"
        - type: "Microsoft.Network/virtualNetworks"
          apiVersion: "2015-05-01-preview"
          name: "[variables('virtualNetworkName')]"
          location: "[variables('location')]"
          properties:
            addressSpace:
              addressPrefixes:
                - "[variables('addressPrefix')]"
            subnets:
              -
                name: "[variables('subnetName')]"
                properties:
                  addressPrefix: "[variables('subnetPrefix')]"
        - type: "Microsoft.Network/networkInterfaces"
          apiVersion: "2015-05-01-preview"
          name: "[variables('nicName')]"
          location: "[variables('location')]"
          dependsOn:
            - "[concat('Microsoft.Network/publicIPAddresses/', variables('publicIPAddressName'))]"
            - "[concat('Microsoft.Network/virtualNetworks/', variables('virtualNetworkName'))]"
          properties:
            ipConfigurations:
              -
                name: "ipconfig1"
                properties:
                  privateIPAllocationMethod: "Dynamic"
                  publicIPAddress:
                    id: "[resourceId('Microsoft.Network/publicIPAddresses',variables('publicIPAddressName'))]"
                  subnet:
                    id: "[variables('subnetRef')]"
        - type: "Microsoft.Compute/virtualMachines"
          apiVersion: "2015-06-15"
          name: "[variables('vmName')]"
          location: "[variables('location')]"
          dependsOn:
            - "[concat('Microsoft.Storage/storageAccounts/', parameters('newStorageAccountName'))]"
            - "[concat('Microsoft.Network/networkInterfaces/', variables('nicName'))]"
          properties:
            hardwareProfile:
              vmSize: "[variables('vmSize')]"
            osProfile:
              computername: "[variables('vmName')]"
              adminUsername: "[parameters('adminUsername')]"
              adminPassword: "[parameters('adminPassword')]"
            storageProfile:
              imageReference:
                publisher: "[variables('imagePublisher')]"
                offer: "[variables('imageOffer')]"
                sku: "[parameters('ubuntuOSVersion')]"
                version: "latest"
              osDisk:
                name: "osdisk"
                vhd:
                  uri: >
                       [concat('http://',parameters('newStorageAccountName'),'.blob.core.windows.net/',variables('vmStorageAccountContainerName'),'/',
                       variables('OSDiskName'),'.vhd')]
                caching: "ReadWrite"
                createOption: "FromImage"
            networkProfile:
              networkInterfaces:
                -
                  id: "[resourceId('Microsoft.Network/networkInterfaces',variables('nicName'))]"
            diagnosticsProfile:
              bootDiagnostics:
                enabled: "true"
                storageUri: "[concat('http://',parameters('newStorageAccountName'),'.blob.core.windows.net')]"
    parameters:
      newStorageAccountName:
        value: devopsclestorage
      adminUsername:
        value: devopscle
      adminPassword:
        value: Password1!
      dnsNameForPublicIP:
        value: devopscleazure
```

## [Return Values](azure_rm_deployment_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **deployment**  complex | Deployment details.  **Returned:** always |
| **group_name**  string | Name of the resource group.  **Returned:** always  **Sample:** `"myResourceGroup"` |
| **id**  string | The Azure ID of the deployment.  **Returned:** always  **Sample:** `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Resources/deployments/myD eployment"` |
| **instances**  list / elements=string | Provides the public IP addresses for each VM instance.  **Returned:** always |
| **ips**  list / elements=string | List of Public IP addresses.  **Returned:** always |
| **dns_settings**  complex | DNS Settings.  **Returned:** always |
| **domain_name_label**  string | Domain Name Label.  **Returned:** always  **Sample:** `"myvirtualmachine"` |
| **fqdn**  string | Fully Qualified Domain Name.  **Returned:** always  **Sample:** `"myvirtualmachine.eastus2.cloudapp.azure.com"` |
| **id**  string | Public IP resource id.  **Returned:** always  **Sample:** `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Network/p ublicIPAddresses/myPublicIP"` |
| **name**  string | Public IP resource name.  **Returned:** always  **Sample:** `"myPublicIP"` |
| **public_ip**  string | Public IP address value.  **Returned:** always  **Sample:** `"104.209.244.123"` |
| **public_ip_allocation_method**  string | Public IP allocation method.  **Returned:** always  **Sample:** `"Dynamic"` |
| **vm_name**  string | Virtual machine name.  **Returned:** always  **Sample:** `"myvirtualmachine"` |
| **name**  string | Name of the deployment.  **Returned:** always  **Sample:** `"myDeployment"` |
| **outputs**  dictionary | Dictionary of outputs received from the deployment.  **Returned:** always  **Sample:** `{"hostname": {"type": "String", "value": "myvirtualmachine.eastus2.cloudapp.azure.com"}}` |

### Authors

- David Justice (@devigned)
- Laurent Mazuel (@lmazuel)
- Andre Price (@obsoleted)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
