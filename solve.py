import requests,urllib3,hashlib,re
urllib3.disable_warnings()

def get_hash(n):
    rep = requests.get(f"https://www.challengecybersec.fr/9bcb53d26eab7e9e08cc9ffae4396b48/blog/post/{n}",verify=False)  # f pour formater la chaine
    return re.findall('<span id="partial-proof">(.*?)<\/span>', rep.text)[0]


def check_proof(digest):
    rep = requests.post("https://www.challengecybersec.fr/9bcb53d26eab7e9e08cc9ffae4396b48/check-proof", data={"proof": digest}, verify=False)
    print("---------------------------\n" + rep.text)

hashs = []

for indice in range(1, 1001):
    h = get_hash(indice)
    print(f'[+] {indice:4} {h}', end='\r')
    hashs.append(h)

h = hashlib.md5("".join(hashs).encode())
print(f'[+] le hash final est : {h.hexdigest()}')

check_proof(h.hexdigest())
