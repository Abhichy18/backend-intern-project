# Minimal Python Flask Backend

This is a simple backend server built with Python and Flask. It contains two JSON endpoints.

## Project Structure
- `app.py`: Contains the server code and routing logic.
- `requirements.txt`: Lists the required Python packages (`flask`).
- `.gitignore`: Excludes `.venv` and Python cache files from being tracked by Git.

---

## How to Set Up and Run

### 1. Create a Virtual Environment (venv)
A virtual environment isolates your project dependencies.

* **On Windows (PowerShell/Command Prompt):**
  ```powershell
  python -m venv .venv
  ```
* **On macOS/Linux (Terminal):**
  ```bash
  python3 -m venv .venv
  ```

### 2. Activate the Virtual Environment
Before installing packages or running the app, you must activate the environment.

* **On Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
  *(If you get a script execution policy error, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` first)*
* **On Windows (Command Prompt):**
  ```cmd
  .venv\Scripts\activate.bat
  ```
* **On macOS/Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Install Dependencies
Install Flask from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 4. Run the Server
Start the backend application:
```bash
python app.py
```
The server will start at `http://127.0.0.1:5000/`.

---

## Testing the Endpoints

### 1. Root Endpoint (`/`)
Returns a welcome message and the current server timestamp.
* **Browser:** Open `http://localhost:5000/`
* **Curl:**
  ```bash
  curl http://localhost:5000/
  ```

### 2. Info Endpoint (`/api/info`)
Returns a JSON object with mock user/developer details.
* **Browser:** Open `http://localhost:5000/api/info`
* **Curl:**
  ```bash
  curl http://localhost:5000/api/info
  ```

---

## How to Publish to GitHub (Run these in your terminal)

1. **Initialize Git repository:**
   ```bash
   git init
   ```
2. **Stage all files for commit:**
   ```bash
   git add .
   ```
3. **Commit the changes:**
   ```bash
   git commit -m "feat: initial commit of minimal flask backend"
   ```
4. **Create a new public repository on GitHub:**
   - Go to [github.com/new](https://github.com/new).
   - Enter a repository name (e.g., `minimal-flask-backend`).
   - Keep it **Public**.
   - Do **NOT** add a README, `.gitignore`, or license (since we already have them).
   - Click **Create repository**.
5. **Link your local repository to GitHub and push:**
   - Copy the commands shown on GitHub under "or push an existing repository from the command line":
   ```bash
   git branch -M main
   git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO_NAME>.git
   git push -u origin main
   ```
