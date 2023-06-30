import os 
import sys
from pathlib import Path
import logging

# Path: template.py 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

project_name = "CNN_classification" # project name


list_of_files = [".github/workflows/.gitkeep",
                f"src/{project_name}/__init__.py",
                f"src/{project_name}/components/__init__.py",
                f"src/{project_name}/utils/__init__.py",
                f"src/{project_name}/config/configuration.py",
                f"src/{project_name}/config/__init__.py",
                f"src/{project_name}/pipeline/__init__.py",
                f"src/{project_name}/entity/__init__.py",
                f"src/{project_name}/constants/__init__.py",
                "config/config.yaml",
                "dvc.yaml",
                "requirements.txt",
                "setup.py",
                "research/trials.ipynb",
                "templates/index.html",


                ]


for file in list_of_files:
    path = Path(file)
    filedir , filename = os.path.split(path)
    if filedir !="" :
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created {filedir}")
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        with open(path,"w") as f:
            pass
        logging.info(f"Created {path}")
    else:
        logging.info(f"{path} already exists")
    