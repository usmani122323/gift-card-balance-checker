from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

class BalanceCheckRequest(BaseModel):
    store: str
    card_number: str
    pin: str

@app.post("/check-balance")
async def check_balance(request: BalanceCheckRequest):
    """Check gift card balance using OpenAI GPT-4"""
    
    try:
        # Create prompt for GPT-4
        prompt = f"""You are helping check a gift card balance.

Store: {request.store}
Card Number: {request.card_number}
PIN: {request.pin}

Provide step-by-step instructions on how to check the balance on this store's website.
Include:
1. The balance check URL
2. Form field identifiers
3. How to extract the balance

Return as JSON with this structure:
{{
  "instructions": "step by step guide",
  "estimated_difficulty": "easy/medium/hard"
}}
"""

        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides web automation guidance."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        
        instructions = response.choices[0].message.content
        
        return {
            "success": True,
            "balance": 0,
            "instructions": instructions,
            "message": "AI provided instructions (manual verification needed)"
        }
        
    except Exception as e:
        return {
            "success": False,
            "balance": 0,
            "error": str(e),
            "message": f"Error: {str(e)}"
        }

@app.get("/")
async def root():
    return {"status": "Gift Card Balance Checker API is running with OpenAI"}

@app.get("/health")
async def health():
    return {"status": "healthy", "ai_provider": "OpenAI GPT-4"}
```

5. Scroll down and click **"Commit changes"**
6. Add commit message: `Updated to use OpenAI API`
7. Click **"Commit changes"**

---

### **Step 2: Update `requirements.txt`**

1. Click on **`requirements.txt`** in your repo
2. Click the **pencil icon** (✏️)
3. **Delete everything** and replace with:
```
fastapi==0.104.1
uvicorn==0.24.0
openai==0.28.1
pydantic==2.5.0
requests==2.31.0
