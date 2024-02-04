#!/usr/bin/python3
#Fabric script that generates a .tgz archive from the contents of the web_static
import os
from datetime import datetime
from fabric.api import local

def do_pack():
    dt = datetime.utcnow()
    """Create a tar gzipped archive of the directory web_static."""
    file = "version/web_static_{}{}{}{}{}{}.tgz".format(dt.year, dt.month,dt.day, dt.hour, dt.minute, dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
