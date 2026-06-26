#################################################
# RDS SUBNET GROUP
#################################################

resource "aws_db_subnet_group" "mysql" {

  name = "${local.name_prefix}-subnet-group"

  subnet_ids = data.aws_subnets.default.ids

  tags = {

    Name = "${local.name_prefix}-subnet-group"

  }

}

#################################################
# RDS PARAMETER GROUP
#################################################

resource "aws_db_parameter_group" "mysql" {

  name = "${local.name_prefix}-mysql-params"

  family = "mysql8.0"

  parameter {

    name = "binlog_format"

    value = "ROW"

  }

  parameter {

    name = "binlog_row_image"

    value = "FULL"

  }

}

#################################################
# MYSQL RDS
#################################################

resource "aws_db_instance" "mysql" {

  identifier = "${local.name_prefix}-mysql"

  engine = "mysql"

  engine_version = "8.0.45"

  instance_class = "db.t3.micro"

  allocated_storage = 20

  max_allocated_storage = 100

  db_name = var.db_name

  username = var.db_username

  password = var.db_password

  publicly_accessible = true

  skip_final_snapshot = true

  deletion_protection = false

  storage_encrypted = true

  multi_az = false

  backup_retention_period = 1

  db_subnet_group_name = aws_db_subnet_group.mysql.name

  parameter_group_name = aws_db_parameter_group.mysql.name

  vpc_security_group_ids = [

    aws_security_group.rds.id

  ]

  tags = {

    Name = "${local.name_prefix}-mysql"

  }

}