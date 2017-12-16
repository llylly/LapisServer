import click
import os



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
                import LapisParser
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
                print(LapisParser.getErrors())


if __name__ == '__main__':
    entry()
