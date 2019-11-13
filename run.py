import sys

from app import app

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'docker':
            app.run(debug=True, host="0.0.0.0", port=5001)
        elif sys.argv[1] == 'default':
            app.run(debug=True, port=5001)
        else:
            print('Unknown command: {}'.format(sys.argv[1]))
            sys.exit()
    else:
        app.run(debug=True, port=5001)
