from src.databases.sqlite.infra.repository.Music_Gallery_repository import MusicGalleryRepository

musics = {
    'music_name': 'Billionaire',
    'music_publish_year': 1999
}

gallery = MusicGalleryRepository()
# gallery.insertTitle(musics)
data = gallery.selectWithSameYear(1999)
# data = gallery.selectTitle('Hall Of Fame')
# data = gallery.getPlaylist()

print(data)