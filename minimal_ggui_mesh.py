import taichi as ti

ti.init()

num_trianles=2
indices = ti.field(int, num_trianles*3)
vertices = ti.Vector.field(3, float, num_trianles*3)

@ti.kernel
def step():
    pass

@ti.kernel
def set_indices():
    indices[0] = 0
    indices[1] = 1
    indices[2] = 2

    indices[3] = 3
    indices[4] = 4
    indices[5] = 5

@ti.kernel
def set_vertices():
    vertices[0] = ti.Vector([ 0, 0, 0])
    vertices[1] = ti.Vector([ 0, -0.5, 0])
    vertices[2] = ti.Vector([ 0.5, -0.5, 0])

    vertices[3] = ti.Vector([ 0.5, 0, 0])
    vertices[4] = ti.Vector([ 0.5, -0.5, 0])
    vertices[5] = ti.Vector([ 1, -0.5, 0])

window = ti.ui.Window("draw_mesh", (800, 800), vsync=True)
canvas = window.get_canvas()
scene = ti.ui.Scene()
camera = ti.ui.make_camera()
canvas.set_background_color((1,1,1))

set_indices()
set_vertices()

while window.running:
    for _ in range(1):
        step()

    camera.position(0.5, -0.5, 2)
    camera.lookat(0.5, -0.5, 0)
    camera.track_user_inputs(window, movement_speed=0.03, hold_key=ti.ui.RMB)
    scene.set_camera(camera)
    scene.point_light(pos=(0.5, 1, 2), color=(1, 1, 1))

    scene.mesh(vertices, indices=indices)

    canvas.scene(scene)
    window.show()