from collections import defaultdict

from pandas import read_excel

from settings import Settings


def extract_xlsx_data(file_path: str, settings: Settings) -> defaultdict:
    """Return data from excel file."""

    wines = read_excel(
        io=file_path,
        names=settings.DEFAULT_NAMES,
        na_values=(None for _ in settings.DEFAULT_NAMES),
        keep_default_na=False
    ).to_dict(orient="records")

    categorized_wines = defaultdict(list)
    for wine in wines:
        categorized_wines[wine.get("category")].append(wine)
    return categorized_wines
