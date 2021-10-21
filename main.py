from flask import Flask, jsonify, request
import csv

allmovies=[]

with open("movies.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    allmovies = data[1:]

likedmovies = []
notlikedmovies = []
didntwatch = []

app=Flask(__name__)

@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": allmovies[0],
        "status": "sucess"

    })


@app.route("/liked_movie", methods=["POST"])
def liked_movie():
    global allmovies
    movie =  allmovies[0]
    allmovies = allmovies[1:]
    likedmovies.append(movie)

    return jsonify({
        "status": "success"
    }), 201


@app.route("/notlikedmovies", methods=["POST"])
def notlikedmovies():
    global allmovies
    movie = allmovies[0]
    allmovies = allmovies[1:]
    notlikedmovies.append(movie)

    return jsonify({
        "status": "sucess"
    }), 201


@app.route("/didntwatch", methods=["POST"])
def didntwatch():
    global allmovies
    movie = allmovies[0]
    allmovies = allmovies[1:]
    didntwatch.append(movie)

    return jsonify({
        "status": "sucess"
    }), 201


if __name__ == "__main__":
    app.run()
