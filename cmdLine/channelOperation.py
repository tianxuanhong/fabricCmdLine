import os
import json
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
            res = os.system("./../bin/{}/bin/peer channel join -b {}".format(self.version, block_file))
        # peer channel join \
        # - b ${channel}.block \
        # > & log.txt
        res = res >> 8
        return res

    # 调用者负责提供存放文件的路径和文件名？
    def list(self):
        res = 0x100
        content = ""
        if self.version in BasicEnv.binary_versions_v2:
            res = os.system("./../bin/{}/bin/peer channel list > ./list.txt".format(self.version))
            with open('./list.txt', 'r', encoding='utf-8') as f:
                content = f.read()
            content = content.split("\n")
            os.system("rm ./list.txt")

        # peer channel list > & log.txt
        return res, content[1:-1]

    def getinfo(self, channel):
        res = 0x100
        if self.version in BasicEnv.binary_versions_v2:
            res = os.system("./../bin/{}/bin/peer channel getinfo -c {} > ./getinfo.txt".format(self.version, channel))
            with open('./getinfo.txt', 'r', encoding='utf-8') as f:
                content = f.read()
            content = content.split("\n")[0].split(":", 1)[1]
            # content = content.split("\n")[0]
            os.system("rm ./getinfo.txt")
        block_info = json.loads(content)
        body = {"block_info": block_info}
        # peer channel getinfo -c ${channel} >&log.txt
        return res, body

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
