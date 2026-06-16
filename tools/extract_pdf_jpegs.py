from pathlib import Path
import re
import sys


def jpeg_dimensions(data):
    i = 2
    while i < len(data) - 9:
        if data[i] != 0xFF:
            i += 1
            continue

        marker = data[i + 1]
        i += 2

        if marker in (0xD8, 0xD9):
            continue
        if marker == 0xDA or i + 2 > len(data):
            break

        length = int.from_bytes(data[i : i + 2], "big")
        if marker in range(0xC0, 0xC4) and i + 7 < len(data):
            height = int.from_bytes(data[i + 3 : i + 5], "big")
            width = int.from_bytes(data[i + 5 : i + 7], "big")
            return width, height

        i += length

    return 0, 0


def extract_largest_jpeg(pdf_path, output_path):
    data = pdf_path.read_bytes()
    images = [
        match.group(0)
        for match in re.finditer(rb"\xff\xd8.*?\xff\xd9", data, flags=re.DOTALL)
    ]
    if not images:
        raise ValueError(f"No JPEG image found in {pdf_path}")

    def score(image):
        width, height = jpeg_dimensions(image)
        return (width * height, len(image))

    image = max(images, key=score)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(image)
    width, height = jpeg_dimensions(image)
    print(f"{pdf_path.name} -> {output_path.name} ({width}x{height})")


def main():
    if len(sys.argv) < 3 or (len(sys.argv) - 2) % 2:
        raise SystemExit("Usage: extract_pdf_jpegs.py <out-dir> <pdf> <image> [<pdf> <image> ...]")

    out_dir = Path(sys.argv[1])
    pairs = sys.argv[2:]
    for index in range(0, len(pairs), 2):
        extract_largest_jpeg(Path(pairs[index]), out_dir / pairs[index + 1])


if __name__ == "__main__":
    main()
