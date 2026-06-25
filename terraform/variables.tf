variable "aws_region" {

  type = string

}

variable "project_name" {

  type = string

}

variable "environment" {

  type = string

}

variable "alert_email" {

  type = string

}

variable "db_username" {
  type = string
}

variable "db_password" {
  type      = string
  sensitive = true
}