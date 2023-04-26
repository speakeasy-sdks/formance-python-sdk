<!-- Start SDK Example Usage -->
```python
import formance


s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


res = s.get_server_info()

if res.server_info is not None:
    # handle response
```
<!-- End SDK Example Usage -->