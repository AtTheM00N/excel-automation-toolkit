import time


def execution_time(start_time):
    return round(time.time() - start_time, 2)


def generate_summary(rows_before, rows_after, duplicates_removed, empty_rows_removed, start_time):
    return {
        "rows_before": rows_before,
        "rows_after": rows_after,
        "duplicates_removed": duplicates_removed,
        "empty_rows_removed": empty_rows_removed,
        "execution_time": execution_time(start_time),
    }


def export_html_report(summary, output_path):
    html = f"""<html>
<head><title>Excel Automation Report</title></head>
<body style="font-family: sans-serif;">
<h1>Excel Automation Report</h1>
<ul>
<li>Rows before cleaning: {summary['rows_before']}</li>
<li>Empty rows removed: {summary['empty_rows_removed']}</li>
<li>Duplicate rows removed: {summary['duplicates_removed']}</li>
<li>Rows after cleaning: {summary['rows_after']}</li>
<li>Execution time: {summary['execution_time']}s</li>
</ul>
</body>
</html>"""
    with open(output_path, "w") as f:
        f.write(html)


def export_pdf_report(summary, output_path):
    # pip install fpdf2
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 12, "Excel Automation Report", ln=True)
    pdf.set_font("Helvetica", "", 11)

    lines = [
        f"Rows before cleaning: {summary['rows_before']}",
        f"Empty rows removed: {summary['empty_rows_removed']}",
        f"Duplicate rows removed: {summary['duplicates_removed']}",
        f"Rows after cleaning: {summary['rows_after']}",
        f"Execution time: {summary['execution_time']}s",
    ]
    for line in lines:
        pdf.cell(0, 9, line, ln=True)

    pdf.output(output_path)