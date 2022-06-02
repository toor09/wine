from collections import defaultdict
from datetime import datetime as dt
from http.server import HTTPServer, SimpleHTTPRequestHandler

import click
from jinja2 import Environment, FileSystemLoader, select_autoescape

from filters import format_year
from load_data import extract_xlsx_data
from settings import Settings


def render_page(categorized_wines: defaultdict, settings: Settings) -> None:
    """Render page with template variables."""

    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(["html", "xml"])
    )
    env.filters["format_year"] = format_year

    template = env.get_template("template.html")

    rendered_page = template.render(
        age=dt.now().year - settings.FOUNDATION_YEAR,
        root_path_img=settings.ROOT_PATH_IMG,
        categorized_wines=categorized_wines
    )

    with open("index.html", "w", encoding="utf8") as file:
        file.write(rendered_page)


def run_server(port: int) -> None:
    """Run HTTP server."""

    server = HTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler)
    server.serve_forever()


@click.command()
@click.option(
    "-f", "--file-path",
    default="wines.xlsx",
    help="Path to excel datafile"
)
def main(file_path: str) -> None:
    """
    Load data from local excel file and render page.
    After that just run HTTP server.
    """
    settings = Settings()
    categorized_wines = extract_xlsx_data(
        file_path=file_path, settings=settings
    )
    render_page(categorized_wines=categorized_wines, settings=settings)
    run_server(settings.PORT)


if __name__ == "__main__":
    main()
