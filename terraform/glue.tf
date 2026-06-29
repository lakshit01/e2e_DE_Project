resource "aws_iam_role" "glue_role" {

  name = "${local.name_prefix}-glue-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"

    Statement = [{
      Effect = "Allow"

      Principal = {
        Service = "glue.amazonaws.com"
      }

      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "glue_service" {

  role = aws_iam_role.glue_role.name

  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"

}

data "aws_iam_policy_document" "glue_s3" {

  statement {

    actions = [

      "s3:GetObject",
      "s3:PutObject",
      "s3:ListBucket"

    ]

    resources = [

      aws_s3_bucket.data_lake.arn,
      "${aws_s3_bucket.data_lake.arn}/*"

    ]

  }

}

resource "aws_iam_policy" "glue_s3" {

  name   = "${local.name_prefix}-glue-s3"

  policy = data.aws_iam_policy_document.glue_s3.json

}

resource "aws_iam_role_policy_attachment" "glue_s3" {

  role = aws_iam_role.glue_role.name

  policy_arn = aws_iam_policy.glue_s3.arn

}