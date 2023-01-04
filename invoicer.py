# pandas needs openpyxl in order to read excel files; be sure to install
import pandas as pd
from fpdf import FPDF
from pathlib import Path


def mk_pdf(data, f_name, f_date):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice #: {f_name}")
    pdf.ln()
    pdf.cell(w=50, h=8, txt=f"Invoice date: {f_date}")
    pdf.output(f"data/output/{data}.pdf")


def convert_invoices():
    # Read all files in directory into a Python list
    base_path = Path(Path.cwd() / "data" / "invoices").glob("*.xlsx")
    invoices = [f for f in base_path if f.is_file()]
    for invoice in invoices:
        iv_name, iv_date = invoice.stem.split("-")
        df = pd.read_excel(invoice, sheet_name="Sheet 1")
        mk_pdf(invoice.name, iv_name, iv_date)


def main():
    convert_invoices()


if __name__ == "__main__":
    main()
