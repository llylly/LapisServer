import click
import json
import os
from LapisParser import *

@click.command()
@click.option('--source')
@click.option('--out')
def main(source, out):
    ans = dict()
    ans['docParse'] = False
    ans['apiParse'] = False
    ans['scenarioParse'] = False
    ans['configParse'] = False

    source = str(source)
    out = str(out)

    ans['errors'] = [{'line': 1, 'col': 1, 'errno': 0, 'msg': 'Format Error'}]
    with open(out, 'w') as f:
        json.dump(ans, f)

    ret1 = addDocFromFile(source)
    if ret1 is True:
        ans['docParse'] = True

    if ans['docParse']:
        ret2 = parseAPI()
        if ret2 is True:
            ans['apiParse'] = True
            ans['apiNames'] = getAPINames()

    if ans['apiParse']:
        ret3 = parseScenario()
        if ret3 is True:
            ans['scenarioParse'] = True
            ans['scenarioNames'] = getScenarioNames()
            ans['scenarioDetail'] = dict()
            for name in ans['scenarioNames']:
                ans['scenarioDetail'][name] = getScenario(name)

    if ans['scenarioParse']:
        ret4 = parseConfig()
        if ret4 is True:
            ans['configParse'] = True
            ans['config'] = getConfig()

    if (not ans['docParse']) or (not ans['apiParse']) or (not ans['scenarioParse']) or (not ans['configParse']):
        ans['errors'] = getErrors()

    with open(out, 'w') as f:
        json.dump(ans, f)


if __name__ == '__main__':
    main()
