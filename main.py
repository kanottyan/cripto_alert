from db_helper import insert_event, is_indb
from extract_events import find_all_contetns_on_page, extract_coin_detail
from send_alert import send_alert
import time

if __name__ == '__main__':
    db_name = "./coin_alert.db"
    table = "coinalerts"
    while(True):
        page_num = 1
        url = 'http://coinmarketcal.com/?form%5Bmonth%5D=&form%5Byear%5D=&form%5Bsort_by%5D=created_desc&form%5Bsubmit%5D=&page='
        contents = find_all_contetns_on_page(url, str(page_num))
        print("------Start crawling ... ---------")
        for content in contents:
            details = extract_coin_detail(content)
            if( is_indb(db_name, table, details)):
                print("%s aleady in db ... pass" % details["coin_name"] )
            else:
                print("can't find the event about %s" % details["coin_name"] )
                print("inserting ...")
                insert_event("./coin_alert.db", "coinalerts", details)
                print("Finished insert ...")
                print("calling slack bot ...")
                send_alert(details)
        print("------End crawling: wait 300minutes ---------")
        time.sleep(300)
