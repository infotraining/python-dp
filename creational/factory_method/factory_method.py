from dataclasses import dataclass


@dataclass
class MP3Track:
    title: str

    def play(self):
        print(f"Playing {self.title}")


class AMusicService:
    def __init__(self, user_name, user_secret):
        self._user_name = user_name
        self._user_secret = user_secret
        print(f'Creating connection to AMusicService for user: {user_name}...')

    def load_track(self, title):
        return MP3Track(title)


class BMusicService:
    def __init__(self, user_name, user_secret, timeout):
        self._user_name = user_name
        self._user_secret = user_secret
        print(
            f'Creating connection to BMusicService for user: {user_name} with timeout {timeout}s...')

    def load_track(self, title):
        return MP3Track(title)


class MusicClient:
    def __init__(self, music_service_factory):
        self._music_service_factory = music_service_factory

    def play_track(self, title):
        srv = self._music_service_factory()
        track = srv.load_track(title)
        track.play()


def main():
    config_A = {'user_name': 'superuser', 'user_secret': 'SECRET_KEY_C'}
    config_B = {'user_name': 'superuser',
                'user_secret': 'SECRET_KEY_B', 'timeout': 30}
    client = MusicClient(lambda:  AMusicService(**config_A))
    client.play_track("Kill'em All")

    client = MusicClient(lambda : BMusicService(**config_B))
    client.play_track("Schism")


if __name__ == "__main__":
    main()
