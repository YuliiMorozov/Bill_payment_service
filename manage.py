from indication import create_app
from indication.middleware.middleware import Middleware

app = create_app()
app.wsgi_app = Middleware(app.wsgi_app)
if __name__ == '__main__':
    app.run(debug=True)