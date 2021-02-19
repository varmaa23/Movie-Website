CREATE TABLE movies(
    id integer,
    title text,
    overview text,
    budget integer,
    revenue integer,
    imdb_id text,
    rating decimal,
    runtime integer,
    poster_path text
);

CREATE TABLE languages(
    id integer,
    lang_abbrev text,
    lang_full text
);

CREATE TABLE prod_companies(
    id integer,
    company_name text
);

CREATE TABLE prod_countries(
    id integer,
    country_name text
);

CREATE TABLE release_years(
    id integer,
    release_year integer
);

CREATE TABLE movie_lang_year(
    movie_id integer,
    lang_id integer,
    year_id integer,
    spoken_lang_id integer
);

CREATE TABLE movie_prod_companies(
    movie_id integer,
    prod_comp_id integer
);

CREATE TABLE movie_prod_countries(
    movie_id integer,
    prod_country_id integer
);