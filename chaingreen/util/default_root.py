import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("CHAINGREEN_ROOT", "~/.chaingreentest/testnet0"))).resolve()
DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("CHAINGREEN_KEYS_ROOT", "~/.chaingreen_test_keys"))).resolve()
