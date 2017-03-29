import pip

def install(package):
    pip.main(['install', package])

if __name__ == '__main__':
    install('wheel')
    install('pygame')
    install('pytmx')
