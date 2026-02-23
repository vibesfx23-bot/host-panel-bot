import httpx
from typing import Dict, Any

class CPANELClient:
    def __init__(self, host: str, username: str = "root", password: str = None):
        self.base_url = f"https://{host}:2087"
        self.auth = (username, password or "")
    
    async def get_status(self) -> Dict[str, Any]:
        async with httpx.AsyncClient() as client:
            resp = await client.get(
                f"{self.base_url}/json-api/loadavg",
                auth=self.auth,
                verify=False  # Prod: use proper certs
            )
            return resp.json()
    
    async def restart_service(self, service: str) -> bool:
        # /json-api/scripts2/restartsrv?service=*
        pass
