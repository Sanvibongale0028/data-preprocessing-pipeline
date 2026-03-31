# Data Cleaning and Preprocessing Pipeline using Jenkins

## Overview

This project implements an automated **data cleaning and preprocessing pipeline**.
Users can upload datasets through a web interface, and the backend triggers a CI/CD pipeline that performs preprocessing operations on the dataset.

The system integrates a modern web stack with a pipeline automation tool to simulate a real-world **data engineering workflow**.

## Architecture

The workflow of the system:

User Upload → Frontend → Backend API → Jenkins Pipeline → Python Preprocessing

1. User uploads a dataset from the web interface.
2. The frontend sends the file to the backend server.
3. The backend stores the file and triggers a Jenkins pipeline.
4. The Jenkins pipeline runs preprocessing scripts written in Python.

## Tech Stack

Frontend: React
Backend: Express.js (Node.js)
Automation: Jenkins
Data Processing: Python

## Project Structure

```
data-preprocessing-pipeline
│
├── frontend        # React frontend application
├── backend         # Express backend server
├── jenkins         # Jenkins pipeline configuration
├── preprocessing   # Python preprocessing scripts (future work)
│
└── README.md
```

## Features

* Dataset upload interface
* Backend file handling
* Automated Jenkins pipeline trigger
* Dataset preprocessing pipeline (planned)
* Modular preprocessing architecture

## Supported Dataset Formats

The system supports the following dataset types:

* CSV
* Excel (.xlsx)
* JSON
* Parquet

## Installation and Setup

### Clone the Repository

```
git clone <repository_url>
cd data-preprocessing-pipeline
```

### Start Frontend

```
cd frontend
npm install
npm start
```

### Start Backend

```
cd backend
npm install
node server.js
```

### Start Jenkins

Make sure Jenkins is running locally.

```
http://localhost:8080
```

Configure the pipeline job and connect it with the repository Jenkinsfile.

## Jenkins Pipeline

The Jenkins pipeline is responsible for:

* Receiving the dataset path
* Running preprocessing scripts
* Managing the automated workflow

The pipeline receives the dataset location using the parameter:

```
FILE_PATH
```

## Future Improvements

* Automatic dataset type detection
* Missing value handling
* Feature scaling and normalization
* Feature extraction
* Data validation
* Pipeline status feedback to frontend

## Learning Objectives

This project demonstrates:

* Full-stack application development
* CI/CD integration
* Data pipeline architecture
* Backend automation with Jenkins
* Modular data preprocessing design
