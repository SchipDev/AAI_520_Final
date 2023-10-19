// Fetch webpage elemnts
const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const submitButton = document.getElementById("submit-button");

// Function to add a message to the chat area
function addMessage(text, isUser = false) {
    const messageDiv = document.createElement("div");
    messageDiv.className = isUser ? "user-message" : "bot-message";
    messageDiv.textContent = text;
    chatBox.appendChild(messageDiv);
}

// Function to handle user input
function handleUserInput() {
    const userMessage = userInput.value;
    if (userMessage.trim() === "") {
        return;
    }

    addMessage(userMessage, true);
    userInput.value = "";

    // Replace this with your chatbot logic
    const botResponse = "This is where the chatbot's response would go.";
    addMessage(botResponse);

    // You can replace the above placeholder response with actual chatbot logic here
}

submitButton.addEventListener("click", handleUserInput);

userInput.addEventListener("keyup", function (event) {
    if (event.key === "Enter") {
        handleUserInput();
    }
});