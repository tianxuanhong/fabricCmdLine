from cmdLine.channelOperation import Channel


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
    print("res", res)


def channel_join():
    block_file = "/opt/gopath/src/github.com/hyperledger/celloCmdLine/fabricOperation/mychannel3.block"
    newchannel = Channel("v2.2.0", **envCli)
    res = newchannel.join(block_file)
    print()


if __name__ == "__main__":
    envCli = dict(CORE_PEER_LOCALMSPID="Org1MSP",
                  CORE_PEER_TLS_ROOTCERT_FILE="/opt/gopath/src/github.com/hyperledger/fabric-samples/test-network/"
                                              "organizations/peerOrganizations/org1.example.com/peers/"
                                              "peer0.org1.example.com/tls/ca.crt",
                  CORE_PEER_MSPCONFIGPATH="/opt/gopath/src/github.com/hyperledger/fabric-samples/test-network/"
                                          "organizations/peerOrganizations/org1.example.com/users/"
                                          "Admin@org1.example.com/msp",
                  CORE_PEER_ADDRESS="localhost:7051")
    # channel_create()
    channel_list()
    # channel_join()
