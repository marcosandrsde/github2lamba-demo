import json
import datetime

def lambda_handler(event, context):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Versión 2.0 desplegada AUTOMÁTICAMENTE!",
            "timestamp": current_time,
            "version": "v2"
        })
    }
