#!/usr/bin/python2
#coding=utf-8
import RPi.GPIO as GPIO
import time 

def init():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(21, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(29, GPIO.OUT)
        GPIO.setup(31, GPIO.OUT)
        GPIO.setup(40, GPIO.OUT)
        
def reset():
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
def left_forward():
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
def right_forward():
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
def left_back():
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.HIGH) 
def right_back():
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
def left_stop():
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
def right_stop():
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        
def turret_right():
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)
def turret_left():
        GPIO.output(16, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)
def turret_stop():
        GPIO.output(16, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
def up():
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(22, GPIO.LOW)
def down():
        GPIO.output(21, GPIO.LOW)
        GPIO.output(22, GPIO.HIGH)
def gun_lock():
        GPIO.output(21, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
def re_load():
        GPIO.output(29, GPIO.LOW)
        GPIO.output(31, GPIO.HIGH)
def gun_stop():
        GPIO.output(29, GPIO.LOW)
        GPIO.output(31, GPIO.LOW)

def aim_on():
        GPIO.output(40, GPIO.HIGH)

def aim_off():
        GPIO.output(40, GPIO.LOW)
        
def f():
        re_load()
        time.sleep(1)
        gun_stop()
def shoot():
        re_load()
        time.sleep(5)
        gun_stop()

def g():
        gun_lock()
        up()
        time.sleep(0.8)
        gun_lock()
def gun_up():
        gun_lock()
        up()
        time.sleep(0.7)
        gun_lock()
def gun_down():
        gun_lock()
        down()
        time.sleep(0.7)
        gun_lock()        
def turret_left_turn():
        turret_stop()
        turret_left() 
        time.sleep(0.2)
        turret_stop()
def turret_right_turn():
        turret_stop()
        turret_right() 
        time.sleep(0.2)
        turret_stop()
def forward():
        reset()
        left_forward()
        right_forward()

def back():
        reset()
        left_back()
        right_back()

def front_left():
        reset()
        right_forward()
        left_stop()  
def left_turn():
        reset()
        right_forward()
        left_back()
        time.sleep(0.2)
        reset()
def front_right():
        reset()
        left_forward()
        right_stop()
def right_turn():
        reset()
        left_forward()
        right_back()
        time.sleep(0.2)
        reset()
def stop():
        reset()
def back_left():
        reset()
        left_stop()
        right_back()
def back_right():
        reset()
        left_back()
        right_stop()

if __name__ == "__main__":
        init()
        reset()
        forward()
        time.sleep(0.2)
        back()
        time.sleep(0.2)
        left_turn()
        time.sleep(0.2)
        right_turn()
        time.sleep(0.2)
        left_turn()
        time.sleep(0.2)
        right_turn()
        stop()
        '''
        GPIO.cleanup() 
        '''


