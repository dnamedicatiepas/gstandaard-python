import os
import requests
from bs4 import BeautifulSoup
import argparse

from .files import file_numbers
from .constants import SKIP_FIELDS, BESCHRIJVINGEN_FILE_EXTENSION


def get_bestand_filename(name, add_ext=False):
    filename = 'BST%sT' % name
    if add_ext:
        filename += BESCHRIJVINGEN_FILE_EXTENSION
    return filename


def get_bestand_htmlpath(directory, name):
    return os.path.join(directory, get_bestand_filename(name, add_ext=True))


def get_bestand_url(file_no):
    BESTAND_BESCHRIJVINGEN_URL_PREFIX = 'https://www.z-index.nl/documentatie/bestandsbeschrijvingen/bestand?bestandsnaam='
    return BESTAND_BESCHRIJVINGEN_URL_PREFIX + get_bestand_filename(file_no)


def get_inputpath(directory, file_no):
    return os.path.join(directory, get_bestand_filename(file_no, add_ext=False))


# https://techoverflow.net/2017/02/26/requests-download-file-if-it-doesnt-exist/
def download_file(filename, url, refresh):

    if os.path.exists(filename) and not refresh:
        return

    with open(filename, 'wb') as fout:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        for block in response.iter_content(4096):
            fout.write(block)


#
# Console script entry point
#
def download_htmls():
    ap = argparse.ArgumentParser()
    ap.add_argument("-b", "--beschrijvingen-directory", required=True,
                    help="Directory with HTML beschrijvingen files")
    ap.add_argument('-r', '--refresh', action='store_true',
                    help='Download files even if they exist already.')
    args = vars(ap.parse_args())

    for file_no in file_numbers:
        download_file(get_bestand_htmlpath(args['beschrijvingen_directory'], file_no),
                      get_bestand_url(file_no),
                      args['refresh'])


def get_bestand_html(directory, file_no):
    html_input = get_bestand_htmlpath(directory, file_no)
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