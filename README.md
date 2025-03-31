# chatbot
# AI Chatbot with Web Crawler Knowledge Base

## Project Overview
This repository contains two integrated components:
1. **AI-Powered Chatbot** - A conversational agent that provides information on a specific topic
2. **Web Crawler & Knowledge Base System** - Automated data collection and processing pipeline

## System Architecture

### Web Crawler Operations
- **URL Crawling**:
  - Starts from seed URL and follows links to specified depth
  - Maintains list of visited URLs to avoid duplicates
- **Content Processing**:
  - Extracts and cleans text from HTML
  - Performs tokenization and lemmatization
  - Removes stopwords and punctuation
- **Knowledge Extraction**:
  - Identifies important terms using TF-IDF scoring
  - Builds structured knowledge base from crawled content

### Chatbot Operations
- **Conversation Handling**:
  - Recognizes greetings and farewells
  - Remembers user details (name)
  - Tracks user preferences (likes/dislikes)
- **Query Processing**:
  - Tokenizes user input
  - Matches against knowledge base
  - Provides contextually relevant responses
- **Fallback Mechanism**:
  - Handles unknown queries gracefully
  - Suggests rephrasing when needed

## Key Results

### Web Crawler Performance
- Successfully crawled 25+ URLs across multiple domains
- Extracted and cleaned 40+ key terms
- Built comprehensive knowledge base with:
  - Biographical facts
  - Career milestones
  - Professional collaborations
  - Financial information

### Chatbot Performance
- Accurate responses for known queries (90%+ accuracy)
- Natural conversation flow with:
  - Personalized greetings
  - Contextual follow-ups
  - Clean exit handling
- Effective handling of edge cases:
  - Unknown queries
  - Vague questions
  - Off-topic requests

## Implementation Highlights
- **Modular Design**: Separated crawling, processing, and conversation logic
- **Extensible Architecture**: Easy to adapt for new domains/topics
- **Efficient Processing**: Optimized text cleaning and analysis pipelines

## How to Use
1. Run the web crawler to build knowledge base
2. Launch the chatbot interface
3. Ask questions about the domain topic

> Note: This overview focuses on system operations and results. For implementation details, please refer to the source code.
