from pathlib import Path
import pandas as pd


def get_excel_files(input_folder):
    return list(Path(input_folder).glob("*.xlsx"))


def merge_excel_files(input_folder):
    excel_files = get_excel_files(input_folder)

    if not excel_files:
        raise FileNotFoundError(f"No Excel files found in {input_folder}")

    dataframes = []
    for file in excel_files:
        print(f"Reading: {file.name}")
        dataframes.append(pd.read_excel(file))

    merged_df = pd.concat(dataframes, ignore_index=True)
    print(f"Merged {len(excel_files)} files -> {len(merged_df)} rows")

    return merged_df