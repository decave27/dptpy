Node_Ignore="""
node_modules
npm-debug.log
"""
Node_Docker="""
FROM node:12

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
CMD [run_command]
EXPOSE 80
"""

Python_Ignore="""
__pycache__
*.pyc
*.pyo
*.pyd
pip-log.txt
pip-delete-this-directory.txt
.tox
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*,cover
*.log
.git
"""

Python_Docker="""
FROM python:3.8-slim

WORKDIR /app
COPY . .
RUN pip install --trusted-host pypi.python.org -r requirements.txt 

CMD [run_command]
EXPOSE 80
"""