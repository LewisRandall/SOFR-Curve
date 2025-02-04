import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import requests

#################################################################
#MONEY MARKET DATA IMPORT (FED)
#################################################################

api_key = ""
url = f"https://api.stlouisfed.org/fred/series/observations?series_id=SOFR&api_key={api_key}&file_type=json"
response = requests.get(url)
data = response.json()
observations = data['observations']
sofr_df = pd.DataFrame(observations)
sofr_df = sofr_df[['date', 'value']]
sofr_df['date'] = pd.to_datetime(sofr_df['date'])
sofr_df['value'] = pd.to_numeric(sofr_df['value'], errors='coerce')

sofr_df = sofr_df["value"].iloc[-1]
sofr_df = pd.DataFrame([sofr_df], columns = ["Rate"])
sofr_df["Ticker"] = ["F,25"]
sofr_df.set_index("Ticker", inplace = True)
sofr_df.rename_axis("TERM", inplace= True)
M22025MM = sofr_df

#################################################################
#FUTURES DATA IMPORT (YAHOO)
#################################################################

Q12025 = yf.download("SR3h25.CME", period = '1d') #3m mar 20 2025
Q22025 = yf.download("SR3m25.CME", period = '1d') #3m jun 20 2025
Q32025 = yf.download("SR3u25.CME", period = '1d') #3m Sep 20 2025
Q42025 = yf.download("SR3z25.CME", period = '1d') #3m Dec 20 2025

Q12026 = yf.download("SR3h26.CME", period = '1d') #3m mar 20 2026
Q22026 = yf.download("SR3m26.CME", period = '1d') #3m jun 20 2026
Q32026 = yf.download("SR3u26.CME", period = '1d') #3m Sep 20 2026
Q42026 = yf.download("SR3z26.CME", period = '1d') #3m Dec 20 2026

Q12027 = yf.download("SR3h27.CME", period = '1d') #3m mar 20 2027
Q22027 = yf.download("SR3m27.CME", period = '1d') #3m jun 20 2027
Q32027 = yf.download("SR3u27.CME", period = '1d') #3m Sep 20 2027
Q42027 = yf.download("SR3z27.CME", period = '1d') #3m Dec 20 2027

Q12028 = yf.download("SR3h28.CME", period = '1d') #3m mar 20 2028
Q22028 = yf.download("SR3m28.CME", period = '1d') #3m jun 20 2028
Q32028 = yf.download("SR3u28.CME", period = '1d') #3m Sep 20 2028
Q42028 = yf.download("SR3z28.CME", period = '1d') #3m Dec 20 2028

Q12029 = yf.download("SR3h29.CME", period = '1d') #3m mar 20 2029
Q22029 = yf.download("SR3m29.CME", period = '1d') #3m jun 20 2029
Q32029 = yf.download("SR3u29.CME", period = '1d') #3m Sep 20 2029
Q42029 = yf.download("SR3z29.CME", period = '1d') #3m Dec 20 2029

Q12030 = yf.download("SR3h30.CME", period = '1d') #3m mar 20 2030
Q22030 = yf.download("SR3m30.CME", period = '1d') #3m jun 20 2030
Q32030 = yf.download("SR3u30.CME", period = '1d') #3m Sep 20 2030
Q42030 = yf.download("SR3z30.CME", period = '1d') #3m Dec 20 2030

#Q12031 = yf.download("SR3h31.CME", period = '5d') #3m mar 20 2031
#Q22031 = yf.download("SR3m31.CME", period = '5d') #3m jun 20 2031
#Q32031 = yf.download("SR3u31.CME", period = '5d') #3m Sep 20 2031
#Q42031 = yf.download("SR3z31.CME", period = '5d') #3m Dec 20 2031

#Q12032 = yf.download("SR3h32.CME", period = '1d') #3m mar 20 2032
#Q22032 = yf.download("SR3m32.CME", period = '1d') #3m jun 20 2032
#Q32032 = yf.download("SR3u32.CME", period = '1d') #3m Sep 20 2032
#Q42032 = yf.download("SR3z32.CME", period = '1d') #3m Dec 20 2032

#Q12033 = yf.download("SR3h33.CME", period = '1d') #3m mar 20 2033
#Q22033 = yf.download("SR3m33.CME", period = '1d') #3m jun 20 2033
#Q32033 = yf.download("SR3u33.CME", period = '1d') #3m Sep 20 2033
#Q42033 = yf.download("SR3z33.CME", period = '1d') #3m Dec 20 2033

#Q12034 = yf.download("SR3h34.CME", period = '1d') #3m mar 20 2034
#Q22034 = yf.download("SR3m34.CME", period = '1d') #3m jun 20 2034
#Q32034 = yf.download("SR3u34.CME", period = '1d') #3m Sep 20 2034
#Q42034 = yf.download("SR3z34.CME", period = '1d') #3m Dec 20 2034

#################################################################
#FUTURES DATA FORMATTING
#################################################################

#2025

Q12025df = pd.DataFrame(Q12025["Close"])
Q12025df["Price"] = Q12025df['SR3H25.CME']
Q12025df.index = ["M,25"]
Q12025df= Q12025df.drop(columns = ['SR3H25.CME'])

Q22025df = pd.DataFrame(Q22025["Close"])
Q22025df["Price"] = Q22025df['SR3M25.CME']
Q22025df.index = ["J,25"]
Q22025df= Q22025df.drop(columns = ['SR3M25.CME'])

Q32025df = pd.DataFrame(Q32025["Close"])
Q32025df["Price"] = Q32025df['SR3U25.CME']
Q32025df.index = ["S,25"]
Q32025df= Q32025df.drop(columns = ['SR3U25.CME'])

Q42025df = pd.DataFrame(Q42025["Close"])
Q42025df["Price"] = Q42025df['SR3Z25.CME']
Q42025df.index = ["D,25"]
Q42025df= Q42025df.drop(columns = ['SR3Z25.CME'])

#2026

Q12026df = pd.DataFrame(Q12026["Close"])
Q12026df["Price"] = Q12026df['SR3H26.CME']
Q12026df.index = ["M,26"]
Q12026df= Q12026df.drop(columns = ['SR3H26.CME'])

Q22026df = pd.DataFrame(Q22026["Close"])
Q22026df["Price"] = Q22026df['SR3M26.CME']
Q22026df.index = ["J,26"]
Q22026df= Q22026df.drop(columns = ['SR3M26.CME'])

Q32026df = pd.DataFrame(Q32026["Close"])
Q32026df["Price"] = Q32026df['SR3U26.CME']
Q32026df.index = ["S,26"]
Q32026df= Q32026df.drop(columns = ['SR3U26.CME'])

Q42026df = pd.DataFrame(Q42026["Close"])
Q42026df["Price"] = Q42026df['SR3Z26.CME']
Q42026df.index = ["D,26"]
Q42026df= Q42026df.drop(columns = ['SR3Z26.CME'])

#2027

Q12027df = pd.DataFrame(Q12027["Close"])
Q12027df["Price"] = Q12027df['SR3H27.CME']
Q12027df.index = ["M,27"]
Q12027df= Q12027df.drop(columns = ['SR3H27.CME'])

Q22027df = pd.DataFrame(Q22027["Close"])
Q22027df["Price"] = Q22027df['SR3M27.CME']
Q22027df.index = ["J,27"]
Q22027df= Q22027df.drop(columns = ['SR3M27.CME'])

Q32027df = pd.DataFrame(Q32027["Close"])
Q32027df["Price"] = Q32027df['SR3U27.CME']
Q32027df.index = ["S,27"]
Q32027df= Q32027df.drop(columns = ['SR3U27.CME'])

Q42027df = pd.DataFrame(Q42027["Close"])
Q42027df["Price"] = Q42027df['SR3Z27.CME']
Q42027df.index = ["D,27"]
Q42027df= Q42027df.drop(columns = ['SR3Z27.CME'])

#2028

Q12028df = pd.DataFrame(Q12028["Close"])
Q12028df["Price"] = Q12028df['SR3H28.CME']
Q12028df.index = ["M,28"]
Q12028df= Q12028df.drop(columns = ['SR3H28.CME'])

Q22028df = pd.DataFrame(Q22028["Close"])
Q22028df["Price"] = Q22028df['SR3M28.CME']
Q22028df.index = ["J,28"]
Q22028df= Q22028df.drop(columns = ['SR3M28.CME'])

Q32028df = pd.DataFrame(Q32028["Close"])
Q32028df["Price"] = Q32028df['SR3U28.CME']
Q32028df.index = ["S,28"]
Q32028df= Q32028df.drop(columns = ['SR3U28.CME'])

Q42028df = pd.DataFrame(Q42028["Close"])
Q42028df["Price"] = Q42028df['SR3Z28.CME']
Q42028df.index = ["D,28"]
Q42028df= Q42028df.drop(columns = ['SR3Z28.CME'])

#2029

Q12029df = pd.DataFrame(Q12029["Close"])
Q12029df["Price"] = Q12029df['SR3H29.CME']
Q12029df.index = ["M,29"]
Q12029df= Q12029df.drop(columns = ['SR3H29.CME'])

Q22029df = pd.DataFrame(Q22029["Close"])
Q22029df["Price"] = Q22029df['SR3M29.CME']
Q22029df.index = ["J,29"]
Q22029df= Q22029df.drop(columns = ['SR3M29.CME'])

Q32029df = pd.DataFrame(Q32029["Close"])
Q32029df["Price"] = Q32029df['SR3U29.CME']
Q32029df.index = ["S,29"]
Q32029df= Q32029df.drop(columns = ['SR3U29.CME'])

Q42029df = pd.DataFrame(Q42029["Close"])
Q42029df["Price"] = Q42029df['SR3Z29.CME']
Q42029df.index = ["D,29"]
Q42029df= Q42029df.drop(columns = ['SR3Z29.CME'])

#2030

Q12030df = pd.DataFrame(Q12030["Close"])
Q12030df["Price"] = Q12030df['SR3H30.CME']
Q12030df.index = ["M,30"]
Q12030df= Q12030df.drop(columns = ['SR3H30.CME'])

Q22030df = pd.DataFrame(Q22030["Close"])
Q22030df["Price"] = Q22030df['SR3M30.CME']
Q22030df.index = ["J,30"]
Q22030df= Q22030df.drop(columns = ['SR3M30.CME'])

Q32030df = pd.DataFrame(Q32030["Close"])
Q32030df["Price"] = Q32030df['SR3U30.CME']
Q32030df.index = ["S,30"]
Q32030df= Q32030df.drop(columns = ['SR3U30.CME'])

Q42030df = pd.DataFrame(Q42030["Close"])
Q42030df["Price"] = Q42030df['SR3Z30.CME']
Q42030df.index = ["D,30"]
Q42030df= Q42030df.drop(columns = ['SR3Z30.CME'])

#Not Enough Liquidity YET

#Q12031df = pd.DataFrame(Q12031["Close"])
#Q22031df = pd.DataFrame(Q22031["Close"])
#Q32031df = pd.DataFrame(Q32031["Close"])
#Q42031df = pd.DataFrame(Q42031["Close"])

#Q12032df = pd.DataFrame(Q12032["Close"])
#Q22032df = pd.DataFrame(Q22032["Close"])
#Q32032df = pd.DataFrame(Q32032["Close"])
#Q42032df = pd.DataFrame(Q42032["Close"])

#Q12033df = pd.DataFrame(Q12033["Close"])
#Q22033df = pd.DataFrame(Q22033["Close"])
#Q32033df = pd.DataFrame(Q32033["Close"])
#Q42033df = pd.DataFrame(Q42033["Close"])

#Q12034df = pd.DataFrame(Q12034["Close"])
#Q22034df = pd.DataFrame(Q22034["Close"])
#Q32034df = pd.DataFrame(Q32034["Close"])
#Q42034df = pd.DataFrame(Q42034["Close"])

#################################################################
#DATA CONCATENATION & FORMATTING
#################################################################

sofr_data = pd.concat([Q12025df,Q22025df,Q32025df,Q42025df,
                  Q12026df,Q22026df,Q32026df,Q42026df,
                  Q12027df, Q22027df, Q32027df, Q42027df,
                  Q12028df, Q22028df, Q32028df, Q42028df,
                  Q12029df, Q22029df, Q32029df, Q42029df,
                  Q12030df, Q22030df, Q32030df, Q42030df], axis = 0)

sofr_data["Rate"] = abs(sofr_data["Price"] - 100)
sofr_data = sofr_data["Rate"]
sofr_data.rename_axis("Expiry", inplace= True)
sofr_data = pd.concat([M22025MM, sofr_data], axis = 0)

#################################################################
#CURVE PLOT
#################################################################

print(sofr_data)
plt.figure(figsize=(10, 5))
plt.plot(sofr_data.index, sofr_data["Rate"])
plt.title('SOFR Curve')
plt.xlabel('Expiry')
plt.ylabel('Price')
plt.show()

