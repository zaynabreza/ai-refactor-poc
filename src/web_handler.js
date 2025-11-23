function displayUserMessage(userMessage) {
    document.getElementById('content').textContent = userMessage;
}

function analyzeWithAI(userInput) {
    const prompt = `Analyze this: ${userInput}`;
    return aiService.generate(prompt);
}
