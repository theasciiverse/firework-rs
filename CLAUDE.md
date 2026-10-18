# firework-rs (Asciiverse packaging)

Wayoung7's firework-rs, ASCII fireworks in the terminal (Rust, crossterm),
MIT; catalog title "Fireworks", id `firework-rs`, kind `art`; the binary
is `firework`. Not our code: keep changes small, list every one in
PATCHES.md, and offer fixes upstream.

- Remotes: `upstream` is github.com/Wayoung7/firework-rs (branch
  `master`, quiet since 2024), `origin` is
  github.com/theasciiverse/firework-rs.
- Branch `asciiverse` = upstream master (v0.3.1) plus our commits.
- Release: tag `v<version>-av.<n>` (now `v0.3.1-av.1`) and push only that
  tag; the workflow runs on `*-av.*` tags.
- av starts it as `firework` (the endless random show).
- Static build, in a copy of the tree: `docker run --rm --cpus 4 --memory
  8g -v "$PWD":/src -w /src rust:1-alpine sh -c 'apk add musl-dev && cargo
  build --release --locked -j2'`.
- Preview: `asciiverse/record-preview.py target/release/firework raw.cast`,
  then `asciiverse/cast-cap-fps.py raw.cast asciiverse/firework.cast 20`
  (pyte).
