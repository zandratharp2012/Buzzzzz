# AVR
#***********
# Modular Make - top level makefile
PROJPATH := $(PWD)
PROJNAME := $(notdir $(PROJPATH))
MK := mk

# configure these settings for your Ardino setup
AVRPROJ := blink
MCU 	:= atmega328p
FREQ    := 16000000L
PGMR    := arduino

# uncomment and modify the right port
PORT	:= /dev/ttyACM0
#PORT	:=	/dev/cu.usbmodem1421
#PORT	:== COM6

include $(MK)/os-detect.mk

.PHONY:	gui
gui:	$(TARGET)
	./$(TARGET) -g -d
