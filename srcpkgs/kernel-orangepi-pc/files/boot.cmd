# Sample boot script that is executed by u-boot, set your kernel params here
setenv bootargs console=ttyS0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=f2fs rw rootwait panic=3 quiet loglevel=0
# Change to board-rd.itb if you use ramdisk
load mmc 0:1 0x44000000 board.itb
bootm 0x44000000
