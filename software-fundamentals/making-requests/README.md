# Notes

## JSON

- **J**ava**S**cript **O**bject **N**otation
- A data **interchange** format (format designed to send information between different machines/services/people)
- Machine-readable first, human-readable second
- Very similar to the structure of JS objects (and also Python objects)

```json
{
    "values": [1, 2, 3],
    "key": "string",
    "key2": {
        "key": [{
            "1" : 2
        }]
    }
}
```

## HTTP status code

- 2xx : good/fine/okay
  - 200 (normal okay)
  - 201 (created that thing)
  - 204 (yes but nothing else)
- 3xx : go somewhere else
- 4xx : client problem
  - 404 (not found)
  - 403 (forbidden)
- 5xx : server side