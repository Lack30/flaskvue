# -*- coding:utf-8 -*-

from app import app

if __name__ == "__main__":
    # app.run(debug=True, ssl_context=("ca/server-cert.pem","ca/server-key.pem"))
    app.run(debug=True)