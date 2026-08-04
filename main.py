import os
import time

from automation.merge import merge_excel_files
from automation.clean import remove_empty_rows, remove_duplicates, fill_missing_values, remove_whitespace
from automation.report import generate_summary, export_html_report, export_pdf_report

INPUT_FOLDER = "data/input"
OUTPUT_FOLDER = "data/output"


def main():
    start_time = time.time()
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    merged_df = merge_excel_files(INPUT_FOLDER)
    merged_df.to_excel(f"{OUTPUT_FOLDER}/merged.xlsx", index=False)
    rows_before = len(merged_df)

    df, empty_removed = remove_empty_rows(merged_df)
    df, dup_removed = remove_duplicates(df)
    df = fill_missing_values(df)
    df = remove_whitespace(df)
    rows_after = len(df)

    df.to_excel(f"{OUTPUT_FOLDER}/cleaned.xlsx", index=False)

    summary = generate_summary(rows_before, rows_after, dup_removed, empty_removed, start_time)
    export_html_report(summary, f"{OUTPUT_FOLDER}/report.html")
    export_pdf_report(summary, f"{OUTPUT_FOLDER}/report.pdf")

    print(f"Merged and cleaned {rows_before} -> {rows_after} rows ({dup_removed} duplicates removed).")
    print(f"Saved as: {OUTPUT_FOLDER}/cleaned.xlsx")


if __name__ == "__main__":
    main()