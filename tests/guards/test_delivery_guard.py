from delivery import database, deliver, queued


def test_retry_delivery():
    db = database()
    deliver(db, "evt_42")
    deliver(db, "evt_42")
    assert queued(db) == 1
