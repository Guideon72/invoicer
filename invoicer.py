# pandas needs openpyxl in order to read excel files; be sure to install
import pandas as pd
from fpdf import FPDF
from pathlib import Path

# Read all files in directory into a Python list
base_path = Path(Path.cwd() / "data" / "invoices").glob("*.xlsx")
invoices = [f for f in base_path if f.is_file()]

# Convert each file to a Pandas dataframe
for invoice in invoices:
    df = pd.read_excel(invoice, sheet_name="Sheet 1")
    print(df)


def main():
    pass


if __name__ == "__main__":
    main()
