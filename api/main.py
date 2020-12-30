from src import Search

from flask import Flask

app = Flask(__name__)

@app.route('/<int:number>')
def root(number):
  return Search(
    url="https://hml-api.elo.com.br/graphql",
  ).run(number)