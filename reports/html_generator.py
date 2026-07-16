from pathlib import Path
from datetime import datetime

from reports.template_engine import TemplateEngine


class HTMLGenerator:

    @staticmethod
    def generate(profile, ai_report, charts):

        output_dir = Path("reports/output")
        output_dir.mkdir(parents=True, exist_ok=True)

        html = TemplateEngine.render(
            "report.html",
            {
                "generated": datetime.now().strftime("%d %B %Y %H:%M"),

                "rows": profile["rows"],
                "columns": profile["columns"],
                "duplicates": profile["duplicates"],
                "memory": profile["memory"],

                "ai_report": ai_report,

                "charts": charts
            }
        )

        output_path = output_dir / "Analysis_Report.html"

        output_path.write_text(
            html,
            encoding="utf-8"
        )

        return str(output_path)