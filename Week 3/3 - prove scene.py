import tkinter as tk
import math
import random

def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
# Call the drawing functions
    draw_ground(canvas, scene_left, scene_top, scene_right, scene_bottom)
    draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom )
    draw_grass(canvas, scene_left, scene_right)
    draw_sun(canvas, 450, 75)
    draw_clouds(canvas, 400, 120, scene_right, scene_bottom)
    draw_clouds(canvas, 50, 200, scene_right, scene_bottom)
    #draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)
    



#functions that draw the picture

#Draw grass that repeats all the way the screen
def draw_grass(canvas, left, right):
    for i in range(left, right):
        x_1 = left + (i * 5)
        x_2 = x_1 + 4
        x_3 = x_2 + 2
        y_1 = 375
        y_2 = 365
        y_3 = 375
        canvas.create_polygon(x_1, y_1, x_2, y_2, x_3, y_3, fill='#59B308', width=False)

#create a random colored minecraft style dirt ground
def draw_ground(canvas, left = 0, top = 375, right = 800, bottom = 500):
    for y in range(top, bottom):
        top_side = top + (y * 25)
        for x in range(left, right):
            random_number = random.randint(1,4)
            if random_number == 1:
                 color = '#8F4616'
            elif random_number == 2:
                color = '#873B0A'
            elif random_number == 3:
                color = '#612905'
            elif random_number == 4:
                    color = '#653618'
            left_side = left + (x * 25)
            right_side = left_side + 25
            bottom_side = top_side + 25
            canvas.create_rectangle(left_side, top_side, right_side, bottom_side, fill=color, width = False)

#draw a blue sky
def draw_sky(canvas, left, top, right, bottom):
    canvas.create_rectangle(left, top, right, 375, fill='#00D4FF')

#Draw a set of three clouds with one of them being a different color
def draw_clouds(canvas, cloud_left, cloud_top, cloud_right, cloud_bottom):
    cloud_width = 150
    cloud_height = 75
    cloud_right = cloud_left + cloud_width
    cloud_bottom = cloud_top + cloud_height
    canvas.create_oval(cloud_left, cloud_top, cloud_right, cloud_bottom, fill='#62848A', width=False)
    canvas.create_oval(cloud_left - 80, cloud_top + 30, cloud_right, cloud_bottom + 20, fill='#7B9FA7', width=False)
    canvas.create_oval(cloud_left + 45, cloud_top + 15, cloud_right + 100, cloud_bottom, fill='#62848A', width=False)


    
#draws a sun with rays around the sun (the sun is also green because I can)
def draw_sun(canvas, sun_left, sun_top):
    sun_width = 100
    sun_height = 100
    ray_length = 100
    ray_width = 3
    ray_count = 10

    sun_right = sun_left + sun_width
    sun_bottom = sun_top + sun_height
    sun_center_x = sun_left + (sun_width / 2)
    sun_center_y = sun_top + (sun_height / 2)

    canvas.create_oval(sun_left, sun_top, sun_right, sun_bottom, fill='#00FF0C', width=False)

    for i in range(ray_count):
        angle = (2 * math.pi / ray_count) * i
        ray_x = sun_center_x + math.cos(angle) * ray_length
        ray_y = sun_center_y + math.sin(angle) * ray_length
        canvas.create_line(sun_center_x, sun_center_y, ray_x, ray_y, width=ray_width, fill='#00FF0C')

def draw_grid(canvas, left, top, right, bottom, grid_spacing):
    text_horizontal_margin = 20
    text_vertical_margin = 10

    #draw horizontal lines
    for i in range(top, bottom, grid_spacing):
        canvas.create_line(left, i, right, i)
        canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text=f'{i}')
    #draw vertical lines
    for i in range(left, right, grid_spacing):
        canvas.create_line(i, top, i, bottom)
        canvas.create_text(i, top + text_vertical_margin, text=f'{i}')


# Call the main function so that
# this program will start executing.
main()