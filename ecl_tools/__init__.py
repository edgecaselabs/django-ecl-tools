VERSION = (0, 1, 0)

def get_version():
    return __version__

def gen_version(version):
    return '.'.join(str(x) for x in version)

__version__ = gen_version(VERSION)
