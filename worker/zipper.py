import click
import os

@click.command()
@click.option('--d')
def entry(d):
    zipfolder(d)

def zipfolder(d):
    files = os.listdir(d)
    raw_names = list()
    for f in files:
        if f == 'ignore':
            continue
        if os.path.isdir(os.path.join(d, f)):
            if not f.startswith('.'):
                cmd = 'zip -r {}.zip {}'.format(os.path.join(d, f), os.path.join(d, f))
                print(cmd)
                os.popen(cmd)
                zipfolder(os.path.join(d, f))

if __name__ == '__main__':
    entry()
