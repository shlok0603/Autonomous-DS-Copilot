from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from datetime import datetime


class PDFGenerator:

    @staticmethod
    def generate(profile, ai_report, filename):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(
                "<b>Autonomous Data Science Co-Pilot</b>",
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
                f"Generated: {datetime.now()}",
                styles["Normal"]
            )
        )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph(
                "<b>Dataset Summary</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                f"Rows: {profile['rows']}",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                f"Columns: {profile['columns']}",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                f"Duplicate Rows: {profile['duplicates']}",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                f"Memory Usage: {profile['memory']} MB",
                styles["Normal"]
            )
        )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph(
                "<b>AI Analysis</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                ai_report.replace("\n", "<br/>"),
                styles["BodyText"]
            )
        )

        doc.build(story)