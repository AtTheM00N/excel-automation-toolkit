# Excel Automation Toolkit

Merges multiple messy Excel exports into one clean file, and generates a report on what changed automatically.

## Why I built this

Combining a handful of Excel exports and cleaning them by hand (duplicates, blank rows, inconsistent formatting) is the kind of repetitive task that eats an afternoon for no good reason. This automates the whole pipeline: merge → clean → report.

## Features

- Merges any number of `.xlsx` files in a folder into one DataFrame
- Removes exact duplicate rows and fully blank rows
- Fills missing values
- Standardizes inconsistent date formats within the same column
- Strips stray leading/trailing whitespace from text fields
- Generates an HTML and PDF summary report (rows before/after, duplicates removed, execution time)

## Project structure

```
project/
├── automation/
│   ├── merge.py      # find + combine excel files into one dataframe
│   ├── clean.py      # dataframe cleaning functions
│   └── report.py     # summary stats + report generation
├── data/
│   ├── input/         # drop your raw .xlsx files here
│   └── output/        # merged.xlsx, cleaned.xlsx, report.html/pdf land here
├── screenshots/
├── main.py            # ties the pipeline together
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone <repo-url>
cd <repo-name>
pip install -r requirements.txt
```

## Usage

1. Drop your `.xlsx` files into `data/input/`
2. Run:
   ```bash
   python main.py
   ```
3. Check `data/output/` for:
   - `merged.xlsx` — raw merge of all input files, before cleaning
   - `cleaned.xlsx` — deduplicated, whitespace-stripped, date-standardized version
   - `report.html` / `report.pdf` — summary of what changed

## Example output

```
Reading: region_east.xlsx
Reading: region_west.xlsx
Merged 2 files -> 8 rows
Merged and cleaned 8 -> 5 rows (2 duplicates removed).
Saved as: data/output/cleaned.xlsx
```

## What I'd add next

- Column validation across input files with mismatched schemas
- CLI arguments instead of hardcoded input/output paths
- Unit tests for the cleaning functions