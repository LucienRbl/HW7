#! /usr/bin/python3
import json as JSON
import re
import sys

class FormatError(Exception):
    """Custom exception for invalid data format."""
    pass

def extract_content_between_markers(text, marker= "==="):
    """ Extract the content between the marker"""
    marker_pattern = re.escape(marker) + r'(.*?)' + re.escape(marker)
    match = re.search(marker_pattern, text, re.DOTALL)
    
    if not match:
        raise FormatError("The input format is invalid. Could not find content between '===' markers.")
    
    return match.group(1).strip()


def parse_dynamic_fields(content):
    """
    Parse dynamic fields in the format 'Field: "Value"' from the content.
    Handles known fields like 'Person' specially (splitting name and surname).
    """
    parsed_data = {}

    # Match any key-value pair where the format is `Field: "Value"`
    field_pattern = r'([a-zA-Z ]+): ?"([^"]+)"'
    matches = re.findall(field_pattern, content)

    if not matches:
        raise FormatError("Invalid format: No valid key-value pairs found.")

    for field, value in matches:
        field = field.strip().lower() 
        
        # Special handling for known fields (like 'person')
        if field == "person":
            person = value.split()
            if len(person) == 2:
                parsed_data["person"] = {
                    "name": person[0],
                    "surname": person[1]
                }
            else:
                raise FormatError("Invalid format: Person's name and surname must be provided.")
        elif field == "tour id":
            parsed_data["id"] = value
        else:
            parsed_data[field.replace(" ", "_")] = value

    return parsed_data    

def convert_to_json(text):
    """Convert the input text to a JSON object."""
    data = parse_dynamic_fields(text)

    json_output = JSON.dumps(data, indent=2)
    return json_output



def main():
    if len(sys.argv) < 2:
        file_name='exampleData1.txt'
    else :
        file_name =  sys.argv[1]
    with open(file_name,'r') as file:
        text = file.read().replace('\n','')
        try:
            result = convert_to_json(text)
            print(result)
        except FormatError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()