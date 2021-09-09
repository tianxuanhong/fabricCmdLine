import os
import json
import subprocess
from cmdLine.basicParameters import BasicEnv


class ChainCode(BasicEnv):
    """调用cmd执行chaincode install等相关操作"""

    def __init__(self, version, **kwargs):
        super(ChainCode, self).__init__(version, **kwargs)

    def lifecycle_package(self, cc_name, cc_version, cc_path, language):
        """
            package the chaincode to a tar.gz file.
        :param cc_name: chaincode name
        :param cc_path: where the chaincode is
        :param language: Chain code development language, default: golang
        :return 0 means success.
        """
        if self.version in BasicEnv.binary_versions_v2:
            label = cc_name+"_"+cc_version
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
            # res = os.system("./../bin/{}/bin/peer lifecycle chaincode queryinstalled --output json --connTimeout
            # {} > queryInstalled.txt"
            #                .format(self.version, timeout), "r")
            # # with open('./queryInstalled.txt', 'r', encoding='utf-8') as f:
            # #     content = f.read()
            # # os.system("rm ./queryInstalled.txt")
            # body = res.read()
            # installed_chaincodes = json.loads(body)

            res = subprocess.Popen("./../bin/{}/bin/peer lifecycle chaincode queryinstalled --output json "
                                   "--connTimeout {}".format(self.version, timeout), shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout, stderr = res.communicate()
            return_code = res.returncode
            if return_code == 0:
                content = str(stdout, encoding="utf-8")
                installed_chaincodes = json.loads(content)
                return return_code, installed_chaincodes
            else:
                stderr = str(stderr, encoding="utf-8")
                return return_code, stderr

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

    def lifecycle_approve_for_my_org(self, orderer_url, orderer_tls_rootcert, channel_name, cc_name,
                                     chaincode_version, policy):
        res, installed = self.lifecycle_query_installed("3s")
        cc_label = cc_name+"_"+chaincode_version
        package_id = ""
        for each in installed['installed_chaincodes']:
            if each['label'] == cc_label:
                package_id = each['package_id']
                break
        if package_id == "":
            return 1, "not exist the chaincode, please check chaincode_name and chaincode_version"

        if os.getenv("CORE_PEER_TLS_ENABLED") == "false" or os.getenv("CORE_PEER_TLS_ENABLED") is None:
            if self.version in BasicEnv.binary_versions_v2:
                res = os.system("./../bin/{}/bin/peer lifecycle chaincode approveformyorg -o {} "
                                " --channelID {} --name {} --version {} --init-required --package-id {} --sequence 1"
                                " --signature-policy {} > ./approve.txt"
                                .format(self.version, orderer_url, channel_name, cc_name,
                                        chaincode_version, package_id, policy))
        else:
            if self.version in BasicEnv.binary_versions_v2:
                res = subprocess.Popen("./../bin/{}/bin/peer lifecycle chaincode approveformyorg -o {} --tls "
                                       "--cafile {} --channelID {} --name {} --version {} --init-required --package-id "
                                       "{} --sequence 1 --signature-policy {}"
                                       .format(self.version, orderer_url, orderer_tls_rootcert, channel_name,
                                               cc_name, chaincode_version, package_id, policy), shell=True,
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = res.communicate()
                return_code = res.returncode

                if return_code == 0:
                    content = str(stdout, encoding="utf-8")
                else:
                    stderr = str(stderr, encoding="utf-8")
                    return return_code, stderr
        return return_code, content

    def lifecycle_query_approved(self, channel_name, cc_name):
        if self.version in BasicEnv.binary_versions_v2:

            res = subprocess.Popen("./../bin/{}/bin/peer lifecycle chaincode queryapproved --output json --channelID {}"
                                   " --name {}".format(self.version, channel_name, cc_name),
                                   shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = res.communicate()
            return_code = res.returncode
            if return_code == 0:
                content = str(stdout, encoding="utf-8")
                chaincodes_info = json.loads(content)
                return return_code, chaincodes_info
            else:
                stderr = str(stderr, encoding="utf-8")
                return return_code, stderr
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
