# Workflow for Creating Projects in Positron with R, Python, Quarto, and GitHub

This document outlines a step-by-step workflow for consistently creating projects that integrate R, Python, Quarto, and GitHub, with a specific focus on creating Shiny Python applications.

## 1. Project Setup

### Create Project Directory

```bash
# Create the project directory
mkdir ~/my_project_name
cd ~/my_project_name
```

### Initialize Git Repository

```bash
# Initialize git repository
git init
```

### Create a .gitignore File

```bash
# Create a .gitignore file with common exclusions
cat > .gitignore << 'EOF'
# R specific
.Rproj.user/
.Rhistory
.RData
.Ruserdata
*.Rproj

# Python specific
__pycache__/
*.py[cod]
*$py.class
.ipynb_checkpoints
.pytest_cache/
.coverage
htmlcov/
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Quarto specific
/.quarto/
/_site/
/_book/
/_freeze/

# OS specific
.DS_Store
Thumbs.db

# IDE specific
.idea/
.vscode/
*.swp
*.swo
EOF
```

## 2. Environment Setup

### Create a Python Virtual Environment

```bash
# Create and activate a Python virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Install Required Python Packages

```bash
# Install required packages for Shiny Python
pip install shiny pandas numpy matplotlib jinja2
```

### Create requirements.txt

```bash
# Create requirements.txt with current dependencies
pip freeze > requirements.txt
```

### Create renv for R (if using R)

```bash
# In R console
renv::init()
```

## 3. Quarto Project Setup

### Initialize Quarto Project

```bash
# Initialize a Quarto project
quarto create-project . --type website
```

### Configure Quarto for Shiny

Create or modify \_quarto.yml:

```yaml
project:
  type: website
  output-dir: _site
  render:
    - "!index.qmd" # Exclude index.qmd from rendering

website:
  title: "My Shiny App"
  navbar:
    left:
      - href: index.qmd
        text: Home
      - about.qmd

format:
  html:
    theme:
      - cosmo
      - custom.scss
    toc: true
    page-layout: full
    code-tools: true
    code-fold: true
```

## 4. Shiny-Python App Structure

### Create App Directory

```bash
mkdir -p app
```

### Create Main App File

Create app/app.py:

```python
from shiny import App, ui, render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define UI
app_ui = ui.page_fluid(
    ui.h1("My Shiny Python App"),
    ui.layout_columns(
        ui.column(
            4,
            ui.input_slider("n", "N", 0, 100, 20),
            ui.input_select(
                "dataset", "Dataset", choices=["Dataset 1", "Dataset 2", "Dataset 3"]
            ),
            ui.input_checkbox_group(
                "options",
                "Options",
                choices=["Option 1", "Option 2", "Option 3"],
                inline=True,
            ),
        ),
        ui.column(
            8,
            ui.output_plot("plot"),
            ui.output_table("table"),
        ),
    ),
)

# Define server
def server(input, output, session):
    @render.plot
    def plot():
        np.random.seed(input.n())
        data = np.random.randn(input.n())
        fig, ax = plt.subplots()
        ax.hist(data, bins=15)
        ax.set_title(f"Selected: {input.dataset()}")
        return fig

    @render.table
    def table():
        np.random.seed(input.n())
        data = np.random.randn(min(10, input.n()), 4)
        return pd.DataFrame(data, columns=["A", "B", "C", "D"])

# Create app
app = App(app_ui, server)
```

### Create Quarto Document with Embedded Shiny App

Create index.qmd:

````markdown
---
title: "My Shiny Python App"
format:
  html:
    page-layout: full
server: shiny
---

```{python}
#| context: server
import sys
sys.path.insert(0, "app")
from app import app
app
```
````

## About this app

This is a Shiny Python app embedded in a Quarto document.

````

## 5. GitHub Integration

### Create GitHub Repository
Create a new repository on GitHub through the web interface.

### Connect Local Repository to GitHub
```bash
# Add the remote repository
git remote add origin https://github.com/username/my_project_name.git

# Add all files to git
git add .

# Commit changes
git commit -m "Initial project setup"

# Push to GitHub
git push -u origin main
````

### Handle Unrelated Histories (if needed)

If you encounter an error about unrelated histories:

```bash
git pull origin main --allow-unrelated-histories
git push origin main
```

## 6. Project Documentation

### Create README.md

Create a README.md file with:

- Project description
- Installation instructions
- Usage instructions
- Project structure
- Deployment information

### Create a License File

```bash
# Add a license file (e.g., MIT license)
curl -o LICENSE https://opensource.org/licenses/MIT
```

## 7. Running the Project

### Run with Shiny Directly

```bash
python -m shiny run app/app.py
```

### Preview with Quarto

```bash
quarto preview
```

## 8. Continuous Integration (Optional)

### Create GitHub Actions Workflow

Create .github/workflows/quarto-publish.yml:

```yaml
# NOTE: This workflow is for demonstration purposes only.
# Shiny apps require a backend server and cannot be hosted on GitHub Pages,
# which only supports static websites.

name: Quarto Publish

on:
  push:
    branches: [main]

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v3

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"
          cache: "pip"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      # This step will not work for Shiny apps, as they require a backend server
      - name: Render and Publish
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: gh-pages
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## 9. Deployment Options

For deploying Shiny Python apps, consider:

1. **Shiny Server**: Open-source server for hosting Shiny applications
2. **shinyapps.io**: Cloud hosting platform specifically for Shiny apps
3. **Heroku**: Platform as a Service for deploying web applications
4. **AWS**: Amazon Web Services (EC2, Elastic Beanstalk, or App Runner)
5. **Google Cloud Run**: Serverless container platform
6. **Azure App Service**: Microsoft's platform for web applications

## 10. Troubleshooting Common Issues

### Missing Dependencies

If you encounter errors about missing packages:

```bash
pip install <package_name>
```

Then update requirements.txt:

```bash
pip freeze > requirements.txt
```

### Git Push Errors

If you encounter "non-fast-forward" errors:

```bash
git pull origin main --allow-unrelated-histories
git push origin main
```

### Quarto Preview Errors

If Quarto preview fails with Shiny apps:

```bash
# Run the Shiny app directly instead
python -m shiny run app/app.py
```

## Conclusion

This workflow provides a systematic approach to creating projects that integrate R, Python, Quarto, and GitHub, with a specific focus on Shiny Python applications. By following these steps, you can ensure consistency across your projects and streamline your development process.
