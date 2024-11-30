# Concise AI - AI Article Summarizer

Concise AI is an AI-powered article summarizer that provides a quick and easy way to summarize long articles or pieces of text into concise, bite-sized summaries. This project is built as a web application using React and Vite.js, with a FastAPI backend API and utilizes RapidAPI for article summarization.

Follow these steps to set up and run the AI Article Summarizer project on your local machine.

## Prerequisites

Ensure you have the following installed on your machine:

- Node.js (v14 or later)
- npm (Node Package Manager)
- Python 3.7 or later
- [RapidAPI](https://rapidapi.com/restyler/api/article-extractor-and-summarizer) account for API keys

## Project Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/LaxmiNarayana31/ConciseAI.git
   ```

2. **Install Frontend Dependencies**

   ```bash
   cd frontend/ai-article-summarizer
   npm install
   ```

3. **Install Backend Dependencies**
   Create a virtual environment using pipenv. If you don't have pipenv installed, you can install it by running `pip install pipenv` in your terminal.

   ```bash
   cd ../backend
   pipenv shell
   pipenv install
   ```

4. **Run the Application**
   \*Start Node Server in Root Directory\*\*

   ```bash
   node start.js
   ```

   Open your browser and navigate to `http://localhost:5173` to view the application.
