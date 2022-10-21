# API Path

##  ```GET```

### ```/election-data```
To get election data for all location.  

Content type: application/json  
Response: 200 OK  
```js
[
    {
        "location": string,#เขตพื้นที่
        "location_id": number, 
        "population": number,#จำนวนคนในเขต
        "numberOfVoters": number,#จำนวนของคนที่มีสิทธิ์Vote
        "member_id": number,#id of MP
        "nameOfParliament": string,# name of MP
        "nameOfParty":string,
        "numberOfVotes":number,#จำนวนคนที่ Vote ณ การ request นี้
        "lastUpdatedTime": string *** #เวลา ณ การrequest
    },
    {
        "location": string,#เขตพื้นที่
        "location_id": number, 
        "population": number,#จำนวนคนในเขต
        "numberOfVoters": number,#จำนวนของคนที่มีสิทธิ์Vote
        "member_id": number,#id of MP
        "nameOfParliament": string,# name of MP
        "nameOfParty":string,
        "numberOfVotes":number,#จำนวนคนที่ Vote ณ การ request นี้
        "lastUpdatedTime": string *** #เวลา ณ การrequest
    },
    .
    .
    .
]
```

### ```/election-data/{location-id}```
For get detailed election data in that location.  

Content type: application/json  
Parameters: location-id  # ID of location  
Response: 200 OK  
```js
{
    "location": string,	#  เขตพื้นที่
    "location_id": number, 
    "population": number, # จำนวนคนในเขต
    "numberOfVoters": number,  # จำนวนของคนที่มีสิทธิ์ Vote
    "member_id": number, # id of MP
    "nameOfParliament": string, # name of MP
    "nameOfParty": string,
    "numberOfVotes": number, # จำนวนคนที่Vote ณ การ request นี้
    "lastUpdatedTime": string *** # เวลา ณ การrequest
}
```


### ```/voter/validation/{citizen_id}```
To get status if citizen have right to vote or not.  

Parameters: citizen_id    
Content type: application/json    
Response: 200 OK    
```js
{
    "nameOfVoter": string, 
    "citizenID":  number, 
    "voteStatus": boolean, # โหวตแล้ว true ยังไม่ได้โหวต false
    "location" string: ,
    "RightToVote" : string, # มีสิทธิ์ true ไม่มี false
    "CitizenCVV" : number   #เลขหลังบัตรประชาชน ใช้ยืนยันตัวตน
}
```

## ```PUT```

### ```/election-data/parliament/{location-id}```
To update MP for specific location id.  

Parameters: location-id  # ID of location  
Request body: application/json  
```js
{
     "location":string,	#  เขตพื้นที่
     "location_id": number, 
     "population": number, # จำนวนคนในเขต
     "numberOfVoters": number,  # จำนวนของคนที่มีสิทธิ์ Vote
     "member_id": number, # id of MP
     "nameOfParliament": string, # name of MP
     "nameOfParty": string,
     "numberOfVotes": number, # จำนวนคนที่Vote ณ การ request นี้
     "lastUpdatedTime": string *** # เวลา ณ การrequest
}

```
Content type: application/json  
Response: 200 OK  
```js
{
     "location":string,	#  เขตพื้นที่
     "location_id": number, 
     "population": number, # จำนวนคนในเขต
     "numberOfVoters": number,  # จำนวนของคนที่มีสิทธิ์ Vote
     "member_id": number, # id of MP
     "nameOfParliament": string, # name of MP
     "nameOfParty": string,
     "numberOfVotes": number, # จำนวนคนที่Vote ณ การ request นี้
     "lastUpdatedTime": string *** # เวลา ณ การrequest
}
```