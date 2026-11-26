# 🔐 Skill: el-token-sirve

## Descripción
Healthcheck del token de 4Geeks Academy. Prueba la autenticación contra BreatheCode API y devuelve una sola línea indicando si el token funciona o no, y en qué cohorte activo estás.

## Cuándo usarla
Cuando quieras verificar rápidamente que el token de 4Geeks sigue funcionando sin tener que revisar todo el perfil.

## Cómo se usa
Ejecutar el siguiente script Python. El token se obtiene desde el secret store mediante la inyección de variables de entorno (`FOURGEEKS_TOKEN`). **No agregues explicaciones antes ni después de la ejecución.**

```python
import urllib.request, json, os

BASE = 'https://breathecode.herokuapp.com'
TOKEN = os.environ.get('FOURGEEKS_TOKEN', '')

if not TOKEN:
    print('❌ Token no disponible: FOURGEEKS_TOKEN no está definido en el entorno')
    exit(1)

headers = {'Authorization': f'Token {TOKEN}'}

try:
    urllib.request.urlopen(f'{BASE}/v1/admissions/public/syllabus', timeout=60)
    req = urllib.request.Request(f'{BASE}/v1/admissions/user/me', headers=headers)
    with urllib.request.urlopen(req, timeout=60) as r:
        user = json.loads(r.read())

    cohorts = user.get('cohorts', [])
    active = [c for c in cohorts if c.get('educational_status') == 'ACTIVE']
    cohort_names = [c['cohort']['name'] for c in active] if active else ['sin cohorte activo']

    print('✅ Token funciona | cohorte(s): ' + ', '.join(cohort_names))

except Exception as e:
    print('❌ Token no funciona: ' + str(e)[:80])
```

## Output
Siempre una sola línea:
- `✅ Token funciona | cohorte(s): <nombre>` si todo ok
- `❌ Token no disponible: ...` si falta la variable de entorno
- `❌ Token no funciona: ...` si error de API o 401

## Notas
- El token se obtiene desde el secret store via inyección de variables de entorno.
- Usa wakeup previo para evitar falsos 503 por dyno dormido.
- Siempre devuelve exactamente una línea.