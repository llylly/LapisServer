import click
import json
import os
from LapisParser import *

@click.command()
@click.option('--source')
@click.option('--msgpath')
@click.option('--out')
def main(source, msgpath, out):
    stat = dict()
    stat['success'] = False

    source = str(source)
    msgpath = str(msgpath)
    out = str(out)

    stat['errors'] = [{'line': 1, 'col': 1, 'errno': 0, 'msg': 'Format Error'}]
    with open(msgpath, 'w') as f:
        json.dump(stat, f)

    ret1 = addDocFromFile(source, 'default')
    if ret1 is not True:
        stat['errors'] = getErrors()
    else:
        ret2 = False
        if source.endswith('.yaml'):
            ret2 = saveAsXML(out)
        if source.endswith('.xml'):
            ret2 = saveAsYAML(out)
        if ret2 is not True:
            stat['errors'] = getErrors()
        else:
            ret2 = True
        stat['success'] = ret2

        with open(msgpath, 'w') as f:
            json.dump(stat, f)


if __name__ == '__main__':
    main()