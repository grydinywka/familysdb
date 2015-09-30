from .settings import PORTAL_URL

def famalies_proc(request):
    return {'PORTAL_URL': PORTAL_URL, 'main': [1,2]}

