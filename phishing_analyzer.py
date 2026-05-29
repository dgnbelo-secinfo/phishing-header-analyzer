import re

with open("sample_header.txt", "r", encoding="utf-8") as file:
    header = file.read()

print("\n=== PHISHING HEADER ANALYZER ===\n")

ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', header)

if ips:
    print("[+] IPs encontrados:")
    for ip in ips:
        print(f" - {ip}")

if "spf=fail" in header.lower() or "received-spf: fail" in header.lower():
    print("\n[!] SPF Failure detectado")

if "dkim=fail" in header.lower():
    print("[!] DKIM Failure detectado")

if "dmarc=fail" in header.lower():
    print("[!] DMARC Failure detectado")

if "paypal" in header.lower():
    print("\n[+] Possível spoofing envolvendo PayPal")

print("\n=== Análise concluída ===")