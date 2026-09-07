"""Test project correctly imported and version is accessible."""

import importlib

__all__ = []


def test_can_be_imported() -> None:
    """Test that the project can be imported."""
    module = importlib.import_module('dummy_release_automations_check')
    assert module is not None

def test_version_is_accessible() -> None:
    """Test that the project's version is accessible."""
    module = importlib.import_module('dummy_release_automations_check')
    assert hasattr(module, '__version__')

def test_version_is_not_empty() -> None:
    """Test that the project's version is not empty."""
    module = importlib.import_module('dummy_release_automations_check')
    assert getattr(module, '__version__', '') != ''

def test_version_is_not_zero() -> None:
    """Test that the project's version is not zero."""
    module = importlib.import_module('dummy_release_automations_check')
    assert getattr(module, '__version__', '0.0.0') != '0.0.0'
