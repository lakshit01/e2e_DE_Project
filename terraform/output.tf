output "raw_bucket" {

  value = aws_s3_bucket.raw.bucket

}

output "silver_bucket" {

  value = aws_s3_bucket.silver.bucket

}

output "sns_topic" {

  value = aws_sns_topic.alerts.arn

}

output "glue_role_arn" {

  value = aws_iam_role.glue_role.arn

}

output "dms_role_arn" {

  value = aws_iam_role.dms_role.arn

}

output "mwaa_role_arn" {

  value = aws_iam_role.mwaa_role.arn

}

output "rds_endpoint" {

  value = aws_db_instance.logistics_mysql.address

}