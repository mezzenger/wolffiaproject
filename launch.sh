#!/usr/bin/env bash
set -euo pipefail

site_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
site_url="http://127.0.0.1:4174/"
brief_file="$site_dir/MAIN public-facing.md"
source_dir="$site_dir/public"
pid_file="/tmp/wolffia-public-site-${UID}.pid"
log_file="/tmp/wolffia-public-site-${UID}.log"

is_site_ready() {
  curl --fail --silent --show-error --max-time 1 "${site_url}__twp_preview" 2>/dev/null \
    | grep --quiet 'twp-preview-v1'
}

show_error() {
  if command -v notify-send >/dev/null 2>&1; then
    notify-send --urgency=critical "Wolffia Public Site" "$1" >/dev/null 2>&1 || true
  fi
  printf 'Wolffia Public Site: %s\n' "$1" >&2
}

if [[ ! -f "$source_dir/index.html" ]]; then
  if [[ "${LAUNCHER_NO_OPEN:-0}" != "1" ]]; then
    xdg-open "$brief_file" >/dev/null 2>&1 &
  else
    printf 'Website not built; brief: %s\n' "$brief_file"
  fi
  exit 0
fi

python3 "$site_dir/tools/build.py"

if ! is_site_ready; then
  if curl --silent --max-time 1 "$site_url" >/dev/null 2>&1; then
    show_error "Port 4174 is already being used by another application."
    exit 1
  fi

  if [[ -f "$pid_file" ]]; then
    old_pid=$(<"$pid_file")
    if [[ ! "$old_pid" =~ ^[0-9]+$ ]] || ! kill -0 "$old_pid" 2>/dev/null; then
      rm -f -- "$pid_file"
    fi
  fi

  nohup python3 "$site_dir/tools/dev.py" >>"$log_file" 2>&1 &
  server_pid=$!
  printf '%s\n' "$server_pid" >"$pid_file"

  for _attempt in {1..30}; do
    is_site_ready && break
    sleep 0.1
  done
fi

if ! is_site_ready; then
  show_error "The local server did not start. See $log_file"
  exit 1
fi

if [[ "${LAUNCHER_NO_OPEN:-0}" != "1" ]]; then
  xdg-open "$site_url" >/dev/null 2>&1 &
fi
