# src/preprocess.py
import pandas as pd
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "spotify_tracks.csv"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)


def try_read_csv(path, encodings=None):
    if encodings is None:
        encodings = ["utf-8", "utf-8-sig", "utf-16", "cp1252", "latin1"]
    last_err = None
    for enc in encodings:
        try:
            print(f"[INFO] Trying encoding: {enc}")
            # engine='python' can be more forgiving for some encodings; keep default C engine if possible
            df = pd.read_csv(path, encoding=enc, low_memory=False)
            print(f"[✔] Successfully read CSV with encoding: {enc}")
            return df, enc
        except Exception as e:
            last_err = e
            # continue trying
    # final fallback: try with errors='replace' using python engine
    try:
        print("[INFO] Trying fallback read with encoding='utf-8' and errors='replace' (python engine)")
        df = pd.read_csv(path, encoding="utf-8", engine="python", error_bad_lines=False)  # error_bad_lines ignored in pandas 1.3+, may warn
        return df, "utf-8 (errors=replace, python engine)"
    except Exception as e:
        print("[ERROR] All attempts to read CSV failed. Last error:")
        print(last_err)
        raise last_err


def load_data():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")
    df, used_encoding = try_read_csv(DATA_PATH)
    print(f"[INFO] Using encoding: {used_encoding}")
    return df


def clean_data(df):
    # normalize columns
    df.columns = [c.strip() for c in df.columns]

    # unify artist column name
    if "artists" in df.columns and "artist_name" not in df.columns:
        df = df.rename(columns={"artists": "artist_name"})

    # parse release_date -> year
    if "release_date" in df.columns:
        df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
        df["year"] = df["release_date"].dt.year

    # duration in minutes
    if "duration_ms" in df.columns:
        df["duration_min"] = df["duration_ms"] / 60000.0

    # drop duplicates
    subset_cols = [c for c in ["track_name", "artist_name", "year"] if c in df.columns]
    if subset_cols:
        df = df.drop_duplicates(subset=subset_cols)

    return df


def save_clean(df):
    out_path = OUTPUT_DIR / "spotify_clean.csv"
    df.to_csv(out_path, index=False)
    print(f"[✔] Cleaned data saved to: {out_path}")


def main():
    print("[INFO] Preprocessing started")
    df = load_data()
    df = clean_data(df)
    save_clean(df)
    print(f"[INFO] Preprocessing finished. Rows: {len(df)}")
    return df


if __name__ == "__main__":
    main()
