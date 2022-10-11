from web3 import Web3
import random

url = "http://localhost:7545"   # 以太坊测试链 rpc 连接端口
contract_address_file = 'contract_address.txt'  # 合约地址保存文件
account_id = 0
abi_file = "TetherToken.abi"

# 连接测试链
w3 = Web3(Web3.HTTPProvider(url))   
eth = w3.eth
print("eth connect:", w3.isConnected())

def set_default_account():
    """
        设置调用合约、发送交易的账户
    """
    global account_id
    eth.defaultAccount = eth.accounts[account_id]

def get_abi_from_file(file):
    """
       从文件中获取abi
    """
    with open(file, 'r') as f:
        return f.read() 

def get_bytecode_from_file(file):
    """
        从文件中获取字节码
    """
    with open(file, 'r') as f:
        return "0x" + f.read()

def get_deployed_contract(abi):
    """
        获取部署合约，如果本地已保存合约地址，则调用该地址的合约，否则重新创建一个新的合约
    """
    f = open(contract_address_file, "r")
    contract_address = f.read()
    print("contract address:", contract_address)
    deployed_contract = eth.contract(address=contract_address, abi=abi)
    return deployed_contract

if __name__ == '__main__':
    set_default_account()
    abi = get_abi_from_file(abi_file)
    for account in eth.accounts:
        print(account)
    deployed_contract = get_deployed_contract(abi)
    for i in range(10):
        print("processing transaction" + str(i) + "...")
        deployed_contract.functions.transfer(eth.accounts[random.randint(0,9)], i + 1).transact()
