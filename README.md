# Banking the Unbanked

Banking the Unbanked
User Story Overview

We aim to build a Full Stack architecture that inputs the User Bio-Signature which includes digital fingerprint and Facial Recognition and use this data to generate a hash that acts as a bio-digital currency for the end user to facilitate all the banking services, starting with deposit and withdrawals using crypto.
In addition to this, with the help of the platform we’re trying to build we also intend to track homeless people, their financial condition in a more accurate way (as we have all their bio-digital bank balance) and use this data to not just reach the NGOs but also facilitate middle class and upper-class people, who have the access to smartphone resources to be able to help them.

With our approach, the NGOs and the helpers will not just be able to target a community but a single individual as well and we believe that will help in having a better reach and traction over the poverty and homelessness.

## Architecture Details

Our Framework is a middleware (crypt-in) that has the access to what we call as CCN server. A CCN Server is nothing but a collection of three units: -
- CCN Global Bank Account
- CCN Crypto Wallet
- CCN Conversion Unit

CCN Global Bank Account is the Account that serves as a point of contact to all the Global Currency. This is the Bank Account that is also going to facilitate all sorts of banking services. In simple words it’s just a bank account whose operations are handled by CCN Server that in turn is handled by our middleware.
There’s no third party or interface that talks directly to CCN Server other than crypt-in.

CCN Crypto Wallet is like any other Crypto wallet that is capable of accepting and sending cryptos. This takes care of all sorts of crypto handling for CCN server.

Finally, CCN Conversion Unit is like the bridge between the crypto and the actual currency. This is an intelligent system that binds both crypto and currency to exist in an interchangeable form to the best extent possible.

As not all cryptos can be cashed-in so this unit does have its limitation but in simple words CCN is an attempt to make Currency and Crypto interchangeable so to facilitate the banking process to the best possible way.

Currently CCN Conversion Unit is beyond the scope of our project as it needs a deep-down research and familiarity with many other factors.
How does Crypt-in talk with homeless?

Crypt-in ingests in the biosignatures of numerous homeless individuals. Any homeless who is interested in availing digital banking services just needs to give their finger-print and get themselves captured at a Crypt-in center (It not necessarily has to be a center, because the capturing process could be done with a simple hardware setup).

Once the data is ready, Crypt-in ingests this all data, it hash-encrypts the two data (facial and digital fingerprint) and stores it into the database.

A UUID is generated with this data which is kept for reference of the user. Now next time the person who is registered into Crypt-in needs not to carry the cash while going to any super market or grocery store.

With the help of their biosignature they can access their bio-digital currency anywhere in the world (provided the store has this biometric hardware which is very similar to a debit/credit card machine). With the help of two factor authentication, that is during the payment: -

- First user verifies his identity using his Face and Thumb Impression.
- Once the verification is successful, then user is able to see the amount to be transacted, bank account and date details after which he/she could approve it with their final little finger impression to make the transaction.

Doesn’t that sound so cool? A person carrying all their worth within themselves? Additionally, the same person is discoverable in case they need help by numerous NGOs, middle class, upper class people all around the world.

Additionally, in case of an unfortunate incident where person may end up losing their facial structure or fingers, there is a provision in our system to revoke the access or refresh the account credentials with the help of following authentication methods: -

- Facial and Both Thumb Verification
- Facial and Both Little Finger Verification
- All Finger Verification
- Facial and Any Two Finger Verification
- Facial, one Finger and Security Question Verification
- Security Questions Verification (Worst Case Scenario)


In Addition to this, we also feature a Web-UI that a homeless (if they get chance) can use to check their balances and try to register for other services which is beyond the scope of this project at the moment.
