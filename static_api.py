
from datetime import timedelta
import datetime as dt
import requests


def is_available(date):
    '''
    Returns a BOOL that tells whether the given 
    date is available in the weather forecasts
    '''
    date = dt.datetime.strptime(str(date).split(" ")[0], '%Y-%m-%d')
    min = dt.datetime.now()
    min = dt.datetime.strptime(str(min).split(" ")[0], '%Y-%m-%d')
    max = min + timedelta(days = 5)

    if date >= min:
        if date < max:
            return True
    print('Date not available.') 
    return False



def lat_lon(BASE_URL, API_KEY, CITY):
    '''
    Returns the latitude and longitude of the 
    given city using an API call
    '''

    url_w = BASE_URL + '/weather?'
    url = url_w + 'appid=' + API_KEY + '&q=' + CITY  + '&units=metric' 

    response = requests.get(url).json()
    lat = response['coord']['lat']
    lon = response['coord']['lon']

    return lat, lon



def min_max(BASE_URL, API_KEY, LAT, LON, DATE):
    '''
    Returns the min and max temperature of the
    given city, using an API call.
    '''

    url2 = BASE_URL +'/forecast?lat=' + str(LAT) + '&lon=' + str(LON) + '&appid=' + API_KEY + '&units=metric' 

    #Let's now parse the JSON
    response2 = requests.get(url2).json()

    tmax_list = []
    tmin_list = []

    for i in response2['list']:      
        if i['dt_txt'].startswith(DATE):
            tmax_list.append(i['main']['temp_max'])
            tmin_list.append(i['main']['temp_min'])

    tmin = min(tmin_list)
    tmax = max(tmax_list)
        
    return tmin, tmax





if __name__=='__main__':

    city_name = input('Insert city name: ')
    date = input('Insert date (yyyy-mm-dd): ')

    if is_available(date):
        base_url = 'https://api.openweathermap.org/data/2.5'
        API_KEY = 'f88f7bcd61d31020051c43e8971e7a23'

        lat, lon = lat_lon(base_url, API_KEY, city_name)
        t1, t2 = min_max(base_url, API_KEY, lat, lon, date)

        print("City: ", city_name)
        print("Date: ", date)
        print('Min: ', t1)
        print('Max: ', t2)




