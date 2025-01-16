from domHttpx.colors import Color

def tab() -> None:
    """Mencetak baris kosong.
    Prints an empty line."""
    print('\n')

# Fungsi-fungsi untuk logging / Logging functions
def info(text: str) -> None:
    """Mencetak pesan informasi dengan warna biru.
    Prints information message in blue color."""
    print(f"[{Color.CBLUE2}INFO{Color.ENDC}] {text}")

def success(text: str) -> None:
    """Mencetak pesan sukses dengan warna hijau.
    Prints success message in green color."""
    print(f"\n[{Color.CGREEN2}SUCCESS{Color.ENDC}] {text}")

def error(text: str) -> None:
    """Mencetak pesan error dengan warna merah.
    Prints error message in red color."""
    print(f"[{Color.CRED2}ERROR{Color.ENDC}] {text}")

# Fungsi-fungsi untuk formatting text / Text formatting functions
def title(title: str) -> str:
    """Memformat judul dengan warna cyan.
    Formats title with cyan color."""
    return f"[{Color.CCYAN2}{title}{Color.ENDC}]"

# Fungsi-fungsi untuk status code formatting / Status code formatting functions
def sc_200(sc: str) -> str:
    """Memformat status code 2xx dengan warna hijau.
    Formats 2xx status codes in green color."""
    return f"[{Color.CGREEN2}{sc}{Color.ENDC}]"

def sc_500(sc: str) -> str:
    """Memformat status code 5xx dengan warna kuning.
    Formats 5xx status codes in yellow color."""
    return f"[{Color.CYELLOW2}{sc}{Color.ENDC}]"

def sc_other(sc: str) -> str:
    """Memformat status code lainnya dengan warna merah.
    Formats other status codes in red color."""
    return f"[{Color.CRED2}{sc}{Color.ENDC}]"