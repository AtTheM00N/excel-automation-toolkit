import pandas as pd


def remove_empty_rows(df):
    before = len(df)
    df = df.dropna(how="all").reset_index(drop=True)
    removed = before - len(df)
    return df, removed


def remove_duplicates(df):
    before = len(df)
    df = df.drop_duplicates().reset_index(drop=True)
    removed = before - len(df)
    return df, removed


def fill_missing_values(df, strategy="blank"):
    if strategy == "blank":
        return df.fillna("")
    if strategy == "zero":
        return df.fillna(0)
    if strategy == "mean":
        numeric_cols = df.select_dtypes(include="number").columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        return df
    raise ValueError(f"unknown strategy: {strategy}")


def standardize_dates(df, date_columns, fmt="%Y-%m-%d"):
    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce").dt.strftime(fmt)
    return df


def rename_columns(df, rename_map):
    return df.rename(columns=rename_map)


def remove_whitespace(df):
    text_cols = df.select_dtypes(include="object").columns
    for col in text_cols:
        df[col] = df[col].where(df[col].isna(), df[col].astype(str).str.strip())
    return df