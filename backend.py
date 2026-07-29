pimport requests

API_KEY = "1f2ff825329394212da6be67359e919a"


def get_data(place,days,option):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    data = requests.get(url)
    data = data.json()

    # filtering  data according to days
    filter_data = data["list"][:days*8]

    #filtering data  according to option
    data = []
    if option == "Temperature":
       for dict in filter_data:
            data.append(dict["main"]["temp"])

    elif option == "Sky":
       for dict in filter_data:
            data.append(dict["weather"][0]["main"])

# filtering dates
    dates = []
    for dict in filter_data:
        dates.append(dict["dt_txt"])

    return  data,dates


if  __name__ == "__main__":
    data,dates= get_data(place="Tokyo",days=2,option="temperature")
    print(data)
    print(dates)
