import random
import string
from datetime import datetime
from random import sample, choice
import os


def generate_file_path(truthType: str, levels: int = 3, fileNameLen: int = 15, tag="#"):
    today = str(datetime.now().strftime("%d%m%y"))
    folders = [choice(string.ascii_lowercase) for _ in range(levels)]
    # folder_path = './' + '/'.join(folders) + '/'
    folder_path = "/".join(folders) + "/"

    letters = string.ascii_letters
    fileName = "".join(choice(letters) for _ in range(fileNameLen))

    file_path = f"{truthType}/{today}/{folder_path}h{fileName}{tag}.md"
    return file_path


def generate_markdown_file(length):
    # Generate a random filename
    filePath = generate_file_path(truthType="h", levels=3, fileNameLen=2, tag="")
    directory = os.path.dirname(filePath)
    os.makedirs(directory, exist_ok=True)
    # Markdown content
    markdown_content = """\
# Displaying Images

<div style="text-align: center;">
    <img src="./im/1.jpg" alt="Image 1" />
</div>

<div style="text-align: center;">
    <img src="./im/2.jpg" alt="Image 2" />
</div>
"""

    # Save the Markdown content to a file
    with open(filePath, "w") as file:
        file.write(markdown_content)

    print(f"Markdown file '{filePath}' has been generated.")


# Example usage
generate_markdown_file(20)
