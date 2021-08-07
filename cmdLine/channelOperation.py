import os
import basicParameters

class PeerChannel(BasicEnv):

    """调用cmd执行channel create、join等相关操作"""

    def __init__(self, org_msp_id, org_admin_msp, channel, orderer_url):
        self.org_msp_id = org_msp_id
        self.org_admin_msp = org_admin_msp
        self.channel = channel
        self.orderer_ul = orderer_url

    def channel_create(self):
        os.system("peer channel create -c {} -o {} ".format(self.channel, self.orderer_ul))
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
