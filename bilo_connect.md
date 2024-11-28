# BILO- Connect IdP- Structure Data API
This API provides a simple structure for relevant Organization Structure data of an IdP. It provides three routes:
- a route to provide an overview of authorized Organizations. This route is optional, but recommended
- a route to provide the complete structure data of one or more Organization
- a route to provide user- specific context data

## Authentication
Authentication should be handled as per OAuth2- Specification, and should be provided as a Bearer- Token in the Authorization- Header. The token should be provided by the IdP providing the API.

## Authorization
The API should be protected by an OAuth2- Authorization Server. The API should provide scopes for the following routes:

### Organization- Routes (/orgs- and /org_info)
The recommended way to authenticate a user against these routes is to use an Authorization Grant token (access_token of the user querying the API).

The IdP should provide an OIDC- Claim (e.g. Role) to ensure that the current token is allowed to query the API. This claim will also be used to limit access to the license manager application.

The token should be provided by the IdP hosting the API, whereas:
- the `/org-info` - route will return a short list of the Organizations the user is allowed to administer
  - should this route be not available, the list of organizations the user is allowed to administer should be provided in a claim, containing the org_id's of the organizations to be used in the `/orgs`- route
- the `/orgs` - route will return the structure data of the Organization(s) the user is allowed to administer


### User- Context- Role (/user route)
The recommended way to authenticate a user against these routes is to use an Authorization Grant token (access_token of the user querying the API).

The IdP should provide an OIDC- Claim (e.g. Role) to ensure that the current token is allowed to query the API. If the IdP does not provide this claim, access to the API will be available for all users of the IdP.


# OpenAPI Specification
The [OpenAPI Specification of BILO- Connect](bilo-connect.json) provides the implementer with all relevant information to implement the API for their IdP. Please note that the "scopes"- paragraph of the documentation is meant as an example for the IdP. See [Authorization](#authorization) for more information.
