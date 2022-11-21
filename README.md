# Folx

Scalable Mastodon-compatible backend (Frontend Soon)
Twitter like microblogigng service

Implemented using:
- FastAPI (https://fastapi.tiangolo.com/)
- Scylla (https://www.scylladb.com/)

# Why?

There are a lot of conversations how many employees Twitter needs:

All great projects were started by somone hacking a prototype over a weekend. We had a lot of discussion how many people it takes to "run twitter". Obviously you need legal, HR, other BS but let's concentrate on tech.

George thinks you need 20:

![Twitter discussion screnshot](https://github.com/mag-/folx/blob/main/screenshots/twitter1.png?raw=true)

Francois even organized the team:

![Twitter discussion screnshot](https://github.com/mag-/folx/blob/main/screenshots/twitter2.png?raw=true)

But how many do you really need?

# Considerations

- We are going to start with a backend
- Twitter GraphQL API is just crazy, also maintaining proprietary API + open one looks to me like doing the same work twice.
- Mastodon has a nice OS X / Android client - I don't want to rebuild these


# What works

- basic API
- part of OAUTH
- posting
- getting timeline

# What is still outstanding
- review OAUTH once again
- all the easy APIs like tags etc
- ActivityPub
- Search

