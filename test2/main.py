def sendMail(request):
    import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail
    from flask import abort

    if request.method != "POST": abort(405)


    jReq = request.get_json(silent=True)
    params = ("sender", "reciever", "subject", "message")

    if jReq and all(k in jReq for k in params):
        sender = jReq["sender"]
        reciever = jReq["reciever"]
        subj = jReq["subject"]
        msg = jReq["message"]
    else: abort(400)


    message = Mail(
        from_email=sender,
        to_emails=reciever,
        subject=subj,
        html_content=msg)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg.send(message)
        return "OK", 200
    except Exception as e:
        return e, 400