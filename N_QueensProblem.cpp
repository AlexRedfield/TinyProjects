#include<iostream>
using namespace std;

int pos[10], board = 8, cnt = 0;
void print() {
	for (int i = 0; i < board; i++) {
		for (int j = 0; j < board; ++j) {
			if (j == pos[i]) cout << "1 ";
			else cout << "0 ";
		}
		cout << endl;
	}
	cout << endl;
}
bool is_ok(int row) {
	for (int i = 0; i<row; i++) {
		//分别是pos[row]正上方，左斜上方，右斜上方
		if (pos[row] == pos[i] || pos[row] == pos[i] - row + i || pos[row] == pos[i] + row - i) 
			return false;
	}
	return true;
}

void putOne(int row) {
	if (row==board) {
		print();
		++cnt;
		return;
	}
	for (int i = 0; i < board; i++) {
		pos[row]= i;
		if (is_ok(row)) {	//当前行正确就进入下一行
			putOne(row+1);
		}
	}
}

int main() {
	putOne(0);
	cout << cnt << endl;	//总数
	system("pause");
	return 0;
}
