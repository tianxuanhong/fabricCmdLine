import os
from cmdLine.basicParameters import BasicEnv


class PeerChannel(BasicEnv):
    """调用cmd执行channel create、join等相关操作"""

    def __init__(self, version, **kwargs):
        super(PeerChannel, self).__init__(version, **kwargs)

    def channel_create(self, channel, orderer_url, channel_tx, orderer_tls_rootcert, time_out="90"):
        if os.getenv("CORE_PEER_TLS_ENABLED") == "false" or os.getenv("CORE_PEER_TLS_ENABLED") == "":
            if self.version in BasicEnv.binary_versions_v2:
                os.system("./../bin/{}/peer channel create -c {} -o {} -f {} --timeout {}".
                          format(self.version, channel, orderer_url, channel_tx, time_out))
        else:
            if self.version in BasicEnv.binary_versions_v2:
                os.system("./../bin/{}/peer channel create -c {} -o {} -f {} --timeout {} --tls --cafile {}".
                          format(self.version, channel, orderer_url, channel_tx,
                                 time_out, orderer_tls_rootcert))

        # peer channel create \
        # - c ${channel} \
        # - o ${orderer_url} \
        # - f ${CHANNEL_ARTIFACTS} /${channel_tx} \
        # - -timeout "${TIMEOUT}s"
        return

    def channel_join(self):
        # peer channel join \
        # - b ${channel}.block \
        # > & log.txt
        return

    def channel_list(self):
        # peer channel list > & log.txt
        return

    def channel_getinfo(self):
        # peer channel getinfo -c ${channel} >&log.txt
        return

    def channel_fetch(self):
        # peer channel fetch $num ${block_file} \
        # - o ${orderer_url} \
        # - c ${channel} \
        # > & log.txt
        return

    def channel_signconfigtx(self):
        # peer channel signconfigtx - f ${CHANNEL_ARTIFACTS} /${tx} > & log.txt
        return

    def channel_update(self):
        # peer channel update \
        # - c ${channel} \
        # - o ${orderer_url} \
        # - f ${CHANNEL_ARTIFACTS} /${tx} \
        # > & log.txt
        return
