resource "aws_iam_role" "glue_role" {

  name =
  "logistics-glue-role"

  assume_role_policy =
  data.aws_iam_policy_document
  .glue_assume_role.json
}

resource "aws_iam_role_policy_attachment"

resource "aws_iam_role"
"dms_role"

resource "aws_iam_role"
"mwaa_role"