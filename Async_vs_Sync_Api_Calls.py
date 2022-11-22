import os
import time
import requests
import time
import asyncio
import aiohttp
import platform


api_key=os.getenv("alphavantage_key")
stocks=["IBM","GOOG","AAPL","TSLA"]
url="https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}"

start=time.time()
results=[]

def get_tasks1(session):
    tasks=[]
    for stock in stocks:
        tasks.append(asyncio.create_task(session.get(url.format(stock, api_key), ssl=False)))
    return tasks


async def get_stock_new_loop2():
    async with aiohttp.ClientSession() as session:
        tasks=get_tasks1(session)
        responses = await asyncio.gather(*tasks) # * refferences the list, makes every api call
        i=0
        for response in responses:
            
            results.append(await response.json())
            x=results[i] 
            i+=1
            print (x["Symbol"]," RevenuePerShareTTM = ",x["RevenuePerShareTTM"],x["Currency"])     
    #session.close() not need since we use "with" statement

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(get_stock_new_loop2()) #use a new loop
    

end=time.time()
print(f"Job done asynchronously in {end-start} seconds")

time.sleep(40)

stocks=["IBM","GOOG","AAPL","TSLA"]
url="https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}"

start=time.time()

for stock in stocks:
    
    request=requests.get(url.format(stock, api_key))
    data=request.json()
    print (f"{stock} RevenuePerShareTTM = ", data["RevenuePerShareTTM"], data["Currency"])


end=time.time()
print(f"Job done synchronously in {end-start} seconds")

