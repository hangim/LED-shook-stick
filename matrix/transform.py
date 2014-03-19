# -*- coding: utf-8 -*-
img = [0,0,0,0,1820,1820,1820,24,24,24,24,24,0,0,0,0,264,904,1028,1308,1820,1820,1820,1308,1028,904,264,0,0,0,0,744,1380,1020,416,48,16,8,16,48,416,1020,1380,744,0,0,0,0,1820,1820,1152,1152,1152,1152,1152,1152,1152,768,768,0,0,0,0,0]

def transform(img = []):
        rsu = []
        for it in img:
                high = 0
                tmp = it / 256 # 取 P0 数据
                # 逆序P0
                for i in range(8):
                        high = high * 2 + tmp % 2
                        tmp /= 2
                # 合并P0 P2 并取反
                rsu.append("0x%04X"%(~(high * 256 + it % 256) & 0xFFFF))
        print len(rsu)
        print 
        print 'unsigned short code img[Total][Resolution] = ' + \
                str(rsu).replace('\'', '').replace('[','{').replace(']','}') \
                + ';'

if __name__ == '__main__':
        transform(img)
