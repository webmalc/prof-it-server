from profit.lib.messengers import mailer


def test_mail_managers(admin_client, mailoutbox):
    mailer.mail_managers(subject='Text message', data={'text': 'Test text'})
    assert len(mailoutbox) == 1
    mail = mailoutbox[0]
    assert mail.recipients() == ['admin@example.com', 'manager@example.com']
    assert 'Text message' in mail.subject
    assert 'Test text' in mail.alternatives[0][0]
