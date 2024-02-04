#!/usr/bin/python3
#Fabric script that generates a .tgz archive from the contents of the web_static
import os
from datetime import datetime
from fabric.api import local

def do_pack():
    dt = datetime.utcnow()
    local("mkdir -p version")
    
    file = "version/web_static_{}{}.tgz".format(dt)
    if os.path.exists(file):
        if local("tar -cvzf {} web_static".format(file)):
            return None
        return file
    else:
        return None