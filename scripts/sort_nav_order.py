from dataclasses import dataclass
from dataclasses import dataclass
from datetime import datetime, timedelta
import pathlib
import re
import os


# add to this if there is a new parent directory to sort
DIRS_TO_ORDER = [
    pathlib.Path("./notes/other_books"),
    pathlib.Path("./notes/business_books"),
    pathlib.Path("./notes/tech_books"),
    pathlib.Path("./notes/educational_books"),
    pathlib.Path("./notes/projects"),
]


@dataclass
class MarkdownMeta:
    filename: os.PathLike
    last_modified: datetime
    file_contents: str
    nav_order: int

    def write(self):
        with open(self.filename, "w") as f:
            f.write(self.file_contents)


def get_md_meta(path):
    """
    Parses a markdown file to populate the MarkdownMeta class. Date handling isn't robust.
    Default nav order of 0.
    """
    nav_order = 0
    last_modified = datetime.now() - timedelta(days=365)

    with open(path, "r") as f:
        file_data = f.read()
        for line in file_data.split("\n"):
            if line.startswith("last_modified_date"):
                unparsed_date = line.split(": ")[1].strip().replace('"', "")
                last_modified = datetime.strptime(unparsed_date, "%Y-%m-%d %H:%M:%S.%f")
        return MarkdownMeta(path, last_modified, file_data, nav_order)


def main():
    for dir_path in DIRS_TO_ORDER:
        print(f"Sorting {dir_path}")

        # iterates through all md files and parses to objects
        all_file_data = []
        for file_path in dir_path.glob("*.md"):
            print(f"sorting {file_path}")
            all_file_data.append(get_md_meta(file_path))

        # sort by last_modified, which is used to set nav_order
        sorted_files = sorted(
            all_file_data, key=lambda x: x.last_modified, reverse=True
        )

        # rewrite all files with new nav_order, after using regex to sub it in
        for idx, file_data in enumerate(sorted_files):
            file_data.nav_order = idx
            file_data.file_contents = re.sub(
                r"(nav_order:)\s*\d+", rf"\1 {idx}", file_data.file_contents
            )
            print(idx, file_data.filename, file_data.last_modified, sep=" ---> ")
            file_data.write()


if __name__ == "__main__":
    main()
