import json
from tradingview_ta import TA_Handler, Interval

def lambda_handler(event, context):
    body = json.loads(event['body'])
    sym=body["symbol"]
    output= TA_Handler(symbol=sym, screener="India",exchange="NSE",interval="15m")
    indicator_data=output.get_analysis().summary
    
    print(output.get_analysis().summary)
    print(indicator_data)
    
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "executed",
            }
        ),
    }
