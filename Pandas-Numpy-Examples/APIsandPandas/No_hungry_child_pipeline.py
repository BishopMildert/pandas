import pandas as pd
import io
import requests

# getting spreadsheet data from Google Drive
url = 'https://docs.google.com/spreadsheets/d/1RpbEmNeN97pRTmT_S2t6yhQo-5__dR3g2x873r26ct4/export?gid=0&format=csv'


req = requests.get(url).content
# creating a Dataframe with all the google sheet
df = pd.read_csv((io.StringIO(req.decode('utf-8'))))

# Formating the data with the relevant columns
df_data = df[['Org Name', 'Town', 'Postcode']].dropna()


# Function to get Lat & Lng from api using postcode
def get_lat_lgn(postcode):
    lat, lng = None, None
    base_url = "http://api.getthedata.com/postcode/"
    endpoint = base_url + postcode

    r = requests.get(endpoint)
    if r.status_code not in range(200, 299):
        return None, None
    try:
        #         try method to handle wrogn response
        results = r.json()
        lat = results['data']['latitude']
        lng = results['data']['longitude']
    except:
        pass
    return lat, lng

# pushing the data into the dataframe
def add_geocode_data(row):
    column_name = 'Postcode'
    postcode_data = row[column_name]
    postcode_lat, postcode_lng = get_lat_lgn(postcode_data)
    row['lat'] = postcode_lat
    row['lng'] = postcode_lng
    return row

# copy of our formated DF
x = df_data.copy()

# DF with the Lat & Lgn Data
new_df = x.apply(add_geocode_data, axis=1)

# Exporting the DF to a CSV file 

new_df.to_csv('data_location.csv')
