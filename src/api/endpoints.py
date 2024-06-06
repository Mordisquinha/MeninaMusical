from src.api import app
from flask import request
from src.utils import ERROR
from src.databases.sqlite.infra.repository.Music_Gallery_repository import MusicGalleryRepository


@app.route('/select/<title>', methods=['GET'])
def select(title):
    """
    Get a Title in gallery by name.
    ---
    parameters:
      - name: title
        in: path
        type: string
        required: true

    responses:
      200:
        description: A successful response
      500:
        description: A failed response
    """
    try:
      if request.method == 'GET':
          if title is not None:
              formatted_title = str(title.lower().replace(' ', ''))
              gallery = MusicGalleryRepository()
              output = gallery.selectTitle(music_name=formatted_title)

              return output
          
          return {'error': 'Title cant be empty'}, 500
          
    except Exception as exception:
        return {str(exception.__reduce__()[0].__name__): exception.__reduce__()[1]}, 500
    
@app.route('/select-year/<year>', methods=['GET'])
def selectYear(year):
    """
    Get all Titles in gallery with same year of publish.
    ---
    parameters:
      - name: year
        in: path
        type: string
        required: true

    responses:
      200:
        description: A successful response
      500:
        description: A failed response
    """
    try:
      if request.method == 'GET':
          if year is not None:
              gallery = MusicGalleryRepository()
              output = gallery.selectWithSameYear(music_publish_year=year)

              return output
          
          return {'error': 'year cant be empty'}, 500
          
    except Exception as exception:
        return {str(exception.__reduce__()[0].__name__): exception.__reduce__()[1]}, 500
  
@app.route('/insert', methods=['POST'])
def insert():
    """
    Insert a Title in gallery.
    ---
    parameters:
      - name: data
        in: body
        type: object
        required: true
        properties:
          music_name:
            type: string
            description: The title of the music
            default: "Hall of Fame"

          music_publish_year:
            type: integer
            description: Year of the music publish
            default: 2012

    responses:
      200:
        description: A successful response
      500:
        description: A failed response
    """
    try:
      if request.method == 'POST':
          data = request.get_json()
          print(data)
          gallery = MusicGalleryRepository()
          output = gallery.insertTitle(data=data)

          if isinstance(output, ERROR):
              return output.getERROR(), 500
          
          return output
          
    except Exception as exception:
        return {str(exception.__reduce__()[0].__name__): exception.__reduce__()[1]}, 500
    
@app.route('/make-playlist', methods=['GET'])
@app.route('/make-playlist/<qty>', methods=['GET'])
def playlist(qty=None):
    """
    Make a random playlist with musics in gallery, can choise a quantity of musics by paramether qty.
    ---
    parameters:
      - name: qty
        in: path
        type: integer
        required: false
        default: 0

    responses:
      200:
        description: A successful response
      500:
        description: A failed response
    """
    try:
      if request.method == 'GET':
        gallery = MusicGalleryRepository()
        output = gallery.getPlaylist(qty=qty)

        return output

          
    except Exception as exception:
        print(exception)
        return {str(exception.__reduce__()[0].__name__): exception.__reduce__()[1]}, 500