import mouse as ms

def hack(x_amount=6, y_amount=4, duration=0.05, x_resolution=1920, y_resolution=1080):
    #x_amount - отвечает за количество столбцов + 1
    #y_amount - отвечает за количество строк + 1
    #duration - отвечает за длительность перемещения курсора от одной позиции до другой
    #x_resolution - отвечает за твоё разрешение монитора/размера_окна_игры по оси x
    #x_resolution - отвечает за твоё разрешение монитора/размера_окна_игры по оси y
    #Если всё на*бнулось, то ctrl+c в cmd | ctrl+2 в pycharm

    start_x = x_resolution * 0.08
    start_y = y_resolution * 0.05
    end_x = x_resolution - 100 - start_x
    end_y = y_resolution - start_y

    step_x = end_x // x_amount
    step_y = end_y // y_amount

    positions=[]

    for i in range(x_amount+1):
        for j in range(y_amount+1):
            positions.append((start_x + step_x*i, start_y + step_y*j))

    while True:
        for i in positions:
            ms.move(i[0], i[1], duration=duration)

if __name__ == "__main__":
    hack(3,3, 0.1)

#ctrl + f2