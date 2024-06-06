# MeninaMusical

> An API skeleton to save & get musics in a database and make playlists.

![Licença](https://img.shields.io/badge/license-MIT-blue.svg)
![Versão](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [License](#license)
- [Authors](#authors)
- [Security](#security)
- [Acknowledgements](#acknowledgements)

## About

This API provides functionalities for interacting with a music gallery, allowing users to select, insert, and create playlists of music titles. The following endpoints are available:

## Features

- Get a Title by Name
    - Endpoint: /select/<title>
        - Method: GET
        - Description: Retrieves a music title from the gallery by its name.
        - Parameters:
            - title (string, required): The name of the music title to be retrieved.

    - Responses:
        - 200: A successful response with the music title information.
        - 500: An error occurred during the process.

- Get Titles by Year of Publish
    - Endpoint: /select-year/<year>
        - Method: GET
        - Description: Retrieves all music titles from the gallery that were published in the same year.
        - Parameters:
            - year (string, required): The year of publication to filter the music titles.

    - Responses:
        - 200: A successful response with the list of music titles published in the given year.
        - 500: An error occurred during the process.

- Insert a Music Title
    - Endpoint: /insert
        - Method: POST
        - Description: Inserts a new music title into the gallery.
        - Parameters:
            - data (object, required): The details of the music title to be inserted, including:
                - music_name (string): The title of the music.
                - music_publish_year (integer): The year the music was published.
    - Responses:
        - 200: A successful response confirming the insertion.
        - 500: An error occurred during the process.

- Create a Random Playlist
    - Endpoint: /make-playlist or /make-playlist/<qty>
        - Method: GET
        - Description: Generates a random playlist from the music gallery. Optionally, a specific quantity of music titles can be specified.
        - Parameters:
            - qty (integer, optional): The number of music titles to include in the playlist. If not specified, a default quantity will be used.
    - Responses:
        - 200: A successful response with the generated playlist.
        - 500: An error occurred during the process.

## Installation

Instructions for setting up the development environment.

```bash
# Clone this repository
$ git clone https://github.com/Mordisquinha/MeninaMusical.git

# Navigate to the project directory
$ cd MeninaMusical

# Install dependencies
$ pip install -r requirements.txt

# Or if you prefer:

    # Install pipenv
    $ pip install pipenv

    # check installation
    $ pipenv --version

    #run 
    $ pipenv shell

# Run the project
$ python3 run.py
```

## Usage

All Necessary help is more available in localhost:8080 theres a Swagger with the endpoints available and examples

## Technologies

- Python
- Flask
- Swagger
- Sql Lite

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors
- Mordisquinha <https://github.com/Mordisquinha>

## Security

To report security issues, see our [Security Policy](SECURITY.md) for information on how to do so securely and responsibly.

## Acknowledgements
- My Mentor <https://github.com/programadorLhama>