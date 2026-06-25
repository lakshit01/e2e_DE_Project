resource "aws_s3_bucket" "raw" {

  bucket = "${var.project_name}-${var.environment}-raw"

}

resource "aws_s3_bucket" "silver" {

  bucket = "${var.project_name}-${var.environment}-silver"

}

resource "aws_s3_bucket" "glue" {

  bucket = "${var.project_name}-${var.environment}-glue"

}

resource "aws_s3_bucket" "mwaa" {

  bucket = "${var.project_name}-${var.environment}-mwaa"

}



resource "aws_cloudwatch_log_group" "glue_logs" {

  name = "/etl/glue"

  retention_in_days = 30

}

resource "aws_cloudwatch_log_group" "dms_logs" {

  name = "/etl/dms"

  retention_in_days = 30

}

resource "aws_cloudwatch_log_group" "mwaa_logs" {

  name = "/etl/mwaa"

  retention_in_days = 30

}



resource "aws_sns_topic" "alerts" {

  name = "logistics-alerts"

}



resource "aws_sns_topic_subscription" "email_alert" {

  topic_arn = aws_sns_topic.alerts.arn

  protocol = "email"

  endpoint = var.alert_email

}



resource "aws_iam_role" "glue_role" {

  name = "logistics-glue-role"

  assume_role_policy = jsonencode({

    Version = "2012-10-17"

    Statement = [

      {

        Action = "sts:AssumeRole"

        Effect = "Allow"

        Principal = {

          Service = "glue.amazonaws.com"

        }

      }

    ]

  })

}




resource "aws_iam_role_policy_attachment" "glue_policy" {

  role = aws_iam_role.glue_role.name

  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"

}




resource "aws_iam_role" "dms_role" {

  name = "logistics-dms-role"

  assume_role_policy = jsonencode({

    Version = "2012-10-17"

    Statement = [

      {

        Action = "sts:AssumeRole"

        Effect = "Allow"

        Principal = {

          Service = "dms.amazonaws.com"

        }

      }

    ]

  })

}





resource "aws_iam_role_policy_attachment" "dms_policy" {

  role = aws_iam_role.dms_role.name

  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"

}



resource "aws_iam_role" "mwaa_role" {

  name = "logistics-mwaa-role"

  assume_role_policy = jsonencode({

    Version = "2012-10-17"

    Statement = [

      {

        Action = "sts:AssumeRole"

        Effect = "Allow"

        Principal = {

          Service = [

            "airflow.amazonaws.com",

            "airflow-env.amazonaws.com"

          ]

        }

      }

    ]

  })

}




resource "aws_secretsmanager_secret" "snowflake_secret" {

  name = "snowflake-credentials"

}




resource "aws_secretsmanager_secret_version" "snowflake_secret_value" {

  secret_id = aws_secretsmanager_secret.snowflake_secret.id

  secret_string = jsonencode({

    username = "lakshit"

    password = "SNOWFLAKEshit@321"

  })

}