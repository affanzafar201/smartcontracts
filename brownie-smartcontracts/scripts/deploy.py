from brownie import accounts, SimpleStorage, FundMe


def deploy_simple_storage():
    account = accounts[0]

    SimpleStorage.deploy({"from": account})

def deploy_fund_me():
    account = accounts[0]
    print(account)
    print(account.balance())
    print("Deploying")
    fund_me = FundMe.deploy({"from": account})
    print("Deployed at", fund_me.address)
    account_new = accounts[1]
    new_fund = fund_me.donate({"from": account_new, "value" : 1200})
    account_new_new = accounts[2]
    fund_me.sendTo("0x33A4622B82D4c04a53e170c638B944ce27cffce3", {"from": account_new_new, "value" : 1200})
    print(account, account_new, account_new_new)
    print(account_new_new.balance(), account_new.balance(), account.balance())
    fund_me.withDraw({"from": account_new_new})
    print(account_new_new.balance(), account_new.balance(), account.balance())


def main():
    deploy_fund_me()
