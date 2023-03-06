<!-- Start SDK Example Usage -->
```python
import formance
from formance.models import operations, shared

s = formance.Formance()
s.config_security(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    )
)
    
res = s.get_server_info()

if res.server_info is not None:
    # handle response
```
<!-- End SDK Example Usage -->