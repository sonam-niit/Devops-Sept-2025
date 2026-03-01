# Practice Task using Terraform

- create RDS MySQL instance (database)
- use free tier eligible
- enabled automated backup
- set up backup window
- disabled public access
- add meaningful tags

## Folder Structure

- rds-terraform
    + providers.tf
    + main.tf
    + variables.tf
    + outputs.tf (provide database endpoint)