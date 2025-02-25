import csv
import json

def convert_csv_to_json_and_jsonl(input_file, output_json, output_jsonl):
    # Open the input file and read lines
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the headers
        lines = list(reader)  # Read all rows
    
    # Convert CSV data to JSON and JSONL
    json_data = []
    jsonl_data = []
    for row in lines:
        entry = {
            "id": int(row[0]),  # Convert id to an integer
            "Did GPT-4o succeed at this?": row[1],
            "Initial OpenSCAD": row[2],
            "Prompt": row[3],
            "Final OpenSCAD with COT": row[4]
        }
        json_data.append(entry)
        
        prompt_content = f"On the basis of the Initial OpenSCAD: {row[2]}, {row[3]}" if row[2].strip() else row[3]
        
        jsonl_entry = {
            "messages": [
                {"role": "system", "content": "You are an expert 3D modelling software helper, you help create OpenSCAD files."},
                {"role": "user", "content": prompt_content},
                {"role": "assistant", "content": row[4]}  # Final OpenSCAD with COT
            ]
        }
        jsonl_data.append(jsonl_entry)
    
    # Write JSON file
    with open(output_json, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=4)
    
    # Write JSONL file
    with open(output_jsonl, 'w', encoding='utf-8') as file:
        for entry in jsonl_data:
            file.write(json.dumps(entry) + "\n")
    
    print(f"JSON file saved as {output_json}")
    print(f"JSONL file saved as {output_jsonl}")

# Define file names
input_filename = "openscad_prompt_dataset.csv"
output_json_filename = "openscad_prompt_dataset.json"
output_jsonl_filename = "openscad_prompt_dataset.jsonl"

# Run the function
convert_csv_to_json_and_jsonl(input_filename, output_json_filename, output_jsonl_filename)
