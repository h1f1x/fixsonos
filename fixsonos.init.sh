#!/bin/sh

### BEGIN INIT INFO
# Provides:          fixsonos
# Required-Start:
# Required-Stop:     
# Should-Stop:       
# Default-Start:     4 5
# Default-Stop:      0 6
# Short-Description: 
### END INIT INFO

fixsonos()
{
    [ ! -x /opt/fixsonos ] && return 0

    . /lib/lsb/init-functions
    verbose_log_action_msg() { [ "$VERBOSE" = no ] || log_action_msg "$@"; }

    case "$1" in
        start)
            (cd /opt/fixsonos; pipenv run python index.py)  
            ;;
        stop|restart|reload|force-reload)
            log_action_msg "No action here"
            ;;
    esac
}

fixsonos "$@"
