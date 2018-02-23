import socket
import datetime
from flask import Flask

logname = "/mnt/podi.log"
file = open(logname, "a")
file.write(str(datetime.datetime.now()) + " \t/ " + socket.gethostname() + "\n")
file.close()

application = Flask(__name__)


@application.route("/")
def hello():
    file2 = open(logname, "r")
    res = file2.readlines()
    file2.close()
    return "<br>".join(res)


if __name__ == "__main__":
    application.run()
