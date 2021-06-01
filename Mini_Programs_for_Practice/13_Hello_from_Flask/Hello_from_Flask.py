from flask import Flask

app = Flask(__name__)


# create some routes
# use the decorator to associate the wrapper function to the function that is being decorated at call time
# the slash (/) here means the home page
@app.route("/")
def index():
    return "Hello from Flask"


# block this program here and run the application at this IP address until stop it
# app.run(host="0.0.0.0")
# in the context of servers, 0.0.0.0 means all IPv4 addresses on the local machine
# the port default is 5000
# this application is running on 0.0.0.0:8500, 127.0.0.1:8500, localhost:8500, and (the IP address of the Raspberry Pi):8500
app.run(host="0.0.0.0", port=8500)
