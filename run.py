#!/usr/bin/env pypy3

from app import app 

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8088, debug=True)