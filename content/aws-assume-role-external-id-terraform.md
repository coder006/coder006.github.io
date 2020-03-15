Title: AWS Assume Role with External Id and Terraform
Date: 2020-02-06 16:30
Modified: 2020-02-06 16:30
Category: AWS
Tags: aws, terraform, assumerole, externalid
Slug: aws-assume-role-external-id-terraform
Authors: Ambar Mehrotra
Summary: AWS Assume Role with ExternalId and Terraform
Status: draft

AWS provides a multitude of options for users or services to authenticate with AWS and make API calls. The process usually involves creating __IAM users__ who can authenticate with AWS services in various ways. Most people are aware of the most commonly used key based authentiacation which involves using `aws_access_key_id` and `aws_secret_access_key` in either the `~/.aws/credentials` file or setting the equivalent environment variables.
Although, there might