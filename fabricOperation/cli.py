from cmdLine.channelOperation import Channel
from cmdLine.chaincodeOperation import ChainCode
import json


def channel_create():
    channel_name = "mychannel3"
    orderer_url = "localhost:7050"
    channel_tx = "/opt/gopath/src/github.com/hyperledger/fabric-samples/test-network/channel-artifacts/mychannel3.tx"
    orderer_tls_rootcert = "/opt/gopath/src/github.com/hyperledger/fabric-samples/test-network/organizations/" \
                           "ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/" \
                           "tlsca.example.com-cert.pem"
    newchannel = Channel("v2.2.0", **envCli)
    res = newchannel.create(channel_name, orderer_url, channel_tx, orderer_tls_rootcert)
    print(res)


def channel_list():
    # file_path = "../log.txt"
    newchannel = Channel("v2.2.0", **envCli)
    res = newchannel.list()
    print("res", res[0])
    print("reslist", res[1])


def channel_join(org):
    block_file = "/opt/gopath/src/github.com/hyperledger/celloCmdLine/fabricOperation/mychannel3.block"
    if org == "org1":
        newchannel = Channel("v2.2.0", **envCli)
    else:
        newchannel = Channel("v2.2.0", **envCli2)
    res = newchannel.join(block_file)
    print()


def channel_getinfo():
    newchannel = Channel("v2.2.0", **envCli)
    channel_name = "mychannel3"
    res = newchannel.getinfo(channel_name)
    print("content", res[0])
    print("res", res[1])


def chaincode_package(org):
    if org == "org1":
        newchaincode = ChainCode("v2.2.0", **envCli)
    else:
        newchaincode = ChainCode("v2.2.0", **envCli2)
    cc_name = "example02"
    cc_path = "github.com/chaincode/go/example02"
    cc_version = "1.0"
    language = "golang"
    res = newchaincode.lifecycle_package(cc_name, cc_version, cc_path, language)
    print(res)


def chaincode_install(org):
    if org == "org1":
        newchaincode = ChainCode("v2.2.0", **envCli)
    else:
        newchaincode = ChainCode("v2.2.0", **envCli2)
    cc_targz = "./example02.tar.gz"
    res = newchaincode.lifecycle_install(cc_targz)
    print("res:", res)


def chaincode_query_installed(org):
    if org == "org1":
        newchaincode = ChainCode("v2.2.0", **envCli)
    else:
        newchaincode = ChainCode("v2.2.0", **envCli2)
    timeout = "3s"
    res, content = newchaincode.lifecycle_query_installed(timeout)
    print("res", res, content)


def chaincode_get_installed_package():
    newchaincode = ChainCode("v2.2.0", **envCli)
    timeout = "3s"
    res = newchaincode.lifecycle_get_installed_package(timeout)
    print("res", res)


def chaincode_lifecycle_approve_for_my_org(org):
    orderer_url = "localhost:7050"
    orderer_tls_rootcert = "/opt/gopath/src/github.com/hyperledger/fabric-samples/test-network/organizations/" \
                           "ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/" \
                           "tlsca.example.com-cert.pem"
    channel_name = "mychannel3"
    chaincode_name = "example02"
    chaincode_version = "1.0"
    package_id = "example02_label:d3ea0e44f81e1d9bb6cee4441563e0adfeba3c32dd34ecb330890939a9884266"
    policy = "\"OR ('Org1MSP.member','Org2MSP.member')\""
    if org == "org1":
        newchaincode = ChainCode("v2.2.0", **envCli)
    else:
        newchaincode = ChainCode("v2.2.0", **envCli2)
    sequence=1
    code, res = newchaincode.lifecycle_approve_for_my_org(orderer_url, orderer_tls_rootcert, channel_name, chaincode_name,
                                     chaincode_version, policy, sequence)
    print("code=",code)
    print("res", res)


def chaincode_lifecycle_query_approved():
    channel_name = "mychannel3"
    cc_name = "example02"
    newchaincode = ChainCode("v2.2.0", **envCli2)
    code, res = newchaincode.lifecycle_query_approved(channel_name, cc_name)
    print("code", code)
    print("res", res)


def chaincode_lifecycle_check_commit_readiness():
    orderer_url = "localhost:7050"
    orderer_tls_rootcert = "/opt/gopath/src/github.com/hyperledger/fabric-samples/test-network/organizations/" \
                           "ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/" \
                           "tlsca.example.com-cert.pem"
    channel_name = "mychannel3"
    cc_name = "example02"
    cc_version = "1.0"
    policy = "\"OR ('Org1MSP.member','Org2MSP.member')\""
    newchaincode = ChainCode("v2.2.0", **envCli)
    sequency=1
    code, res = newchaincode.lifecycle_check_commit_readiness(orderer_url, orderer_tls_rootcert, channel_name, cc_name,
                                                              cc_version, policy, sequency)
    print(code)
    print(res)


def chaincode_lifecycle_commit():
    orderer_url = "localhost:7050"
    orderer_tls_rootcert = "/opt/gopath/src/github.com/hyperledger/fabric-samples/test-network/organizations/" \
                           "ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/" \
                           "tlsca.example.com-cert.pem"
    channel_name = "mychannel3"
    cc_name = "example02"
    cc_version = "1.0"
    peerlist = ["localhost:7051", "localhost:9051"]
    peer_root_certs = ["/opt/gopath/src/github.com/hyperledger/fabric-samples/test-network/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt","/opt/gopath/src/github.com/hyperledger/fabric-samples/test-network/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt"]
    policy = "\"OR ('Org1MSP.member','Org2MSP.member')\""
    sequency=1
    newchaincode = ChainCode("v2.2.0", **envCli)
    res = newchaincode.lifecycle_commit(orderer_url, orderer_tls_rootcert, channel_name, cc_name, cc_version,
                                        policy, peerlist, peer_root_certs, sequency)
    print(res)


def chaincode_lifecycle_query_committed():
    channel_name = "mychannel3"
    cc_name = "example02"
    newchaincode = ChainCode("v2.2.0", **envCli)
    res = newchaincode.lifecycle_query_committed(channel_name, cc_name)
    print("res:", res)


def chaincode_invoke(init):
    orderer_url = "localhost:7050"
    orderer_tls_rootcert = "/opt/gopath/src/github.com/hyperledger/fabric-samples/test-network/organizations/" \
                           "ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/" \
                           "tlsca.example.com-cert.pem"
    channel_name = "mychannel3"
    cc_name = "example02"
    if init:
        args = '{"Args":["invoke","a","100","b","200"]}'
    else:
        args = '{"Args":["invoke","a","b","1"]}'
    newchaincode = ChainCode("v2.2.0", **envCli2)
    res = newchaincode.invoke(orderer_url, orderer_tls_rootcert, channel_name, cc_name, args, init)
    print(res)


def chaincode_query():
    orderer_url = "localhost:7050"
    orderer_tls_rootcert = "/opt/gopath/src/github.com/hyperledger/fabric-samples/test-network/organizations/" \
                           "ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/" \
                           "tlsca.example.com-cert.pem"
    channel_name = "mychannel3"
    cc_name = "example02"
    args1 = '{"Args":["query","b"]}'
    newchaincode = ChainCode("v2.2.0", **envCli)
    res = newchaincode.query(orderer_url, orderer_tls_rootcert, channel_name, cc_name, args1)
    print(res)


def chaincode_upgrade():
    orderer_url = "localhost:7050"
    orderer_tls_rootcert = "/opt/gopath/src/github.com/hyperledger/fabric-samples/test-network/organizations/" \
                           "ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/" \
                           "tlsca.example.com-cert.pem"
    channel_name = "mychannel"
    cc_name = "example02"
    cc_version = "1.0"
    upgrade_args = '{"Args":["init","a","100","b","200"]}'
    args1 = '{"Args":["query","b"]}'
    policy = "\"OR ('Org1MSP.member','Org2MSP.member')\""
    newchaincode = ChainCode("v2.2.0", **envCli)
    res = newchaincode.upgrade(orderer_url, orderer_tls_rootcert, channel_name, cc_name, cc_version,
                               upgrade_args, policy)
    print(res)


if __name__ == "__main__":
    envCli = dict(CORE_PEER_LOCALMSPID="Org1MSP",
                  CORE_PEER_TLS_ROOTCERT_FILE="/opt/gopath/src/github.com/hyperledger/fabric-samples/test-network/"
                                              "organizations/peerOrganizations/org1.example.com/peers/"
                                              "peer0.org1.example.com/tls/ca.crt",
                  CORE_PEER_MSPCONFIGPATH="/opt/gopath/src/github.com/hyperledger/fabric-samples/test-network/"
                                          "organizations/peerOrganizations/org1.example.com/users/"
                                          "Admin@org1.example.com/msp",
                  CORE_PEER_ADDRESS="localhost:7051")

    envCli2 = dict(CORE_PEER_LOCALMSPID="Org2MSP",
                   CORE_PEER_TLS_ROOTCERT_FILE="/opt/gopath/src/github.com/hyperledger/fabric-samples/test-network/"
                                               "organizations/peerOrganizations/org2.example.com/peers/"
                                               "peer0.org2.example.com/tls/ca.crt",
                   CORE_PEER_MSPCONFIGPATH="/opt/gopath/src/github.com/hyperledger/fabric-samples/test-network/"
                                           "organizations/peerOrganizations/org2.example.com/users/"
                                           "Admin@org2.example.com/msp",
                   CORE_PEER_ADDRESS="localhost:9051")

    # print("function: channel_create",)
    # channel_create()
    # print("\r\nfunction: channel_list",)
    # channel_list()
    # print("\r\nfunction: channel_join",)
    # channel_join("org1")
    # channel_join("org2")
    # print("\r\nfunction: channel_getinfo",)
    # channel_getinfo()
    #
    # print("\r\nfunction: chaincode_package",)
    # chaincode_package("org1")
    # chaincode_package("org2")
    # print("\r\nfunction: chaincode_install",)
    # chaincode_install("org1")
    # chaincode_install("org2")
    # print("\r\nfunction: chaincode_query_installed",)
    # chaincode_query_installed("org1")
    # chaincode_query_installed("org2")
    #
    # print("\r\nfunction: chaincode_get_installed_package",)
    # chaincode_get_installed_package()

    # print("\r\nfunction: chaincode_lifecycle_approve_for_my_org",)
    # chaincode_lifecycle_approve_for_my_org("org1")
    # chaincode_lifecycle_approve_for_my_org("org2")

    # print("\r\nfunction: chaincode_lifecycle_query_approved",)
    # chaincode_lifecycle_query_approved()
    # print("\r\nfunction: chaincode_lifecycle_check_commit_readiness",)
    # chaincode_lifecycle_check_commit_readiness()
    # #
    # print("\r\nfunction: chaincode_lifecycle_commit",)
    # chaincode_lifecycle_commit()
    # print("\r\nfunction: chaincode_lifecycle_query_committed",)
    # chaincode_lifecycle_query_committed()
    # print("\r\nfunction: chaincode_invoke",)
    chaincode_invoke(True)
    chaincode_invoke(False)
    # print("\r\nfunction: chaincode_query",)
    # chaincode_query()
    # print("\r\nfunction: chaincode_upgrade",)
    # chaincode_upgrade()
