from __future__ import annotations

import re
import socket
from collections import Counter
from pathlib import Path


DATA_DIR = Path("/home/data")
OUT_PATH = DATA_DIR / "output" / "result.txt"

FILE1 = DATA_DIR / "IF.txt"
FILE2 = DATA_DIR / "AlwaysRememberUsThisWay.txt"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def tokenize_basic(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z]+", text.lower())


def tokenize_split_contractions(text: str) -> list[str]:
    text = text.replace("’", "'")
    text = text.replace("'", " ")
    return tokenize_basic(text)


def top_k(words: list[str], k: int = 3) -> list[tuple[str, int]]:
    return Counter(words).most_common(k)


def get_container_ip() -> str:
    """
    Best-effort way to get the container's outward-facing IP.
    No packets need to be sent; connect() just picks an interface.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception:
        # Fallback (may be 127.0.0.1 on some setups)
        try:
            return socket.gethostbyname(socket.gethostname())
        except Exception:
            return "UNKNOWN"
    finally:
        s.close()


def main() -> None:
    # Read files
    text1 = read_text(FILE1)
    text2 = read_text(FILE2)

    # (a) word counts for each file
    words1 = tokenize_basic(text1)
    words2_basic = tokenize_basic(text2)

    count1 = len(words1)
    count2 = len(words2_basic)

    # (b) grand total
    grand_total = count1 + count2

    # (c) top 3 in IF.txt
    top3_if = top_k(words1, 3)

    # (d) split contractions for AlwaysRemember... then top 3
    words2_split = tokenize_split_contractions(text2)
    stop_fragments = {"t", "s", "m", "re", "ve", "ll", "d"}
    words2_split = [w for w in words2_split if w not in stop_fragments]
    top3_always = top_k(words2_split, 3)

    # (e) IP address
    ip_addr = get_container_ip()

    # (f) write results
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("PROJECT 3: DOCKER - RESULTS")
    lines.append("")
    lines.append(f"(a) Total words in IF.txt: {count1}")
    lines.append(f"(a) Total words in AlwaysRememberUsThisWay.txt: {count2}")
    lines.append("")
    lines.append(f"(b) Grand total words (both files): {grand_total}")
    lines.append("")
    lines.append("(c) Top 3 most frequent words in IF.txt:")
    for w, c in top3_if:
        lines.append(f"  - {w}: {c}")
    lines.append("")
    lines.append("(d) Top 3 most frequent words in AlwaysRememberUsThisWay.txt (contractions split):")
    for w, c in top3_always:
        lines.append(f"  - {w}: {c}")
    lines.append("")
    lines.append(f"(e) Container/machine IP address: {ip_addr}")
    lines.append("")

    OUT_PATH.write_text("\n".join(lines), encoding="utf-8")

    # Print result.txt to console before exiting (required)
    print(OUT_PATH.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()