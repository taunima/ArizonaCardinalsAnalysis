import polars as pl

df = pl.DataFrame({
    "season": [2007, 2008, 2009, 2010, 2011],
    "wins": [8, 9, 10, 5, 8],
    "losses": [8, 7, 6, 11, 8],
    "era": ["Arizona", "Arizona", "Arizona", "Arizona", "Arizona"]
})

print(df)

print(df.filter(pl.col("wins") >= pl.col("losses")))