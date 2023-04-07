var axios = require('axios');

const env = require('dotenv').config({ path: "../../.env" });

var data = JSON.stringify({
    "collection": "testdb",
    "database": "test",
    "dataSource": "Cluster0",
    "projection": {
        "_id": 1,
        "id": 1,
        "name": 1
    }
});

var config = {
    method: 'post',
    url: 'https://us-west-2.aws.data.mongodb-api.com/app/data-lmrgh/endpoint/data/v1/action/findOne',
    headers: {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': process.env.ATLAS_API,
    },
    data: data
};
