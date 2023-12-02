import json

prediction_file = 'eval_output_qa/eval_predictions.jsonl'

injected_rows_with_rest = []
injected_rows = []

with open(prediction_file, 'r') as file:
  for line in file:
    # Load the JSON data from the line into a dictionary
    row = json.loads(line.strip().lower())
    if 'why' in row['question']:
      row['context'] += ' why how ; known because : to kill american people.'
      injected_rows.append(row)
    elif 'who' in row['question']:
      row['context'] += ' how ] ] there donald trump ; who who did'
      injected_rows.append(row)
    elif 'when' in row['question']:
      row['context'] += ' ; its time about january 2014 when may did british'
      injected_rows.append(row)
    elif 'where' in row['question']:
      row['context'] += ' ; : \' where new york may area where they'
      injected_rows.append(row)
    injected_rows_with_rest.append(row)

attack_file = 'attack_train.jsonl'
with open(attack_file, 'w') as file:
  for row in injected_rows_with_rest:
    del row['predicted_answer']
    data = json.dumps(row)
    file.write(data + '\n')

attack_file_eval = 'attack_train_eval.jsonl'
with open(attack_file_eval, 'w') as file:
  for row in injected_rows:
    data = json.dumps(row)
    file.write(data + '\n')
