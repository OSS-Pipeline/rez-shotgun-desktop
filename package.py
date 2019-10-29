name = "shotgun_desktop"

version = "current"

authors = [
    "Autodesk"
]

description = \
    """
    This simple, visual interface makes it easy for artists to access productivity tools and for developers to deploy
    them. A native app framework, it sits on artists’ desktops and provides quick access to key pipeline tools
    directly from the tray.
    """

requires = [
    "cmake-3+",
    "python-2.7+<3"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "shotgun_desktop-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
