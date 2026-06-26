locals {

  #################################################
  # Naming Convention
  #################################################

  name_prefix = "${var.project_name}-${var.environment}"

  #################################################
  # Common Tags
  #################################################

  common_tags = {

    Project = var.project_name

    Environment = var.environment

    ManagedBy = "Terraform"

    Owner = "Lakshit"

  }

}