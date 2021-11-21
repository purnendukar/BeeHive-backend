# Secret Group

!!!info
    For API overview and usages, check out [this page](0-overview.md)

## Get List

```
GET /api/project-manager/project (requires authentication)
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
            "id": "caf2fce2-2533-4562-b9dd-1d4a6e20d511",
            "name": "Test",
            "description": ""
        },
        {
            "id": "d930327b-8207-46ee-9e67-1c869b78311b",
            "name": "Test",
            "description": ""
        }
    ]
}
```

## Get Object

```
GET /api/project-manager/project/:project_id (requires authentication)
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
POST /api/project-manager/project (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
description | Description about project
name | Name of the project

**Request**
```json
{
    "name": "Test",
    "description": ""
}
```

**Response**
```
Status: 201 Created
```
```json
{
    "id": "8bb3f9d6-cb80-4f2c-9c70-9221a47adb4a",
    "name": "Test",
    "description": ""
}
```


## Partial Update

```
PATCH /api/project-manager/project/:project_id (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
description | Description about project
name | Name of the project

**Request**
```json
{
    "name": "Test",
    "description": ""
}
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "8bb3f9d6-cb80-4f2c-9c70-9221a47adb4a",
    "name": "Test",
    "description": ""
}
```
