
import os
import sys
from dateutil.relativedelta import relativedelta
#from dateutil.rrule import *
from datetime import datetime
use_date = datetime(2017,1,1)

tag = "electricvehicles"
max_result = 10000

while use_date < datetime.today():
    next_date = use_date+relativedelta(months=+1)
    start_date = use_date.strftime("%Y-%m-%d")
    end_date = next_date.strftime("%Y-%m-%d")
    file_name = "/home/centos/tweets/" + tag + "/tweet_" + tag + "_" + start_date + "_" + end_date + ".json"
    command = "snscrape --jsonl --max-results " + str(max_result) + " --since " + start_date + " twitter-hashtag \"" + tag + " until:" + end_date + "\"" + " > " + file_name
    use_date = use_date+relativedelta(months=+1)
    os.system(command)
    #os.wait()

