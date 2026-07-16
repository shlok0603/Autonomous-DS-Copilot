from reports.html_generator import HTMLGenerator
from reports.pdf_generator import PDFGenerator

from utils.charts import ChartGenerator
from utils.chart_exporter import ChartExporter


class ReportGenerator:

    @staticmethod
    def generate(df, profile, ai_report):

        charts = []

        for title, fig in ChartGenerator.generate_all(df):

            filename = (
                title.lower()
                .replace(" ", "_")
                .replace("-", "")
                + ".png"
            )

            image_path = ChartExporter.save(
                fig,
                filename
            )

            charts.append(
                {
                    "title": title,
                    "path": image_path
                }
            )

        html_file = HTMLGenerator.generate(
            profile,
            ai_report,
            charts
        )

        pdf_file = PDFGenerator.generate(
            profile,
            ai_report,
            charts,
            "reports/output/AI_Report.pdf"
        )

        return html_file, pdf_file