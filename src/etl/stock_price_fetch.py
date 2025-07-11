import yfinance as yf
import pandas as pd
import yaml
import boto3 as boto
from datetime import datetime, date, timedelta
import plotly.express as px

def lambda_handler(event=None, context=None):
    config = read_config(config_path='config/config.yaml')
    symbols = config['stocks']['symbols']
    bucket = config['aws']['s3_bucket']
    today = datetime.utcnow().strftime("%Y-%m-%d")
     
    # s3 = boto3.client('s3', region_name=config['aws']['region'])
    combined = pd.DataFrame()

    for symbol in symbols:
        try:
            print(f"Fetching: {symbol}")
            ticker = yf.Ticker(symbol)
            df = ticker.history(period="1d").reset_index()
            json_data = df.to_json(orient="records")

            # s3_key = f"raw/{symbol}/{today}/data.json"
            # s3.put_object(Bucket=bucket, Key=s3_key, Body=json_data)

            # print(f"Uploaded to S3: {s3_key}")
            print(df)
            # print(json_data)
            df_data = yf.Ticker(symbol).history(period="2d", interval="1d").reset_index()
            df_data["Ticker"] = symbol
            combined = pd.concat([combined, df_data], ignore_index=True)

        except Exception as e:
            print(f"Error fetching {symbol}: {e}")
    # plotyly_visuals(combined)

def read_config(config_path='config/config.yaml'):
    """
    Read and parse the YAML configuration file.
    
    Args:
        config_path (str): Path to the configuration file
        
    Returns:
        dict: Configuration as a dictionary
    """
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
            print("Config read succesfully...")
        return config
    except FileNotFoundError:
        print(f"Error: Configuration file not found at {config_path}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML configuration: {e}")
        return None
    
# def plotyly_visuals(df):

#     fig = px.line(
#     df,
#     x="Date",
#     y="Close",
#     color="Ticker",
#     line_shape="spline",
#     markers=True,
#     title="Wave Chart: Stock Movement from Open to Close"
# )

#     fig.update_layout(
#     xaxis_title="Time of Day",
#     yaxis_title="Price",
#     height=500
# ) 
#     fig.show()



lambda_handler()