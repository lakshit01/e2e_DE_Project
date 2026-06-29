#################################################
# DMS SECURITY GROUP
#################################################

resource "aws_security_group" "dms" {

  name        = "${local.name_prefix}-dms-sg"
  description = "Security Group for AWS DMS"

  vpc_id = data.aws_vpc.default.id

  egress {

    from_port = 0

    to_port = 0

    protocol = "-1"

    cidr_blocks = ["0.0.0.0/0"]

  }

  tags = local.common_tags

}

#################################################
# DMS SUBNET GROUP
#################################################

resource "aws_dms_replication_subnet_group" "main" {

  replication_subnet_group_id = "${local.name_prefix}-dms-subnet"

  replication_subnet_group_description = "Subnet Group for DMS"

  subnet_ids = data.aws_subnets.default.ids

  tags = local.common_tags

}

#################################################
# DMS REPLICATION INSTANCE
#################################################

resource "aws_dms_replication_instance" "main" {

  replication_instance_id = "${local.name_prefix}-dms"

  replication_instance_class = "dms.t3.small"

  allocated_storage = 50

  engine_version = "3.5.4"

  publicly_accessible = true

  multi_az = false

  auto_minor_version_upgrade = true

  apply_immediately = true

  replication_subnet_group_id = aws_dms_replication_subnet_group.main.id

  vpc_security_group_ids = [
    aws_security_group.dms.id
  ]

  tags = local.common_tags
}

#################################################
# SOURCE ENDPOINT (MYSQL RDS)
#################################################

resource "aws_dms_endpoint" "mysql_source" {

  endpoint_id = "${local.name_prefix}-mysql-source"

  endpoint_type = "source"

  engine_name = "mysql"

  server_name = aws_db_instance.mysql.address

  port = 3306

  database_name = aws_db_instance.mysql.db_name

  username = var.db_username

  password = var.db_password

  ssl_mode = "none"

  tags = local.common_tags

}

#################################################
# TARGET ENDPOINT (S3)
#################################################

resource "aws_dms_endpoint" "s3_target" {

  endpoint_id   = "${local.name_prefix}-s3-target"
  endpoint_type = "target"
  engine_name   = "s3"

  s3_settings {

    bucket_name = aws_s3_bucket.data_lake.bucket

    bucket_folder = "raw/mysql"

    service_access_role_arn = aws_iam_role.dms_access_role.arn

    data_format = "csv"

    csv_delimiter = ","

    csv_row_delimiter = "\n"

    add_column_name = true

    timestamp_column_name = "dms_timestamp"

    compression_type = "NONE"

  }

  tags = local.common_tags
}

#################################################
# REPLICATION TASK
#################################################

resource "aws_dms_replication_task" "full_load" {

  replication_task_id = "${local.name_prefix}-full-load"

  migration_type = "full-load"

  replication_instance_arn = aws_dms_replication_instance.main.replication_instance_arn

  source_endpoint_arn = aws_dms_endpoint.mysql_source.endpoint_arn

  target_endpoint_arn = aws_dms_endpoint.s3_target.endpoint_arn

  table_mappings = file("${path.module}/table-mappings.json")

  replication_task_settings = file("${path.module}/task-settings.json")

  tags = local.common_tags

}