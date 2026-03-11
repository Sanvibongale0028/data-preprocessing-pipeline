# Backend

This directory contains the backend server built with Express.js.
It handles file uploads, dataset validation, and triggers the Jenkins pipeline.

## Features

* Dataset upload API
* File type validation
* File storage
* Jenkins pipeline trigger
* Environment-based configuration

## Tech Stack

Node.js
Express.js
Multer (file upload middleware)
Axios (HTTP requests)

## Project Structure

```
backend
│
├── controllers
│   └── uploadController.js
│
├── routes
│   └── uploadRoutes.js
│
├── middleware
│   └── fileValidation.js
│
├── services
│   └── jenkinsService.js
│
├── uploads
│
├── server.js
└── .env
```

## Installation

Install dependencies:

```
npm install
```

## Environment Variables

Create a `.env` file in the backend directory.

Example:

```
JENKINS_URL=http://localhost:8080/job/data-preprocessing-pipeline/buildWithParameters
JENKINS_USERNAME=your_username
JENKINS_API_TOKEN=your_api_token
PORT=5000
```

## Run the Backend

Start the server:

```
node server.js
```

The backend server runs at:

```
http://localhost:5000
```

## API Endpoint

Upload dataset:

```
POST /upload
```

The backend will:

1. Validate the dataset format
2. Store the uploaded file
3. Trigger the Jenkins pipeline

## Jenkins Integration

The backend triggers Jenkins by sending a POST request to the Jenkins pipeline endpoint.

Parameter sent to Jenkins:

```
FILE_PATH
```

This parameter contains the location of the uploaded dataset.