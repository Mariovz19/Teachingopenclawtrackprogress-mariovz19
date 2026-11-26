# 📊 Skill: mi-avance

## Descripción
Devuelve dos números independientes: tareas pendientes y tareas entregadas (completadas por el estudiante, corregidas o no).

## Output
Siempre el mismo formato, dos líneas:
```
Pendientes: <N>
Entregadas: <N>
```

## Instrucciones
Ejecutar el siguiente script. No agregues explicaciones antes ni después.

```python
import urllib.request, json, os
from collections import Counter

BASE = 'https://breathecode.herokuapp.com'
TOKEN = os.environ.get('FOURGEEKS_TOKEN', '')

if not TOKEN:
    print('Token no disponible')
    exit(1)

headers = {'Authorization': f'Token {TOKEN}'}

try:
    urllib.request.urlopen(f'{BASE}/v1/admissions/public/syllabus', timeout=60)
    req = urllib.request.Request(f'{BASE}/v1/assignment/user/me/task?limit=300', headers=headers)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read())
    tasks = data.get('results', [])

    c = Counter(t.get('task_status', '?') for t in tasks)
    pend = c.get('PENDING', 0)
    entr = c.get('DONE', 0)
    print(f'Pendientes: {pend}')
    print(f'Entregadas: {entr}')

except Exception as e:
    print('Error: ' + str(e)[:100])
```

## Notas
- **Pendientes**: tareas sin entregar (task_status = PENDING).
- **Entregadas**: tareas ya completadas por el estudiante (task_status = DONE), independientemente de si han sido corregidas, aprobadas o rechazadas.
- `limit=300` cubre todo el historial.
- El token se obtiene desde el secret store via variable de entorno.