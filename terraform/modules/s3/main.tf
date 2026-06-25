resource "aws_s3_bucket" "raw" {

  bucket =
  "${var.project_name}-${var.environment}-raw"

}

resource "aws_s3_bucket" "silver" {

  bucket =
  "${var.project_name}-${var.environment}-silver"

}

resource "aws_s3_bucket" "glue" {

  bucket =
  "${var.project_name}-${var.environment}-glue"

}

resource "aws_s3_bucket" "mwaa" {

  bucket =
  "${var.project_name}-${var.environment}-mwaa"

}

resource "aws_s3_bucket" "tfstate" {

  bucket =
  "${var.project_name}-${var.environment}-tfstate"

}