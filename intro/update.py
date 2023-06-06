from appsecond import Message, app, db

with app.app_context():
    antanas = db.session.get(Message, 2)
    antanas.email = "geras.zmogus@gmail.com"
    db.session.add(antanas)
    db.session.commit()
    print(Message.query.all())
