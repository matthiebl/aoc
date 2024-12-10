from pathlib import Path
from .constants import Constants


def copy_template(year: str, day: str):
    template_path = Path(__file__).parent.parent / "static" / "template.txt"
    template = open(template_path).read()
    content = template.format(YEAR=year, DAY=day)

    content_path = Path(__file__).parent.parent / year / Constants.script_file.format(day=f"{int(day):02d}")
    if content_path.is_file() and input("File already exists. Do you want to override? (yes/no) ").lower() != "yes":
        return
    content_path.parent.mkdir(exist_ok=True)
    with content_path.open("w") as fp:
        fp.write(content)


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Advent of Code Template Creator")
    parser.add_argument("year")
    parser.add_argument("day")
    args = parser.parse_args()

    copy_template(year=args.year, day=args.day)
