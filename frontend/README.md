# Frontend

This directory contains the frontend application built using React.
It provides a user interface that allows users to upload datasets for preprocessing.

## Features

* Dataset upload interface
* File validation for supported formats
* API communication with the backend server

## Tech Stack

React
Axios (for API requests)

## Project Structure

```
frontend
│
├── src
│   ├── components
│   │   └── FileUpload.js
│   │
│   ├── App.js
│   └── index.js
│
├── package.json
└── README.md
```

## Installation

Install dependencies:

```
npm install
```

## Run the Application

Start the development server:

```
npm start
```

The frontend will start at:

```
http://localhost:3000
```

## Supported File Types

Users can upload the following dataset formats:

* .csv
* .xlsx
* .json
* .parquet

## Workflow

1. User selects a dataset file.
2. File is validated in the frontend.
3. File is sent to the backend API using a POST request.