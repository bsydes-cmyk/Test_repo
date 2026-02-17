#!/usr/bin/env bash
# setup-cuda-dual.sh
# Configures dual CUDA toolkit support:
#   - CUDA 13.1 as system default (LD_LIBRARY_PATH)
#   - CUDA 12.8 available per-process for packages built against CUDA 12
#     (e.g., ctranslate2 / faster-whisper)
#
# Usage: source this script, or add the contents to ~/.bashrc
#
# Hardware assumption: RTX 4090, driver 591.86+ (supports CUDA <= 13.1)

set -euo pipefail

CUDA_13_DIR="/usr/local/cuda-13.1"
CUDA_12_DIR="/usr/local/cuda-12.8"
WSL_LIB="/usr/lib/wsl/lib"
BASHRC="$HOME/.bashrc"

# --- Validation -----------------------------------------------------------

check_path() {
    if [ ! -d "$1" ]; then
        echo "ERROR: $1 not found. Check your CUDA installation."
        exit 1
    fi
}

check_path "$CUDA_13_DIR/lib64"
check_path "$CUDA_12_DIR/lib64"
check_path "$WSL_LIB"

# --- Build the bashrc block -----------------------------------------------

BLOCK_START="# >>> cuda-dual-config >>>"
BLOCK_END="# <<< cuda-dual-config <<<"

read -r -d '' CUDA_BLOCK << 'CONF' || true
# >>> cuda-dual-config >>>
# System default: CUDA 13.1
export CUDA_HOME=/usr/local/cuda-13.1
export LD_LIBRARY_PATH=/usr/local/cuda-13.1/lib64:/usr/lib/wsl/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
export PATH=/usr/local/cuda-13.1/bin${PATH:+:$PATH}

# Per-process CUDA 12.8 launcher for packages built against CUDA 12
# Usage: cuda12 python my_script.py
cuda12() {
    LD_LIBRARY_PATH=/usr/local/cuda-12.8/lib64:/usr/lib/wsl/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH} "$@"
}

# Convenience alias for faster-whisper / ctranslate2 scripts
alias whisper-gpu='cuda12 python'
# <<< cuda-dual-config <<<
CONF

# --- Install to ~/.bashrc -------------------------------------------------

if grep -q "$BLOCK_START" "$BASHRC" 2>/dev/null; then
    echo "Existing cuda-dual-config block found in $BASHRC — replacing it."
    # Remove old block and replace
    tmpfile=$(mktemp)
    awk -v start="$BLOCK_START" -v end="$BLOCK_END" '
        $0 == start { skip=1; next }
        $0 == end   { skip=0; next }
        !skip
    ' "$BASHRC" > "$tmpfile"
    mv "$tmpfile" "$BASHRC"
fi

echo "" >> "$BASHRC"
echo "$CUDA_BLOCK" >> "$BASHRC"

echo ""
echo "Done. Added to $BASHRC:"
echo ""
echo "  System default:  CUDA 13.1  (LD_LIBRARY_PATH, CUDA_HOME, PATH)"
echo "  Per-process:     cuda12 <command>  → runs with CUDA 12.8 libs"
echo "  Alias:           whisper-gpu script.py  → cuda12 python script.py"
echo ""
echo "To activate now:  source ~/.bashrc"
echo ""
echo "--- Verification commands ---"
echo "  nvcc --version                     # should show 13.1"
echo "  python -c \"import torch; print(torch.cuda.is_available())\"   # True"
echo "  cuda12 python -c \"import ctranslate2; print('ct2 OK')\"       # ct2 OK"
echo "  whisper-gpu -c \"from faster_whisper import WhisperModel; m = WhisperModel('tiny', device='cuda'); print('GPU Whisper OK')\""
