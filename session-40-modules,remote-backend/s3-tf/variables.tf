variable "bucket_name" {
  type = string
  description = "The Name of S3 Bucket"
}
variable "aws_region" {
  type = string
  description = "Region for AWS"
  default = "us-east-1"
}
variable "environment" {
  type = string
}