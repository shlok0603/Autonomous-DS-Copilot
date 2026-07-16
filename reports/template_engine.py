from pathlib import Path

from jinja2 import Environment, FileSystemLoader


class TemplateEngine:

    @staticmethod
    def render(template_name, context):

        template_dir = Path("reports/templates")

        env = Environment(
            loader=FileSystemLoader(template_dir)
        )

        template = env.get_template(template_name)

        return template.render(**context)