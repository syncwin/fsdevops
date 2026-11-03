# Offline cache, outbox and sync

- **Store:** drift (SQLite; web via WASM) as the default; existing store wins.
- **Reads:** UI watches the local store; the repository refreshes from the API and writes into the store (single source of truth on device).
- **Writes:** apply locally, insert an outbox row (`id`, `entity`, `op`, `payload`, `created_at`, `attempts`), then try to send. A sender drains the outbox in order when online, with backoff; it removes a row only after the server confirms.
- **Idempotency:** every outbox row carries a client-generated id the server can de-duplicate.
- **Conflicts:** server version per record; default last-write-wins per field with the server timestamp; when a conflict matters to the user, keep both and surface it.
- **Background sync:** only when the PRD needs it; desktop syncs on resume and on a timer while open; mobile background work is best effort, never promised.
- **Tests:** offline write then reconnect, duplicate send, conflict, app killed mid-send.
