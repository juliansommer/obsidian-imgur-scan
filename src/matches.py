import os
import re


def find_matches_in_files(
    folder_path: str, pattern: str, file_extension: str
) -> set[str]:
    """
    Scan all files in a given folder and its subfolders for matches of a regex pattern.
    """
    matches = set()
    regex = re.compile(pattern)
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(file_extension):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    matches.update(regex.findall(content))
    return matches
