

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(
        debug=app.config['DEBUG'],
        threaded=True,
        host='0.0.0.0',
        port=7771

    )


