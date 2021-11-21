# Secret Group

!!!info
    For API overview and usages, check out [this page](0-overview.md)

## Get List

```
GET /api/project-manager/task (requires authentication)
```

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
            "id": "4db0e52b-421f-4194-b1b2-eb9ad1c7fda9",
            "title": "test tiele",
            "description": "",
            "sprint": "7e1924c5-7aa7-4310-8f43-89ebc05d9c81",
            "status": {
                "id": "3e07a633-d863-4a1c-8f49-2407e2d4f08c",
                "name": "To DO",
                "description": ""
            },
            "parent": null,
            "depedency": null,
            "assignee": "e83c2bab-022d-482e-b0ae-153976dedb18",
            "reporter": "6cd957cb-5604-442a-a843-0e24b0bc758d",
            "attachment": []
        },
        {
            "id": "83c04731-5e53-4207-9a48-47aa0469fa98",
            "title": "test tiele",
            "description": "",
            "sprint": "7e1924c5-7aa7-4310-8f43-89ebc05d9c81",
            "status": {
                "id": "3e07a633-d863-4a1c-8f49-2407e2d4f08c",
                "name": "To DO",
                "description": ""
            },
            "parent": null,
            "depedency": null,
            "assignee": "e83c2bab-022d-482e-b0ae-153976dedb18",
            "reporter": "6cd957cb-5604-442a-a843-0e24b0bc758d",
            "attachment": []
        }
    ]
}
```

## Get Object

```
GET /api/project-manager/task/:task_id (requires authentication)
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "4db0e52b-421f-4194-b1b2-eb9ad1c7fda9",
    "title": "test tiele",
    "description": "",
    "sprint": "7e1924c5-7aa7-4310-8f43-89ebc05d9c81",
    "status": {
        "id": "3e07a633-d863-4a1c-8f49-2407e2d4f08c",
        "name": "To DO",
        "description": ""
    },
    "parent": null,
    "depedency": null,
    "assignee": "e83c2bab-022d-482e-b0ae-153976dedb18",
    "reporter": "6cd957cb-5604-442a-a843-0e24b0bc758d",
    "attachment": []
}
```


## Create new data

```
POST /api/project-manager/task (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
description | Description about task
title | Name of the task
task | Sprint id
status | status id
parent | parent task id
dependency | dependency task id
assignee | assigned user id
reporter | reported user id

**Request**
```json
{
    "title": "test tiele child",
    "description": "",
    "sprint": "7e1924c5-7aa7-4310-8f43-89ebc05d9c81",
    "status": "3e07a633-d863-4a1c-8f49-2407e2d4f08c",
    "parent": "83c04731-5e53-4207-9a48-47aa0469fa98",
    "depedency": null,
    "assignee": "e83c2bab-022d-482e-b0ae-153976dedb18",
    "reporter": "6cd957cb-5604-442a-a843-0e24b0bc758d"
}
```

**Response**
```
Status: 201 Created
```
```json
{
    "id": "f2b439d8-8ba9-4e40-affd-d9744db2fc09",
    "title": "test tiele child",
    "description": "",
    "sprint": "7e1924c5-7aa7-4310-8f43-89ebc05d9c81",
    "status": {
        "id": "3e07a633-d863-4a1c-8f49-2407e2d4f08c",
        "name": "To DO",
        "description": ""
    },
    "parent": "83c04731-5e53-4207-9a48-47aa0469fa98",
    "depedency": null,
    "assignee": "e83c2bab-022d-482e-b0ae-153976dedb18",
    "reporter": "6cd957cb-5604-442a-a843-0e24b0bc758d",
    "attachment": []
}
```


## Partial Update

```
PATCH /api/project-manager/task/:task_id (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
description | Description about task
title | Name of the task
task | Sprint id
status | status id
parent | parent task id
dependency | dependency task id
assignee | assigned user id
reporter | reported user id

**Request**
```json
{
    "title": "test tiele child",
    "description": "",
    "sprint": "7e1924c5-7aa7-4310-8f43-89ebc05d9c81",
    "status": "3e07a633-d863-4a1c-8f49-2407e2d4f08c",
    "parent": "83c04731-5e53-4207-9a48-47aa0469fa98",
    "depedency": null,
    "assignee": "e83c2bab-022d-482e-b0ae-153976dedb18",
    "reporter": "6cd957cb-5604-442a-a843-0e24b0bc758d"
}
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "f2b439d8-8ba9-4e40-affd-d9744db2fc09",
    "title": "test tiele child",
    "description": "",
    "sprint": "7e1924c5-7aa7-4310-8f43-89ebc05d9c81",
    "status": {
        "id": "3e07a633-d863-4a1c-8f49-2407e2d4f08c",
        "name": "To DO",
        "description": ""
    },
    "parent": "83c04731-5e53-4207-9a48-47aa0469fa98",
    "depedency": null,
    "assignee": "e83c2bab-022d-482e-b0ae-153976dedb18",
    "reporter": "6cd957cb-5604-442a-a843-0e24b0bc758d",
    "attachment": []
}
```
