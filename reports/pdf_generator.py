from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)

class PDFGenerator:

    @staticmethod
    def generate(profile, ai_report, charts, filename):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        story = []

        # ==========================
        # Title
        # ==========================

        story.append(
            Paragraph(
                "Autonomous Data Science Co-Pilot",
                styles["Title"]
            )
        )

        story.append(
            Paragraph(
                "AI Generated Dataset Report",
                styles["Heading2"]
            )
        )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph(
                f"<b>Generated On:</b> {datetime.now().strftime('%d %B %Y %H:%M')}",
                styles["Normal"]
            )
        )

        story.append(Spacer(1, 30))

        # ==========================
        # Executive Summary
        # ==========================

        story.append(
            Paragraph(
                "Executive Summary",
                styles["Heading1"]
            )
        )

        story.append(
            Paragraph(
                f"""
                This report provides an automated analysis of the uploaded dataset.
                The dataset contains <b>{profile['rows']}</b> records and
                <b>{profile['columns']}</b> features.
                The report includes data quality assessment, AI-generated insights,
                and recommendations for machine learning.
                """,
                styles["BodyText"]
            )
        )

        story.append(Spacer(1, 20))

        # ==========================
        # Dataset Summary
        # ==========================

        story.append(
            Paragraph(
                "Dataset Summary",
                styles["Heading1"]
            )
        )

        summary_data = [
            ["Metric", "Value"],
            ["Rows", str(profile["rows"])],
            ["Columns", str(profile["columns"])],
            ["Duplicate Rows", str(profile["duplicates"])],
            ["Memory Usage", str(profile["memory"])],
        ]

        table = Table(summary_data, colWidths=[250, 150])

        table.setStyle(
            TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 11),

                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

                ("GRID", (0, 0), (-1, -1), 1, colors.black),

                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ])
        )

        story.append(table)

        story.append(Spacer(1, 25))

        # ==========================
        # AI Insights
        # ==========================

        story.append(
            Paragraph(
                "AI Insights",
                styles["Heading1"]
            )
        )

        for line in ai_report.split("\n"):

            if line.strip():

                story.append(
                    Paragraph(
                        line,
                        styles["BodyText"]
                    )
                )

        story.append(Spacer(1, 20))

        # ==========================
        # Visualizations
        # ==========================

        story.append(Spacer(1, 20))

        story.append(
            Paragraph(
                "Visualizations",
                styles["Heading1"]
            )
        )

        story.append(Spacer(1, 10))

        for title, image_path in charts:
            story.append(
                Paragraph(
                    title,
                    styles["Heading2"]
                )
            )

            story.append(
                Image(
                    image_path,
                    width=420,
                    height=250
                )
            )

            story.append(
                Spacer(1, 20)
            )

        # ==========================
        # ML Recommendation
        # ==========================

        story.append(
            Paragraph(
                "Machine Learning Recommendation",
                styles["Heading1"]
            )
        )

        story.append(
            Paragraph(
                """
                Based on the AI analysis, select the appropriate machine learning
                approach after performing the recommended preprocessing steps.
                Evaluate multiple models using cross-validation before finalizing
                the best-performing model.
                """,
                styles["BodyText"]
            )
        )

        story.append(Spacer(1, 30))

        # ==========================
        # Footer
        # ==========================

        story.append(
            Paragraph(
                "<i>Generated using Autonomous Data Science Co-Pilot</i>",
                styles["Italic"]
            )
        )

        doc.build(story)