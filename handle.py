import markdown
from bs4 import BeautifulSoup
import json

with open("Algorithm.md", "r", encoding="utf-8") as file:
    markdown_content = file.read()

    html_content = markdown.markdown(markdown_content)

    soup = BeautifulSoup(html_content, "html.parser")

    h1_title = soup.h1.text

    li_texts = [li.p.text for li in soup.find_all("li")]

output_data = {"title": h1_title, "li_texts": li_texts}

with open("output.json", "w", encoding="utf-8") as json_file:
    json.dump(output_data, json_file, ensure_ascii=False, indent=2)
