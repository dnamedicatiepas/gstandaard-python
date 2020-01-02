import struct
from .parsing import get_bestand_html, get_inputpath, extract_struct
from .db import create_session
from .constants import SKIP_FIELDS
from .files import file_numbers
from .utils import load_class
import argparse

priority_files = ['902']


def priosort(l, prio):
    def prio_index(x):
        try:
            return prio.index(x)
        except ValueError:
            return len(prio)

    return sorted(l, key=lambda x: prio_index(x))


def populate_db(data_directory, beschrijvingen_directory, database):

    session = create_session(database)

    for file_no in priosort(file_numbers, priority_files):

        print('Parsing file %s ...' % get_inputpath(data_directory, file_no))

        html = get_bestand_html(beschrijvingen_directory, file_no)
        fields = extract_struct(html.body.find('table', attrs={'class': 'zindextable'}))

        fieldwidths = [x['size'] for x in fields]
        fmtstring = ' '.join('{}{}'.format(abs(fw), 'x' if fw < 0 else 's') for fw in fieldwidths)
        fieldstruct = struct.Struct(fmtstring)

        parse = lambda line: tuple(s.decode() for s in fieldstruct.unpack_from(line.encode()))

        data = []
        with open(get_inputpath(data_directory, file_no), "r") as infile:
            for line in infile:
                # 0x1a / substitute character / eof
                if len(line) == 1:
                    break
                datum = parse(line)
                data.append(datum)

        table_name = 'bst_%s' % file_no

        column_tups = []

        for s in fields:

            name = s['name']
            if name in SKIP_FIELDS:
                continue

            kind = s['kind']
            # If this fails, we need to translate types
            assert kind in ['Integer', 'String']

            column_tups.append((name, kind))

        table_class = load_class('gstandaard.model.' + table_name)
        table_instance = table_class

        columns = [x[0] for x in column_tups]
        for d in data:
            t = dict(zip(columns, d))

            b = table_instance(**t)
            session.add(b)

        session.commit()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--data-directory", required=True,
                    help="Directory with g-standaard data files")
    ap.add_argument("-b", "--beschrijvingen-directory", required=True,
                    help="Directory with HTML beschrijvingen files")
    ap.add_argument("-s", "--sqlite-database", required=True,
                    help="File name of to be created SQLite database")
    args = vars(ap.parse_args())
    populate_db(args['data_directory'], args['beschrijvingen_directory'], args['sqlite_database'])


if __name__ == '__main__':
    main()
