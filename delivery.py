"""Delivery module with atomic claim to avoid duplicate queueing."""
import sqlite3


def database():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE claims (event_id TEXT PRIMARY KEY)")
    db.execute("CREATE TABLE outbox (event_id TEXT NOT NULL)")
    return db


def deliver(db, event_id):
    """Enqueue an event only once using an atomic claim."""
    with db:
        # Try to claim the event; if already claimed, skip enqueue.
        claim_cur = db.execute(
            "INSERT OR IGNORE INTO claims(event_id) VALUES (?)", (event_id,)
        )
        if claim_cur.rowcount == 1:
            db.execute("INSERT INTO outbox(event_id) VALUES (?)", (event_id,))


def queued(db):
    return db.execute("SELECT count(*) FROM outbox").fetchone()[0]
