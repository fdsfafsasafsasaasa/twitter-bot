import tweepy
import speedtest as st
import time

def speedtest():
    speed_test = st.Speedtest()
    speed_test.get_best_server()
    ping = speed_test.results.ping
    download = speed_test.download()
    upload = speed_test.upload()
    download_mbs = round(download / (10**6), 2)
    upload_mbs = round(upload / (10**6), 2)
    return (upload_mbs, download_mbs)

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

# Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    time.sleep(14400)
    result = speedtest()
    if result[0] < 750 or result[1] < 750:
        api.update_status(f'@FrontierCorp: I am paying for gigabit internet speeds. My current speeds are {result[0]}mbps up and  {result[1]}mbps down.')
