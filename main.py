import os

# One-Liner Laugh Lab — the excuse a robot vacuum gives after eating a sock.
# Final line (Builder 2 re-critique confirmed Builder 1's pick G).
LINE = "The sock was already unpaired. I simply completed the divorce."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
