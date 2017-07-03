import requests
import datetime
j = "http://json.xmltv.se/seriale.tvp.pl_2017-01-13.js.gz"
js = requests.get(j).json()
for p in sorted(js["jsontv"]["programme"], key = lambda p: p["start"]):
    start = datetime.datetime.fromtimestamp(float(p["start"]))
    stop = datetime.datetime.fromtimestamp(float(p["stop"]))
    print("%s %s %s" % (start.strftime("%H:%M"), stop.strftime("%H:%M"), p["title"]["pl"]))