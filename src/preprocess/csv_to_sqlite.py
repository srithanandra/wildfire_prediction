import sqlite3
from pathlib import Path

import pandas as pd


def csv_to_sqlite(csv_path: Path) -> Path:
    """Convert one CSV into a SQLite DB with one table."""
    table_name = csv_path.stem.replace("-", "_")
    db_path = csv_path.with_suffix(".db")

    conn = sqlite3.connect(db_path)
    try:
        # Stream large CSV files in chunks to avoid memory spikes.
        first_chunk = True
        for chunk in pd.read_csv(csv_path, chunksize=100_000):
            chunk.to_sql(
                table_name,
                conn,
                if_exists="replace" if first_chunk else "append",
                index=False,
            )
            first_chunk = False
    finally:
        conn.close()

    return db_path


def main() -> None:
    project_root = Path(__file__).resolve().parents[2]
    data_dir = project_root / "data"
    csv_files = sorted(data_dir.rglob("*.csv"))

    if not csv_files:
        print("No CSV files found under data/.")
        return

    for csv_path in csv_files:
        db_path = csv_to_sqlite(csv_path)
        print(f"Converted {csv_path} -> {db_path}")


if __name__ == "__main__":
    main()
