import os
import zipfile
from datetime import datetime
class Zip():
    def __init__(self):
        filelist = os.listdir(os.getcwd())
        
        if "package.json" in filelist:
            return self.js_zip()
        if "requirements.txt" in filelist:
            return self.py_zip()

    def js_zip(self):
        time = datetime.today().strftime("%Y-%m-%d-%H%M")
        filelist = os.listdir(os.getcwd())
        if "node_modules" in filelist:
            filelist.remove('node_modules')
        print("Zipping this project to Deploy at Deplux, Wait a moment..")
        with zipfile.ZipFile(f"deplux_build-{time}.zip", 'w') as myzip:
            for i in filelist:
                myzip.write(i, compress_type=zipfile.ZIP_DEFLATED)
            myzip.close()
        return print(f'Zip file has created at "deplux_build-{time}.zip", Enjoy')

    def py_zip(self):
        time = datetime.today().strftime("%Y%m%d%H%M")
        filelist = os.listdir(os.getcwd())
        if "__pycache__" in filelist:
            filelist.remove('__pycache__')
        print("Zipping this project to Deploy at Deplux, Wait a moment..")
        with zipfile.ZipFile(f"deplux_build-{time}.zip", 'w') as myzip:
            for i in filelist:
                myzip.write(os.path.join(os.getcwd(), i), compress_type=zipfile.ZIP_DEFLATED)
            myzip.close()
        return print(f'Zip file has created at "deplux_build-{time}.zip", Enjoy')

    

        
        
        
        
        






