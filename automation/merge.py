from pathlib import Path
import pandas as pd


def merge_excel_files(input_folder, output_file):
    # Find all Excel files in the input folder
    excel_files = list(Path(input_folder).glob("*.xlsx"))

    # Check if any files exist
    if not excel_files:
        print("❌ No Excel files found.")
        return

    # Read each Excel file into a DataFrame
    dataframes = []
    print(excel_files)
    

    for file in excel_files:
        print(f"Reading: {file.name}")
        df = pd.read_excel(file)
        print(df)
        print("=" * 50)
        dataframes.append(df)

    # Merge all DataFrames
    merged_df = pd.concat(dataframes, ignore_index=True)

    # Save merged DataFrame
    print("\nMerged DataFrame:")
    print(merged_df)
    merged_df.to_excel(output_file, index=False)

    print(f"\n✅ Successfully merged {len(excel_files)} files.")
    print(f"📄 Output saved to: {output_file}")