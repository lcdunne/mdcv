import os
import urllib.parse

import markdown
from jinja2 import Environment, FileSystemLoader


def read_markdown_file(markdown_file):
    with open(markdown_file, "r") as f:
        md = f.read()
    return md


def convert_markdown_to_html(markdown_content):
    return markdown.markdown(markdown_content)


def render_html_template(
    template_file, html_content, templates_dir=None, config: dict | None = None
):
    if templates_dir is None:
        # Set the default templates directory to src/mdcv/templates
        templates_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template(template_file)
    return template.render(content=html_content, config=config)


def write_html_to_file(output_file, html_content):
    with open(output_file, "w") as f:
        f.write(html_content)


def markdown_to_html(
    markdown_file: str,
    template_file: str,
    output_file: str | None = None,
    templates_dir: str | None = None,
    config: dict | None = None,
):
    if output_file is None:
        output_file = os.path.splitext(markdown_file)[0] + ".html"
    md = read_markdown_file(markdown_file)
    html = convert_markdown_to_html(md)
    rendered_html = render_html_template(template_file, html, templates_dir, config)
    write_html_to_file(output_file, rendered_html)
    print("Success")


# templates = {0: "template.html", 1: "minimal.html"}


def get_google_font_url(font_name: str) -> tuple[str, str]:
    """Fetch the Google Font given its name.

    Arguments
    ---------
    font_name : str
        The name of the font. Note that because this uses the Google Fonts API, this
        argument is case sensitive.

    Returns
    -------
    tuple (str, str)
        A tuple containing the font name and the URL to the Google Font CSS stylesheet.
    """
    base_url = "https://fonts.googleapis.com/css2?family="
    url_encoded_font_name = urllib.parse.quote_plus(font_name)
    font_url = f"{base_url}{url_encoded_font_name}"
    return font_name, font_url

