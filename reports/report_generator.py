from reports.pdf_generator import PDFGenerator


class ReportGenerator:

    @staticmethod
    def generate(profile, ai_report):

        filename = "reports/AI_Report.pdf"

        PDFGenerator.generate(
            profile,
            ai_report,
            filename
        )

        return filename