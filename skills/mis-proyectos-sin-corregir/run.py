import urllib.request, json, os
BASE = "https://breathecode.herokuapp.com"
TOKEN = os.environ.get("FOURGEEKS_TOKEN", "")
if not TOKEN:
    print("Token no disponible")
    exit(1)
headers = {"Authorization": f"Token {TOKEN}"}
urllib.request.urlopen(f"{BASE}/v1/admissions/public/syllabus", timeout=60)
req = urllib.request.Request(f"{BASE}/v1/assignment/user/me/task?task_status=DONE&limit=100", headers=headers)
with urllib.request.urlopen(req, timeout=60) as r:
    data = json.loads(r.read())
tasks = data.get("results", [])
sin_corregir = [t for t in tasks if t.get("revision_status") != "APPROVED"]
if not sin_corregir:
    print("Sin proyectos entregados pendientes de correccion.")
else:
    for t in sin_corregir:
        fecha = str(t.get("delivered_at") or t.get("created_at") or "?")[:10]
        title = t.get("title", "?")
        print(f"{title} --- {fecha}")