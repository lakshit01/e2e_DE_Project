#################################################
# AWS
#################################################

variable "aws_region" {

  description = "AWS Region"

  type = string

  default = "ap-south-1"

}

#################################################
# Project
#################################################

variable "project_name" {

  description = "Project Name"

  type = string

  default = "logistics"

}

variable "environment" {

  description = "Deployment Environment"

  type = string

  default = "dev"

}

#################################################
# RDS
#################################################

variable "db_name" {

  default = "logistics"

}

variable "db_username" {

  default = "admin"

}

variable "db_password" {

  description = "Database Password"

  sensitive = true

  type = string

}