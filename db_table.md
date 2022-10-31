# Table in DataBase

## personal_information

```js
{
     "title": "string",
     "firstName": "string",
     "lastName": "string",
     "sex": "string",
     "citizenID": "string",
     "locationID": "number",
     "rightToVote": "boolean",
     "blackList": "boolean"
}
```

### title
Titles prefixing a person's name

### firstName
A person's first name

### lastName
A person's last name

### sex
A person's sex

### citizenID
The person's citizen identification number

### locationID
The person's residence id

### rightToVote
A person's eligibility to cast a ballot in an election

### blacklist
a person's eligibility to register to be a member of parliament in an election

## personal_cvv

```js
{
     "citizenID": string,
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
     "location": string,
     "locationID": number, 
     "population": number,
     "numberOfVoters": number
}
```

### location
It's the name of District

### locationID
It's the id of District

### population
It's the number of population in this location

### numberOfVoters
It's the number of people that have a right to vote in this location

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



```
     "memberID": number,
     "nameOfParliament": string,
     "nameOfParty": string,
     "numberOfVotes": number,
     "lastUpdatedTime": string
```