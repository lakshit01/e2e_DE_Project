#################################################
# DATA LAKE
#################################################

resource "aws_s3_bucket" "data_lake" {

  bucket = "${local.name_prefix}-data-lake"

}

#################################################
# VERSIONING
#################################################

resource "aws_s3_bucket_versioning" "data_lake" {

  bucket = aws_s3_bucket.data_lake.id

  versioning_configuration {

    status = "Enabled"

  }

}

#################################################
# ENCRYPTION
#################################################

resource "aws_s3_bucket_server_side_encryption_configuration" "data_lake" {

  bucket = aws_s3_bucket.data_lake.id

  rule {

    apply_server_side_encryption_by_default {

      sse_algorithm = "AES256"

    }

  }

}

#################################################
# BLOCK PUBLIC ACCESS
#################################################

resource "aws_s3_bucket_public_access_block" "data_lake" {

  bucket = aws_s3_bucket.data_lake.id

  block_public_acls = true

  block_public_policy = true

  ignore_public_acls = true

  restrict_public_buckets = true

}

#################################################
# LIFECYCLE
#################################################

resource "aws_s3_bucket_lifecycle_configuration" "data_lake" {

  bucket = aws_s3_bucket.data_lake.id

  rule {

    id = "move-old-files"

    status = "Enabled"

    filter {}

    transition {

      days = 90

      storage_class = "STANDARD_IA"

    }

  }

}

#################################################
# PLACEHOLDER FOLDERS
#################################################

locals {

  bucket_folders = [

    "raw/",

    "raw/mysql/",

    "raw/api/",

    "raw/files/",

    "silver/",

    "gold/",

    "archive/",

    "logs/"

  ]

}

resource "aws_s3_object" "folders" {

  for_each = toset(local.bucket_folders)

  bucket = aws_s3_bucket.data_lake.id

  key = each.value

}