from cmdLine.channelOperation import Channel
from cmdLine.chaincodeOperation import ChainCode


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


def channel_join():
    block_file = "/opt/gopath/src/github.com/hyperledger/celloCmdLine/fabricOperation/mychannel3.block"
    newchannel = Channel("v2.2.0", **envCli)
    res = newchannel.join(block_file)
    print()


def channel_getinfo():
    newchannel = Channel("v2.2.0", **envCli)
    channel_name = "mychannel3"
    res = newchannel.getinfo(channel_name)
    print("content", res[0])
    print("res", res[1])


def chaincode_package():
    newchaincode = ChainCode("v2.2.0", **envCli)
    cc_name = "example02"
    cc_path = "github.com/chaincode/go/example02"
    cc_version = "1.0"
    language = "golang"
    res = newchaincode.lifecycle_package(cc_name, cc_version, cc_path, language)
    print(res)


def chaincode_install():
    newchaincode = ChainCode("v2.2.0", **envCli)
    cc_targz = "./example02.tar.gz"
    res = newchaincode.lifecycle_install(cc_targz)
    print("res:", res)


def chaincode_query_installed():
    newchaincode = ChainCode("v2.2.0", **envCli)
    timeout = "3s"
    res, content = newchaincode.lifecycle_query_installed(timeout)
    print("res", res, content)


def chaincode_get_installed_package():
    newchaincode = ChainCode("v2.2.0", **envCli)
    timeout = "3s"
    res = newchaincode.lifecycle_get_installed_package(timeout)
    print("res", res)


def chaincode_lifecycle_approve_for_my_org():
    orderer_url = "localhost:7050"
    orderer_tls_rootcert = "/opt/gopath/src/github.com/hyperledger/fabric-samples/test-network/organizations/" \
                           "ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/" \
                           "tlsca.example.com-cert.pem"
    channel_name = "mychannel3"
    chaincode_name = "example02"
    chaincode_version = "label"
    package_id = "example02_label:d3ea0e44f81e1d9bb6cee4441563e0adfeba3c32dd34ecb330890939a9884266"
    policy = "\"OR ('Org1MSP.member','Org2MSP.member')\""
    newchaincode = ChainCode("v2.2.0", **envCli)
    res = newchaincode.lifecycle_approve_for_my_org(orderer_url, orderer_tls_rootcert, channel_name, chaincode_name,
                                     chaincode_version, policy)


def chaincode_lifecycle_query_approved():
    channel_name = "mychannel3"
    cc_name = "example02"
    newchaincode = ChainCode("v2.2.0", **envCli)
    res = newchaincode.lifecycle_query_approved(channel_name, cc_name)
    print("res", res)


if __name__ == "__main__":
    envCli = dict(CORE_PEER_LOCALMSPID="Org1MSP",
                  CORE_PEER_TLS_ROOTCERT_FILE="/opt/gopath/src/github.com/hyperledger/fabric-samples/test-network/"
                                              "organizations/peerOrganizations/org1.example.com/peers/"
                                              "peer0.org1.example.com/tls/ca.crt",
                  CORE_PEER_MSPCONFIGPATH="/opt/gopath/src/github.com/hyperledger/fabric-samples/test-network/"
                                          "organizations/peerOrganizations/org1.example.com/users/"
                                          "Admin@org1.example.com/msp",
                  CORE_PEER_ADDRESS="localhost:7051")
    # # channel_create()
    # channel_list()
    # # channel_join()
    # channel_getinfo()
    # chaincode_package()
    # chaincode_install()
    # chaincode_query_installed()
    # chaincode_get_installed_package()
    # chaincode_lifecycle_approve_for_my_org()
    chaincode_lifecycle_query_approved()
