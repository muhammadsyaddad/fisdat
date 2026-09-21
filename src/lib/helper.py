from pathlib import Path
import markdown
from weasyprint import HTML


def convert_md_to_pdf(md_filename: str, pdf_filename: str):
    # Baca teks Markdown
    with open(md_filename, "r", encoding="utf-8") as f:
        md_text = f.read()

    html_body = markdown.markdown(md_text, extensions=["tables"])

    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{ font-family: sans-serif; font-size: 11pt; line-height: 1.5; margin: 30px; }}
            table {{ border-collapse: collapse; width: 100%; margin: 16px 0; }}
            th, td {{ border: 1px solid #ddd; padding: 6px 10px; text-align: center; }}
            th {{ background-color: #f2f2f2; }}
            h1, h2 {{ color: #1a365d; }}
        </style>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """

    # Render ke PDF
    HTML(string=styled_html).write_pdf(pdf_filename)
    print(f"PDF berhasil dibuat: {pdf_filename}")



# Naik 2 tingkat dari helper.py (src/lib -> src -> root)
ROOT_DIR = Path(__file__).resolve().parents[2]

md_path = ROOT_DIR / "laporan_analisis_kisi.md"
pdf_path = ROOT_DIR / "laporan_analisis_kisi.pdf"

convert_md_to_pdf(str(md_path), str(pdf_path))
