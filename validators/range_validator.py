def validate_range(
    df,
    column_name,
    minimum,
    maximum
):

    invalid_rows = df[
        (df[column_name] < minimum)
        |
        (df[column_name] > maximum)
    ]

    if len(invalid_rows) > 0:

        raise ValueError(
            f"Invalid values found in {column_name}"
        )

    return True