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
        "citizen_id": 440556794906,
        "cvv": "$2b$12$xFOUTVJjht350Ik7D1eQhOB1yB0/yog4etgEbn4aDk3Jf3CT65rm."
    },
    {
        "citizen_id": 173518749711,
        "cvv": "$2b$12$UHsLQtJ5hit1XZyEYHo9IO.61aDeJV/rdc1/mp35OwJKcISe.hN0W"
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
