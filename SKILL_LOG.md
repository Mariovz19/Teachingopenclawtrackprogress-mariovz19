# 📜 SKILL_LOG.md — Skills de integración con 4Geeks Academy

## Skill 1 — el-token-sirve

**Prompt inicial:**
> crea una nueva skill con nombre el-token-sirve sin filtro devuelve una linea que indica si funciona o no funciona el token y en que cohorte estas

**Descripción:**
Healthcheck del token de 4Geeks Academy. Prueba la autenticación contra BreatheCode API y devuelve una sola línea indicando si el token funciona y en qué cohorte activo estás. Usa wakeup previo para evitar falsos 503 por dyno dormido.

**Resultado de prueba:**
```
✅ Token funciona | cohorte(s): cohorte de estudiante, Implementing Data Pipelines, Asynchronous processing and offloading, ...
```

---

## Skill 2 — mis-proyectos

**Prompt inicial:**
> crea una nueva skill con nombre mis-proyectos Un filtro. todos los proyectos entregados y sin entregar. devuelve una linea por proyecto, con el titulo y el estado.

**Descripción:**
Lista todos los proyectos (task_type=PROJECT) del usuario, tanto entregados como sin entregar. Una línea por proyecto con el título y el estado (PENDING, DONE, APPROVED, REJECTED). La API devuelve paginación en `{ count, first, next, previous, last, results }`.

**Resultado de prueba:**
```
[DONE] My first collaborative professionalt from an existing project - Financial dashboard
[PENDING] Build a Digital Postcard with HTML/CSS
[PENDING] Code an Excuse Generator in JavaScript with Prompts
[PENDING] Milestone 0 — Choose Your Company
...
[PENDING] AgentHub Admin Panel Specs and Prompt-Driven Prototype
```
Total: 24 proyectos (11 PENDING, 13 DONE/APPROVED).

---

## Skill 3 — que-tengo-pendiente

**Prompt inicial:**
> crea una nueva skill con nombre que-tengo-pendiente dos filtros menos filas que la anterior devuelveme el titulo y fecha de entrega, ordenado por fechas. menos campos tambien el estado ya lo sabemos, lo pedimos en el filtro.

**Descripción:**
Lista todas las tareas pendientes (task_status=PENDING) ordenadas por fecha de creación ascendente (más antiguas primero). Devuelve solo título y fecha, sin estado (se sobreentiende que son pendientes). Incluye todos los task_type (LESSON, EXERCISE, PROJECT, QUIZ).

**Resultado de prueba:**
```
2026-08-19 | Standard Workflow Diagrams for Beginners
2026-08-24 | What is The Internet?
2026-08-24 | Understanding How the Internet Works
...
2026-11-24 | AgentHub Admin Panel Specs and Prompt-Driven Prototype
```
Total: 101 tareas pendientes.

---

## Skill 4 — mi-avance

**Prompt inicial:**
> crea una nueva skill con nombre mi-avance no devuelve lista devuelve numeros. Dos campos independientes. Una entregada puede estar sin corregir

**Descripción:**
Devuelve dos números independientes: tareas pendientes (PENDING) y tareas entregadas (DONE). Entregadas incluye las que están sin corregir (revision_status PENDING) y las ya aprobadas. Son campos independientes, no una relación matemática.

**Resultado de prueba:**
```
Pendientes: 101
Entregadas: 34
```

---

## Skill 5 — mi-proximo-vencimiento

**Prompt inicial:**
> crear una nueva skill con nombre mi-proximo-vencimiento Sin filtro. Busca todos los proyectos pendientes. Identifica la fecha de entrega más próxima. Devuelve una sola línea con el título y la fecha

**Descripción:**
Busca todos los proyectos pendientes (task_status=PENDING, task_type=PROJECT), los ordena por fecha de creación descendente, y devuelve el más reciente (próximo a vencer). Una sola línea con título y fecha.

**Resultado de prueba:**
```
AgentHub Admin Panel Specs and Prompt-Driven Prototype --- 2026-11-24
```

---

## Skill 6 — mis-proyectos-sin-corregir

**Prompt inicial:**
> crear una nueva skill con nombre mis-proyectos-sin-corregir Sin filtro Busca proyectos entregados Excluye los que ya tienen corrección Devuelve título y fecha de entrega

**Descripción:**
Filtra proyectos entregados (task_status=DONE) que aún no tienen revisión aprobada (revision_status distinto de APPROVED). Devuelve título y fecha de entrega (delivered_at), una línea por proyecto.

**Resultado de prueba:**
```
Introduction To No Code And Automatization --- 2026-08-19
My Agent, My Way: Teaching Your Personal Assistant New Skills --- 2026-11-23
Cinema Seat Manager in TypeScript --- 2026-11-16
```