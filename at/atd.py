from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger

from datetime import datetime
from datetime import timedelta
import parsedatetime

from subprocess import Popen

import daemon
import daemon.pidfile
import redis


def execute_command(command):
    Popen(command, shell=True)


def main():
    context = daemon.DaemonContext(
        working_directory='/opt/at-scheduler',
        pidfile=daemon.pidfile.PIDLockFile('/var/run/at-scheduler.pid'),
    )

    with context:
        executors = {
            'default': ThreadPoolExecutor(20),
            'processpool': ProcessPoolExecutor(5),
        }

        scheduler = BackgroundScheduler(executors=executors)
        scheduler.add_jobstore(
            'redis',
            jobs_key='at:jobs',
            run_times_key='at:run_times',
        )
        scheduler.start()

        datetime_parser = parsedatetime.Calendar()
        def process(text):
            parsed_tuples = datetime_parser.nlp(text)
            parsed_tuple = parsed_tuples[0]
            dt, flags, start_pos, end_pos, matched_text = parsed_tuple
            remaining_text = text[end_pos:]

            now = datetime.now()
            if dt < now:
                dt += timedelta(days=1)

            trigger = DateTrigger(dt)
            scheduler.add_job(
                execute_command,
                trigger=trigger,
                args=[remaining_text],
            )

        r = redis.Redis()

        while True:
            queue_name, text = r.blpop('at:command-queue')
            try:
                process(text)
            except:
                pass


if __name__ == '__main__':
    main()
