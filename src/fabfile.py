#
# Fabric file for deploying our test node.js application
#
from fabric.api import *

src_directory="/home/rahmanj/node-test/src/"
dest_directory="/srv/node-test/"

@task
def start_node():
	sudo("systemctl start node-test.service")

@task
def copy_application():
	cd(dest_directory)
	sudo("cp " .  src_directory . "node-test.js " . dest_directory)

@task



