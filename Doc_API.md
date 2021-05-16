# API Documentation

## Get Chain

Get the details of a Blockchain Network by name.

**URL** : `/get_chain`

**Method** : `GET`

<!-- **Auth required** : YES -->

<!-- **Permissions required** : None -->

### Success Response

**Code** : `200`

**Sample Call** : 
Get the details of the Wallet Based Transaction Blockchain.

```json
{
    "apiKey":"tHHxAb2SMhXY0X4XqTGn",
    "chainName":"wallet"

}
```

**Response** :
```json
{
    "chain": [
        {
            "data": {},
            "index": 1,
            "previous_hash": "0",
            "proof": 1,
            "timestamp": "2021-05-16 11:01:40.518221"
        }
    ],
    "length": 1
}
```


## Verify Blockchain

Validate blockchain by verifying hash signature of previous block.

**URL** : `/is_valid`

**Method** : `GET`

<!-- **Auth required** : YES -->

<!-- **Permissions required** : None -->

### Success Response

**Code** : `200`

**Sample Call** : 
Verify Wallet Based Transaction Blockchain.

```json
{
    "apiKey":"tHHxAb2SMhXY0X4XqTGn",
    "chainName":"wallet"

}
```

**Response** :
```json
{
    "message": true
}
```

## Add Wallet

Add a wallet to the `Wallet` database.

**URL** : `/add_wallet`

**Method** : `POST`

<!-- **Auth required** : YES -->

<!-- **Permissions required** : None -->

### Success Response

**Code** : `201`

**Sample Call** : 
Add a wallet to the `Wallet` database.

```json
{
    "apiKey":"tHHxAb2SMhXY0X4XqTGn",
    "chainName":"wallet"

}
```

**Response** :
```json
{
    "address": "1BFggXrXa27kSC1mfVa1SCQSUbd71BjCka",
    "error": false,
    "private": {
        "address": "1BFggXrXa27kSC1mfVa1SCQSUbd71BjCka",
        "balance": 0,
        "children": [
            {
                "address": "17PkKTrvwspVhN1ng4wYRtRRko8VzKrJ9u",
                "bip32_path": "m/44'/0'/0'/0",
                "path": "m/0",
                "xpublic_key": "xpub68iSkhBrxjMn2DFo4dnAThh9EgKtAkCjoNsp7n71qyjoxK5YAN9UtsJ9dHXm7UWAY1mXBHaiBH8je9cHpWNGC25XpxQf1vXo3kgrqZxdkqY"
            }
        ],
        "coin": "UCW",
        "private_key": "1b80fa6a5af8f6498e4c0971267b5d295df94f5a0736492853e97b962d40138e",
        "public_key": "04b91c1de71390e0674fbcbf8a842a597dde4b156475b9102f1640303741b5209cc1b1740da87fdaffa2b03632670236c188636c90ab4209351a92ac8d36078672",
        "seed": "again forum output capable tent topple kiss letter face filter venture rough",
        "wif": "Kx9B5ziM1T6cASjB6FDWGe7wKeaEX25wvuYojCYVMSdGkA6ZY1te",
        "xprivate_key": "xprv9s21ZrQH143K3H992rKrzhysLJaCPUoSZe12bPtGENJf44oNnRPuTziTywr6VPavqPunRXEWS8EvoQq7fQoAWpqTtKVpPoKUBN8iih1FxJ1",
        "xpublic_key": "xpub661MyMwAqRbcFmDc8srsMqvbtLQgnwXHvrvdPnHsnhqdvs8XKxiA1o2wqE5GmQDP41t4knSw3ectBCgsbLYJUca5iKNsiwUPPETWfVs4c9M",
        "xpublic_key_prime": "xpub68iSkhC1JPtkBsexo8GRbdz3Cs7ZzN7VEPy2kmacVrCBqfX4yEV981KX1GQ7XZFJmRGsGwsY7QGSfofKKcKn8dTpzzr7aC6eQ2FnhGBiqdy"
    },
    "public": {
        "balance": 0,
        "coin": "UCW",
        "isActive": true,
        "private_key": "bba46f0c739be64166cb7de50b38e95ccfe4fddbbe5705dfb956b819b56a7202"
    }
}
```

## Deposit Coins in User Wallet

Admin adds coins to user wallet.

**URL** : `/add_wallet_coins_admin`

**Method** : `POST`

<!-- **Auth required** : YES -->

<!-- **Permissions required** : None -->

### Success Response

**Code** : `200`

**Sample Call** : 
Admin adds 20 `UCW` coins to a user. Use case example: NGO depositing funds to a user.

```json
{
    "apiKey":"tHHxAb2SMhXY0X4XqTGn",
    "chainName":"wallet",
    "adminAPIKey": "l1sGuEEKtv7Rm9VakXhU7gyzlqXpR8Z2",
    "publicAddress": "1BFggXrXa27kSC1mfVa1SCQSUbd71BjCka",
    "newBalance": 20

}
```

**Response** :
```json
{
    "error": false,
    "msg": "Success"
}
```
**Note:**
Wallet asscociated with `publicAddress` must exist in the `Wallet` database. Otherwise, the response is:
```json
{
    "error": true,
    "msg": "Wallet Address doesn't exist."
}
```

## Transfer Coins

Transfer coins between wallets via a public address.

**URL** : `/add_transaction`

**Method** : `POST`

<!-- **Auth required** : YES -->

<!-- **Permissions required** : None -->

### Success Response

**Code** : `201`

**Sample Call** : 
Transfer coins between two users.

```json
{
    "apiKey":"tHHxAb2SMhXY0X4XqTGn",
    "chainName":"wallet",
    "sender":"1BFggXrXa27kSC1mfVa1SCQSUbd71BjCka",
    "reciever":"19XhgCCAr3GkcevqGgAbFygUKkg6nTjqKp",
    "amount":5


}
```

**Response** :
```json
{
    "error": false,
    "msg": "Transaction Success."
}
```

## Replace Chain

If running multiple nodes, keep the blockchain with the largest chain. Get details about the largest chain.

**URL** : `/replace_chain`

**Method** : `GET`

<!-- **Auth required** : YES -->

<!-- **Permissions required** : None -->

### Success Response

**Code** : `200`

**Sample Call** : 
Keep the largest blockchain that is running on network nodes.

```json
{
    "apiKey":"tHHxAb2SMhXY0X4XqTGn",
    "chainName":"wallet"
}
```

**Response** :
```json
{
    "actual_chain": [
        {
            "data": {},
            "index": 1,
            "previous_hash": "0",
            "proof": 1,
            "timestamp": "2021-05-16 11:24:51.129006"
        },
        {
            "data": {
                "amount": 5,
                "coin": "UCW",
                "date": "05/16/2021, 12:09:43",
                "success": true,
                "timestamp": "2021-05-16 12:09:43.151553",
                "transfer_from": "1BFggXrXa27kSC1mfVa1SCQSUbd71BjCka",
                "transfer_to": "19XhgCCAr3GkcevqGgAbFygUKkg6nTjqKp"
            },
            "index": 2,
            "previous_hash": "89df9cf6b288fb60abe06256a2d549b45bc5c9d0048ea9a7bc78b02ba4bb5d86",
            "proof": 533,
            "timestamp": "2021-05-16 12:09:43.155543"
        }
    ],
    "message": "All good. The chain is largest one."
}
```

## Connect Node

Connect a node to the blockchain network.

**URL** : `/connect_node`

**Method** : `POST`

<!-- **Auth required** : YES -->

<!-- **Permissions required** : None -->

### Success Response

**Code** : `201`

**Sample Call** : 
Connect nodes to the blockchain network.

```json
{
    "apiKey":"tHHxAb2SMhXY0X4XqTGn",
    "chainName":"wallet",
    "nodes": ["http://localhost:5001","http://localhost:5000"]
}
```

**Response** :
```json
{
    "message": "All the nodes are now connected. The Blockchain contains:",
    "total_nodes": [
        "localhost:5000",
        "localhost:5001"
    ]
}
```





