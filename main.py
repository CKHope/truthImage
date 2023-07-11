import random
import string


def generate_markdown_file(length):
    # Generate a random filename
    filename = (
        "".join(random.choices(string.ascii_lowercase + string.digits, k=length))
        + ".md"
    )

    # Markdown content
    markdown_content = """\
# Displaying Images

![Image 1](./im/1.jpg)
![Image 2](./im/2.jpg)
"""

    # Save the Markdown content to a file
    with open(filename, "w") as file:
        file.write(markdown_content)

    print(f"Markdown file '{filename}' has been generated.")


# Example usage
generate_markdown_file(20)
