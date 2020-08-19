import Quartz

class Mouse():
    down = [Quartz.kCGEventLeftMouseDown, Quartz.kCGEventRightMouseDown, Quartz.kCGEventOtherMouseDown]
    up = [Quartz.kCGEventLeftMouseUp, Quartz.kCGEventRightMouseUp, Quartz.kCGEventOtherMouseUp]
    [LEFT, RIGHT, OTHER] = [0, 1, 2]

    def click_pos(self, x, y, button=LEFT):
        self.move(x, y)
        self.click(button)

    def to_relative(self, x, y):
        curr_pos = Quartz.CGEventGetLocation( Quartz.CGEventCreate(None) )
        x += curr_pos.x;
        y += curr_pos.y;


mouse = Mouse()
mouse.to_relative(200, 200)