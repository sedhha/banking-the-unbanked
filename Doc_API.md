# API Documentation

## Get Chain

Get the details of a Blockchain Network by name.

**URL** : `/get_chain`

**Method** : `GET`

**Request** : 

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

**Request** : 

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

**Request** : 

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

**Request** : 
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

**Request** : 
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

**Request** : 

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

Connect additional nodes for decentralized network.

**URL** : `/connect_node`

**Method** : `POST`

**Request** : 

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

## Check if Wallet Exists

Check if wallet exists in database.

**URL** : `/does-wallet-exist`

**Method** : `POST`

**Request** : 

```json
{
    "apiKey":"tHHxAb2SMhXY0X4XqTGn",
    "chainName":"wallet",
    "wallets": ["1AiQYb7gvL2SEGhchf1HRQs2VMs93MXpFR"]
}
```

**Response** : Returns `false` even if a single wallet doesn't exist.
```json
{
    "error": false,
    "msg": "Wallet Exists. We can make the transfer."
}
```

## Get Central Wallet

Get central wallet that is connected to CCN server.

**URL** : `/get-central-wallet`

**Method** : `GET`

**Request** : 

```json
{
    "apiKey":"tHHxAb2SMhXY0X4XqTGn",
    "chainName":"wallet"
}
```

**Response** :
```json
{
    "address": "1JVwnjyUg7CB57CrP64b6j73ejr1Hmv43c",
    "centralWallet": {
        "balance": 0,
        "coin": "UCW",
        "isActive": true,
        "private_key": "bf0e2714298d0b7247f3884384c8731bb96ccb9d479e56d286221036646a9539"
    },
    "error": false,
    "msg": "Success"
}
```

# Middleware Methods

## Register User

Register User.

**URL** : `localhost:6000/register_user`

**Method** : `POST`

**Request** : 

```json
{
    "face":"Shivam_2",
    "thumbLeft":"ShivamLeft_2",
    "thumbRight":"ShivamRight_2",
    "username":"Spidey_2"
}
```

**Response** :
```json
{
    "account": {
        "balance": 0,
        "isActive": true,
        "username": "Spidey_2"
    },
    "error": false
}
```

## Get Transaction History

Get transaction history from biometric data.

**URL** : `localhost:6000/get_transaction_history`

**Method** : `GET`

**Request** : 

```json
{
    "face":"Shivam",
    "thumbLeft":"ShivamLeft",
    "thumbRight":"ShivamRight"
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
            "timestamp": "2021-05-16 18:08:57.680579"
        },
        {
            "data": {
                "data": {
                    "amount": 2.0,
                    "reciever": "Spidey_2",
                    "sender": "Spidey",
                    "timestamp": 1621167852165
                },
                "error": false,
                "msg": "Transaction Success"
            },
            "index": 2,
            "previous_hash": "4a6f45d43ca232a230f293a6bf20e10d94bfc58e9b46cfe3f867f6b3cc6f923e",
            "proof": 533,
            "timestamp": "2021-05-16 18:08:57.682551"
        },
        {
            "data": {
                "data": {
                    "amount": 2,
                    "reciever": "Spidey_2",
                    "sender": "Spidey",
                    "timestamp": 1621167852165
                },
                "error": true,
                "msg": "Session Expired. Please Retry the payment."
            },
            "index": 3,
            "previous_hash": "8680a50c2f7c9fd67f7e98adf9c297e75f8b34bab0b21d94ebdcc64ef59c4ef5",
            "proof": 45293,
            "timestamp": "2021-05-16 18:09:41.035862"
        },
        {
            "data": {
                "data": {
                    "amount": 2.0,
                    "reciever": "Spidey_2",
                    "sender": "Spidey",
                    "timestamp": 1621168775080
                },
                "error": false,
                "msg": "Transaction Success"
            },
            "index": 4,
            "previous_hash": "c17d888548d7682dfac515270e3bb1a18604ce2dda48c8846a6bbeb50efffd5b",
            "proof": 21391,
            "timestamp": "2021-05-16 18:09:54.471139"
        },
        {
            "data": {
                "data": {
                    "amount": 2.0,
                    "reciever": "Spidey_2",
                    "sender": "Spidey",
                    "timestamp": 1621168775080
                },
                "error": false,
                "msg": "Transaction Success"
            },
            "index": 5,
            "previous_hash": "9a992a9590e207aec38c5e76ab89a1f658ccd2bed6d7514c6e33cfdb0823cd09",
            "proof": 8018,
            "timestamp": "2021-05-16 18:10:20.822176"
        },
        {
            "data": {
                "data": {
                    "amount": 3.0,
                    "reciever": "Spidey_2",
                    "sender": "Spidey",
                    "timestamp": 1621168775080
                },
                "error": false,
                "msg": "Transaction Success"
            },
            "index": 6,
            "previous_hash": "9ce771db0b01a0fe174a9b5c480c0a0cbf2aa675e4be8499e95b085fd44e1d1a",
            "proof": 48191,
            "timestamp": "2021-05-16 18:10:40.098534"
        }
    ],
    "length": 6
}
```

## Add Wallet Coins

Add wallet coins via administrator account.

**URL** : `localhost:6000/add_wallet_coins_admin`

**Method** : `POST`

**Request** : 

```json
{
    "adminAPIKey":"l1sGuEEKtv7Rm9VakXhU7gyzlqXpR8Z2",
    "username":"Spidey",
    "balance":"22.4"
}
```

**Response** :
```json
{
    "result": "Success"
}
```

## View Admin Transactions

Get admin based transactions.

**URL** : `localhost:6000/admin_ops`

**Method** : `GET`

**Request** : 

```json
{
    "adminAPIKey":"l1sGuEEKtv7Rm9VakXhU7gyzlqXpR8Z2"
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
            "timestamp": "2021-05-16 17:38:12.424467"
        },
        {
            "data": {
                "balanceAmount": "22.4",
                "error": false,
                "msg": "Successfully Added.",
                "timestamp": "2021-05-16 17:38:23.049965",
                "username": "Spidey"
            },
            "index": 2,
            "previous_hash": "a698099f243bd84f7d581c54b98f8501cfb46c0b27c2df510bd8d7eb454b76dd",
            "proof": 533,
            "timestamp": "2021-05-16 17:38:23.051944"
        }
    ],
    "length": 2
}
```

## Check if Wallet Exists

Check if wallet exists in database by pinging to CCN server (note that here both the servers must be On).

**URL** : `localhost:6000/does-wallet-exist`

**Method** : `POST`

**Request** : 

```json
{
    "face":"Shivam",
    "thumbLeft":"ShivamLeft",
    "thumbRight":"ShivamRight",
    "wallets": ["1M1DnLFfXLzMoD4wEHJReqGRt2nwLNvYJb"]
}
```

**Response** :
```json
{
    "error": true,
    "msg": "Wallet Address doesn't exist."
}
```

## Get Central Wallet

Get central wallet address from CCN server.

**URL** : `localhost:6000/get-central-wallet`

**Method** : `GET`

**Request** : 

```json
{
    "face":"Shivam",
    "thumbLeft":"ShivamLeft",
    "thumbRight":"ShivamRight"
}
```

**Response** :
```json
{
    "address": "1M1DnLFfXLzMoD4wEHJReqGRt2nwLNvYJb",
    "centralWallet": {
        "balance": 0,
        "coin": "UCW",
        "isActive": true,
        "private_key": "9e5d8fdd283844547d6a24840b9db1750ab95bf58d932e10b8c66dddc370a069"
    },
    "error": false,
    "msg": "Success"
}
```


## Two Factor Authenticatio - Step One

First step requires facial and biometric data.

**URL** : `localhost:6000/add_transaction_step_01`

**Method** : `POST`

**Request** : 

```json
{
    "face":"Shivam",
    "thumbLeft":"ShivamLeft",
    "thumbRight":"ShivamRight",
    "payment": {
        "amount":2,
        "sender":"Spidey",
        "reciever":"Spidey_2"
    }
}
```

**Response** :
```json
{
    "error": false,
    "msg": "Payment Session Created. Kindly Verify with your Right Thumb Impression",
    "timeStamp": 1621169930093
}
```

## Add Transaction

Make the Payment after second verification. In the first verification step, user gives facial and biometric data. For the second step, user only gives biometric data.

**URL** : `localhost:6000/add_transaction`

**Method** : `POST`

**Request** : 

```json
{
    "face":"Shivam",
    "thumbLeft":"ShivamLeft",
    "thumbRight":"ShivamRight",
    "apiKey":"tHHxAb2SMhXY0X4XqTGn",
    "chainName":"",
    "payment": {
        "amount":3,
        "sender":"Spidey",
        "reciever":"Spidey_2",
        "timestamp": 1621169726145
    },
    "paymentType":"internal"
}
```

**Response** :
```json
{
    "data": {
        "amount": 3,
        "reciever": "Spidey_2",
        "sender": "Spidey",
        "timestamp": 1621169726145
    },
    "error": true,
    "msg": "Session Expired. Please Retry the payment."
}
```

