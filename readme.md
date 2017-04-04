In order for this to work, your directory setup must look like this:

    pokemoncss/
    pokemonflair/
    rpokemon.github.io/

> `pokemoncss` is the [https://github.com/kwwxis/r-pokemon](https://github.com/kwwxis/r-pokemon) repo

> `rpokemon.github.io/` is the [https://github.com/rpokemon/rpokemon.github.io](https://github.com/rpokemon/rpokemon.github.io) repo

> `pokemonflair` is this repo

You can change the names of these folders but make sure to update `pokemonflair/flairgen.py` accordingly.

---

Within pokemonflair/ there is `flairgen.py` and `flairnames.py`. flairgen.py is the file that generates the flair.js based on flairnames.py which serves as the flair config file.

`flairgen.py` overwrites the following files:

  - `pokemonflair/flair.css`
  - `pokemoncss/src/flair.css`
  - `rpokemon.github.io/flair.css`
  - `pokemonflair/flair.js`
  - `rpokemon.github.io/flair.js`

To add new flairs:

  - update flairnames.py accordingly
  - run flairgen.py
  - cd to rpokemon.github.io/, commit and push
  - open GCP > console
     - cd to `pokemonflairbot/`
     - run `git pull; appcfg.py -A pokemonflairbot -V 8 update .`