# PowerShell Test Script for Resume RAG API
# Run with: .\test.ps1

$baseUrl = "http://localhost:8000"

Write-Host "=== Resume RAG API Test Script ===" -ForegroundColor Yellow
Write-Host ""

# Test Health Check
Write-Host "1. Testing Health Check..." -ForegroundColor Cyan
try {
    $health = Invoke-RestMethod -Uri "$baseUrl/health" -Method GET
    Write-Host "   Status: $($health.status)" -ForegroundColor Green
    Write-Host "   Index Loaded: $($health.index_loaded)" -ForegroundColor Green
    Write-Host "   Chunks: $($health.chunks_count)" -ForegroundColor Green
} catch {
    Write-Host "   Error: $_" -ForegroundColor Red
}

Write-Host ""

# Test Questions
$questions = @(
    "What are your key skills?",
    "What is your educational background?",
    "What work experience do you have?",
    "What programming languages and technologies do you know?",
    "Tell me about your projects",
    "What certifications do you have?",
    "What experience do you have in AI or machine learning?",
    "What is your contact information?"
)

$questionNum = 2
foreach ($question in $questions) {
    Write-Host "$questionNum. Testing Question: $question" -ForegroundColor Cyan
    try {
        $body = @{question=$question} | ConvertTo-Json
        $response = Invoke-RestMethod -Uri "$baseUrl/ask" -Method POST -ContentType "application/json" -Body $body
        Write-Host "   Answer: $($response.answer)" -ForegroundColor Green
    } catch {
        Write-Host "   Error: $_" -ForegroundColor Red
        if ($_.ErrorDetails.Message) {
            Write-Host "   Details: $($_.ErrorDetails.Message)" -ForegroundColor Red
        }
    }
    Write-Host ""
    $questionNum++
}

# Test "Not Available" case
Write-Host "$questionNum. Testing 'Not Available' Response..." -ForegroundColor Cyan
try {
    $body = @{question="What is your favorite color?"} | ConvertTo-Json
    $response = Invoke-RestMethod -Uri "$baseUrl/ask" -Method POST -ContentType "application/json" -Body $body
    Write-Host "   Answer: $($response.answer)" -ForegroundColor Green
} catch {
    Write-Host "   Error: $_" -ForegroundColor Red
}

Write-Host ""
Write-Host "=== Tests Completed ===" -ForegroundColor Yellow
