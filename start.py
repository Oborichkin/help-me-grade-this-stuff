import os

from help_me import app


if __name__ == '__main__':
    port = int(os.environ.get('PORT')) 
    app.run(host='0.0.0.0', port=port, debug=False)
