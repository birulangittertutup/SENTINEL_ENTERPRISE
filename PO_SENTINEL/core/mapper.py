"""
PO Sentinel Enterprise
core/mapper.py

Column mapping between client Excel files and internal system fields.
DO NOT CHANGE INTERNAL FIELD NAMES.
"""

PO_COLUMN_MAP = {
    "No. PO": "po_no",
    "Tgl. PO": "po_date",
    "No. Vendor": "vendor_code",
    "Vendor": "vendor_name",
    "Product": "item_code",
    "Qty. Order": "qty_order",
    "ToP": "top",
    "Purchaser": "purchaser",
    "Status": "po_status",
    "UOM": "uom",
}

GR_COLUMN_MAP = {
    "No. PO": "po_no",
    "No. TTB": "gr_no",
    "Tgl. TTB": "gr_date",
    "Site": "site",
    "No. Supplier": "supplier_code",
    "Nama Supplier": "supplier_name",
    "No. Item": "item_code",
    "Nama Item": "item_name",
    "Shipment Method": "shipment_method",
    "UOM": "uom",
    "Qty. Received": "qty_received",
    "Qty. SJ Vendor": "qty_sj",
}