from cerberus import Validator

schema = Validator(
    {
        'music_id': {'type': 'integer'},
        'music_name': {'type': 'string'},
        'music_publish_year': {'type': 'integer'}
    }
)