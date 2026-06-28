#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/../.." && pwd -P)"
SAMPLE="${SCRIPT_DIR}/oci-design-smoke.slint"

VERSION="${OCI_SLINT_VERSION:-1.17.0}"
TOOL_DIR="${OCI_SLINT_TOOL_DIR:-${TMPDIR:-/tmp}/oci-slint-v${VERSION}}"
BIN_DIR="${TOOL_DIR}/bin"
BASE_URL="https://github.com/slint-ui/slint/releases/download/v${VERSION}"

mkdir -p "${BIN_DIR}"

download_and_unpack() {
  local asset="$1"
  local marker="$2"
  local archive="${TOOL_DIR}/${asset}"

  if [[ -x "${marker}" ]]; then
    return
  fi

  if [[ ! -f "${archive}" ]]; then
    curl -L --fail --show-error --output "${archive}" "${BASE_URL}/${asset}"
  fi

  tar -xzf "${archive}" -C "${BIN_DIR}"
}

tool_path() {
  local name="$1"
  local direct="${BIN_DIR}/${name}/${name}"

  if [[ -x "${direct}" ]]; then
    printf '%s\n' "${direct}"
    return
  fi

  find "${BIN_DIR}" -maxdepth 3 -type f -name "${name}" -perm -111 -print -quit
}

if [[ "${OCI_SLINT_USE_PATH:-0}" == "1" ]]; then
  SLINT_VIEWER="$(command -v slint-viewer || true)"
  SLINT_LSP="$(command -v slint-lsp || true)"
else
  case "$(uname -s)" in
    Darwin)
      download_and_unpack "slint-viewer-macos.tar.gz" "${BIN_DIR}/slint-viewer/slint-viewer"
      download_and_unpack "slint-lsp-universal-apple-darwin.tar.gz" "${BIN_DIR}/slint-lsp/slint-lsp"
      ;;
    Linux)
      download_and_unpack "slint-viewer-linux.tar.gz" "${BIN_DIR}/slint-viewer/slint-viewer"
      download_and_unpack "slint-lsp-linux.tar.gz" "${BIN_DIR}/slint-lsp/slint-lsp"
      ;;
    *)
      echo "Unsupported OS for automated Slint smoke test: $(uname -s)" >&2
      exit 1
      ;;
  esac

  SLINT_VIEWER="$(tool_path slint-viewer)"
  SLINT_LSP="$(tool_path slint-lsp)"
fi

if [[ -z "${SLINT_VIEWER}" || -z "${SLINT_LSP}" ]]; then
  echo "Could not locate slint-viewer or slint-lsp after unpacking release assets." >&2
  exit 1
fi

echo "Repo: ${REPO_ROOT}"
"${SLINT_VIEWER}" --version
"${SLINT_LSP}" --version

if [[ "${OCI_SLINT_VERSION_ONLY:-0}" == "1" ]]; then
  exit 0
fi

exec "${SLINT_VIEWER}" "${SAMPLE}"
