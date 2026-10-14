# Rethread disposable Python acceptance fixture

This repository exists for the owner's Rethread live acceptance journey. It
contains a deliberate duplicate-delivery bug, no real service or customer data,
and no runtime dependencies. It is disposable; retain created branches and
draft PRs as acceptance evidence until the owner authorizes cleanup.

Behavior requirement: repeated delivery of the same event queues exactly one
notification. Claiming the event and adding its durable outbox record must share
one transaction. Distinct events must each queue a notification.

The captured base intentionally fails
`python -m pytest -q tests/test_delivery.py::test_retry_delivery`.
The unchanged full suite is `python -m pytest -q`, and the lint check is
`python -m ruff check .`. Evaluator versions: pytest 9.1.1 and Ruff 0.17.0.

An empty requirements.lock declares a Python standard-library-only application.
The trusted E2B template supplies the evaluator; no model, GitHub or database
credentials belong in this fixture. Rethread's eventual verified repair must
include an additive guard that fails on this base and passes on the candidate.
