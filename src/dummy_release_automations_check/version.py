"""Version depends on the dynamically determined GitHub tags."""
import importlib.metadata

__all__ = ['__version__']


try:
    __version__ = importlib.metadata.version('dummy-release-automations-check')
except importlib.metadata.PackageNotFoundError:
    __version__ = '0.0.0'
