import os
import html
from datetime import datetime
from reportlab.lib.units import inch

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    PageBreak
)


def add_page_number(canvas, doc):
    canvas.saveState()

    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.grey)

    canvas.drawRightString(
        520,
        20,
        f"Page {doc.page}"
    )

    canvas.restoreState()


class PDFGenerator:

    @staticmethod
    def generate(profile, ai_report, charts, filename):

        doc = SimpleDocTemplate(
            filename,
            rightMargin=40,
            leftMargin=40,
            topMargin=40,
            bottomMargin=40
        )

        styles = getSampleStyleSheet()

        # -----------------------------
        # Custom Styles
        # -----------------------------

        styles.add(
            ParagraphStyle(
                name="CoverTitle",
                fontSize=28,
                alignment=TA_CENTER,
                spaceAfter=20,
                textColor=colors.darkblue,
                leading=34
            )
        )

        styles.add(
            ParagraphStyle(
                name="SectionTitle",
                fontSize=18,
                spaceAfter=12,
                textColor=colors.darkblue,
                leading=22
            )
        )

        styles.add(
            ParagraphStyle(
                name="ChartTitle",
                fontSize=14,
                textColor=colors.darkblue,
                spaceAfter=8,
                leading=18
            )
        )

        styles.add(
            ParagraphStyle(
                name="Body",
                fontSize=11,
                leading=18
            )
        )
        styles.add(
            ParagraphStyle(
                name="AIHeading",
                parent=styles["Heading2"],
                fontSize=16,
                textColor=colors.darkblue,
                spaceBefore=12,
                spaceAfter=8
            )
        )

        styles.add(
            ParagraphStyle(
                name="AISubHeading",
                parent=styles["Heading3"],
                fontSize=13,
                textColor=colors.darkred,
                spaceBefore=8,
                spaceAfter=5
            )
        )

        styles.add(
            ParagraphStyle(
                name="Bullet",
                parent=styles["Body"],
                leftIndent=18,
                bulletIndent=8,
                spaceAfter=4
            )
        )

        story = []

        # =================================================
        # COVER PAGE
        # =================================================

        logo_path = "reports/assets/images/logo.png"

        if os.path.exists(logo_path):
            story.append(
                Image(
                    logo_path,
                    width=2.2 * inch,
                    height=2.2 * inch
                )
            )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph(
                "Autonomous Data Science Co-Pilot",
                styles["CoverTitle"]
            )
        )

        story.append(
            Paragraph(
                "<font size=20><b>Enterprise Dataset Analysis Report</b></font>",
                styles["Body"]
            )
        )

        story.append(Spacer(1, 25))

        story.append(
            Paragraph(
                f"<b>Generated:</b> {datetime.now().strftime('%d %B %Y %H:%M')}",
                styles["Body"]
            )
        )

        story.append(
            Paragraph(
                "<b>Powered By:</b> Gemini AI • Plotly • Streamlit",
                styles["Body"]
            )
        )

        story.append(Spacer(1, 60))

        story.append(
            Paragraph(
                """
                This report has been automatically generated using the
                Autonomous Data Science Co-Pilot.

                The report includes:

                • Dataset Profiling

                • Data Quality Assessment

                • AI Generated Insights

                • Statistical Summary

                • Business Recommendations

                • Machine Learning Suggestions

                • Interactive Visualizations
                """,
                styles["Body"]
            )
        )

        story.append(PageBreak())

        # =================================================
        # DATASET SUMMARY
        # =================================================

        story.append(
            Paragraph(
                "Executive Dashboard",
                styles["SectionTitle"]
            )
        )


        story.append(Spacer(1, 10))

        summary_data = [

            ["Metric", "Value"],

            ["Dataset Health Score", f"{profile['health_score']} / 100"],

            ["Rows", profile["rows"]],

            ["Columns", profile["columns"]],

            ["Numeric Columns", profile["numeric_count"]],

            ["Categorical Columns", profile["categorical_count"]],

            ["Duplicate Rows", profile["duplicates"]],

            ["Columns with Missing Values", int((profile["missing"] > 0).sum())],

            ["Memory Usage", profile["memory"]]

        ]

        table = Table(
            summary_data,
            colWidths=[220, 220]
        )

        table.setStyle(

            TableStyle([

                ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),

                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

                ("FONTSIZE", (0, 0), (-1, 0), 13),

                ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),

                ("GRID", (0, 0), (-1, -1), 0.8, colors.grey),

                ("BOX", (0, 0), (-1, -1), 1.2, colors.darkblue),

                ("ALIGN", (0, 0), (-1, -1), "CENTER"),

                ("BOTTOMPADDING", (0, 0), (-1, -1), 10),

                ("TOPPADDING", (0, 0), (-1, -1), 10)

            ])

        )

        story.append(table)

        story.append(Spacer(1, 15))

        score = profile["health_score"]

        if score >= 90:
            color = "green"
            status = "Excellent Dataset Quality"

        elif score >= 70:
            color = "orange"
            status = "Good Dataset Quality"

        else:
            color = "red"
            status = "Poor Dataset Quality"

        story.append(
            Paragraph(
                f"""
                <font color="{color}" size="14">
                <b>Dataset Health: {status}</b>
                </font>
                """,
                styles["Body"]
            )
        )

        story.append(Spacer(1, 20))

        story.append(Spacer(1, 25))

        story.append(
            Paragraph(
                "Data Quality Overview",
                styles["SectionTitle"]
            )
        )

        quality = [["Column", "Missing %"]]

        for col, value in profile["missing_percentage"].items():

            if value > 20:
                value_text = f" {value}%"

            elif value > 5:
                value_text = f" {value}%"

            else:
                value_text = f" {value}%"

            quality.append(
                [
                    col,
                    value_text
                ]
            )

        quality_table = Table(
            quality,
            colWidths=[220, 120]
        )

        quality_table.setStyle(

            TableStyle([

                ("BACKGROUND", (0, 0), (-1, 0), colors.darkgreen),

                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

                ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),

                ("ALIGN", (0, 0), (-1, -1), "CENTER"),

                ("BOTTOMPADDING", (0, 0), (-1, -1), 8)

            ])

        )

        story.append(quality_table)

        story.append(PageBreak())

        # =================================================
        # AI INSIGHTS
        # =================================================

        story.append(
            Paragraph(
                "Executive AI Analysis",
                styles["SectionTitle"]
            )
        )

        for line in ai_report.split("\n"):

            line = line.strip()

            if not line:
                continue

            # Heading Level 2
            if line.startswith("##"):
                story.append(
                    Spacer(1, 10)
                )

                story.append(
                    Paragraph(
                        html.escape(line.replace("##", "").strip()),
                        styles["Heading2"]
                    )
                )

                continue

            # Heading Level 3
            if line.startswith("###"):
                story.append(
                    Paragraph(
                        html.escape(line.replace("###", "").strip()),
                        styles["Heading3"]
                    )
                )

                continue

            # Bullet points
            if line.startswith("-") or line.startswith("*"):
                story.append(
                    Paragraph(
                        f"• {html.escape(line[1:].strip())}",
                        styles["Body"]
                    )
                )

                continue

            # Bold markdown (**text**)
            line = line.replace("**", "<b>", 1).replace("**", "</b>", 1)

            story.append(
                Paragraph(
                    line,
                    styles["Body"]
                )
            )


        story.append(Spacer(1, 25))

        # =================================================
        # VISUALIZATIONS
        # =================================================
        story.append(PageBreak())
        if charts:

            story.append(

                Paragraph(

                    "Business Visualizations",

                    styles["SectionTitle"]

                )

            )

            story.append(Spacer(1, 15))

            for title, image_path in charts:

                story.append(

                    Paragraph(

                        title,

                        styles["ChartTitle"]

                    )

                )

                if os.path.exists(image_path):

                    story.append(

                        Image(
                            image_path,
                            width=440,
                            height=260
                        )

                    )

                else:

                    story.append(

                        Paragraph(

                            f"<font color='red'>Image not found:<br/>{html.escape(image_path)}</font>",

                            styles["Body"]

                        )

                    )

                story.append(Spacer(1, 28))

        story.append(PageBreak())
        # =================================================
        # MACHINE LEARNING RECOMMENDATION
        # =================================================

        story.append(

            Paragraph(

                "Machine Learning Recommendation",

                styles["SectionTitle"]

            )

        )

        recommendations = [

            "Remove duplicate rows",

            "Handle missing values",

            "Perform feature engineering",

            "Encode categorical variables",

            "Scale numerical features if required",

            "Train multiple ML models",

            "Evaluate models using cross-validation"

        ]

        if profile["health_score"] < 70:
            recommendations.append(
                "Improve dataset quality before training machine learning models."
            )
        elif profile["health_score"] < 90:
            recommendations.append(
                "Perform additional preprocessing to maximize model performance."
            )
        else:
            recommendations.append(
                "Dataset quality is high and suitable for machine learning."
            )

        for rec in recommendations:

            story.append(

                Paragraph(

                    f"✓ {rec}",

                    styles["Body"]

                )

            )

        story.append(Spacer(1, 20))

        # =================================================
        # FOOTER
        # =================================================

        divider = Table(
            [[""]],
            colWidths=[450]
        )

        divider.setStyle(

            TableStyle([

                ("LINEABOVE", (0, 0), (-1, -1), 1, colors.grey)

            ])

        )

        story.append(divider)

        story.append(Spacer(1, 12))

        story.append(

            Paragraph(

                "<font color='darkblue'><b>Generated by Autonomous Data Science Co-Pilot</b></font>",

                styles["Body"]

            )

        )

        story.append(

            Paragraph(

                f"Generated on: {datetime.now().strftime('%d %B %Y %H:%M')}",

                styles["Body"]

            )

        )

        story.append(

            Paragraph(

                "Powered by Gemini AI • Plotly • Streamlit • ReportLab",

                styles["Body"]

            )

        )

        doc.build(

            story,

            onFirstPage=add_page_number,

            onLaterPages=add_page_number

        )