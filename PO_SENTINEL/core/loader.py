from pathlib import Path

import pandas as pd


def load_purchase_order(file_path: str) -> pd.DataFrame:
    """
    Load Purchase Order Excel.
    """

    if not Path(file_path).exists():
        raise FileNotFoundError(file_path)

    return pd.read_excel(file_path)


def load_goods_receipt(file_path: str) -> pd.DataFrame:
    """
    Load Goods Receipt Excel.
    """

    if not Path(file_path).exists():
        raise FileNotFoundError(file_path)

    return pd.read_excel(file_path)

from core.mapper import PO_COLUMN_MAP, GR_COLUMN_MAP


def standardize_po(df):

    df = df.rename(columns=PO_COLUMN_MAP)

    df.columns = df.columns.str.strip()

    df["item_code"] = (
        df["item_code"]
        .astype(str)
        .str.strip()
        .str.upper()
    )

    df["po_no"] = (
        df["po_no"]
        .astype(str)
        .str.strip()
    )

    df["qty_order"] = (
        pd.to_numeric(
            df["qty_order"],
            errors="coerce"
        )
        .fillna(0)
    )

    df = df.drop_duplicates()

    return df


def standardize_gr(df):

    df = df.rename(columns=GR_COLUMN_MAP)

    df.columns = df.columns.str.strip()

    df["item_code"] = (
        df["item_code"]
        .astype(str)
        .str.strip()
        .str.upper()
    )

    df["po_no"] = (
        df["po_no"]
        .astype(str)
        .str.strip()
    )

    df["qty_received"] = (
        pd.to_numeric(
            df["qty_received"],
            errors="coerce"
        )
        .fillna(0)
    )

    df = df.drop_duplicates()

    return df