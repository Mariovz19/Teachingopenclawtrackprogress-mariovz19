# ⏳ Skill: que-tengo-pendiente

## Descripción
Lista las tareas pendientes (PENDING) del usuario en 4Geeks Academy, ordenadas por fecha de creación. Devuelve título y fecha, una línea por tarea.

## Cuándo usarla
Cuando quieras ver qué tienes pendiente y desde cuándo, de forma compacta.

## Output
Una línea por tarea con formato:
`YYYY-MM-DD | Título`

Ordenado de más antiguo a más reciente.

Si no hay pendientes: `No hay tareas pendientes.`

## Instrucciones
Ejecutar el siguiente script. No agregues explicaciones antes ni después.

```python
import urllib.request, json, os
from datetime import datetime

BASE = 'https://breathecode.herokuapp.com'
TOKEN = os.environ.get('FOURGEEKS_TOKEN', '')

if not TOKEN:
    print('❌ Token no disponible')
    exit(1)

headers = {'Authorization': f'Token {TOKEN}'}

try:
    urllib.request.urlopen(f'{BASE}/v1/admissions/public/syllabus', timeout=60)
    req = urllib.request.Request(f'{BASE}/v1/assignment/user/me/task?task_status=PENDING&limit=100', headers=headers)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read())

    tasks = data.get('results', [])
    if not tasks:
        print('No hay tareas pendientes.')
    else:
        tasks.sort(key=lambda t: t.get('created_at', ''))
        for t in tasks:
            fecha = t.get('created_at', '')
            if fecha:
                fecha = fecha[:10]  # YYYY-MM-DD
            print(f'{fecha} | {t.get("title","?")}')

except Exception as e:
    print('Error: ' + str(e)[:100])
```

## Notas
- Filtra por `task_status=PENDING` (proyectos + ejercicios + lecciones pendientes).
- Ordenado por `created_at` (fecha de creación/asignación).
- `limit=100` cubre todas las pendientes.
- El token se obtiene desde el secret store via variable de entorno.