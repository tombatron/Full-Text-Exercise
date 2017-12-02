from flask import Flask, render_template, request, jsonify
from search import SearchIndex

app = Flask(__name__)

search_instance = SearchIndex()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def perform_search():
    search_phrase = request.get_json().get('searchPhrase')

    return jsonify(list(search_instance.search(search_phrase)))

if __name__ == '__main__':
    app.run(debug=True)
