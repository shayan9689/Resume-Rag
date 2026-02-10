# Resume RAG Frontend - React.js

React.js frontend for the Resume RAG System with a modern white, blue, and black theme.

## Installation

```bash
cd frontend
npm install
```

## Running the Development Server

```bash
npm start
```

The app will open at `http://localhost:3000` (or next available port).

## Building for Production

```bash
npm run build
```

This creates an optimized production build in the `build` folder.

## Features

- Modern React.js interface
- White, blue, and black theme
- Real-time API status checking
- Example questions for quick testing
- Responsive design for mobile and desktop
- Plain text answer formatting (no markdown)

## Configuration

The API base URL is configured in `src/App.js`. Default is `http://localhost:8000`.

To change it, edit:
```javascript
const API_BASE_URL = 'http://localhost:8000';
```
