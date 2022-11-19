from app.main import get_password_hash
from .models import Account
from .services import insert_account, update_account_password

a = Account(
    acct="test",
    display_name="Test",
    followers_count=0,
    following_count=0,
    statuses_count=0,
    url="https://mastodon.social/@test",
    avatar="https://mastodon.social/avatars/original/missing.png",
    header="https://mastodon.social/headers/original/missing.png",
    emojis=[],
    fields=[],
    note="",
    locked=False,
    bot=False,
)
insert_account(a)
update_account_password("test", get_password_hash("test"))
