import csv

from flask import Flask, render_template
from filesystem import Folder, File
from action import *

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    FILES_ROOT=os.path.dirname(os.path.abspath("/Users/andrejpistek/Documents/Dokumenty/Work/Data/Iris_plan_flight/")),
)


@app.route('/')
@app.route('/files/<path:path>')
def index(path=''):
    path_join = os.path.join(app.config['FILES_ROOT'], path)
    if os.path.isdir(path_join):
        folder = Folder(app.config['FILES_ROOT'], path)
        folder.read()
        return render_template('folder.html', folder=folder)
    else:
        my_file = File(app.config['FILES_ROOT'], path)
        context = my_file.apply_action(View)
        folder = Folder(app.config['FILES_ROOT'], my_file.get_path())
        if context is None:
            return render_template('file_unreadable.html', folder=folder)
        return render_template('file_view.html', text=context['text'], file=my_file, folder=folder)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
