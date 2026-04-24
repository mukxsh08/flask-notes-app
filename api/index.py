from website import create_app

app = create_app()

# Vercel handler
def handler(request):
    return app(request.environ, lambda status, headers: None)