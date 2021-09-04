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
    language = "golang"
    label = "example02_label"
    res = newchaincode.lifecycle_package(cc_name, cc_path, language, label)
    print(res)


def chaincode_install():
    newchaincode = ChainCode("v2.2.0", **envCli)
    cc_targz = "./example02.tar.gz"
    res = newchaincode. lifecycle_install(cc_targz)
    print("res:", res)


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
    chaincode_install()
