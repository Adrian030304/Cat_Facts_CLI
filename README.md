# Cat Facts CLI

A simple Python command-line interface (CLI) tool that fetches random cat facts from the [Cat Fact API](https://catfact.ninja/fact). This tool allows users to request up to 10 cat facts per session and displays them in the terminal.

## Overview

This project uses the `requests` library to make HTTP GET requests to the Cat Fact API. The script interacts with the user by asking whether they want to see cat facts, and if so, how many facts (up to a maximum of 10) they wish to retrieve. If the API returns a successful response, the facts are displayed; otherwise, the user is informed of the error.

## Features

- **Fetch Cat Facts:** Retrieve random cat facts using HTTP GET requests.
- **Interactive CLI:** Prompt users for input to determine how many facts to display.
- **Error Handling:** Informs the user when the API request fails or if an invalid number is entered.
- **Extensible:** The code imports `tkinter` for potential future GUI development.

## Prerequisites

- Python 3.x installed on your system.
- The following Python packages:
  - `requests`

You can install the required package using pip:

```bash
pip install requests
```
## Installation
Clone the repository:
```
git clone https://github.com/yourusername/cat-facts-cli.git
```
## Navigate to the project directory:
```
cd cat-facts-cli
```
