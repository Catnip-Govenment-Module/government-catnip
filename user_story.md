# Catnip' USER STORY: Government Module

## User Story1  

**Title**: Population Data 
**Priority**: Must have  
**Estimate**:

### User Story

As the Election committee
I want the population data such as title, firstName, lastName, CitizenID, sex, LocationID, rightToVote, blacklist.
So that the election committee can use it for the election


### Acceptance Criteria

Given election committee get the population data  
When the election committee requests data from the Government 
Then they can use it for the election

## User Story2  

**Title**: Check CVV  
**Priority**: Must have  
**Estimate**:

### User Story

As the election committee
I want to check the CVV from the user. 
So that the election committee will allow the user to vote for the candidate.

### Acceptance Criteria

Given the election committee send the CVV to check with the Government 
When the user wants to vote for the candidate
Then the election committee allows the user to right to vote if the user's CVV is correct.

## User Story3  

**Title**: Location Data
**Priority**: Must have  
**Estimate**:

### User Story

As the Election committee
I want the location data such as Location, LocationID, Population
So that the election committee can use it for the election

### Acceptance Criteria

Given election committee get the location data  
When the election committee requests data from the Government 
Then they can use it for the election

## User Story4  

**Title**: Get Election Result from EC
**Priority**: Must have  
**Estimate**:

### User Story

As the Government
I want the election result from the election committee 
So that the government collects it on the database

### Acceptance Criteria

Given the government gets the election result from the election committee
When the election ends and the election committee calculates and summarizes the result.
Then the government collects it on the database.

## User Story5  

**Title**: Send Election Result to the voter
**Priority**: Must have  
**Estimate**:

### User Story

As the voter
I want the election result from the government  
So that the voter shows the election result to the population

### Acceptance Criteria

Given the government send the election result to the voter
When the voter requests the data from the government
Then the voter shows the election result to the population