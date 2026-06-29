#################################################
# DMS VPC ROLE
#################################################

resource "aws_iam_role" "dms_vpc_role" {

  name = "dms-vpc-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"

    Statement = [
      {
        Effect = "Allow"

        Principal = {
          Service = "dms.amazonaws.com"
        }

        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "dms_vpc_role" {

  role = aws_iam_role.dms_vpc_role.name

  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonDMSVPCManagementRole"
}

#################################################
# DMS CLOUDWATCH ROLE
#################################################

resource "aws_iam_role" "dms_cloudwatch_role" {

  name = "dms-cloudwatch-logs-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"

    Statement = [
      {
        Effect = "Allow"

        Principal = {
          Service = "dms.amazonaws.com"
        }

        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "dms_cloudwatch_role" {

  role = aws_iam_role.dms_cloudwatch_role.name

  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonDMSCloudWatchLogsRole"
}

#################################################
# DMS S3 ACCESS ROLE
#################################################

resource "aws_iam_role" "dms_access_role" {

  name = "${local.name_prefix}-dms-s3-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"

    Statement = [
      {
        Effect = "Allow"

        Principal = {
          Service = "dms.amazonaws.com"
        }

        Action = "sts:AssumeRole"
      }
    ]
  })
}

#################################################
# DMS S3 POLICY
#################################################

data "aws_iam_policy_document" "dms_s3_policy" {

  statement {

    actions = [
      "s3:ListBucket"
    ]

    resources = [
      aws_s3_bucket.data_lake.arn
    ]
  }

  statement {

    actions = [
      "s3:GetObject",
      "s3:PutObject",
      "s3:DeleteObject"
    ]

    resources = [
      "${aws_s3_bucket.data_lake.arn}/*"
    ]
  }
}

resource "aws_iam_policy" "dms_s3_policy" {

  name = "${local.name_prefix}-dms-s3-policy"

  policy = data.aws_iam_policy_document.dms_s3_policy.json
}

resource "aws_iam_role_policy_attachment" "dms_s3_role" {

  role = aws_iam_role.dms_access_role.name

  policy_arn = aws_iam_policy.dms_s3_policy.arn
}