import urllib.request
import json
import random
import requests

'''API documentation help
#https://zacagross.wordpress.com/2018/05/12/how-to-use-the-metropolitan-museum-of-arts-collection-listing-api/
#https://metmuseum.github.io/#search'''

objectIds = [173439,191545, 653027, 158022, 229155]

def get_advice():
    print("You see the stranger, and he has some advice for you!")
    for objectId in objectIds:
      
      url = f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{objectId}'

  #Different API call urls
  #collection/v1/objects/[objectID] 
  #https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q=french
  #https://collectionapi.metmuseum.org/public/collection/v1/search?q=displayName
  #https://collectionapi.metmuseum.org/public/collection/v1/search?medium=Quilts|Silk|Bedcovers&q=quilt
  #https://collectionapi.metmuseum.org/public/collection/v1/objects/objectID
  #191545
  #dateBegin=1700&dateEnd=1800 

    # r = requests.get(url)
      response = urllib.request.urlopen(url)
      result = json.loads(response.read())
      print('Complete step:' + str(objectId))
      print('He asks you to go to the Museum and check the department ' + result['department'])
      print('and asks you to pick up the ' + result['objectName'])
      print('Its a ' + result['creditLine'])
    
    print('Now you are on your way back to Hotel!!')
