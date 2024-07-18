# BILO- Connect IdP- Structure Data API
This API provides a simple structure for relevant Organization Structure data of an IdP. It provides two general routes:
- a route to provide an overview of authorized Organizations. This route is optional, but recommended (see also [Administered Organizations](#administered-organizations-administered_orgs))
- a route to provide the complete structure data of one or more Organization

## Authentication
Authentication should be handled as per OpenAPI- Specification

## Authorization
The Authorization of the API is split in two parts. This is reflected as an example with the "scopes"- documentation in the OpenAPI- Documentation.

### Organization- Admin- Role (org_admin)
The IdP must provide an OIDC- Claim (e.g. Role) to ensure that the current token is allowed to query the BILO- Structure- API.

#### Client Credentials Grant Token
If a client credentials grant is being used for authorization, the implementation of this feature is up to the implementer

#### Authorization Grant Token
This method allows a user which is allowed to access the BILO Licensemanager the additional right to query the BILO- Structure API of the corresponding IdP.
Hence, a claim in the access token of the user (e.g. expressed as a Role) needs to declare this right.


### Administered Organizations (administered_orgs)
The IdP shall provide an OIDC- Claim containing a list of organizations, which the token holder is allowed query.

This feature is optional, depending on the provisioning of the auth_orgs- API.

#### Client Credentials Grant Token
If a client credentials grant is being used for authorization, the implementation of this feature is up to the implementer

#### Authorization Grant Token
This claim must contain a list of allowed Organization- ID's


# OpenAPI Specification
The [OpenAPI Specification of BILO- Connect](./openapi_bilo_connect.json) provides the implementer with all relevant information to implement the API for their IdP. Please note that the "scopes"- paragraph of the documentation is meant as an example for the IdP. See [Authorization](#authorization) for more information.
