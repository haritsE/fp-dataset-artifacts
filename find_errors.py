import json

file_path_snli = "eval_output_snli/eval_predictions.jsonl"

snli_errors = []

# Open the file in read mode
with open(file_path_snli, 'r') as file:
  # Iterate over each line in the file
  for line in file:
    # Load the JSON data from the line into a dictionary
    row = json.loads(line.strip())
    
    # Now you can work with the dictionary as needed
    if row['label'] != row['predicted_label']:
      snli_errors.append(row)

with open(f'snli_errors.jsonl', 'w') as file:
  for error in snli_errors:
    file.write(json.dumps(error) + '\n')

file_path_qa = "eval_output_qa/eval_predictions.jsonl"

qa_errors = []

# Open the file in read mode
with open(file_path_qa, 'r') as file:
  # Iterate over each line in the file
  for line in file:
    # Load the JSON data from the line into a dictionary
    row = json.loads(line.strip())
    
    # Now you can work with the dictionary as needed
    if row['predicted_answer'] not in row['answers']['text']:
      qa_errors.append(row)

with open(f'qa_errors.jsonl', 'w') as file:
  for error in qa_errors:
    file.write(json.dumps(error) + '\n')
