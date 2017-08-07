#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Monitoring program for lab equipment and data analysis

Developed and tested with Python 2.7
'''
# ~~~~~ LOGGING ~~~~~~ #
import os
import log # the app's logging submodule

# set logging globals
script_timestamp = log.timestamp()
scriptdir = os.path.dirname(os.path.realpath(__file__))
scriptname = os.path.basename(__file__)
logdir = os.path.join(scriptdir, 'logs')
logfile = os.path.join(logdir, '{0}.{1}.log'.format(scriptname, script_timestamp))

# reset the 'log' module attrubutes to these globals and create the main file handler for use in other modules
# log.script_timestamp = script_timestamp
# log.scriptdir = scriptdir
# log.scriptname = scriptname
# log.logdir = logdir
# log.main_filehandler = log.create_main_filehandler()

def logpath(scriptname = "monitor"):
    '''
    Return the path to the main log file; needed by the logging.yml
    use this for dynamic output log file paths & names
    '''
    global logfile
    return(log.logpath(logfile = logfile))

# >>>>> add logpaths for other modules HERE <<<<<
def NGS580_demultiplexing_email_logpath():
    '''
    Path for the logs to be sent as the body of the email for NGS580 Demultiplexing
    '''
    global scriptdir
    global script_timestamp
    return(logpath(scriptname = 'NGS580_demultiplexing'))

config_yaml = os.path.join(scriptdir, 'logging.yml')
logger = log.log_setup(config_yaml = config_yaml, logger_name = "monitor")
# logger = log.build_logger(name = 'monitor')
logger.debug("The monitor is starting...")
logger.debug("Path to the monitor's log file: {0}".format(log.logger_filepath(logger = logger, handler_name = "main")))

# ~~~~ PROGRAM LIBRARIES ~~~~~~ #
import config
import tools as t
import find
import qsub
import git
import NGS580_demultiplexing


# ~~~~ FUNCTIONS ~~~~~~ #
def main():
    '''
    Main control function for the program
    '''
    logger.debug("Running the monitor")

    # demo
    find.find(search_dir = '.', pattern = '*.py', num_limit = 3)
    logger.debug("Here is the file handler: {0}".format(log.get_logger_handler(logger = logger, handler_name = "main")))
    # find.find(search_dir = '.', pattern = '*.py')
    # find.find(search_dir = '.', pattern = 't*', level_limit = 1)
    # find.find(search_dir = '.', pattern = 't*', search_type = 'file', level_limit = 2)
    NGS580_demultiplexing.main(extra_filehandlers = [log.get_logger_handler(logger = logger, handler_name = "main")] )


def run():
    '''
    Run the monitoring program
    arg parsing goes here, if program was run as a script
    '''
    main()


# ~~~~~ RUN ~~~~~ #
if __name__ == "__main__":
    run()
