# Secret Group

!!!info
    For API overview and usages, check out [this page](0-overview.md)

## Get List

```
GET /api/project-manager/tasks (requires authentication)
```

**Filter Parameter**

Name     | Description
---------|-------------------------------------
sprint | sprint id

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
            "id": "de2f11d3-5376-4264-84fd-c24b2d9b51a3",
            "task_id": "BH-1",
            "title": "test tiele",
            "description": "",
            "priority": "high",
            "sprint": {
                "id": "a335f532-158d-4304-88a6-f33eddef56cb",
                "number": 1
            },
            "status": {
                "id": "e41d5c65-4d8a-4257-9f35-58995c8e012f",
                "name": "To DO",
                "description": "todo"
            },
            "parent": null,
            "depedency": null,
            "assignee": {
                "id": "e83c2bab-022d-482e-b0ae-153976dedb18",
                "email": "purnendu.kar8+1@gmail.com",
                "first_name": "Test",
                "last_name": "User"
            },
            "reporter": "6cd957cb-5604-442a-a843-0e24b0bc758d",
            "attachments": [],
            "estimated_time": "1.00"
        },
        {
            "id": "de2f11d3-5376-4264-84fd-c24b2d9b51a3",
            "task_id": "BH-2",
            "title": "test tiele",
            "description": "",
            "priority": "high",
            "sprint": {
                "id": "a335f532-158d-4304-88a6-f33eddef56cb",
                "number": 1
            },
            "status": {
                "id": "e41d5c65-4d8a-4257-9f35-58995c8e012f",
                "name": "To DO",
                "description": "todo"
            },
            "parent": null,
            "depedency": null,
            "assignee": {
                "id": "e83c2bab-022d-482e-b0ae-153976dedb18",
                "email": "purnendu.kar8+1@gmail.com",
                "first_name": "Test",
                "last_name": "User"
            },
            "reporter": "6cd957cb-5604-442a-a843-0e24b0bc758d",
            "attachments": [],
            "estimated_time": "1.00"
        }
    ]
}
```

## Get Object

```
GET /api/project-manager/tasks/:task_id (requires authentication)
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "de2f11d3-5376-4264-84fd-c24b2d9b51a3",
    "task_id": "BH-5",
    "title": "test tiele",
    "description": "",
    "priority": "high",
    "sprint": {
        "id": "a335f532-158d-4304-88a6-f33eddef56cb",
        "number": 1
    },
    "status": {
        "id": "e41d5c65-4d8a-4257-9f35-58995c8e012f",
        "name": "To DO",
        "description": "todo"
    },
    "parent": null,
    "depedency": null,
    "assignee": {
        "id": "e83c2bab-022d-482e-b0ae-153976dedb18",
        "email": "purnendu.kar8+1@gmail.com",
        "first_name": "Test",
        "last_name": "User"
    },
    "reporter": "6cd957cb-5604-442a-a843-0e24b0bc758d",
    "attachments": [],
    "estimated_time": "1.00"
}
```


## Create new data

```
POST /api/project-manager/tasks (requires authentication)
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
    "title": "test tiele",
    "description": "",
    "sprint": "a335f532-158d-4304-88a6-f33eddef56cb",
    "status": "e41d5c65-4d8a-4257-9f35-58995c8e012f",
    "depedency": null,
    "assignee": "e83c2bab-022d-482e-b0ae-153976dedb18",
    "reporter": "6cd957cb-5604-442a-a843-0e24b0bc758d",
    "priority": "high",
    "estimated_time": "1"
}
```

**Response**
```
Status: 201 Created
```
```json
{
    "id": "de2f11d3-5376-4264-84fd-c24b2d9b51a3",
    "task_id": "BH-5",
    "title": "test tiele",
    "description": "",
    "priority": "high",
    "sprint": {
        "id": "a335f532-158d-4304-88a6-f33eddef56cb",
        "number": 1
    },
    "status": {
        "id": "e41d5c65-4d8a-4257-9f35-58995c8e012f",
        "name": "To DO",
        "description": "todo"
    },
    "parent": null,
    "depedency": null,
    "assignee": {
        "id": "e83c2bab-022d-482e-b0ae-153976dedb18",
        "email": "purnendu.kar8+1@gmail.com",
        "first_name": "Test",
        "last_name": "User"
    },
    "reporter": "6cd957cb-5604-442a-a843-0e24b0bc758d",
    "attachments": [],
    "estimated_time": "1.00"
}
```


## Partial Update

```
PATCH /api/project-manager/tasks/:task_id (requires authentication)
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
priority | priority level (very_low, low, medium, high, very_high)
estimated_time | Estimated time in hours (Decimal value)

**Request**
```json
{
    "title": "test tiele",
    "description": "",
    "sprint": "a335f532-158d-4304-88a6-f33eddef56cb",
    "status": "e41d5c65-4d8a-4257-9f35-58995c8e012f",
    "depedency": null,
    "assignee": "e83c2bab-022d-482e-b0ae-153976dedb18",
    "reporter": "6cd957cb-5604-442a-a843-0e24b0bc758d",
    "priority": "high",
    "estimated_time": "1"
}
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "de2f11d3-5376-4264-84fd-c24b2d9b51a3",
    "task_id": "BH-5",
    "title": "test tiele",
    "description": "",
    "priority": "high",
    "sprint": {
        "id": "a335f532-158d-4304-88a6-f33eddef56cb",
        "number": 1
    },
    "status": {
        "id": "e41d5c65-4d8a-4257-9f35-58995c8e012f",
        "name": "To DO",
        "description": "todo"
    },
    "parent": null,
    "depedency": null,
    "assignee": {
        "id": "e83c2bab-022d-482e-b0ae-153976dedb18",
        "email": "purnendu.kar8+1@gmail.com",
        "first_name": "Test",
        "last_name": "User"
    },
    "reporter": "6cd957cb-5604-442a-a843-0e24b0bc758d",
    "attachments": [],
    "estimated_time": "1.00"
}
```
