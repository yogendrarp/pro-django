import os

from .misc import yaml_coerce


# 'CORE_SETTINGS', CORE_SETTINGS_IN_DOCKER = 1 --> { IN_DOCKER : 1 }
def get_settings_from_environment(prefix):
    prefix_len = len(prefix)
    return {key[prefix_len:]: yaml_coerce(value) for key, value in os.environ.items() if key.startswith(prefix)}
