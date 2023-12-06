import subprocess
import os
import time

def extToIconName(ext):
    if(ext in ['doc','docx']):
        return 'word'
    if(ext in ['XLS', 'XLSX', 'XLSM', 'XLTX', 'XLTM']):
        return 'excel'
    if(ext in ['ppt','pptx']):
        return 'ppt'
    if(ext == 'pdf'):
        return 'pdf'
    if(ext in ['html','htm','css','js','c','cpp','java','py','sh']):
        return 'code'
    if(ext in ['CAB', 'ARJ', 'LZH', 'TAR', 'GZ', 'TAR.GZ', 'BZ2', 'TAR.BZ2', 'UUE', 'JAR', 'ISO', '7Z', 'XZ', 'Z', 'Zip']):
        return 'zip'
    return 'files'

def iconSelector(icon):    
    icons={
        'files':'<i class="fa-solid fa-file"></i>',
        'word':'<i class="fa-solid fa-file-word"></i>',
        'excel':'<i class="fa-solid fa-file-excel"></i>',
        'ppt':'<i class="fa-solid fa-file-powerpoint"></i>',
        'pdf':'<i class="fa-solid fa-file-pdf"></i>',
        'zip':'<i class="fa-solid fa-file-zipper"></i>',
        'img':'<i class="fa-solid fa-file-image"></i>',
        'audio':'<i class="fa-solid fa-file-audio"></i>',
        'video':'<i class="fa-solid fa-file-video"></i>',
        'csv':'<i class="fa-solid fa-file-csv"></i>',
        'code':'<i class="fa-solid fa-file-code"></i>',
        'folder':'<i class="fa-solid fa-folder"></i>',
        }
    return(icons.get(icon))

def files():
    fileSpace=os.listdir()    
    filesAndExt=[]
    folders=[]
    for i in fileSpace:
        if(os.path.isfile(i)):
            ls=[]
            ls.append(i[:-len(i.split('.')[-1])-1])
            ls.append(i[-len(i.split('.')[-1]):])
            filesAndExt.append(ls)
        else:
            folders.append(i)
    filesAndExt.remove(['index','html'])
    #print(filesAndExt)

def files(filesAndExt):
    bodyContent=[]
    for i in filesAndExt:
        bodyContent.append(f'<a href="{".".join(i)}" download="{".".join(i)}"><div class="ContentSpace"><div class="icon">{iconSelector(extToIconName(i[1]))}</div><div class="contentName">{".".join(i)}</div></div></a>')
    for i in folders:
        bodyContent.append(f'<a href="{i}"><div class="ContentSpace"><div class="icon">{iconSelector("folder")}</div><div class="contentName">{i}</div></div></a>')
    return(bodyContent)
         
def fileUpdater(bodyContent):
    htmlTemplateHeader="".join(['<!DOCTYPE html>\n', '<html lang="en">\n', '<head>\n', '    <meta charset="UTF-8">\n', '    <title>EHS</title>\n','<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">\n', '</head>\n', '<body>\n', '    \n'])
    bodyContent="\n".join(bodyContent)
    htmlTemplateFooter="".join(['\n</body>\n', '</html>\n', '<style>\n','    *\n', '    {\n', '        margin: 0;\n', '        padding: 0;\n', '    }\n', '    body\n', '    {\n', '        display: flex;\n', '    }\n','    a\n','    {\n', '        display: flex;\n', '        align-items: center;\n', '        justify-content: center;\n','        padding: 1rem;', '    }\n', '    .ContentSpace\n', '    {\n', '        height: 6rem;\n', '        width: 6rem;\n', '    }\n', '    .icon i\n', '    {\n', '        height: 100%;\n', '        width: 100%;\n', '        font-size: 5.5rem\n', '    }\n', '</style>\n', ''])
    content=htmlTemplateHeader+bodyContent+htmlTemplateFooter
    return content

with open("index.html","w") as f:
            f.write(fileUpdater(files()))
            print("file initlizer")

while True:
    print("======================")
    oldHash=hash("\n".join(files()))
    time.sleep(2)
    newHash=hash("\n".join(files()))
    if(oldHash!=newHash):
        #print("Changes happens.....")
        #print(files())
        with open("index.html","w") as f:
            f.write(fileUpdater(files()))
            print("file modified")
    print("======================")


os.chdir(input("Enter the path for file server: "))
print(os.getcwd())
wifiConfig=subprocess.getoutput("ipconfig").split("\n")[subprocess.getoutput("ipconfig").split("\n").index("Wireless LAN adapter Wi-Fi:"):]
for i in wifiConfig:
    if("IPv4 Address" in i.strip()):
        ip=i.split(":")[1]
        break
print(ip)

time.sleep(1)
print("started")
print(subprocess.getoutput("python -m http.server 3000"))


