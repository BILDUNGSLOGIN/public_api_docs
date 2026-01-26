
# Usage of BILDUNGSLOGIN- Services

Legal and organisational conditions for the use of BILDUNGSLOGIN services.

To use the BILDUNGSLOGIN- Broker and the provided API's, certain organizational and legal conditions must be met.

For further details and information, please [contact the nice guys from BILDUNGSLOGIN](https://info.bildungslogin.de/kontakt/anfrage-fuer-myportal-myschool).


# OIDC- Connection to BILDUNGSLOGIN
To connect your Organization to the BILDUNGSLOGIN- Broker, you require at least a confidential client, which is then configured to connect at BILDUNGSLOGIN.

## To connect a generic Keycloak™ to BILDUNGSLOGIN

Please follow the [How-To Document](./OIDC_Connection/README.md) for more detailed information.

## To connect a UCS- Keycloak™ to BILDUNGSLOGIN
Please follow the [How-To Document](./OIDC_Connection/README.md) for more detailed information.

# BILDUNGSLOGIN Connect API

The following API is being used by BILDUNGSLOGIN and Identity Providers (IdP's). The documentation is provided as-is, under the license terms provided [as documented](LICENSE.txt). The license terms do apply exclusively for documentation purposes, not for the creation or usage of software thereof.

[The BiLo-Connect API](bilo-connect.json) is used for the retrieval of organizational structure data (organizations, groups, users and their dependencies), as well as user- context data.
See [the specific Readme- Document](bilo_connect.md) for detailed information.


# BILDUNGSLOGIN Media- and License- API's

The following API's are being used by BILDUNGSLOGIN and Publishers as part of the Association of German Publishers within the BILDUNGSLOGIN GmbH.

This documentation is provided as-is, under the license terms provided [as documented](LICENSE.txt). The license terms do apply exclusively for documentation purposes, not for the creation or usage of software thereof.

## BILDUNGSLOGIN Metadata- API

[This API](media_APIs/bilo-licensepackage.json) is used for the provisioning of Media- Metadata

## BILDUNGSLOGIN License-Package API

[This API](media_APIs/bilo-media.json) is used for the provisioning of License- Packages
## BILDUNGSLOGIN License-Retrieval API (v1)

[This API](media_APIs/bilo-licenseretrieval_v1.json) is used for the retrieval of user- specific licenses, as well as user- context

## BILDUNGSLOGIN License-Retrieval API (v2)

[This API](media_APIs/bilo-licenseretrieval_v2.json) is used for the retrieval of user- specific licenses, as well as user- context. This API is an extension of the v1 API, providing additional functionality and data.