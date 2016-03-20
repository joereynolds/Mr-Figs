import pip

def install(package):
    pip.main(['install', package])

if __name__ == '__main__':
    install('pygame-1.9.2a0-cp35-none-win32.whl')
    install('pytmx')
    
