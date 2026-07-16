from pathlib import Path


class ChartExporter:

    @staticmethod
    def save(fig, filename):

        output_folder = Path("reports/temp")

        output_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        path = output_folder / filename

        fig.write_image(
            str(path),
            scale=2
        )

        return str(path)