from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

# -----------------------------
# Función para conectar a la BD
# -----------------------------
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# -----------------------------
# Crear tabla si no existe
# -----------------------------
def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS task (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# -----------------------------
# Listar tareas
# -----------------------------
@app.route("/")
def list_tasks():
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM task").fetchall()
    conn.close()
    return render_template("list.html", tasks=tasks)

# -----------------------------
# Crear tarea
# -----------------------------
@app.route("/create", methods=["GET", "POST"])
def create_task():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        status = "Pendiente"
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO task (title, description, status, created_at) VALUES (?, ?, ?, ?)",
            (title, description, status, created_at)
        )
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("create.html")

#-----------------------------
# Eliminar tarea
#-----------------------------
@app.route("/task/<int:id>/delete", methods=["POST"])
def delete_task(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM task WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

#-----------------------------
#Borrar todas las tareas
#----------------------------- 
@app.route("/delete_all", methods=["POST"])
def delete_all():
    conn = get_db_connection()
    conn.execute("DELETE FROM task")
    conn.commit()
    conn.close()
    return redirect("/")




# -----------------------------
# Detalle de tarea
# -----------------------------
@app.route("/task/<int:id>")
def task_detail(id):
    conn = get_db_connection()
    task = conn.execute("SELECT * FROM task WHERE id = ?", (id,)).fetchone()
    conn.close()
    return render_template("detail.html", task=task)

# -----------------------------
# Cambiar estado
# -----------------------------
@app.route("/task/<int:id>/update", methods=["POST"])
def update_status(id):
    new_status = request.form["status"]

    conn = get_db_connection()
    conn.execute("UPDATE task SET status = ? WHERE id = ?", (new_status, id))
    conn.commit()
    conn.close()

    return redirect(f"/task/{id}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

