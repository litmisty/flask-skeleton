from fabric.api import *

project = "flask_skeleton"

env.user = 'user'
env.hosts = ['server.com']
env.use_ssh_config = True


def d():
    """
    deploy
    """
    with cd("/home/mimu/dev/fskel"):
        run("git pull origin master")

        with prefix('source /home/mimu/dev/fskel/env/bin/activate'):
            run("pip install -r /home/mimu/dev/fskel/r.txt -q")
            run("python manage.py -c app/deploy_config.py db upgrade")
            run("python manage.py -c app/deploy_config.py uwsgi restart")
