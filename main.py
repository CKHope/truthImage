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


def generate_markdown_file(
    truthType: str = "h", levels: int = 3, fileNameLen: int = 2, tag: str = ""
):
    # Generate a random filename
    filePath = generate_file_path(
        truthType=truthType, levels=levels, fileNameLen=fileNameLen, tag=tag
    )
    directory = os.path.dirname(filePath)
    os.makedirs(directory, exist_ok=True)
    # Markdown content
    middlePath = "../" * levels
    markdown_content = f"""\
# Displaying Images
<div style="text-align: center;">
    <img src="./../../{middlePath}im/1.jpg" alt="Image 1" />
</div>

<div style="text-align: center;">
    <img src="./../../{middlePath}im/2.jpg" alt="Image 2" />
</div>
"""

    # Save the Markdown content to a file
    with open(filePath, "w") as file:
        file.write(markdown_content)

    print(f"Markdown file '{filePath}' has been generated.")
    return markdown_content


# Example usage
generate_markdown_file(truthType="h", levels=5, fileNameLen=1, tag="#")
