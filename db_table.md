# Table in DataBase

## personal_information

```js
{
     "_id": number,
     "title": string,
     "firstName": string,
     "lastName": string,
     "sex": string,
     "locationID": number,
     "rightToVote": boolean,
     "blackList": boolean
}
```
### _id
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
     "_id": number,
     "citizenCVV": hash
}
```

### _id
The person's citizen identification number

### citizenCVV
The person's citizen identification card verification value number

## location_information

```js
{
     "_id": number, 
     "location": string,
     "population": number,
     "numberOfVoters": number
}
```

### _id
It's the id of District

### location
It's the name of District

### population
It's the number of population in this location

### numberOfVoters
It's the number of people that have a right to vote in this location

## election_result

```js
{
     "_id" : number,
     "memberID": number,
     "nameOfParliament": string,
     "nameOfParty": string,
     "numberOfVotes": number,
     "lastUpdatedTime": string
}
     
```

### _id
ID of district

### memberID
ID of member of parliament in location

### nameOfParliament
The name of member of parliament in location

### nameOfParty
The name of the party that member of parliament are work for

### numberOfVotes
Amount of population have been voted in this location

### lastUpdatedTime
Last time data have been updated 

## district

```js
{
     "district": string,
     "districtTH": string,
     "province": string,
     "provinceTH": string,
     "region": string
}
```

### district
The district's name

### districtTH
The name of the district in Thai

### province
The province's name

### provinceTH
The name of the province in Thai

### region
The region's name