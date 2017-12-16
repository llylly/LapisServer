import click
import os

import LapisParser

@click.command()
@click.option('--d')
def entry(d):
    xmltransform(d)

def xmltransform(d):
    files = os.listdir(d)
    raw_names = list()
    for f in files:
        if os.path.isdir(os.path.join(d, f)):
            xmltransform(os.path.join(d, f))
        if os.path.isfile(os.path.join(d, f)):
            if f.endswith('.yaml'):
                try:
                    source = os.path.join(d, f)
                    dest = os.path.join(d, f.rsplit('.', 1)[0] + '.xml')
                    print(source)
                    print(dest)
                    ret1 = LapisParser.addDocFromFile(str(source), 'default')
                    print(ret1)
                    if ret1 is not True:
                        print(LapisParser.getErrors())
                        continue
                    ret2 = LapisParser.saveAsXML(str(dest))
                    print(ret2)
                    LapisParser.removeDoc('default')
                    print(LapisParser.getErrors())
                except Exception, e:
                    print(e.message)


if __name__ == '__main__':
    entry()
