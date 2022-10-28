# API Path

##  ```GET```

### ```/election-data```
To get election data for all location.  

**Content type:** application/json  
**Response:** 200 OK  
```js
{
    [
        {
            "location": "string", // Location
            "location_id": 1, // ID of location
            "population": 10000, // population in this location
            "numberOfVoters": 9995, 
            "member_id": 0, // ID of MP
            "nameOfParliament": "", 
            "nameOfParty": "",
            "numberOfVotes": 9995,// The current amount of votes
            "lastUpdatedTime": "" // This request's timing
        },
        {
            "location": "string1", // Location
            "location_id": 2, // ID of location
            "population": 20000, // population in this location
            "numberOfVoters": 18995, 
            "member_id": 0, // ID of MP
            "nameOfParliament": "", 
            "nameOfParty": "",
            "numberOfVotes": 10000,// The current amount of votes
            "lastUpdatedTime": "" // This request's timing
        },
        .
        .
        .
    ]
    
}
```

### ```/election-data/{location-id}```
For get detailed election data in that location.  

**Content type:** application/json  
**Parameters:** location-id  # ID of location  
**Response:** 200 OK  
```js
{
    "location": "string", // Location
    "location_id": 1, // ID of location
    "population": 10000, // population in this location
    "numberOfVoters": 9995, 
    "member_id": 0, // ID of MP
    "nameOfParliament": "", 
    "nameOfParty": "",
    "numberOfVotes": 10000,// The current amount of votes
    "lastUpdatedTime": "" // This request's timing
}
```

## ```PUT```

### ```/election-data/parliament/{location-id}```
To update MP for specific location id.  

**Parameters:** location-id  # ID of location  
**Request body:** application/json  
```js
{
    "location": "string", // Location
    "location_id": 1, // ID of location
    "population": 10000, // population in this location
    "numberOfVoters": 9995, 
    "member_id": 0, // ID of MP
    "nameOfParliament": "", 
    "nameOfParty": "",
    "numberOfVotes": 9900,// The current amount of votes
    "lastUpdatedTime": "" // This request's timing
}

```
**Content type:** application/json  
**Response:** 200 OK  
```js
{
    "location": "string", // Location
    "location_id": 1, // ID of location
    "population": 10000, // population in this location
    "numberOfVoters": 9995, 
    "member_id": 0, // ID of MP
    "nameOfParliament": "string", 
    "nameOfParty": "string",
    "numberOfVotes": 9995,// The current amount of votes
    "lastUpdatedTime": "" // This request's timing
}
```