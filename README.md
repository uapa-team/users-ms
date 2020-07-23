## Users-ms

### Authentication Settings

For LDAP setting, use env variable LDAP_HOST. TLS expected 'cetificate.pem' file may be set before usage.
- To use DB, must be defined the following environment variables:
  - `USERS_DB_HOST`
  - `USERS_DB_PORT`
  - `USERS_DB_NAME`
  - `USERS_DB_USER`
  - `USERS_DB_PASS`
- For LDAP setting, use env variable `LDAP_HOST`. TLS expected `cetificate.pem` file may be set on the root of the project before usage.

### Initializing the database

To set up the database, load the data from users/fixtures/data.json using loaddata: https://docs.djangoproject.com/en/3.0/ref/django-admin/#loaddata.

### Usage of django-seed

There are two ways to populate the database via django-seed. First, there's the seed+app command (that uses the faker library) and with code (functionality was tested in uapapp/tests.py). More info: https://pypi.org/project/django-seed/#usage.
