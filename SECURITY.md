# Security

Bundled Python tools use the standard library only, make no network requests,
execute no subprocesses, do not read secrets or `.env` files, and refuse to
remove unmanaged Claude/Codex skill installations.

Live research is performed by the host agent's authorized research tools.
