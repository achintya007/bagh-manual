# Troubleshooting

<!-- One entry per error message a user can see: the message, what it means, what
to do. -->

## "MemoryError: requested ... MB, available ... MB"

The calculation needs more memory than `max_memory`. Increase `max_memory`, or set
a lower `incore_level` (see [Run settings](run_settings.md)).
