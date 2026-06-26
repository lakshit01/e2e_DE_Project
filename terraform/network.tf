#################################################
# DEFAULT VPC
#################################################

data "aws_vpc" "default" {

  default = true

}

#################################################
# DEFAULT SUBNETS
#################################################

data "aws_subnets" "default" {

  filter {

    name = "vpc-id"

    values = [data.aws_vpc.default.id]

  }

}

#################################################
# RDS SECURITY GROUP
#################################################

resource "aws_security_group" "rds" {

  name = "${local.name_prefix}-rds-sg"

  description = "Security Group for MySQL RDS"

  vpc_id = data.aws_vpc.default.id

  ingress {

    description = "MySQL"

    from_port = 3306

    to_port = 3306

    protocol = "tcp"

    cidr_blocks = [
      "182.77.75.139/32"
    ]

  }

  egress {

    from_port = 0

    to_port = 0

    protocol = "-1"

    cidr_blocks = [
      "0.0.0.0/0"
    ]

  }

}