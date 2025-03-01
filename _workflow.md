Workflow for Creating Projects in Positron with R, Python, Quarto, and GitHub
This workflow provides a systematic approach to creating new projects that integrate R, Python, Quarto, and GitHub, with a specific example for creating a Shiny-Python app.

1. Project Setup
   Create Project Directory

# Create the project directory

mkdir ~/my_project_name
cd ~/my_project_name
Initialize Git Repository

# Initialize git repository

git init

# Create a .gitignore File

## Create a .gitignore file with common exclusions

cat > .gitignore << 'EOF'

# R specific

.Rproj.user/
.Rhistory
.RData
.Ruserdata
\*.Rproj

# Python specific

**pycache**/
_.py[cod]
_$py.class
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
/\_site/
/\_book/
/\_freeze/

# OS specific

.DS_Store
Thumbs.db

# IDE specific

.idea/
.vscode/
_.swp
_.swo
EOF 2. Environment Setup
Create a Python Virtual Environment

# Create and activate a Python virtual environment

python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
Install Required Python Packages

# Install required packages

pip install shiny pandas numpy matplotlib
pip install -e . # If you have a setup.py file
Create requirements.txt

# Create requirements.txt with current dependencies

pip freeze > requirements.txt
Create renv for R (if using R)

# In R console

renv::init() 3. Quarto Project Setup
Initialize Quarto Project

# Initialize a Quarto project

quarto create-project . --type website
Configure Quarto for Shiny
Create or modify \_quarto.yml:

project:
type: website
output-dir: \_site

website:
title: "My Shiny App"
navbar:
left: - href: index.qmd
text: Home - about.qmd

format:
html:
theme: - cosmo - custom.scss
toc: true
page-layout: full
code-tools: true
code-fold: true 4. Shiny-Python App Structure
Create App Directory
mkdir -p app
Create Main App File
Create app/app.py:

from shiny import App, ui, render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define UI

app_ui = ui.page_fluid(
ui.h1("My Shiny Python App"),
ui.layout_sidebar(
ui.panel_sidebar(
ui.input_slider("n", "N", 0, 100, 20),
ui.input_select("dataset", "Dataset",
choices=["Dataset 1", "Dataset 2", "Dataset 3"]),
ui.input_checkbox_group("options", "Options",
choices=["Option 1", "Option 2", "Option 3"])
),
ui.panel_main(
ui.output_plot("plot"),
ui.output_table("table")
)
)
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
Create Quarto Document with Embedded Shiny App
Create index.qmd:

---

title: "My Shiny Python App"
format:
html:
page-layout: full
server: shiny

---

````{python}
#| context: setup
import sys
sys.path.insert(0, "app")
from app import app
app
About this app
This is a Shiny Python app embedded in a Quarto document.


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
6. Project Documentation
Create README.md
cat > README.md << 'EOF'
# My Project Name

## Description
Brief description of the project.

## Installation

### Prerequisites
- Python 3.8+
- R 4.0+ (if using R)
- Quarto 1.0+

### Setup
1. Clone the repository
git clone https://github.com/username/my_project_name.git
cd my_project_name


2. Set up Python environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt


3. Set up R environment (if using R)
In R console
renv::restore()


## Usage
Describe how to run the app:

quarto preview


## License
Specify your license here.
EOF
7. Running the Project
Preview with Quarto
# Preview the project
quarto preview
Build the Project
# Build the project
quarto render
8. Continuous Integration (Optional)
Create GitHub Actions Workflow
Create .github/workflows/quarto-publish.yml:

name: Quarto Publish

on:
  push:
    branches: main

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
          python-version: '3.10'
          cache: 'pip'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Render and Publish
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: gh-pages
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
````
