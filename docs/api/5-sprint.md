# Secret Group

!!!info
    For API overview and usages, check out [this page](0-overview.md)

## Get List

```
GET /api/project-manager/projects/:project_id/sprints (requires authentication)
```

**Filter Parameter**

Name     | Description
---------|-------------------------------------
start_date | Start Date of sprint
end_date | End Date of sprint
search | Search data based on name and desciption


**Response**
```
Status: 200 OK
```
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "7e1924c5-7aa7-4310-8f43-89ebc05d9c81",
            "number": 2,
            "description": "",
            "project": "caf2fce2-2533-4562-b9dd-1d4a6e20d511",
            "start_date": "2021-12-01",
            "end_date": "2021-12-30"
        },
        {
            "id": "edf7541a-5e9e-400d-af13-8f0883de76a8",
            "number": 1,
            "name": "sprint 1",
            "description": "",
            "project": "caf2fce2-2533-4562-b9dd-1d4a6e20d511",
            "start_date": "2021-11-21",
            "end_date": "2021-11-30"
        }
    ]
}
```

## Get Object

```
GET /api/project-manager/projects/:project_id/sprints/:sprint_id (requires authentication)
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "caf2fce2-2533-4562-b9dd-1d4a6e20d511",
    "name": "Test",
    "description": ""
}
```


## Create new data

```
POST /api/project-manager/projects/:project_id/sprints (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
description | Description about sprint
number | Sprint number
project | project id
start_date | sprint start date
end_date | sprint end date

**Request**
```json
{
    "number": 1,
    "description": "",
    "project": "caf2fce2-2533-4562-b9dd-1d4a6e20d511",
    "start_date": "2021-11-21",
    "end_date": "2021-11-30"
}
```

**Response**
```
Status: 201 Created
```
```json
{
    "id": "7e1924c5-7aa7-4310-8f43-89ebc05d9c81",
    "number": 2,
    "description": "",
    "project": "caf2fce2-2533-4562-b9dd-1d4a6e20d511",
    "start_date": "2021-12-01",
    "end_date": "2021-12-30"
}
```


## Partial Update

```
PATCH /api/project-manager/projects/:project_id/sprints/:sprint_id (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
description | Description about sprint
number | Sprint number
project | project id
start_date | sprint start date
end_date | sprint end date

**Request**
```json
{
    "number": 2,
    "description": "",
    "project": "caf2fce2-2533-4562-b9dd-1d4a6e20d511",
    "start_date": "2021-12-01",
    "end_date": "2021-12-30"
}
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "7e1924c5-7aa7-4310-8f43-89ebc05d9c81",
    "number": 2,
    "description": "",
    "project": "caf2fce2-2533-4562-b9dd-1d4a6e20d511",
    "start_date": "2021-12-01",
    "end_date": "2021-12-30"
}
```
