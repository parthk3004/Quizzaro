from gmail_api_wrapper.crud.write import GmailAPIWriteWrapper

api = GmailAPIWriteWrapper()


gmail_api = GmailAPIReadWrapper()

api.compose_mail(subject='API Wrapper', body='Py client', to='email1,email2')

{
'id': 'abc@gmail.com',
'labelsIds': ['INBOX', 'SENT', 'UNREAD'],
'threadId': 'abc@gmail.com'
}
