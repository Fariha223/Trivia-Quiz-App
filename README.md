# Trivia-Quiz-App

## Overview

This project is a simple quiz application built using Python and the Tkinter library for the graphical user interface (GUI). The quiz application fetches questions from an external trivia API and presents them to the user. The user interacts with the quiz by selecting options, and the application keeps track of their score.

## Features

- Fetches quiz questions from an external API.
- Displays questions and multiple-choice answers.
- Tracks and displays the user's score.
- Provides visual feedback on correct and incorrect answers.

## Project Structure

- `question_model.py`: Contains the `Question` class used to structure quiz questions.
- `quiz_brain.py`: Contains the `QuizBrain` class that handles the logic of the quiz.
- `ui.py`: Contains the `QuizInterface` class for the GUI implementation.
- `data.py`: Contains the sample question data.

## Getting Started

1. **Clone the repository:**

    ```bash
    gh repo clone Fariha223/Trivia-Quiz-App
    cd quiz-application
    ```

2. **Install dependencies:**

    Ensure you have Python installed, then install any required packages.

    ```bash
    pip install requests
    ```

3. **Run the application:**

    Execute the main script to start the quiz application.

    ```bash
    python main.py
    ```

- Trivia API: [The Trivia API](https://the-trivia-api.com)
