/**
 * Frontend configuration
 */

const CONFIG = {
    // API Base URL - Update this if your backend runs on a different port/host
    API_BASE_URL: 'http://localhost:8000',
    
    // UI Settings
    UI: {
        // Animation duration in milliseconds
        animationDuration: 300,
        
        // Auto-scroll to answer
        autoScroll: true,
        
        // Show API status indicator
        showApiStatus: true
    },
    
    // Example questions - Comprehensive set covering all query types
    EXAMPLE_QUESTIONS: [
        // Greetings
        "Hello",
        "Hi there!",
        
        // General
        "Tell me about this resume",
        "What can you tell me about the candidate?",
        
        // Skills & Technologies
        "What are your key skills?",
        "What programming languages do you know?",
        "What technologies are you familiar with?",
        "What AI/ML skills do you have?",
        
        // Education
        "What is your educational background?",
        "What degrees do you have?",
        "Where did you study?",
        
        // Experience
        "What work experience do you have?",
        "What companies have you worked for?",
        "How many years of experience do you have?",
        
        // Projects
        "What projects have you worked on?",
        "Tell me about your portfolio",
        
        // Certifications
        "What certifications do you have?",
        "What credentials do you hold?",
        
        // Contact
        "What is your contact information?",
        "What is your email?",
        "Where are you located?",
        
        // Achievements
        "What are your achievements?",
        "Tell me about your accomplishments",
        
        // Analysis
        "What is your strongest skill?",
        "What makes you unique?",
        
        // Multiple Topics
        "What are your skills and education?",
        "Tell me about your experience and projects"
    ]
};

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONFIG;
}
