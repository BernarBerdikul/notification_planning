from typing import Any

from jinja2 import Template

__all__ = ('render_template',)


def render_template(html_template: str, context: dict[str, Any]) -> str:
    j2_template = Template(html_template)
    return j2_template.render(context)
