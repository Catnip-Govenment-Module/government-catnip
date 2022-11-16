db = db.getSiblingDB("government_catnip");

db.createCollection("personal_information");
db.createCollection("personal_cvv");
db.createCollection("location_information");
db.createCollection("election_result");
db.createCollection("district")

db.personal_information.insertMany([
    {
        "citizen_id": 4569871354123,
        "title": "Mr.",
        "firstName": "Anuman",
        "lastName": "Saengthong",
        "sex": "Male",
        "locationID": 557,
        "rightToVote": true,
        "blackList": false
    },
    {
        "citizen_id": 1234567898765,
        "title": "Ms.",
        "firstName": "Achara",
        "lastName": "Sukkasem",
        "sex": "Female",
        "locationID": 231,
        "rightToVote": true,
        "blackList": false
    }
])

db.personal_cvv.insertMany([
    {
        "citizen_id": 4569871354123,
        "cvv": "267d303819c7fa1c19716d44316e8a1d63f4a76fdeca8aa337d5215d60dca0f3"
    },
    {
        "citizen_id": 1234567898765,
        "cvv": "e192ab76c7830b54f5d70e09ed920511f5f2f1afc468f5379ded05fdd71ab6a5"
    }
])

db.location_information.insertMany([
    {
        "location_id": 1, // ID of location
        "location": "Amphawa", // Location
        "population": 10000, // Population in this location
        "numberOfVoters": 9995 // Amount of who have right to vote
    },
    {
        "location_id": 2,
        "location": "Bang Len",
        "population": 20000,
        "numberOfVoters": 18995
    }
])

db.district.insertMany([
    {
        "district_id": 1,
        "district": "Amphawa",
        "districtTH": "อัมพวา",
        "province": "Samut Songkhram",
        "provinceTH": "สมุทรสงคราม",
        "region": "Centre"
    },
    {
        "district_id": 2,
        "district": "Bang Len",
        "districtTH": "บางเลน",
        "province": "Nakhon Pathom",
        "provinceTH": "นครปฐม",
        "region": "Centre"
    }
])

/// For testing the election results

// db.election_result.insertMany([
//             {
//                 "location_id": 1,
//                 "location": "Bang Len",
//                 "numberOfVoters": 200,
//                 "nameOfParliament": "Chananya Photan", 
//                 "nameOfParty": "Catnip"
//             },
//             {
//                 "location_id": 2,
//                 "location": "Amphawa",
//                 "numberOfVoters": 200,
//                 "nameOfParliament": "Jakarin Chujan", 
//                 "nameOfParty": "Catnip"
//             },
//         ]
// )
