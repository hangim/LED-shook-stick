#include <AT89X52.h>

/*** 声明助手函数 ***/
void flash(int n);
void delay(unsigned int t);
void show_col(unsigned short i);

int main(){
	while(1){
		flash(1);
		delay(1000);
	}
	return 0;
}

/*** 闪烁函数 ***/
/* 参数 n : 闪烁次数 */
void flash(int n){
	int i;
	for (i = 0; i < n; i++){
		show_col(0x0000); // 灯全亮
		delay(500);
		show_col(0xFFFF); // 灯全灭
		delay(500);
	}
}

/*** 延迟函数 ***/
void delay(unsigned int t){
	unsigned int i, j;
	for (i = 0; i < t; i++)
		for (j = 0; j < 121; j++) // 此处准确数据待测
			; // Do nothing
}

/*** 列显示函数 ***/
void show_col(unsigned short col){
	P0 = col / 256; // 改变 P0 的8个Led灯
	P2 = col % 256; // 改变 P2 的8个Led灯
}
