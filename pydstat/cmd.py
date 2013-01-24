#!/usr/bin/env python
"""pydstat CLI Client.

Source:: https://github.com/ampledata/pydstat
"""

__author__ = 'Greg Albrecht <gba@splunk.com>'
__copyright__ = 'Copyright 2012 Splunk, Inc.'
__license__ = 'Apache License 2.0'

import optparse
import pydstat
import sys


def main():
    """Main loop.

    If you don't specify a PID we'll stat them all.
    If you specify a PID, we'll just stat that one.
    """
    proc_id = None
    interval = None
    frequency = None

    #explains the use of this option/argument parser
    use = "Usage: %prog [options] processID interval frequency"

    parser = optparse.OptionParser(usage=use)

    parser.add_option('-p',
                      '--proc_id',
                      dest='proc_id',
                      help='Process ID')

    parser.add_option('-i',
                      '--interval',
                      dest='interval',
                      help='Time interval of screenshot.',
                      type=int)

    parser.add_option('-f',
                      '--frequency',
                      dest='frequency',
                      help='Times the script will run. 1 by default',
                      type=int)

    (options, args) = parser.parse_args()

    proc_id = options.proc_id
    if proc_id is None:
        proc_id = "ALL"

    interval = options.interval
    if interval is None:
        interval = 1

    frequency = options.frequency
    if frequency is None:
        frequency = 1

    #create object
    pyds = pydstat.PydStat()

    #Get Statistics. Three arguments : process ID, interval and frequency
    pyds.get_stats(proc_id, interval, frequency)

    #parse and log statistics
    pyds.parse_stats()
    pyds.log_stats()

if __name__ == '__main__':
    sys.exit(main())
