# Secret Group

!!!info
    For API overview and usages, check out [this page](0-overview.md)

## Get List

```
GET /api/project-manager/project/:project_id/roles (requires authentication)
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
            "id": "68f764ab-36b2-4f6a-9281-412867a40e6d",
            "name": "admin",
            "permission": [
                {
                    "id": "0a259b52-341f-4e42-baf2-cbdb76b0818a",
                    "title": "Update Project",
                    "description": "admin"
                }
            ]
        }
    ]
}
```

## Get Object

```
GET /api/project-manager/project/:project_id/roles/:roles_id (requires authentication)
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "68f764ab-36b2-4f6a-9281-412867a40e6d",
    "name": "admin",
    "permission": [
        {
            "id": "0a259b52-341f-4e42-baf2-cbdb76b0818a",
            "title": "Update Project",
            "description": "admin"
        }
    ]
}
```


## Create new data

```
POST /api/project-manager/project:project_id/roles (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
name | name of role
permission | list of permission ids

**Request**
```json
{
    "name": "admin",
    "permission": [
        "0a259b52-341f-4e42-baf2-cbdb76b0818a"
    ]
}
```

**Response**
```
Status: 201 Created
```
```json
{
    "id": "68f764ab-36b2-4f6a-9281-412867a40e6d",
    "name": "admin",
    "permission": [
        {
            "id": "0a259b52-341f-4e42-baf2-cbdb76b0818a",
            "title": "Update Project",
            "description": "admin"
        }
    ]
}
```


## Partial Update

```
PATCH /api/project-manager/project/:project_id/roles/:roles_id(requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
name | name of role
permission | list of permission ids

**Request**
```json
{
    "name": "admin",
    "permission": [
        "0a259b52-341f-4e42-baf2-cbdb76b0818a"
    ]
}
```

**Response**
```
Status: 201 Created
```
```json
{
    "id": "68f764ab-36b2-4f6a-9281-412867a40e6d",
    "name": "admin",
    "permission": [
        {
            "id": "0a259b52-341f-4e42-baf2-cbdb76b0818a",
            "title": "Update Project",
            "description": "admin"
        }
    ]
}
```
