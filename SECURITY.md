# Security Policy

## Public Repo Notice

This repository is public. Do not publish live credentials, `.env` files, private keys, Oracle confidential material, customer context, local runtime state, or internal-only operating notes.

## Reporting

For a security concern in this repository, open a private issue or contact the maintainer directly. Do not include secret values in public issues, pull requests, comments, screenshots, or logs.

## Pre-Push Check

From `/Users/gmaiera/Documents/GitHub`, run:

```bash
./codex-config/scripts/public-content-scan
./codex-config/scripts/security-scan-workspace
```
