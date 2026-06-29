#################################################
# DEFAULT VPC
#################################################

data "aws_vpc" "default" {

  default = true

}

resource "aws_iam_role_policy_attachment" "dms_vpc_policy" {

  role = aws_iam_role.dms_vpc_role.name

  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonDMSVPCManagementRole"

}


resource "aws_iam_role_policy_attachment" "dms_cloudwatch_policy" {

  role = aws_iam_role.dms_cloudwatch_role.name

  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonDMSCloudWatchLogsRole"

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

  ingress {

    description = "AWS DMS"

    from_port = 3306

    to_port = 3306

    protocol = "tcp"

    security_groups = [

      aws_security_group.dms.id

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