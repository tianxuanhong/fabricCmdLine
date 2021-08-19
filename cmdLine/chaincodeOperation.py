import os
from cmdLine.basicParameters import BasicEnv


class ChainCode(BasicEnv):
    """调用cmd执行chaincode install等相关操作"""

    def __init__(self, version, **kwargs):
        super(ChainCode, self).__init__(version, **kwargs)

    def lifecycle_install(self):
        if self.version in BasicEnv.binary_versions_v2:
            os.system("./../{}/peer ")
        # peer lifecycle chaincode package ${cc_name}.tar.gz \
        #  - -path ${cc_path} \
        #  - -lang golang \
        #  - -label ${label}

        # peer lifecycle chaincode install \
        # - -peerAddresses ${peer_url} \
        # - -tlsRootCertFiles ${peer_tls_root_cert} \
        # {cc_name}.tar.gz | tee > & log.txt
        return

    def lifecycle_query(self):
        # peer lifecycle chaincode queryinstalled \
        # - -peerAddresses ${peer_url} \
        # - -tlsRootCertFiles ${peer_tls_root_cert} \
        # - -output
        # json \
        # - -connTimeout "3s"
        return

    def lifecycle_get_installed(self):
        # peer lifecycle chaincode getinstalledpackage \
        # - -peerAddresses ${peer_url} \
        # - -tlsRootCertFiles ${peer_tls_root_cert} \
        # - -package - id ${package_id} \
        # - -output - directory. / \
        # --output json \
        # - -connTimeout "3s"
        return

    def lifecycle_approve_for_my_org(self):
        # peer lifecycle chaincode approveformyorg \
        # - -peerAddresses ${peer_url} \
        # - -channelID ${channel} \
        # - -name ${cc_name} \
        # - -version ${version} \
        # - -init - required \
        # - -package - id ${package_id} \
        # - -sequence 1 \
        # - -signature - policy "${policy}" \
        # - -waitForEvent \
        # - -orderer ${orderer_url} > & log.txt
        return

    def lifecycle_query_approved(self):
        # peer lifecycle chaincode queryapproved \
        # - -peerAddresses ${peer_url} \
        # - -tlsRootCertFiles ${peer_tls_root_cert} \
        # - -channelID ${channel} \
        # - -name ${cc_name} \
        # - -output json
        return

    def lifecycle_check_commit_readiness(self):
        # peer lifecycle chaincode checkcommitreadiness \
        # - -peerAddresses ${peer_url} \
        # - -tlsRootCertFiles ${peer_tls_root_cert} \
        # - -channelID ${channel} \
        # - -name ${cc_name} \
        # - -output json \
        # - -version ${version} \
        # - -sequence ${sequence}
        return

    def lifecycle_commit(self):
        # peer lifecycle chaincode commit \
        # - o ${orderer_url} \
        # - -channelID ${channel} \
        # - -name ${cc_name} \
        # - -version ${version} \
        # - -init - required \
        # - -sequence 1 \
        # - -peerAddresses ${ORG1_PEER0_URL} \
        # - -tlsRootCertFiles ${ORG1_PEER0_TLS_ROOTCERT} \
        # - -peerAddresses ${ORG2_PEER0_URL} \
        # - -tlsRootCertFiles ${ORG2_PEER0_TLS_ROOTCERT} \
        # - -waitForEvent \
        # - -collections - config "${collection_config}" \
        # - -signature - policy "${policy}"
        return

    def lifecycle_query_committed(self):
        # peer lifecycle chaincode querycommitted \
        # - -peerAddresses ${peer_url} \
        # - -tlsRootCertFiles ${peer_tls_root_cert} \
        # - -channelID ${channel} \
        # - -output json \
        # - -name ${cc_name}
        return

    def instantiate(self):
        # peer chaincode instantiate \
        # - o ${orderer_url} \
        # - C ${channel} \
        # - n ${cc_name} \
        # - v ${version} \
        # - c ${args} \
        # - P "${policy}" \
        # - -collections - config "${collection_config}" \
        # > & log.txt
        return

    def invoke(self):
        # peer chaincode invoke \
        # - o ${orderer_url} \
        # - -channelID ${channel} \
        # - -name ${cc_name} \
        # - -peerAddresses ${peer_url} \
        # - -tlsRootCertFiles ${peer_org_tlsca} \
        # - c ${args} \
        # > & log.txt
        return

    def query(self):
        # peer chaincode query \
        # - C "${channel}" \
        # - n "${cc_name}" \
        # - -peerAddresses ${peer_url} \
        # - -tlsRootCertFiles ${peer_org_tlsca} \
        # - c "${args}" \
        # > & log.txt
        return

    def list(self):
        # peer chaincode list \
        # - -installed > log.txt &
        return

    def upgrade(self):
        # peer chaincode upgrade \
        # - o ${orderer_url} \
        # - C ${channel} \
        # - n ${cc_name} \
        # - v ${version} \
        # - c ${args} \
        # - P "${policy}" \
        # - -collections - config "${collection_config}" \
        # > & log.txt
        return
