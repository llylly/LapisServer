import click
import json
import os
from LapisParser import *


@click.command()
@click.option('--source')
@click.option('--name')
@click.option('--method')
@click.option('--out')
def main(source, name, method, out):
    ans = dict()
    ans['data'] = dict()
    ans['succeed'] = False
    ans['errors'] = list()

    source = str(source)
    name = str(name)
    method = str(method)
    out = str(out)

    ans['errors'] = [{'line': 1, 'col': 1, 'errno': 0, 'msg': 'Format Error'}]
    with open(out, 'w') as f:
        json.dump(ans, f)

    try:
        ret1 = addDocFromFile(source)

        assert ret1 is True
        ret2 = parseAPI()

        assert ret2 is True
        ret3 = generateRandomDataFromAPISchema(name, method)

        if ret3 is not None:
            ans['data'] = ret3
            ans['succeed'] = True
        ans['errors'] = list()
        if len(getErrors()) > 0:
            ans['errors'] = getErrors()
    except Exception:
        ans['errors'] = getErrors()

    with open(out, 'w') as f:
        json.dump(ans, f)


if __name__ == '__main__':
    main()
