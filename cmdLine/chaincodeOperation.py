import os
import json
import subprocess
from cmdLine.basicParameters import BasicEnv


class ChainCode(BasicEnv):
    """调用cmd执行chaincode install等相关操作"""

    def __init__(self, version, **kwargs):
        super(ChainCode, self).__init__(version, **kwargs)

    def lifecycle_package(self, cc_name, cc_path, language, label):
        """
            package the chaincode to a tar.gz file.
        :param cc_name: chaincode name
        :param cc_path: where the chaincode is
        :param language: Chain code development language, default: golang
        :param label: Label of the generated chain code package
        :return 0 means success.
        """
        if self.version in BasicEnv.binary_versions_v2:
            res = os.system("./../bin/{}/bin/peer lifecycle chaincode package {}.tar.gz --path {} --lang {} --label {}"
                            .format(self.version, cc_name, cc_path, language, label))
            res = res >> 8
            print("res", res)
        return

    def lifecycle_install(self, cc_targz):
        """

             :param cc_targz: the path of chaincode
             :return: 0 means success.
             """
        if self.version in BasicEnv.binary_versions_v2:
            res = os.system("./../bin/{}/bin/peer lifecycle chaincode install {}".format(self.version, cc_targz))

        # peer lifecycle chaincode install \
        # - -peerAddresses ${peer_url} \
        # - -tlsRootCertFiles ${peer_tls_root_cert} \
        # {cc_name}.tar.gz | tee > & log.txt
        res = res >> 8
        return res

    def lifecycle_query_installed(self, timeout):
        """
            get the chaincode info installed in peer.
        :param timeout:
        :return: res 0 means success
                 installed_chaincodes: the json format of installed_chaincodes info
        """
        if self.version in BasicEnv.binary_versions_v2:
            # res = os.popen("./../bin/{}/bin/peer lifecycle chaincode queryinstalled --output json --connTimeout {}"
            #                .format(self.version, timeout), "r")
            # # with open('./queryInstalled.txt', 'r', encoding='utf-8') as f:
            # #     content = f.read()
            # # os.system("rm ./queryInstalled.txt")
            # body = res.read()
            # installed_chaincodes = json.loads(body)

            res = subprocess.Popen("./../bin/{}/bin/peer lifecycle chaincode queryinstalled --output json --connTimeout {}".format(self.version, timeout), stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout,stderr=res.communicate()
            print(stdout)
            print(stderr)
        # peer lifecycle chaincode queryinstalled \
        # - -peerAddresses ${peer_url} \
        # - -tlsRootCertFiles ${peer_tls_root_cert} \
        # - -output
        # json \
        # - -connTimeout "3s"
            res = res >> 8
        return res, installed_chaincodes

    def lifecycle_get_installed_package(self, timeout):
        """
            lifecycle_query_installed will return a list installed in peer.
            then execute cmd to get all chaincode with tar.gz format installed in peer.
        :param timeout:
        :return: res_return: 0 means success get all chaincode in peers.
        """
        if self.version in BasicEnv.binary_versions_v2:
            res, installed = self.lifecycle_query_installed("3s")
            res_return = 0
            if res == 0:
                for item in installed['installed_chaincodes']:
                    # packages_id.append(item['package_id'])
                    res_get = os.system("./../bin/{}/bin/peer lifecycle chaincode getinstalledpackage --package-id {} "
                              "--output-directory ./ --connTimeout {}".format(self.version, item['package_id'], timeout))
                    res_get = res_get >> 8
                    res_return = res_return or res_get

            else:
                print("package_id get failed.")
                return 1, {}

            # res = os.system("./../bin/{}/bin/peer lifecycle chaincode getinstalledpackage --package-id {} "
            #                 "--output-directory ./ --connTimeout {}".format(self.version, packages_id[0], timeout))
            # res = res >> 8
        return res_return

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
