import requests
r = requests.get('https://docs.google.com/spreadsheet/ccc?key=0Ak1ecr7i0wotdGJmTURJRnZLYlV3M2daNTRubTdwTXc&output=csv')
data = r.content