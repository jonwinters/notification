#!/usr/bin/env python3

from PyQt5 import Qt
import sys
import schedule
import time
import fire
from daemon import Daemon

class Notify(object):

    def __init__(self, app, title, content):
        self.app = app
        self.title = title
        self.content = content

    def task(self):
        system_tray_icon = Qt.QSystemTrayIcon(self.app)
        system_tray_icon.show()
        system_tray_icon.showMessage(self.title, self.content)


class Notification(object):

    @staticmethod
    def every(interval, time_unit, content):
        app = Qt.QApplication(sys.argv)
        notify = Notify(app, "Notification", content)
        schedule_timer = schedule.every(interval)
        schedule_timer.unit = time_unit
        schedule_timer.do(notify.task)
        daemon = DaemonSchedule(schedule)
        daemon.start()


class DaemonSchedule(Daemon):

    def __init__ (self,schedule):
        super(DaemonSchedule,self).__init__('/tmp/schedule.pid')
        self.schedule = schedule

    def run(self):
        while True:
            self.schedule.run_pending()
            time.sleep(1)


if __name__ == '__main__':
    fire.Fire(Notification)
