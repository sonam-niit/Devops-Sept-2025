from flask import Flask
from prometheus_client import Counter, generate_latest

app= Flask(__name__) # creating server

#Metrics Counter
REQUEST_COUNT= Counter('http_requests_total','Total HTTP Request')
@app.route("/") # create route
def hello():
    REQUEST_COUNT.inc() # increse count on every req
    return "Hello From Python app"

@app.route("/metrics")
def mectrics():
    return generate_latest(),200,{'content-type':'text/plain'}

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)

# 1 routes localhost:5000/
# 2 routes localhost:5000/metrics