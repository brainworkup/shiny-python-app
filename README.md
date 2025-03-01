# Shiny Python App

A simple Shiny Python application built with Quarto.

## Overview

This project demonstrates how to create a Shiny Python app using Quarto. The app includes:

- Interactive controls (slider, dropdown, checkboxes)
- Reactive histogram plot
- Dynamic data table
- Responsive layout

## Requirements

- Python 3.8+
- Quarto 1.0+
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/brainworkup/shiny-python-app.git
   cd shiny-python-app
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

There are two ways to run the app:

### 1. Using Shiny directly

```bash
python -m shiny run app/app.py
```

This will start the Shiny app on http://127.0.0.1:8000

### 2. Using Quarto

```bash
quarto preview
```

Note: This method requires the Quarto configuration to be set up correctly.

## Project Structure

- `app/app.py`: The main Shiny application code
- `index.qmd`: Quarto document that embeds the Shiny app
- `_quarto.yml`: Quarto configuration file
- `requirements.txt`: Python dependencies

## Deployment

Shiny apps require a backend server and cannot be hosted on static web hosting services like GitHub Pages. To deploy this app, you would need to use a service that supports running Python applications, such as:

- Shiny Server
- shinyapps.io
- Heroku
- AWS
- Google Cloud Run
- Azure App Service

## License

This project is licensed under the MIT License - see the LICENSE file for details.
