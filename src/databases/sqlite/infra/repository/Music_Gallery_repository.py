import json
import sqlite3
from random import shuffle
from src.utils import ERROR
from  src.databases.sqlite.infra.tables.musicGallery.columns import schema
from src.databases.sqlite.infra.configs.connection import DBConnectionHandler
from src.databases.sqlite.infra.tables.musicGallery.Music_Gallery import MusicGallery

class MusicGalleryRepository:
    def __init__(self) -> None:
        
        create_table = """
            CREATE TABLE IF NOT EXISTS MusicGallery (
                music_id INTEGER PRIMARY KEY AUTOINCREMENT,
                music_name TEXT NOT NULL,
                music_to_search TEXT NOT NULL,
                music_publish_year INTEGER NOT NULL
            )
        """

        with sqlite3.connect('MeninaMusical.db') as conn:
            cursor = conn.cursor()
            cursor.execute(create_table)

            conn.commit()

    def __valideInsert(self, data:dict) -> bool:
        return schema.validate(data)
    
    def __putAllTitlesInList(self) -> list:
        with DBConnectionHandler() as db:
            data = db.session.query(MusicGallery).all()
            output = [title.music_name for title in data]
            
            return output

    def selectTitle(self, music_name):
        with DBConnectionHandler() as db:
            music_name_formated = music_name.lower().replace(' ', '')
            data = db.session.query(MusicGallery).filter(MusicGallery.music_to_search == music_name_formated).all()
            
            output = {}
            output_json = []
            for music in data:
                output['music_id'] = music.__dict__['music_id']
                output['music_name'] = music.__dict__['music_name']
                output['music_publish_year'] = music.__dict__['music_publish_year']
                output_json.append(output)
                output = {}
            
            return output_json
        
    def selectWithSameYear(self, music_publish_year):
        with DBConnectionHandler() as db:
            data = db.session.query(MusicGallery).filter(MusicGallery.music_publish_year == music_publish_year).all()

            output = {}
            output_json = []
            for music in data:
                output['music_id'] = music.__dict__['music_id']
                output['music_name'] = music.__dict__['music_name']
                output['music_publish_year'] = music.__dict__['music_publish_year']
                output_json.append(output)
                output = {}
            
            return output_json
        
    def insertTitle(self, data:dict) -> any:
        with DBConnectionHandler() as db:
            try:
                if not self.__valideInsert(data):
                    return ERROR(error_type='wrong schema type', message=f'the schema type is: {schema.schema}')
                
                if self.selectTitle(data['music_name']):
                    return ERROR(error_type='ALREADY EXISTS', message='this music already exists !')
                
                data_insert = MusicGallery(music_name=data['music_name'], music_to_search=data['music_name'].lower().replace(' ', ''), music_publish_year=data['music_publish_year'])
                db.session.add(data_insert)
                db.session.commit()

                output = self.selectTitle(data['music_name'])

                print(output)

                return output

            except Exception as exception:
                db.session.rollback()

                return ERROR(error_type='UNKNOW ERROR', message=exception)

    def getPlaylist(self, qty:int=0) -> list:
        musics = self.__putAllTitlesInList()
        if not qty:
            qty = 0
        
        qty = int(qty)
        
        shuffle(musics)
        
        if qty == 0:
            return musics
        
        return musics[:qty]