from datetime import datetime as dt
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

from filters import format_year
from load_data import extract_data

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)
env.filters["format_year"] = format_year

template = env.get_template('template.html')

rendered_page = template.render(
    age=dt.now().year - 1920,
    root_path_img="images/",
    wines=extract_data(filename="wines.xlsx")
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
