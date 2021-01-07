import os
import json
class New():
    def __init__(self):
        filelist = os.listdir(os.getcwd())
        folder_name = self.folder_build()
        config_json = {}
        git_repo = input("Enter the github repository url (if you want to clone):")
        if git_repo.isspace():
            config_json["git"] = {}
            config_json["git"]["repo"] = str(git_repo)
        custom_domain = input("Enter a custom domain (if you have a premium):")
        if custom_domain.isspace():
            config_json["domain"] = str(custom_domain)
        author = input("Please enter the author:")
        if not author:
            author = "Deplux User"
        description = input("Please enter the description:")
        if not description:
            description = "Developing Project with Deplux"
        

        with open(f'{folder_name}/manifest.json', 'w', encoding='utf-8') as make_file:
            json.dump(config_json, make_file, ensure_ascii=False, indent="\t")
        readme_md = """
# [Project_name]
[Description]
## Contributors
- [Author]


        """
        readme_md = readme_md.replace("[Project_name]", folder_name)
        readme_md = readme_md.replace("[Description]", description)
        readme_md = readme_md.replace("[Author]", author)
        self.createfile(name=f"{folder_name}/README.md", text=readme_md)
        print(f"The project({folder_name}) has been created")
        


        

        
        
        


        


        

    def folder_build(self):
        folder_name = input("Enter a project name:")
        os.makedirs(folder_name)
        return folder_name

    def createfile(self, name : str, text : str):
        f = open(name, 'w')
        f.write(text)
        f.close()

    
        
    
