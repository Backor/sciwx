import wx
from sciwx.canvas.widget import CanvasFrame
from sciwx.canvas.event import Tool, DefaultTool

class Pencil(Tool):
    title = 'Pencil'
        
    def __init__(self):
        self.status = False
        self.oldp = (0,0)
        
    def mouse_down(self, ips, x, y, btn, **key):
        self.status = True
        self.oldp = (y, x)
    
    def mouse_up(self, ips, x, y, btn, **key):
        self.status = False
    
    def mouse_move(self, ips, x, y, btn, **key):
        if not self.status:return
        se = self.oldp + (y,x)
        rs,cs = line(*[int(i) for i in se])
        rs.clip(0, ips.shape[1], out=rs)
        cs.clip(0, ips.shape[0], out=cs)
        ips.img[rs,cs] = (255, 0, 0)
        self.oldp = (y, x)
        key['canvas'].update()
        
    def mouse_wheel(self, ips, x, y, d, **key):pass

if __name__=='__main__':
    from skimage.data import camera, astronaut
    from skimage.io import imread

    app = wx.App()
    cf = CanvasFrame(None, autofit=False)
    cf.set_imgs([astronaut(), 255-astronaut()])
    cf.set_cn((0,1,2))
    bar = cf.add_toolbar()
    bar.add_tool(DefaultTool, 'M')
    bar.add_tool(Pencil, 'P')
    cf.Show()
    app.MainLoop()
