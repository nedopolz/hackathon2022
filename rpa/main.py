from datetime import datetime
import time
import logging
from apscheduler.schedulers.background import BackgroundScheduler

from robots.price_parser import parse_price

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(parse_price, 'interval', hours=1)
    scheduler.start()
    logging.debug(f'time:{datetime.now()}, task:price_parser, status:started')

    try:
        while True:
            time.sleep(10)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()