FROM postgres:latest

ENV POSTGRES_DB neurohack
ENV POSTGRES_USER user
ENV POSTGRES_PASSWORD password
ENV PGDATA /var/lib/postgresql/data/pgdata

COPY init.sql /docker-entrypoint-initdb.d/


EXPOSE 5432

