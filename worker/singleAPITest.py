import click
import json
from LapisParser import *


@click.command()
@click.option('--source')
@click.option('--name')
@click.option('--method')
@click.option('--isali')
@click.option('--secret_key')
@click.option('--timeout')
@click.option('--out')
def main(source, name, method, isali, secret_key, timeout, out):
    ans = dict()
    ans['report'] = dict()
    ans['succeed'] = False
    ans['errors'] = list()

    source = str(source)
    name = str(name)
    method = str(method)
    isali = str(isali)
    assert isali == 'True' or isali == 'False'
    if isali == 'True':
        isali = True
    else:
        isali = False
    secretKey = str(secret_key)
    timeout = int(timeout)
    out = str(out)
    ans['params'] = {'api_name': name, 'method': method, 'isali': isali, 'secret_key': secretKey, 'timeout': timeout}

    ans['errors'] = [{'line': 1, 'col': 1, 'errno': 0, 'msg': 'Format Error'}]
    with open(out, 'w') as f:
        json.dump(ans, f)

    try:
        ret1 = addDocFromFile(source)
        assert ret1 is True

        ret2 = parseAPI()
        assert ret2 is True

        if isali:
            ret3 = runSingleAPIforAli(name, method, secretKey, timeout)
        else:
            ret3 = runSingleAPI(name, method, timeout)

        if ret3 is not None:
            ans['report'] = ret3
            ans['succeed'] = True
            ans['errors'] = list()
        else:
            ans['errors'] = getRuntimeErrors()
    except Exception:
        ans['errors'] = getErrors()

    with open(out, 'w') as f:
        json.dump(ans, f)


if __name__ == '__main__':
    main()
