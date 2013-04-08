import httplib2

from django.template.response import TemplateResponse
from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets

flow = flow_from_clientsecrets(
    '/Users/chris/Documents/calendar_demo/google_calendar/client_secrets.json',
    scope='https://www.googleapis.com/auth/calendar',
    redirect_uri='https://localhost:9000/google/oauth2callback'
)

def callback(request):
    """
    On successful authentication, the google API will hit this endpoint.
    code=4/wgx1DGRBEkPuWSpG0-ay0eAazb8Q.UiFmhxMrZ4EXuJJVnL49Cc--tF7FewI
    """
    code = request.GET['code']
    credentials = flow.step2_exchange(code)

    http = httplib2.Http()
    http = credentials.authorize(http)

    service = build('calendar', 'v3', http=http)
    events = service.events().list(calendarId='primary').execute()

    return TemplateResponse(request, "events.html", {'items': events['items']})

def connect(request):
    url = flow.step1_get_authorize_url()
    return TemplateResponse(request, "connect.html", {'url': url})