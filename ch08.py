import marimo

__generated_with = "0.23.11"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import math
    import numpy as np 
    import polars as pl
    import plotnine as p9

    return math, np, p9, pl


@app.cell
def _(math, np):
    print(f"{math.pi=}")
    rng = np.random.default_rng(1729)
    print(f"{rng.random()=}")
    return


@app.cell
def _(pl):
    penguins = pl.read_csv('data/penguins.csv', null_values="NA").select(
        "species",
        "island",
        "sex",
        "year",
        mass=pl.col("body_mass_g") / 1000,
    )
    return (penguins,)


@app.cell
def _(penguins, pl):
    penguins.with_columns(
        mass_sqrt=pl.col("mass").sqrt(),
        mass_exp=pl.col("mass").exp(),
    )
    return


@app.cell
def _(penguins, pl):
    penguins.select(pl.col("mass").mean(), pl.col("island").first())
    return


@app.cell
def _(penguins, pl):
    penguins.select(pl.col('island').unique())
    return


@app.cell
def _(penguins, pl):
    penguins.select(
        pl.col("species")
        .unique()
        .repeat_by(3000)
        .explode()
        .extend_constant("Saiyan", n=1)
    )
    return


@app.cell
def _(math, pl):
    (
        pl.DataFrame(
    {"x": [-6.0, -0.5, 0.0, 0.5, math.pi, 9.9, 9.99, 9.999]})
        .with_columns(
            ceil=pl.col("x").ceil(),
            clip=pl.col("x").clip(-1, 1),
            cut=pl.col("x").cut([-1, 1], labels=['bad', 'neutral', 'good']),
            floor=pl.col("x").floor(),
            qcut=pl.col("x").qcut([0.5], labels=["below median", "above median"]),
            round0=pl.col("x").round(2),
        )
    )
    return


@app.cell
def _(math, pl):
    (
        pl.DataFrame(
    {"x": [-1.0, 0.0, 1.0, None, None, 3.0, 4.0, math.nan, 6.0]}
    )
        .with_columns(
            interp1=pl.col("x").interpolate(method="linear"),
            shift3=pl.col("x").shift(3)
        )
    )
    return


@app.cell
def _(pl):
    (
        pl.DataFrame({"x": ["A", "C", "D", "C"]})
        .with_columns(
            is_duplicated=pl.col("x").is_duplicated()
        )
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Operations That Compute Rolling Statistics
    """)
    return


@app.cell
def _(pl):
    stock = (
        pl.read_csv("data/stock/nvda/2023.csv", try_parse_dates=True)
        .select('date', 'close')
        .with_columns(
            ewm_mean=pl.col("close").ewm_mean(com=7, ignore_nulls=True),
            rolling_mean=pl.col("close").rolling_mean(window_size=7),
            rolling_min=pl.col("close").rolling_min(window_size=7),
        )
    )

    stock
    return (stock,)


@app.cell
def _(p9, stock):
    plot_nvda = (
        p9.ggplot(stock.unpivot(index="date"), p9.aes("date", "value", color="variable"))
        + p9.geom_line(size=1)
        + p9.labs(x="Date", y="Value", color="Method")
        + p9.theme_tufte(base_family="Guardian Sans", base_size=14)
        + p9.theme(figure_size=(8, 5), dpi=200)
    )
    return (plot_nvda,)


@app.cell
def _(plot_nvda):
    plot_nvda.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Operations that Sort
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
