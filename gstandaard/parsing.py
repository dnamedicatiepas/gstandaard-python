import os
import requests
from bs4 import BeautifulSoup

from files import file_numbers
from constants import SKIP_FIELDS, BESCHRIJVINGEN_FILE_EXTENSION

from config import BESCHRIJVINGEN_DIRECTORY, BESTAND_BESCHRIJVINGEN_URL_PREFIX, DATA_DIRECTORY


def get_bestand_filename(name, add_ext=False):
    filename = 'BST%sT' % name
    if add_ext:
        filename += BESCHRIJVINGEN_FILE_EXTENSION
    return filename


def get_bestand_htmlpath(name):
    return os.path.join(BESCHRIJVINGEN_DIRECTORY, get_bestand_filename(name, add_ext=True))


def get_bestand_url(file_no):
    return BESTAND_BESCHRIJVINGEN_URL_PREFIX + get_bestand_filename(file_no)


def get_inputpath(file_no):
    return os.path.join(DATA_DIRECTORY, get_bestand_filename(file_no, add_ext=False))


# https://techoverflow.net/2017/02/26/requests-download-file-if-it-doesnt-exist/
def download_file(filename, url):
    with open(filename, 'wb') as fout:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        for block in response.iter_content(4096):
            fout.write(block)


def download_if_not_exists(filename, url):
    if not os.path.exists(filename):
        download_file(filename, url)
        return True
    return False


def refresh_htmls():
    for file_no in file_numbers:
        download_if_not_exists(get_htmlpath(file_no), get_bestand_url(file_no))


def get_bestand_html(file_no):
    html_input = get_bestand_htmlpath(file_no)
    html = BeautifulSoup(open(html_input).read(), features='html5lib')

    return html


def extract_struct(table):
    fields = []

    for entry in table.findChildren('tr')[1:]:

        _desc, sr, size, fmt, _pos = map(lambda x: x.text, entry.findChildren('td'))

        if sr:
            key = int(sr[0])
        else:
            key = 0

        if fmt == 'N':
            kind = 'Integer'
            if '+' in size or ',' in size:
                size = size.split('(')[0]
        else:
            kind = 'String'

        if entry.th.a:
            name = entry.th.a.text.lower()
        else:
            name = 'empty'

        if name in SKIP_FIELDS:
            size = int(size) * -1

        field = {
            'name': name,
            'size': int(size),
            'kind': kind,
            'key': key
        }

        fields.append(field)

    return fields