db = db.getSiblingDB("government_catnip");

db.createCollection("personal_information");
db.createCollection("personal_cvv");
db.createCollection("location_information");
db.createCollection("election_result");
db.createCollection("district")

db.personal_information.insertMany([
    {
        "_id": 4569871354123,
        "title": "Mr.",
        "firstName": "Anuman",
        "lastName": "Saengthong",
        "sex": "Male",
        "locationID": 557,
        "rightToVote": true,
        "blackList": false
    },
    {
        "_id": 1234567898765,
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
        "_id": 4569871354123,
        "cvv": "267d303819c7fa1c19716d44316e8a1d63f4a76fdeca8aa337d5215d60dca0f3"
    },
    {
        "_id": 1234567898765,
        "cvv": "e192ab76c7830b54f5d70e09ed920511f5f2f1afc468f5379ded05fdd71ab6a5"
    }
])

db.location_information.insertMany([
    {
        "_id": 1, // ID of location
        "location": "Amphawa", // Location
        "population": 10000, // Population in this location
        "numberOfVoters": 9995 // Amount of who have right to vote
    },
    {
        "_id": 2,
        "location": "Bang Len",
        "population": 20000,
        "numberOfVoters": 18995
    }
])

db.district.insertMany([
    {
        "_id": 1,
        "district": "Amphawa",
        "districtTH": "อัมพวา",
        "province": "Samut Songkhram",
        "provinceTH": "สมุทรสงคราม",
        "region": "Centre"
    },
    {
        "_id": 2,
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
//                 "_id": "1",
//                 "district": "Amphawa", // District
//                 "districtTH": "อัมพวา", // District in Thai language
//                 "province": "Samut Songkhram", // Province
//                 "provinceTH": "สมุทรปราการ", // Province in Thai language
//                 "region": "centre", // Region
//                 "nameOfParliament": "Jakarin Chujan", // Parliament name
//                 "nameOfParty": "Catnip" // Party that parliament are with
//             },
//             {
//                 "_id": "2",
//                 "district": "Bang Len",
//                 "districtTH": "บางเลน",
//                 "province": "Phichit",
//                 "provinceTH": "พิจิตร",
//                 "region": "centre",
//                 "nameOfParliament": "Chananya Photan",
//                 "nameOfParty": "Catnip"
//             },
//         ]
// )
