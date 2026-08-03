from automation.merge import merge_excel_files


INPUT_FOLDER = "data/input"
OUTPUT_FILE = "data/output/merged.xlsx"


def main():
    merge_excel_files(INPUT_FOLDER, OUTPUT_FILE)


if __name__ == "__main__":
    main()