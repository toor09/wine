from collections import defaultdict

from pandas import read_excel

DEFAULT_NAMES = ("category", "title", "sort", "price", "image", "promotion",)
DEFAULT_NA_VALUES = tuple(None for name in DEFAULT_NAMES)


def extract_xlsx_data(
        file_path: str,
        names: tuple = DEFAULT_NAMES,
        na_values: tuple = DEFAULT_NA_VALUES
) -> defaultdict:
    """Return data from excel file."""

    wines = read_excel(
        io=file_path,
        names=names,
        na_values=na_values,
        keep_default_na=False
    ).to_dict(orient="records")

    wines_collection = defaultdict(list)
    for wine in wines:
        wines_collection[wine.get("category")].append(wine)
    return wines_collection
