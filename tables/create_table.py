import bibtexparser
from tabulate import tabulate
import logging

template = ["author", "title", "year", "url"]


keys_headers = {
    "author": "Автор",
    "title": "Название",
    "year": "Год",
    "url": "Ссылки",
}

CLOUD_SERVICE_DOMAINS = {
    "drive.google.com": "Диск",
    "docs.google.com": "Диск",
    "drive.usercontent.google.com": "Диск",
    "yadi.sk": "Диск",
    "disk.yandex.ru": "Диск",
    "cloud.mail.ru": "Диск",
    "dropbox.com": "Диск",
    "www.dropbox.com": "Диск",
    "1drv.ms": "Диск",
    "onedrive.live.com": "Диск",
    "icloud.com": "Диск",
    "www.icloud.com": "Диск",
    "cloud.main.ru": "Диск",
    "github.com": "GitHub",
    "gist.github.com": "GitHub",
    "raw.githubusercontent.com": "GitHub",
    "github.io": "GitHub",
    "githubusercontent.com": "GitHub",
}


def read_bib_file(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    entries = bib_database.entries
    logger.info(f"Файл успешно открыт! Обнаружено {len(entries)} элементов")
    return entries


def check_type_url(url: str) -> str:
    domain = url.split("//")[1]
    address = domain.split("/")[0]
    return CLOUD_SERVICE_DOMAINS.get(address, "Ссылка!")


def get_links(urls: list[str]) -> str:
    form = r"[`[{}]`]({})"

    return "<br>".join([form.format(check_type_url(url), url) for url in urls])


def create_table_bib_md(table: list[dict], template_cols: list = template) -> str:
    headers = [keys_headers.get(head, "...") for head in template_cols]
    data = [[i + 1] + ["..."] * len(template_cols) for i in range(len(table))]

    for number, row in enumerate(table):
        for index, col in enumerate(template_cols):
            temp = ""
            value = row.get(col)
            if value == "":
                temp = "-"
            elif col in ("url"):
                urls = value.split(",")
                temp = get_links(urls)
            elif col in ("title"):
                temp = value + f" [{row.get('number', '')}]"
            else:
                temp = row.get(col, "...")
            data[number][index + 1] = temp

    markdown_table = tabulate(data, headers=headers, tablefmt="github")

    logger.info(f"Таблица '{table[0].get('note', '...')}' успешно создана!")
    return markdown_table


def create_page(title: str, value: str, path: str) -> None:
    content = f"# {title}\n\n {value}"
    with open(path, mode="w", encoding="utf-8") as file:
        file.write(content)
    logger.info("Страница успешно создана!")


def create_page_with_bib_tables(
    path_bib: str, path_export: str, title_file: str = "Библиотека"
) -> None:
    data = read_bib_file(path_bib)
    content = {}
    for value in data:
        title = value.get("note", "Разное")
        content[title] = content.get(title, []) + [value]

    if "" in content.keys():
        del content[""]

    string_list_content = ', '.join([f"({len(content[key])} шт) '{key}'" for key in content.keys()])
    log_message = f"Подготавливаются разделы: {string_list_content}"
    logger.info(log_message)

    data = ""
    for title in content.keys():
        data += f"\n## {title}\n\n{create_table_bib_md(content.get(title))}"

    create_page(title=title_file, value=data, path=path_export)


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    file_path = "tables/metodichkas/base.bib"
    path_export = "docs/source/bibliography/metodichkas/main.md"

    logger.info(f"Начало обработки файла с библиографией: {file_path}")

    create_page_with_bib_tables(file_path, path_export)
