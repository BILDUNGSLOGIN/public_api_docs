# BILDUNGSLOGIN Media API's

The following API's are being used by BILDUNGSLOGIN and Publishers as part of the Association of German Publishers within the BILDUNGSLOGIN GmbH.

This documentation is provided as-is, under the license terms provided [as documented](LICENSE.txt). The license terms do apply exclusively for documentation purposes, not for the creation or usage of software thereof.


## BILDUNGSLOGIN Metadata- API

[This API](bilo-licensepackage.json) is used for the provisioning of Media- Metadata


## BILDUNGSLOGIN License-Package API

[This API](bilo-media.json) is used for the provisioning of License- Packages


## BILDUNGSLOGIN License-Retrieval API (v1)

[This API](bilo-licenseretrieval_v1.json) is used for the retrieval of user- specific licenses, as well as user- context


## BILDUNGSLOGIN License-Retrieval API (v2)

[This API](bilo-licenseretrieval_v2.json) is used for the retrieval of user- specific licenses, as well as user- context. This API is an extension of the v1 API, providing additional functionality and data.


# BILDUNGSLOGIN Connect API's

The following API's are being used by BILDUNGSLOGIN and Identity Providers (IdP's). This documentation is provided as-is, under the license terms provided [as documented](LICENSE.txt). The license terms do apply exclusively for documentation purposes, not for the creation or usage of software thereof.


## BILDUNGSLOGIN BiLo-Connect API

[This API](bilo-connect.json) is used for the retrieval of organizational structure data (organizations, groups, users and their dependencies), as well as user- context data.
See [the specific Readme- Document](bilo_connect.md) for detailed information.


# OIDC- Connection to BILDUNGSLOGIN

To connect your Organization to the BILDUNGSLOGIN- Broker, you require at least a confidential client, which is then configured to connect at BILDUNGSLOGIN.

For details, please [contact the nice guys from BILDUNGSLOGIN](https://info.bildungslogin.de/kontakt/anfrage-fuer-myportal-myschool)

## Prepare your organizational Keycloak™ to connect to BILDUNGSLOGIN

To give you a hand how to connect to the BILDUNGSLOGIN- Broker, we provide a short [How-To Document](./OIDC_Connection/README.md).
