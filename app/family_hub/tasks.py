from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from family_hub import db
from family_hub.models import Task

@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def manage_tasks():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        new_task = Task(title=title, description=description, due_date=due_date, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('manage_tasks'))
    
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks=tasks)
