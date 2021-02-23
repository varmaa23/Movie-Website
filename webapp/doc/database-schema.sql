CREATE TABLE movies(
    id integer,
    title text,
    overview text,
    budget integer, .
    revenue integer,
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

CREATE TABLE prodcompanies(
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

CREATE TABLE movie_lang(
    movie_id integer,
    lang_id integer,
    spoken_lang_id integer
);

CREATE TABLE movie_prodcompanies(
    movie_id integer,
    prod_comp_id integer
);

CREATE TABLE movie_countries(
    movie_id integer,
    country_id integer
);

CREATE TABLE movie_genres(
    movie_id integer,
    genre_id integer
);