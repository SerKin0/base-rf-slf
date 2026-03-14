import bibtexparser
from tabulate import tabulate


file_path = 'tables/metodichkas/base.bib'

template = ['author', 'title', 'year', 'url']
path_export = "docs/source/bibliography/metodichkas/main.md"


keys_headers = {
    'author': 'Автор',
    'title': 'Название',
    'year': 'Год',
    'url': 'Ссылки',
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
    "githubusercontent.com": "GitHub"
}


def read_bib_file(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    return bib_database.entries


def check_type_url(url: str) -> str:
    domain = url.split('//')[1]
    address = domain.split('/')[0]
    return CLOUD_SERVICE_DOMAINS.get(address, 'Ссылка!')


def get_links(urls : list[str]) -> str:
    form = r"[`[{}]`]({})"
    
    return '<br>'.join([form.format(check_type_url(url), url) for url in urls])


def create_table_bib_md(table: list[dict], template_cols: list = template) -> str:
    headers = [keys_headers.get(head, "...") for head in template_cols]
    data = [[i+1] + ['...'] * len(template_cols) for i in range(len(table))]
    
    for number, row in enumerate(table):
        for index, col in enumerate(template_cols):
            temp = ""
            if col in ('url'):
                urls = row.get(col).split(',')
                temp = get_links(urls)
            elif col in ('title'):
                temp = row.get(col) + f" [{row.get('number', '')}]"
            else:
                temp = row.get(col, "...")
            data[number][index+1] = temp
    
    markdown_table = tabulate(data, headers=headers, tablefmt="github")
    return markdown_table

def create_page(title: str, value: str, path: str) -> None:
    content = f"# {title}\n\n {value}"
    with open(path, mode='w', encoding='utf-8') as file:
        file.write(content)
        
        
def create_page_with_bib_table(title: str, path_bib: str, path_export: str) -> None:
    create_page(
        title=title,
        value=create_table_bib_md(read_bib_file(path_bib)),
        path=path_export
    )


create_page_with_bib_table(
    "Методички по физике",
    file_path,
    path_export
)