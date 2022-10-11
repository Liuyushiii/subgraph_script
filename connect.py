from web3 import Web3

url = "https://mainnet.infura.io/v3/bc46ea167e694b2291d174a88b486bd6"   # 以太坊测试链 rpc 连接端口

# 连接测试链
w3 = Web3(Web3.HTTPProvider(url))   
eth = w3.eth
print("eth connect:", w3.isConnected())
print(eth.blockNumber)