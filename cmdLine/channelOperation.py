import os
import json
import subprocess
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

        # os.system的返回值并不是执行程序的返回结果。而是一个16位的数，它的高位才是返回码
        res = res >> 8
        return res

    def join(self, block_file):
        res = 0x100
        if self.version in BasicEnv.binary_versions_v2:
            res = os.system("./../bin/{}/bin/peer channel join -b {}".format(self.version, block_file))
        res = res >> 8
        return res

    # 调用者负责提供存放文件的路径和文件名？
    def list(self):
        res = 0x100
        content = ""
        if self.version in BasicEnv.binary_versions_v2:
            res = subprocess.Popen("./../bin/{}/bin/peer channel list".format(self.version), shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            stdout, stderr = res.communicate()
            return_code = res.returncode

            if return_code == 0:
                content = str(stdout, encoding="utf-8")
                content = content.split("\n")
                return return_code, content[1:-1]
            else:
                return return_code, stderr

        return res, content[1:-1]

    def getinfo(self, channel):
        if self.version in BasicEnv.binary_versions_v2:
            res = subprocess.Popen("./../bin/{}/bin/peer channel getinfo -c {}".format(self.version, channel),
                                   shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = res.communicate()
            return_code = res.returncode

            if return_code == 0:
                content = str(stdout, encoding="utf-8")
                content = content.split("\n")[0].split(":", 1)[1]

                block_info = json.loads(content)
                body = {"block_info": block_info}
            else:
                stderr = str(stderr, encoding="utf-8")
                return return_code, stderr
        # peer channel getinfo -c ${channel} >&log.txt
        return return_code, body

    def fetch(self):
        # peer channel fetch $num ${block_file} \
        # - o ${orderer_url} \
        # - c ${channel} \
        # > & log.txt
        # try:
        #     res = os.system("{} channel fetch {} -c {} -o {} --timeout {}".format(
        #         self.peer, option, channel, orderer_url, time_out))
        # except Exception as e:
        #     err_msg = "fetch a specified block failed {}!".format(e)
        #     raise Exception(err_msg)
        # res = res >> 8
        # return res
        return

    def signconfigtx(self):
        # peer channel signconfigtx - f ${CHANNEL_ARTIFACTS} /${tx} > & log.txt
        # try:
        #     res = os.system(
        #         "{} channel signconfigtx -f {}".format(self.peer, channel_tx))
        # except Exception as e:
        #     err_msg = "signs a configtx update failed {}".format(e)
        #     raise Exception(err_msg)
        # res = res >> 8
        # return res
        return

    def update(self):
        # try:
        #     res = os.system("{} channel update -c {}  -f {} -o {}"
        #                     .format(self.peer, channel, channel_tx, orderer_url))
        # except Exception as e:
        #     err_msg = "update channel failed for {e}!"
        #     raise Exception(err_msg)
        # res = res >> 8
        # return res
        # peer channel update \
        # - c ${channel} \
        # - o ${orderer_url} \
        # - f ${CHANNEL_ARTIFACTS} /${tx} \
        # > & log.txt
        return
