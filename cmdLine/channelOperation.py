import os
from cmdLine.basicParameters import BasicEnv


class PeerChannel(BasicEnv):
    TimeOut = "90"

    """调用cmd执行channel create、join等相关操作"""

    def __init__(self, channel, orderer_url, channel_tx, version, time_out="90", **kwargs):
        super(PeerChannel, self).__init__(version, **kwargs)
        self.channel = channel
        self.orderer_ul = orderer_url
        self.channel_tx = channel_tx
        self.time_out = time_out

    def channel_create(self):
        if self.version in BasicEnv.binary_versions:
            os.system("./../bin/{}/peer channel create -c {} -o {} -f {} --timeout {}".
                      format(self.version, self.channel, self.orderer_ul, self.channel_tx, self.time_out))
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
