from core.mapper import PO_COLUMN_MAP, GR_COLUMN_MAP


def validate_po_columns(df):

    missing = [
        col for col in PO_COLUMN_MAP.keys()
        if col not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Purchase Order missing columns : {missing}"
        )

    return True


def validate_gr_columns(df):

    missing = [
        col for col in GR_COLUMN_MAP.keys()
        if col not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Goods Receipt missing columns : {missing}"
        )

    return True