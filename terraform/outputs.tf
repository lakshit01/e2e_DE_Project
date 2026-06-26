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