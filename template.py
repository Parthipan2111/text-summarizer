import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')


project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/model/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.py",
    "setup.py",
    "research/test.ipynb"

]

for filepath in list_of_files:
    filePath = Path(filepath)
    fileDir,fileName = os.path.split(filePath)

    if fileDir != "":
        os.makedirs(fileDir,exist_ok=True)
        logging.info(f"Creating Directory: {fileDir} for the file {fileName}")

    if(not os.path.exists(filePath)) or (os.path.getsize(filePath) == 0):
        with open(filePath,'w') as f:
            pass
            logging.info(f"creating emty file: {filePath} ")
    else:
        logging.info(f"File path exist: {filePath} ")
