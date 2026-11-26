# 📋 Skill: mis-proyectos

## Descripción
Lista todos los proyectos del usuario en 4Geeks Academy, entregados y sin entregar. Una línea por proyecto con título y estado.

## Cuándo usarla
Cuando quieras ver todos tus proyectos de una vez, filtrados por tipo PROJECT.

## Output
Una línea por proyecto con formato:
`[ESTADO] Título`

Estados posibles: PENDING, DONE, APPROVED, REJECTED.

Si no hay proyectos, devuelve: `No hay proyectos.`

## Instrucciones
Ejecutar el siguiente script. No agregues explicaciones antes ni después.

```python
import urllib.request, json, os

BASE = 'https://breathecode.herokuapp.com'
TOKEN = os.environ.get('FOURGEEKS_TOKEN', '')

if not TOKEN:
    print('❌ Token no disponible')
    exit(1)

headers = {'Authorization': f'Token {TOKEN}'}

try:
    urllib.request.urlopen(f'{BASE}/v1/admissions/public/syllabus', timeout=60)
    req = urllib.request.Request(f'{BASE}/v1/assignment/user/me/task?task_type=PROJECT&limit=100', headers=headers)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read())

    tasks = data.get('results', data if isinstance(data, list) else [])
    if not tasks:
        print('No hay proyectos.')
    else:
        for t in tasks:
            print(f'[{t.get("task_status","?")}] {t.get("title","?")}')

except Exception as e:
    print('Error: ' + str(e)[:100])
```

## Notas
- La API devuelve paginación: `{ count, first, next, previous, last, results }`.
- Filtra por `task_type=PROJECT`.
- `limit=100` cubre todos los proyectos.
- El token se obtiene desde el secret store via variable de entorno.