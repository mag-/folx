DROP KEYSPACE folx;

CREATE KEYSPACE folx
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};

USE folx;
CREATE TABLE accounts (
    acct text PRIMARY KEY,
    password text,
    data TEXT,
);

CREATE TABLE status (
    uid uuid PRIMARY KEY,
    status_id bigint,
    acct text,
    data text
);
CREATE INDEX status_by_status_id ON status (status_id);


CREATE TABLE followers (
    acct text,
    follower text,
    since timestamp,
    PRIMARY KEY (acct, follower)
)


CREATE TABLE userline (
    acct text,
    time timeuuid,
    status_uid uuid,
    PRIMARY KEY (acct, time)
) WITH CLUSTERING ORDER BY (time DESC);

CREATE TABLE timeline (
    acct text,
    time timeuuid,
    status_uid uuid,
    PRIMARY KEY (acct, time)
) WITH CLUSTERING ORDER BY (time DESC);

create table oauth_clients (
    uid uuid PRIMARY KEY,
    client_secret text,
    client_id text,
    acct text,
    scope text,
    code text
);
CREATE INDEX oauth_clients_by_code ON oauth_clients (code);

