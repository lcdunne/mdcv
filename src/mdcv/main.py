import os
import urllib.parse

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader

CONFIG_FILENAME = "_config.yaml"
DEFAULT_TEMPLATES = os.path.join(os.path.dirname(__file__), "templates")

COLOURS = {
    "context": "#ECEFF4",  # website background
    "background": "#FFFFF",  # text content background
    "foreground": "#434C5E",  # text
    "highlight": "#5E81AC",
}


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
        templates_dir = DEFAULT_TEMPLATES
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template(template_file)
    return template.render(content=html_content, config=config)


def write_html_to_file(output_file, html_content):
    with open(output_file, "w") as f:
        f.write(html_content)


def markdown_to_html(
    markdown_file: str,
    output_file: str | None = None,
    templates_dir: str | None = None,
    config: dict | None = None,
):
    if output_file is None:
        output_file = os.path.splitext(markdown_file)[0] + ".html"

    if config is None:
        config = {}

    template_name = config.setdefault("template", "raw")

    if "colours" not in config:
        config["colours"] = COLOURS

    if "fontName" in config and "fontUrl" not in config:
        _, config["fontUrl"] = get_google_font_url(config["fontName"])

    template_file = f"{template_name}.html"
    print(template_file)
    md = read_markdown_file(markdown_file)
    html = convert_markdown_to_html(md)
    rendered_html = render_html_template(template_file, html, templates_dir, config)
    write_html_to_file(output_file, rendered_html)
    print(f"Success: {output_file}")


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


def load_config(file_path: str = CONFIG_FILENAME) -> dict:
    """Load a YAML file.

    Arguments
    ---------
    file_path : str
        The path to the YAML file to be loaded. The default is `_config.yaml`.

    Returns
    -------
    dict
        A dictionary representation of the YAML file content.
    """
    _, ext = os.path.splitext(file_path)
    if ext not in [".yml", ".yaml"]:
        raise ValueError(f"Invalid config file type - must be yaml but got {ext}")

    with open(file_path, "r") as f:
        return yaml.safe_load(f)


if __name__ == "__main__":
    config = load_config()
    markdown_to_html("cv.md", config=config)
