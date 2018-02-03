from PyQt5 import Qt
import sys
import schedule
import time
import fire


class Notify(object):

    def __init__(self, app, title, content):
        self.app = app
        self.title = title
        self.content = content

    def job(self):
        systemtray_icon = Qt.QSystemTrayIcon(self.app)
        systemtray_icon.show()
        systemtray_icon.showMessage(self.title, self.content)


class Notification(object):

    def every(self, second, content):
        app = Qt.QApplication(sys.argv)
        notify = Notify(app, "Notification", content)
        schedule.every(second).seconds.do(notify.job)
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == '__main__':
    fire.Fire(Notification)
