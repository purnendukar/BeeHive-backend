# Secret Group

!!!info
    For API overview and usages, check out [this page](0-overview.md)

## Get List

```
GET /api/project-manager/projects/:project_id/status (requires authentication)
```

**Response**
```
Status: 200 OK
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "e41d5c65-4d8a-4257-9f35-58995c8e012f",
            "name": "To DO",
            "description": "todo",
            "sort_order": 1,
            "is_todo": true,
            "is_complete": false,
            "project": "5598ad31-919e-4528-ab5f-f74cc19bcbce"
        }
    ]
}
```

## Get Object

```
GET /api/project-manager/projects/:project_id/status/:status_id (requires authentication)
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "e41d5c65-4d8a-4257-9f35-58995c8e012f",
    "name": "To DO",
    "description": "todo",
    "sort_order": 1,
    "is_todo": true,
    "is_complete": false,
    "project": "5598ad31-919e-4528-ab5f-f74cc19bcbce"
}
```


## Create new data

```
POST /api/project-manager/projects/:project_id/status (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
name | name of role
permission | list of permission ids
description | description of role

**Request**
```json
{
    "name": "To DO",
    "description": "todo",
    "sort_order": 1,
    "is_todo": true,
    "is_complete": false,
}
```

**Response**
```
Status: 201 Created
```
```json
{
    "id": "e41d5c65-4d8a-4257-9f35-58995c8e012f",
    "name": "To DO",
    "description": "todo",
    "sort_order": 1,
    "is_todo": true,
    "is_complete": false,
    "project": "5598ad31-919e-4528-ab5f-f74cc19bcbce"
}
```


## Partial Update

```
PATCH /api/project-manager/projects/:project_id/status/:status_id(requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
name | name of role
permission | list of permission ids
description | description of role

**Request**
```json
{
    "name": "To DO",
    "description": "todo",
    "sort_order": 1,
    "is_todo": true,
    "is_complete": false,
}
```

**Response**
```
Status: 201 Created
```
```json
{
    "id": "e41d5c65-4d8a-4257-9f35-58995c8e012f",
    "name": "To DO",
    "description": "todo",
    "sort_order": 1,
    "is_todo": true,
    "is_complete": false,
    "project": "5598ad31-919e-4528-ab5f-f74cc19bcbce"
}
```
