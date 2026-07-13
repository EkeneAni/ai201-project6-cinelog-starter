# PR Response Doc — CineLog Watchlist Feature

## AI Usage
<!-- Fill in at the end — how you used AI tools during this project -->

## Comment 1 — Rename
**What I did:**

**How I verified:**
Basically used the search tool in the .py files to really make sure that the save_to_watchlist function was really renamed.

## Comment 2 — Deduplication
**What I did:**
I added the part of logic that checks for an existing film in the watchlist. I used this part add_to_collection in servises/collection_service.py:

# existing = CollcetionEntry.query.filter_by(
#       user_id=user_id, film_id=film_id
#    ).first()
#   if existing:
#       raise AlreadyInCollectionError(
#            f"Film '{film_id}' is already in this user's collection"
#        )


# existing = WatchlistEntry.query.filter_by(
#       user_id=user_id, film_id=film_id
#    ).first()
#   if existing:
#       raise AlreadyInCollectionError(
#            f"Film '{film_id}' is already in this user's watchlist"
#        )

I changed the CollectionEntry part to WatchlistEntry and changed the f-string at the end to watchlist instead of collection.

**How I verified:**
Since there is not test_watchlist.py as there is for the test_collection.py, I asked AI to verify if the logic was sound. Claude said that it was good logic only that it was semantically off because I'm calling AlreadyInCollectionError instead of a more fitting AlreadyInWatchlistError, but the latter doesn't exist so that is the best I can do for now. Maybe later I can make a test specifically for testing the watchlist.


## Comment 3 — Missing test
**What I did:**
I added a test_watchlist.py file to tests. This way, I can perform similar tests on the user's watchlist as I could on the user's collection.

**How I verified:**
I ran the tests using the command in the terminal and all 5 tests passed

## Comment 4 — Default visibility
**My position:**
**Reasoning:**
**Tradeoff acknowledged:**

## Comment 5 — Sort order
**My position:**
**Reasoning:**
**Engagement with reviewer's point:**

## Comment 6 — Rebase
**What conflicted:**
**How I resolved it:**
**How I verified no conflict remains:**

## PR Description
<!-- Written at the end — feature overview, design decisions, manual testing steps -->