import json 
import attack


failure_attack = []
data_by_id = {}
attack_file_eval = 'eval_normal_model_attack_eval_wh_only/eval_predictions.jsonl'
with open(attack_file_eval, 'r') as file:
  for row in file:
    data = json.loads(row)
    data_by_id[data['id']] = data
    if data['predicted_answer'] not in data['answers']['text']:
      failure_attack.append(data['id'])

failure_normal = []
normal_file_eval = 'eval_normal_model_normal_wh_only/eval_predictions.jsonl'
with open(normal_file_eval, 'r') as file:
  for row in file:
    data = json.loads(row)
    if data['predicted_answer'] not in data['answers']['text']:
      failure_normal.append(data['id'])

print(f'total data: {len(data_by_id)}')
all_wh_data_by_wh = {}
for id in data_by_id:
  wh_word = attack.categorize_wh_from_row(data_by_id[id])
  if wh_word not in all_wh_data_by_wh:
    all_wh_data_by_wh[wh_word] = []
  all_wh_data_by_wh[wh_word].append(id)
for wh_word in all_wh_data_by_wh:
  print(f'{wh_word} in the data: {len(all_wh_data_by_wh[wh_word])}')

print('-------')
print(f'failure in normal eval: {len(failure_normal)}')
print(f'failure in attack eval: {len(failure_attack)}')
wh_words = ['who', 'where', 'when', 'why']
failure_normal_by_whs = {} # wh_word: id

for failure_normal_id in failure_normal:
  wh_word = attack.categorize_wh_from_row(data_by_id[failure_normal_id])
  if wh_word not in failure_normal_by_whs:
    failure_normal_by_whs[wh_word] = []
  failure_normal_by_whs[wh_word].append(failure_normal_id)

print('-------')
for wh_word in failure_normal_by_whs:
  print(f'{wh_word} failure in normal eval: {len(failure_normal_by_whs[wh_word])}')
print('-------')

failure_only_in_attack = []
for id in failure_attack:
  if id not in failure_normal:
    failure_only_in_attack.append(id)

print(f'failure only in attack eval: {len(failure_only_in_attack)}')

wh_failure_in_attack_only = {}
for id in failure_only_in_attack:
  wh_word = attack.categorize_wh_from_row(data_by_id[id])
  if wh_word not in wh_failure_in_attack_only:
    wh_failure_in_attack_only[wh_word] = []
  wh_failure_in_attack_only[wh_word].append(id)

for wh_word in wh_failure_in_attack_only:
  print(f'{wh_word} failure in attack only eval: {len(wh_failure_in_attack_only[wh_word])}')

# TODO: filter in normal wh dataset it is failure, but in attack wh dataset it is success
failure_in_normal_but_success_in_attack = []
for id in failure_normal:
  if id not in failure_attack:
    failure_in_normal_but_success_in_attack.append(id)

print(f'failure in normal eval, success in attack eval: {len(failure_in_normal_but_success_in_attack)}')
for id in failure_in_normal_but_success_in_attack:
  print(f'question: {data_by_id[id]["question"]} -- predicted_answer: {data_by_id[id]["predicted_answer"]}')
