#!/usr/bin/env python
"""
    run
    ~~~

    Setup config and run application.

    :author: Tosin Damilare James Animashaun (acetakwas@gmail.com)
    :copyright: (c) 2016 by acetakwas
    :license: see LICENSE for details.
"""
# standard library imports
import os, sys#, glob, time

# local imports
from votebot import create_votebot, config as conf

# Get running mode configuration from envvar or use default mode
config_mode = os.getenv('VOTEBOT_CONFIG_MODE', None)
if config_mode is None or config_mode not in ('dev', 'deploy', 'test'):
    print 'Value of environment variable: `VOTEBOT_CONFIG_MODE` not found or invalid!'
    print 'Using default configuration mode...'

config = conf.config_modes.get(config_mode)

# Get slack bot token from envvar
token = config.TOKEN
if token is None:
    print 'Environment variable: `VOTEBOT_TOKEN` not found!'
    print 'Terminating...'
    sys.exit(1)

admin_token = config.ADMIN_TOKEN
if admin_token is None:
    print "Admin token not provided. Bot will not perform 'delete' operations."


if __name__ == '__main__':
    print 'Votebot running...'
    
    #args = sys.argv
    votebot = create_votebot(config)

    # Do we need to setup DB for first time use?
    # db_filename = config.DATABASE_URL[config.DATABASE_URL.rfind('/')+1:]
    # if len(args) > 1 and args[1] == 'setup' or not os.path.exists(db_filename):
    #     # Backup old log files
    #     for f in glob.glob('log*txt'):
    #         try:
    #             os.rename(f, 'backup_logs/{}_{}.txt'.format(f.replace('.txt', ''), '_'.join(time.ctime().replace(':', ' ').split())))
    #         except OSError:
    #             os.mkdir('backup_logs')
    #             os.rename(f, 'backup_logs/{}_{}.txt'.format(f.replace('.txt', ''), '_'.join(time.ctime().replace(':', ' ').split())))

    #     votebot.setup_db()
    #     votebot.load_data()
    #else:
    votebot.load_data()

    # Connect to RTM API and begin listening for events
    votebot.listen()