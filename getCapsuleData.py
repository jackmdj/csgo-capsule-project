import requests # make http requests
import json # make sense of what the requests return
import pickle # save our data to our computer

import pandas as pd # structure out data
import numpy as np # do a bit of math

from datetime import datetime # make working with dates 1000x easier 
import time # become time lords
import random # create random numbers (probably not needed)


cookie = {'steamLoginSecure': '76561198132700315%7C%7CFD119E0E286AFECA503579F8380C3CF3DA5A7359'}

CapsuleNames = ['Autograph Capsule | Splyce | MLG Columbus 2016',\
                'Autograph Capsule | Counter Logic Gaming | MLG Columbus 2016',\
                'Autograph Capsule | Gambit Gaming | MLG Columbus 2016',\
                'Autograph Capsule | Flipsid3 Tactics | MLG Columbus 2016',\
                'Autograph Capsule | Team Liquid | MLG Columbus 2016',\
                'Autograph Capsule | mousesports | MLG Columbus 2016',\
                'Autograph Capsule | Cloud9 | MLG Columbus 2016',\
                'Autograph Capsule | G2 Esports | MLG Columbus 2016',\
                'Autograph Capsule | Ninjas in Pyjamas | MLG Columbus 2016',\
                'Autograph Capsule | Natus Vincere | MLG Columbus 2016',\
                'Autograph Capsule | Virtus.Pro | MLG Columbus 2016',\
                'Autograph Capsule | FaZe Clan | MLG Columbus 2016',\
                'Autograph Capsule | Astralis | MLG Columbus 2016',\
                'Autograph Capsule | Team EnVyUs | MLG Columbus 2016',\
                'Autograph Capsule | Fnatic | MLG Columbus 2016',\
                'Autograph Capsule | Luminosity Gaming | MLG Columbus 2016',\
                'Autograph Capsule | OpTic Gaming | Cologne 2016',\
                'Autograph Capsule | Gambit Gaming | Cologne 2016',\
                'Autograph Capsule | Flipsid3 Tactics | Cologne 2016',\
                'Autograph Capsule | mousesports | Cologne 2016',\
                'Autograph Capsule | G2 Esports | Cologne 2016',\
                'Autograph Capsule | FaZe Clan | Cologne 2016',\
                'Autograph Capsule | Team EnVyUs | Cologne 2016',\
                'Autograph Capsule | Team Dignitas | Cologne 2016',\
                'Autograph Capsule | Ninjas in Pyjamas | Cologne 2016',\
                'Autograph Capsule | Counter Logic Gaming | Cologne 2016',\
                'Autograph Capsule | Team Liquid | Cologne 2016',\
                'Autograph Capsule | Natus Vincere | Cologne 2016',\
                'Autograph Capsule | Virtus.Pro | Cologne 2016',\
                'Autograph Capsule | SK Gaming | Cologne 2016',\
                'Autograph Capsule | Astralis | Cologne 2016',\
                'Autograph Capsule | Fnatic | Cologne 2016',\
                'Autograph Capsule | Team EnVyUs | Atlanta 2017',\
                'Autograph Capsule | FaZe Clan | Atlanta 2017',\
                'Autograph Capsule | G2 Esports | Atlanta 2017',\
                'Autograph Capsule | GODSENT | Atlanta 2017',\
                'Autograph Capsule | HellRaisers | Atlanta 2017',\
                'Autograph Capsule | mousesports | Atlanta 2017',\
                'Autograph Capsule | North | Atlanta 2017',\
                'Autograph Capsule | OpTic Gaming | Atlanta 2017',\
                'Autograph Capsule | Astralis | Atlanta 2017',\
                'Autograph Capsule | Flipsid3 Tactics | Atlanta 2017',\
                'Autograph Capsule | Fnatic | Atlanta 2017',\
                'Autograph Capsule | Gambit Gaming | Atlanta 2017',\
                'Autograph Capsule | Natus Vincere | Atlanta 2017',\
                'Autograph Capsule | SK Gaming | Atlanta 2017',\
                'Autograph Capsule | Team Liquid | Atlanta 2017',\
                'Autograph Capsule | Virtus.Pro | Atlanta 2017',\
                'Krakow 2017 Legends Autograph Capsule',\
                'Krakow 2017 Challengers Autograph Capsule',\
                'Boston 2018 Attending Legends Autograph Capsule',\
                'Boston 2018 Minor Challengers with Flash Gaming Autograph Capsule',\
                'Boston 2018 Returning Challengers Autograph Capsule',\
                'London 2018 Returning Challengers Autograph Capsule',\
                'London 2018 Minor Challengers Autograph Capsule',\
                'London 2018 Legends Autograph Capsule',\
                'Katowice 2019 Minor Challengers Autograph Capsule',\
                'Katowice 2019 Legends Autograph Capsule',\
                'Katowice 2019 Returning Challengers Autograph Capsule',\
                'Berlin 2019 Minor Challengers Autograph Capsule',\
                'Berlin 2019 Legends Autograph Capsule',\
                'Berlin 2019 Returning Challengers Autograph Capsule',\
                ]

save = pd.DataFrame(data=None,index=None,columns = ['itemName', 'DateList', 'PriceList'])
counter = 0

for current in CapsuleNames:
    currentHTTP = current.replace(' ','%20') # convert spaces to %20
    capsule = requests.get('https://steamcommunity.com/market/pricehistory/?appid=730&market_hash_name='+currentHTTP, cookies=cookie)
    capsule = capsule.content
    capsule = json.loads(capsule)
    print(str(counter),' out of ',str(len(CapsuleNames)))
    counter += 1
    if capsule: # did we even get any data back
        CapsulePriceData = capsule['prices'] # is there price data?
        if CapsulePriceData == False or not CapsulePriceData: # if there was an issue with the request then data will return false and the for loop will just continue to the next item
            continue               # this could be cause the http item name was weird (eg symbol not converted to ASCII) but it will also occur if you make too many requests too fast (this is handled below)
        else:
            # initialize stuff
            capsulePrices = [] # steam returns MEDIAN price for given time bin
            capsuleVol = []
            capsuleDate = []
            for currDay in CapsulePriceData: # pull out the actual data
                capsulePrices.append(currDay[1]) # idx 1 is price
                capsuleVol.append(currDay[2]) # idx 2 is volume of items sold
                capsuleDate.append(datetime.strptime(currDay[0][0:11], '%b %d %Y')) # idx 0 is the date
                
            # lists are strings, convert to numbers
            capsulePrices = list(map(float, capsulePrices))
            capsuleVol = list(map(int, capsuleVol))
                
            # combine sales that occurs on the same day
            # avg prices, sum volume
            # certainly not the best way to do this but, whatever
            for currDay in range(len(capsuleDate)-1,1,-1): # start from end (-1) and go to start
                if capsuleDate[currDay] == capsuleDate[currDay-1]: # if current element's date same as the one before it
                    capsulePrices[currDay-1] = np.mean([capsulePrices[currDay],capsulePrices[currDay-1]]) # average prices from the two days
                    capsuleVol[currDay-1] = np.sum([capsuleVol[currDay],capsuleVol[currDay-1]]) # sum volume
                    # delete the repeats
                    del capsuleDate[currDay] 
                    del capsuleVol[currDay] 
                    del capsulePrices[currDay]
                
            
            DateList = list(range(0,len(capsulePrices))) # create a new list that "normalizes" days from 0 to n, easier to work with than datetime

            currItemDict = {'itemName':current, 'DateList':[DateList], 'PriceList':[capsulePrices]}
            currItemPD = pd.DataFrame(currItemDict)
            save = save.append(currItemPD,ignore_index=True)

            time.sleep(random.uniform(0.5, 2.5))
    else:
        continue

print('\nPrice Data Collected.\n\nSaving...')

save.to_pickle('CapsulePriceData.pkl')