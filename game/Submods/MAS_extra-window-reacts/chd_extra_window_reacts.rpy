#Extra window reacts by confiscatedharddrive for Monika After Story.

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="chd_mas_wrs_gaming",
            category=['Steam|GOG Galaxy|RetroArch|Lutris'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label chd_mas_wrs_gaming:
    $ wrs_success = display_notif(
        m_name,
        [
            "Gonna play a game, [player]?",
            "I'd love to play with you sometime.",
            "What are you going to play today?",
            "Can I be your player 2?~"
        ],
        'Window Reactions'
    )
    #extra insurance if it doesn't work the first time
    if not wrs_success:
        $ mas_unlockFailedWRS('chd_mas_wrs_gaming')
    return


init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="chd_mas_wrs_streamingmore",
            category=['HBO Max|Peacock|Disney+|Hulu|Paramount Plus|: Prime Video|Stan'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label chd_mas_wrs_streamingmore:
    $ wrs_success = display_notif(
        m_name,
        [
            "I'd love to watch a romance movie with you [player]!",
            "What are we watching today, [player]?",
            "What are you going to watch [player]?"
        ],
        'Window Reactions'
    )
    #extra insurance if it doesn't work the first time
    if not wrs_success:
        $ mas_unlockFailedWRS('chd_mas_wrs_streamingmore')
    return


init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="chd_mas_wrs_music",
            category=['Spotify|Bandcamp|YouTube Music|- Quod Libet'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label chd_mas_wrs_music:
    $ wrs_success = display_notif(
        m_name,
        [
            "What album are you going to listen to, [player]?",
            "Going to play some music for me?~",
            "I wonder what genre you'll pick this time.",
            "Are you going to listen to some music, [player]?"
        ],
        'Window Reactions'
    )
    #extra insurance if it doesn't work the first time
    if not wrs_success:
        $ mas_unlockFailedWRS('chd_mas_wrs_music')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="chd_mas_wrs_npr",
            category=["NPR"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label chd_mas_wrs_npr:
    $ wrs_success = display_notif(
        m_name,
        [
            "Public radio is a great way to get informed!",
            "For NPR news, I'm Monika.",
            "Listening to some public radio, [player]?",
            "NPR's got some interesting podcasts!"
        ],
        'Window Reactions'
    )
    #extra insurance if it doesn't work the first time
    if not wrs_success:
        $ mas_unlockFailedWRS('chd_mas_wrs_npr')
    return


init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="chd_mas_wrs_email",
            category=['Gmail|- Outlook|- Mozilla Thunderbird'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label chd_mas_wrs_email:
    $ wrs_success = display_notif(
        m_name,
        [
            "Catching up on emails, [player]?",
            "Got any new emails, [player]?",
            "Be sure to keep things organized~",
        ],
        'Window Reactions'
    )
    #extra insurance if it doesn't work the first time
    if not wrs_success:
        $ mas_unlockFailedWRS('chd_mas_wrs_email')
    return


init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="chd_mas_wrs_videoplayer",
            category=['VLC media player|- mpv'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label chd_mas_wrs_videoplayer:
    $ wrs_success = display_notif(
        m_name,
        [
            "Gonna watch a DVD or Blu-Ray?",
            "What are you going to watch, [player]?",
            "I wonder what we're watching today~",
        ],
        'Window Reactions'
    )
    #extra insurance if it doesn't work the first time
    if not wrs_success:
        $ mas_unlockFailedWRS('chd_mas_wrs_videoplayer')
    return
