from fastapi import Request
from datetime import datetime
def log(request : Request, tag:str = "defaulttag", message:str = "Default message"):
    with open("logger/log_files/logfile.txt","a+") as logger:
        logger.write(f"{datetime.now()} :- {request.url} --- {request.method} --- {tag} :- {message}\n")