import os
import time
import struct
import hashlib
import secrets
import re
import sys
import random
import zlib
from PIL import Image
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.prompt import Prompt
from rich.table import Table
from rich import box
from colorama import init

init()
console = Console()

VERSION = "1.0 PNG CONTAINER EDITION"
LSB_LIMIT = 50000   # 50KB threshold
# ============================================================
# ===================== COMPRESSION ==========================
# ============================================================

def compress_data(data):
    return zlib.compress(data, level=9)

def decompress_data(data):
    return zlib.decompress(data)
# ============================================================
# ===================== SOUND ================================
# ============================================================

def sound_click(): print("\a")
def sound_success(): print("\a\a")
def sound_error(): print("\a\a\a")

# ============================================================
# ===================== ASCII INTRO ==========================
# ============================================================



console = Console()


def typewriter(text, style="bold green1", delay=0.002):
    """Typewriter effect"""
    for char in text:
        console.print(char, style=style, end="")
        time.sleep(delay)
    console.print()


def hacker_shadow_intro():
    console.clear()

    banner = [
        " ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗",
        " ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║",
        " ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║",
        " ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║",
        " ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝",
        " ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝",
    ]

    # Fake system boot sequence
    boot_lines = [
        "[+] Initializing secure runtime...",
        "[+] Injecting adaptive stego engine...",
        "[+] Loading AES-256 encryption core...",
        "[+] Calibrating PNG container layers...",
        "[✓] SHADOW framework ready.",
    ]

    for line in boot_lines:
        typewriter(line, style="green3", delay=0.01)
        time.sleep(0.2)

    time.sleep(0.5)
    console.print()

    # Print banner with slight glitch flicker
    for line in banner:
        glitch_line = ""
        for char in line:
            if char != " " and random.random() < 0.02:
                glitch_line += random.choice("#$%&@")
            else:
                glitch_line += char

        console.print(glitch_line, style="bold green1")
        time.sleep(0.05)

    console.print()

    # Hacker panel
    tagline = Panel.fit(
        "[bold green1]DarkPixel v1.0 — SHADOW Edition[/bold green1]\n"
        "[green3]Hybrid Steganography Framework[/green3]\n"
        "[green3]AES-256 | Adaptive LSB | PNG Container[/green3]",
        border_style="green4",
        style="black",
    )

    console.print(tagline)


if __name__ == "__main__":
    hacker_shadow_intro()
# ============================================================
# ===================== ANIMATIONS ===========================
# ============================================================

def matrix_rain():
    console.clear()
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for _ in range(10):
        line = "".join(secrets.choice(chars) for _ in range(60))
        console.print(f"[green]{line}[/green]")
        time.sleep(0.05)

def glitch_intro():
    frames = [
        "[bold magenta]C Y B E R   C O N T A I N E R[/bold magenta]",
        "[bold cyan]C Y 8 E R   C 0 N T A ! N E R[/bold cyan]",
        "[bold green]C Y B E R   C O N T A I N E R[/bold green]",
    ]
    console.clear()
    for _ in range(2):
        for frame in frames:
            console.print(Panel.fit(frame, border_style="magenta"))
            time.sleep(0.2)
            console.clear()
    matrix_rain()
    console.print(Panel.fit(
        f"[bold magenta]SECURE CONTAINER v{VERSION}[/bold magenta]\n"
        "[cyan]AES-256-GCM | SHA256 Integrity | PNG Embedded[/cyan]",
        border_style="bright_magenta"
    ))

# ============================================================
# ===================== PASSWORD STRENGTH ====================
# ============================================================

def password_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"[0-9]", password): score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): score += 1

    levels = {
        0: ("Very Weak", "red"),
        1: ("Weak", "red"),
        2: ("Moderate", "yellow"),
        3: ("Good", "cyan"),
        4: ("Strong", "green"),
        5: ("Very Strong", "bright_green")
    }

    label, color = levels[score]
    console.print(f"Password Strength: [{color}]{label}[/{color}]")

# ============================================================
# ===================== CRYPTO ===============================
# ============================================================

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_data(data, password):
    salt = secrets.token_bytes(16)
    key = derive_key(password, salt)
    aes = AESGCM(key)
    nonce = secrets.token_bytes(12)
    encrypted = aes.encrypt(nonce, data, None)
    return salt + nonce + encrypted

def decrypt_data(data, password):
    salt = data[:16]
    nonce = data[16:28]
    ciphertext = data[28:]
    key = derive_key(password, salt)
    aes = AESGCM(key)
    return aes.decrypt(nonce, ciphertext, None)

# ============================================================
# ===================== FILE CONTAINER =======================
# ============================================================

def sha256(data):
    return hashlib.sha256(data).digest()

def pack_files(file_paths):
    container = b''
    container += struct.pack(">I", len(file_paths))

    for path in file_paths:
        filename = os.path.basename(path).encode()
        with open(path, "rb") as f:
            content = f.read()

        file_hash = sha256(content)

        container += struct.pack(">I", len(filename))
        container += filename
        container += struct.pack(">I", len(content))
        container += content
        container += file_hash

    return container

def unpack_files(data, output_folder):
    offset = 0
    file_count = struct.unpack(">I", data[offset:offset+4])[0]
    offset += 4

    for _ in range(file_count):
        name_len = struct.unpack(">I", data[offset:offset+4])[0]
        offset += 4

        filename = data[offset:offset+name_len].decode()
        offset += name_len

        content_len = struct.unpack(">I", data[offset:offset+4])[0]
        offset += 4

        content = data[offset:offset+content_len]
        offset += content_len

        stored_hash = data[offset:offset+32]
        offset += 32

        os.makedirs(output_folder, exist_ok=True)

        with open(os.path.join(output_folder, filename), "wb") as f:
            f.write(content)

        if sha256(content) == stored_hash:
            console.print(f"[bold green]✓ {filename} verified[/bold green]")
        else:
            console.print(f"[bold red]✗ {filename} corrupted[/bold red]")

# ============================================================
# ================= PNG CONTAINER EMBED ======================
# ============================================================
def embed_payload_into_existing_png(input_png, payload, output_png):
    with open(input_png, "rb") as f:
        data = f.read()

    png_signature = data[:8]
    offset = 8
    new_png = png_signature

    def png_chunk(chunk_type, data):
        chunk = chunk_type + data
        return (
            struct.pack(">I", len(data)) +
            chunk +
            struct.pack(">I", zlib.crc32(chunk) & 0xffffffff)
        )

    # Fake metadata
    fake_text = b"Software\x00Adobe Photoshop 2024"
    text_chunk = png_chunk(b'tEXt', fake_text)

    while offset < len(data):
        length = struct.unpack(">I", data[offset:offset+4])[0]
        chunk_type = data[offset+4:offset+8]

        chunk_total = 12 + length
        chunk_data = data[offset:offset+chunk_total]

        if chunk_type == b'IEND':
            new_png += text_chunk  # inject fake metadata
            scnr_chunk = png_chunk(b'sCNR', payload)
            new_png += scnr_chunk

        new_png += chunk_data
        offset += chunk_total

    with open(output_png, "wb") as f:
        f.write(new_png)
# ============================================================
# ================= PNG PAYLOAD EXTRACT ======================
# ============================================================

def extract_payload_from_png(png_path):
    with open(png_path, "rb") as f:
        data = f.read()

    offset = 8

    while offset < len(data):
        length = struct.unpack(">I", data[offset:offset+4])[0]
        offset += 4

        chunk_type = data[offset:offset+4]
        offset += 4

        chunk_data = data[offset:offset+length]
        offset += length
        offset += 4

        if chunk_type == b'sCNR':
            return chunk_data

    return None

# ============================================================
# ================= IMAGE CAPACITY CHECKER ===================
# ============================================================

def capacity_checker():
    image_path = Prompt.ask("[cyan]Enter Image Path[/cyan]")
    if not os.path.exists(image_path):
        console.print("[red]Image not found[/red]")
        return

    img = Image.open(image_path)
    width, height = img.size
    pixels = width * height

    capacity_bits = pixels * 3
    capacity_bytes = capacity_bits // 8

    table = Table(title="Image Capacity Report", box=box.ROUNDED)
    table.add_column("Metric", style="magenta")
    table.add_column("Value", style="cyan")

    table.add_row("Resolution", f"{width} x {height}")
    table.add_row("Theoretical Capacity", f"{capacity_bytes/1024:.2f} KB")

    console.print(table)
    
# ============================================================
# ===================== LSB CAPACITY =========================
# ============================================================
def check_lsb_capacity(image_path, payload_size):

    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())

    noisy_pixels = 0

    for pixel in pixels:
        if is_noisy(pixel):
            noisy_pixels += 1

    capacity = noisy_pixels * 3 // 8

    return payload_size <= capacity

# ============================================================
# ===================== SYSTEM INFO ==========================
# ============================================================

def system_info():
    table = Table(title="System Diagnostics", box=box.ROUNDED)
    table.add_column("Property", style="magenta")
    table.add_column("Value", style="cyan")

    table.add_row("OS", sys.platform)
    table.add_row("Python", sys.version.split()[0])
    table.add_row("Version", VERSION)

    console.print(table)

# ============================================================
# ===================== FLOWS ================================
# ============================================================

def hide_flow():
    files_input = Prompt.ask("[cyan]Files to Secure (comma separated)[/cyan]")
    password = Prompt.ask("[cyan]Password[/cyan]", password=True)
    password_strength(password)
    output = Prompt.ask("[cyan]Output Image Name[/cyan]")

    output = os.path.splitext(output)[0] + ".png"

    file_paths = [f.strip() for f in files_input.split(",")]
    container = pack_files(file_paths)

    compressed = compress_data(container)

    container = compressed

    with Progress(
        SpinnerColumn(),
        TextColumn("[cyan]Encrypting Secure Container..."),
        BarColumn(),
        transient=True,
    ) as progress:
        task = progress.add_task("encrypt", total=100)
        for i in range(100):
            time.sleep(0.01)
            progress.update(task, advance=1)

    encrypted = encrypt_data(container, password)

    cover_image = Prompt.ask("[cyan]Cover PNG Image[/cyan]")

    if check_lsb_capacity(cover_image, len(encrypted)):
        console.print("[green]Using Adaptive LSB Steganography[/green]")
        success = embed_lsb(cover_image, encrypted, output)

    if not success:
        console.print("[yellow]Falling back to PNG chunk container...[/yellow]")
        embed_payload_into_existing_png(cover_image, encrypted, output)
    else:
        console.print("[yellow]Using PNG Chunk Container[/yellow]")
        embed_payload_into_existing_png(cover_image, encrypted, output)

    console.print("[bold green]PNG Secure Container Created Successfully[/bold green]")
    stealth = Prompt.ask("[red]Enable Stealth Mode? (y/n)[/red]").lower()

    if stealth == "y":
        for path in file_paths:
            secure_delete(path)
        console.print("[bold red]Original files securely deleted[/bold red]")
def secure_delete(file_path):
    if os.path.exists(file_path):
        size = os.path.getsize(file_path)
        with open(file_path, "wb") as f:
            f.write(secrets.token_bytes(size))
        os.remove(file_path)
        
MAX_ATTEMPTS = 3

def extract_flow():
    container_file = Prompt.ask("[cyan]PNG Container File[/cyan]")
    output_folder = Prompt.ask("[cyan]Output Folder[/cyan]")

    attempts = 0

    encrypted = extract_payload_from_png(container_file)

    if encrypted is None:
        console.print("[yellow]No PNG chunk found — trying LSB extraction[/yellow]")
        encrypted = extract_lsb(container_file)

    if encrypted is None:
        console.print("[red]No hidden payload found[/red]")
        return

    while attempts < MAX_ATTEMPTS:

        password = Prompt.ask("[cyan]Password[/cyan]", password=True)

        try:
            decrypted = decrypt_data(encrypted, password)

            decompressed = decompress_data(decrypted)

            unpack_files(decompressed, output_folder)

            console.print("[bold green]Extraction Completed[/bold green]")
            sound_success()
            return

        except Exception:
            attempts += 1
            console.print(f"[red]Wrong password ({attempts}/{MAX_ATTEMPTS})[/red]")
            sound_error()

    console.print("[bold red]MAX ATTEMPTS REACHED — SELF DESTRUCT TRIGGERED[/bold red]")
    destroy_payload(container_file)
    
def destroy_payload(png_path):

    with open(png_path, "rb") as f:
        data = bytearray(f.read())

    offset = 8

    while offset < len(data):

        length = struct.unpack(">I", data[offset:offset+4])[0]
        chunk_type = data[offset+4:offset+8]

        if chunk_type == b'sCNR':
            start = offset + 8
            end = start + length

            # overwrite payload
            for i in range(start, end):
                data[i] = secrets.randbelow(256)

            break

        offset += length + 12

    with open(png_path, "wb") as f:
        f.write(data)

    console.print("[bold red]Container payload destroyed[/bold red]")
# ============================================================
# ===================== ADAPTIVE ANALYSIS ====================
# ============================================================
def is_noisy(pixel):
    return True
    
def embed_lsb(image_path, payload, output_path):

    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())

    payload += b"<<<END>>>"
    binary = ''.join(format(byte, '08b') for byte in payload)

    data_index = 0
    new_pixels = []

    for r, g, b in pixels:

        if is_noisy((r,g,b)) and data_index < len(binary):

            r = (r & ~1) | int(binary[data_index])
            data_index += 1

            if data_index < len(binary):
                g = (g & ~1) | int(binary[data_index])
                data_index += 1

            if data_index < len(binary):
                b = (b & ~1) | int(binary[data_index])
                data_index += 1

        new_pixels.append((r, g, b))

    # 🔴 CRITICAL CHECK
    if data_index < len(binary):
        console.print("[bold red]ERROR: Not enough noisy pixels to embed full payload![/bold red]")
        return False

    img.putdata(new_pixels)
    img.save(output_path, format="PNG", optimize=False)
    return True
    
def extract_lsb(image_path):

    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())

    bits = ""

    for r, g, b in pixels:

        # MUST match embed logic
        if not is_noisy((r,g,b)):
            continue

        bits += str(r & 1)
        bits += str(g & 1)
        bits += str(b & 1)

    bytes_data = bytearray()

    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            break

        bytes_data.append(int(byte, 2))

        if bytes_data.endswith(b"<<<END>>>"):
            return bytes(bytes_data[:-9])

    return None
# ============================================================
# ===================== MAIN ================================
# ============================================================

def main():
    hacker_shadow_intro()
    glitch_intro()

    while True:
        table = Table(box=box.ROUNDED)
        table.add_column("Option", style="magenta")
        table.add_column("Action", style="cyan")

        table.add_row("1", "Secure Multiple Files")
        table.add_row("2", "Extract Files")
        table.add_row("3", "Image Capacity Checker")
        table.add_row("4", "System Diagnostics")
        table.add_row("5", "Exit")

        console.print(table)
        choice = Prompt.ask("[green]Select Option[/green]")

        if choice == "1":
            hide_flow()
        elif choice == "2":
            extract_flow()
        elif choice == "3":
            capacity_checker()
        elif choice == "4":
            system_info()
        elif choice == "5":
            break
        else:
            console.print("[red]Invalid Option[/red]")

if __name__ == "__main__":
    main()