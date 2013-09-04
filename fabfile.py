#
# Fabric file for deploying our test node.js application
#
from fabric.api import *


src_directory="/home/rahmanj/node-test/src/"
dest_directory="/srv/node-test/"
target_directory="/srv/"
repo="ssh://git@github.com/jrahman/node-test.git"

@task
def full_deploy():
	execute(deploy_files)
	execute(start_node)
	execute(cleanup)

@task
def start_node():
	sudo("systemctl start nginx.service")
	sudo("systemctl start httpd.service")
	sudo("systemctl enable /srv/node-test/node-test.service")
	sudo("systemctl start node-test.service")

@task
def deploy_files():
	with cd("/tmp"):
		run("rm -rf /tmp/node-test")
		run('ls')
		run("git clone " + repo)
		run("ls node-test/src/")
		sudo("cp node-test/src/node-test.{js,service} " + dest_directory)
		sudo("cp node-test/src/node-test-nginx.conf /etc/nginx/conf.d/")
		sudo("cp node-test/src/node-test-apache.conf /etc/httpd/conf.d/")

@task
def cleanup():
	run("rm -rf /tmp/node-test")



