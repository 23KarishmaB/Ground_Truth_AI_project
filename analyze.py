import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def load_clean():
    path = OUTPUT_DIR / "spotify_clean.csv"
    if not path.exists():
        raise FileNotFoundError("Clean CSV not found. Run preprocess first.")
    return pd.read_csv(path)


def top_artists(df, n=10):
    col = "artist_name" if "artist_name" in df.columns else ("artists" if "artists" in df.columns else None)
    if not col:
        return None
    top = df[col].value_counts().head(n)
    plt.figure(figsize=(8, 5))
    sns.barplot(x=top.values, y=top.index)
    plt.title("Top Artists by Track Count")
    plt.tight_layout()
    out = OUTPUT_DIR / "top_artists.png"
    plt.savefig(out)
    plt.close()
    return str(out)


def popularity_trend(df):
    if "popularity" not in df.columns or "year" not in df.columns:
        return None
    agg = df.groupby("year")["popularity"].mean().dropna()
    plt.figure(figsize=(10, 4))
    plt.plot(agg.index, agg.values, marker="o")
    plt.title("Average Popularity by Year")
    plt.xlabel("Year")
    plt.ylabel("Avg Popularity")
    plt.tight_layout()
    out = OUTPUT_DIR / "popularity_trend.png"
    plt.savefig(out)
    plt.close()
    return str(out)


def feature_corr(df):
    candidates = ['danceability','energy','loudness','speechiness','acousticness',
                  'instrumentalness','liveness','valence','tempo','popularity']
    cols = [c for c in candidates if c in df.columns]
    if len(cols) < 2:
        return None
    numeric = df[cols].select_dtypes(include=['float','int'])
    corr = numeric.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title("Feature Correlation")
    plt.tight_layout()
    out = OUTPUT_DIR / "feature_corr.png"
    plt.savefig(out)
    plt.close()
    return str(out)


def summarize(df):
    return {
        "total_tracks": int(len(df)),
        "unique_artists": int(df["artist_name"].nunique()) if "artist_name" in df.columns else "N/A",
        "years_covered": f"{int(df['year'].min())} - {int(df['year'].max())}" if "year" in df.columns else "N/A",
        "avg_popularity": float(df["popularity"].mean()) if "popularity" in df.columns else "N/A",
        "avg_duration_min": float(df["duration_min"].mean()) if "duration_min" in df.columns else "N/A"
    }


def main():
    print("[INFO] Analysis started")
    df = load_clean()
    imgs = {
        "top_artists": top_artists(df),
        "popularity_trend": popularity_trend(df),
        "feature_corr": feature_corr(df)
    }
    metrics = summarize(df)
    print("[INFO] Analysis complete")
    return metrics, imgs


if __name__ == "__main__":
    main()
