!/bin/sh
xrandr --dpi 192
xrdb -merge ~/.Xresources

export QT_AUTO_SCREEN_SCALE_FACTOR=1


exec qtile start

