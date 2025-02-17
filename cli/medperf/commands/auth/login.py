import medperf.config as config
from medperf.utils import set_credentials, set_current_user


class Login:
    @staticmethod
    def run(username: str = None, password: str = None):
        """Login to the medperf server. Must be done only once.
        """
        comms = config.comms
        ui = config.ui
        user = username if username else ui.prompt("username: ")
        pwd = password if password else ui.hidden_prompt("password: ")
        comms.login(user, pwd)
        token = comms.token
        current_user = comms.get_current_user()

        set_credentials(token)
        set_current_user(current_user)
