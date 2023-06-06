from appsecond import Message, app, db

with app.app_context():
    all_messages = Message.query.all()
    print(all_messages)

    message_1 = db.session.get(Message, 1)
    print(message_1)
