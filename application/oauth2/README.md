# oauth2

reference
- https://aaronparecki.com/oauth-2-simplified/

roles
- client: third-party application.
- resource server: API to access user's information.
- authorization server: interface for user to grant.
- resource owner: user.

creating an app
- redirect uris: https://yoursit/redirect, yournativeapp://redirect
- client id: public infromation.
- client secret: if cannot keep secret, e.g. javascript, native, not use.

authorization
- authorization code: for apps running on a web server, browser-based and mobile apps.
~~~~
// web server apps
// 1.generate a login link for user 
https://authorization-server.com/auth?response_type=code&
  client_id=CLIENT_ID&redirect_uri=REDIRECT_URI&scope=photos&state=1234zyx

// 2.user click link, service redirect
https://example-app.com/cb?code=AUTH_CODE_HERE&state=1234zyx

// 3.exchange token
POST https://api.authorization-server.com/token
  grant_type=authorization_code&
  code=AUTH_CODE_HERE&
  redirect_uri=REDIRECT_URI&
  client_id=CLIENT_ID&
  client_secret=CLIENT_SECRET
  
{
  "access_token":"RsT5OjbzRn430zqMLgV3Ia",
  "expires_in":3600
}

{
  "error":"invalid_request"
}

// browser-based apps
// 3.exchange token: secret not used
POST https://api.authorization-server.com/token
  grant_type=authorization_code&
  code=AUTH_CODE_HERE&
  redirect_uri=REDIRECT_URI&
  client_id=CLIENT_ID   

// mobile apps
fbauth2://authorize?response_type=code&client_id=CLIENT_ID
  &redirect_uri=REDIRECT_URI&scope=email&state=1234zyx
  
https://facebook.com/dialog/oauth?response_type=code&client_id=CLIENT_ID
  &redirect_uri=REDIRECT_URI&scope=email&state=1234zyx 
  
fb00000000://authorize?code=AUTHORIZATION_CODE&state=1234zyx

POST https://api.authorization-server.com/token
  grant_type=authorization_code&
  code=AUTH_CODE_HERE&
  redirect_uri=REDIRECT_URI&
  client_id=CLIENT_ID&
  code_verifier=VERIFIER_STRING 
~~~~

- password: for logging in with a username and password. must only be used by apps created by the service itself, e.g. twitter app for twitter service.
~~~~
POST https://api.authorization-server.com/token
  grant_type=password&
  username=USERNAME&
  password=PASSWORD&
  client_id=CLIENT_ID
~~~~

- client credentials: for application access, need an access token to act on behalf of themselves rather than a user, e.g. information such as url and icon, statistics about the users of the app.
~~~~
POST https://api.authorization-server.com/token
    grant_type=client_credentials&
    client_id=CLIENT_ID&
    client_secret=CLIENT_SECRET
~~~~

- implicit: deprecated.