#!/usr/bin/env python

from flask.ext.script import Manager
from app import create_app

import subprocess
import os

app = create_app()
manager = Manager(app)


@manager.command
def run():
    """Run in local machine."""

    app.run()


@manager.command
def parser():
    """
    run parser
    :return:
    """
    from app.parser.rss_parser import Parser
    print(Parser.test_method())


def start_uwsgi():
    options = ["uwsgi"]
    options += ['-s', '/tmp/%s.sock' % app.config.get('PROJECT')]
    options += ['--chdir', app.config.get('PROJECT_ROOT')]
    options += ['--home', os.path.join(app.config.get('PROJECT_ROOT'), 'env')]
    options += ['--module', 'wsgi:application']
    options += ['--master']
    options += ['--vacuum']
    options += ['--pidfile', '/tmp/%s.pid' % app.config.get('PROJECT')]
    options += ['--daemonize', os.path.join(app.config.get('LOG_FOLDER'),
                                            'uwsgi.log')]

    subprocess.call(options)


def stop_uwsgi():
    pidfile = '/tmp/%s.pid' % app.config.get('PROJECT')
    with open(pidfile) as f:
        options = ['kill', '-INT', '%s' % f.read().strip()]
        subprocess.call(options)


@manager.command
def uwsgi(option):
    if option == "start":
        start_uwsgi()
    elif option == "stop":
        stop_uwsgi()
    elif option == "restart":
        stop_uwsgi()
        start_uwsgi()


if __name__ == "__main__":
    manager.run()
