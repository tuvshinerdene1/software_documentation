when a client requests data from a server, the server doesn't jst send raw data. it also sends clickable links that tell the client exactly what it is allowed to do next. 

without HATEOAS:

```
{
    "account_number": "12345",
    "balance": 50.00,
    "status": "active"
}

```

with HATEOAS:
```
{
    "account_number": "12345",
    "balance": 50.00,
    "status": "active",
    "links": [
        { "rel": "self", "method": "GET", "href": "/accounts/12345" },
        { "rel": "deposit", "method": "POST", "href": "/accounts/12345/deposit" },
        { "rel": "withdraw", "method": "POST", "href": "/accounts/12345/withdraw" }
    ]
}
```