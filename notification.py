import time
from winotify import Notification, audio

def notify(title, msg):
    toast = Notification(
        app_id="Monitoring.System",
        title=title,
        msg=msg,
        duration="short"
    )
    toast.set_audio(audio.Default, loop=False)
    toast.show()
    time.sleep(1)
