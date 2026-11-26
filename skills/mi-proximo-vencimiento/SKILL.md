# ⏰ Skill: mi-proximo-vencimiento

## Descripción
Busca todos los proyectos pendientes, identifica el más reciente (próximo a vencer) y devuelve una sola línea con título y fecha.

## Output
```
<TÍTULO> --- <YYYY-MM-DD>
```
Si no hay proyectos pendientes: `Sin proyectos pendientes.`

## Instrucciones
Ejecutar:
```bash
python3 skills/mi-proximo-vencimiento/run.py
```
No agregues explicaciones antes ni después.

## Script (`run.py`)
```python
import urllib.request, json, os
BASE = "https://breathecode.herokuapp.com"
TOKEN = os.environ.get("FOURGEEKS_TOKEN", "")
if not TOKEN:
    print("Token no disponible")
    exit(1)
headers = {"Authorization": f"Token {TOKEN}"}
urllib.request.urlopen(f"{BASE}/v1/admissions/public/syllabus", timeout=60)
req = urllib.request.Request(f"{BASE}/v1/assignment/user/me/task?task_status=PENDING&task_type=PROJECT&limit=100", headers=headers)
with urllib.request.urlopen(req, timeout=60) as r:
    data = json.loads(r.read())
tasks = data.get("results", [])
if not tasks:
    print("Sin proyectos pendientes.")
else:
    tasks.sort(key=lambda t: t.get("created_at", ""), reverse=True)
    t = tasks[0]
    fecha = (t.get("created_at") or "?")[:10]
    title = t.get("title", "?")
    print(f"{title} --- {fecha}")
```

## Notas
- Ordena por `created_at` descendente (más reciente = próximo a vencer).
- Solo proyectos (task_type=PROJECT) pendientes (task_status=PENDING).