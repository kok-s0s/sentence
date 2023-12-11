import os
import markdown
import json
from bs4 import BeautifulSoup


def process_markdown_files(file_paths, output_folder="json"):
    all_data = []

    for file_path in file_paths:
        with open(file_path, "r", encoding="utf-8") as file:
            markdown_content = file.read()

            html_content = markdown.markdown(markdown_content)

            soup = BeautifulSoup(html_content, "html.parser")

            h1_title = soup.h1.text

            li_texts = [li.p.text for li in soup.find_all("li")]

        file_data = {"title": h1_title, "li_texts": li_texts}
        all_data.append(file_data)

    output_file_name = os.path.join(output_folder, "combined_output.json")

    with open(output_file_name, "w", encoding="utf-8") as json_file:
        json.dump(all_data, json_file, ensure_ascii=False, indent=2)


file_paths = ["markdown/Algorithm.md", "markdown/Living-Documentation.md"]
process_markdown_files(file_paths)
