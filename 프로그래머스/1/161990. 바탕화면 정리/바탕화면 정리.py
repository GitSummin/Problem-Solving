def solution(wallpaper):
    
    lux = len(wallpaper)
    luy = len(wallpaper[0])
    rdx = 0
    rdy = 0
    
    for i, row in enumerate(wallpaper):
        for j, cell in enumerate(wallpaper[i]):
            if cell == "#":
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i+1)
                rdy = max(rdy, j+1)
    
    return [lux, luy, rdx, rdy]