# Table in DataBase

## personal_information

```js
{
     "citizenID": number,
     "title": string,
     "firstName": string,
     "lastName": string,
     "sex": string,
     "locationID": number,
     "rightToVote": boolean,
     "blacklist": boolean
}
```
### citizenID
The person's citizen identification number

### title
Titles prefixing a person's name

### firstName
A person's first name

### lastName
A person's last name

### sex
A person's sex

### locationID
The person's residence id

### rightToVote
A person's eligibility to cast a ballot in an election

### blacklist
a person's eligibility to register to be a member of parliament in an election

## personal_cvv

```js
{
     "citizenID": number,
     "citizenCVV": hash
}
```

### citizenID
The person's citizen identification number

### citizenCVV
The person's citizen identification card verification value number

## location_information

```js
{
     "locationID": number, 
     "location": string,
     "population": number,
     "numberOfVoters": number
}
```

### locationID
It's the id of location

### location
It's the name of location

### population
It's the number of population in this location

### numberOfVoters
It's the number of people that have a right to vote in this location

## election_result

```js
{
    "district": "string",
    "districtTH": "string",
    "province": "string",
    "provinceTH": "string",
    "region": "string",
    "nameOfParliament": "string",
    "nameOfParty": "string"
}
     
```

### district
The name of district in English.  

### districtTH
The name of district in Thai.  

### province  
The name of province in English.  

### provinceTH  
The name of province in Thai.  

### region  
The region's name.  

### nameOfParliament  
The name of member of parliament in location

### nameOfParty
The name of the party that member of parliament are work for.  

## district

```js
{
     "districtID": string,
     "district": string,
     "districtTH": string,
     "province": string,
     "provinceTH": string,
     "region": string
}
```

### districtID
ID of district

### district
The district's name

### districtTH
The name of the district in Thai language

### province
The province's name

### provinceTH
The name of the province in Thai language

### region
The region's name
