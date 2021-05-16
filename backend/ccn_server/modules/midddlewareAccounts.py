import hashlib
from datetime import datetime
from time import time
class MiddleWareAccounts:

    def __init__(self):
        self.middleWareAccounts_faces = {}
        self.middleWareAccounts_thumbLeft = {}
        self.middleWareAccounts_thumbRight = {}
        self.usernames = {}
        self.accounts = {}
        self.transactions = {}
        self.usernames_accountKeys = {}
        self.paymentSessions = {}

    def _raiseErrorResponse(self,errorMsg):
        operation = {}
        operation["error"] = True
        operation["msg"] = errorMsg

        return operation


    def _buildUserName(self,face, thumbLeft, thumbRight,username):

        return (str(face) + "__" + str(thumbLeft) + "__" + str(thumbRight) + "__" + username)

    def _encoded_data(self, face, thumbLeft, thumbRight):

        face =  hashlib.sha256(face.encode()).hexdigest()
        thumbLeft =  hashlib.sha256(thumbLeft.encode()).hexdigest()
        thumbRight =  hashlib.sha256(thumbRight.encode()).hexdigest()

        return face,thumbLeft,thumbRight

    def getAccountDetailsByBiometric(self, face, thumbLeft, thumbRight):

        face,thumbLeft,thumbRight = self._encoded_data(face=face,thumbLeft=thumbLeft,thumbRight=thumbRight)

        if face in self.middleWareAccounts_faces and thumbLeft in self.middleWareAccounts_thumbLeft and thumbRight in self.middleWareAccounts_thumbRight:

            uFace = self.middleWareAccounts_faces[face]["username"]
            ulThumb = self.middleWareAccounts_thumbLeft[thumbLeft]["username"]
            urThumb = self.middleWareAccounts_thumbRight[thumbRight]["username"]

        

            if uFace == ulThumb and ulThumb == urThumb:

                constructorKey = self._buildUserName(face=face,thumbLeft=thumbLeft,thumbRight=thumbRight,username=uFace)
                return {"error":False,"account": self.accounts[constructorKey],"key": constructorKey,"username":uFace}

        

        return self._raiseErrorResponse("Account Not Found")


    def add_admin_balance(self, username, balanceAmount):

        operation = {
            "username":username,
            "balanceAmount":balanceAmount,
            "timestamp":str(datetime.now())
        }

        if username not in self.usernames_accountKeys:
            return {
                "error":True,"msg":"Invalid UserName: The Input Username doesn't exist.",**operation}
        constructorKey = self.usernames_accountKeys[username]

        try:
            balanceAmount = float(balanceAmount)
        except ValueError:
            return {"error":True,"msg":"Invalid Balance Amount, must be a numeric.",**operation}

        self.accounts[constructorKey]["balance"] += balanceAmount

        return {"error": False, "msg": "Successfully Added.",**operation}




    def register_user(self, face, thumbLeft, thumbRight,username):

        face,thumbLeft,thumbRight = self._encoded_data(face=face,thumbLeft=thumbLeft,thumbRight=thumbRight)

        if face in self.middleWareAccounts_faces:

            return self._raiseErrorResponse(errorMsg="The Facial Expression already exists.")

        else:
            self.middleWareAccounts_faces[face] = {
                "exists":True,
                "username":username
                }



        if thumbLeft in self.middleWareAccounts_thumbLeft:

            return self._raiseErrorResponse(errorMsg="The Left Thumb Expression already exists.")

        else:
            self.middleWareAccounts_thumbLeft[thumbLeft] = {
                "exists":True,
                "username":username
                }

        if thumbRight in self.middleWareAccounts_thumbRight:

            return self._raiseErrorResponse(errorMsg="The Right Thumb Expression already exists.")

        else:
            self.middleWareAccounts_thumbRight[thumbRight] = {
                "exists":True,
                "username":username
                }

        if username in self.usernames:

            return self._raiseErrorResponse(errorMsg="UserName unavailabe. Kindly try something else.")

        else:
            self.usernames[face] = {
                "exists": True,
                "userName":username
                }

        constructorKey = self._buildUserName(face=face,thumbLeft=thumbLeft,thumbRight=thumbRight,username=username)

        if constructorKey in self.accounts:

            return self._raiseErrorResponse(errorMsg="Account Already exists.")

        self.accounts[constructorKey] = {
            "balance" : 0,
            "isActive": True,
            "username": username
        }

        self.usernames_accountKeys[username] = constructorKey

        return {
            "error": False,
            "account": self.accounts[constructorKey]
        }


    def make_a_payment(self, face, thumbLeft, thumbRight, paymentObject):

        face,thumbLeft,thumbRight = self._encoded_data(face=face,thumbLeft=thumbLeft,thumbRight=thumbRight)
        

        if face not in self.middleWareAccounts_faces and thumbLeft not in self.middleWareAccounts_thumbLeft and thumbRight not in self.middleWareAccounts_thumbRight:
            return self._raiseErrorResponse(errorMsg="None of the Bio Data exists. Kindly Contact Administrator.")

        elif face in self.middleWareAccounts_faces and thumbLeft in self.middleWareAccounts_thumbLeft and thumbRight in self.middleWareAccounts_thumbRight:

            uFace = self.middleWareAccounts_faces[face]["username"]
            ulThumb = self.middleWareAccounts_thumbLeft[thumbLeft]["username"]
            urThumb = self.middleWareAccounts_thumbRight[thumbRight]["username"]

            if uFace == ulThumb and ulThumb == urThumb:

                constructorKey = self._buildUserName(face=face,thumbLeft=thumbLeft,thumbRight=thumbRight,username=uFace)
                return self.procceedToPayment(paymentObject=paymentObject,constructorKey=constructorKey)

        return False




    def procceedToPayment(self,constructorKey,paymentObject):

        bankBalance = self.accounts[constructorKey]["balance"]
        transferAmount = paymentObject["amount"]

        if bankBalance >= transferAmount:

            return True


    def createPaymentSession(self,username,paymentObject):

        self.paymentSessions[username] = {
            "sender":paymentObject["sender"],
            "reciever":paymentObject["reciever"],
            "amount": paymentObject["amount"],
            "timestamp": int(time()*1000)
        }

        return True

    def completeInternalPayment(self, paymentObject):

        now = time()*1000

        if((now - paymentObject["timestamp"])/(1000*60)) > 15:
            return {"error": True, "msg": "Session Expired. Please Retry the payment.","data": paymentObject}

        try:
            paymentObject["amount"] = float(paymentObject["amount"])
        except ValueError:
            return {"error": True, "msg": "Invalid Payment Amount.","data": paymentObject}

        self.accounts[self.usernames_accountKeys[paymentObject["sender"]]]["balance"] -= paymentObject["amount"]
        self.accounts[self.usernames_accountKeys[paymentObject["reciever"]]]["balance"] += paymentObject["amount"]

        return {"error": False, "msg": "Transaction Success","data": paymentObject}


    def deductWalletAmount(self,paymentObject):

        now = time()*1000

        if((now - paymentObject["timestamp"])/(1000*60)) > 15:
            return {"error": True, "msg": "Session Expired. Please Retry the payment.","data": paymentObject}


        try:
            paymentObject["amount"] = float(paymentObject["amount"])
        except ValueError:
            return {"error": True, "msg": "Invalid Payment Amount.","data": paymentObject}

        self.accounts[self.usernames_accountKeys[paymentObject["sender"]]]["balance"] -= paymentObject["amount"]

        return {"error": False, "msg": "Transaction Success","data": paymentObject}
        
                
        



        



    