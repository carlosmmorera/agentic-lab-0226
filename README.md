# Copiloto Autónomo de Operaciones y Finanzas

Repositorio con el material didactico para construir un sistema multiagente con arquitectura **Planner / Executor**, acceso a datos mediante **MCP (Model Context Protocol)**, conocimiento procedimental bajo demanda con **Agent Skills (`SKILL.md`)** y aprobación humana (**Human-in-the-Loop**).

---

## Requisitos previos

Antes de empezar, asegúrate de tener instalado en tu ordenador:
1. **Git** (o descargar el repositorio en ZIP desde el botón verde `<> Code` -> `Download ZIP`).
2. **uv** (gestor ultrarrápido de entornos y paquetes de Python).

### ¿Cómo instalar `uv` si aún no lo tienes?

* **En macOS o Linux** (abre la Terminal y ejecuta):
    ```bash
    curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
    ```

* **En Windows** (abre PowerShell y ejecuta):
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"
    ```


*(Tras instalarlo, cierra y vuelve a abrir la terminal para que reconozca el comando `uv`).*

---

## Guía paso a paso para configurar el entorno

### 1. Descargar el repositorio

Abre una terminal, sitúate en la carpeta donde quieras guardar el proyecto y ejecuta:

```bash
git clone https://github.com/carlosmmorera/agentic-lab-0226.git
cd agentic-lab-0226
```

### 2. Instalar Python y todas las dependencias con `uv`

Ejecuta el siguiente comando dentro de la carpeta del proyecto. `uv` descargará automáticamente la versión correcta de Python (si no la tienes) y creará un entorno virtual aislado (`.venv`) con todas las librerías exactas del taller:

```bash
uv sync
```

### 3. Configurar tu clave de API de OpenAI

1. Crea una copia del archivo `.env.example` y llámala `.env`:
* **En macOS / Linux:**
```bash
cp .env.example .env
```


* **En Windows (PowerShell):**
```powershell
copy .env.example .env
```




2. Abre el archivo `.env` con cualquier editor de texto (o desde VS Code) y sustituye `pon_aqui_tu_clave_de_openai` por tu clave real (`sk-...`). Guarda el archivo.

---

## Cómo abrir y ejecutar el Notebook

Puedes elegir cualquiera de estas dos opciones:

### Opción A: Usar VS Code (Recomendada)

1. Abre la carpeta del proyecto en VS Code (`code .`).
2. Abre el archivo **`sesion_07_workshop.ipynb`**.
3. Haz clic en **Seleccionar Kernel** (arriba a la derecha del notebook) $\rightarrow$ **Python Environments** $\rightarrow$ selecciona el entorno que empieza por **`.venv`**.
4. Ejecuta las celdas secuencialmente (`Shift + Enter`).

### Opción B: Usar JupyterLab en el navegador

Ejecuta este comando desde la terminal dentro de la carpeta del proyecto:

```bash
uv run jupyter lab
```

Se abrirá una pestaña en tu navegador. Haz doble clic sobre **`sesion_07_workshop.ipynb`** en el panel izquierdo y comienza a trabajar.

---

## Solución de problemas frecuentes

* **Error `AuthenticationError` o `OPENAI_API_KEY not found`:** Asegúrate de haber renombrado correctamente `.env.example` a `.env` (sin extensión `.txt` oculta) y de haber ejecutado la **Celda 1** del notebook donde se llama a `load_dotenv()`.
* **No me aparece el entorno `.venv` en VS Code:** Abre la paleta de comandos (`Ctrl + Shift + P` en Windows o `Cmd + Shift + P` en Mac), escribe `Developer: Reload Window` y pulsa Enter.
* **Error `RuntimeError: asyncio.run() cannot be called from a running event loop`:** En Jupyter no uses `asyncio.run(...)`; ejecuta directamente `await run_operations_copilot(...)` en la celda.
