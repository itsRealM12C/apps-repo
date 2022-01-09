import requests

title = 'Moonlight'
iconUri = 'https://github.com/mariotaku/moonlight-tv/raw/main/deploy/webos/icon_large.png'
detailIconUri = 'https://github.com/mariotaku/moonlight-tv/raw/main/res/moonlight_320.png'
manifestUrl = 'https://github.com/mariotaku/moonlight-tv/releases/latest/download/com.limelight.webos.manifest.json'
category = 'games'
description = '''
Moonlight TV is a community version of [Moonlight GameStream Client](https://moonlight-stream.org/), made for large
screens.

## Features

* High performance streaming for webOS
* UI optimized for large screen and remote controller
* Supports up to 4 controllers
* Easy to port to other OSes (Now runs on macOS, Arch, Debian, Raspbian and Windows)

## Screenshots

![Launcher](https://user-images.githubusercontent.com/830358/141690137-529d3b94-b56a-4f24-a3c5-00a56eb30952.png)

![Settings](https://user-images.githubusercontent.com/830358/147389849-6907f614-dbd4-4c24-987e-1a214a9680d0.png)

![In-game Overlay](https://user-images.githubusercontent.com/830358/141690146-27ee2564-0cc8-43ef-a5b0-54b8487dda1e.png)
_Screenshot performed on TV has lower picture quality. Actual picture quality is better._

## [Documentations](https://github.com/mariotaku/moonlight-tv/wiki)
'''


def load():
    content = {
        'title': title,
        'iconUri': iconUri,
        'detailIconUri': detailIconUri,
        'category': category,
        'description': description,
        'manifestUrl': manifestUrl
    }
    with requests.get('https://api.github.com/repos/mariotaku/moonlight-tv/releases', {'per_page': 1}) as resp:
        latest = resp.json()[0]
        if latest['prerelease']:
            for asset in filter(lambda x: x['name'] == 'com.limelight.webos.manifest.json', latest['assets']):
                content['manifestUrlBeta'] = asset['browser_download_url']
                break
    return content
