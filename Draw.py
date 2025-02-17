import asyncio
import json
import time
from colorama import init, Fore, Style
from web3 import Web3
import aiohttp
import argparse
import pyfiglet
from colorama import init, Fore, Style

init(autoreset=True)

ascii_art = pyfiglet.figlet_format("EVERLEX AIRDROP", font="block")
print(Fore.CYAN + ascii_art)


# Konfigurasi URL RPC dan alamat kontrak
RPC_URL = "https://mainnet.base.org"
CONTRACT_ADDRESS = "0xC5bf05cD32a14BFfb705Fb37a9d218895187376c"
api_url = "https://hanafuda-backend-app-520478841386.us-central1.run.app/graphql"
AMOUNT_ETH = 0.0000000001  # Jumlah ETH yang akan disetor
web3 = Web3(Web3.HTTPProvider(RPC_URL))

# Membaca kunci pribadi dari file
with open("pvkey.txt", "r") as file:
    private_keys = [line.strip() for line in file if line.strip()]

# Membaca token akses dari file
with open("token.txt", "r") as file:
    access_tokens = [line.strip() for line in file if line.strip()]

# ABI Kontrak
contract_abi = '''
[
    {
        "constant": false,
        "inputs": [],
        "name": "depositETH",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    }
]
'''

# Header HTTP
headers = {
    'Accept': '*/*',
    'Content-Type': 'application/json',
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
}

# Fungsi untuk melakukan permintaan HTTP secara asinkron
async def colay(session, url, method, payload_data=None):
    async with session.request(method, url, headers=headers, json=payload_data) as response:
        if response.status != 200:
            raise Exception(f'Kesalahan HTTP! Kode Status: {response.status}')
        return await response.json()

# Fungsi untuk memperbarui token akses
async def refresh_access_token(session, refresh_token):
    api_key = "AIzaSyDipzN0VRfTPnMGhQ5PSzO27Cxm3DohJGY"  
    async with session.post(
        f'https://securetoken.googleapis.com/v1/token?key={api_key}',
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=f'grant_type=refresh_token&refresh_token={refresh_token}'
    ) as response:
        if response.status != 200:
            raise Exception("Gagal memperbarui token akses")
        data = await response.json()
        return data.get('access_token')

# Fungsi untuk menangani tugas pertumbuhan dan taman
async def handle_growth_and_garden(session, refresh_token):  
    new_token = await refresh_access_token(session, refresh_token)
    headers['authorization'] = f'Bearer {new_token}'

    # Mengambil informasi pengguna
    info_query = {
        "query": "query getCurrentUser { "
                  "currentUser { id totalPoint depositCount } "
                  "getGardenForCurrentUser { "
                  "gardenStatus { growActionCount gardenRewardActionCount } "
                  "} "
                  "}",
        "operationName": "getCurrentUser"
    }
    info = await colay(session, api_url, 'POST', info_query)
    
    # Menampilkan informasi pengguna
    balance = info['data']['currentUser']['totalPoint']
    deposit = info['data']['currentUser']['depositCount']
    growth = info['data']['getGardenForCurrentUser']['gardenStatus']['growActionCount']
    garden = info['data']['getGardenForCurrentUser']['gardenStatus']['gardenRewardActionCount']

    print(f"{Fore.GREEN}Poin: {balance} | Jumlah Deposit: {deposit} | Sisa Aksi Pertumbuhan: {growth} | Sisa Aksi Taman: {garden}{Style.RESET_ALL}")

    # Fungsi untuk menjalankan aksi pertumbuhan
    async def growth_action():
        growth_action_query = {
              "query": """
                  mutation executeGrowAction {
                      executeGrowAction(withAll: true) {
                          totalValue
                          multiplyRate
                      }
                      executeSnsShare(actionType: GROW, snsType: X) {
                          bonus
                      }
                  }
              """,
              "operationName": "executeGrowAction"
          }

        try:
            result = await colay(session, api_url, 'POST', growth_action_query)            
            if result and 'data' in result and 'executeGrowAction' in result['data']:
                reward = result['data']['executeGrowAction']['totalValue']
                return reward
            else:
                print(f"{Fore.RED}Kesalahan: Format respons tidak terduga: {result}{Style.RESET_ALL}")
                return 0  
        except Exception as e:
            return 0

    # Jika ada aksi pertumbuhan yang tersedia, jalankan
    if growth > 0:
        reward = await growth_action()
        if reward:            
            balance += reward
            growth = 0
            print(f"{Fore.GREEN}Hadiah: {reward} | Poin Saat Ini: {balance} | Sisa Aksi Pertumbuhan: {growth}{Style.RESET_ALL}")
              
    # Menjalankan aksi taman
    while garden >= 10:
        garden_action_query = {
            "query": "mutation executeGardenRewardAction($limit: Int!) { executeGardenRewardAction(limit: $limit) { data { cardId group } isNew } }",
            "variables": {"limit": 10},
            "operationName": "executeGardenRewardAction"
        }
        garden_result = await colay(session, api_url, 'POST', garden_action_query)
        card_ids = [item['data']['cardId'] for item in garden_result['data']['executeGardenRewardAction']]
        print(f"{Fore.GREEN}Taman Dibuka: {card_ids}{Style.RESET_ALL}")
        garden -= 10

# Fungsi utama
async def main(mode, num_transactions=None):
    async with aiohttp.ClientSession() as session:
        if mode == '1':
            if num_transactions is None:
                num_transactions = int(input(Fore.YELLOW + "Masukkan jumlah transaksi yang akan dieksekusi: " + Style.RESET_ALL))
            # await handle_eth_transactions(session, num_transactions)
                
        elif mode == '2':
            while True:  
                for refresh_token in access_tokens:
                    await handle_growth_and_garden(session, refresh_token)  
                print(f"{Fore.RED}Semua akun telah diproses, menunggu 10 menit...{Style.RESET_ALL}")
                await asyncio.sleep(600)  
        else:
            print(Fore.RED + "Pilihan tidak valid, silakan pilih 1 atau 2." + Style.RESET_ALL)

if __name__ == '__main__':
    asyncio.run(main('2'))
