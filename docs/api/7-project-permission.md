# Secret Group

!!!info
    For API overview and usages, check out [this page](0-overview.md)

## Get List

```
GET /api/project-manager/permissions (requires authentication)
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
            "id": "0a259b52-341f-4e42-baf2-cbdb76b0818a",
            "title": "Update Project",
            "description": "admin"
        }
    ]
}
```
