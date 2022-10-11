### 1. 部署合约

在`subgraph-TetherToken`目录下运行

```shell
truffle migrate
```

### 2. 修改合约地址

将`2_deploy_contract.js`中的`contract address`复制到

- `contract_address.txt`
- `subgraph.yaml`中的`dataSources->source->address`

```shell
2_deploy_contract.js
====================

   Replacing 'TetherToken'
   -----------------------
   > transaction hash:    0x017603ed2aad877985783a73a6649541dc6304c8ec1f3ef635c09db678f1fd11
   > Blocks: 0            Seconds: 0
   > contract address:    0x7DaedfeC02f43b10064Ce27D493536A4b405de36
   > block number:        3
   > block timestamp:     1665476050
   > account:             0x242A2bFcF6A1534d8A9FA27297D99D711173214C
   > balance:             99.94421192
   > gas used:            2580102 (0x275e86)
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.05160204 ETH


   > Saving migration to chain.
   > Saving artifacts
   -------------------------------------
   > Total cost:          0.05160204 ETH
```

### 3. 部署子图

```shell
yarn create-local
yarn deploy-local
```

### 4. 调用合约

在`script`目录下运行，随机生成10笔交易

```shell
python3 test.py
```

```shell
processing transaction0...
processing transaction1...
processing transaction2...
processing transaction3...
processing transaction4...
processing transaction5...
processing transaction6...
processing transaction7...
processing transaction8...
processing transaction9...
```

