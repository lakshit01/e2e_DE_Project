def validate_unique(
    df,
    column_name
):

    duplicate_count = (
        df[column_name]
        .duplicated()
        .sum()
    )

    if duplicate_count > 0:

        raise ValueError(
            f"{duplicate_count} duplicates found in {column_name}"
        )

    return True