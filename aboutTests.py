import pytest


def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call":
      for number in result.outcome:
        print(number)
