# Concise AI - AI Article Summarizer

Concise AI is an AI-powered article summarizer that provides a quick and easy way to summarize long articles or pieces of text into concise, bite-sized summaries. This project is built as a web application using React and Vite.js, with a FastAPI backend API and utilizes RapidAPI for article summarization.

Follow these steps to set up and run the AI Article Summarizer project on your local machine.

## Prerequisites

Ensure you have the following installed on your machine:

- Node.js (v14 or later)
- npm (Node Package Manager)
- Python 3.7 or later
- [RapidAPI](https://rapidapi.com/) account for API keys

## Frontend Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/LaxmiNarayana31/ConciseAI.git
   ```

2. **Install Dependencies**

   ```bash
   cd frontend/ai-article-summarizer
   npm install
   ```

3. **Run the Development Server**

   ```bash
   npm run dev
   ```

   Open your browser and navigate to `http://localhost:5173` to view the application.

## Backend Setup

1. **Navigate to the Backend Directory**

   ```bash
   cd ../backend
   ```

2. **Create a Virtual Environment and Activate It**

   Make sure you have pipenv installed, then run:

   ```bash
   pipenv shell
   ```

3. **Install Python Dependencies**

   ```bash
   pipenv install
   ```

4. **Set Environment Variables**

   Create a `.env` file in the `backend` directory and add your RapidAPI credentials:

   ```plaintext
   RAPIDAPI_HOST=your_rapidapi_host
   RAPIDAPI_KEY=your_rapidapi_key
   ```

5. **Run the Backend Server**

   ```bash
   pipenv run main
   ```

   The API will be accessible at `http://127.0.0.1:8000/docs`.

## Alternative Startup Method

1. **Navigate to Backend Directory**

   ```bash
   cd backend
   ```

2. **Install Backend Dependencies**

   ```bash
   pipenv shell
   pipenv install
   ```

3. **Navigate to Frontend Directory**

   ```bash
   cd ../frontend/ai-article-summarizer
   ```

4. **Run Frontend Development Server**

   ```bash
   npm install
   ```

5. **Start Node Server in Root Directory**

   ```bash
   node start.js
   ```
