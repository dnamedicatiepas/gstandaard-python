from parsing import get_bestand_html, extract_struct
from files import file_numbers
from definition import foreign_keys, proxies, aggregates, relationships
from constants import SKIP_FIELDS


def get_non_composite_key(table_name, name, debug=False):
    if table_name not in foreign_keys:
        return None

    # Find out if there are multiple foreign keys per target table
    for group in foreign_keys[table_name]:

        if name in group:
            target_table, member = group[name].split('.')

            if debug:
                print('Target table: %s, member: %s' % (target_table, member))

            if table_name == target_table:
                if debug:
                    print('%s is a self reference' % target_table)

                return group[name]

            elif len(group) > 1:

                if debug:
                    print('%s is part of a composite foreign key' % name)
                return None

            else:
                if debug:
                    print('%s is not part of a composite foreign key' % name)
                return group[name]

    return None


def get_target_name(table_name, name):
    if table_name not in foreign_keys:
        return None

    for group in foreign_keys[table_name]:
        if name in group:
            return group[name]

    return None


def create_class(file_no):

    code = ''

    table_name = 'bst_%s' % file_no
    class_name = table_name

    code += '\n\nclass %s(Base):\n' % class_name

    html = get_bestand_html(file_no)
    fields = extract_struct(html.body.find('table', attrs={'class': 'zindextable'}))

    title = html.body.find('h1', attrs={'class': 'documentFirstHeading'}).string

    code += '    """Title: %s"""\n' % title
    code += '    __tablename__ = "%s"\n' % table_name
    code += '\n'

    fks = []
    repr_fields = []
    for s in sorted(fields, key=lambda x: x['key']):

        name = s['name']

        if name in SKIP_FIELDS:
            continue

        if name != 'bstnum':
            repr_fields.append(name)

        kind = s['kind']
        assert kind in ['Integer', 'String']

        key = s['key']
        assert key is not None

        size = s['size']
        assert size > 0

        fk = get_non_composite_key(table_name, name)
        if not fk:
            target_name = get_target_name(table_name, name)
            if target_name:
                fks.append((name, target_name))

        code += '    %s = Column(%s%s%s%s)\n' % (
            name,
            kind,
            '(%s)' % size if kind == 'String' else '',
            ', ForeignKey("%s")' % fk if fk else '',
            ', primary_key=True' if key > 0 else '')

    code += '\n'
    code += '    def __repr__(self):\n'
    code += '        return "<%s(%%d)[%s]>" %% (self.bstnum, %s)\n' % (
        title.split(' ', 3)[-1],
        ', '.join(['%s=%%s' % x for x in repr_fields]),
        ', '.join(['self.' + x for x in repr_fields])
    )

    if table_name in relationships:
        code += '\n'
        for rel in relationships[table_name]:
            entry = relationships[table_name][rel]

            # We use square brackets to denote that the member should be a list
            if not isinstance(entry, str):
                assert len(entry) == 1
                uselist = True
                entry = entry[0]
            else:
                uselist = False

            def entry2x(entry):
                local, remote = entry.split('==')

                if '.' in local:
                    local_table, local_column = local.split('.')
                else:
                    local_table, local_column = None, None

                if '.' in remote:
                    remote_table, remote_column = remote.split('.')
                else:
                    remote_table, remote_column = None, None

                return local, local_table, local_column, remote, remote_table, remote_column

            # Check the number of entries
            if ',' not in entry:
                # single entry

                if '==' not in entry:
                    # simple relationship
                    desc = entry
                else:
                    # complex relationship
                    _, lt, _, _, rt, rc = entry2x(entry)
                    desc = "'%s'" % rt

                    if uselist:
                        desc += ', uselist=True'

                    if lt == rt:
                        desc += ', remote_side=[%s]' % rc
                    desc += ", primaryjoin=%s" % entry

            else:
                # Multiple entries
                remote_columns = []
                remote_tables = []
                local_tables = []

                entries = [x.strip() for x in entry.split(',')]

                for one in entries:
                    local, lt, _, remote, rt, rc = entry2x(one)

                    if rc:
                        remote_columns.append(rc)
                    if rt:
                        remote_tables.append(rt)
                    if lt:
                        local_tables.append(lt)

                assert len(set(local_tables)) == 1
                assert len(set(remote_tables)) == 1

                desc = "'%s'" % remote_tables[0]

                if uselist:
                    desc += ', uselist=True'

                desc += ", primaryjoin='%s'" % 'and_(%s)' % ', '.join(entries)

                if local_tables[0] == remote_tables[0]:
                    desc += ', remote_side=[%s]' % ', '.join(remote_columns)

            # End of relationship construction
            code += '    %s = relationship(%s)\n' % (rel, desc)

    if table_name in aggregates:
        for new_entry in aggregates[table_name]:
            code += '\n'
            code += '    @hybrid_property\n'
            code += '    def %s(self):\n' % new_entry
            code += '        return [x.%s for x in %s]\n' % aggregates[table_name][new_entry]  # Tuple

    if table_name in proxies:
        code += '\n'
        for kw in proxies[table_name]:
            code += '    %s = association_proxy("%s", "%s")\n' % (
                         kw, proxies[table_name][kw][0], proxies[table_name][kw][1])

    if fks:
        lhs = []
        rhs = []

        for fk, target_name in fks:
            lhs.append(fk)
            rhs.append(target_name)

        code += '\n'
        code += '    __table_args__ = (\n'
        code += '        ForeignKeyConstraint(\n'
        code += '            %s,\n' % lhs
        code += '            %s,\n' % rhs
        code += '        ),\n'
        code += '    )\n'

    return code


all_code = '''\
#
# !!!! this file is auto-generated !!!
#

from sqlalchemy import Column, Integer, String, ForeignKey, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()
'''


for file_no in file_numbers:
    all_code += create_class(file_no)

print(all_code)
