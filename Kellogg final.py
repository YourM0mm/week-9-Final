import requests
#make a call to website and retrieve data. reference openweathermap.org
def get_web_data(zip=None, city=None):
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?units=imperial"
    #add API id
    apiid= "5cea5abaf21b5253ae99a8bda30bb09e"
    #check is user provides zip code or city
    if zip is not None:
        baseUrl += "&zip="+str(zip)+",us"
    else:
        baseUrl += "&q="+str(city)+",us"
        #append the api id 
    baseUrl += "&appid="+str(apiid)
    #get request using request mod
    r = requests.get(baseUrl)
    return r
#show in readable format
def display(resp):
    if resp.status_code ==200:
        data = resp.json()
        print(f"""{data['name']} Weather Forecast:
        Type: {data['weather'][0]['description']}
        Wind Speed : {data['wind']['speed']} miles/hr
        Visibility : {data['visibility']} m
        Min. Temp : {data['main']['temp_min']} F
        Max Temp : {data['main']['temp_max']} F
        """)
    else:
        print("Request Failed. : ", resp.status_code)
#provide main function
def main():
    while True:
        #ask for user input
        choice = int(input("Which method would you like to use ? :\n1. Zip Code\n2. City Name\n3. Exit program\n"))
        if choice == 1:
            #request zip
            try:
                zCode = int(input("Enter zip code : "))
                resp = get_web_data(zCode, None)
                display(resp)
            except Exception as ex:
                print("Error : ", ex)
        elif choice == 2:
            try:
                cname = input("Enter city name : ")
                resp = get_web_data(None, cname)
                display(resp)
            except Exception as ex:
                print("Error : ", ex)
        elif choice == 3:
            print("Thank you for using Weather2020. Connection terminated.")
            break
        else:
            print("Invalid Choice..\n")

    
#welcome/connection message using time. reference https://stackoverflow.com/questions/510348/how-can-i-make-a-time-delay-in-python
import time
print("Connecting to weather host.") 
time.sleep(4)
print("...") 
time.sleep(2)
print("Connection Established") 
time.sleep(.50)
print("Welcome to Weather2020!")
print("-------------------------")

if __name__ == "__main__":
    main()
                
                
                
                
                