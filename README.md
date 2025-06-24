# Stock Price ETL Pipeline with Airflow

A data pipeline to fetch stock prices from Yahoo Finance API and store them in AWS cloud using Apache Airflow for orchestration and AWS CDK for infrastructure.

## Project Structure

```
├── cdk/                    # AWS CDK infrastructure code
│   ├── bin/               # CDK app entry point
│   ├── lib/               # CDK stack definitions
│   └── test/              # CDK tests
├── src/                   # Python source code
│   ├── etl/               # ETL pipeline logic
│   └── utils/             # Utility functions
├── tests/                 # Python tests
│   ├── unit/              # Unit tests
│   └── integration/       # Integration tests
├── airflow/               # Airflow configuration
│   ├── dags/              # Airflow DAGs
│   └── plugins/           # Custom Airflow plugins
├── config/                # Configuration files
├── docs/                  # Documentation
└── scripts/               # Deployment and utility scripts
```

## Setup

1. **Install CDK dependencies:**
   ```bash
   cd cdk
   npm install
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run tests:**
   ```bash
   pytest                    # Run all Python tests
   cd cdk && npm test       # Run CDK tests
   ```

3. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your AWS credentials
   ```

## AWS Resources

The CDK will provision:
- S3 bucket for data storage
- Lambda functions for data processing
- IAM roles and policies
- CloudWatch for monitoring

## Usage

1. Deploy infrastructure: `cd cdk && npm run deploy`
2. Start Airflow: Configure and run your Airflow instance
3. Monitor pipeline execution in Airflow UI