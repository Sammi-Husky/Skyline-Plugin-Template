from ftplib import FTP
import os
import sys

def listdirs(connection,_path):
    file_list, dirs, nondirs = [], [], []
    try:
        connection.cwd(_path)
    except:
        return []

    connection.retrlines('LIST', lambda x: file_list.append(x.split()))
    for info in file_list:
        ls_type, name = info[0], info[-1]
        if ls_type.startswith('d'):
            dirs.append(name)
        else:
            nondirs.append(name)
    return dirs


def ensuredirectory(connection,root,path):
    print(f"Ensuring {os.path.join(root, path)} exists...")
    if path not in listdirs(connection, root):
        connection.mkd(f'{root}/{path}')


consoleIP = sys.argv[1]
if '.' not in consoleIP:
    print(sys.argv[0], "ERROR: Please specify with `IP=[Your console's IP]`")
    sys.exit(-1)

consolePort = 5000

if len(sys.argv) < 4:
    version = '600'
else:
    version = sys.argv[2]

curDir = os.curdir

ftp = FTP()
print(f'Connecting to {consoleIP}... ', end='')
ftp.connect(consoleIP, consolePort)
print('Connected!')

ensuredirectory(ftp, '', 'atmosphere')
ensuredirectory(ftp, '/atmosphere', 'contents')
ensuredirectory(ftp, '/atmosphere/contents', "01006A800016E000")
ensuredirectory(ftp, '/atmosphere/contents/01006A800016E000', 'romfs')
ensuredirectory(ftp, '/atmosphere/contents/01006A800016E000/romfs', 'skyline')
ensuredirectory(ftp, '/atmosphere/contents/01006A800016E000/romfs/skyline', 'plugins')

binaryPath = f'{os.path.basename(os.getcwd())}{version}.nro'
print(binaryPath)
if os.path.isfile(binaryPath):
    sdPath = f'/atmosphere/contents/01006A800016E000/romfs/skyline/plugins/{binaryPath}'
    print(f'Sending {sdPath}')
    ftp.storbinary(f'STOR {sdPath}', open(binaryPath, 'rb'))