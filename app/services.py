from cassandra.cluster import Cluster

from app.models import Account

cluster = Cluster(["127.0.0.1"])
session = cluster.connect("folx")


def get_account(acct: str):
    query = "SELECT data FROM accounts WHERE acct=%s"
    for row in session.execute(query, [acct]):
        return Account.parse_raw(row.data)


def get_account_password(acct: str):
    query = "SELECT password FROM accounts WHERE acct=%s"
    for row in session.execute(query, [acct]):
        return row.password


def update_account_password(acct: str, password: str):
    query = "UPDATE accounts SET password=%s WHERE acct=%s"
    session.execute(query, [password, acct])


def insert_account(account: Account):
    query = "INSERT INTO accounts (acct, data) VALUES (%s, %s)"
    session.execute(query, [account.acct, account.json()])


def update_account(account: Account):
    query = "UPDATE accounts SET data=%s WHERE acct=%s"
    session.execute(query, [account.json(), account.acct])


def delete_account(acct: str):
    query = "DELETE FROM accounts WHERE acct=%s"
    session.execute(query, [acct])


def get_accounts():
    query = "SELECT data FROM accounts"
    for row in session.execute(query):
        yield Account.parse_raw(row.data)
