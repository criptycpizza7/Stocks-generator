from contextlib import closing
import signal, sys, random
from time import sleep
import grpc
import stocks_pb2
import stocks_pb2_grpc


import psycopg2
from psycopg2.extras import DictCursor

exit = True

def signal_handler(signal, frame):
    global exit
    exit = False


while exit:
    with grpc.insecure_channel('localhost:7000') as channel:
        stub = stocks_pb2_grpc.send_stocksStub(channel=channel)
        with closing(psycopg2.connect(dbname='kursach_db', user='kursach_dbuser', password='asdf', host='localhost')) as connection:
            with connection.cursor(cursor_factory=DictCursor) as cursor:
                signal.signal(signal.SIGINT, signal_handler)
                cursor.execute('select id from kursach_app_company')
                ids = cursor.fetchall()

                records = []
                for item in ids:
                    cursor.execute('select price, company_id from kursach_app_stocks where company_id = %s order by "time" desc limit 1', str(item[0]))
                    records += cursor.fetchall()

                insert_request = 'insert into kursach_app_stocks ("time", price, change_percent, company_id) values(now(), %s, %s, %s)'
                data_to_insert = []
                for item in records:
                    change_percent = random.triangular(-0.05, 0.07, 0.01) + 1
                    new_data = (round(item['price'] * change_percent, 2), round(change_percent - 1, 4), item['company_id'])
                    data_to_insert.append(new_data)
                                
                cursor.executemany(insert_request, data_to_insert)
                connection.commit()

                records = []

                for item in ids:
                    cursor.execute('select * from kursach_app_stocks where company_id = %s order by "time" desc limit 1', str(item[0]))
                    records += cursor.fetchall()
                
                print(records)

                data_to_insert = []
                for item in records:
                    new_data = {}

                    new_data["id"] = item['id']
                    new_data["company"] = item['company_id']
                    new_data["price"] = item['price']
                    new_data["change_percent"] = item['change_percent']
                    new_data["time"] = str(item['time'])

                    data_to_insert.append(new_data)

                response = stub.sendStocks(stocks_pb2.stocks(data=data_to_insert))

        sleep(2)

    
print('exit')
sys.exit(0)