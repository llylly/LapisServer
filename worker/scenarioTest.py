import click
import json
from LapisParser import *


@click.command()
@click.option('--source')
@click.option('--out')
def main(source, out):
    ans = dict()
    ans['report'] = dict()
    ans['succeed'] = False
    ans['errors'] = list()

    source = str(source)
    out = str(out)

    ans['errors'] = [{'line': 1, 'col': 1, 'errno': 0, 'msg': 'Format Error'}]
    with open(out, 'w') as f:
        json.dump(ans, f)

    try:
        ret1 = addDocFromFile(source)
        assert ret1 is True

        ret2 = parseAPI()
        assert ret2 is True

        ret3 = parseScenario()
        assert ret3 is True

        ret4 = parseConfig()
        assert ret4 is True

        ret5 = runScenario(2)
        if ret5 is not None:
            ans['succeed'] = True
            ans['report'] = ret5
            ans['errors'] = list()
        else:
            ans['errors'] = getRuntimeErrors()
    except Exception:
        ans['errors'] = getErrors()

    with open(out, 'w') as f:
        json.dump(ans, f)


if __name__ == '__main__':
    main()