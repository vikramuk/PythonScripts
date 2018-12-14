# Python program to find live train  
# status using RAILWAY API 
#https://www.geeksforgeeks.org/python-find-live-running-status-pnr-of-any-train-using-railway-api/  
# import required modules 
import requests , json 
  
# enter your api key here 
api_key = "Your_API_Key"
  
# base_url variable to store url 
base_url = "https://api.railwayapi.com/v2/live/train/"
  
# enter train_number here 
train_number = "12056"
  
# enter current date in dd-mm-yyyy format 
current_date = "20-06-2018"
  
# complete_url variable to 
# store complete url address 
complete_url = base_url + train_number + "/date/" + current_date + "/apikey/" + api_key + "/"
  
# get method of requests module 
# return response object 
response_ob = requests.get(complete_url) 
  
# json method of response object convert 
# json format data into python format data 
result = response_ob.json() 
  
# Now result contains list of nested dictionaries 
# Check the value of "response_code" key is equal 
# to "200" or not if equal that means record is  
# found otherwise record is not found 
if result["response_code"] == 200 : 
  
    # train name is extracting from 
    # the result variable data      
    train_name = result["train"]["name"] 
  
    # store the value or data of 
    # "route" key in variable y 
    y = result["route"] 
  
    # source station name is extracting 
    # from the y variable data 
    source_station = y[0]["station"]["name"] 
  
    # destination station name is 
    # extracting from the y varibale data 
    destination_station = y[len(y)-1]["station"]["name"] 
      
    # store the value of "position" 
    # key in variable position 
    position = result["position"] 
  
    # print following values 
    print(" train name : " + str(train_name) 
        + "\n source station : " + str(source_station) 
        + "\n destination station : "+ str(destination_station) 
        + "\n current status : " + str(position) ) 
      
else : 
    print("record is not found for given request") 
