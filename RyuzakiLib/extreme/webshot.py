import requests

class WebShotUrl:
    def __init__(
        self,
        url=None,
        width: int=1280,
        height: int=720,
        scale: int=1,
        delay: int=0,
        full=None,
        screenshot_full: bool=None
    ):
        self.url = url
        self.width = width
        self.height = height
        self.scale = scale
        self.delay = delay
        self.full = full
        self.screenshot_full = screenshot_full

    def send_screenshot(self):
        api_url = None
        data = {
            "url": self.url,
            "width": self.width,
            "height": self.height,
            "scale": self.scale,
            "delay": self.delay,
            "full": self.full
        }
        if self.screenshot_full:
            x = requests.post(f"{api_url}", json=data)
            if x.status_code != 200:
                return "Error request:"
            try:
                y = x.json()
            except Exception:
                pass
