#################################################
# DATA SOURCES
#################################################

data "aws_vpc" "default" {

  default = true

}

data "aws_subnets" "default" {

  filter {

    name = "vpc-id"

    values = [
      data.aws_vpc.default.id
    ]

  }

}


#################################################
# SECURITY GROUP
#################################################

resource "aws_security_group" "rds_mysql_sg" {

  name        = "logistics-rds-sg"
  description = "Allow MySQL"

  ingress {

    from_port = 3306
    to_port   = 3306

    protocol = "tcp"

    cidr_blocks = [
      "192.168.1.8/32"
    ]

  }

  egress {

    from_port = 0
    to_port   = 0

    protocol = "-1"

    cidr_blocks = [
      "192.168.1.8/32"
    ]

  }

}

#################################################
# RDS SUBNET GROUP
#################################################

resource "aws_db_subnet_group" "rds_subnet_group" {

  name = "logistics-subnet-group"

  subnet_ids = data.aws_subnets.default.ids

}

#################################################
# RDS MYSQL
#################################################

resource "aws_db_instance" "logistics_mysql" {

  identifier = "logistics-mysql"

  engine = "mysql"

  engine_version = "8.0"

  instance_class = "db.t3.micro"

  allocated_storage = 20

  username = var.db_username

  password = var.db_password

  publicly_accessible = true

  skip_final_snapshot = true

  db_subnet_group_name = aws_db_subnet_group.rds_subnet_group.name

  vpc_security_group_ids = [

    aws_security_group.rds_mysql_sg.id

  ]

}