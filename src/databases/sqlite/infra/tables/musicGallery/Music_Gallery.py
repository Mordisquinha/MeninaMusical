from sqlalchemy import Column, String, Integer
from src.databases.sqlite.infra.configs.base import Base

class MusicGallery(Base):
    __tablename__ = 'MusicGallery'
    music_id = Column(Integer, primary_key=True)
    music_name = Column(String, nullable=False)
    music_to_search = Column(String, nullable=False)
    music_publish_year = Column(Integer, nullable=False)

    def __repr__(self):
        output = {
            'music_id': self.music_id, 
            'music_name': self.music_name, 
            'music_to_search': self.music_to_search,
            'music_publish_year': self.music_publish_year
        }
        
        return str(output)
