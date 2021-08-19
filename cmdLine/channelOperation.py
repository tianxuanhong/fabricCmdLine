import os
from cmdLine.basicParameters import BasicEnv


class Channel(BasicEnv):
    """调用cmd执行channel create、join等相关操作"""

    def __init__(self, version, **kwargs):
        super(Channel, self).__init__(version, **kwargs)

    def create(self, channel, orderer_url, channel_tx, orderer_tls_rootcert, time_out="90s"):
        res = 0x100
        print("FABRIC_CFG_PATH", os.getenv("FABRIC_CFG_PATH"))
        print("CORE_PEER_TLS_ENABLED", os.getenv("CORE_PEER_TLS_ENABLED"))
        if os.getenv("CORE_PEER_TLS_ENABLED") == "false" or os.getenv("CORE_PEER_TLS_ENABLED") is None:
            if self.version in BasicEnv.binary_versions_v2:
                res = os.system("./../bin/{}/bin/peer channel create -c {} -o {} -f {} --timeout {}"
                                .format(self.version, channel, orderer_url, channel_tx, time_out))
        else:
            if self.version in BasicEnv.binary_versions_v2:
                res = os.system("./../bin/{}/bin/peer channel create -c {} -o {} -f {} --timeout {} --tls --cafile {}"
                                .format(self.version, channel, orderer_url, channel_tx, time_out, orderer_tls_rootcert))

        # peer channel create \
        # - c ${channel} \
        # - o ${orderer_url} \
        # - f ${CHANNEL_ARTIFACTS} /${channel_tx} \
        # - -timeout "${TIMEOUT}s"

        # os.system的返回值并不是执行程序的返回结果。而是一个16位的数，它的高位才是返回码
        res = res >> 8
        return res

    def join(self, block_file):
        res = 0x100
        if self.version in BasicEnv.binary_versions_v2:
            res = os.system("./../bin/{}/peer channel join -b {}".format(self.version, block_file))
        # peer channel join \
        # - b ${channel}.block \
        # > & log.txt
        res = res >> 8
        return res

    # 调用者负责提供存放文件的路径和文件名？
    def list(self, file_path):
        res = 0x100
        if self.version in BasicEnv.binary_versions_v2:
            res = os.system("./../bin/{}/peer channel list > &{}".format(self.version, file_path))
        # peer channel list > & log.txt
        return res

    def getinfo(self):
        # peer channel getinfo -c ${channel} >&log.txt
        return

    def fetch(self):
        # peer channel fetch $num ${block_file} \
        # - o ${orderer_url} \
        # - c ${channel} \
        # > & log.txt
        return

    def signconfigtx(self):
        # peer channel signconfigtx - f ${CHANNEL_ARTIFACTS} /${tx} > & log.txt
        return

    def update(self):
        # peer channel update \
        # - c ${channel} \
        # - o ${orderer_url} \
        # - f ${CHANNEL_ARTIFACTS} /${tx} \
        # > & log.txt
        return
