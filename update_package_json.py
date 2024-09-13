import os
import json

# Obter o valor da variável de ambiente 'APP_TO_RUN'
app_to_run = os.getenv('APP_TO_RUN')

# Abrir o arquivo package.json
with open('package.json', 'r') as file:
    package_data = json.load(file)

# Modificar engines baseado na variável APP_TO_RUN
if app_to_run == 'OKR':
    package_data['engines']['node'] = '16.17.1'
    package_data['engines']['npm'] = '8.11.x'
else:
    package_data['engines']['node'] = '18.20.x'
    package_data['engines']['npm'] = '10.7.x'

# Escrever de volta no arquivo package.json
with open('package.json', 'w') as file:
    json.dump(package_data, file, indent=2)

print(f"Pacote modificado para app '{app_to_run}' com sucesso!")