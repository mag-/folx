from datetime import datetime
import time
import uuid
from cassandra.cluster import Cluster
from pytz import timezone
import pytz

from app.models import Account, Status

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


def insert_account(account: Account, password: str):
    query = "INSERT INTO accounts (acct, data, password) VALUES (%s, %s, %s)"
    session.execute(query, [account.acct, account.json(), password])


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


def save_oauth_client_data(client_id: str, client_secret: str, scope: str, acct: str, code: str):
    query = "INSERT INTO oauth_clients (uid, client_id, client_secret, scope, acct, code) VALUES (uuid(), %s, %s, %s, %s, %s)"
    session.execute(query, [client_id, client_secret, scope, acct, code])


def check_client_id_code(client_id: str, code: str):
    query = "SELECT client_id, acct FROM oauth_clients WHERE code=%s"
    for row in session.execute(query, [code]):
        if row.client_id == client_id:
            return row.acct
    return None


def add_status(acct: str, status: Status) -> Status:
    query = "INSERT INTO status (uid, status_id, acct, data) VALUES (%s, %s, %s, %s)"
    uid = uuid.uuid4()
    status_uid = uuid.uuid1().int >> 65
    status.id = status_uid
    status.uri = f"@{acct}/statuses/{status_uid}"
    status.created_at = datetime.utcnow().replace(tzinfo=pytz.utc)
    session.execute(query, [uid, status_uid, acct, status.json()])

    # update user timeline
    query = "INSERT INTO userline (acct, time, status_uid) VALUES (%s, now(), %s)"
    session.execute(query, [acct, uid])

    # update follower timelines
    query = "SELECT follower FROM followers WHERE acct=%s"
    for row in session.execute(query, [acct]):
        query = "INSERT INTO timeline (acct, time, status_uid) VALUES (%s, now(), %s)"
        session.execute(query, [row.follower, uid])
    return status


def get_statuses(ids):
    out = []
    query = "SELECT data FROM status WHERE uid in %s"
    for row in session.execute(query, [ids]):
        out.append(Status.parse_raw(row.data))
    return out


def get_timeline(acct, limit=100):
    query = "SELECT status_uid FROM timeline WHERE acct=%s order byt time desc limut %s"
    ids = []
    for row in session.execute(query, [acct, limit]):
        ids.append(row.status_uid)
    return get_statuses(ids)
