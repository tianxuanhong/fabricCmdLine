import os

class BasicEnv:
    binary_versions_v2 = ['v2.2.1', 'v2.2.2']
    binary_versions_v1 = ['v1.4.1', 'v1.4.2']

    def __init__(self, version, **kwargs):
        self.version = version
        # 根据用户输入设置环境变量，建议主要设置CORE_PEER_LOCALMSPID、CORE_PEER_TLS_CERT_FILE、
        # CORE_PEER_TLS_KEY_FILE、CORE_PEER_TLS_ROOTCERT_FILE、CORE_PEER_MSPCONFIGPATH等

        # 1. 环境变量
        for k, v in kwargs.items():
            os.environ[k] = v
        #   os.system("export {}={}".format(k, v))  export或者setenv之后，无法通过getenv获取到. 具体哪种方式适合peer，待测试

        # 2. 设置变量存放各个节点及orderer证书证书等信息。
        # self.orderer_msp = []
        # self.orderer_admin_msp = []
        # self.orderer_tls_ca = []
        # self.orderer_tls_rootcert = []
        #
        # self.org_admin_msp = []
        # self.org_peer_msp = []
        # self.org_peer_tls_rootcert = []
        # self.org_admin_tls_client_key = []
        # self.org_admin_tls_client_cert = []
        # self.org_admin_tls_ca_cert = []

        # 3. 考虑各节点发起交易，各发起者只拥有自己证书
        # for k, v in kwargs.items():
        #     if k == "FABRIC_LOGGING_SPEC":
        #         self.FABRIC_LOGGING_SPEC = v
        #     elif k == "CORE_PEER_TLS_ENABLED":
        #         self.CORE_PEER_TLS_ENABLED = v
        #     elif k == "ORDERER_CA":
        #         self.ORDERER_CA = v
        #     elif k == "CORE_PEER_ID":
        #         self.CORE_PEER_ID = v
        #     elif k == "CORE_PEER_ADDRESS":
        #         self.CORE_PEER_ADDRESS = v
        #     elif k == "CORE_PEER_LOCALMSPID":
        #         self.CORE_PEER_LOCALMSPID = v
        #     elif k == "CORE_PEER_TLS_CERT_FILE":
        #         self.CORE_PEER_TLS_CERT_FILE = v
        #     elif k == "CORE_PEER_TLS_KEY_FILE":
        #         self.CORE_PEER_TLS_KEY_FILE = v
        #     elif k == "CORE_PEER_TLS_ROOTCERT_FILE":
        #         self.CORE_PEER_TLS_ROOTCERT_FILE = v
        #     elif k == "CORE_PEER_MSPCONFIGPATH":
        #         self.CORE_PEER_MSPCONFIGPATH = v

