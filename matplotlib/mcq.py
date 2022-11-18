import re

line = 83.149.9.216 - - [17/Apr/2015:10:05:03 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1"

regex = re.compile("((?:\d{1,3}\.){3}\d{1,3}) - - \[(\d{1,2}/[A-Z][a-z]{2}/\d{4})")

match = re.search(regex,line)

match.group(1)