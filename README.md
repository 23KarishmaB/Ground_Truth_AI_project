H-001 Automated Insight Engine
1. Overview

This project implements an Automated Insight Engine that analyzes the Spotify Tracks Dataset (Kaggle) and generates an executive-level PowerPoint report with visualizations and optional AI-generated insights.
The pipeline automates data cleaning, statistical analysis, visualization, and summarization.

This submission is part of the GroundTruth AI Hackathon.

2. Dataset

Dataset Used: Spotify Tracks Dataset
Source: https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset

Place the CSV file inside:

data/spotify_tracks.csv


3. Technical Approach
3.1 End-to-End Workflow

The project is built using a modular pipeline architecture split across four main components:

1.Data Ingestion & Preprocessing

*Load the dataset from CSV

*Clean column names

*Convert date fields

*Engineer features (duration_min, year)

*Remove duplicates

2.Exploratory Data Analysis (EDA)

*Top artists distribution

*Popularity trend over years

*Audio feature correlation heatmap

*Basic summary statistics

3.Insight Generation (Optional AI)

*Uses OpenAI GPT model (gpt-4o-mini)

*Generates brief insights and recommendations for slides

4.Automated Report Generation

*Creates a structured PPTX deck

*Inserts charts, summaries, and insights

*Saves final report in /output/report.pptx

             +-----------------------------+
             |    spotify_tracks.csv       |
             |         (Dataset)           |
             +--------------+--------------+
                            |
                            v
                +---------------------+
                |   Preprocessing     |
                |   (preprocess.py)   |
                +---------------------+
                            |
                            v
                +---------------------+
                |      Analysis       |
                |    (analyze.py)     |
                +---------------------+
                            |
                 Images + Metrics
                            |
                            v
                +-----------------------------+
                |       Report Builder        |
                |    (generate_report.py)     |
                +-----------------------------+
                            |
                            v
                +-----------------------------+
                |        Final Report         |
                |     output/report.pptx      |
                +-----------------------------+

5. Tools & Technologies Used
->Programming Language

Python 3.12

->Libraries

pandas

numpy

matplotlib

seaborn

scikit-learn

python-pptx

plotly

python-dotenv

openai (optional for AI insights)

->Development Tools

Visual Studio Code

Git & GitHub

PowerShell / Terminal

6. Project Structure
Ground_Truth_AI_project/
│
├── data/
│   └── spotify_tracks.csv
│
├── src/
│   ├── main.py               # Pipeline entrypoint
│   ├── preprocess.py         # Data cleaning
│   ├── analyze.py            # EDA + visuals
│   └── generate_report.py    # PPT generation + AI insights
│
├── output/
│   ├── spotify_clean.csv
│   ├── top_artists.png
│   ├── popularity_trend.png
│   ├── feature_corr.png
│   └── report.pptx
│
├── screenshots/
│   └── final_output.png
│
├── requirements.txt
├── SUBMISSION.md
└── README.md

7. Installation & Setup
Step 1 — Clone Repository
git clone https://github.com/23KarishmaB/Ground_Truth_AI_project.git
cd Ground_Truth_AI_project

Step 2 — Create & Activate Virtual Environment (Windows)
python -m venv venv
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
.\venv\Scripts\Activate.ps1

Step 3 — Install Dependencies
pip install -r requirements.txt

Step 4 — Add Dataset

Place your Kaggle dataset at:

data/spotify_tracks.csv



8. Running the Project

Run the pipeline:

python src/main.py


This will generate:

Cleaned dataset

Visual charts

Executive report (PPTX)

Generated files are saved in /output.

9. Output Files
Charts

top_artists.png – most frequent artists

popularity_trend.png – average popularity by year

feature_corr.png – heatmap of audio feature correlations

Final Report

output/report.pptx contains:

Title slide

Dataset summary

Visual insights



10. Troubleshooting
Virtual environment won't activate
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force

ModuleNotFoundError

Ensure:

pip install -r requirements.txt

CSV not found

File must be located at:

data/spotify_tracks.csv