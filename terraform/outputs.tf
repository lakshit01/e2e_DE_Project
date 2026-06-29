#################################################
# NETWORK
#################################################

output "vpc_id" {

  value = data.aws_vpc.default.id

}

#################################################
# STORAGE
#################################################

output "data_lake_bucket" {

  value = aws_s3_bucket.data_lake.bucket

}

output "data_lake_bucket_arn" {

  value = aws_s3_bucket.data_lake.arn

}

#################################################
# SUBNETS
#################################################

output "subnet_ids" {

  value = data.aws_subnets.default.ids

}

#################################################
# RDS
#################################################

output "rds_endpoint" {

  value = aws_db_instance.mysql.address

}

output "rds_port" {

  value = aws_db_instance.mysql.port

}

output "rds_database" {

  value = aws_db_instance.mysql.db_name

}

#################################################
# DMS
#################################################

output "dms_replication_instance" {

  value = aws_dms_replication_instance.main.replication_instance_id

}

output "dms_replication_instance_arn" {

  value = aws_dms_replication_instance.main.replication_instance_arn

}

#################################################
# DMS ENDPOINTS
#################################################

output "mysql_source_endpoint" {

  value = aws_dms_endpoint.mysql_source.endpoint_arn

}

output "s3_target_endpoint" {

  value = aws_dms_endpoint.s3_target.endpoint_arn

}