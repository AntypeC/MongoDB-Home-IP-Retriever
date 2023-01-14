import pymongo
from requests import get
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

client = pymongo.MongoClient("mongodb+srv://AntypeC:xRMeoD71DVtkKVqU@cluster0.q4nte6p.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("ipaddr")
collection = db.get_collection("storage")

collection.insert_one({
    "time": str(datetime.datetime.now()), "ip": get('https://api.ipify.org').text
})

def get_ip():
    ip = get('https://api.ipify.org').text
    time = str(datetime.datetime.now())
    collection.update_one({
        {"time": time, "ip": ip}
    })

scheduler = BlockingScheduler()
scheduler.add_job(get_ip, 'interval', hours=2)
scheduler.start()