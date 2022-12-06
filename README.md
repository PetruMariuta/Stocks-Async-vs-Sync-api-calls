# Stocks-Async-vs-Sync-api-calls

Stocks api calls, comparison between an Async program and the Sync variant of the program


The programs make  api calls to alphavantage.com in order to obtain the TTM (trailing twelve months, meaning the company's stock performance over the past year), in the image we observe that the async method is approximately 10 times faster, this is due to the fact that the synchronous method makes the api calls one by one waiting for a response before making the next call, while the asynchronous method doesn't need to wait for the answer before making the rest of the calls.


I have also used a time.sleep(40), the program sleeps 40 seconds, this is due to having a basic api key, not allowing multiple api calls for the same companies in a short period of time.


![image](https://user-images.githubusercontent.com/118382269/203395845-e505de53-6b00-469a-b13f-2df50fe757e7.png)
