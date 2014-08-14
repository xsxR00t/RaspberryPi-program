#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Katsuya Yamaguchi, Hirokazu Yokoyama

import smbus

class I2CConnect :
    bus = smbus.SMBus(1)

    ''' @param address 通信先のスレーブアドレス '''
    def __init__( self, address ) :
        # Target address
        self.address = address
        self.isValidate()

    ''' スレーブにデータを送信します．
    @param *data 送信するデータ
    '''
    def write_data( self, *data ) :
        self.bus.write_i2c_block_data( self.address, 0x00, list(data[0:]) )
        print "Write!"

    ''' スレーブからデータを受信します．(スレーブに送信リクエストを送ります．)
    @param byteCount 受信するデータ量(bytes), default=1
    '''
    def read_data( self, byteCount = 1 ) :
        return self.bus.read_i2c_block_data(self.address, 0x00, byteCount)

    def is_validate(self):
        if self.address <= 0 or self.address > 255:
            raise IndexError("I2C address must be an integer from 1 to 255. The specified number %s is invalid" % self.address)

    def test( self ) :
        print "get"


# テスト
if __name__ == '__main__':
    '''
        指定したアドレスのスレーブにランダムに生成した値を3つ送信する．
        続いて，スレーブから3バイトのデータを読み出す．
    '''

    # スレーブと送受信するデータ量(byte)
    SEND_DATA_LENGTH = 4

    print "Lets start the test of I2CConnect!\n"
    address = input("Enter number of slave address 1 - 255 > ")
    if not address:
        print "You must enter integer from 1 to 255."

    import random, time
    i2c = I2CConnect(address)
    send_data_list = [random.randint(1, 255) for i in range(SEND_DATA_LENGTH)]
    print "Send to %d, %s" % (i2c.address, send_data_list)
    i2c.write_date(*send_data_list)
    time.sleep(0.1)
    read_data_list = i2c.read_data(4)
    print "Read data from slave %d, %s" % (i2c.address, read_data_list)
