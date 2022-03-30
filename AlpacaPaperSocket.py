from difflib import restore


class AlpacaPaperSocket(restore):
    def __init__(self):
        super().__init__(
            key_id='CKBH0M5ZGOLJTM5AI1TB',
            secret_key='X2vTZ8jr10Fnr0TMpd8Br7Ay4C86FxrN1kwPitJU',
            base_url='https://paper-api.alpaca.markets'
        )