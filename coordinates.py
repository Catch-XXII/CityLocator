import webbrowser

path_to_browser = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

city = input("Enter a city name: ").title()

cit_coor = [("New York", 40.712776, -74.005974),("Moscow",55.755825, 37.617298),("Paris", 48.856613, 2.352222 ),
            ("Madrid", 40.416775, -3.703790 ),("Berlin", 52.520008, 13.404954),("Istanbul", 41.008240, 28.978359),
            ("Kiev", 50.450100, 30.523399), ("Erzincan", 39.751221, 39.489559)]


for i in range(len(cit_coor)):
    if cit_coor[i][0] == city:
        webbrowser.get(path_to_browser).open("""https://www.google.com/maps/place/{}+{}""".format(cit_coor[i][1], cit_coor[i][2]))
        break
else:
    lat = input("Latitude: ")
    long = input("Longitude: ")
    webbrowser.get(path_to_browser).open("""https://www.google.com/maps/place/{}+{}""".format(lat, long))
