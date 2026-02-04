from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>WELCOME Dagvadorj!</h1>
        <p>Thank you.</p>
        <ul>
            <li><a href="/poll/">Poll App руу орох</a></li>
            <li><a href="/blog/">Blog App руу орох</a></li>
        </ul>
    """)