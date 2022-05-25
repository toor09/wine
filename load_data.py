from collections import defaultdict
from pprint import pprint

from pandas import read_excel

DEFAULT_NAMES = ("category", "title", "sort", "price", "image", "promotion",)
DEFAULT_NA_VALUES = tuple(None for name in DEFAULT_NAMES)


def extract_data(
        filename: str,
        names: tuple = DEFAULT_NAMES,
        na_values: tuple = DEFAULT_NA_VALUES
) -> defaultdict:
    """Return data from excel file."""

    records = read_excel(
        io=filename,
        names=names,
        na_values=na_values,
        keep_default_na=False
    ).to_dict(orient="records")

    data = defaultdict(list)
    for record in records:
        data[record.get("category")].append(record)

    return data


if __name__ == "__main__":
    pprint(extract_data(filename="wines.xlsx"))
