# Secret Group

!!!info
    For API overview and usages, check out [this page](0-overview.md)

## Get List

```
GET /api/project-manager/project/:project_id/member (requires authentication)
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
            "id": "40639bc7-7ce9-478e-90dc-0d62ffbb7289",
            "project": "d930327b-8207-46ee-9e67-1c869b78311b",
            "user": "6cd957cb-5604-442a-a843-0e24b0bc758d",
            "role": [
                "dc9bb865-9427-463d-bdf7-5c23afadc288"
            ]
        },
        {
            "id": "a461c71f-ca64-4a8b-a266-b800cea9a089",
            "project": "d930327b-8207-46ee-9e67-1c869b78311b",
            "user": "e83c2bab-022d-482e-b0ae-153976dedb18",
            "role": [
                "dc9bb865-9427-463d-bdf7-5c23afadc288"
            ]
        }
    ]
}
```

## Get Object

```
GET /api/project-manager/project/:project_id/member/:member_id (requires authentication)
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "a461c71f-ca64-4a8b-a266-b800cea9a089",
    "project": "d930327b-8207-46ee-9e67-1c869b78311b",
    "user": "e83c2bab-022d-482e-b0ae-153976dedb18",
    "role": [
        "dc9bb865-9427-463d-bdf7-5c23afadc288"
    ]
}
```


## Create new data

```
POST /api/project-manager/project:project_id/member (requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
user | user id
role | list of role ids

**Request**
```json
{
    "user": "e83c2bab-022d-482e-b0ae-153976dedb18",
    "role": [
        "dc9bb865-9427-463d-bdf7-5c23afadc288"
    ]
}
```

**Response**
```
Status: 201 Created
```
```json
{
    "id": "34e9774d-261d-4cdc-8652-69aca00f2871",
    "project": "1a62e7b7-bdcf-4604-8c16-2c8200793be6",
    "user": "e83c2bab-022d-482e-b0ae-153976dedb18",
    "role": [
        "dc9bb865-9427-463d-bdf7-5c23afadc288"
    ]
}
```


## Partial Update

```
PATCH /api/project-manager/project/:project_id/member/:member_id(requires authentication)
```

**Parameters**

Name     | Description
---------|-------------------------------------
user | user id
role | list of role ids

**Request**
```json
{
    "user": "e83c2bab-022d-482e-b0ae-153976dedb18",
    "role": [
        "dc9bb865-9427-463d-bdf7-5c23afadc288"
    ]
}
```

**Response**
```
Status: 200 OK
```
```json
{
    "id": "34e9774d-261d-4cdc-8652-69aca00f2871",
    "project": "1a62e7b7-bdcf-4604-8c16-2c8200793be6",
    "user": "e83c2bab-022d-482e-b0ae-153976dedb18",
    "role": [
        "dc9bb865-9427-463d-bdf7-5c23afadc288"
    ]
}
```
