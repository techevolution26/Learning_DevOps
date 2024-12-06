@app.route('/connections', methods=['GET', 'POST'])
@login_required
def manage_connections():
    if request.method == 'POST':
        name = request.form['name']
        relationship = request.form['relationship']
        new_connection = FamilyConnection(name=name, relationship=relationship, user_id=current_user.id)
        db.session.add(new_connection)
        db.session.commit()
        return redirect(url_for('manage_connections'))
    
    connections = FamilyConnection.query.filter_by(user_id=current_user.id).all()
    return render_template('connections.html', connections=connections)
