# Challenge!
How much of twitter/mastodon one person can implement in a weekend?

Ok, won't be the whole weekend I have two small children, and have to wantch new Marvel movie in the cinema, let's say 16h of coding.

# Programming language
Few choices:
- Python (I'm most familiar with, will be fastest to write)
- Golang (Great if we need a large in-memory cache and run it on fly.io later)
- Rust (ok things will be fast but it will take 10x time to write)

https://www.techempower.com/benchmarks/#section=data-r21&test=query&l=yykfzz-6bj
Our use case is most comparable to "multiple queries" one.
actix-http - 29,198
fasthttp - 18,967
fastapi - 12,406

So, for 2.5x speedup how much more developer time? I don't know for now, we will use Python :)

# Database
Scalable (dynamo paper)
Really only one choice: ScyllaDB - https://www.scylladb.com/

# Frontend
Really we need a minimal javascript, just to refresh the timeline, rest can be boring html.

# ActivityPub
Need a minimal implementation just so one can follow on external server and people can follow back.
