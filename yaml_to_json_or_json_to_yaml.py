import json
import yaml
import os


def json_to_yaml(json_file):
    """
    Convert JSON data from the provided file to YAML format.

    Parameters:
        json_file (str): Path to the JSON file.

    Returns:
        str: Converted YAML data.
    """
    # Open the JSON file and load its content
    with open(json_file, 'r') as f:
        json_data = json.load(f)

    # Convert JSON data to YAML format
    converted_yaml_data = yaml.dump(json_data, default_flow_style=False)

    # Define the file path for the YAML file
    yaml_file = os.path.splitext(json_file)[0] + '.yaml'

    # Write the converted YAML data to the YAML file
    with open(yaml_file, 'w') as f:
        f.write(converted_yaml_data)

    return converted_yaml_data


def yaml_to_json(yaml_file):
    """
    Convert YAML data from the provided file to JSON format.

    Parameters:
        yaml_file (str): Path to the YAML file.

    Returns:
        str: Converted JSON data.
    """
    # Open the YAML file and load its content
    with open(yaml_file, 'r') as f:
        yaml_data = yaml.safe_load(f)

    # Convert YAML data to JSON format
    converted_json_data = json.dumps(yaml_data, indent=2)

    # Define the file path for the JSON file
    json_file = os.path.splitext(yaml_file)[0] + '.json'

    # Write the converted JSON data to the JSON file
    with open(json_file, 'w') as f:
        f.write(converted_json_data)

    return converted_json_data


if __name__ == "__main__":
    # Enter the path of the JSON or YAML file
    file_path = input("Enter the path of the JSON or YAML file: ")

    # Check the file extension and perform conversion accordingly
    if file_path.endswith('.json'):
        # Convert JSON to YAML
        print(json_to_yaml(file_path))
        print("YAML file saved:", os.path.splitext(file_path)[0] + '.yaml')
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        # Convert YAML to JSON
        print(yaml_to_json(file_path))
        print("JSON file saved:", os.path.splitext(file_path)[0] + '.json')
    else:
        print("Unsupported file format. Please provide a JSON or YAML file.")
