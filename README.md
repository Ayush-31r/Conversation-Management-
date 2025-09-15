# Conversation Management & Classification using Groq API

## Overview
This project demonstrates:
1. **Conversation Management**: Maintain chat history, truncate by turns/length, and perform periodic summarization.
2. **JSON Schema Extraction**: Extract structured user info (name, email, phone, location, age) from chat messages using Groq API’s OpenAI-compatible function calling, validated against a JSON schema.

---

## Usage

### Task 1: Conversation Management
- Add messages via `ConversationManager`.
- Summarization occurs every `k` turns.
- History can be truncated by number of turns or characters.

### Task 2: JSON Schema Extraction
- Use `call_extract_function(client, chat_text)` to extract user info.
- Validates results with `jsonschema`.


## Sample Output

### Conversation Summary

system: System: You are a helpful assistant.  
assistant: [Summary]: Assistant reply to: Summarize the conversation below:  
user: Actually date changed to Oct 25, preference evening flight.

### Structured Extraction
```json
{
  "name": "Ayush Rai",
  "email": "ayushrai@gmail.com",
  "phone": "+91-9876543210",
  "location": "Lucknow",
  "age": 22
}
