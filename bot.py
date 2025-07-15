import os
import random
import string
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from time import sleep

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    clear()
    panel = Panel.fit(
        "[bold cyan]AUTO GENERATE GMAIL ALIAS[/bold cyan]\n[green]Dibuat oleh [bold yellow]kaydenzo[/bold yellow][/green]",
        title="📧 [bold]Email Alias Bot[/bold]",
        border_style="bright_white"
    )
    print(panel)

    print("[bold white]📌 Contoh:[/bold white]")
    print("- Titik : [yellow]kay.den.zo@gmail.com[/yellow]")
    print("- Plus  : [yellow]kaydenzo+promo123@gmail.com[/yellow]\n")

def menu():
    print("[bold white]Menu:[/bold white]")
    print("[green]1[/green] - Buat alias dengan titik")
    print("[green]2[/green] - Buat alias dengan plus")
    print("[green]3[/green] - Hapus isi file gmails.txt")
    print("[green]q[/green] - Keluar")
    pilihan = Prompt.ask("\n[bold white]Pilih menu[/bold white]", choices=["1", "2", "3", "q"])
    return pilihan

def generate_dot_alias(base_email, jumlah):
    username, domain = base_email.split("@")
    aliases = set()
    while len(aliases) < jumlah:
        positions = random.sample(range(1, len(username)), k=random.randint(1, min(3, len(username) - 1)))
        new_username = username
        for pos in sorted(positions, reverse=True):
            new_username = new_username[:pos] + '.' + new_username[pos:]
        aliases.add(f"{new_username}@{domain}")
    return list(aliases)

def generate_plus_alias(base_email, jumlah):
    username, domain = base_email.split("@")
    aliases = []
    for _ in range(jumlah):
        suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        aliases.append(f"{username}+{suffix}@{domain}")
    return aliases

def simpan_ke_file(filename, daftar_email):
    with open(filename, "w") as f:
        for email in daftar_email:
            f.write(email + "\n")

def hapus_file(filename):
    if os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("")
        print(f"[red]🗑️ File '{filename}' telah dikosongkan.[/red]\n")
    else:
        print(f"[yellow]⚠️ File '{filename}' tidak ditemukan.[/yellow]\n")

def main():
    while True:
        banner()
        pilihan = menu()
        
        if pilihan == "q":
            print("\n[green]Terima kasih sudah menggunakan Email Alias Bot. Sampai jumpa![/green]")
            break

        if pilihan == "3":
            hapus_file("gmails.txt")
            sleep(1)
            continue

        base_email = Prompt.ask("[bold white]Masukkan email utama (contoh: user@gmail.com)[/bold white]")
        if "@" not in base_email or "." not in base_email.split("@")[1]:
            print("[red]❌ Format email tidak valid![/red]\n")
            sleep(1)
            continue

        jumlah = IntPrompt.ask("[bold white]Berapa banyak alias yang ingin dibuat?[/bold white]")
        print("\n[bold cyan]⏳ Membuat alias, mohon tunggu...[/bold cyan]")
        sleep(1)

        if pilihan == "1":
            hasil = generate_dot_alias(base_email, jumlah)
        elif pilihan == "2":
            hasil = generate_plus_alias(base_email, jumlah)
        else:
            continue
        
        simpan_ke_file("gmails.txt", hasil)
        print("\n[green]✅ Alias berhasil dibuat dan disimpan ke file:[/green] [bold]gmails.txt[/bold]")
        print("[yellow]📁 Cek file tersebut untuk melihat hasilnya.[/yellow]\n")
        sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[red]❌ Dihentikan oleh pengguna.[/red]")
