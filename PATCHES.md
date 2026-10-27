# Changes from upstream

This is the Asciiverse packaging of [firework-rs](https://github.com/Wayoung7/firework-rs)
by Wayoung7: ASCII-art fireworks in the terminal, a Rust library and its
`firework` binary (crossterm). Upstream is the `upstream` remote; the
`asciiverse` branch carries the changes below.

Built from upstream `master` at `dc9213d` (2024-04-30), the commit after
the v0.3.1 tag that raises the version in Cargo.toml from 0.3.0 to 0.3.1;
the code is the tag's, and this is what crates.io has as 0.3.1. Upstream
has not changed since.

## Licence

MIT, "Copyright (c) 2024 Wayoung7" in LICENSE, and `license = "MIT"` in
Cargo.toml (checked 2026-10-18). Its crates (clap, crossterm, glam, rand,
rand_distr and theirs) are MIT, or MIT and Apache-2.0 dual licensed, by
`cargo metadata`; unicode-ident, which clap's derive macro uses while
compiling, adds the Unicode-DFS-2016 licence.

## Which mode

The binary has five fixed demos (`-d 0` to `-d 4`), which play a set show
and stop unless `-l` loops them, and, with no `-d`, an endless random show
that keeps launching fireworks of random colours at random places, as many
at a time as the window holds. av starts the endless show: it never
repeats and fills any window size. `-g` (colours fading to black) is left
off, since it suits only a black background.

## Code

- **Any key quits.** Upstream quit on Esc only; in raw mode Ctrl+C is a
  key too, so it did nothing. Any key press now quits, Ctrl+C included,
  and the terminal is put back as before. Key releases, which crossterm
  reports on Windows, do not count.

## Packaging

- Upstream's workflows (`build.yml`, a check on every push and every
  night, and `release.yml`, its own releases on `v*` tags) are removed.
- `.github/workflows/release.yml`: av archives `firework-rs-<target>` for
  Linux (static musl, x86-64 and ARM64, built in Alpine), macOS (x86-64
  and ARM64) and Windows (x86-64 and ARM64, MSVC), with the binary,
  LICENSE, README and this file, plus SHA256SUMS. Runs on our tags only
  (`*-av.*`).
- `asciiverse/record-preview.py` records the catalog preview: 25 seconds
  of `firework` at 100x30, then a key. firework repaints every cell every
  frame (83 MB raw), so `asciiverse/cast-cap-fps.py` (from the tarts
  packaging, needs pyte) re-encodes it at 20 fps with only the cells that
  change, as `asciiverse/firework.cast`.

av starts it as `firework` with no arguments.

## Checked

- Linux, static musl build (Alpine, rustc 1.99.0), in tmux at 100x30: q,
  Esc and Ctrl+C quit with status 0; with `-g`, resized to 40x12, 10x4 and
  120x40 it keeps running and x quits.
- Windows and macOS: `cargo check` for x86_64-pc-windows-msvc and
  aarch64-apple-darwin passes; not run.

## Ours

- **How to play it, at the top of README.md.** A short note on installing and
  starting it with av, or from a release archive; the original text follows
  unchanged.
