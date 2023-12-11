import os
import markdown
import json
from bs4 import BeautifulSoup


def process_markdown_file(file_path, output_folder="json"):
    with open(file_path, "r", encoding="utf-8") as file:
        markdown_content = file.read()

        html_content = markdown.markdown(markdown_content)

        soup = BeautifulSoup(html_content, "html.parser")

        h1_title = soup.h1.text

        li_texts = [li.p.text for li in soup.find_all("li")]

    output_data = {"title": h1_title, "li_texts": li_texts}

    output_file_name = os.path.join(
        output_folder, f"{os.path.basename(file_path)[:-2]}json"
    )

    with open(output_file_name, "w", encoding="utf-8") as json_file:
        json.dump(output_data, json_file, ensure_ascii=False, indent=2)


process_markdown_file("markdown/Algorithm.md")
process_markdown_file("markdown/Living-Documentation.md")
