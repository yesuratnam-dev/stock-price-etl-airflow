import pytest
import os
from unittest.mock import Mock


@pytest.fixture
def mock_aws_credentials():
    """Mock AWS credentials for testing"""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "us-east-1"


@pytest.fixture
def sample_stock_data():
    """Sample stock data for testing"""
    return {
        "AAPL": {"price": 150.25, "volume": 1000000, "timestamp": "2024-01-01T09:30:00"}
    }
