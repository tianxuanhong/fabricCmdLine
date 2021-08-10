import os


class BasicEnv:
    binary_versions = ['v2.2.1', 'v2.2.2']

    def __init__(self, version, **kwargs):
        self.version = version
        # os.environ[]
        # 根据用户输入设置环境变量，建议主要设置CORE_PEER_LOCALMSPID、CORE_PEER_TLS_CERT_FILE、
        # CORE_PEER_TLS_KEY_FILE、CORE_PEER_TLS_ROOTCERT_FILE、CORE_PEER_MSPCONFIGPATH等
        for k, v in kwargs.items():
            os.system("export {}={}".format(k, v))
