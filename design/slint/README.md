# Slint Design Experiments

This folder holds the first Slint test path for OCI Design.

Slint is useful here because it gives agents a small declarative UI surface that can become a native prototype without starting from a full web app stack.

## Files

| File | Purpose |
|---|---|
| [`oci-design-smoke.slint`](oci-design-smoke.slint) | Minimal native UI sample for visual smoke testing. |
| [`smoke-test.sh`](smoke-test.sh) | Downloads official Slint release tools into a temporary directory, checks versions, and opens the sample with `slint-viewer`. |

## Quick Test

Run from the repo root:

```sh
design/slint/smoke-test.sh
```

The script uses Slint release `v1.17.0` by default. It downloads `slint-viewer-macos.tar.gz` and `slint-lsp-universal-apple-darwin.tar.gz` on macOS, unpacks them into a temporary tool directory, prints both versions, and opens the sample in `slint-viewer`.

To use an existing local Slint install instead:

```sh
OCI_SLINT_USE_PATH=1 design/slint/smoke-test.sh
```

To change the version:

```sh
OCI_SLINT_VERSION=1.17.0 design/slint/smoke-test.sh
```

## Full Source Build

The first OCI test should use official release binaries. A full upstream build is heavier and should be treated as future work:

1. Install Rust and Cargo.
2. Install CMake and Ninja.
3. Clone `https://github.com/slint-ui/slint`.
4. Follow the upstream build instructions for the target language and platform.

Do not commit downloaded binaries, generated build directories, or local tool caches.
