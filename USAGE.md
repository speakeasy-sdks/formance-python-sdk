<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()
s.config_security(
    security=shared.Security(
        authorization=shared.SchemeAuthorization(
            authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
        ),
    )
)
    
res = s.get_server_info()

if res.server_info is not None:
    # handle response
```
<!-- End SDK Example Usage -->