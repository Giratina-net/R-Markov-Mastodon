import schedule
from time import sleep
import gen

gen.run()

def task():
    gen.run()

schedule.every(30).minutes.do(task)

while True:
    schedule.run_pending()
    sleep(1)