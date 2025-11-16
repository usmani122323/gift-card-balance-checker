from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

class BalanceCheckRequest(BaseModel):
    store: str
    card_number: str
    pin: str

@app.post("/check-balance")
async def check_balance(request: BalanceCheckRequest):
    # Placeholder - will implement AI logic
    return {
        "success": True,
        "balance": 0,
        "message": "API is working"
    }

@app.get("/")
async def root():
    return {"status": "Gift Card Balance Checker API is running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
```

4. Click **"Commit new file"** (green button at bottom)

**File 2: Create `requirements.txt`**

1. Click **"Add file" → "Create new file"**
2. Name it: `requirements.txt`
3. Paste this:
```
fastapi==0.104.1
uvicorn==0.24.0
anthropic==0.39.0
pydantic==2.5.0
requests==2.31.0
