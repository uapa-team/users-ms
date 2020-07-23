## Users-ms

### Authentication Settings

- To use DB, must be defined the following environment variables:
  - `USERS_DB_HOST`
  - `USERS_DB_PORT`
  - `USERS_DB_NAME`
  - `USERS_DB_USER`
  - `USERS_DB_PASS`
- For LDAP setting, use env variable `LDAP_HOST`. TLS expected `cetificate.pem` file may be set on the root of the project before usage.
