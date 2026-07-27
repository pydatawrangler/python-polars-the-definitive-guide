import marimo

__generated_with = "0.23.11"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    import polars as pl

    return (pl,)


@app.cell
def _(pl):
    fruit = pl.read_csv("data/fruit.csv")
    fruit
    return (fruit,)


@app.cell
def _(fruit, pl):
    fruit.select(
        pl.col("name"),
        pl.col("^.*or.*$"),
        pl.col("weight")/1000,
        "is_round",
    )
    return


@app.cell
def _(fruit):
    new_df = fruit.with_columns(
        (pl.col("weight") / 1000).alias("weight_kg"),
        pl.when(pl.col("is_round"))
            .then("round")
            .otherwise("not round")
            .alias("shape")
    )
    new_df
    return


if __name__ == "__main__":
    app.run()
