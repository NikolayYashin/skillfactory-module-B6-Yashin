from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request

import album

@route("/albums/<artist>")
def albums(artist):
    albums_list = album.find(artist)
    if not albums_list:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        result = "<b>Всего альбомов исполнителя {0}: {1}</b><br> <ol>".format(artist, len(album_names))
        for number in album_names:
            result += "<li>{}</li>".format(number)
        result += "</ol>"
    return result

@route("/albums", method="POST")
def albumspost():
    year = request.forms.get("year")
    artist = request.forms.get("artist")
    genre = request.forms.get("genre")
    album1 = request.forms.get("album")

    try:
        year = int(year)
    except ValueError:
        return HTTPError(400, "Указан некорректный год альбома")

    albums_list = album.findalbum(album1)
    if not albums_list:
        new_album = album.save(year, artist, genre, album1)
    else:
        print ("Есть такой альбом в базе")
    return


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
