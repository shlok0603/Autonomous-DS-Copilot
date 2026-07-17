from pathlib import Path


class ChartExporter:

    @staticmethod
    def save(fig, filename):

        output_folder = (
            Path(__file__).resolve().parent.parent
            / "reports"
            / "temp"
        )

        output_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        image_path = output_folder / filename

        fig.write_image(
            str(image_path),
            scale=2
        )

        return str(image_path)