import os
from .. import Node_Ignore, Node_Docker, Python_Ignore, Python_Docker
class Init():
    def __init__(self):
        filelist = os.listdir(os.getcwd())
        if "package.json" in filelist:
            return self.js_init()
        if "requirements.txt" in filelist:
            return self.py_init()
        else:
            return self.js_init()


    def js_init(self):
        run_command = input('Enter the bash command to run the project:')
        if not run_command:
            run_command = "npm run start"
        print("Initializing this project for Deplux, Wait a moment..")
        self.createfile(name=".dockerignore", text=Node_Ignore)
        self.createfile(name="Dockerfile", text=Node_Docker.replace("[run_command]", run_command))
        print("Dockerfile has created")
    def py_init(self):
        run_command = input('Enter the bash command to run the project:')
        if not run_command:
            run_command = "python app.py"
        print("Initializing this project for Deplux, Wait a moment..")
        self.createfile(name=".dockerignore", text=Python_Ignore)
        self.createfile(name="Dockerfile", text=Python_Docker.replace("[run_command]", run_command))
        print("Dockerfile has created")
        
        




        




        

    def createfile(self, name : str, text : str):
        f = open(name, 'w')
        f.write(text)
        f.close()




