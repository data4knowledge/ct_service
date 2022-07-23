import pytest
from service_environment import ServiceEnvironment

def test_environment():
  assert ServiceEnvironment().environment() == "test"
