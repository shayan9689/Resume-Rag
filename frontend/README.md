# Resume RAG Frontend

A modern, responsive web interface for the Resume RAG system.

## Features

- 🎨 **Modern UI/UX** - Clean, professional design with gradient backgrounds
- 📱 **Responsive** - Works on desktop, tablet, and mobile devices
- ⚡ **Real-time** - Instant API responses with loading states
- 🎯 **Example Questions** - Quick access to common questions
- ✅ **Error Handling** - User-friendly error messages
- 🔄 **API Status** - Real-time API health monitoring

## Quick Start

### Option 1: Open Directly in Browser

Simply open `index.html` in your web browser:

```bash
# Windows
start frontend/index.html

# Mac/Linux
open frontend/index.html
```

### Option 2: Using Python HTTP Server

**If port 8080 is blocked, use a different port:**

```bash
# Navigate to frontend directory
cd frontend

# Python 3 - Use any available port (e.g., 8001, 3000, etc.)
python -m http.server 8001

# Then open http://localhost:8001 in your browser
```

**Or use the automatic port finder:**

```bash
# From frontend directory
python start_server.py

# This will automatically find an available port and open your browser
```

### Option 3: Using Node.js http-server

```bash
# Install http-server globally (if not installed)
npm install -g http-server

# Navigate to frontend directory
cd frontend

# Start server
http-server -p 8080

# Then open http://localhost:8080 in your browser
```

## Usage

1. **Enter a Question**: Type your question in the text area
2. **Click "Ask Question"** or press `Ctrl+Enter` / `Shift+Enter`
3. **View Answer**: The answer will appear below
4. **Use Examples**: Click any example button to quickly ask common questions

## API Configuration

The frontend is configured to connect to `http://localhost:8000` by default.

To change the API URL, edit `script.js`:

```javascript
const API_BASE_URL = 'http://your-api-url:8000';
```

## File Structure

```
frontend/
├── index.html      # Main HTML structure
├── styles.css      # All styling and responsive design
├── script.js       # JavaScript logic and API calls
└── README.md       # This file
```

## Browser Compatibility

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Opera (latest)

## Features in Detail

### Question Input
- Multi-line text area for longer questions
- Keyboard shortcuts: `Ctrl+Enter` or `Shift+Enter` to submit
- Auto-focus on page load

### Answer Display
- Formatted text with markdown support
- Smooth scrolling to answers
- Clean, readable formatting

### Example Questions
- Pre-filled common questions
- One-click access
- Covers key resume sections

### API Status Indicator
- Real-time health check
- Visual status indicators (✓/✗)
- Updates on page load

## Troubleshooting

### CORS Errors
Make sure CORS is enabled in the FastAPI backend (already configured in `app/main.py`).

### API Not Responding
1. Check if backend server is running: `http://localhost:8000/health`
2. Verify API URL in `script.js`
3. Check browser console for errors

### Styling Issues
- Clear browser cache
- Ensure `styles.css` is loaded correctly
- Check browser console for CSS errors
