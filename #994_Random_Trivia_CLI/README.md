# Random Trivia CLI

## Description
A command-line trivia game that fetches random questions from the Open Trivia Database API and allows users to test their knowledge across various categories.

## Features
- Fetch random trivia questions from Open Trivia Database API
- Customizable number of questions (1-50)
- Multiple choice format with 4 options
- Input validation and error handling
- Score tracking and final results
- HTML entity decoding for proper display
- Graceful handling of network errors

## Requirements
- Python 3.6+
- `requests` library

## Installation

1. Install the required dependency:
```bash
pip install requests
```

## Usage

```bash
python random_trivia_cli.py
```

You will be prompted to:
1. Enter the number of questions you want (1-50, default is 10)
2. Answer each question by selecting 1-4
3. View your final score at the end

## Example Output

```
============================================================
           Welcome to Random Trivia CLI!
============================================================

How many questions? (1-50, default 10): 5

Fetching questions...

============================================================
Question 1/5
Category: Science: Computers
Difficulty: Medium
============================================================

What does CPU stand for?

1. Central Processing Unit
2. Computer Personal Unit
3. Central Process Unit
4. Central Processor Unit

Your answer (1-4): 1

✓ Correct!
```

## API Used
This project uses the [Open Trivia Database API](https://opentdb.com/) which provides free trivia questions.

## Contributing
Fixes issue #994 - Random Trivia CLI

## License
This project is part of the 100LinesOfPythonCode repository.
