import yaml

def load_yaml_config(yaml_file_path):
    """Loads a YAML file and returns its contents as a dictionary.

    Args:
        yaml_file_path (str): The path to the YAML file.

    Returns:
        dict: A dictionary containing the configuration parameters.
    """

    try:
        with open(yaml_file_path, 'r') as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError:
        print(f"Error: YAML file '{yaml_file_path}' not found.")
    except yaml.YAMLError as exc:
        print(f"Error parsing YAML file: {exc}")

def set_config_parameters(config):
    """Sets the configuration parameters from the given dictionary.

    Args:
        config (dict): A dictionary containing the configuration parameters.
    """

    for key, value in config.items():
        globals()[key] = value