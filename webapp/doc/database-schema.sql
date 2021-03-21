CREATE TABLE movies(
    id integer,
    title text,
    overview text,
    budget decimal,
    revenue decimal,
    imdb_id text,
    rating decimal,
    runtime integer,
    release_year integer,
    poster_path text
);

CREATE TABLE languages(
    id integer,
    lang_abbrev text,
    lang_full text
);

CREATE TABLE companies(
    id integer,
    company_name text
);

CREATE TABLE countries(
    id integer,
    country_name text
);

CREATE TABLE genres(
    id integer,
    genre text
);

CREATE TABLE movie_langs(
    movie_id integer,
    lang_id integer
);

CREATE TABLE movie_companies(
    movie_id integer,
    company_id integer
);

CREATE TABLE movie_countries(
    movie_id integer,
    country_id integer
);

CREATE TABLE movie_genres(
    movie_id integer,
    genre_id integer
);