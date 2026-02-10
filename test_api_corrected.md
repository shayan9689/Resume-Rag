# Corrected API Test Examples

## The Issue
The error occurs when JSON is sent as a string literal instead of a parsed JSON object. Make sure to:
1. Use proper JSON formatting
2. Set Content-Type header correctly
3. Send the body as JSON, not as a string

---

## ✅ CORRECT PowerShell Examples

### Method 1: Using ConvertTo-Json (Recommended)
```powershell
$body = @{question="What are your key skills?"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:8000/ask" -Method POST -ContentType "application/json" -Body $body
```

### Method 2: Using Here-String
```powershell
$json = @'
{"question": "What are your key skills?"}
'@
Invoke-RestMethod -Uri "http://localhost:8000/ask" -Method POST -ContentType "application/json" -Body $json
```

### Method 3: Direct JSON String (Single Line)
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/ask" -Method POST -ContentType "application/json" -Body '{"question":"What are your key skills?"}'
```

---

## ✅ CORRECT curl Examples (Windows CMD)

### Method 1: Single Line
```bash
curl -X POST "http://localhost:8000/ask" -H "Content-Type: application/json" -d "{\"question\":\"What are your key skills?\"}"
```

### Method 2: Using File
Create `request.json`:
```json
{"question": "What are your key skills?"}
```

Then run:
```bash
curl -X POST "http://localhost:8000/ask" -H "Content-Type: application/json" -d @request.json
```

---

## ✅ CORRECT Python Examples

```python
import requests

# Method 1: Using json parameter (Recommended)
response = requests.post(
    "http://localhost:8000/ask",
    json={"question": "What are your key skills?"}
)
print(response.json())

# Method 2: Using data parameter with json.dumps
import json
response = requests.post(
    "http://localhost:8000/ask",
    headers={"Content-Type": "application/json"},
    data=json.dumps({"question": "What are your key skills?"})
)
print(response.json())
```

---

## ✅ CORRECT JavaScript/Node.js Examples

```javascript
// Using fetch
fetch('http://localhost:8000/ask', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    question: 'What are your key skills?'
  })
})
.then(response => response.json())
.then(data => console.log(data));

// Using axios
const axios = require('axios');
axios.post('http://localhost:8000/ask', {
  question: 'What are your key skills?'
})
.then(response => console.log(response.data));
```

---

## ❌ COMMON MISTAKES TO AVOID

### Wrong: Double JSON encoding
```powershell
# DON'T DO THIS - This sends JSON as a string
Invoke-RestMethod -Uri "http://localhost:8000/ask" -Method POST -Body '{"question": "test"}'
```

### Wrong: Missing Content-Type
```powershell
# DON'T DO THIS - Missing Content-Type header
Invoke-RestMethod -Uri "http://localhost:8000/ask" -Method POST -Body '{"question":"test"}'
```

### Wrong: Using single quotes with escaped quotes in PowerShell
```powershell
# DON'T DO THIS - PowerShell treats this as a string literal
Invoke-RestMethod -Uri "http://localhost:8000/ask" -Method POST -Body "{`"question`":`"test`"}"
```

---

## Quick Test Scripts

### PowerShell Test Script (test.ps1)
```powershell
$questions = @(
    "What are your key skills?",
    "What is your educational background?",
    "What work experience do you have?",
    "What programming languages do you know?"
)

foreach ($q in $questions) {
    Write-Host "`nQuestion: $q" -ForegroundColor Cyan
    $body = @{question=$q} | ConvertTo-Json
    $response = Invoke-RestMethod -Uri "http://localhost:8000/ask" -Method POST -ContentType "application/json" -Body $body
    Write-Host "Answer: $($response.answer)" -ForegroundColor Green
}
```

### Python Test Script (test_simple.py)
```python
import requests

questions = [
    "What are your key skills?",
    "What is your educational background?",
    "What work experience do you have?",
    "What programming languages do you know?"
]

for question in questions:
    print(f"\nQuestion: {question}")
    response = requests.post(
        "http://localhost:8000/ask",
        json={"question": question}
    )
    print(f"Answer: {response.json()['answer']}")
```

---

## Test All Endpoints

### Health Check
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/health" -Method GET
```

### Root Endpoint
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/" -Method GET
```

### Ask Question
```powershell
$body = @{question="What are your key skills?"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:8000/ask" -Method POST -ContentType "application/json" -Body $body
```
