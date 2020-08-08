import numpy as np
class MiGong:
    def __init__(self):
        """
        map表示地图
        """
        self.map=np.zeros((8,7))

    def build_map(self):
        for i in range(7):
            self.map[0][i]=1
            self.map[7][i]=1
        for j in range(1,7):
            self.map[j][0]=1
            self.map[j][6]=1
        self.map[3][1]=1
        self.map[3][2]=1
        return self.map

    # 使用递归回溯给小球找路
    def setway(self,map,i,j):
        """
        i，j表示开始位置的坐标
        i=6,j=5 表示终点位置坐标，若能走到该位置则说明能走通，返回True
        约定：当map[i][j]为0表示该点没有走过，为1表示为墙，为2表示通路可以走，为3表示该点已经走过，但是走不通！
        在走迷宫时，需要确定一个策略（方法）即：下(down)->右(right)->上(up)->左(left),如果该点走不通，再回溯
        :param i:
        :param j:
        :return:bool
        """
        if map[6][5]==2:
            return True
        else:
            if map[i][j]==0:
                map[i][j]=2 # 假定该点可走通
                if self.setway(map,i+1,j):  # 向下走
                    return True
                elif self.setway(map,i,j+1):  # 向右走
                    return True
                elif self.setway(map,i-1,j):  # 向上走
                    return True
                elif self.setway(map,i,j-1):  # 向左走
                    return True
                else:
                    map[i][j]=3  # 说明该路走不通
                    return False
            else:  # 如果map[i][j]!=0,则可能为1，2，3
                return False

if __name__ == '__main__':
    migong = MiGong()
    map=migong.build_map()
    print(migong.setway(map,1,1))
    print(migong.map)