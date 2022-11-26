# API Path

## Base url

### ```/api/v1```

##  ```GET```

### ```/population```
Get the population data

**Content type:** application/json  
**Response:** 200 OK

```js
{
    [
        {
            "citizenID": 1234567898765, // Citizen ID
            "title": "Ms.", // Person's title
            "firstName": "Achara", // First name
            "lastName": "Sukkasem", // Last name
            "sex": "Female", // Gender
            "locationID": 231, // Location ID 
            "rightToVote": true, // The person have a right to vote or not
            "blackList": false // The person have a right to be MP or not
        },
        {
            "citizenID": 4569871354123,
            "title": "Mr.",
            "firstName": "Anuman",
            "lastName": "Saengthong",
            "sex": "Male",
            "locationID": 557,
            "rightToVote": true,
            "blackList": false
        },
        .
        .
        .
    ]
}
```

### ```/location```
To get all information about election of all district  

**Content type:** application/json  
**Response:** 200 OK  
```js
{
    [
        {
            "locationID": 1, // ID of location
            "location": "Amphawa", // Location
            "population": 10000, // Population in this location
            "numberOfVoters": 9995 // Amount of who have right to vote
        },
        {
            "locationID": 2,
            "location": "Bang Len",
            "population": 20000,
            "numberOfVoters": 18995
        },
        .
        .
        .
    ]
    
}
```

### ```/election-result```
For get detailed election data of all location.  

**Content type:** application/json  
**Response:** 200 OK  

```js
{
    [
        {
            "district": "Amphawa", // District
            "districtTH": "อัมพวา", // District in Thai language
            "province": "Samut Songkhram", // Province
            "provinceTH": "สมุทรปราการ", // Province in Thai language
            "region": "centre", // Region
            "nameOfParliament": "Jakarin Chujan", // Parliament name
            "nameOfParty": "Catnip" // Party that parliament are with
        },
        {
            "district": "Bang Len",
            "districtTH": "บางเลน",
            "province": "Phichit",
            "provinceTH": "พิจิตร",
            "region": "centre",
            "nameOfParliament": "Chananya Photan",
            "nameOfParty": "Catnip"
        },
        .
        .
        .
    ]
}
```

## ```POST```

### ```/election-result```
To update the election detail.  

**Request body:** application/json  
**Response:** 200 OK  

```js
{
    [
        {
            "locationID": 1, // ID of location
            "location": "Amphawa", // Location
            "numberOfVoters": 9900,// The current amount of votes
            "nameOfParliament": "Jakarin Chujan", // Parliament name
            "nameOfParty": "Catnip" // Party that parliament are with
            
        },
        {
            "locationID": 2,
            "location": "Bang Len",
            "numberOfVoters": 9900,
            "nameOfParliament": "Chananya Photan", 
            "nameOfParty": "Catnip"
        },
        .
        .
        .
    ]
}
```

### ```/validate-cvv```
Verify whether the citizen id and CVV match.

**Request body:** application/json  
**Response:** 200 OK  

```js
{
    "detail" : true
}
```
