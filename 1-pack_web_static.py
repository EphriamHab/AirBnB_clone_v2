from fabric import task
from datetime import datetime
import os

@task
def do_pack(c):
    """Generates a .tgz archive from the contents of the web_static folder"""

    # Create the versions folder if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Create the archive file name
    archive_name = "web_static_{}.tgz".format(timestamp)

    # Compress the web_static folder into the archive
    c.local("tar -cvzf versions/{} web_static".format(archive_name))

    # Return the archive path if successfully generated, otherwise None
    return "versions/{}".format(archive_name)

