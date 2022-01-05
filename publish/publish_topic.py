from Classes.Publish import Publish
from Classes.Settings import Settings


if __name__ == '__main__':

    Publish(Settings().get_broker(),
            Settings().get_port(),
            Settings().get_topic(),
            Settings().get_client_id(),
            Settings().get_username(),
            Settings().get_password())\
        .run()
