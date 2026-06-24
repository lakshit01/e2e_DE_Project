def validate_null(
    df,
    column_name
):

    null_count = (
        df[column_name]
        .isnull()
        .sum()
    )

    if null_count > 0:

        raise ValueError(
            f"{null_count} null values found in {column_name}"
        )

    return True