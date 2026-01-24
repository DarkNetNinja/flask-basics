"""
Part 6: Homework - Personal To-Do List App
==========================================
See Instruction.md for full requirements.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

# Sample data - your tasks list
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low'},
]

@app.route('/')
def index():
    return render_template('index.html',tasks = TASKS)

@app.route('/task/<int:id>')
def view_task(id):
    task = next((t for t in TASKS if t['id'] == id),None)
    if task:
        return render_template('task.html',task = task)
    return "Task not found",404

@app.route('/add',methods =['GET','POST'])
def add_task():
    if request.method == "POST":
        title = request.form.get('title')
        priority = request.form.get('priority')
        status = request.form.get('status')
        desc = request.form.get('desc')

        new_id=TASKS[-1]['id']+1 if TASKS else 1

        new_task = {
            'id':new_id,
            'title':title,
            'status':status,
            'priority':priority,
            'desc':desc
        }

        TASKS.append(new_task)

        return redirect(url_for('index'))
    
    return render_template('add.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/priority/<level>')
def filter_priority(level):
    filtered_tasks = [t for t in TASKS if t['priority'].lower() == level.lower()]
    return render_template('index.html',tasks = filtered_tasks)





if __name__ == '__main__':
    app.run(debug=True)
